# Issue 5302: Numerical noise in graph.py get_pos() and graph_plot.py

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2009-02-18 11:35:18

Assignee: rlm

On Fedora 9 and 10, 32 bits:


```
sage -t  "devel/sage/sage/graphs/graph.py"                  
**********************************************************************
File "/home/jaap/downloads/sage-3.3.alpha1/devel/sage/sage/graphs/graph.py", line 5814:
    sage: G.get_pos()
Expected:
    {0: [-0.81..., -0.32...],
    1: [-0.49..., 0.53...],
    2: [0.04..., 0.96...],
    3: [0.00..., 0.01...],
    4: [0.17..., -0.71...],
    5: [-0.47..., 0.06...],
    6: [0.35..., -0.17...],
    7: [0.54..., 0.50...],
    8: [-0.30..., -0.57...],
    9: [0.95..., -0.28...]}
Got:
    {0: [-0.80999357280480733, -0.35674303178095085], 1: [-0.5137985651989595, 0.53516030613479626], 2: [0.04267232662930763, 0.9733718008664739], 3: [-0.0030625205151234456, 0.025523074413981252], 4: [0.20666820211352116, -0.73775138260652107], 5: [-0.48704143554494495, 0.075148546351255105], 6: [0.35418721150812299, -0.17351758872721781], 7: [0.54564695734576318, 0.51479808833141838], 8: [-0.29589999259318039, -0.57812915207589943], 9: [0.96062138906029881, -0.27786066090733674]}
**********************************************************************
1 items had failures:
   1 of  78 in __main__.example_133
***Test Failed*** 1 failures.

sage -t  "devel/sage/sage/graphs/graph_plot.py"             
**********************************************************************
File "/home/jaap/downloads/sage-3.3.alpha1/devel/sage/sage/graphs/graph_plot.py", line 108:
    sage: g.get_pos()
Expected:
    {0: [6.123233995736766e-17, 1.0],
     1: [-0.95105651629515353, 0.30901699437494751],
     2: [-0.58778525229247325, -0.80901699437494734],
     3: [0.58778525229247292, -0.80901699437494756],
     4: [0.95105651629515364, 0.30901699437494717]}
Got:
    {0: [6.1230317691118863e-17, 1.0], 1: [-0.95105651629515353, 0.30901699437494751], 2: [-0.58778525229247325, -0.80901699437494734], 3: [0.58778525229247292, -0.80901699437494756], 4: [0.95105651629515364, 0.30901699437494717]}
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.3.alpha1/tmp/.doctest_graph_plot.py
	 [28.9 s]

```


Jaap


---

Comment by rlm created at 2009-02-18 19:30:09

The numerical values themselves are useless in this doctest anyway. The point of the docstring is to illustrate that positions are returned, and that they're in a certain format.


---

Comment by jsp created at 2009-02-18 19:47:37

Ok, this patch looks stupid :-) but it works:



```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.3.rc2, Release Date: 2009-02-17                     |
| Type notebook() for the GUI, and license() for information.        |
sage: 
Exiting SAGE (CPU time 0m0.08s, Wall time 0m5.28s).
[jaap`@`paix sage-3.3.alpha1]$ ./sage -t  "devel/sage/sage/graphs/graph_plot.py"
sage -t  "devel/sage/sage/graphs/graph_plot.py"             
	 [47.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 47.9 seconds
[jaap`@`paix sage-3.3.alpha1]$ ./sage -t  "devel/sage/sage/graphs/graph.py"
sage -t  "devel/sage/sage/graphs/graph.py"                  
	 [109.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 109.9 seconds

```


So positive review.

Jaap


---

Comment by mabshoff created at 2009-02-18 19:54:34

Well, if one could add a comment before the doctest is run *why* we dot out all the output I would be happier.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2009-02-19 21:40:19

Replying to [comment:3 mabshoff]:
> Well, if one could add a comment before the doctest is run *why* we dot out all the output I would be happier.

Done


---

Comment by mabshoff created at 2009-02-20 06:10:54

Thanks, looks better to me :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 06:39:59

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 06:39:59

Resolution: fixed
