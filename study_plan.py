"""План подготовки лабораторной №1 для варианта 3."""


def format_plan():
    tasks = [
        ("Среднее 3", "Добавить Python-файл и сохранить коммит"),
        ("Среднее 5", "Создать feature и добавить новый файл"),
        ("Среднее 9", "Отправить ветки на GitHub"),
        ("Повышенное 3", "Открыть Pull Request из feature в main"),
        ("Повышенное 7", "Опубликовать тег релиза на GitHub"),
    ]
    return "\n".join(f"{number}. {level}: {task}" for number, (level, task)
                     in enumerate(tasks, start=1))


if __name__ == "__main__":
    print(format_plan())
