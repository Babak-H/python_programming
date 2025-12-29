from tkinter import *
from tkinter import messagebox
import base64
import json
import pickle
import string
import random

def key_generator(size=20, char=string.ascii_uppercase + string.digits):
    '''
    Generates a random string of characters to be used as an encryption key
    It randomly selects size characters from char and returns them as a string, 'R7U3Z2M8P9X1L0BVDQKC'
    size: Length of the key (default is 20 characters)
    char: Pool of characters to choose from (uppercase letters and digits)
    '''
    return ''.join(random.choice(char) for x in range(size))


def encode(key, clear):
    '''
    Encrypts a plaintext string using a simple custom cipher with the provided key, then encodes it using base64.
    Loops through each character in the 'clear' text
    For each character, it:
    Gets the corresponding character from the key (repeats key if shorter).
    Adds their ASCII values and wraps with % 256 to keep it in byte range
    Joins all encrypted characters and encodes the result in base64 for safe storage.
    '''
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]  # key character
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)  # encoded character
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def save(login, password, path, destiny):
    '''
    Encrypts login credentials and saves them to a JSON file, while also saving the encryption key in a separate file.
    Calls key_generator() to get a new key, based on destiny flag, sets file names for storing the key and credentials.
    Saves the generated key using pickle to a .key file
    Encrypt Login and Password, Uses the encode() function to encrypt both
    Stores encrypted login and password as a JSON dictionary in a .json file
    True if successful, False if any step fails

    login: The login string to encrypt and save.
    password: The password string to encrypt and save
    path: Directory path where files should be saved
    destiny: A flag to choose between two sets of filenames
    '''
    key = key_generator()
    if destiny == 1:
        Path_key = path + "\\KeyDB.key"
        Path = path + "\\credentialsDB.json"
    else:
        Path_key = path + "\\KeyiSara.key"
        Path = path + "\\credentialsiSara.json"

    try:
        Key_file = open(Path_key, "wb")
        pickle.dump(key, Key_file)
        Key_file.close()
    except Exception as error:
        return False
    
    Login = encode(key, login)
    Password = encode(key, password)
    json_data = {"log":Login, "pass":Password}

    try:
        with open(Path, 'w') as file:
            json.dump(json_data, file)
    except Exception as error:
        return False
    
    return True


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Encryptor")

        self.label_login = Label(master, text="Login:")
        self.label_login.grid(row=0)

        self.login = Entry(master,  width=40) 
        self.login.grid(column=1, row=0, columnspan=5)
        self.login.focus()
        self.clear_login_button = Button(master, text="Clear", command=self.clear_log)
        self.clear_login_button.grid(column=6, row=0, padx=5, pady=2)

        self.label_password = Label(master, text="Password:")
        self.label_password.grid(row=1)

        self.password = Entry(master, show='*',  width=40) 
        self.password.grid(column=1, row=1, columnspan=5)

        self.clear_password_button = Button(master, text="Clear", command=self.clear_pass)
        self.clear_password_button.grid(column=6, row=1, padx=5, pady=2)

        self.label_path = Label(master, text="Path:")
        self.label_path.grid(row=2)

        self.path = Entry(master, width=40)
        self.path.grid(column=1, row=2, columnspan=5)

        self.clear_path_button = Button(master, text="Clear", command=self.clear_path)
        self.clear_path_button.grid(column=6, row=2, padx=5, pady=2)

        self.var_DB = IntVar(value=1)
        DB_checkbox = Checkbutton(master, text="MS SQL Server", variable=self.var_DB)
        DB_checkbox.grid(column=1, row=3)

        self.var_iSara = IntVar()
        iSara_checkbox = Checkbutton(master, text="iSara", variable=self.var_iSara)
        iSara_checkbox.grid(column=4, row=3)

        self.greet_button = Button(master, text="Encrypt", command=self.encrypt)
        self.greet_button.grid(column=4, row=4)

        self.info_button = Button(master, text="Information", command=self.info)
        self.info_button.grid(column=1, row=4, columnspan=3)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=5, row=4)


    def info(self):
        messagebox.showinfo("Information","This program will encrypt credentials\nand save them in JSON file in the given path\n\nIn login and password sections writedown credentials.")

    
    def encrypt(self):
        path = self.path.get()
        login = self.login.get()
        password = self.password.get()

        if path == '' or login == '' or password == '':
            messagebox.showwarning("Warning", "Something missing")
        else:
            value_DB = self.var_DB.get()
            value_iSara = self.var_iSara.get()
            if value_DB == 0 and value_iSara == 0:
                messagebox.showwarning("Warning", "Check one box")
            elif value_DB == 1 and value_iSara == 1:
                messagebox.showwarning("Warning", "Choose only one box")
            else:
                encryption_to_what = 1
                if value_iSara == 1:
                    encryption_to_what = 0
                    # encrypt the username and password in the given path address
                    if save(login, password, path, encryption_to_what):
                        messagebox.showinfo("Status", "Done, check folder")
                    else:
                        messagebox.showerror("Error", "Invalid path")
    
    def clear_log(self):
        self.login.delete(0, 'end')


    def clear_pass(self):
        self.password.delete(0, 'end')


    def clear_path(self):
        self.path.delete(0, 'end')


root = Tk()
my_gui = GUI(root)
    
root.resizable(False, False)  # prevent window from resizing
window_height = 160
window_width = 370
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

root.mainloop()
