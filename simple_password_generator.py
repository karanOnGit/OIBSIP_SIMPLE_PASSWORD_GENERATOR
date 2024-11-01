from tkinter import *
import pyperclip
import random
import string


def gen_password():
    password = ""
    try:
        size = int(password_entry.get())
        if level.get():
            for i in range(size):
                if i == 0 or i == 1:
                    password += chr(random.randrange(65, 91))
                elif i == 2 or i == 3:
                    password += chr(random.randrange(35, 39))
                elif i < size // 2:
                    password += chr(random.randrange(97, 123))
                else:
                    ran = random.randrange(0, 10)
                    password += str(ran)
            result_label.config(text=password)
        else:
            num = random.randrange(0, 4)
            if num == 0:
                password += string.ascii_uppercase
                password = "".join(random.choice(password) for _ in range(size))
                result_label.config(text=password)
            elif num == 1:
                password += string.ascii_lowercase
                password = "".join(random.choice(password) for _ in range(size))
                result_label.config(text=password)
            elif num == 2:
                password += string.ascii_letters
                password = "".join(random.choice(password) for _ in range(size))
                result_label.config(text=password)
            elif num == 3:
                password += string.digits
                password = "".join(random.choice(password) for _ in range(size))
                result_label.config(text=password)
            else:
                password += string.punctuation
                password = "".join(random.choice(password) for _ in range(size))
                result_label.config(text=password)
    except ZeroDivisionError:
        result_label.config(text="Value Error")
    return


def copy():
    random_password = result_label.cget("text")
    if random_password:
        pyperclip.copy(random_password)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x330")
    root.title("Password Generator")

    main_frame = Frame(root, padx=20, pady=20, bg="#123")
    main_frame.pack(fill=BOTH, expand=True)

    heading_label = Label(
        main_frame,
        text="Password Generator",
        font=("Arial", 18, "bold"),
        anchor="w",
        bg="#123",
        fg="#fff",
    )
    heading_label.pack(fill=X, pady=(0, 20))

    password_size = Frame(main_frame, height=30, bg="#123")
    password_size.pack(fill=X, pady=(0, 10))
    password_size.pack_propagate(False)

    password_label = Label(
        password_size,
        text="Password Size:",
        font=("Arial", 12, "bold"),
        anchor="w",
        bg="#123",
        fg="#fff",
    )
    password_label.pack(side=LEFT)

    password_entry = Entry(
        password_size,
        border=3,
        width=12,
        font=("Arial", 10, "bold"),
        bg="#123",
        fg="#fff",
    )
    password_entry.pack(side=RIGHT, expand=False, fill=BOTH)

    unit_frame = Frame(main_frame, bg="#123")
    unit_frame.pack(fill=X, pady=(0, 10))

    level = BooleanVar()
    check_box = Checkbutton(
        unit_frame,
        text="Hard",
        variable=level,
        bg="#123",
        fg="#fff",
        selectcolor="#123",
        activebackground="#123",
        activeforeground="#fff",
    )
    check_box.pack(side=LEFT)

    submit_button = Button(
        main_frame,
        text="Generate",
        font=("Arial", 12, "bold"),
        command=gen_password,
        bg="#123",
        fg="#fff",
        cursor="hand2",
    )
    submit_button.pack(pady=(0, 20))

    result_label = Label(
        main_frame, text="", font=("Arial", 14, "bold"), bg="#123", fg="#fff"
    )
    result_label.pack()

    copy_button = Button(
        main_frame,
        text="Copy",
        command=copy,
        bg="#123",
        fg="#fff",
        cursor="hand2",
    )
    copy_button.pack()

    root.resizable(False, False)
    root.mainloop()
