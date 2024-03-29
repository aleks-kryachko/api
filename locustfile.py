# http://localhost:8089
# https://pypi.org/project/locust/
#
from locust import HttpUser, SequentialTaskSet, task, between


class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):
        wait_time = between(1, 3)

        @task
        def mainPage(self):
            # self.client.get("/")
            self.client.get("http://jsonplaceholder.typicode.com/todos")

        @task
        def login(self):
            # self.client.options("https://api.demoblaze.com/login")
            # self.client.post("https://api.demoblaze.com/login", json={"username": "aaaa", "password": "YWFhYQ=="})
            # self.client.options("https://api.demoblaze.com/check")
            self.client.get("http://jsonplaceholder.typicode.com/todos/1")
            # self.client.post("https://petstore.swagger.io/v2/swagger.json", json={"token": "YWFhYTE2MzA5NDU="})

        @task
        def clickProduct(self):
            self.client.get("http://jsonplaceholder.typicode.com/todos/2")
            # self.client.options("https://api.demoblaze.com/check")
            # self.client.options("https://api.demoblaze.com/view")
            # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            # self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

        # @task
        # def addToCart(self):
            # self.client.options("https://api.demoblaze.com/addtocart")
            # self.client.post("https://api.demoblaze.com/addtocart",
            #                  json={"id": "fb3d5d23-f88c-80d9-a8de-32f1b6034bfd", "cookie": "YWFhYTE2MzA5NDU=",
            #                        "prod_id": 1, "flag": 'true'})

        # @task
        # def viewCart(self):
            # self.client.get("/cart.html")
            # self.client.options("https://api.demoblaze.com/check")
            # self.client.options("https://api.demoblaze.com/viewcart")
            # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            # self.client.post("https://api.demoblaze.com/viewcart", json={"cookie": "YWFhYTE2MzA5NDU=", "flag": 'true'})
            # self.client.options("https://api.demoblaze.com/view")
            # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            # self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

# class AwesomeUser(HttpUser):
#     tasks = ['CredentialLoadTest']
#     host = "https://url.com"
#
#     # wait time between tasks, 5 and 9 seconds
#     wait_time = between(5, 9)
from locust import HttpUser, task

# class HelloWorldUser(HttpUser):
#     def task(self):
#         @task
#         def hello_world(self):
#             self.client.get("/hello")
#             self.client.get("/world")


