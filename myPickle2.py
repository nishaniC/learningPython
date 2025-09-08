import pickle
class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size


#cucu = Cucumber()

#with open('cucumber.pckl', 'wb') as file_out:
#    pickle.dump(cucu, file_out)


with open('cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())
