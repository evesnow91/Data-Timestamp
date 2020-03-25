"""Starlette is a very fast python web framework, so in order to stress-test it effectively we have to use the locust distributed load testing framework ."""

from locust import HttpLocust, TaskSet, task, between

class StamperTaskSet(TaskSet):

    @task(6)
    def stamp(self):
        response = self.client.post("/api/v1/stamp", {"checksum": "000"})
        if response.status_code != 200:
            response.failure("The stamp response was an eror")

    @task(1)
    def validate(self):
        response = self.client.post("/api/v1/validate")
    
    @task(1)
    def consistency(self):
        response = self.client.post("/api/v1/consistency")



class VerifierTaskSet(TaskSet):

    @task(6)
    def stamp(self):
        response = self.client.post("/api/v1/stamp")

    @task(1)
    def validate(self):
        response = self.client.post("/api/v1/validate")
    
    @task(1)
    def chain_check(self):
        response = self.client.post("/api/v1/consistency")

class Stamper(HttpLocust):
    host = "127.0.0.1:5000"
    task_set = StamperTaskSet
    wait_time = between(0.1, 12)


class ChainVerifier(HttpLocust):
    host = "127.0.0.1:5000"
    task_set = VerifierTaskSet
    wait_time = between(2, 30)
