#!/bin/bash

echo '# Books I read'
echo
echo 'This list contains the books i read. Enjoy :)'
echo
echo '### Sorted by date published'
echo

bash read.sh $1 | csvtomd
