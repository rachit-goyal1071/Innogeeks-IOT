import tkinter

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password":
        label_result.config(text="Login successful!")
    else:
        label_result.config(text="Login failed!")

# Create the main window
window = tkinter.Tk()
window.title("Login")

# Create the username label and entry
label_username = tkinter.Label(window, text="Username:")
label_username.pack()
entry_username = tkinter.Entry(window)
entry_username.pack()

# Create the password label and entry
label_password = tkinter.Label(window, text="Password:")
label_password.pack()
entry_password = tkinter.Entry(window, show="*")
entry_password.pack()

# Create the login button
button_login = tkinter.Button(window, text="Login", command=login)
button_login.pack()

# Create the result label
label_result = tkinter.Label(window, text="")
label_result.pack()

# Start the main loop
window.mainloop()