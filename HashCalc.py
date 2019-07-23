"""
Date: 23-07-2019
Application name: Hash Calculator
Author: Dhruvik Mevada
Email: dhruvik333@gmail.com
Github Username: dhruvikmevada
"""

import tkinter
import hashlib
from tkinter import *


root = tkinter.Tk()
root.configure(bg='lightblue')
root.title("Hash Calculator")
root.geometry("550x250")
root.resizable(0,  0)


def clearbox():
    txt_shw_md5.delete(0, 'end')
    txt_shw_sha256.delete(0, 'end')
    txt_shw_sha1.delete(0, 'end')


def flbl_md5():

    invalid_input = 'Invalid Input'
    if len(txt_str_input.get()) == 0:

        txt_shw_md5.insert('end', invalid_input)
        txt_shw_md5.configure(state='readonly')

        txt_shw_sha256.insert('end', invalid_input)
        txt_shw_sha256.configure(state='readonly')

        txt_shw_sha1.insert('end', invalid_input)
        txt_shw_sha1.configure(state='readonly')
    else:

        txt_shw_md5.configure(state=NORMAL)
        txt_shw_sha256.configure(state=NORMAL)
        txt_shw_sha1.configure(state=NORMAL)

        clearbox()
        txt_input = txt_str_input.get()

        txt_md5_output = hashlib.md5(txt_input.encode())
        shmd = txt_md5_output.hexdigest()
        txt_shw_md5.insert('end', shmd)
        txt_shw_md5.configure(state='readonly')

        txt_sha256_output = hashlib.sha256(txt_input.encode())
        a_shmd = txt_sha256_output.hexdigest()
        txt_shw_sha256.insert('end', a_shmd)
        txt_shw_sha256.configure(state='readonly')

        txt_sha1_output = hashlib.sha1(txt_input.encode())
        b_shmd = txt_sha1_output.hexdigest()
        txt_shw_sha1.insert('end', b_shmd)
        txt_shw_sha1.configure(state='readonly')


# GUI

blank_lbl = tkinter.Label(root, text=' ', bg='lightblue')
blank_lbl.grid(row=0, column=0, padx=10)
lbl_str_input = tkinter.Label(root, text='Input String', bg='lightblue')
lbl_str_input.grid(row=1, column=0, padx=10, pady=10)
txt_str_input = tkinter.Entry(root, width='70')
txt_str_input.grid(row=1, column=1, padx=10, pady=10)

# md5

lbl_md5 = tkinter.Label(root, text='Md5', bg='lightblue')
lbl_md5.grid(row=2, column=0, padx=10, pady=10)
txt_shw_md5 = tkinter.Entry(root, width='70')
txt_shw_md5.grid(row=2, column=1, padx=10, pady=10)

# sha256

lbl_sha256 = tkinter.Label(root, text='Sha256', bg='lightblue')
lbl_sha256.grid(row=3, column=0, padx=10, pady=10)
txt_shw_sha256 = tkinter.Entry(root, width='70')
txt_shw_sha256.grid(row=3, column=1, padx=10, columnspan=2)

# sha1

lbl_sha1 = tkinter.Label(root, text='Sha-1', bg='lightblue')
lbl_sha1.grid(row=4, column=0, padx=10, pady=10)
txt_shw_sha1 = tkinter.Entry(root, width='70')
txt_shw_sha1.grid(row=4, column=1, padx=10, columnspan=2)

btn_add = tkinter.Button(root, text="Convert", fg="green", command=flbl_md5)
btn_add.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
