from tkinter import*
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('currency converter')
root.geometry("500x500")


# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#Create two frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

#Add Our Tabs
my_notebook.add(currency_frame, text="currencies")
my_notebook.add(conversion_frame, text="convert")

# Disable 2 tab
my_notebook.tab(1, state='disabled')

#########***************************#########
#########********CURRENCY STUFF*****#########
##########**************************#########

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING!", "You didn't fill out all the fills")
    else:
        #Disable entry boxex
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        # Enable tab
        my_notebook.tab(1, state='normal')
        amount_lable.config(text=f' Amount of {home_entry.get()} To convert To { conversion_entry.get()}' )
        converted_lable.config(text=f'Equals This Many {conversion_entry.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')


def Unlock():
        # Enable entry boxex
        home_entry.config(state="normal")
        conversion_entry.config(state="normal")
        rate_entry.config(state="normal")
        # Disable tab
        my_notebook.tab(1, state='disabled')

home = LabelFrame(currency_frame, text="Your Home currency")
home.pack(pady=20)

# Home currency entry box
home_entry = Entry(home, font=("helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="conversion currency")
conversion.pack(pady=20)

#conver to lable
conversion_lable = Label(conversion, text="currency to convert to...")
conversion_lable.pack(pady=10)

# Convert to entry
conversion_entry = Entry(conversion, font=("helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

#rate to lable
rate_lable = Label(conversion, text="current conversion rate...")
rate_lable.pack(pady=10)

# rate to entry
rate_entry = Entry(conversion, font=("helvetica", 24))
rate_entry.pack(pady=10, padx=10)

#Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)
# Create button
lock_button = Button(button_frame, text="lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="unlock", command=Unlock)
unlock_button.grid(row=0, column=1, padx=10)

##########*********************########
##########****CONVERTED STUFF**########
##########********************#########
def convert():
    # clear converted entry box
    converted_entry.delete(0, END)
    #convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # convert to two decimal places
    conversion = round(conversion, 2)
    # Adding commas
    conversion = '{:,}'.format(conversion)
    #upload entry box
    converted_entry.insert(0, conversion)

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

    
amount_lable = LabelFrame(conversion_frame, text="Amount To Convert")
amount_lable.pack(pady=20)

# Entry Box For amount
amount_entry = Entry(amount_lable, font=("helvetica", 24))
amount_entry.pack(pady=10)

#convert Button
convert_button = Button(amount_lable, text="convert", command=convert)
convert_button.pack(pady=20)

#Equals Frame
converted_lable = LabelFrame(conversion_frame, text="Converted currency")
converted_lable.pack(pady=20) 
#Converted Entry
converted_entry = Entry(converted_lable, font=("helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)
#Clear Button
clear_button = Button(conversion_frame, text="Clear" , command=clear)
clear_button.pack(pady=20)


root.mainloop()