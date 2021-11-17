#!/bin/bash
# @author Manuel Gieseking
INPUTFOLDER=./sdn

ADAM=../../deploy/adamMC

MAX=$(ls -f $INPUTFOLDER/*.apt | wc -l)

CUR_DATE=$(date +"%m%d%y")

NAME=packetCoherence
FOLDER=$CUR_DATE"_"$NAME
mkdir -p $FOLDER
echo "-------------------- Creating the Petri net with transits ------------------------------"
count=1
for filename in $INPUTFOLDER/*.apt; do
	if [[ $(($count/2)) -lt $MAX ]]; then
		FILE_NAME=$(basename "$filename" .apt)
		FILE=$INPUTFOLDER/$FILE_NAME".apt"

		$ADAM gen_topologie_zoo -i "$FILE" -c packetCoherence -o "$FOLDER"'/'"$FILE_NAME"
	else
		break;
	fi
done
