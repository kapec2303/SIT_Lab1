from abc import ABC, abstractmethod


# Абстрактная фабрика
# интерфейс для создания семейств взаимосвязанных или взаимозависимых объектов,
# не специфицируя их конкретных классов.
# Шаблон реализуется созданием абстрактного класса Factory,
# который представляет собой интерфейс для создания компонентов системы

class UIFactory(ABC):
    @abstractmethod
    def create_button(self, name: str):
        pass

    @abstractmethod
    def create_checkbox(self, name: str):
        pass


class WindowsFactory(UIFactory):
    def create_button(self, name: str):
        return WindowsButton(name)

    def create_checkbox(self, name: str):
        return WindowsCheckbox(name)


class MacFactory(UIFactory):
    def create_button(self, name: str):
        return MacButton(name)

    def create_checkbox(self, name: str):
        return MacCheckbox(name)


# Паттерн Компоновщик
# Объединяет объекты в древовидную структуру для представления иерархии от частного к целому.
# Компоновщик позволяет клиентам обращаться к отдельным объектам и к группам объектов одинаково.

class UIComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    def add(self, component: "UIComponent"):
        raise NotImplementedError("Нельзя добавить в лист")

    def remove(self, component: "UIComponent"):
        raise NotImplementedError("Нельзя удалить из листа")

    @abstractmethod
    def render(self, indent=0):
        pass


# Листья
class Button(UIComponent):
    pass


class Checkbox(UIComponent):
    pass


class WindowsButton(Button):
    def render(self, indent=0):
        print(" " * indent + f"WindowsButton: {self.name}")


class MacButton(Button):
    def render(self, indent=0):
        print(" " * indent + f"MacButton: {self.name}")


class WindowsCheckbox(Checkbox):
    def render(self, indent=0):
        print(" " * indent + f"WindowsCheckbox: {self.name}")


class MacCheckbox(Checkbox):
    def render(self, indent=0):
        print(" " * indent + f"MacCheckbox: {self.name}")


# Контейнер
class UIContainer(UIComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []

    def add(self, component: UIComponent):
        self.children.append(component)

    def remove(self, component: UIComponent):
        self.children.remove(component)

    def render(self, indent=0):
        print(" " * indent + f"Container: {self.name}")
        for child in self.children:
            child.render(indent + 4)


# Клиент

def create_ui(factory: UIFactory):
    root = UIContainer("Главное окно")

    header = factory.create_button("Кнопка меню")
    root.add(header)

    settings_panel = UIContainer("Панель настроек")
    settings_panel.add(factory.create_checkbox("Тёмная тема"))
    settings_panel.add(factory.create_button("Сохранить"))

    root.add(settings_panel)

    return root


if __name__ == "__main__":
    print("=== Windows UI ===")
    windows_ui = create_ui(WindowsFactory())
    windows_ui.render()

    print("\n=== Mac UI ===")
    mac_ui = create_ui(MacFactory())
    mac_ui.render()
