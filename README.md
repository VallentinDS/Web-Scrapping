# Features Scrapper- Web-Scraping with JavaScript
Programming Language: JS
A script meant to be running in the console for getting the information from a mat-table object from a Google Marketing Platform page.
Open the console -> Sources -> New snippet -> Copy-Paste the script in there.
OR
Be on the page with the GA Integrations and run it from the console. They console will return 'undefined' but the data is in the clipboad. Go to this website (https://www.convertcsv.com/json-to-csv.htm) and copy-paste the data there. Open the .csv file in Sheets/Excel after this.

# Building requests in Python

Programming language: Python
Tools: Postman (the app, not the Chrome extension)
Page link: https://marketingplatform.google.com/home/integrations?authuser=0

Access the page link above and enter the Chrome Console -> Network (Fetch/XHR) -> copy cURL of the POST request that you get when you access the page with the Analytics 360 integrations.

Take the cURL from each of the POST methods and insert them into Postman. 
  - You can import the cURL into Postman. It should automatically transform it. If not, remove all the " ' " and " \ " that you see at the start and/or end of the values.
  - Minimize the number of headers to the minimum, in order to get the data needed (anything extra won't be needed)
  - By importing the cURL this should automatically detect the Headers and the Body.
    - NOTE: In the Body tab, make sure that the option raw is selected, and the method is JSON

Same process for the other POST request that comes up when you open sub-integration.

With the code displayed, the process should be similar in case it will be throwing errors when trying to pull other integrations.

IMPORTANT:
The headers that are selected in the variables `entity_summaries_url` and `list_links_url` could be working only for a period of time. Headers, such as cookies, can change in time which would require going again through the same process. Google gives a set of credentials through these cookies.

