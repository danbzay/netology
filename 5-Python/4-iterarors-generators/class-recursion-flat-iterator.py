class FlatIterator:

    def __init__(self, list_of_list):
        self.nested = None
        #print(f'5 {self =}')
        self.base = iter(list_of_list)
        self.wrapper = None

    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            if self.nested == None:
                item = self.base.__next__()
            else: 
                item = self.nested.__next__()
            if isinstance(item, list):
                self.nested = FlatIterator(item)
                self.nested.wrapper = self
                item = self.nested.__next__()
        except StopIteration:
            if self.wrapper == None:
                raise StopIteration
            else:
                self.wrapper.nested = None
                item = self.wrapper.__next__()
            
        #print(f'return {item =}')
        return item

def test_1():
    
    print('test1')

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_3():
    
    print('test3')

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_1()
    test_3()

    