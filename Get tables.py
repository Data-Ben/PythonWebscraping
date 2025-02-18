import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to scrape all tables and extract data
def scrape_all_tables(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    all_data = []
    
    for table in tables:
        rows = table.find_all('tr')
        
        # Iterate through table rows (skip header row)
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) > 5:
                bond_code = cells[0].get_text(strip=True)
                issue_date = cells[1].get_text(strip=True)
                maturity_date = cells[2].get_text(strip=True)
                issuance_size = cells[3].get_text(strip=True)
                isin = cells[4].get_text(strip=True)
                document_url = cells[5].find('a', href=True)['href'] if cells[5].find('a', href=True) else None
                
                all_data.append({
                    'Document Name': f"{bond_code}_Pricing_Supplement.pdf",
                    'Bond Code': bond_code,
                    'Issue Date': issue_date,
                    'Maturity Date': maturity_date,
                    'Issuance Size': issuance_size,
                    'ISIN': isin,
                    'Document URL': document_url
                })
    return all_data

# Main function to create a CSV file with the extracted data
def main():
    website_url = '' #add your website here
    scraped_data = scrape_all_tables(website_url)
    
    if scraped_data:
        df = pd.DataFrame(scraped_data)
        df.to_csv('all_tables_documents3.csv', index=False)
        print("CSV file 'all_tables_documents.csv' has been created.")
    else:
        print("No data to save.")

if __name__ == '__main__':
    main()
