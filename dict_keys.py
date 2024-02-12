'''class getDict(dict):
   def __getitem__(self,key):
       if dict.__getitem
       if key in self:
          return dict.__getitem__(self,key)
       else:
          return None
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.template = {}'''


def get_template(target, template):
        for key in target:
            if isinstance(target.get(key), dict):
                template[key] = {}
                get_template(target.get(key), template[key])
            else:
                template[key] = 'v'
        return template

d = {'k1':1,'k2':{'k31':3,'k32':4}}
t={}
print(str(d), get_template(d,t))


'''
flatten = lambda *n: (e for a in n
    for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))'''
