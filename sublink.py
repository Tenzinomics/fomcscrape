import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os



folder_path = "C:/Users/tchozin/Desktop/FOMC Scrape/text data"

def fomcspeechpage(primarylink,secondary_link):

    response = requests.get(primarylink+secondary_link)
    response.raise_for_status()  # Check for request errors

    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.find('div', id='article')

    texts = div.find_all('p')  # Adjust as needed

    emptyarr = []

    for text in texts:
            
            text_inside = text.get_text(strip=True)
            emptyarr.append(text_inside)


    date_str = texts[0].get_text(strip=True)

    # Parse the original date string into a datetime object
    date_obj = datetime.strptime(date_str, '%B %d, %Y')

    # Convert the datetime object to the desired format
    formatted_date = date_obj.strftime('%d-%m-%Y')

    #print(formatted_date)  # Output: 31-07-2024

    single_string = '\n'.join(emptyarr)

    # Define the file name and the full file path
    file_name = formatted_date+'.txt'
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(single_string)

