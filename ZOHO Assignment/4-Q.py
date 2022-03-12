'''Support delete role operation. If a role is deleted then all its properties (child roles) will be transferred to the role entered by the user as input.'''





roles=[]     #STORE ALL NODES

root_role=str(input("Enter root role name : "))
roles.append(root_role)

while True:
    print("Operations")
    print("1.Add Sub Role")
    print("2. Display Roles.")
    print("3. Delete Role.")
    operation=int(input())
    if operation==1:
        print("operation to be performed : 1")
        sub_role=str(input("Enter sub role name : "))
        rep_role=str(input("Enter reporting to role name : "))
        if rep_role == root_role:     #CHECK SUB ROLES OF CEO
            roles.append(sub_role)
        elif rep_role != root_role:    #CHECK SUB ROLES OF COO,CTO
            if rep_role in roles:
                roles.append(sub_role)
        
    elif operation==2:
        print(*roles)
        
    elif operation==3:            
        print("Operation to be performed : 3")
        delete_role=str(input("Enter the role to be deleted :"))
        if delete_role in roles:  #FIND AND DELETE A ROLE
            del_index=roles.index(delete_role)
            roles.remove(delete_role)                 
        transfer_role=str(input("Enter the role to be transferred :"))
        if transfer_role in roles:   #FIND AND REPLACE THE ROLE
            roles.remove(transfer_role)
            roles.insert(del_index,transfer_role)
         







