'''Display each user with the list of users who are working under the particular user. (This is decided based on the role of the user). For example, according to the above given role diagram, Manager - Engineering, Developer, Tester, DevOps works under Sr Product Eng Manager.'''




all_role=[]  #ALL ROLE
list1=[] #ROOT ROLE
list2=[]  #CEO SUB ROLE
list3=[]  #COO,CTO SUB ROLE
list4=[]  #SENIOR SUB ROLE
role_with_user=[]  #STORING ROLE ONLY ALLOCATE THE USER
all_namelist=[] #ALL all_namelist
listname1=[] #USER OF ROOT ROLE
listname2=[] #USER OF CEO SUB ROLE
listname3=[] #USER OF COO,CTO SUB ROLE 
listname4=[] #USER OF SENIOR SUB ROLE
ordername=[] #ALL USER WITH ORDER

root_role=str(input("Enter root role name : "))
all_role.append(root_role)
list1.append(root_role)

while True:
    print("Operations.")
    print("1.Add Sub Role.")
    print("2. Display Roles.")
    print("3. Delete Role.")
    print("4. Add User.")
    print("5. Display Users.")
    print("6. Display Users and Sub Users.")
    operation=int(input())

    if operation==1:
        print("operation to be performed : 1")
        sub_role=str(input("Enter sub role name : "))
        rep_role=str(input("Enter reporting to role name : "))
        if rep_role == root_role:     #CHECK SUB ROLE OF CEO
            all_role.append(sub_role)
            list2.append(sub_role)
        elif rep_role != root_role:    #CHECK SUB ROLE OF CEO
            for x in list2:
                if list2[0]==rep_role:
                    all_role.append(sub_role)
                    list3.append(sub_role)
                    break
                elif list2[1]==rep_role:
                    all_role.append(sub_role)
                    list4.append(sub_role)
                    break

    elif operation==2:
        print(*all_role)

    elif operation==3:     #DELETE AND TRANSFER
        print("Operation to be performed : 3")
        delete_role=str(input("Enter the role to be deleted :"))
        if delete_role in all_role:     #FIND AND DELETE
            indx=all_role.index(delete_role)
            all_role.remove(delete_role)
        transfer_role=str(input("Enter the role to be transferred :"))
        if transfer_role in all_role:     #FIND AND TRANSFER
            all_role.remove(transfer_role)
            all_role.insert(indx,transfer_role)
                    
    elif operation==4:  #ADD USER
        print("operation to be performed : 4")
        user_name=str(input("Enter User Name :"))
        role_name=str(input("Enter Role :"))
        if role_name in all_role:
            role_with_user.append(role_name)   #ROLE ONLY ALLOCATE THE USER
            all_namelist.append(user_name)   #USERS LIST

    elif operation==5:   
        print("operation to be performed : 5")
        if len(all_namelist)==len(role_with_user):   
            for x in range (len(all_namelist)):
                print( all_namelist[x]," - ",role_with_user[x])  #PRINT USERS
            
    elif operation==6:
        print("operation to be performed : 6")
        for x in range(len(all_namelist)):  #ARRANGE THE USER BASED ON ROLES
            store=role_with_user[x]
            store1=all_namelist[x]
            if store in list1:     #FIND A ROOT ROLE OF USER
                listname1.append(store1)
            if store in list2:                  #FIND A CEO SUB ROLE OF USER
                listname2.append(store1)
            if store in list3:         #FIND A COO SUB ROLE OF USER
                listname3.append(store1)
            if store in list4:    #FIND A CTO SUB ROLE OF USER
                listname4.append(store1)
        ordername.extend(listname1) #STORE THE ARRANGED USER
        ordername.extend(listname2)
        ordername.extend(listname4)
        ordername.extend(listname3)
        for x in ordername: #PRINT THE ALL USER
            stor1=x
            if stor1 in listname1:   #PRINT A ROOT ROLE OF USER
                print(stor1," - ",*listname2,*listname4,*listname3)
            if stor1 in listname2:    #PRINT A CEO SUB ROLE OF USER
                print(stor1," - ",*listname3)
            if stor1 in listname4:    #PRINT A COO SUB ROLE OF USER
                print(stor1)
            if stor1 in listname3:   #PRINT A CTO SUB ROLE OF USER
                print(stor1)
   

