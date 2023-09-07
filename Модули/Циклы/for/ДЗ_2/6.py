educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы: '))
total_expense = 0
total_cashup = 0
for i in range(10):
    total_cashup += educational_grant
    total_expense += expenses
    expenses *= 1.03
    print(f"Месяц траты {int(expenses)}, не хватает {int(expenses - educational_grant)}")
print('У родителей нужно попросить: ',total_expense-total_cashup)
