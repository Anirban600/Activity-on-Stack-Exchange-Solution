To prompt the output:
$ cat Posts.xml | ./mapper_3a.py | sort | ./reducer_3a.py

To save the output:
$ cat Posts.xml | ./mapper_3a.py | sort | ./reducer_3a.py > Part_3a_out.txt

To generate distribution graph:
$ cat Part_3a.txt | ./plotter_3a.py
