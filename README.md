# Задание на вакансию стажёра-разработчика Python (Инфраструктура вертикальных сервисов)

## Производительность
тестовые данные: файл размером 3GB

`$ python test_gen.py 100 100 300`
#### время работы при чтении с SSD(среднее по трём запускам):
```
$ time python first.py maxtest.mailbox 
real	0m12.147s
user	0m5.388s
sys	    0m5.956s
```
```
$ time pypy first.py maxtest.mailbox 
real	0m10.499s
user	0m4.128s
sys	    0m4.536s
```
```
$ time ./a.out maxtest.mailbox 
real	0m9.316s
user	0m1.148s
sys	    0m3.864s
```
#### время работы при чтении с RAM-диска(среднее по трём запускам):
```
$ time python first.py maxtest.mailbox 
real	0m13.435s
user	0m8.596s
sys	    0m4.844s
```
```
$ time pypy first.py maxtest.mailbox 
real	0m11.636s
user	0m7.612s
sys	    0m4.024s
```
```
$ time ./fast.out maxtest.mailbox 
real	0m5.913s
user	0m1.648s
sys	    0m4.256s
```