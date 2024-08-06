from tkinter import *

# window
window = Tk()
window.minsize(300, 250)
window.title("BMI Calculator")

my_label = Label(window, text="Enter Your Weight (kg)",font=('arial', 15, "normal"))
my_label.place(x=50, y=20)

my_entry = Entry(window, width=20)
my_entry.place(x=85,y=60)

my_label_2 = Label(window, text="Enter Your Height (cm)",font=('arial', 15, "normal"))
my_label_2.place(x=50, y=80)

my_entry_2 = Entry(window, width=20)
my_entry_2.place(x=85,y=120)

def show_entry():
    get_entry = my_entry.get()
    get_entry_2 = my_entry_2.get()
    if get_entry.replace('.', '', 1).isdigit() and get_entry_2.replace('.', '', 1).isdigit():
        my_weight = float(get_entry)
        my_height = float(get_entry_2)/100
        if my_weight <= 0 or my_height <= 0:
            output_label.config(text="Values must be greater than 0!", font=('arial', 12, "normal"))
        else:
            bmi_value = my_weight / (my_height ** 2)
            if bmi_value < 16.0:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nSeverly Underweight",font=('arial', 15, "normal"))
            elif 16.0 < bmi_value < 18.4:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nUnderweight",font=('arial', 15, "normal"))
            elif 18.5 < bmi_value < 24.9:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nNormal",font=('arial', 15, "normal"))
            elif 25.0 < bmi_value < 29.9:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nOverweight",font=('arial', 15, "normal"))
            elif 30 < bmi_value < 34.9:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nModerately Obese",font=('arial', 15, "normal"))
            elif 35 < bmi_value < 39.9:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nSeverly Obese",font=('arial', 15, "normal"))
            elif bmi_value >= 40:
                output_label.config(text=f"BMI Score is:{bmi_value:.2f} \nMorbidly Obese",font=('arial', 15, "normal"))
    else:
        output_label.config(text="Enter valid numbers!", font=('arial', 15, "normal"))

my_button = Button(window, text="Calculate",command=show_entry)
my_button.place(x=115, y=150)

output_label = Label(window, text="",font=('arial', 15, "normal"))
output_label.place(x=50, y=180)

window.mainloop()