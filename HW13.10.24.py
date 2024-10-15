# Задание 1
# Создайте трёхтабличную базу данных Sales(продажи). В этой базе данных должны быть
# следующие таблицы Sales (информация о конкретных продажах), Salesmen (информация о
# продавцах), Customers (информация о покупателях). Создайте приложение для отображения
# данных из таблиц. Меню приложения должно содержать такой минимальный набор отчётов:
# ■ Отображение всех сделок;
# ■ Отображение сделок конкретного продавца;
# ■ Отображение максимальной по сумме сделки;
# ■ Отображение минимальной по сумме сделки;
# ■ Отображение максимальной по сумме сделки для конкретного продавца;
# ■ Отображение минимальной по сумме сделки для конкретного продавца;
# ■ Отображение максимальной по сумме сделки для конкретного покупателя;
# ■ Отображение минимальной по сумме сделки для конкретного покупателя;
# ■ Отображение продавца, у которого максимальная сумма продаж по всем сделкам;
# ■ Отображение продавца, у которого минимальная сумма продаж по всем сделкам;
# ■ Отображение покупателя, у которого максимальная сумма покупок по всем сделкам;
# ■ Отображение средней суммы покупки для конкретного покупателя;
# ■ Отображение средней суммы покупки для конкретного продавца.

# Задание 2
# Добавьте механизмы для обновления, удаления и вставки данных в базу данных используя интерфейс
# меню. Пользователь не может ввести запросы INSERT, UPDATE, DELETE напрямую. Запретите возможность
# обновления и удаления всех данных для каждой из таблиц (UPDATE и DELETE без условий).

# Задание 3
# Добавьте к первому заданию возможность сохранения результатов фильтров в файл. Путь и название
# к файлу указываются в настройках приложения.

