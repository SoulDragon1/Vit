class Employee:
    def __init__(self, name, emp_id):
        self._name = name  # инкапсуляция, атрибуты защищены
        self._emp_id = emp_id

    def get_info(self):
        return f"Employee Name: {self._name}, ID: {self._emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        # Вызов конструктора родительского класса
        Employee.__init__(self, name, emp_id)  
        self._department = department

    def manage_project(self, project_name):
        return f"Managing project: {project_name} in the {self._department} department"

    def get_info(self):
        return super().get_info() + f", Department: {self._department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        # Вызов конструктора родительского класса
        Employee.__init__(self, name, emp_id)  
        self._specialization = specialization

    def perform_maintenance(self, task):
        return f"Performing maintenance task: {task} in the field of {self._specialization}"

    def get_info(self):
        return super().get_info() + f", Specialization: {self._specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        # Вызов конструкторов обоих родителей с нужными аргументами
        Manager.__init__(self, name, emp_id, department)  # Инициализируем атрибуты менеджера
        Technician.__init__(self, name, emp_id, specialization)  # Инициализируем атрибуты техника
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        team_info = "Team Info:\n"
        for subordinate in self.subordinates:
            team_info += subordinate.get_info() + "\n"
        return team_info

    def get_info(self):
        return super().get_info() + f", Department: {self._department}, Specialization: {self._specialization}"


# Создание сотрудников
emp1 = Employee("John Doe", 101)
manager1 = Manager("Alice Smith", 102, "Marketing")
technician1 = Technician("Bob Brown", 103, "Software Engineering")

# Создание TechManager и добавление сотрудников в команду
tech_manager = TechManager("Eve White", 104, "IT", "Network Administration")
tech_manager = TechManager("Eve Black", 105, "IT", "Network Protect")
tech_manager.add_employee(manager1)
tech_manager.add_employee(technician1)

# Демонстрация функциональности
print(emp1.get_info())  # Информация о базовом сотруднике
print(manager1.get_info())  # Информация о менеджере
print(manager1.manage_project("New Website"))  # Менеджер управляет проектом
print(technician1.get_info())  # Информация о техническом специалисте
print(technician1.perform_maintenance("Server Update"))  # Техник выполняет обслуживание
print(tech_manager.get_info())  # Информация о тех-менеджере
print(tech_manager.manage_project("System Upgrade"))  # Тех-менеджер управляет проектом
print(tech_manager.perform_maintenance("Router Replacement"))  # Тех-менеджер выполняет техническое обслуживание

# Информация о команде тех-менеджера
print(tech_manager.get_team_info())  # Выводим информацию о подчинённых
