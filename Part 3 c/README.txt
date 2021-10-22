To prompt the output:
$ cat Posts.xml | ./mapper_3c.py | sort | ./reducer_3c.py

To save the output:
$ cat Posts.xml | ./mapper_3c.py | sort | ./reducer_3c.py > Part_3c_out.txt
