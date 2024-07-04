import tkinter as tk

def calculate():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    height = height/100
    bmi = weight/(height*height)
    bmi_result.config(text="Your BMI : {:.2f}".format(bmi))
    
    if bmi <= 18.4:
        status.config(text="Status : Underweight", fg="#E4080A")
    elif bmi > 18.5 and bmi < 24.9 :
        status.config(text="Status : Normal", fg="#67E535")
    elif bmi > 25.0 and bmi < 39.9 :
        status.config(text="Status : Overweight", fg="#E4080A")
    else :
        status.config(text="Status : Obese", fg="#E4080A")
        
    
    
    
def clear():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
   

b = "#A783FA"
f = "#000000"

canvas = tk.Tk()
canvas.title("BMI Calculator")
canvas.geometry("350x350")
canvas.config(bg=b)
canvas.resizable(0,0)

label_weight = tk.Label(canvas, text="weight (kg) :", font=("Poppins",15,"bold"), bg=b)
label_weight.pack(pady=10)

entry_weight = tk.Entry(canvas, font=("Poppins",15))
entry_weight.pack()

label_height = tk.Label(canvas, text="height (cm) :", font=("Poppins",15,"bold"), bg=b)
label_height.pack(pady=15)

entry_height = tk.Entry(canvas, font=("Poppins",15))
entry_height.pack()

#frame for button
frame = tk.Frame(canvas)
frame.pack(pady=30)
frame.config(bg=b)

calculate_button = tk.Button(frame, text="calculate", font=("Poppins",15), activebackground=b, activeforeground=f, command=calculate)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(frame, text="clear", font=("Poppins",15), activebackground=b, activeforeground=f, command=clear)
clear_button.grid(row=0, column=1, padx=10)

bmi_result = tk.Label(canvas, text="", font=("Poppins", 15))
bmi_result.config(bg=b)
bmi_result.pack()

status = tk.Label(canvas, text="", font=("Poppins", 15))
status.config(bg=b)
status.pack(pady=10)



canvas.mainloop()