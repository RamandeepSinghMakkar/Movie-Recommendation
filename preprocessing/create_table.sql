-- Create the recommendations table
CREATE TABLE recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for each record
    user_id INT NOT NULL,                  -- User identifier (you can link this to a users table)
    movie_name VARCHAR(255) NOT NULL,       -- Name of the movie the user selected
    user_query TEXT,                        -- The query/request made by the user
    recommended_movies TEXT,                -- A list of recommended movies (you can store this as a comma-separated string)
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Time when the query was made
);

-- You can also add an index to optimize queries based on user_id
CREATE INDEX idx_user_id ON recommendations (user_id);
