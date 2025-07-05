import tkinter as tk

# إنشاء نافذة البرنامج
root = tk.Tk()
root.title("آلة حاسبة")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#e6e6e6")

# متغير لتخزين العملية
expression = ""

# دالة لكتابة الأرقام والعمليات
def press(symbol):
    global expression
    expression += str(symbol)
    equation.set(expression)

# دالة لحساب الناتج
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("خطأ")
        expression = ""

# دالة للمسح
def clear():
    global expression
    expression = ""
    equation.set("")

# شاشة العرض
equation = tk.StringVar()
screen = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=2,
                  width=14, borderwidth=4, relief="ridge", justify='right')
screen.grid(row=0, column=0, columnspan=4, pady=20)

# أزرار الآلة الحاسبة
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

# إنشاء الأزرار
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="#4CAF50", fg="white",
                  command=equalpress).grid(row=row, column=col, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="#f44336", fg="white",
                  command=clear).grid(row=row, column=col, columnspan=4, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="#ddd", fg="black",
                  command=lambda t=text: press(t)).grid(row=row, column=col, sticky="nsew")

# تشغيل البرنامج
root.mainloop()
