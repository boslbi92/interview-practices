import random

class HashMap():
    def __init__(self):
        self.size = 32
        self.map = [None] * self.size

    def get_hash_key(self, key):
        total = 0
        for c in str(key):
            total += ord(c)
        return total % self.size

    # jason - 921006
    def insert(self, key, value):
        hash_index = self.get_hash_key(key)
        pair = (key, value)
        if self.map[hash_index] is None:
            self.map[hash_index] = [pair]
        else:
            # collision handing
            temp = self.map[hash_index]
            for i in range(len(temp)):
                k, v = temp[i][0], temp[i][1]
                # duplicate exists
                if k == key:
                    temp[i][0] = key
                    temp[i][1] = value
                    break
            self.map[hash_index].append(pair)

    def find(self, key):
        hash_index = self.get_hash_key(key)
        data = self.map[hash_index]
        if data is None:
            return None
        for i in range(len(data)):
            k, v = data[i][0], data[i][1]
            if k == key:
                return v
        return None

    def remove(self, key):
        hash_index = self.get_hash_key(key)
        data = self.map[hash_index]

        if data is None:
            return False
        for i in range(len(data)):
            k, v = data[i][0], data[i][1]
            if k == key:
                data.pop(i)
                return True
        return False
