users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printNames(users):
    for userType in users:
        print(userType)
        i = 1
        for user in users[userType]:
            string = str(i) + " - "
            nameString = user['first_name'] + " " + user['last_name']
            string += nameString
            print string + " - " + str(len(nameString)-1)
            i += 1
printNames(users)