import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('Sales.db')
    cursor = connection.cursor()

    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS Salesmens (
    #   SalesmenId INTEGER PRIMARY KEY,
    #   FIO TEXT NOT NULL,
    #   email TEXT NOT NULL,
    #   telephone INTEGER NOT NULL
    #   );
    # ''')
    # cursor.execute('''
    #   CREATE TABLE IF NOT EXISTS Customers (
    #   CustomerId INTEGER PRIMARY KEY,
    #   FIO TEXT NOT NULL,
    #   email TEXT NOT NULL,
    #   telephone INTEGER NOT NULL
    #   );
    # ''')
    # cursor.execute('''
    #   CREATE TABLE IF NOT EXISTS Sales (
    #   SaleId INTEGER PRIMARY KEY,
    #   SalesmenId INTEGER NOT NULL,
    #   CustomerId INTEGER NOT NULL,
    #   ProductName TEXT NOT NULL,
    #   SalePrice INTEGER NOT NULL,
    #   DateTrade TEXT NOT NULL,
    #   FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId) ON DELETE RESTRICT ON UPDATE RESTRICT,
    # 	FOREIGN KEY (SalesmenId) REFERENCES Salesmens(SalesmenId) ON DELETE RESTRICT ON UPDATE RESTRICT
    #   )
    # ''')

    while True:
        print('1. Отображение всех сделок')
        print('2. Отображение сделок конкретного продавца')
        print('3. Отображение максимальной по сумме сделки')
        print('4. Отображение минимальной по сумме сделки')
        print('5. Отображение максимальной по сумме сделки для конкретного продавца')
        print('6. Отображение минимальной по сумме сделки для конкретного продавца')
        print('7. Отображение максимальной по сумме сделки для конкретного покупателя')
        print('8. Отображение минимальной по сумме сделки для конкретного покупателя')
        print('9. Отображение продавца, у которого максимальная сумма продаж по всем сделкам')
        print('10. Отображение продавца, у которого минимальная сумма продаж по всем сделкам')
        print('11. Отображение покупателя, у которого максимальная сумма покупок по всем сделкам')
        print('12. Отображение продавца, у которого минимальная сумма продаж по всем сделкам')
        print('13. Отображение средней суммы покупки для конкретного покупателя')
        print('14. Отображение средней суммы покупки для конкретного продавца')
        print('15. Обновление данных')
        print('16. Удаление данных')
        print('17. Добавление данных')
        print('18. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cursor.execute('''
                        SELECT * FROM Sales
                        JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId
                        JOIN Customers  on Sales.CustomerId = Customers.CustomerId;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '2':
            FIO = input('Введите ФИО продавца: ')
            comanda = "SELECT * FROM Sales join Salesmens on Sales.SalesmenId = Salesmens.SalesmenId WHERE Salesmens.FIO == '" + FIO + "'"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '3':
            cursor.execute('''
                        SELECT * FROM Sales
                        JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId
                        JOIN Customers  on Sales.CustomerId = Customers.CustomerId
                        group by SalePrice ORDER by SalePrice DESC LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '4':
            cursor.execute('''
                        SELECT * FROM Sales
                        JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId
                        JOIN Customers  on Sales.CustomerId = Customers.CustomerId
                        group by SalePrice ORDER by SalePrice LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '5':
            FIO = input('Введите ФИО продавца: ')
            comanda = "SELECT * FROM Sales JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId WHERE Salesmens.FIO == '" + FIO + "' group by SalePrice ORDER by SalePrice DESC LIMIT 1;"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '6':
            FIO = input('Введите ФИО продавца: ')
            comanda = "SELECT * FROM Sales JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId WHERE Salesmens.FIO == '" + FIO + "' group by SalePrice ORDER by SalePrice LIMIT 1;"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '7':
            FIO = input('Введите ФИО покупателя: ')
            comanda = "SELECT * FROM Sales JOIN Customers on Sales.CustomerId = Customers.CustomerId WHERE Customers.FIO == '" + FIO + "' group by SalePrice ORDER by SalePrice DESC LIMIT 1;"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '8':
            FIO = input('Введите ФИО покупателя: ')
            comanda = "SELECT * FROM Sales JOIN Customers on Sales.CustomerId = Customers.CustomerId WHERE Customers.FIO == '" + FIO + "' group by SalePrice ORDER by SalePrice LIMIT 1;"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '9':
            cursor.execute('''
                        SELECT Salesmens.FIO FROM Sales
                        JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId
                        group by SalePrice ORDER by SalePrice DESC LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '10':
            cursor.execute('''
                        SELECT Salesmens.FIO FROM Sales
                        JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId
                        group by SalePrice ORDER by SalePrice LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '11':
            cursor.execute('''
                        SELECT Customers.FIO FROM Sales
                        JOIN Customers  on Sales.CustomerId = Customers.CustomerId
                        group by SalePrice ORDER by SalePrice DESC LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '12':
            cursor.execute('''
                        SELECT Customers.FIO FROM Sales
                        JOIN Customers  on Sales.CustomerId = Customers.CustomerId
                        group by SalePrice ORDER by SalePrice LIMIT 1;
                        ''')
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '13':
            FIO = input('Введите ФИО покупателя: ')
            comanda = "SELECT AVG(Sales.SalePrice) FROM Sales JOIN Customers on Sales.CustomerId = Customers.CustomerId WHERE Customers.FIO = '" + FIO + "';"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '14':
            FIO = input('Введите ФИО продавца: ')
            comanda = "SELECT AVG(Sales.SalePrice) FROM Sales JOIN Salesmens on Sales.SalesmenId = Salesmens.SalesmenId WHERE Salesmens.FIO = '" + FIO + "';"
            cursor.execute(comanda)
            sales = cursor.fetchall()
            for sale in sales:
                print(sale)
        elif choice == '15':
            table = input('Введите название таблицы для обновления данных (Salesmens, Customers, Sales): ')
            if table == 'Salesmens':
                ID = int(input('Введите ИД, по которому необходимо обновить данные: '))
                answer = input('Введите False / True, если необходимо обновить ФИО: ')
                if answer == 'True':
                    FIO = input('Введите ФИО для обновления: ')
                    cursor.execute('UPDATE Salesmens SET FIO = ? WHERE SalesmenId = ?', (FIO, ID))
                answer = input('Введите False / True, если необходимо обновить email: ')
                if answer == 'True':
                    email = input('Введите email для обновления: ')
                    cursor.execute('UPDATE Salesmens SET email = ? WHERE SalesmenId = ?', (email, ID))
                answer = input('Введите False / True, если необходимо обновить телефон: ')
                if answer == 'True':
                    telephone = int(input('Введите телефон для обновления: '))
                    cursor.execute('UPDATE Salesmens SET telephone = ? WHERE SalesmenId = ?', (telephone, ID))
            elif table == 'Customers':
                ID = int(input('Введите ИД, по которому необходимо обновить данные: '))
                answer = input('Введите False / True, если необходимо обновить ФИО: ')
                if answer == 'True':
                    FIO = input('Введите ФИО для обновления: ')
                    cursor.execute('UPDATE Customers SET FIO = ? WHERE CustomerId = ?', (FIO, ID))
                answer = input('Введите False / True, если необходимо обновить email: ')
                if answer == 'True':
                    email = input('Введите email для обновления: ')
                    cursor.execute('UPDATE Customers SET email = ? WHERE CustomerId = ?', (email, ID))
                answer = input('Введите False / True, если необходимо обновить телефон: ')
                if answer == 'True':
                    telephone = int(input('Введите телефон для обновления: '))
                    cursor.execute('UPDATE Customers SET telephone = ? WHERE CustomerId = ?', (telephone, ID))
            elif table == 'Sales':
                ID = input('Введите ИД, по которому необходимо обновить данные: ')
                answer = input('Введите False / True, если необходимо обновить ИД продавца: ')
                if answer == 'True':
                    SalesmenId = int(input('Введите ИД продавца для обновления: '))
                    cursor.execute('UPDATE Sales SET SalesmenId = ? WHERE SaleId = ?', (SalesmenId, ID))
                answer = input('Введите False / True, если необходимо обновить ИД покупателя: ')
                if answer == 'True':
                    CustomerId = int(input('Введите ИД покупателя для обновления: '))
                    cursor.execute('UPDATE Sales SET CustomerId = ? WHERE SaleId = ?', (CustomerId, ID))
                answer = input('Введите False / True, если необходимо обновить наименование товара: ')
                if answer == 'True':
                    ProductName = input('Введите наименование товара для обновления: ')
                    cursor.execute('UPDATE Sales SET ProductName = ? WHERE SaleId = ?', (ProductName, ID))
                answer = input('Введите False / True, если необходимо обновить стоимость продажи: ')
                if answer == 'True':
                    SalePrice = int(input('Введите стоимость продажи для обновления: '))
                    cursor.execute('UPDATE Sales SET SalePrice = ? WHERE SaleId = ?', (SalePrice, ID))
                answer = input('Введите False / True, если необходимо обновить дату сделки: ')
                if answer == 'True':
                    DateTrade = input('Введите дату сделки для обновления: ')
                    cursor.execute('UPDATE Sales SET DateTrade = ? WHERE SaleId = ?', (DateTrade, ID))
            connection.commit()
        elif choice == '16':
            table = input('Введите название таблицы для удаления данных (Salesmens, Customers, Sales): ')
            if table == 'Salesmens':
                ID = int(input('Введите ИД, по которому необходимо удалить данные: '))
                cursor.execute('DELETE FROM Salesmens WHERE SalesmenId = ?', (ID,))
            elif table == 'Customers':
                ID = int(input('Введите ИД, по которому необходимо удалить данные: '))
                cursor.execute('DELETE FROM Customers WHERE CustomerId = ?', (ID,))
            elif table == 'Sales':
                ID = int(input('Введите ИД, по которому необходимо удалить данные: '))
                cursor.execute('DELETE FROM Sales WHERE SaleId = ?', (ID,))
            connection.commit()
        elif choice == '17':
            table = input('Введите название таблицы для добавления данных (Salesmens, Customers, Sales): ')
            if table == 'Salesmens':
                FIO = input('Введите ФИО для добавления: ')
                email = input('Введите email для обновления: ')
                telephone = int(input('Введите телефон для обновления: '))
                cursor.execute('INSERT INTO Salesmens (FIO, email, telephone) VALUES (?, ?, ?)', (FIO, email, telephone))
            elif table == 'Customers':
                FIO = input('Введите ФИО для добавления: ')
                email = input('Введите email для добавления: ')
                telephone = int(input('Введите телефон для добавления: '))
                cursor.execute('INSERT INTO Customers (FIO, email, telephone) VALUES (?, ?, ?)', (FIO, email, telephone))
            elif table == 'Sales':
                SalesmenId = int(input('Введите ИД продавца для обновления: '))
                CustomerId = int(input('Введите ИД покупателя для обновления: '))
                ProductName = input('Введите наименование товара для обновления: ')
                SalePrice = int(input('Введите стоимость продажи для обновления: '))
                DateTrade = input('Введите дату сделки для обновления: ')
                cursor.execute('INSERT INTO Sales (SalesmenId, CustomerId, ProductName, SalePrice, DateTrade) VALUES (?, ?, ?)', (SalesmenId, CustomerId, ProductName, SalePrice, DateTrade))
            connection.commit()
        elif choice == '18':
            connection.close()
            break
        else:
            print('Неверный пункт меню!')
