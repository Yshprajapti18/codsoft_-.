import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Add":
        result.set(num1 + num2)
    elif operation == "Subtract":
        result.set(num1 - num2)
    elif operation == "Multiply":
        result.set(num1 * num2)
    elif operation == "Divide":
        if num2 == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(num1 / num2)
    elif operation == "Power":
        result.set(num1 ** num2)

app = tk.Tk()
app.title("Simple Calculator")

entry_num1 = tk.Entry(app, width=15)
entry_num2 = tk.Entry(app, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num2.grid(row=0, column=2, padx=10, pady=5)

operations = ["Add", "Subtract", "Multiply", "Divide", "Power"]
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(app, operation_var, *operations)
operation_menu.grid(row=0, column=1, padx=10, pady=5)

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

result = tk.StringVar()
result_label = tk.Label(app, text="Result:")
result_value = tk.Label(app, textvariable=result)
result_label.grid(row=2, column=0, padx=10, pady=5)
result_value.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

app.mainloop()
