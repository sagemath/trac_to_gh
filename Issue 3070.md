# Issue 3070: bug in SymmetricGroup(1).cayley_graph()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-01 05:20:47

Assignee: boothby

In https://groups.google.com/group/sage-support/browse_thread/thread/443ce49730b43396 M. Fix reported:

```
Hello-
I input the following:

sage: s1 = SymmetricGroup(1)
sage: s = s1.cayley_graph()
sage: s.vertices()
[]

Shouldn't the set of vertices have one element in it for the
identity?  s1 reports this element, but as shown the graph does not.
I suppose this is trivial, but it seems like it should be fixed at
some point.  I am, however, still fairly new to SAGE, and could easily
be missing something.  Any thoughts on this? 
```


Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-05-01 18:13:17

Applied to sage-3.0 on my macbook:


```
$ ./sage -t devel/sage/sage/groups/
... 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 178.3 seconds
$ ./sage -t devel/sage/sage/graphs
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 217.6 seconds
```



---

Comment by rlm created at 2008-05-01 18:14:45

Conclusion:

The function `cayley_graph` was unnecessarily complicated.


---

Comment by jason created at 2008-05-02 16:07:44

the patch looks good to me.  I didn't apply or doctest it, though.


---

Comment by mabshoff created at 2008-05-02 17:07:35

Doctests pass with the patch applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 17:07:53

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 17:07:53

Merged in Sage 3.0.1.rc0
