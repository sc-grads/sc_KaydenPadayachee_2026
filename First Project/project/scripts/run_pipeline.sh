#!/bin/bash


echo " STARTING PIPELINE "


cd "$(dirname "$0")/.."


if [ -d "venv" ]; then
    source venv/bin/activate
fi


python3 scripts/process_data.py


if [ -f "output/clean_sales.csv" ]; then
 
    echo " PIPELINE SUCCESSFUL "
    echo " FILE CREATED: output/clean_sales.csv "
    
else
    echo " PIPELINE FAILED "
fi
