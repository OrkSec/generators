#!/bin/bash

if [ "$1" == "1" ]; then

        for i in $(seq $2); do string=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3| head -n 1); echo 1811MR05${string}8; done > Serials.txt

elif [ "$1" == "2" ]; then
        for i in $(seq $2); do string=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3| head -n 1); echo 1806MR06${string}8 ; done > Serials.txt

elif [ "$1" == "3" ]; then
        lettera=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 1| head -n 1)
        letterb=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 1| head -n 1)
        echo 1625ML00${RANDOM:0:1}${lettera}${letterb} 
else
echo "@shmadul's Logitech Serial Generator"
echo "Enter Selection"
echo "1: G810 (RGB)"
echo "2: G810 (Red)"
echo "95% Accuracy, check with https://support.logitech.com/en_us/register"
read selection
if [ "$selection" == "1" ]; then

    string=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3| head -n 1)
    echo "G810(RGB) Serial:"
    echo 1811MR05${string}8

elif [ "$selection" == "2" ]; then

    string=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3| head -n 1)
        echo "G810(Red) Serial:"
        echo 1806MR06${string}8

elif [ "$selection" == "3" ]; then
    lettera=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 1| head -n 1)
    letterb=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 1| head -n 1)
    echo 1625ML00${RANDOM:0:1}${lettera}${letterb} 
else
    echo "Invalid syntax"
fi
fi

