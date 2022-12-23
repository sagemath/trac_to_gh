# Issue 1147: change location of valgrind output files to something less obnoxious

Issue created by migration from https://trac.sagemath.org/ticket/1147

Original creator: was

Original creation time: 2007-11-11 14:44:26

Assignee: mabshoff

When running 

``` 
  sage -valgrind
```


the output files are all over in $HOME/.sage.  They should be put in a file 

```
  $HOME/.sage/valgrind
```




---

Comment by mabshoff created at 2007-11-11 15:03:08

:) - will do once I add proper omega report for 2.8.13.

Cheers,

Michael


---

Comment by malb created at 2007-11-11 15:44:37

At least these should be put in `$HOME/.sage/valgrind-memcheck`, `$HOME/.sage/valgrind-cachgrind` etc.


---

Attachment

Apply this to the scripts repo!


---

Comment by mabshoff created at 2007-12-18 21:32:05

It fails to apply cleanly against 2.9. The patch itself is good, if I have some time later I will try to correct the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 19:23:23

I fixed the hunk that gets rejected. positive review now ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 19:23:46

Resolution: fixed


---

Comment by mabshoff created at 2008-01-25 19:23:46

Merged in Sage 2.10.1.alpha2
