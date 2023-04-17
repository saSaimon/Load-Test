from locust import HttpUser, task, user, constant


class MyLoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/")
