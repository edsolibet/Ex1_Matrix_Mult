#!/bin/bash

m1=$(cat $1)
m2=$(cat $2)

python3 matrixmult.py $m1 $m2
