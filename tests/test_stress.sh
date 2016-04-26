#!/bin/bash
rm *@*
rm maxtest.mailbox
rm result

python3 ../test_gen.py 100 1 10000 1000
echo "generated"

time python3 ../kirill_timofeev.py maxtest.mailbox

echo "test diff"
touch result 
for i in `seq 0 99`;
do
	cat "sender"$i"@mail.com" >> result
done    

diff result maxtest.mailbox
if [ $? != 0 ]; then
	echo "files aren't equal"
else
	echo "OK"
fi
