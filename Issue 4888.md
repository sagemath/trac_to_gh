# Issue 4888: laplacian_matrix() broken for DiGraphs

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-29 21:56:16

Assignee: rlm

David reports in http://groups.google.com/group/sage-devel/t/51fdef25ed45ceee


```
I am running Sage 3.1.4 under Fedora 9 and have found a bug in the 
file graph.py. 
------------------------------------------------------------------- 
sage: G = DiGraph({0:{}, 1:{0:1}, 2:{0:1}}, weighted = True) 
sage: G.weighted_adjacency_matrix() 
[0] 
[1] 
[1] 
sage: G.adjacency_matrix() 
[0 0 0] 
[1 0 0] 
[1 0 0] 
sage: G.laplacian_matrix() 
--------------------------------------------------------------------------- 
IndexError                                Traceback (most recent call 
last) 
/home/davidp/.sage/temp/xyzzy/16886/ 
_home_davidp_math_sandpile_sage_sandpile_sage_14.py in <module>() 
----> 1 
      2 
      3 
      4 
      5 
/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ 
sage/graphs/graph.pyc in kirchhoff_matrix(self, weighted, 
boundary_first) 
    904         S = [sum(M.row(i)) for i in range(M.nrows())] 
    905         for i in range(len(A)): 
--> 906             A[i][i] = S[i] 
    907         return M.parent()(A) 
    908 
/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ 
sage/modules/free_module_element.so in 
sage.modules.free_module_element.FreeModuleElement_generic_sparse.__setitem __ 
(sage/modules/free_module_element.c:15074)() 
   1765 
   1766 
-> 1767 
   1768 
   1769 
IndexError: index (i=1) must be between 0 and 0 
sage: 
--------------------------------------------------------------------------- --------- 
The laplacian_matrix function is not working because 
weighted_adjacency matrix is not returning a square matrix.  A 
suggested fix is to change line 845 (in the graph.py code for 
weighted_adjacency_matrix) from 
M = matrix(D, sparse=sparse) 
to 
M = matrix(self.num_verts(), D, sparse=sparse) 
David 
```



---

Comment by rlm created at 2009-01-04 18:51:43

I agree with David's proposed fix, and blame boothby ;)


---

Comment by mabshoff created at 2009-01-04 19:37:42

Let's get this into 3.3 then.

Cheers,

Michael


---

Attachment

Positive review for the fix suggested by rlm. I have attached the patch with a doctest and it passes `-t -long` with my current merge tree. Credit for authorship goes to David Perkinson in whose name I committed the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 05:53:27

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 05:53:27

Merged in Sage 3.3.alpha0
