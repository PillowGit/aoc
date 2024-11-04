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

# Make dir & files
year_dir=$(dirname $(realpath $0))/src/$YEAR
if [ ! -d $year_dir ]; then
    mkdir -p $year_dir
fi
if [ ! -f $year_dir/$DAY.py ]; then
    cp $(dirname $(realpath $0))/daytemplate.py $year_dir/$DAY.py
fi
if [ -f $year_dir/$DAY.txt ]; then
    exit 0
fi

# Validate & curl from adventofcode website
if [ ! -f $(dirname $(realpath $0))/.env ]; then
    echo "No .env file found"
    exit 1
fi
source $(dirname $(realpath $0))/.env
if [ -z "$AOC_SESSION_COOKIE" ]; then
    echo "AOC_SESSION_COOKIE is not set in env file, can't pull input"
    exit 1
fi
curl -s -b "session=$AOC_SESSION_COOKIE" https://adventofcode.com/$YEAR/day/$DAY/input > $year_dir/$DAY.txt