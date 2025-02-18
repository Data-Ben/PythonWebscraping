# PythonWebscraping
I recently had to web scrape a lot of pdfs that were publicly available on the internet and I thought this would be helpful to share. Especially in the legal industry (who were my stakeholder for this project) this is a common request, so I thought I'd share. 
I relied on 2 excel files (surprise our old friend excel is still a key dependency in 2025) with the following data: 
1.	A table with document URLs 
2.	A table with ISINs ( these were finance documents)


**Script for table with URLS**
My script does the following: 

1.	Loads an Excel file containing URLs.
2.	Extracts the URLs and downloads each file, saving them to a specified folder (./downloads).
3.	Logs the download results (success/failure and error messages) in a CSV file (download_results.csv).
4.	Uses requests for downloading and pandas for handling the Excel and CSV files.
The script ensures error handling for failed downloads and missing files.

Check out the script at [My file](WebScrape2.py)

