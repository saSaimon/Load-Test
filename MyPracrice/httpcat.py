import random

from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")

    # @task
    # def get_random_status(self):
    #     status_codes = [100, 101, 102, 103, 104, 105]
    #     random_url = "/" + str(random.choice(status_codes))
    #     res = self.client.get(random_url)
    #
    #     print("Random https status")
    @task
    class MyAnotherHTTPCat(TaskSet):

        @task
        def get_500_status(self):
            self.client.get("/500")
            print("Get status of 500")
            self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)