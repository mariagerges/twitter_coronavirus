#!/bin/sh

for file in /data-fast/twitter\ 2020/geoTwitter20-*; do
    nohup ./src/map.py "--input_path=$file" &
    echo $file
done
