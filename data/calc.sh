#!/usr/bin/bash

TARGET_DIR="../result_csv"
APPEXE="/home/Valdemare/Projects/UNN/Somov/cpp/nncdb/build/nncdb symmol
"
GROUP="--group"
#--progress
FLAGS="--divide-into-molecules --progress --time --import-by-refcode"

#INPUT="F23.cif"
for INPUT in *.cif
do
echo ${INPUT}
${APPEXE} ${FLAGS} -i "${INPUT}" -o "${TARGET_DIR}/${INPUT}.csv"
done


