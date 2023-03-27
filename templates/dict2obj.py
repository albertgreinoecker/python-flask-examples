import json

class Person:
    def __init__(self, name, street, number):
        self.name = name
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.street, self.number)


if __name__ == '__main__':
    js = '{"name":"Hubert", "street":"Fürstenweg","number":"19-22"}'
    j = json.loads(js)
    print(j)
    u = Person(**j)  #flattens the dictionary
    print(u)
