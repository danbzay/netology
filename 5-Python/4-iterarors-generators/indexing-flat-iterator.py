class FlatIterator:

    def __init__(self, list_of_list):
        self.base_list = list_of_list

    def __iter__(self):
        self.index = [-1]
        self.lens = [len(self.base_list)]
        return self
            
    def check_index(self):
        # if ]
        if self.index[len(self.index)-1]  >= self.lens[len(self.lens)-1]:
            self.index.pop()
            self.lens.pop()
            
            print('pop')
            if self.index == []:
                raise StopIteration
            self.index[len(self.index) -1] += 1
            return False                       
        # if [
        item = self.get_current_item()
        if isinstance(item, list):
            self.index += [0]
            self.lens += [len(item)]
            return False
        return True        


    def __next__(self):
        
        self.index[len(self.index)-1] +=1
        
        while not self.check_index():
            pass
            
        print(f'{self.index}')
        print(f'{self.get_current_item() =}')
        return self.get_current_item()
        
    def get_current_item(self):
        item = self.base_list
        for i in self.index:
            item = item[i]
        
        return item
            

def test_1():
    
    print('test1')

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    #print(f'{FlatIterator(list_of_lists_1) =}')
    print(list(zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    )))

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    print(list(FlatIterator(list_of_lists_1)))
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
