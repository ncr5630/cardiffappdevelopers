# cardiffappdevelopers
Software Engineer (Python) - Take-home Task

## Service start

#### 1.Add "data_handler" as the source root.

#### 2.Install the requirements from requirements.txt using the command: pip install -r requirements.txt.

#### 3.Run application.py.

#### 4.Open the link http://127.0.0.1:8080/ui/ and provide the required body to check the data saving endpoint.

#### 5.Use the first endpoint.
### swagger
http://127.0.0.1:8080/ui/#/default/create_records
### curl
```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/data' \
  -H 'accept: */*' \
  -H 'Content-Type: text/plain' \
  -d '1649941817 Voltage 1.39'

  ```
6.Get endpoint.
### swagger
http://127.0.0.1:8080/ui/#/default/get_data

### curl
```bash
curl -X 'GET' \
  'http://127.0.0.1:8080/data?from_date=2022-10-01&to_date=2023-10-01' \
  -H 'accept: */*'
```
# Additional Considerations
## 1. How can we test the code to be confident in the implementation?
### Ans.
#### We can use unit testing, code review with seniors, proper error handling, and so on.

## 2. How can we make sure this code is easy to maintain for future developers?
### Ans.
#### i .need to provide clear documentation 
#### ii. break down the code into modular components
#### iii. simple codebase without over engineering

## 3.Our API needs to be high-performance — how can we measure the performance of our API?
### Ans.
#### i.monitor response time 
#### ii.concurrency testing
#### iii.check database performance

## 4.How could we optimise this code if the API receives many more POST requests than GET requests? What about if the API receives many more GET requests than POST requests?
### Ans.
#### i.increase backend resources
#### ii.can used message queue system (i.e AWS-SQS, AZURE - SERVICE BUS)
#### iii. optimize database operations
#### iv. used aws , azure or GCP popper optimized cloud envs
