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
- количество новых заявок (не было заявок и покупок от этого клиента раньше)
- количество покупателей (кто купил в течение недели после заявки)
- количество новых покупателей (кто купил в течение недели после заявки, и не покупал раньше)
- доход от покупок новых покупателей
#### Итоговый отчёт нужно вывести в свой документ Google Sheets:
Для обработки данных написать код на Python  
Данные выгружать из Google Sheets и загружать в свой документ через Google Sheets API  
Для итогового отчёта использовать pivot table Google Sheets

