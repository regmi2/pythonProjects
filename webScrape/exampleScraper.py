# AUTHOR: Pallav Regmi
# DATE: JAN 2023

import requests
import csv
from bs4 import BeautifulSoup

# go to website using the requests package, url is changed for showing purposes
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup - package to parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with the id 'business'
business_divs = soup.find_all('div', {'id': 'business'})

# Extract the links from the onclick attribute of the span tag - link to business 
links = []
for div in business_divs:
    for span in div.find_all('span'):
        link = span['onclick']
        link = link.replace("location='","")
        links.append(link)

    # Extract the text from the p tag - name of the business
    p_text = div.find('p').text
    links.append(p_text)

# Write the links to a .csv file
with open('links.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Links', 'Text'])
    for link,text in zip(links[::2],links[1::2]):
        writer.writerow([link,text])

print("Links and Text have been saved to links.csv")
