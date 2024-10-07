import requests
from bs4 import BeautifulSoup
import sublink

# URL of the FOMC statements page
url = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'
primarylink = "https://www.federalreserve.gov"

response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')
#search_text = "Federal Reserve issues FOMC statement"

div = soup.find('div', id='article')

statements = div.find_all('a', href=True)  # Adjust as needed


# Example to print all statement links
for link in statements[0:len(statements)-6]:
    
    link_text = link.get_text(strip=True)
    
    #print(link_text, link['href']) 
        
    secondary_link = link['href']

    response = requests.get(primarylink+secondary_link)
    response.raise_for_status()  # Check for request errors


    soup = BeautifulSoup(response.content, 'html.parser')


    div = soup.find('div', id='content')


    statements2 = div.find_all('a', href=True)  # Adjust as needed


    for link in statements2:
        
        
        link_text = link.get_text(strip=True)
        #print(link_text)

        search_text = "Federal Reserve issues FOMC statement"
       
        if search_text in link_text:
            href = link['href']
            print(f'Found link with text "{search_text}": {href}')
            found = True
            
            sublink.fomcspeechpage(primarylink,href)
    
   
for link in statements[len(statements)-7:len(statements)]:
    
    link_text = link.get_text(strip=True)
    
    #print(link_text, link['href']) 
        
    secondary_link = link['href']

    response = requests.get(primarylink+secondary_link)
    response.raise_for_status()  # Check for request errors


    soup = BeautifulSoup(response.content, 'html.parser')


    div = soup.find('div', id='content')


    statements2 = div.find_all('a', href=True)  # Adjust as needed


    for link in statements2:
        
        
        link_text = link.get_text(strip=True)
        #print(link_text)


        search_text2 = "FOMC statement"

        if search_text2 in link_text:
            href = link['href']
            print(f'Found link with text "{search_text2}": {href}')
            found = True

            sublink.fomcspeechpage(primarylink, href)
