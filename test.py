def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历tuple中所有项目
    for single_item in numbers:
        print('tuple:', single_item)
    
    # 遍历dict中所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, jack=1123, john=2231, inge=1460))
