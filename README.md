# Задание на вакансию стажёра-разработчика Python (Инфраструктура вертикальных сервисов)

Тесты лежат в tests/

## Производительность
Производительность можно тестировать скриптом `tests/speedtest.sh`

Тестовые данные: файл размером 2GB

#### Время работы при чтении с SSD (среднее по трём запускам):
- `$ python test_gen.py 100 150 200 1000`

```
$ time python kirill_timofeev.py maxtest.mailbox 
real	0m5.447s
user	0m1.156s
sys	    0m1.456s
```
```
$ time pypy kirill_timofeev.py maxtest.mailbox 
real	0m18.815s
user	0m15.936s
sys	    0m1.844s
```
```
$ time ./fast.out maxtest.mailbox 
real	0m4.828s
user	0m0.572s
sys	    0m1.780s
```
- `$ python test_gen.py 100 1000 2000 10`
```
$ time python kirill_timofeev.py maxtest.mailbox 
real	1m1.093s
user	0m57.772s
sys	    0m2.176s
```
```
$ time pypy kirill_timofeev.py maxtest.mailbox 
real	0m33.779s
user	0m30.268s
sys	    0m2.096s
```
```
$ time ./fast.out maxtest.mailbox 
real	0m29.887s
user	0m25.812s
sys	    0m2.024s
```
