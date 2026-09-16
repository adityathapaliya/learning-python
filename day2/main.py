# thisdict = dict(name = "aditya", age = 18, country = "nepal")
# print(thisdict)
#########


# print the dictionary / access and print a value using its key / find the length of the dictionary / get a value using get()
# d = {'aditya':96 , 'alson':83 , 'sudip':89 }
# print(d)

# x = d['aditya']
# print(x)
# print(d['aditya'])
# print(len(d))
# x = d.get('aditya')
#print(x)
#########


#print the keys only/ print values of the key only /and both key and value pair(items)
# d = {1:'aditya', 2:'harshit' , 3:'aditi'}
# print(d.keys())
# print(d.values())
# print(d.items())
##########


#this program changes the value of the key/ adds new key value pair to the dictionry
# d = {1:'aditya', 2:'harshit' , 3:'aditi'}
# x = d.values()
# print(x)

# d[1] = 'thups'
# print(x)

# d[4] = 'hello'
# print(x)
# print(d.items())
##########


#changing items in a dictionary
# d = {1:'aditya', 2:'harshit' , 3:'aditi'}
# print(d)
# d[1]= 'yo'
# print(d)
# d.update({1: 'thups' })       //update can also be used to add items
# print(d)
##########


#the program teaches how to remove items in dictionary
# d = {1:'aditya', 2:'harshit' , 3:'aditi'}
# print(d)
# d.pop(1)                                 #remove the item from its key 
# print(d)
# d.popitem()                              #removes the last item (before version 7 remoces random item)
# print(d)
# del d[2]                                 #removes item by its key  name
# print(d)
# d = {1:'aditya', 2:'harshit' , 3:'aditi'}
# print(d)
# d.clear()                                #remover all the value of the dictionary
# print(d)
##########


#copying one dictionary to the other
# d = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 2010
# }
# mydict = d.copy()                         #using copt methord
# print(mydict) 
# thisdict = dict(d)                        #using clever trick to copy
# print(thisdict)
##########


#created list inside dictionary/ created didt inside dict / accesing vlaue of dict dict value
# dl = {'aditya': [95,87,98,78,93], 'swornim':[87,98,76,78,98] , 'adarsh':[67,67,78,57,84]}
# s1 = {'name':'aditya', "year": 1, 'semister' : 2}
# s2 = {'name':'sudip', "year": 1, 'semister' : 2}
# s3 = {'name':'sudip', "year": 1, 'semister' : 2}
# dd = {'student1':s1, 'student2':s2, 'student3':s3}
# print(dd.items())
# print(dd['student1']['name'])
































