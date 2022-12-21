# Issue 4712: Make the doctest timeouts in Sage easily adjustable

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-05 06:49:41

Assignee: mabshoff

This is a left over from #717. The fix here is to define some env variables that can be used to overwrite the default doctesting timeouts. Those are defined in sage-doctest right at the top:

```
# the default timeout for doctests: 6 minutes (in seconds)
TIMEOUT      = 20
# the timeout value for long doctests: 30 minutes (in seconds)
TIMEOUT_LONG = 30 * 60
# the timeout for doctests running under valgrind tools: unreasonably long
TIMEOUT_VALGRIND = 1024*1024
```

Canonical names would be IMHO:

```
SAGE_TIMEOUT
SAGE_TIMEOUT_LONG
SAGE_TIMEOUT_VALGRIND
```

Bonus points for running some performance counter once and then adjusting the timeout by some factor on slower machines.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-06-10 23:16:38

Here's a patch; apply to the scripts repository.

(This doesn't earn the bonus points Michael referred to.)


---

Attachment

Fine by me.


---

Comment by boothby created at 2009-06-26 17:46:55

Resolution: fixed
