# Issue 1582: 2.9.1.alph2: doctest failure in sage/graphs/graph.py with x86 Linux

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-21 12:27:52

Assignee: rlm

Jaap reported:

```
sage -t  devel/sage-main/sage/graphs/graph.py
**********************************************************************
File "graph.py", line 4150:
     sage: E[1][0]
Expected:
     Vector space of degree 5 and dimension 1 over Real Double Field
     User basis matrix:
     [ 0.632455532034 -0.632455532034   -0.4472135955 -0.013900198608 0.0738411279702]
Got:
     Vector space of degree 5 and dimension 1 over Real Double Field
     User basis matrix:
     [  0.632455532034  -0.632455532034    -0.4472135955   0.047561829961 -0.0797092534371]
********************************************************************** 
```


Cheers,

Michael


---

Comment by rlm created at 2007-12-21 22:13:42


```
[4:44pm] wstein-924: Regarding the graph.py example, I would just put
[4:44pm] wstein-924: sage: E[1][0]    # eigenspace computation is somewhat random.
[4:45pm] rlm-1584: +1
```


Merged in 2.9.1 alpha3


---

Comment by rlm created at 2007-12-21 22:13:42

Resolution: fixed
