# Issue 1959: [with spkg] Solaris 9 fixes for rubiks

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-28 04:37:36

Assignee: mabshoff

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/rubiks-20070912.p1.spkg

builds fine on Solaris 9, OSX and Linux.

Cheers,

Michael 


---

Comment by mabshoff created at 2008-01-28 04:37:44

Changing status from new to assigned.


---

Comment by jkantor created at 2008-01-28 04:51:26

Spkg compiles fine, tested cube, works ok.


---

Comment by mabshoff created at 2008-01-28 05:06:11

Resolution: fixed


---

Comment by mabshoff created at 2008-01-28 05:06:11

Merged in Sage 2.10.1.rc2


---

Comment by robertwb created at 2008-01-28 19:11:24

Has this fix been reported upstream?


---

Comment by mabshoff created at 2008-01-28 21:38:47

Replying to [comment:4 robertwb]:
> Has this fix been reported upstream?

Nope, not yet. It is mostly a work around for neron since the Sun compiler on there is busted. In fact, Sun stopped shipping their compiler suit for free [as in beer] many years ago, but recently started to offer them again for free [as in beer]. I can send a patch upstream, but the fix is trivial, i.e. replacing a hard coded `cc` in the makefile of the dik solver with `$(CC)`.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-28 22:08:20

That sounds pretty trivial. I just emailed the author, with a link to this page.
