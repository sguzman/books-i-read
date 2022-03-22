#!/bin/bash
cat $1 |
    xsv search --delimiter ',' --select 'Exclusive Shelf' '^read$' |
    xsv select 'Title,Author,Number of Pages,Year Published' |
    xsv sort --select 'Year Published' --reverse
