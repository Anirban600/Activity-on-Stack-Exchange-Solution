To prompt the output:
$ cat Posts.xml | ./mapper_3b.py | sort | ./reducer_3b.py

To save the output:
$ cat Posts.xml | ./mapper_3b.py | sort | ./reducer_3b.py > Part_3b_out.txt

To generate distribution graph:
$ cat Part_3b.txt | ./plotter_3b.py
