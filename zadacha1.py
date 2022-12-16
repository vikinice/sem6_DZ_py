# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


test_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
print(f"список: {test_list}")
test_item = input("Ищем: ")


def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):                          
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1


print(f"ответ: {check_list(test_list, test_item)}")