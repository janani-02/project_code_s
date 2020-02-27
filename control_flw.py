some_var=5
if some_var>10:
    print("some_var is totally bigger than 10.")
elif some_var<10:
    print("some_var is smaller than 10.")
else:
    print("some_var is indeed 10.")




for animal in["dog","cat","mouse"]:
    print("{} is a mammal".format(animal))



  
for i in range(5):
    print(i)




for i in range(4,8):
    print(i)





for i in range(4,8,2):
    print(i)





animals=["dog","cat","mouse"]
for i, value in enumerate(animals):
    print(i,value)

x=0
while x<4:
    print(x)
    x+=1

try:
    raise IndexError("This is an IndexError")
except IndexError as e:
    pass
except(TypeError,NameError):
    pass
else:
    print("allgood!")
finally:
    print("we can clean up resources here")

contents = {"aa":12,"bb":21}
with open("myfile1.txt","w+")as file:
    file.write(str(contents))
[
        
        {
            "type": "node",
            "request": "attach",
            "name": "Attach",
            "port": 88,
            "skipFiles": [
                "<node_internals>/**"
            ]
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",    
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
with open("myfile2.txt","w+")as file:
    file.write(json.dumps(contents))

with open('myfile1.txt',"r+")as file:
    contents=file.read()
print(contents)
    
with open('myfile2.txt',"r+")as file:
    contents=json.load(file)
print(contents)
    

filled_dict={"one":1,"two":2,"three":3}
our_iterable=filled_dict.keys()
print(our_iterable)

for i in our_iterable:
    print(i)


our_iterable[1]


our_iterator=iter(our_iterable)
next(our_iterator)
next(our_iterator)
next(our_iterator)

out_iterator=iter(our_iterable)
for i in our_iterator:
    print(i)

list(our_iterable)
list(our_iterator)

















