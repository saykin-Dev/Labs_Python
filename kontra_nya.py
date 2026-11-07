# декоратор для подсчета кол-ва вызова той или иной функции
def count_of_call(some_func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return some_func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

# генетатор беск последовательности фибоначи 
 
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def gen_fib():
    n = 0
    while True:
        yield fib(n)
        n += 1

# тесты:
gen = gen_fib()
for i in range(10):
    print(next(gen), end=" ")
print()

# быстрая сортировка чисел в спиське 

def quicksort(user_list):
    if len(user_list) <= 1:
        return user_list

    pivot = user_list[len(user_list) // 2]
    less = [x for x in user_list if x < pivot]
    equal = [x for x in user_list if x == pivot]
    great = [x for x in user_list if x > pivot]

    return quicksort(less) + equal + quicksort(great)









