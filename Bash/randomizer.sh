#!/bin/bash

SIZE=1000
counter=0
while [ $counter -le $SIZE ]
do
    # Using arbitrary precision numbers (bc)
    echo $RANDOM % 10 + 1 | bc
    ((counter=counter+1))
done