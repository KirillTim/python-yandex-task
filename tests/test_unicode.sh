#!/bin/bash
function check {
    touch result
    cat auth1@china.com >> result 
    cat auth2@japan.com >> result
    cat auth3@arab.com >> result
    diff result unicode.mailbox
    if [ $? != 0 ]; then
        echo "files aren't equal"
    else
        echo "OK"
    fi
}

rm auth1@china.com auth2@japan.com auth3@arab.com result
python3 ../kirill_timofeev.py unicode.mailbox
check
rm auth1@china.com auth2@japan.com auth3@arab.com result
python3 ../kirill_timofeev.py unicode.mailbox
check
