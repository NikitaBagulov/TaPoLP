from enum import Enum
import json


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_child(self)

    def add_child(self, child: "Widget"):
        self.children.append(child)

    def to_json(self):
        
        if self.__class__.__name__ == "MainWindow":
            return json.dumps({
            "mw":[[child.to_json() for child in self.children],self.title]})
        elif self.__class__.__name__ == "Layout":
            return {
            "l": [[child.to_json() for child in self.children], 1 if self.alignment == Alignment.HORIZONTAL else 2]}
        elif self.__class__.__name__ == "LineEdit":
            return {
            "le": [[child.to_json() for child in self.children], self.max_length]}
        elif self.__class__.__name__ == "ComboBox":
            return {
            "cb": [[child.to_json() for child in self.children], self.items]}


    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        class_type = list(data.keys())[0]
        if class_type == 'mw':
            title = data['mw'][1]
            instance = MainWindow(title)
            for child_data in data['mw'][0]:
              child_instance = cls.from_json(json.dumps(child_data))  # Рекурсивно создаем объекты для дочерних элементов
              instance.add_child(child_instance)
        elif class_type == 'l':
            alignment = Alignment.HORIZONTAL if data['l'][1]==1 else Alignment.VERTICAL
            instance = Layout(None, alignment)
            for child_data in data['l'][0]:
              child_instance = cls.from_json(json.dumps(child_data))  # Рекурсивно создаем объекты для дочерних элементов
              instance.add_child(child_instance)
        elif class_type == 'le':
            max_length = data['le'][1]
            instance = LineEdit(None, max_length)
            for child_data in data['le'][0]:
              child_instance = cls.from_json(json.dumps(child_data))  # Рекурсивно создаем объекты для дочерних элементов
              instance.add_child(child_instance)
        elif class_type == 'cb':
            items = data['cb'][1]
            instance = ComboBox(None, items)
            for child_data in data['cb'][0]:
              child_instance = cls.from_json(json.dumps(child_data))  # Рекурсивно создаем объекты для дочерних элементов
              instance.add_child(child_instance)
        else:
            raise ValueError(f"Unknown type: {class_type}")

        return instance

    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)


class MainWindow(Widget):
    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):
    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):
    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length


class ComboBox(Widget):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
# print(app.to_json())
layout1 = Layout(app, Alignment.HORIZONTAL)
# print(layout1.to_json())
layout2 = Layout(app, Alignment.VERTICAL)
# print(layout2.to_json())

edit1 = LineEdit(layout1, 20)
# print(edit1.to_json())
edit2 = LineEdit(layout1, 30)
# print(edit2.to_json())

box1 = ComboBox(layout2, [1, 2, 3, 4])
# print(box1.to_json())
box2 = ComboBox(layout2, ["a", "b", "c"])
# print(box2.to_json())
print(app)
print(app.to_json())

json_data = app.to_json()
print(len(json_data))

new_app = Widget.from_json(json_data)
print(new_app)
