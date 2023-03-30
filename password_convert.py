password = input("Enter password: ")
new = password
for i in range(33):
    char = '0'
    if len(new) < 32:
        new+= char
    
is_alpha = new.isalnum()
print(len(new), is_alpha)
print("new", new)


        

