'''Users can be added and a role can be assigned to them. Same role can be assigned to more than one user but an user can have only single role. So support Add User operation and Display Users operation (users can be displayed in any order).'''


roles=[]     #STORE ALL NODES
roles_with_user=[]  #STORING ROLE ONLY ALLOCATE THE USER AND ALL NAME
all_name=[]  #ALL NAMES LIST

root_role=str(input("Enter root role name : "))
roles.append(root_role)

while True:
    print("Operations")
    print("1. Add Sub Role")
    print("2. Display Roles.")
    print("3. Delete Role.")
    print("4. Add User.")
    print("4. Display Users.")
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
    
    elif operation==4: #ADD USER
        print("Operation to be performed : 4")
        user_name=str(input("Enter User Name :"))
        role_name=str(input("Enter Role :"))
        if role_name in roles:
            roles_with_user.append(role_name) #ROLE ONLY ALLOCATE THE USER
            all_name.append(user_name) #USERS LIST
            
    elif operation==5:
        print("Operation to be performed : 5")
        if len(all_name)==len(roles_with_user):
            for x in range (len(all_name)): #PRINT USERS
                print( all_name[x]," - ",roles_with_user[x])



