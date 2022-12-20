from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_web.get()
    username = input_username.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error message", message="All the fields is required")
    else:
        is_ok = messagebox.askyesnocancel(title=website,
                                          message=f"These are the details entered: \nEmail : {username} \nPassword: {password}\n is it oke to save?")

        if is_ok:
            with open("contact.txt", "a") as data_file:
                data_file.write(f"website: {website} | email :{username} | password : {password} \n")
                input_web.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website")
web_label.grid(row=1, column=0)
web_label.focus()

username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

input_web = Entry(width=40)
input_web.grid(row=1, column=1, padx=5)

input_username = Entry(width=40)
input_username.grid(row=2, column=1, pady=8, padx=5)
input_username.insert(0, "gabenley1@gmail.com")

input_password = Entry(width=40)
input_password.grid(row=3, column=1, pady=8, padx=5)

btn_password = Button(text="Generator Password", width=20)
btn_password.grid(row=3, column=2)

btn_add = Button(text="Add", width=34, bg="blue", fg="white", command=save_password)
btn_add.grid(row=4, column=1)

window.mainloop()
