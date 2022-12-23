# Issue 1464: [with patch] binary code canonical labels & automorphism group generators

Issue created by migration from https://trac.sagemath.org/ticket/1464

Original creator: rlm

Original creation time: 2007-12-11 23:25:32

Assignee: rlm

The following bundle is based on 2.9 alpha5, so should merge easily

http://sage.math.washington.edu/home/rlmill/sage-2.9.alpha5/binary_codes.hg

Note that the coverage in the new file, binary_codes.pyx, is 100%.


---

Comment by rlm created at 2007-12-11 23:26:10

Changing status from new to assigned.


---

Comment by jsp created at 2007-12-12 00:08:26

The bundle worked for me on Fedora 7.


```
sage -t  devel/sage-main/sage/coding/binary_code.pyx        
         [2.8 s]
 
----------------------------------------------------------------------
All tests passed!

```




```
[jaap@paix sage-2.9.alpha5]$ ./sage -t devel/sage/sage/graphs*
sage -t  devel/sage-main/sage/graphs/print_graphs.py        
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_database.py      
         [12.9 s]
sage -t  devel/sage-main/sage/graphs/graph_fast.pyx         
         [1.8 s]
sage -t  devel/sage-main/sage/graphs/graph_list.py          
         [8.9 s]
sage -t  devel/sage-main/sage/graphs/graph_genus1.py        
         [12.8 s]
sage -t  devel/sage-main/sage/graphs/graph.py               
         [36.8 s]
sage -t  devel/sage-main/sage/graphs/linearextensions.py    
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_isom.pyx         
         [28.6 s]
sage -t  devel/sage-main/sage/graphs/all.py                 
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
         [61.9 s]
sage -t  devel/sage-main/sage/graphs/bruhat_sn.pyx          
         [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 169.8 seconds

```



---

Comment by rlm created at 2007-12-14 18:02:27

There are still some bugs...


---

Comment by rlm created at 2007-12-15 22:24:19

Use the bundle at

http://sage.math.washington.edu/home/rlmill/bcodes_2.9.alpha7.hg

instead.


---

Comment by was created at 2007-12-15 23:37:42

Do this after applying the bundle:

```
was@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg rm binary_code_backup.pyx 
was@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg ci
```



---

Comment by mabshoff created at 2007-12-16 00:46:58

Merged in 2.9.rc2.


---

Comment by mabshoff created at 2007-12-16 00:46:58

Resolution: fixed
