class OwnDict(dict):
    def __setitem__(self,_key,_val):
        super().__setitem__(_key,_val)

    def update(self,*args,**kwargs):
        for _key,_val,in dict(*args,**kwargs).items():
            self.__setitem__(_key,_val)
own_dict = OwnDict()
own_dict[4]=1
own_dict[2]=0.5
print(own_dict)
