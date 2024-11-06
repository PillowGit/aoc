
#!/usr/bin/env bash

# Get input
if [ -z "$1" ]; then
    echo "Usage: ./day.sh <day_number> <optional year>"
    exit 1
fi
DAY=$1
YEAR=${2:-$(date +'%Y')}

# Validate input
if [ $DAY -lt 1 ] || [ $DAY -gt 25 ]; then
    echo "Day should be between 1 and 25"
    exit 1
fi
if [ $YEAR -lt 2015 ]; then
    echo "Year should be greater than or equal to 2015"
    exit 1
fi

# Run the python main file at the path src/YEAR/DAY.py with python3 -m src.YEAR.DAY
clear
python3 -m src.$YEAR.$DAY