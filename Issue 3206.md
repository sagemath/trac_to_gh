# Issue 3206: sage -i http://url.of.an.spkg doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/3206

Original creator: was

Original creation time: 2008-05-14 22:26:12

Assignee: mabshoff

For some reason nobody ever got around to implementing "sage -i" on URL's.  E.g.,
this should work but doesn't yet.  I'm amazed this still isn't done!

```
sage -i http://sagemath.org/packages/optional/database_odlyzko_zeta.spkg
```



---

Attachment

I've fixed the indicated problem, cleaned up the code, and documented the heck out of local/bin/sage-download_package/.


---

Comment by mabshoff created at 2008-06-23 07:01:09

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 07:01:09

Merged in Sage 3.0.4.alpha0
