# Issue 2311: remove stupid timeout from sage-location

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-26 04:44:56

Assignee: mabshoff




---

Attachment


---

Comment by was created at 2008-02-26 04:47:11


```
>  > $ wgethttp://sagemath.org/SAGEbin/linux/64bit/sage-2.10.2-debian-64bit-inte...
>  
> > $ tar xzf sage-2.10.2-debian-64bit-intel-x86_64-Linux.tar.gz
>  > $ ln -s sage-2.10.2-debian-64bit-intel-x86_64-Linux/ sage
>  > $ cd sage
>  > $ ./sage
>  > ----------------------------------------------------------------------
>  > | SAGE Version 2.10.2, Release Date: 2008-02-22                      |
>  > | Type notebook() for the GUI, and license() for information.        |
>  > ----------------------------------------------------------------------
>  > The SAGE install tree may have moved.
>  > Regenerating Python.pyo and .pyc files that hardcode the install PATH
>  > (please wait less than a minute)...
>  > Please do not interrupt this.
>  > /home/ondra/ext/sage/local/bin/sage-sage: line 149: 18575 Alarm clock
>  >            "$SAGE_ROOT/local/bin/"sage-location
>  
>  I just grepped through my tree and there is no "Alarm clock" string
>  anywhere. I also checked the binary you tried and there is no string
>  in there either. The log in SAGE_LOCAL/bin doesn't indicate any
>  commits that I don't have and the repo is clean, i.e. no outstanding
>  changes.
>  
>  So: can anybody else reproduce this?

This is in sage-location:

import signal   
signal.alarm(360)

This is *stupid*.  It's doing a process that really really better not get interrupted, and it's
interrupting itself if it takes more than 6 minutes.  I can't imagine what idiot wrote such 
bad code....

... oh wait, that was me.  I think that was in there right when that code was first written,
mainly for debugging purposes when I was doing some testing.  Anyway...  didn't
David Harvey say something in irc about all my old code being "impatient" -- I guess
this is a prime example of that!

```



---

Comment by mabshoff created at 2008-02-26 04:59:20

Patch looks good.


---

Comment by mabshoff created at 2008-02-26 04:59:37

Merged in Sage 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-26 04:59:37

Resolution: fixed
