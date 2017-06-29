# methodsingledispatch

modify singledispatch from functools standard library to work with class methods

## example
```python
from dispatchtool import method_single_dispatch


class Num:
    def __init__(self, num):
        self.num = num

    @method_single_dispatch
    def __add__(self, other):
        pass

    @__add__.register(int)
    def int_add(self, other):
        return self.num + other

    @__add__.register(str)
    def str_add(self, other):
        return str(self.num) + other


if __name__ == '__main__':
    first_num = Num(10)
    print(first_num + 10)
    print(first_num + 'python')
```