''''''
usernames = []

if usernames:
   for username in usernames:
        if username == 'admin':
         print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", welcome back!")
else:
    print("We need to find some users!")

# This one was fun i dont really have much to say