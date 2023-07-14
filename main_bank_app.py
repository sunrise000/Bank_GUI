from tkinter import *

from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.window = window
        self.window.title("Bank app ")
        self.window.geometry("300x266")
        self.window.config(background= "#1AA7EC")

        # balance withdrawal limit
        self.balance_value = 15000.00
        self.withdrawal_limit = 5000.00

        # Account type selection
        self.account_type_label = Label(window, text="select your account type", bg="#4ADEDE")
        self.account_type_label.pack()

        self.account_type_var = StringVar()
        self.account_type_var.set("savings")

        # savings button
        self.savings_rd = Radiobutton(window, text="Savings", bg="#4ADEDE", variable=self.account_type_var, value="savings", command=self.update_buttons, highlightthickness=0,  font=("Arial", 12, "italic"))
        self.savings_rd.pack()

        # Current button
        self.current_rd = Radiobutton(window, text="Current", bg="#4ADEDE", variable=self.account_type_var, value="current", command=self.update_buttons, highlightthickness=0,  font=("Arial", 12, "italic"))
        self.current_rd.pack()

        # Balance
        self.balance_lbl = Label(window, text=f"Balance: {self.balance_value}\nWithdrawal/deposit limit\n{self.withdrawal_limit}", bg="#4ADEDE", font=("Arial", 12, "italic"))
        self.balance_lbl.pack()

        # withdraw button
        self.withdrawal_btn = Button(master=window, text="Withdrawal", command=self.withdrawal, highlightthickness=0, bg="#4ADEDE")
        self.withdrawal_btn.pack()

        # Deposit button
        self.deposit_btn = Button(master=window, text="   Deposit   ", bg="#4ADEDE", command=self.deposit, highlightthickness=0)
        self.deposit_btn.pack()
        # Amount entry
        self.amount_entry = Entry(window)
        self.amount_entry.pack()


    def update_buttons(self):
        account_type = self.account_type_var.get()
        if account_type == "Savings":
            self.withdrawal_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.withdrawal_limit = 30000
        elif account_type == "current":
            self.withdrawal_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.deposit_btn.config(state=NORMAL)
            self.withdrawal_limit = float("int")

    def withdrawal(self):
        amount = float(self.amount_entry.get())
        if amount <= self.withdrawal_limit and amount <= self.balance_value:
            self.balance_value -= amount
            self.update_balance_label()
        elif amount > self.withdrawal_limit:
            messagebox.showerror("issue", "limit exceeded")
        else:
            messagebox.showerror("issue", "Not sufficient funds")

    def deposit(self):
        amount = float(self.amount_entry.get())
        self.balance_value += amount
        self.update_balance_label()

    def update_balance_label(self):
        self.balance_lbl.config(text="Balance: $" + str(self.balance_value))

window = Tk()
app = BankApp(window)
main_lbl = Label(master=window, text="SunRize holdings plc", bg="#4ADEDE")
main_lbl.pack()
window.mainloop()
