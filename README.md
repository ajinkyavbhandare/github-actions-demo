# github-actions-demo

- github actions demo execrise 1.1 from practical mlops


- command to run fastapi
```
   # Ensure you are in your virtual environment
   uvicorn main:app --workers 4 --host 127.0.0.1 --port 8000
```
- command to run locust for local stress testing
```
   locust -f locustfile.py --host=http://127.0.0.1:8000

```
