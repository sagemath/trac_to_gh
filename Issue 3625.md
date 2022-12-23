# Issue 3625: fix latex2html'ing of the sage docs, which is broken

Issue created by migration from https://trac.sagemath.org/ticket/3625

Original creator: was

Original creation time: 2008-07-09 18:28:37

Assignee: was

For some reason running latex2html to make the sage docs doesn't work -- the images rarely get built.  This must be fixed, because it causes massive frustration when I try to do releases, etc.

I suspect mistakes in paths or something else.  I don't know. 


---

Comment by was created at 2008-07-10 03:03:02

http://sage.math.washington.edu/home/was/patches/doc-3625.patch


---

Comment by mabshoff created at 2008-07-10 04:33:51

Positive review. There might be some spacing issues with the pdf, but we can sort those issues out later since an actually building documentation is much more important than some small spacing issues :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-10 04:34:12

Merged in Sage 3.0.4.rc3


---

Comment by mabshoff created at 2008-07-10 04:34:12

Resolution: fixed
