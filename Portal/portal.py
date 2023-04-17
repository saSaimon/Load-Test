from locust import User, constant, task, HttpUser, TaskSet


class PortalLoadTest(TaskSet):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        self.client.get("/login", auth=("sadiqul.alam@wtvglobal.com", ""))
        self.client.post("/login",
                         {"item": "123", "button": "submit"},
                         auth=("sadiqul.alam@wtvglobal.com", "")
                         )
        print("Launching in URL")

    @task
    def session(self):
        self.client.get("/session")
        print("Launching Sessions")

    @task
    def agenda_speaker(self):
        self.client.get("/agenda-speakers")
        print("Launching Agenda & Speaker")


class MyLoadTest(HttpUser):
    host = "https://connectstudio-portal.world-television.com/62a31398e1849904a780e784"
    tasks = [PortalLoadTest]
    wait_time = constant(1)