# Movie-Recommendation
MYSQL, NLP, Streamlit, webAPI
This Movie Recommendation System suggests movies based on the user’s input, provides in-depth details of selected movies, and saves user interactions to a MySQL database for further personalization.

### 1. Movie Recommendation Based on User Input
When a user searches for a movie (e.g., "Spider-Man 3"), the system recommends similar movies using NLP-based similarity matching.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/4c963d09-14c5-4965-a0b2-9ed8bf72ba86" />

###2. Detailed Movie Description
Users can click on "Describe a Movie" to view a detailed overview including:

Ratings

Budget

Revenue

Other metadata
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/9752599b-3f46-4bd5-8977-befb16856ad5" />

### 3. Cast Information & Expandable Details
The system also allows users to explore the cast of the movie. By using the "Show More" dropdown, users can access extended information about specific cast members.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/17254afd-f96a-4f7b-a2d9-14f14a686c43" />

###4. MySQL Database Integration
All user activity, including search history and recommended movies, is stored in a MySQL database.

Each action is linked to a unique user ID (default ID: 1).

The system can be scaled to support multiple users, allowing for personalized recommendations based on user behavior.
<img width="1432" alt="image" src="https://github.com/user-attachments/assets/167c1527-89eb-4dcd-bb26-f63ae7a7764b" />

