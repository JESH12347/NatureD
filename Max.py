Students ={
     "Alice": "5",
     "Thomas": "3",
     "Ali" :"4",
     "Wei":"2",
     "Rohita":"1"
}

def get_value(item):
    return item[1]
    
sorted_asc=dict(sorted( Students.items() , key=get_value))
print("Ascending order: ", sorted_asc)

sorted_des= dict(sorted(Stu.items(), key=get_value, reverse=True))
print("Descending order: ", sorted_des)








































    