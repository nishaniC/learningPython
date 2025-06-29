class luxuryWatch:
    watches_created=0
    
    def __init__(self):
        luxuryWatch.watches_created += 1
        
    def reduce(self,num):
        return luxuryWatch.get_number_of_watches_created()- num
    
    def reduce2(self):
        return self.reduce(10)
   
    @classmethod
    def engraving(cls, text):
        try:
            luxuryWatch.validateEngraving(text)
            _watch = cls()
            _watch.engrave=text
            return _watch
        except:
            print("Engariving provided is incorrect")
     
    @classmethod
    def addto(cls, num):
        return luxuryWatch.get_number_of_watches_created()+num
        
    @classmethod
    def get_number_of_watches_created(cls):
        return luxuryWatch.watches_created
        
    @staticmethod
    def validateEngraving(text):
        # print("in validateEngraving ")
        if (len(text)>40):
            # print("length is ok ")
            if (text.isalnum):
                # print("isalnum")
                return True
            else:
                raise ValueError
        else:
                raise ValueError        
        
print("before creating any, watches_created: ",luxuryWatch.get_number_of_watches_created())    
watch=luxuryWatch()  
print("after creating a plain watch, watches_created: ",luxuryWatch.get_number_of_watches_created())  
engravedWatch=luxuryWatch.engraving("WanniArachchigeNishaniErandikaChandrasiri1")
print("after creating en engraved watch too, watches_created: ",luxuryWatch.get_number_of_watches_created())  
engravedWatch2=luxuryWatch.engraving("foo@baz.com")
print("after trying to create an incorrectly engraved watch: watches_created: ",luxuryWatch.get_number_of_watches_created())  
print(luxuryWatch.addto(10))
print(watch.reduce2())
print(luxuryWatch.validateEngraving("WanniArachchigeNishaniErandikaChandrasiri"))
        
    
        
        
    
