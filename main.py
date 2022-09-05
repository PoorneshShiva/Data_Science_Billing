from tkinter import *
import datetime
import pandas
from tkinter import ttk

import pandas as pd

store_items = {
    "1": ["Vada", 10],
    "2": ["Idly", 30]
}
items = pd.read_csv('items.csv', index_col=False)


id = 0
ddict = {
    "ID": [],
    "item": [],
    "price": [],
    "quantity": [],
    "date": [],
    "time": []
}
date = (datetime.datetime.now().strftime("%d-%h-%Y %H-%M-%S"))

data = pandas.DataFrame(ddict)
total_price = 0


def add_to_csv():
    global data, label_count, id, total_price
    for each in tree.get_children():
        item = tree.item(each)['values'][0]
        quantity = tree.item(each)['values'][1]
        price = tree.item(each)['values'][2]
        # new = pandas.Series([id, item,price, quantity, date.split()[0], date.split()[1]], index=data.columns)
        # data = data.append(new, ignore_index=True)
        # new = pandas.DataFrame([id,item,quantity])
        data.loc[len(data)] = [id, item, price, quantity, date.split()[0], date.split()[1]]
        # data = pandas.concat([data,new], axis=0, ignore_index=True)
        tree.delete(each)
    id += 1
    total_price = 0


def Save():
    save = f"item {date}.csv"
    data.to_csv(save)


def Add():
    global row, col, label_count, quantity, var_name, total_price
    var_name = f"new_text{label_count}"
    user_entered_item = (item_entry.get())
    if user_entered_item.isdigit():

        item = items.name[(items.id == int(user_entered_item)) ].values[0]
        price = items.price[(items.id == int(user_entered_item))].values[0]
    else:
        item = items.name[(items.name == user_entered_item) ].values[0]
        price = items.price[(items.name == (user_entered_item)) ].values[0]
    # ][1]

    quantity = int(quantity_entry.get())
    total_price += price * quantity
    # list_box.insert(END, f"{item} {quantity}")
    tree.insert('', END, text="1", values=(item, quantity, price * quantity))
    # f"new_text{label_count}" = canvas.create_text(70, col, text=f"{item}  {quantity}", font="Arial, 20")
    # print(var_name)
    # print(canvas.itemcget(var_name, 'text'))
    col += 30
    # var_name = Label(tk, text=f"{item}  {quantity}", font=("Arial", 15, "normal"))
    # var_name.grid(row=row, column=1, columnspan=5)

    price_label.config(text=total_price)



    submit_button = Button(text="Submit", command=add_to_csv)
    submit_button.place(x=1170, y=400)



    item_entry.delete(0, END)
    quantity_entry.delete(0, END)


def Delete():
    global total_price
    selected_tree = tree.selection()
    for each in selected_tree:
        price_to_remove =(tree.item(item=each)['values'][2])
        tree.delete(each)
        total_price -= price_to_remove
    price_label.config(text=total_price)


tk = Tk()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
tk.geometry("%dx%d" % (width, height))
tk.title("Data Science Billing")
# frame = Frame(tk, width=800, height=500)
# frame.pack_forget()
# canvas = Canvas(width=1000, height=400, bg="white")
# canvas.create_window((0,0), window=my_frame)
my_frame = Frame(tk, bg="yellow", width=50)
my_frame.grid(padx=220, pady=50, column=1, row=0)

# txt = canvas.create_text(0,149,text="gslha", font="Arial, 20")
# bbox = canvas.bbox(txt)
# canvas.create_rectangle(bbo)
#
# hbar = Scrollbar(canvas,orient=VERTICAL)
# hbar.place(x=900,y=400)
# hbar.config(command=canvas.yview)

# text = canvas.create_text(50, 20, text="Hello", font="Arial, 20")
# canvas.grid(padx=20, pady=20,row=0, column=0)
# canvas.place(x=50, y=10)

item_Label = Label(tk, text="Item", font=("Arial", 20, "normal"))
item_Label.place(x=520, y=525)
# item_Label.grid(row=1, column=0)

quantity_Label = Label(tk, text="Quantity", font=("Arial", 20, "normal"))
# quantity_Label.grid(row=1, column=2)
quantity_Label.place(y=525, x=850)
# price_Label = Label(text="Price", font=("Arial", 20, "normal"))
# price_Label.grid(row=0, column=3)

item_entry = Entry(tk, width=50)
# item_entry.grid(row=2, column=1, sticky="E", padx=12, ipady=5)
item_entry.place(x=350, y=575, height=30)

quantity_entry = Entry(tk, width=20)
# quantity_entry.grid(row=2, column=2, padx=12, ipady=5)
quantity_entry.place(x=820, y=575, height=30)

total_price_label = Label(tk, text="Total Price:", font=("Arial", 20, "normal"))
total_price_label.place(x=820,y=450, height=20)
# price_entry = Entry(width=20, justify="right")
# price_entry.grid(row=1, column=3, padx=12, ipady=5)


add_button = Button(tk, text="Add", command=Add)
# add_button.grid(row=1, column=4, columnspan=4, padx=20, ipady=2, pady=20, ipadx=50)
add_button.place(x=620, y=625, height=30)

delete_button = Button(tk, text="Delete", command=Delete)
delete_button.place(x=760, y=625, height=30)

tree = ttk.Treeview(my_frame, columns=("c1", "c2", "c3"), show="headings", height=18)
tree.column('# 1', anchor=CENTER, width=500)
tree.heading("# 1", text="Item")
tree.column('# 2', anchor=CENTER, width=200)
tree.heading("# 2", text="Quantity")
tree.column('# 3', anchor=CENTER, width=200)
tree.heading("# 3", text="Price")

tree.grid(sticky="nwes")

# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","1","1"))
# tree.insert('', END, text="1", values=("1","2","1"))
price_label = Label(tk, text=total_price, font=("Arial", 20, "normal"))
price_label.place(x=970, y=450, height=20)

myscrollbar = Scrollbar(my_frame, orient=VERTICAL, command=tree.yview)
myscrollbar.grid(row=0, column=1, sticky="news")
tree.config(yscrollcommand=myscrollbar.set)
# print(tree.item(tree.get_children()[0])['values'][0])
# for each in tree.item(tree.get_children()[0]).values():
#     print(type(each))
# myscrollbar.
# print(tree.get_children())
# my_frame.conf


# my_frame.pack()

row = 4
col = 20
label_count = 0

save = Button(text="Save", command=Save)
# save.grid(row=row + 1, column=1, columnspan=5, pady=20, ipadx=20, ipady=5)
save.place(x=1270, y=400)
# print(quantity_entry.get())
# item = (item_entry.get())
tk.columnconfigure(1, minsize=3)

tk.mainloop()
