import requests
from bs4 import BeautifulSoup

# Define the URL of the web page to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Make a GET request to the URL and retrieve the HTML content
response = requests.get(URL)
empire_web_page = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(empire_web_page, "html.parser")

# Find all movie elements on the web page using the specified HTML tags and classes
movies = soup.find_all(name="div", class_="article-title-description__text")
movies_list = []

# Iterate through each movie element and extract the movie title
for movie in movies:
    title = movie.find(name="h3", class_="title").getText()
    movies_list.append(title)

# Write the extracted movie titles to a text file in reverse order
# The [::-1] is used to reverse the order of items in the movies_list before writing to the file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies_list[::-1]:
        file.write(item + "\n")
