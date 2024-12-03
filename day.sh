#!/usr/bin/env bash

# Get input
if [ -z "$1" ]; then
    echo "Usage: ./day.sh <day_number> <optional year>"
    exit 1
fi
# Get day and year
DAY=$1
YEAR=${2:-$(date +'%Y')}

# Validate inputs
if [ $DAY -lt 1 ] || [ $DAY -gt 25 ]; then
    echo "Day should be between 1 and 25"
    exit 1
fi
if [ $YEAR -lt 2015 ]; then
    echo "Year should be greater than or equal to 2015"
    exit 1
fi

# Make dir & files if they don't exist
year_dir=$(dirname $(realpath $0))/src/$YEAR
if [ ! -d $year_dir ]; then
    mkdir -p $year_dir
fi
if [ ! -f $year_dir/$DAY.py ]; then
    cp $(dirname $(realpath $0))/daytemplate.py $year_dir/$DAY.py
fi

# If input already exists AND its not empty, exit
if [ -s $year_dir/$DAY.txt ]; then
    echo "Input already exists, didn't fetch from aoc site"
    exit 0
fi

# Ensure env exists
if [ ! -f $(dirname $(realpath $0))/.env ]; then
    echo "No .env file found"
    exit 1
fi
# Fetch aoc cookie
source $(dirname $(realpath $0))/.env
if [ -z "$AOC_SESSION_COOKIE" ]; then
    echo "AOC_SESSION_COOKIE is not set in env file, can't pull input"
    exit 1
fi
# Attempt curl
curl -s -b "session=$AOC_SESSION_COOKIE" https://adventofcode.com/$YEAR/day/$DAY/input > $year_dir/$DAY.txt
# Make sure input is available from aoc site
if grep -q "Please don't repeatedly request this endpoint before it unlocks!" $year_dir/$DAY.txt; then
    rm $year_dir/$DAY.txt
    echo "Input not available yet"
    exit 1
fi