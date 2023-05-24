# Группирования пар объектов
## Описание задачи
Дано множество объектов, каждый объект характеризуется набором свойств. 
Для любой пары объектов задается отношение на основе сопоставления их свойств. 
Например, для объектов типа производственное задание имеет место такое свойство, как директивный интервал - "окно", т.е. период, когда задание должно быть выполнено. Данный период характеризуется парой временных меток: ранее и позднее  завершение. 
Для любых двух заданий можно задать отношение, как пересечение их директивных интервалов. Т.е. чем болше пересекаются окна, тем сильнее их связность. 
Необходимо объединить задания в  группы, не более указанного количества,  таким образом, чтобы их директивные интервалы максимально пересекались,  т.е. полученные группы обладали наибольшей суммарной силой связи, и какждая такая группа состояла из уникальных заданий.

## Подходы к  решению

* [Методы вычисления на графах](https://github.com/plaguedoctor39/graph-search/tree/c7a0e2a7259ef6ef9a6bb69fba16a389ca16f0e7/graph)
* [Методы целочисленного программирования (MIP)](https://github.com/plaguedoctor39/graph-search/tree/c7a0e2a7259ef6ef9a6bb69fba16a389ca16f0e7/MIP)

## Оптмизация производительности

[Заметки сделанные в ходе решения](https://github.com/plaguedoctor39/graph-search/tree/c7a0e2a7259ef6ef9a6bb69fba16a389ca16f0e7/notes)


