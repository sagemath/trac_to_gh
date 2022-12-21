# Issue 5637: [with patch, needs review] allow \[ and \] to delimit math in %html blocks

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-30 00:57:53

Assignee: boothby

Without the patch,

```
%html
test
\[ x^2 \]
```

is not typeset with `x^2` in math mode.  With the patch, the above is treated just like 

```
%html
test
$$ x^2 $$
```




---

Attachment


---

Comment by jhpalmieri created at 2009-03-30 01:07:17

Changing assignee from boothby to jhpalmieri.


---

Comment by jhpalmieri created at 2009-03-30 01:07:17

Changing status from new to assigned.


---

Comment by ncalexan created at 2009-06-15 19:47:19

Looks good to me.


---

Comment by rlm created at 2009-06-24 10:07:44

Resolution: fixed
