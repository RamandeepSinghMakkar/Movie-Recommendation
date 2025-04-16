# Movie-Recommendation

This project implements a movie recommendation system that not only suggests movies based on user searches but also provides in-depth movie details and cast information. User interactions, including search queries and recommendations, are logged into a MySQL database, allowing the system to be trained and improved over time. By default, the system uses a single user ID (1), but it is structured for future scalability.

### Technologies Used:

MySQL – Database for storing user search data and recommendations

NLP – Natural Language Processing to analyze movie similarity and user preferences

Streamlit – Fast and interactive web application framework

WebAPI – External APIs to fetch movie details and metadata

# Features

### 1. Movie Recommendation Based on User Input
On searching for a movie (e.g., "Spider-Man 3"), similar movies are suggested based on NLP similarity matching.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/4c963d09-14c5-4965-a0b2-9ed8bf72ba86" />

### 2. Detailed Movie Description
Click "Describe a Movie" to reveal additional details including ratings, budget, revenue, and more.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/9752599b-3f46-4bd5-8977-befb16856ad5" />

### 3. Cast Information & Expandable Details
The system also allows users to explore the cast of the movie. View the complete cast list with an expandable section ("Show More") to access detailed information about each cast member.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/17254afd-f96a-4f7b-a2d9-14f14a686c43" />

### 4. MySQL Database Integration
All user activity, including search history and recommended movies, is stored in a MySQL database.
Each action is linked to a unique user ID (default ID: 1).

<img width="1432" alt="image" src="https://github.com/user-attachments/assets/69a126f4-d520-4627-929e-07d3ca11090d" />

