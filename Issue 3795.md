# Issue 3795: increase coverage of sage/server/notebook/cell.py

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-09 15:13:45

Assignee: boothby




---

Attachment


---

Comment by mhansen created at 2008-08-09 15:18:11

Before:

```
SCORE cell.py: 8% (7 of 82)
```


After:

```
SCORE cell.py: 79% (67 of 84)
```



---

Attachment


---

Comment by ncalexan created at 2008-08-10 23:19:25

I think mhansen's patch is excellent, but it broke if applied after #3568.  My updated patch depends on #3568 and makes the "get a test notebook" interface uniform using #3568.

All credit to mhansen.

Attach only `3795-mhansen-doctest-cell.patch`, *after* #3568.


---

Comment by ncalexan created at 2008-08-10 23:20:01

I think this can get "positive review" if it doctests.


---

Comment by mabshoff created at 2008-08-11 08:19:25

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 08:19:25

Merged trac_3795.patch in Sage 3.1.alpha1. Sorry Nick, due to #3568 causing massive doctest failures William will redo it for 3.1.alpha2. Hopefully someone will take your patch and rebase it on the new release.

Cheers,

Michael
