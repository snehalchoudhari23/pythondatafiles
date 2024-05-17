import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_company_data(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
        
        data = []
        for result in search_results:
            data.append(result.text)
        
        return data
    else:
        print("Failed to retrieve data from the URL:", url)
        return []

def main():
    query = "IT companies in Bangalore"
    search_results = scrape_company_data(query)
    
    # Example: creating a DataFrame with fetched data
    company_data = pd.DataFrame(columns=["Company Name", "Location", "Address", "Employee Count"])
    for result in search_results:
        # Here you'll need to parse the result and extract the relevant information
        # Then append it to the DataFrame
        
        # For demonstration purposes, we'll just print the result
        print(result)

if __name__ == "__main__":
    main()
