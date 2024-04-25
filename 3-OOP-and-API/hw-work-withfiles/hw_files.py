
def get_recipes(recipes_filename):
    with  open(recipes_filename) as recipes_file:
        recipes = [_.split('\n') for _ in recipes_file.read().split('\n\n')]
        if recipes[-1][-1] == '':
            recipes[-1].pop()
        recipes_dickt = {_[0]:[dict(zip(['ingredient_name', 'measure', 
             'quantity'], [__.split(' | ')[0], int(__.split(' | ')[1]), 
             __.split(' | ')[2]])) for __ in _[2:]] for _ in recipes } 
    return recipes_dickt

def flatten(*n):
    return (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) 
                                               else (a,)))

def get_shop_list_by_dishes(dishes, person_count):
    recipes_dickt = get_recipes('recipes')
    recipes_dickt_flatten = sorted([list(__.values()) for __ in list(flatten(
                            [recipes_dickt[_] for _ in dishes]))])
    prevous_ingredient = recipes_dickt_flatten[0]
    in_total_dickt = {}
    for ingredient in recipes_dickt_flatten[1:]:
        if ingredient[0] != prevous_ingredient[0]:
            in_total_dickt[prevous_ingredient[0]] = {
                     'measure': prevous_ingredient[2], 
                     'quantity': person_count*prevous_ingredient[1]}
            prevous_ingredient = ingredient
        else:
            prevous_ingredient[1] += ingredient[1]
        in_total_dickt[prevous_ingredient[0]] = {'measure': 
                prevous_ingredient[2], 'quantity': prevous_ingredient[1]}
    return in_total_dickt
   
dishes = ['Запеченный картофель', 'Омлет', 'Фахитос']
print('dishes:', dishes)
print('\n get_shop_list_by_dishes(dishes, 2):')
print(get_shop_list_by_dishes(dishes, 2))


class OutFile:

    def __init__(self, outfile_name):
        self.outfile_struct = [] #infile name, number of lines, start, size 
        open(outfile_name, 'w').close() #clear existed out file
        self.outfile = open(outfile_name,'r+')
            
    def add_infile(self, infile_name):
        with open(infile_name) as infile:
            lines_count = sum(1 for _ in infile)
            infile.seek(0)
            offset = 0
            start = 0
            if self.outfile_struct:
                for i in range(len(self.outfile_struct)):
                    if lines_count < self.outfile_struct[i][1]:
                        start = self.outfile_struct[i][2]
                        self.outfile.seek(start)
                        rest = self.outfile.read()
                        self.outfile.seek(start)
                        offset = self.outfile.write(infile_name + '\n' + 
                               str(lines_count) + '\n' + infile.read() + rest)
                        self.outfile_struct.insert(i, 
                            [infile_name, lines_count, start, offset])
                    if offset != 0:
                        self.outfile_struct[i+1][2] += offset  
                if offset == 0:
                    self.outfile.seek(0,2)
                    self.outfile_struct.insert(0, [infile_name, lines_count, 
                            self.outfile.tell(), self.outfile.write(
                            infile_name + '\n' +  str(lines_count) + '\n' + 
                            infile.read())])
            else:
                self.outfile_struct.insert(0, [infile_name, lines_count, 
                                    0, self.outfile.write(infile_name + '\n' + 
                        str(lines_count) + '\n' + infile.read())])
        return
            

def unity_files(in_filenames, out_filename):
    outfile1 = OutFile(out_filename)
    for infn in in_filenames:
        outfile1.add_infile(infn)
    outfile1.outfile.close()
    return

filenames = ['1', '2', '3']
out_filename = 'out'

unity_files(filenames, out_filename)
