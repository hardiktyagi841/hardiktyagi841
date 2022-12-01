# Ask a user for name
# Example - Hardik tyagi
# print count of each words
# output : 
        # H : 1
        # a : 2
        # r : 1
        # d : 3
        # i : 3
        # k : 2
        # T:  1
   
     
        


name = input("Enter your full name : ")

temp_var = ""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1    
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
