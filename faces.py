class Faces(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.storage = {}

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b
        elif key == 2:
            return self.c
        else:
            return None
