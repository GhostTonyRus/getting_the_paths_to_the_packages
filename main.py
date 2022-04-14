import subprocess  # для работы в терминале
from pathlib import Path  # для того, чтобы опредедлить путь к созданному файлу


def get_installed_packages():
    """В ДАННОЙ ФУНКЦИИ ВЫПОЛНЯЕМ ФУНКЦИЮ В ТЕРМИНАЛЕ, ЧТОБЫ ПОЛУЧИТЬ
    СПИСОК УСТАНВОЛЕННЫХ ПАКЕТОВ"""
    args = ["dpkg-query", "-f`${binary:Package}\n`", "-W"]  # аргументы
    process = subprocess.Popen(args, stdout=subprocess.PIPE)  # вызываем функцию
    data = process.communicate(timeout=1)
    res = data[0].decode("utf-8").replace("`", "")  # получаем результаты
    list_of_packages = res.split("\n")  # формируем список полученных пакетов
    return list_of_packages  # возвращаем список полученных пакетов


def get_path():
    """В ДАННОЙ ФУНКЦИИ ПОЛУЧАЕМ ПУТИ КАЖДОГО УСТАНОВЛЕННОГО ПАКЕТА"""
    packages = get_installed_packages()  # вызываем функцию, которая возвращает список пакетов
    path = ""  # переменная для сохранения результата и дальнейшего использования
    for i in packages:  # используем цикл. чтобы пробежаться по каждому элементу в писке
        args = ["which", f"{i}"]  # команда which будет применяться к каждому элементу в списке
        process = subprocess.Popen(args, stdout=subprocess.PIPE)  # вызываем функцию
        data = process.communicate(timeout=1)
        res = data[0].decode("utf-8")  # получаем результаты
        path += res  # сохраняем результаты в переменную
    return path  # возвращаем переменную


def write_to_file(data):
    """ДАННАЯ ФУНКЦИЯ ПРИНИМАЕТ ДАННЫЕ С ПУТЯМИ К ФАЙЛАМ И ЗАПИСЫВАЕТ ИХ В ФАЙЛ"""
    file_path = Path(__file__)
    try:
        with open("packages_list.txt", "w") as file:  # открываем файл на запись
            file.write(data)  # записываем данные в файл
            print("Data has been successfully recorded!")
            print(f"Path file: {file_path}")
    except FileExistsError as err:  # отлавливаем ошибку
        print(f"Ошибка: {err}")  # сообщение об ошибке


def main():
    """ГЛАВНАЯ ФУНКЦИЯ"""
    write_to_file(get_path())


if __name__ == '__main__':
    # точка входа в скрипт
    main()
