#!/usr/bin/env python
knowledge1 = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge=knowledge1):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        pass
        return self.knowledge[random.randint(0,len(self.knowledge)-1)]