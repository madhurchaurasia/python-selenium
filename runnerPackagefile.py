#from pythonLearning import pythonPackage1
# print(al.PI)
# print(al.connection)
# print(bi.GNA.getNameCity())
# print(bi.GNA.getAll())

from pythonLearning.pythonPackage1 import mb,cl,av

if __name__ == "__main__":
    myBioDataObject = mb("Madhur", 34, "Bhopal")
    print(type(myBioDataObject))
    get_all = myBioDataObject.getAll()
    print(type(get_all))
    print(get_all)
    addResult = cl.addition_two(4, 5)
    print(type(addResult))
    print(addResult)
    print(av.PI)