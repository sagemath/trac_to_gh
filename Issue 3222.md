# Issue 3222: sqlite -- add cygwin support to sqlite

Issue created by migration from https://trac.sagemath.org/ticket/3222

Original creator: was

Original creation time: 2008-05-16 17:29:15

Assignee: mabshoff

See the related trac ticket #3176. 

This spkg:

  * adds an hg repo
  * patches the Makefile.in
  * adds an SPKG.txt (but probably not as complete as some would want, since maybe already mabshoff did that for #3176!).


---

Comment by mhansen created at 2008-05-17 09:11:28

This spkg builds for me under cygwin.


---

Comment by mabshoff created at 2008-05-18 12:43:41

Spkg looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 12:43:55

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 12:43:55

Resolution: fixed
