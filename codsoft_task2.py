import tkinter as tk

calculation = ""
def add_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear()
        text_result.insert(1.0,"Error")
def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0 ,"end")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

text_result  = tk.Text(root, height=2, width=16, font=("gintronic", 24))
text_result.grid(columnspan=5)

bt_1 = tk.Button(root, text="1", command=lambda: add_calc(1), width=5, font=("gintronic",14))
bt_1.grid(column=1, row=2)

bt_2 = tk.Button(root, text="2", command=lambda: add_calc(2), width=5, font=("gintronic",14))
bt_2.grid(column=2, row=2)

bt_3 = tk.Button(root, text="3", command=lambda: add_calc(3), width=5, font=("gintronic",14))
bt_3.grid(column=3, row=2)

bt_4 = tk.Button(root, text="4", command=lambda: add_calc(4), width=5, font=("gintronic",14))
bt_4.grid(column=1, row=3)

bt_5 = tk.Button(root, text="5", command=lambda: add_calc(5), width=5, font=("gintronic",14))
bt_5.grid(column=2, row=3)

bt_6 = tk.Button(root, text="6", command=lambda: add_calc(6), width=5, font=("gintronic",14))
bt_6.grid(column=3, row=3)

bt_7 = tk.Button(root, text="7", command=lambda: add_calc(7), width=5, font=("gintronic",14))
bt_7.grid(column=1, row=4)

bt_8 = tk.Button(root, text="8", command=lambda: add_calc(8), width=5, font=("gintronic",14))
bt_8.grid(column=2, row=4)

bt_9 = tk.Button(root, text="9", command=lambda: add_calc(9), width=5, font=("gintronic",14))
bt_9.grid(column=3, row=4)

bt_0 = tk.Button(root, text="0", command=lambda: add_calc(0), width=5, font=("gintronic",14))
bt_0.grid(column=2, row=5)

bt_p = tk.Button(root, text="+", command=lambda: add_calc("+"), width=5, font=("gintronic",14))
bt_p.grid(column=4, row=2)

bt_s = tk.Button(root, text="-", command=lambda: add_calc("-"), width=5, font=("gintronic",14))
bt_s.grid(column=4, row=3)

bt_m = tk.Button(root, text="*", command=lambda: add_calc("*"), width=5, font=("gintronic",14))
bt_m.grid(column=4, row=4)

bt_d = tk.Button(root, text="/", command=lambda: add_calc("/"), width=5, font=("gintronic",14))
bt_d.grid(column=4, row=5)

bt_op = tk.Button(root, text="(", command=lambda: add_calc("("), width=5, font=("gintronic",14))
bt_op.grid(column=1, row=5)

bt_cp = tk.Button(root, text=")", command=lambda: add_calc(")"), width=5, font=("gintronic",14))
bt_cp.grid(column=3, row=5)

bt_eq = tk.Button(root, text="=", command=evaluate, width=11, font=("gintronic",14))
bt_eq.grid(column=3, row=6, columnspan=2)

bt_clear = tk.Button(root, text="C", command=clear, width=11, font=("gintronic",14), bg='Gold')
bt_clear.grid(column=1, row=6, columnspan=2)
root.mainloop()