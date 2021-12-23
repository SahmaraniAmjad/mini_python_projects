pwd = input("What is the master password? ")
# we have to install a library :)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", passw)


def add():
    name = input('Account name: ')
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("Would like to add a new password or view existing ones (view, add) ?, q for Quit").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode. ")
