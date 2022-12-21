# Issue 8272: R's spkg-install tries to disable iconv, but it is *essential* for R.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-15 11:17:11

Assignee: amhou

R has long since wanted iconv support, although there was an option to disable it. That option has now been removed, and R *must* have iconv. However, there is junk left over in R's spkg-install which tries to disable iconv, and reports it is doing so. 


```
Disabling libiconv support on Solaris
```


It likewise tries to do that same on OS X. 


---

Comment by drkirkby created at 2010-02-17 01:02:14

#8285 addresses this issue, along with several other issues.


---

Comment by drkirkby created at 2010-07-19 07:39:59

This has long been resolved, so can be closed.


---

Comment by drkirkby created at 2010-07-19 07:39:59

Resolution: fixed
