# Issue 1444: [with patch] some serious hard-coding issues that break all binary installs

Issue created by migration from https://trac.sagemath.org/ticket/1444

Original creator: was

Original creation time: 2007-12-10 01:11:39

Assignee: mabshoff


```
Hi,

There are a few very serious (but easy to fix)
problems with the current sage and upcoming packages
that involving hardcoding of paths.  These
will cause problems if you move a sage install.

POLYBORI:
I noticed this in a SAGE_ROOT/local/bin/:

   lrwxr-xr-x  1 was  was       47 Dec  4 10:52 ipbori -> /Users/was/s/local/share/polybori/ipbori/ipbori

That link *must* not be hard coded.  Make sure this gets fixed before polybori is in sage.

SINGULAR (very serious):
   Several Singular-related files in SAGE_ROOT/local/bin/ have hardcoded paths.
   This makes it so singular will fail to work for everybody who downloads a sage
   binary right now :-(. 

   The package singular-3-0-4-1-20071209.spkg fixes the problem.  Just do 
   sage -upgrade to get it, or download it from 
       http://sagemath.org/packages/standard/singular-3-0-4-1-20071209.spkg

BZIP2:
   Some minor path hardcoding problems.  Easy to fix.  I've put the file that needs
to be replaced here...
```



---

Attachment

put this file in spkg/base/   overwriting the one there already.


---

Comment by mabshoff created at 2007-12-10 03:39:12

Resolution: fixed


---

Comment by mabshoff created at 2007-12-10 03:39:12

Merged in 2.9.alpha3.
