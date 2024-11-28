import streamlit as st
from processing import preprocess
from processing.display import Main

# Setting the wide mode as default
st.set_page_config(layout="wide")

displayed = []

# Initialize session state variables
st.session_state.setdefault('movie_number', 0)
st.session_state.setdefault('selected_movie_name', "")
st.session_state.setdefault('user_menu', "")


def calculate_metrics(recommended_items, user_relevant_items, K=22):  # Increased K
    relevant_at_k = [item for item in recommended_items[:K] if item in user_relevant_items]
    precision_k = len(relevant_at_k) / K
    recall_k = len(relevant_at_k) / len(user_relevant_items) if user_relevant_items else 0
    hit_rate = 1 if len(relevant_at_k) > 0 else 0

    st.write(f"relevant_at_k: {relevant_at_k}")
    st.write(f"precision_k: {precision_k}, recall_k: {recall_k}, hit_rate: {hit_rate}")

    return precision_k, recall_k, hit_rate


def display_metrics(recommended_items, user_relevant_items):
    """
    Display the calculated metrics in the Streamlit app.
    """
    precision, recall, hit_rate = calculate_metrics(recommended_items, user_relevant_items)

    st.write("### Performance Metrics")
    st.write(f"**Precision:** {precision:.2f}")
    st.write(f"**Recall:** {recall:.2f}")
    st.write(f"**Hit Rate:** {hit_rate}")


def recommend_display(new_df):
    """
    Display recommendations for a selected movie.
    """
    st.title('Movie Recommender System')
    st.text('Recommend will show similar movies')
    selected_movie_name = st.selectbox(
        'Select a Movie...', new_df['title'].values
    )

    rec_button = st.button('Recommend')
    if rec_button:
        if selected_movie_name != st.session_state.selected_movie_name:
            st.session_state.selected_movie_name = selected_movie_name
        # st.session_state.selected_movie_name = selected_movie_name
        recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tags.pkl', "are")
        recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_genres.pkl', "on the basis of genres are")
        recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tprduction_comp.pkl', "from the same production company are")
        recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_keywords.pkl', "on the basis of keywords are")
        recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tcast.pkl', "on the basis of cast are")

        # Increase K to expand the number of recommendations
        recommended_movies, _ = preprocess.recommend(new_df, selected_movie_name, r'Files/similarity_tags_tags.pkl')
        display_metrics(recommended_movies, recommended_movies)


def recommendation_tags(new_df, selected_movie_name, pickle_file_path, tag_str):
    """
    Display recommendations with posters based on a specific tag.
    """
    movies, posters = preprocess.recommend(new_df, selected_movie_name, pickle_file_path)
    st.subheader(f'Best Recommendations {tag_str}...')

    rec_movies = []
    rec_posters = []
    cnt = 0
    # Adding only 10 unique recommendations
    for i, j in enumerate(movies):
        if cnt == 10:  # Limit to 10 recommendations
            break
        if j not in displayed:
            rec_movies.append(j)
            rec_posters.append(posters[i])
            displayed.append(j)
            cnt += 1

    # Display movie titles and posters in columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if idx < len(rec_movies):
            with col:
                st.text(rec_movies[idx])
                st.image(rec_posters[idx])


def display_movie_details():
    """
    Display detailed information about a selected movie.
    """
    if not st.session_state.selected_movie_name:
        st.warning("First select a movie!")
        return  # Exit the function if no movie is selected

    selected_movie_name = st.session_state.selected_movie_name
    info = preprocess.get_details(selected_movie_name)

    with st.container():
        image_col, text_col = st.columns((1, 2))
        with image_col:
            st.text('\n')
            st.image(info[0])

        with text_col:
            st.text('\n')
            st.text('\n')
            st.title(selected_movie_name)
            st.text('\n')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text("Rating")
                st.write(info[8])
            with col2:
                st.text("No. of ratings")
                st.write(info[9])
            with col3:
                st.text("Runtime")
                st.write(info[6])

            st.text('\n')
            st.write("Overview")
            st.write(info[3], wrapText=False)
            st.text('\n')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text("Release Date")
                st.text(info[4])
            with col2:
                st.text("Budget")
                st.text(info[1])
            with col3:
                st.text("Revenue")
                st.text(info[5])

            st.text('\n')
            col1, col2, col3 = st.columns(3)
            with col1:
                genres = " . ".join(info[2])
                st.text("Genres")
                st.write(genres)

            with col2:
                available_in = " . ".join(info[13])
                st.text("Available in")
                st.write(available_in)
            with col3:
                st.text("Directed by")
                st.text(info[12][0])
            st.text('\n')

    # Displaying information about the cast
    st.header('Cast')
    cnt = 0
    urls = []
    bio = []
    for i in info[14]:
        if cnt == 5:
            break
        url, biography = preprocess.fetch_person_details(i)
        urls.append(url)
        bio.append(biography)
        cnt += 1

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if idx < len(urls):
            with col:
                st.image(urls[idx])
                # Use an expander to show the biography
                with st.expander("Show More"):
                    st.write(bio[idx])


def paging_movies(movies):
    """
    Paginate and display the list of all movies.
    """
    max_pages = movies.shape[0] // 10
    max_pages = int(max_pages) - 1

    col1, col2, col3 = st.columns([1, 9, 1])

    with col1:
        st.text("Previous page")
        prev_btn = st.button("Prev")
        if prev_btn:
            if st.session_state['movie_number'] >= 10:
                st.session_state['movie_number'] -= 10

    with col2:
        new_page_number = st.slider("Jump to page number", 0, max_pages, st.session_state['movie_number'] // 10)
        st.session_state['movie_number'] = new_page_number * 10

    with col3:
        st.text("Next page")
        next_btn = st.button("Next")
        if next_btn:
            if st.session_state['movie_number'] + 10 < len(movies):
                st.session_state['movie_number'] += 10

    display_all_movies(movies, st.session_state['movie_number'])


def display_all_movies(movies, start):
    """
    Display a subset of movies starting from a given index.
    """
    i = start
    cols = [st.columns(5) for _ in range(2)]
    for row in cols:
        for col in row:
            if i < movies.shape[0]:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                col.image(link, caption=movies['title'][i])
                i += 1


def initial_options(new_df, movies):
    """
    Display the initial menu for user options.
    """
    st.session_state.user_menu = st.radio(
        "What are you looking for? 👀",
        options=['Recommend me a similar movie', 'Describe me a movie', 'Check all Movies'],
        index=0,
        horizontal=True
    )

    if st.session_state.user_menu == 'Recommend me a similar movie':
        recommend_display(new_df)

    elif st.session_state.user_menu == 'Describe me a movie':
        display_movie_details()

    elif st.session_state.user_menu == 'Check all Movies':
        paging_movies(movies)


def main():
    with Main() as bot:
        bot.main_()
        new_df, movies, movies2 = bot.getter()

    initial_options(new_df, movies)


if __name__ == '__main__':
    main()
