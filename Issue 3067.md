# Issue 3067: matrices:  numeric_array() is missing an import

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-30 15:23:45

Assignee: was

This happens for all matrices:


```
sage: m = matrix([])
sage: m.numeric_array()
<type 'exceptions.ImportError'>: No module named Numeric
sage: q= random_matrix(ZZ,2)
sage: q.numeric_array()
<type 'exceptions.ImportError'>: No module named Numeric
```



---

Attachment

I deleted this function since it looks like sage doesn't use Numeric anymore. Or I could do a conditional import. Thoughts?


---

Comment by mabshoff created at 2008-05-01 05:50:37

Resolution: fixed


---

Comment by mabshoff created at 2008-05-01 05:50:37

Merged in Sage 3.0.1.alpha1
