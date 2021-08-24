 #!/bin/bash
debug=${4:-2}

python shortestpath.py -p $1 -n1 $2 -n2 $3 -d $debug
