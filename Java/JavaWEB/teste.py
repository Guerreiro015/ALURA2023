import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_pay()
        return total_payroll

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Salão de Beleza")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Nome:")
        self.name_label.pack(side="left")

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side="left")

        self.hours_worked_label = tk.Label(self, text="Horas trabalhadas:")
        self.hours_worked_label.pack(side="left")

        self.hours_worked_entry = tk.Entry(self)
        self.hours_worked_entry.pack(side="left")

        self.hourly_rate_label = tk.Label(self, text="Taxa horária:")
        self.hourly_rate_label.pack(side="left")

        self.hourly_rate_entry = tk.Entry(self)
        self.hourly_rate_entry.pack(side="left")

        self.add_employee_button = tk.Button(self, text="Adicionar funcionário", command=self.add_employee)
        self.add_employee_button.pack(side="left")

        self.calculate_payroll_button = tk.Button(self, text="Calcular folha de pagamento", command=self.calculate_payroll)
        self.calculate_payroll_button.pack(side="left")

        self.quit_button = tk.Button(self, text="Sair", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="right")

    def add_employee(self):
        name = self.name_entry.get()
        hours_worked = float(self.hours_worked_entry.get())
        hourly_rate = float(self.hourly_rate_entry.get())

        employee = Employee(name, hours_worked, hourly_rate)
        payroll.add_employee(employee)

        self.name_entry.delete(0, tk.END)
        self.hours_worked_entry.delete(0, tk.END)
        self.hourly_rate_entry.delete(0, tk.END)

    def calculate_payroll(self):
        total_payroll = payroll.calculate_total_payroll()
        tk.messagebox.showinfo("Folha de pagamento", f"O salão de beleza pagou um total de R${total_payroll:.2f} em salários.")

payroll = Payroll()

root = tk.Tk()
app = Application(master=root)
app.mainloop()