from itertools import chain

# Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class Flat_iterator:
    def __init__(self, nested_list):
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self
    # reassigning "__str__" method to print out the result of itteration el by el

    def __str__(self):
        return '\n'.join(str(el)for el in nested_list[self.start])

    def chain_list(nested_list):
        print(list(chain.from_iterable(nested_list)))


class Flat_generator:

    def flat_generator(self, nested_list):
        return [num for el in nested_list for num in el]


if __name__ == '__main__':
    # printing "unpacked" nested list element by element
    for elem in Flat_iterator(nested_list):
        print(elem)
    print("--------------------------------------------")
    # printing "unpacked" nested list in a single list
    Flat_iterator.chain_list(nested_list)
    print('--------------------------------------------')
    # printing generated elements from nested list one by one
    result = Flat_generator()
    for el in result.flat_generator(nested_list):
        print(el)
