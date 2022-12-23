# Issue 4368: Create a function which gets an attributed from an object and calls it with specified arguments and keywords

Issue created by migration from https://trac.sagemath.org/ticket/4368

Original creator: mhansen

Original creation time: 2008-10-25 21:33:46

Assignee: cwitty

Example:


```
sage: f = attrcall('r_core', 3); f
*.r_core(3)
sage: [f(p) for p in Partitions(5)]
[[2], [1, 1], [1, 1], [3, 1, 1], [2], [2], [1, 1]]
```




---

Comment by mhansen created at 2008-10-25 21:34:57

Changing assignee from cwitty to mhansen.


---

Comment by mhansen created at 2008-10-25 21:34:57

Changing status from new to assigned.


---

Comment by mvngu created at 2008-10-26 11:17:20

Reply to [comment:2 mhansen]



The following snippet is from the attached patch *trac_4368.patch*:

```
+def attrcall(name, *args, **kwds):
+    """
+    Returns a callable which takes in an object, gets the method
+    named name from that objects, and calls it with the specified
+    arguments and keywords.
```

Why "named name from that _objects_"? (my emphasis) My understanding is that I can pass in an object (not more than one) to the proposed class `AttrCallObject`. If you mean that I can pass in only one object in order to get a returned callable, then you might want to consider the following documentation change:

```
-named name from that objects, and calls it with the specified
+named name from that object, and calls it with the specified
```



---

Comment by robertwb created at 2008-10-30 21:44:49

Any reason you're not using functools http://www.python.org/doc/2.5.2/lib/module-functools.html ?


---

Comment by robertwb created at 2008-10-30 22:24:49

OK, looking into this more, I see that functools won't help much (as the callable isn't specified ahead of time). It looks good and works well. 

Positive review, pending the (presumably just a typo) fix from mvngu above. BTW, I like the "*.foo(x)" string representation.


---

Attachment


---

Comment by mhansen created at 2008-10-30 22:33:15

I've updated the patch to fix the typo.


---

Comment by mabshoff created at 2008-10-31 00:24:52

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 00:24:52

Merged in Sage 3.2.alpha2
