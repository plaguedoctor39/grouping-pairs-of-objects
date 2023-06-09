## Муравьиный алгоритм

### Реализация
1. Класс [Ant](https://github.com/plaguedoctor39/grouping-pairs-of-objects/blob/ffbb342d756bb7a4c629f5943ddb22dc38860406/ACO/aco.py#LL15C7-L15C10)
   * Представляет экземпляр муравья в колонии. У каждого муравья есть список вершин, которые он еще не посетил (nodes) и группа, которую он формирует (group).
   * Метод [find_group](https://github.com/plaguedoctor39/grouping-pairs-of-objects/blob/ffbb342d756bb7a4c629f5943ddb22dc38860406/ACO/aco.py#LL21C12-L21C12) реализует поиск комбинации групп с условием максимизировать общий вес комбинации групп. Итерационно выбирается вершина, у которой наивысшая сумма весов с уже имеющимися вершинами в группе пока группа не достигает максимального размера.
2. Функция [aco](https://github.com/plaguedoctor39/grouping-pairs-of-objects/blob/ffbb342d756bb7a4c629f5943ddb22dc38860406/ACO/aco.py#L32)
    * Это основаная функция, которая реализует Ant Colony Optimization algorithm. В качестве аргументов получает список вершин, их ребра, кол-во муравьев в колонии и максимальное кол-во итераций для алгоритма.
    * Для каждой итерации создается новый сет муравьев и для каждого муравья вызывается метод find_group для поиска комбинации. Далее высчитывается общий вес комбинации групп найденной муравьем.
    * Если найденный общий вес больше общего веса найденного раньше, результат перезаписывается.


### Bechmarks

| n   | Time    |
|-----|---------|
| 10  | 0.13 s  |
| 30  | 0.48 s  |
| 80  | 2.81 s  |
| 200 | 31.36 s |

На n=200 более точный результат получен с увеличенным параметром итераций 