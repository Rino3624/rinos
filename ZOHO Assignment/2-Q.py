'''Now support the add sub role operation to the root role'''



roles=[]  #STORE THE ROLES
i=1

root_role=str(input("Enter root role name : "))
roles.append(root_role)

while i<=2 :   #PERFORMS 2 TIMES ONLY
    print("Operations")
    print("1.Add Sub Role")
    operation=int(input())
    
    if operation==1:
        print("operation to be performed : 1")
        sub_role=str(input("Enter sub role name : "))
        rep_role=str(input("Enter reporting to role name : "))
        if rep_role == root_role:          #CHECK SUB ROLES OF CEO
            roles.append(sub_role)
    
    i=i+1

print(*roles)

