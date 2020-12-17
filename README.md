# datadog-django-loadtest

The realworld application with datadog integration is from: https://github.com/DataDog/trace-examples/tree/master/python/django/django-realworld

I did change datadog site to use .eu and I added a line in the django-readworld dockerfile to run migrations.

## Setup

```
cd django-readlworld-example-app
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
export DD_API_KEY=...
docker-compose up --build
```

## Run load test with datadog tracing.
1. Install k6 (https://k6.io/ or use whatever load testing helper you want)
2. Start the application
    ```
    docker-compose up --build
    ```

3. Then go to k6loadtest folder and run (monitor CPU usage also)
    ```
    cd k6loadtest
    k6 run --vus 10 --duration 30s script.js  
    ```

## Run load test (using locust) with datadog tracing.
1. Make sure you have python 3.6 or above before pip installing locust (https://locust.io/) below:
    ```
    cd locust
    pip install -r requirements.txt
    ```
2. run "locust" command from command line
3. Observe load test from the UI when browsing to http://0.0.0.0:8089


## Run load test without datadog tracing.
1. Go to django-realworld-example-app and disable datadog by removing "ddtrace-run" from dockerfile
    ```
    CMD python manage.py runserver 0.0.0.0:3000
    ```
2. Run the load test again (monitor cpu usage)

There is a clear performance cost to running the datadog agent, both in terms of transaction times and cpu usage.