# Issue 4979: do not use xdg-open on Solaris to open the browser when starting the notebook

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-15 00:54:44

Assignee: mabshoff

CC:  dimpase mkoeppe

See http://groups.google.com/group/sage-devel/browse_thread/thread/f037b3c4cc4509eb for a discussion about the problem.

xdg-open is not available on Solaris, so we should be using a Solaris specific mechanism to open the default browser. It is unclear at least to me at the moment what this would be.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-15 01:19:32

We should use sdtwebclient for now on Solaris since it is the default way to open a url by the default system browser on Solaris:

```
-bash-3.00$ /usr/dt/bin/sdtwebclient --help
/usr/dt/bin/sdtwebclient[117]: getopts: help bad option(s)
Usage: sdtwebclient [-b browser] [-o browser_opts] url-string
-bash-3.00$ man sdtwebclient
No manual entry for sdtwebclient. [:(]
```


Cheers,

Michael


---

Comment by drkirkby created at 2010-02-23 12:08:56

I've just seen a bug report of this on sci.math.symbolic and comp.unix.solaris. 

I found this bug report on comp.unix.solaris and sci.math.symbolic

http://groups.google.com/group/comp.unix.solaris/msg/ce5b85e425cdcb90?hl=en

I thought this has been fixed on a recent patch, but I must admit I can't find it. This obviously needs solving asap. I'll work on this. 


Dave


---

Comment by chapoton created at 2020-05-03 08:11:27

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-05-03 08:11:27

I propose to close this ancient ticket about deprecated SageNB. Agreed ?


---

Comment by dimpase created at 2020-05-03 09:31:40

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-05-03 09:38:33

thanks. Closing as invalid.


---

Comment by chapoton created at 2020-05-03 09:38:33

Resolution: invalid
