# Issue 4543: sage -sh fails to start

Issue created by migration from https://trac.sagemath.org/ticket/4543

Original creator: burcin

Original creation time: 2008-11-18 08:36:12

Assignee: burcin

CC:  craigcitro

With 3.2.rc1, I get this:


```
burcin@karr ~/sage/sage-3.2.rc1 $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

basename: invalid option -- a
Try `basename --help' for more information.
Exited Sage subshell.
```


On my system `basename` does not accept a parameter `-a`.


```
burcin@karr ~/sage/sage-3.2.rc1 $ basename --version
basename (GNU coreutils) 6.10
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by FIXME unknown.
```


This can be fixed by removing the `-a` parameter on line 375 of the `sage-sage` script.


---

Attachment

attachment:trac_4543.patch removes the `-a` parameter from `basename` in the `sage-sage` script. This fixes the problem on my system.


---

Comment by craigcitro created at 2008-11-18 08:48:03

I don't really know where I got the `-a` argument -- I think I was copying it from somewhere else. Deleting it seems to work fine on my system, too, and I don't see why we'd need it. Positive review.


---

Comment by mabshoff created at 2008-11-18 18:46:00

Merged in Sage 3.2.rc2


---

Comment by mabshoff created at 2008-11-18 18:46:00

Resolution: fixed
