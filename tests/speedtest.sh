#!/bin/bash
function run {
	rm *@*
	echo "python3:"
	time python3 ../kirill_timofeev.py maxtest.mailbox
    
    rm *@*
	echo "pypy:"
	time pypy ../kirill_timofeev.py maxtest.mailbox
	
    rm *@*
	echo "cpp:"
	time ../a.out maxtest.mailbox    
}

echo "100 150 200 1000"
python3 ../test_gen.py 100 100 200 1000
echo "run 1"
run
echo "run 2"
run
echo "run 3"
run

echo "100 1500 2000 10"
python3 ../test_gen.py 100 1000 2000 10
echo "run 1"
run
echo "run 2"
run
echo "run 3"
run
