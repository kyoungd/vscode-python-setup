import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("hello"))
r = requests.get("https://www.duckduckgo.com")
print(r.status_code)
