class Company:
        def __init__(self, company_bank, company_name):
                self.company_bank = company_bank
                self.company_name = company_name

class Person(Company):
        def __init__(self, company_bank, company_name, first_name, last_name, salary):
                super().__init__(company_bank, company_name)
                self.first_name = first_name
                self.last_name = last_name
                self.salary = salary
        
        def get_salary(self):
                if self.salary > self.company_bank:
                        print(f'У компании {self.company_name} недостаточно средств!')
                else:
                        b = self.company_bank - self.salary
                        print(f'Остаток средств компании {b}')
        def person_info(self):
                print(f'{self.first_name} {self.last_name} {self.salary}')

person = Person(int(input('Company\'s money: ')), 'OptimaBank', 'Jonh', 'Mrs', int(input('Зарплата сотрудника: ')))
person.get_salary()
person.person_info()