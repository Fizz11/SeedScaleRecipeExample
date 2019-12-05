#!/bin/bash
if [ $((RANDOM%2)) -eq 0 ]
then
    echo "Yes I generated a file"
    RANDOM_NUMBER=$RANDOM
    FILENAME="${OUTPUT_DIR}/$RANDOM_NUMBER.tmp"
    echo "why would you even look in here??!!!!" > $FILENAME
else
    echo "Nah I didnt generate a file"
fi

