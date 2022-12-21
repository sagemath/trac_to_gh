# Issue 2182: undefined symbol: gzopen64 when starting the notebook()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-16 22:13:06

Assignee: mabshoff

The issue was reported in https://groups.google.com/group/sage-support/t/8f03a6f2f3d0aea8 by Matthias Hillenbrand:

```
Hello,

Since I have upgraded to SAGE 2.10.x I get the following error message
when starting the notebook:

gnome-www-browser: symbol lookup error: /usr/lib/libxml2.so.2:
undefined symbol: gzopen64

I get this error message on two different computers (one running
Ubuntu 7.10 the other Debian Testing, which I installed today) and
with any browser (e.g. Firefox as standard browser). If I open a
session of the browser before starting SAGE, the error won't occur.
```


Jason Grout figured out that `SAGE_ORIG_LD_LIBRARY_PATH` is being overwritten improperly when the second Sage session starts (due to the launch of the notebook). He has proposed a fix and is working on a patch which will hopefully make it into 2.10.2.

Cheers,

Michael


---

Comment by jason created at 2008-02-17 03:07:11

To be applied to the sage repository.


---

Attachment

To be applied to the sage-scripts repository (changes sage-env)


---

Comment by jason created at 2008-02-17 03:12:58

The sage patch above fixes the open_page function (which opens the notebook in the browser) to use the standard sage mechanism for opening an external app instead of the previously hard-coded way.  The sage-scripts patch changes sage-env so that recursively run sage sessions do not clobber the saved original LD_LIBRARY environment variable.


---

Comment by mabshoff created at 2008-02-17 04:11:48

Both patches look good to me. Positive review. Thanks for the excellent work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 04:14:15

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 04:14:15

Merged in Sage 2.10.2.alpha1
