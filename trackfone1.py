import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel

# Creating tkinter window
window = tk.Tk()
window.title('DASHBOARD')
window.geometry('700x250')

# label text for title
ttk.Label(window, text="Trackfone", foreground="blue",
          font=("Times New Roman", 25)).grid(row=0, column=3)

#label text for subtitle
ttk.Label(window, text="FINANCIAL", foreground="black",
          font=("Arial", 10)).grid(row=1, column=2)

ttk.Label(window, text="FORECASTING", foreground="black",
          font=("Arial", 10)).grid(row=1, column=3)

ttk.Label(window, text="DASHBOARD", foreground="black",
          font=("Arial", 10)).grid(row=1, column=4)

# Carrier dropdown
ttk.Label(window, text="Carrier",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)

# Combobox creation
a = tk.StringVar()
carrierchoosen = ttk.Combobox(window, width=8, textvariable=a)

# Adding combobox drop down list
carrierchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April')

# label
ttk.Label(window, text="PLAN",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=6, padx=10, pady=25)

# Combobox creation
n = tk.StringVar()
planchoosen = ttk.Combobox(window, width=8, textvariable=n)

# Adding combobox drop down list
planchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April')

# label 2
ttk.Label(window, text="TECHNOLOGY",
          font=("Times New Roman", 10)).grid(column=2,
                                             row=6, padx=10, pady=25)

# Combobox creation
m = tk.StringVar()
technologychoosen = ttk.Combobox(window, width=8, textvariable=m)

# Adding combobox drop down list
technologychoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April')

# label 3
ttk.Label(window, text="DEVICE TYPE",
          font=("Times New Roman", 10)).grid(column=4,
                                             row=6, padx=10, pady=25)

# Combobox creation
p = tk.StringVar()
devicechoosen = ttk.Combobox(window, width=8, textvariable=p)

# Adding combobox drop down list
devicechoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April')

# label 4
ttk.Label(window, text="DRIVER",
          font=("Times New Roman", 10)).grid(column=6,
                                             row=6, padx=10, pady=25)

# Combobox creation
v = tk.StringVar()
driverchoosen = ttk.Combobox(window, width=8, textvariable=v)

# Adding combobox drop down list
driverchoosen['values'] = ('0-10',
                           '11-20',
                           '21-30',
                           '31-40',
                           '41-50',
                           '51-60',
                           '61-70',
                           '71-80',
                           '81-90',
                           '91-100')

carrierchoosen.grid(column=1, row=5)
carrierchoosen.current()
planchoosen.grid(column=1, row=6)
planchoosen.current()
technologychoosen.grid(column=3,row=6)
technologychoosen.current()
devicechoosen.grid(column=5,row=6)
devicechoosen.current()
driverchoosen.grid(column=7,row=6)
driverchoosen.current()

window.mainloop()