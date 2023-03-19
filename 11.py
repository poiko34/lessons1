my_list = [1, 2, 3]
iterator = iter(my_list)


# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for elem in iterator:
#     print(elem)

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


# count = Counter(5)
# for elem in count:
#     print(elem)

# iter(count)
# print(count.__next__())
# print(next(count))

def my_negerator(n, max):
    i = 0
    while True:
        result = n ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1


gen = my_negerator(122345, 500)
print(next(gen))
for _ in gen:
    print(_)


class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"I will help you with {self.work}. ALSO HELP WITH {work}"


def Helper2(work):
    work_in_memory = work

    def helper(work):
        return f"I will help you with {work_in_memory}. ALSO HELP WITH {work}"

    return helper


# helper3 = Helper2("homework")
# print(helper3("cleaning"))
# print(helper3("driving"))
# helper = Helper('homework')
# print(helper("cleaning"))

def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problem {exc}")
        else:
            print(f"No problem result = {result}")

    return checker


@checker
def calculate(expressin):
    return eval(expressin)


print(calculate("(346566764875685637356*5675686783763786857367)+(346566764875685637356*5675686783763786857367)"))
