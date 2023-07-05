# cardiffappdevelopers
Software Engineer (Python) - Take-home Task
# cardiffappdevelopers
Software Engineer (Python) - Take-home Task

## Service start

1.Add "data_handler" as the source root.

2.Install the requirements from requirements.txt using the command: pip install -r requirements.txt.

3.Run application.py.

4.Open the link http://127.0.0.1:8080/ui/ and provide the required body to check the data saving endpoint.

5.Use the first endpoint.
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
