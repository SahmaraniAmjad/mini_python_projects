from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


# we have to install a library :)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account name: ')
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


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
