'''Support an operation to find the height of the entire role hierarchy (height of the hierarchy tree).'''


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
    print("7. Delete User.")
    print("8. Number of users from top")
    print("9. Height of role hierachy.")
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

    elif operation==7:
        print("operation to be performed : 7")
        delete_user=str(input("Enter username to be deleted :"))
        if delete_user in listname4:   #FIND AND DELETE THE USER
            listname4.remove(delete_user)
        if delete_user in listname1:
            listname1.remove(delete_user)
        if delete_user in listname2:
            listname2.remove(delete_user)
        if delete_user in listname3:
            listname3.remove(delete_user)
        for x in ordername:   #PRINT THE ALL USER
            stor1=x
            if stor1 in listname1:   #PRINT THE ROLE UNDER ROOT ROLE
                print(stor1," - ",*listname2,*listname4,*listname3)
            if stor1 in listname2:   
                print(stor1," - ",*listname3)
            if stor1  in listname4:
                print(stor1," - ")
            if stor1 in listname3:
                print(stor1," - ")
   
    elif operation==8:    
        print("operation to be performed : 8")
        usr_name=str(input("Enter user name :"))
        if x==usr_name in listname1:    #IF ROOT ROLE
            print(" This is the root user ")
        if usr_name in listname2:  #IF SUB ROLE OF CEO
            print("Number of users from top : 1 ")
        if usr_name in listname3:  #IF SUB ROLE OF COO
            print("Number of users from top : 2 ")
        if usr_name in listname4:    #IF SUB ROLE OF CTO
            print("Number of users from top : 3 ")

    elif operation==9:      #CHECK LENGTH
        print("operation to be performed : 9")
        if len (list4):    #CHECK BOTTOM TO TOP ROLES
            print("Height - 3")
        elif len (list3):
            print("Height - 3")
        elif len (list2):
            print("Height - 2")
        elif len (all_role):
            print("Height - 1")
                        

