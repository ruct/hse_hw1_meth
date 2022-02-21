## hse_hw1_meth

[Google коллаб](https://colab.research.google.com/drive/11Heblh6Wg-uCqgD31M1V6CzjrtOucr_5?usp=sharing)

![image](data/1sc.png)
8cell.

Цитозина стало заметно меньше относительно обычных ридов. Тимина, наоборот, сильно больше.

![image](data/3sc.png)
Длины ридов по распределению не сильно, но отличаются от нормы.

![image](data/2sc.png)

Распределение GC content имеет несколько пиков, не является нормальным распределением.

По сравнению с предыдущими анализами нет адаптера, пропуски и дупликации ожидаемы.

## Участок хромосомы. Чтения

| name     |1347700-11367700  |  40185800-40195800 |
|----------|------------------|--------------------|
| 8cell    |  1090            |  464               |
| icm      |  1456            |  630               |
| epiblast |  2328            |  1062              |

## Дуплицированные чтения

| name     | percent |
|----------|---------|
| 8cell    | 18.31 % |
| icm      | 9.08 %  |
| epiblast | 2.92 %  |

### M bias plots
8cell m-bias plots:
![image](data/8cell_m1.png)
![image](data/8cell_m2.png)

icm m-bias plots:
![image](data/icm_m1.png)
![image](data/icm_m2.png)

epiblast m-bias plots:
![image](data/epiblast_m1.png)
![image](data/epiblast_m2.png)

В нашем дз нам нужно обратить внимание на CpG, для них графики около константы, за исключением иногда возрастания\убывания в начале сторону уменьшения позиции. Объектов других видов относительно этого немного, но они имеют большее отклонение. Но опять же, в целом их немного.

## Гистограммы bismark cov

8cell:
![image](data/8cell_hist.png)

icm:
![image](data/icm_hist.png)

epiblast:
![image](data/epiblast_hist.png)

По гистограммам видно, что сначала большинство значений возле нуля, а после - резко в 100%.

###

8cell:
![image](data/result_cell8.png)

icm:
![image](data/result_icm.png)

epiblast:
![image](data/result_epiblast.png)
