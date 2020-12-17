from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "http://localhost:3000"

    def on_start(self):
        pass

    @task
    def index(self):
        self.client.get("/api/articles")
