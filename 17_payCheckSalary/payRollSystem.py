import csv

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Palkkalaskelma')
            print('==============')
            print(f'Henkilölle: {employee.id} - {employee.name}')
            print(f'- Maksetaan: {format(employee.calculate_salary(), ".2f")}')
            print('')

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.commission = commission

    def calculate_salary(self):
        return super().calculate_salary() + self.commission

def my_join(words, separator):
    result = []
    for i, word in enumerate(words):
        if i > 0:
            result.append(separator)
        result.append(str(word))
    return ''.join(result)

def write_employees_to_csv(employees, filename='employee.csv'):
    with open(filename, mode='w') as file:
        for employee in employees:
            if isinstance(employee, SalaryEmployee) and not isinstance(employee, CommissionEmployee):
                row = (employee.id), employee.name, 'M', float(employee.monthly_salary)
            elif isinstance(employee, HourlyEmployee):
                row = (employee.id), employee.name, 'H', float(employee.hours_worked), float(employee.hour_rate)
            elif isinstance(employee, CommissionEmployee):
                row = (employee.id), employee.name, 'C', float(employee.monthly_salary), float(employee.commission)
            file.write(my_join(row, ',') + '\n')

def read_employees_from_csv(filename='employee.csv'):
    employees = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            id, name, emp_type = row[0], row[1], row[2]
            if emp_type == 'M':
                employees.append(SalaryEmployee(id, name, float(row[3])))
            elif emp_type == 'H':
                employees.append(HourlyEmployee(id, name, float(row[3]), float(row[4])))
            elif emp_type == 'C':
                employees.append(CommissionEmployee(id, name, float(row[3]), float(row[4])))
    return employees

def main():
    employees = []
    payroll = PayrollSystem()

    while True:
        print("(1) Lisää työntekijöitä")
        print("(2) Kirjoita työntekijät tiedostoon")
        print("(3) Lue työntekijät tiedostosta")
        print("(4) Tulosta palkkalaskelma")
        print("(0) Lopeta\n")

        choice = input("Valitse toiminto: ")

        if choice == '1':
            while True:
                print("Anna palkkatyyppi:")
                print("(1) Kuukausi")
                print("(2) Tunti")
                print("(3) Komissio")
                print("(0) Lopeta")
                emp_type = input()
                if emp_type == '0':
                    break
                name = input("Anna työntekijän nimi:")
                if emp_type == '1':
                    salary = float(input("Anna kuukausipalkka:").replace(',', '.'))
                    employees.append(SalaryEmployee(len(employees)+1, name, salary))
                elif emp_type == '2':
                    hours = int(input("Anna tehdyt tunnit:"))
                    rate = float(input("Anna tuntipalkka:").replace(',', '.'))
                    employees.append(HourlyEmployee(len(employees)+1, name, rate, hours))
                elif emp_type == '3':
                    salary = float(input("Anna kuukausipalkka:").replace(',', '.'))
                    commission = float(input("Anna komissio:").replace(',', '.'))
                    employees.append(CommissionEmployee(len(employees)+1, name, salary, commission))

        elif choice == '2':
            write_employees_to_csv(employees)
            print(f"{len(employees)}  työntekijä(ä) lisätty tiedostoon employee.csv")

        elif choice == '3':
            employees = read_employees_from_csv()
            print(f"{len(employees)}  työntekijä(ä) luettu tiedostosta employee.csv")

        elif choice == '4':
            payroll.calculate_payroll(employees)

        elif choice == '0':
            print("Palvelu suljetaan, kiitos.")
            break

if __name__ == "__main__":
    main()