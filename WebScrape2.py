import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to download file
def download_file(url, destination_folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        file_name = url.split("/")[-1]  # Extract the file name from the URL
        
        # Save the file in the specified destination folder
        file_path = os.path.join(destination_folder, file_name)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return (file_name, True, '')  # Successful download
    except requests.exceptions.RequestException as e:
        return (url.split("/")[-1], False, str(e))  # Return error message if failed

# Function to load the locally saved Excel file
def load_excel_file(df):
    try:
        # Load the Excel file using pandas
        df = pd.read_excel('Absafile.xlsx')
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Main function to orchestrate downloading
def main():
    # Path to the locally saved Excel file
    excel_path = r'' #add your file path
    
    # Folder to save downloaded documents
    destination_folder = './downloads'   # Replace with your desired folder path
    os.makedirs(destination_folder, exist_ok=True)
    
    # Load the Excel file
    df = load_excel_file(excel_path)
    if df is None:
        print("Failed to load the Excel file.")
        return
    
    # Assuming URLs are in the first column, you can modify this if needed
    doc_links = df.iloc[:, 0].dropna().tolist()
    
    # List to store the results of each download
    results = []
    
    # Download each document
    for doc_url in doc_links:
        file_name, success, error_message = download_file(doc_url, destination_folder)
        results.append({
            'Document Name': file_name,
            'Download Successful': success,
            'Error Message': error_message
        })
    
    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results)
    
    # Save the results to a CSV file
    results_df.to_csv(os.path.join(destination_folder, 'download_results.csv'), index=False)
    print("Download results saved to 'download_results.csv'")

if __name__ == '__main__':
    main()
