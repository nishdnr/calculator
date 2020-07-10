import tkinter


def btnclick(n):
    global operator
    operator = operator + str(n)
    entry_var.set(operator)


def errorcheck(number_string):
    """ This function checks for the presence of alphabets
    """
    for check_alpha in number_string:
        if check_alpha.isalpha():
            entry_var.set('Please enter only numbers')
        


def main_execution():
    """ This function performs the calculation after the equal '='
     button is pressed"""
    user_entry = entry_var.get()
    number_string = ''.join(user_entry)
    errorcheck(number_string)
    calc_eqn = eval(number_string)
    entry_var.set(calc_eqn)


def clear_all():
    """ This function clears the entry box when CE button is pressed"""
    global operator
    entry.delete(0, 'end')
    operator = ''


def clear():
    """Function similar to backspace"""
    length = len(entry.get())
    entry.delete(length-1, 'end')


main_window = tkinter.Tk()
main_window.title('Calculator')
main_window.geometry('300x300')
main_window['padx'] = 10
operator = ''


# screen
entry_var = tkinter.StringVar()
entry = tkinter.Entry(main_window, textvariable=entry_var, font=('Arial', 12, 'bold'))
entry.place(relwidth=1, relheight=0.1)
entry.config(bg='papaya whip')

# frame for keys
key_frame = tkinter.Frame(main_window, bg='light blue', border=5)
key_frame.place(relx=0.5, rely=0.15, relwidth=1, relheight=0.8, anchor='n')

# clear and delete buttons

button_clear = tkinter.Button(key_frame, text='C', font=('Arial', 12, 'bold'), command=lambda: clear())
button_clear.place(relx=0.01, rely=0.03, relwidth=0.2, relheight=0.12)

button_clear_screen = tkinter.Button(key_frame, text='CE', font=('Arial', 12, 'bold'), command=lambda: clear_all())
button_clear_screen.place(relx=0.25, rely=0.03, relwidth=0.2, relheight=0.12)


# row 1 buttons
button_seven = tkinter.Button(key_frame, text='7', font=('Arial', 12, 'bold'), command=lambda: btnclick(7))
button_seven.place(relx=0.01, rely=0.21, relwidth=0.2, relheight=0.12)

button_eight = tkinter.Button(key_frame, text='8', font=('Arial', 12, 'bold'), command=lambda: btnclick(8))
button_eight.place(relx=0.25, rely=0.21, relwidth=0.2, relheight=0.12)

button_nine = tkinter.Button(key_frame, text='9', font=('Arial', 12, 'bold'), command=lambda: btnclick(9))
button_nine.place(relx=0.50, rely=0.21, relwidth=0.2, relheight=0.12)

button_plus = tkinter.Button(key_frame, text='+', font=('Arial', 12, 'bold'), command=lambda: btnclick('+'))
button_plus.place(relx=0.75, rely=0.21, relwidth=0.2, relheight=0.12)

# row 2 buttons
button_four = tkinter.Button(key_frame, text='4', font=('Arial', 12, 'bold'), command=lambda: btnclick(4))
button_four.place(relx=0.01, rely=0.40, relwidth=0.2, relheight=0.12)

button_five = tkinter.Button(key_frame, text='5', font=('Arial', 12, 'bold'), command=lambda: btnclick(5))
button_five.place(relx=0.25, rely=0.40, relwidth=0.2, relheight=0.12)

button_six = tkinter.Button(key_frame, text='6', font=('Arial', 12, 'bold'), command=lambda: btnclick(6))
button_six.place(relx=0.50, rely=0.40, relwidth=0.2, relheight=0.12)

button_minus = tkinter.Button(key_frame, text='-', font=('Arial', 12, 'bold'), command=lambda: btnclick('-'))
button_minus.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.12)

# row 3 buttons
button_one = tkinter.Button(key_frame, text='1', font=('Arial', 12, 'bold'), command=lambda: btnclick(1))
button_one.place(relx=0.01, rely=0.60, relwidth=0.2, relheight=0.12)

button_two = tkinter.Button(key_frame, text='2', font=('Arial', 12, 'bold'), command=lambda: btnclick(2))
button_two.place(relx=0.25, rely=0.60, relwidth=0.2, relheight=0.12)

button_three = tkinter.Button(key_frame, text='3', font=('Arial', 12, 'bold'), command=lambda: btnclick(3))
button_three.place(relx=0.50, rely=0.60, relwidth=0.2, relheight=0.12)

button_multip = tkinter.Button(key_frame, text='*', font=('Arial', 12, 'bold'), command=lambda: btnclick('*'))
button_multip.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.12)

# row 4 buttons
button_zero = tkinter.Button(key_frame, text='0', font=('Arial', 12, 'bold'), command=lambda: btnclick(0))
button_zero.place(relx=0.01, rely=0.80, relwidth=0.2, relheight=0.12)

button_equal = tkinter.Button(key_frame, text='=', font=('Arial', 12, 'bold'), command=lambda: main_execution())
button_equal.place(relx=0.25, rely=0.80, relwidth=0.2, relheight=0.12)

button_point = tkinter.Button(key_frame, text='.', font=('Arial', 12, 'bold'), command=lambda: btnclick('.'))
button_point.place(relx=0.50, rely=0.80, relwidth=0.2, relheight=0.12)

button_division = tkinter.Button(key_frame, text='/', font=('Arial', 12, 'bold'), command=lambda: btnclick('/'))
button_division.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.12)

main_window.mainloop()


