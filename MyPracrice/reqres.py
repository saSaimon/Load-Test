from locust import HttpUser, constant, task

class MyReqRest(HttpUser):

    # host = "https://reqres.in/"
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("api/users?page=2")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        res = self.client.post("api/users", data= '''{"name":"morpheus","job":"leader","id":"252","createdAt":"2022-06-13T10:34:07.993Z"}''')
        print(res.text)
        print(res.status_code)
        print(res.headers)
