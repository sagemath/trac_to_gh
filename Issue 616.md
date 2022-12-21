# Issue 616: sage -coverage improvements

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-09-07 06:23:11

Assignee: craigcitro

sage -coverage is currently easy to trick: just add a doctest that doesn't actually test your function. This can also happen by accident: if you copy-paste a function, and then don't look at the docstring, you end up with a function that has fake doctests. (This occurs in various places in the sage source code.) 

This patch makes sage -coverage a little smarter: it looks every time to make sure that the function name occurs in the doctests, and if not, adds the function to a list of "possibly wrong" functions that it spits out at the end. If the function begins and ends with __, we don't bother looking for the name in the docstring. Also, if the string 'indirect doctest' occurs anywhere, we don't look. 

This patch also sneaks in a change so that scons is replaced by scons -Q, making it quieter whenever it's called. Time for the first line-item veto in a sage patch? :)


---

Attachment


---

Comment by craigcitro created at 2007-09-07 06:24:37

Yeah, I just got bit by trac formatting. In the above, it says that if the function name begins and ends with a double underscore (such as add, etc).


---

Attachment

trac_616_pt2.hg makes sage -coverage just a bit smarter.


---

Comment by mabshoff created at 2007-09-07 19:08:59

Didn't make it, retagged for 2.9

Cheers,

Michael


---

Comment by craigcitro created at 2007-09-07 22:29:11

Changing status from new to assigned.


---

Comment by craigcitro created at 2007-10-12 21:44:53

Actually, I'm adding one more patch, that's a combination of the previous two. I don't know how to remove a file I've added, sadly.


---

Attachment

I should have mentioned that in addition, the previous two patches made some modifications to the scons/c_lib stuff that no longer applies, so definitely use sage-coverage.hg. This is a patch against $SAGE_ROOT/local/bin.


---

Comment by was created at 2007-10-13 06:34:19

Resolution: fixed
