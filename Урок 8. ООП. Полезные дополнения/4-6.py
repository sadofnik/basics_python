from time import sleep
# Необходимо установить pip install translate через terminal
from translate import Translator

translator = Translator(to_lang="ru")


class Office:
    office_data = [f"\nПодразделения компании",
                   ["Выход", "Главный офис", "Отдел продаж", "Отдел закупок", "Бухгалтерия", "Служба безопасности"]]

    def __init__(self, office_name):
        self.office_name = office_name


class Warehouse:
    """Несколько базовых значений для итоговой проверки, удалить значения после написания кода"""
    data = {'printer': [{'Company': 'xerox', 'Model': "XX2", 'Price': 123.00, 'Quantity': 1},
                        {'Company': 'canon', 'Model': "XX23", 'Price': 143.00, 'Quantity': 10}],
            'scanner': [{'Company': 'Samsung', 'Model': "SSG1", 'Price': 123.00, 'Quantity': 1},
                        {'Company': 'Xerox', 'Model': "SSG2", 'Price': 143.00, 'Quantity': 10}],
            'xerox': [{'Company': 'Canon', 'Model': "XSSG2", 'Price': 143.00, 'Quantity': 10},
                      {'Company': 'Samsung', 'Model': "XSSG12", 'Price': 123.00, 'Quantity': 1}]}
    dict_model = {'printer': ["XX2", "XX23"], 'scanner': ["SSG1", "SSG2"], 'xerox': ["XSSG2", "XSSG12"]}

    def __init__(self, type_equip, company_name, model, price, amount):
        self.type_equip = type_equip
        self.company_name = company_name
        self.model = model
        self.price = price
        self.amount = amount

    @staticmethod
    def select_type_device():
        """Метод интеракивного выбора оборудования"""
        l = ["printer", "scanner", "xerox"]
        for e, el in enumerate(l, 1):
            print(e, el)
        return l[int(input("Введите значение: ")) - 1]

    @staticmethod
    def quest():
        """Меню ввода оборудования"""
        try:
            exit_quest = input("Нажмите Enter (для выхода введите 'q'): ")
            if exit_quest == 'q':
                start_func()
            else:
                t = Warehouse.select_type_device()
                f = input("Название фирмы: ").title()
                m = input(f"Название Модели: ").upper()
                p = float(input("Цена за шт.: "))
                a = int(input("Количество: "))
                Warehouse(t, f, m, p, a).update_device_dict()
        except ValueError:
            print("Введены некорректные данные.")
            return Warehouse.quest()

    def update_device_dict(self):
        """Проверка наличия техники в базе, если нет - создание новой записи"""
        if self.model not in self.dict_model.get(self.type_equip):
            self.data.get(self.type_equip).append(
                {'Firm': self.company_name, 'Model': self.model, 'Price': self.price, 'Amount': self.amount})
            self.dict_model.get(self.type_equip).append(self.model)
        else:
            """temp_var - временная переменная для упрощения кода"""
            temp_var = self.data.get(self.type_equip)[self.dict_model.get(self.type_equip).index(self.model)]
            temp_var.update(
                {'Price': temp_var.get('Price') + self.price, 'Amount': temp_var.get('Amount') + self.amount})
        return Warehouse.quest()


class OfficeEquipment(Warehouse):
    def __init__(self, type_equip, company_name, model, price, amount):
        super().__init__(type_equip, company_name, model, price, amount)

    @staticmethod
    def all_equip():
        """Метод запуска отчётов"""
        q = OfficeEquipment.quest()
        if q == 0:
            start_func()
        if q == 1:
            OfficeEquipment.report_all()
        if q == 2:
            Printer.report_printer()
        if q == 3:
            Scanner.report_scanner()
        if q == 4:
            Xerox.report_xerox()

    @staticmethod
    def quest():
        """Меню отчётов"""
        try:
            i = ["Выход", "Полный отчёт", "Отчёт по принтерам", "Отчёт по сканерам", "Отчёт по Ксероксам"]
            for e, el in enumerate(i, 0):
                print(e, el)
            q = int(input("Введите значение: "))
            if q > len(i):
                print(f"\nВы ввели недопустимое значение.")
                sleep(1)
                OfficeEquipment.quest()
            return q
        except ValueError:
            print(f"\nВведены некорректные данные.")
            sleep(1)
            OfficeEquipment.quest()

    @classmethod
    def report_all(cls):
        """Отчёты по всей технике"""
        for i in OfficeEquipment.data.keys():
            print(f"{translator.translate(i)}")
            for el in OfficeEquipment.data.get(i):
                for k, j in el.items():
                    print(f"    {translator.translate(k):<10}: {j}")
        OfficeEquipment.all_equip()


class Printer(OfficeEquipment):
    def __init__(self, type_equip, company_name, model, price, amount, speed_page):
        super().__init__(type_equip, company_name, model, price, amount)
        self.speed_page = speed_page

    @classmethod
    def report_printer(cls):
        """Отчёты по принтерам"""
        print(f"{translator.translate('printer')}")
        for el in OfficeEquipment.data.get('printer'):
            for k, j in el.items():
                print(f"    {translator.translate(k):<10}: {j}")
        OfficeEquipment.all_equip()


class Scanner(OfficeEquipment):
    def __init__(self, type_equip, company_name, model, price, amount, interface):
        super().__init__(type_equip, company_name, model, price, amount)
        self.interface = interface

    @classmethod
    def report_scanner(cls):
        """Отчёты по сканерам"""
        print(f"{translator.translate('scanner')}")
        for el in OfficeEquipment.data.get('scanner'):
            for k, j in el.items():
                print(f"    {translator.translate(k):<10}: {j}")
        OfficeEquipment.all_equip()


class Xerox(OfficeEquipment):
    def __init__(self, type_equip, company_name, model, price, amount):
        super().__init__(type_equip, company_name, model, price, amount)

    @classmethod
    def report_xerox(cls):
        """Отчёты по ксероксам"""
        print(f"{translator.translate('xerox')}")
        for el in OfficeEquipment.data.get('xerox'):
            for k, j in el.items():
                print(f"    {translator.translate(k):<10}: {j}")
        OfficeEquipment.all_equip()


def home_menu():
    """Фунеция домашнего меню"""
    try:
        for i, el in enumerate(menu_list[1]):
            print(i, el)
        user_input = int(input("Введите номер: "))
        if user_input > len(menu_list[1]):
            raise ValueError
        return user_input
    except ValueError:
        print("Введены некорректные данные.")
        sleep(1)
        return start_func()


def test_func():
    print("Данный функционал в разработке \nВы будете перенаправлены в Главное меню.")
    sleep(2)
    start_func()


def start_func():
    """Функция запуска разделов Главного меню"""
    q = home_menu()
    if q == 0:
        print("Завершение работы программы.")
    elif q == 1:
        Warehouse.quest()
    elif q == 2:
        print("Функционал в разработке")
        sleep(1)
        start_func()
    elif q == 3:
        print("Функционал в разработке")
        sleep(1)
        start_func()
    elif q == 4:
        OfficeEquipment.all_equip()


menu_list = ["Главное меню", ["Выход", "Приём техники", "Распределение техники по офису - (В разработке)",
                              "Списание техники - (В разработке)", "Отчёты"]]

start_func()
print(OfficeEquipment.data.get('printer'))
print(OfficeEquipment.dict_model)
