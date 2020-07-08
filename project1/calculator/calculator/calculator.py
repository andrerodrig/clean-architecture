"""Main module."""

from functools import reduce

class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        return reduce(lambda x, y: x - y, args)

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        if not b:
            return 'inf'
        return a / b


    def avg(self, arr, ut=None, lt=None):
        _arr = arr[:]

        if lt:
            _arr = [x for x in _arr if x >= lt]

        if ut:
            _arr = [x for x in _arr if x <= ut]

        if not len(_arr):
            return 0

        return sum(_arr)/len(_arr)
