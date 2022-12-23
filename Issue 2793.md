# Issue 2793: Bug in the sage preparser!  "\"Yes,\" he said."

Issue created by migration from https://trac.sagemath.org/ticket/2793

Original creator: was

Original creation time: 2008-04-04 00:44:28

Assignee: cwitty

In the Python tutorial (http://docs.python.org/tut/node5.html#SECTION005120000000000000000)
 there's an example of making a string:

```
>>> "\"Yes,\" he said."
'"Yes," he said.'
```


This fails in Sage because of the preparser!


```
sage: "\"Yes,\" he said."
------------------------------------------------------------
   File "<ipython console>", line 1
     "\"Yes,._backslash_()" he said."
                             ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


This is obviously a bug in the _backslash_ or "in quotes" part of the preparser.  So it's almost certainly my fault.



---

Attachment


---

Comment by robertwb created at 2008-04-04 07:34:36

Breaks on `s = "\\"`.


---

Attachment


---

Comment by was created at 2008-04-04 19:01:10

I've attached a part 2 patch which addresses the referee's (nick's) comments.


---

Comment by robertwb created at 2008-04-04 19:23:30

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 21:27:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 21:27:04

Merged both patches in Sage 3.0.alpha1
