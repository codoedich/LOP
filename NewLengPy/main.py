from Lekser import Lekser
from Parc import Parc
from InterPrit import InterPrit
code0 = ["a = ( 6 + 7 * ( 6 - 5 ) - 2 ) * 2 - 20 ; ",
         "PRINT ( a ) ;",
         "WHILE ( a < 10 ) { a = a + 3 ; PRINT ( a ) ; } ;",
         "b = 6 / a ;",
         "IF ( 40 > b ) { PRINT ( b ) ; } ;",
         "PRINT ( b ) ;",
         ]
code1 = ["LinkedList link_list = { 1 , 3 , 4 } ;",
         "link_list .insertAtEnd ( 2 ) ;",
         "link_list .insertAtHead ( 1 ) ;",
         "link_list .delete ( 2 ) ;",
         "link_list .deleteAtHead ( ) ;",
         "link_list .search ( 2 ) ;",
         "link_list .isEmpty ( ) ;"
        ]


def get_code():
    code = list()
    while True:
        line = input("Введите строку кода: ")
        if line:
            code.append(line)
        else:
            break
    print(f"Введено строк: {len(code)}\n")
    return code


def main():

    # ввод нужного кода
    # code = get_code()

    # лексический поиск
    lexer = Lekser(code0)

    # вывод строк кода
    # print(code)

    # анализирование лексем
    lexer.analise()

    # вывод списка лексем
    lexemes = lexer.get()

    # вывод всех лексемы
    # lexer.show()

    # вывод объектов для парсинга
    parser = Parc(lexemes)

    # старт парсинга
    parser.parse()

    # получение список НОДов
    node_list = parser.NodList()

    # вывод объектов для запуска
    inter = InterPrit(node_list)

    # - COMMANDER CODY, THE TIME HAS COME... EXECUTE ORDER 66
    # - Yes, my Lord
    inter.ORDER66()

    # вывести все переменные
    # print(inter.linkedlist_values)

    # вывести все LL переменные
    # print(inter.variables_values)


if __name__ == '__main__':
    main()
