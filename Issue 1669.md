# Issue 1669: remove bogus recommendation to set SAGE_ATLAS when numpy fails

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-03 15:51:27

Assignee: jkantor

When numpy fails to build it prints the following error message which is no longer valid:

```
 Error building numpy.
Try setting SAGE_ATLAS to the directory that contains lib/libatlas.a ?
```



---

Comment by mabshoff created at 2008-01-09 00:01:52

This will be fixed via the new numpy.spkg linked from #1720.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-09 01:56:05

Resolution: fixed


---

Comment by mabshoff created at 2008-01-09 01:56:05

Fixed in Sage 2.10.alpah1.
