# cardiffappdevelopers
Software Engineer (Python) - Take-home Task

## Service start

1 . add "data_handler" as source root

2. install requirements.txt i.e pip install -r requirements.txt

3. run application.py

4. open link http://127.0.0.1:8080/ui/ and required body and check data saving endpoint

5. used first end point
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
6. get endpoint
### swagger
http://127.0.0.1:8080/ui/#/default/get_data

### curl
```bash
curl -X 'GET' \
  'http://127.0.0.1:8080/data?from_date=2022-10-01&to_date=2023-10-01' \
  -H 'accept: */*'
```
