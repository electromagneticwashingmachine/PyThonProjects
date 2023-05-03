"""This is importing"""

import requests


def greet(who_to_greet):
    """this is to greet"""
    greeting = f"Hello, {who_to_greet}!"
    return greeting


print(greet("Welcome!"))
print(greet("Tyron!"))


r = requests.get("https://coreyms.com", timeout=5)
print(r.status_code)
