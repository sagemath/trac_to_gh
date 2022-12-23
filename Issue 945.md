# Issue 945: preparser should ignore "    ....:" when it ignores "sage:"

Issue created by migration from https://trac.sagemath.org/ticket/945

Original creator: cwitty

Original creation time: 2007-10-20 17:15:06

Assignee: was

Here's a test case.  First I define a function:

```
sage: def foo(x):
....:     return x+3
....: 
```


Then I copy/paste the above session:

```
sage: sage: def foo(x):
....:     ....:     return x+3
------------------------------------------------------------
<type 'exceptions.IndentationError'>: expected an indented block (<ipython console>, line 2)

sage: 
```




---

Comment by tscrim created at 2013-05-24 17:59:10

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-05-24 17:59:10

This was fixed at some point (tested on `5.10.beta2`):

```
sage: def foo(x):
....:     return x
....: 
sage: sage: def foo(x):        
....:     ....:     return x
....: ....: 
sage: 
sage: def foo(x):
....:     ....:     return x
....: 
```



---

Comment by tmonteil created at 2013-06-01 13:50:46

I confirm that this works, hence i put a positive review. I do not know who shoud be the author though. Maybe ipython ?


---

Comment by tmonteil created at 2013-06-01 13:50:46

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-06-01 15:04:46

For duplicate tickets, there is no author since there is no patch to be merged.


---

Comment by jdemeyer created at 2013-06-03 13:07:55

Resolution: worksforme


---

Comment by vbraun created at 2013-06-03 15:34:42

See also #14665 for a related bug.
