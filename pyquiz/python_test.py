def comprehension():
    x = [100,110,120,130,140,150]
    y = [a*5 for a in x]
    print(y)

comprehension()


def divisible_by_three():
    n = range(1,9)
    for x in n:
        if x%3==0:
            print(x)
        

divisible_by_three()


def nested_list():
     x = [[1,2],[3,4],[5,6]]
     for a in x:
         print(a)

nested_list()


def smallest():
    list = [3,6,8,2,4,1,5,7]
    print(min(list))

smallest()

def remove():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    r = set(x)
    print(r)

remove()

def  divisible_by_seven():
    y = range(100,200)

    for t in y:
        if t%7==0:
            print(t)

divisible_by_seven()

# def greeting():
#     students =[
#         {"age": 19, "name": "Eunice"},
#         {"age": 21, "name": "Agnes"},
#         {"age": 18, "name": "Teresa"}, 
#         {"age": 22, "name": "Asha"}
#     ]
    
#     print(students['age'])

# greeting()
    


class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        



    





