### Task description

#### Make a report on requests for an arbitrary period in days (from 1 day or more)
The data needs to be collected using the Google Sheets API from the document https://docs.google.com/spreadsheets/d/1Ycg7zTxds9DZnDvTrFcyNNKuTUxg6Yy6WF0a8Wc02WQ
#### Report format:
Dimensions:
- request attraction channel (d_utm_source)
- club (d_club)
- manager (d_manager)

Metrics:
- number of applications
- number of junk orders (no client has been created based on the order)
- number of new orders (there were no orders and purchases from this client before)
- number of buyers (those who bought within a week after the order)
- number of new buyers (those who bought within a week after the application, and had not bought earlier)
- income from new customers’ purchases
#### The final report needs to be replaced to your Google Sheets document:
Write Python code to process data  
Extract data from Google Sheets and load it into your document via Google Sheets API  
For the final report, use the pivot table Google Sheets  

