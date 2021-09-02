import pickle
# cars = ["Audi", "BMW", "Ferrari", "Mercedes"]
# file = "mycars.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "mycars.pkl"
fileobj = open(file, "rb")
mycars = pickle.load(fileobj)
print(mycars)