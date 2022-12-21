# Issue 2323: updated tutorial to include dsage section

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-26 18:15:52

Assignee: tba

updated the tutorial to add a section of distributed computing.


---

Attachment


---

Comment by mhansen created at 2008-02-27 23:43:38

Looks good to me.


---

Comment by mabshoff created at 2008-02-27 23:56:39

No dice against my merge tree:

```
hg unbundle trac_2323_dsage-tut.hg
adding changesets
transaction abort!
rollback completed
abort: unknown parent 2af41ec9da8d!
```

Please post a flattened patch or tell me which patches to merge first.

Cheers,

Michael


---

Attachment


---

Attachment

Merged in Sage 2.10.3.rc0. Please indicate clearly that this bundle is against the doc repo since it wasn't immediately clear and it cause some confusion.


---

Comment by mabshoff created at 2008-02-28 00:13:27

Resolution: fixed
