# Issue 4012: notebook -- Text tab gives bad text version of worksheet

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-31 02:08:21

Assignee: boothby

Edit tab gives:

```


Print a & b
system:sage

{{{id=3|
%latex
x^2
///
}}}

{{{id=0|
print "a"
///
a
}}}

{{{id=1|
print "b"
///
b
}}}

{{{id=2|

///
}}}



```


Text tab gives:

```
sage: %latex
sage: x^2
sage: print "a"
a
sage: print "b"
b
```


The Text tab should show a textual version similar to that of the Edit tab.


---

Comment by boothby created at 2009-01-22 00:47:28

WT?

 1. Why does this ticket have "major" priority?
 1. Why is this a "defect"?
 1. Why would we have two buttons that do the same thing?
 1. The text tab *does* show a textual version of the notebook.

The edit tab allows one to edit the worksheet.  The text tab gives output similar to that which you would get by using the command line.  What's the problem?


---

Comment by boothby created at 2009-01-22 00:47:28

Resolution: invalid
