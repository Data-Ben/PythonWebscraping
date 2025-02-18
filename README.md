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

Check out the script at [Webscrape](WebScrape2.py)

**Script for table with ISINs**

For the excel table with ISINs the documents were in HTML tables on the website, so I ran a script that returned a data frame with the document URLs and other available data points. I then used this data frame to run the same [Script](WebScrape2.py) as above.

It was lucky that an ISIN is a unique identifier so there was no need to deduplicate or perform other data cleaning, in a scenario where you are not given a unique identifier, you'd need the business to define clear parameters that allow you to find and identify the correct data. As usual its ultimately the business problem that you are trying to fix that is going to determine the code you'll use vs the other way round. 

enough waffling! here's what the script does: 
1.	Fetch the webpage.
2.	Extract relevant bond details.
3.	Save the details in a structured CSV file.

Check out the script at [Get tables](Get Tables.py)

As per usual when building solutions there is lots of ways to accomplish it and I just used the first 1 that ran without any errors so please do suggest any other ways to do this I'd be super grateful for any comments and suggestions on how to improve code or on the methodology as a whole.
