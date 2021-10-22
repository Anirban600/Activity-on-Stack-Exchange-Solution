To prompt the output:
$ cat Comments.xml | ./mapper_4.py | sort | ./reducer_4.py

To save the output:
$ cat Comments.xml | ./mapper_4.py | sort | ./reducer_4.py > Part_4_out.txt