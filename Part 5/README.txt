To prompt the output:
$ cat PostHistory.xml Users.xml | ./mapper_5.py | sort | ./reducer_5.py

To save the output:
$ cat PostHistory.xml Users.xml | ./mapper_5.py | sort | ./reducer_5.py > Part_5_out.txt