from locust import HttpUser, TaskSet, task


class LoginWithUniqueUsersSteps(TaskSet):
    @task
    def login(self):
        self.client.post("/login", {
            'email': 'sadiqul.alam@wtvglobal.com', 'password': ''
        })


class LoginWithUniqueUsersTest(HttpUser):
    task_set = LoginWithUniqueUsersSteps
    host = "https://connectstudio-portal-dev.world-television.com/62b46d6089dd457d94c51d1c"
    sock = None

    def __init__(self):
        super(LoginWithUniqueUsersTest, self).__init__()
