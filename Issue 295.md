# Issue 295: '??' doesn't always print last line of last function in file

Issue created by migration from https://trac.sagemath.org/ticket/295

Original creator: justin

Original creation time: 2007-02-25 18:49:28

Assignee: was

A file with this content (w/o the "==="'s) shows the problem:


```
def Foo(x)
    x = 1
```


After load/attaching this file, typing "??Foo" prints only the 'def' line.

If the file looks like this (i.e., with an 'extra' blank line):


```
def Foo(x)
    x = 1

```


then '??' works properly.



---

Comment by justin created at 2007-02-25 18:51:41

Ignore the "==="s part; forgot to remove this after fiddling with formatting.


---

Comment by was created at 2007-02-25 19:15:09

Changing assignee from was to Nick Alexander.


---

Comment by ncalexan created at 2007-02-28 20:21:13

Changing assignee from Nick Alexander to ncalexan.


---

Comment by ncalexan created at 2007-02-28 20:33:49

Resolution: fixed


---

Comment by ncalexan created at 2007-02-28 20:33:49

Fixed in ncalexan's local tree by 34c022ed2482.

This requires the doctest.ELLIPSIS option be added to local/bin/sage-doctest, so I haven't sent it upstream yet.  When I finish touching the testing infrastructure, I'll send it along, or ask for it :)
