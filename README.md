# Book Recommendation API

## Overview

This project involves creating a book recommendation system using data from [Project Gutenberg](https://www.gutenberg.org/). The application allows users to query a database of books and receive recommendations based on specific search terms. The system is accessible via an API that returns results in JSON format.

The project holds significant importance in terms of access to and discovery of classic literature. Project Gutenberg is one of the largest digital libraries of public domain books, offering access to a vast range of historical literary works that may be less known or less accessible on other platforms.

## Installation

To run this project, follow these steps:

1. Clone this repository:
    ```bash
    https://github.com/cribeirop/ProjectGutenberg_Book_Recommendation
    ```
2. Create a virtual environment in the root of the project and activate it:
    - Creating the `venv`:
    ```bash
    python3 -m venv venv
    ```
    - Activating the virtual environment:
    ```bash
    source venv/bin/activate
    ```
3. Install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Configure Database

For the creation of the database, web scraping was performed to catalog all the books available in the Project Gutenberg collection, i.e., over 70,000 books. The data was obtained through the initials of the books, in alphabetical order, starting with the [letter A](https://www.gutenberg.org/browse/titles/a). Each page corresponding to a letter has all the cataloged books with the respective initial. Thus, information on each of the books for each letter of the alphabet is tracked.

- To set up the database and verify its construction, run the `scraper.py` file:
    ```bash
    python3 scraper.py
    ```

## Testing the Application

1. After completing the installation steps, test the application by running the `main.py` file:
    ```bash
    python3 main.py
    ```

2. Access the URL http://10.103.0.28:34567, which is the root of the book recommendation API.

## Test Examples

1. Test that produces 10 results: http://10.103.0.28:34567/query?query=love

This test uses the word "love", which is a very common word, especially in romantic literature.

2. Test that produces fewer than 10 results: http://10.103.0.28:34567/query?query=kill

This test, using a less common word, filters books through the word "kill" which are not as common given the primary type of literature the site usually refers to, as well as reflecting a taste that may be very particular.

3. Test that produces something non-obvious: http://10.103.0.28:34567/query?query=full%20moon

In this last test, a compound word "full moon" was used, which is commonly used but not well-cataloged in the site’s books. Results predominantly showed the word "moon" only. This is due to the recommender's lack of handling multiple words, especially compound words.

# Using Docker Container

To use the application in a container, follow these steps:

1. Build the program:
    ```bash
    docker build -t gutenberg_project .
    ```
2. Run the application:
    ```bash
    docker run -d -p 9876:8080 gutenberg_project
    ```
3. Test the application through logs: copy the container ID (result from the previous command) and paste it into the following command:
    ```bash
    docker logs <container-ID>
    ```