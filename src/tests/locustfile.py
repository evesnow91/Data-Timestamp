"""Starlette is a very fast python web framework, so in order to stress-test it effectively we have to use the locust distributed load testing framework ."""

from locust import HttpLocust, TaskSet, between


def stamp(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
