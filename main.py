from datetime import datetime

from controller import Controller


def stringInNumbersArray(input_as_string):
    input_as_array = input_as_string.split(' ')

    converted_input = []

    for element in input_as_array:
        try:
            converted_input.append(int(element))
        except:
            return False, []

    return True, converted_input


def inputValidate():
    validated_input = False

    initial = []

    while not validated_input:
        print('Entre com o seguinte formato:')
        print('Linha 1: 2 0 3')
        print('Linha 2: 1 7 4')
        print('Linha 3: 6 8 5')
        print()

        data1_as_string = input('Linha 1: ')
        data2_as_string = input('Linha 2: ')
        data3_as_string = input('Linha 3: ')
        print()

        all_int, data1_as_array = stringInNumbersArray(
            data1_as_string)

        message_all_int = 'Todos numeros devem ser inteiros'

        if not all_int:
            print(message_all_int)
            continue

        all_int, data2_as_array = stringInNumbersArray(
            data2_as_string)

        if not all_int:
            print(message_all_int)
            continue

        all_int, data3_as_array = stringInNumbersArray(
            data3_as_string)

        if not all_int:
            print(message_all_int)
            continue

        duplicate = False

        for i in range(len(data1_as_array)):
            for j in range(len(data1_as_array)):
                for k in range(len(data1_as_array)):
                    if data1_as_array[i] == data2_as_array[j] or data2_as_array[j] == data3_as_array[k]:
                        duplicate = True

        if duplicate:
            print('Nao podem haver numeros duplicados')
            continue

        if len(data1_as_array) + len(data2_as_array) + len(data3_as_array) != 9:
            print('Devem haver 9 numeros')
            continue

        initial.extend(data1_as_array)

        initial.extend(data2_as_array)

        initial.extend(data3_as_array)

        out_of_range = False

        for element in initial:
            if not (element >= 0 and element <= 8):
                out_of_range = True

        if out_of_range:
            initial = []

            print('Os numeros devem estar entre 0 e 8.')

            continue

        validated_input = True

    return initial


def main():
    initial = inputValidate()

    graph = Controller(initial)

    bidirectionalInitialTime = datetime.now()
    print('Busca bidirecional iniciada')

    graph.bidirectionalSearch()

    print('Busca bidirecional finalizada')
    bidirectionalfinalTime = datetime.now()

    print(
        f'Tempo da busca bidirecional: {abs(bidirectionalInitialTime-bidirectionalfinalTime).total_seconds()}')

    print('----------------------------------------------------------------')

    aStarInitialTime = datetime.now()
    print('Busca a-estrela iniciada')

    graph.starASearch()

    print('Busca a-estrela finalizada')
    aStarFinalTime = datetime.now()

    print(
        f'Tempo da busca bidirecional: {abs(aStarInitialTime-aStarFinalTime).total_seconds()}')

    print('----------------------------------------------------------------')

    best_result = None

    for element in graph.results:
        out_file = open('resultado.log', 'wt')
        out_file.write(str(element))
        out_file.close()

        if not best_result:
            best_result = element
        else:
            best_result = best_result if len(best_result.path) < len(
                element.path) or best_result.time - element.time < -4 else element

    print(
        f'O melhor resultado foi do metodo {best_result.name} com duracao de {round(best_result.time, 6)} segundos')


main()
