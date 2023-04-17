import time

from locust import User, task, constant, between, constant_pacing


class MyuUser(User):

    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(5)
        print("Constant Pacing Demo")