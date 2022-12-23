# Issue 3125: chromatic_polynomial incorrectly blocks control-c

Issue created by migration from https://trac.sagemath.org/ticket/3125

Original creator: was

Original creation time: 2008-05-07 16:14:33

Assignee: mhansen

Try this:

```
sage: graphs.CubeGraph(5).chromatic_polynomial()
[control-c]
```


control-c is ignored.  Probably somebody doesn't understand _sig_on/_sig_off!





---

Comment by rlm created at 2008-05-07 17:46:03

Changing assignee from mhansen to rlm.


---

Attachment

After attached patch:

```
sage: graphs.CubeGraph(5).chromatic_polynomial()
^C---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

/Users/rlmill/sage-3.0.1/<ipython console> in <module>()

/Users/rlmill/sage-3.0.1/local/lib/python/site-packages/sage/graphs/graph.py in chromatic_polynomial(self)
   7099         """
   7100         from sage.graphs.chrompoly import chromatic_polynomial
-> 7101         return chromatic_polynomial(self)
   7102 
   7103     def chromatic_number(self):

<type 'exceptions.KeyboardInterrupt'>: 
```



---

Comment by mabshoff created at 2008-05-11 10:41:34

Patch is good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 10:43:49

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 10:43:49

Merged in Sage 3.0.2.alpha0
