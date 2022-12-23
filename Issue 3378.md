# Issue 3378: [with patch, needs review] graphs.nauty_geng fails due to missing imports

Issue created by migration from https://trac.sagemath.org/ticket/3378

Original creator: mhansen

Original creation time: 2008-06-06 17:55:56

Assignee: rlm




---

Attachment

I suppose this didn't get caught by doctests because nauty is an optional package. Is it possible to have doctests that actually get run?

Also, in installing the optional nauty spkg, I notice that there is an interactive do-you-accept-this-license step. This doesn't seem right at all... Mabshoff, thoughts?


---

Comment by mabshoff created at 2008-06-08 22:55:42

Re the license: This is on purpose since it isn't GPL compatible and I think it is fine. It has been proposed to create a non-free repo and then stick all non-GPL compatible spkgs in there.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-08 22:57:50

Resolution: fixed


---

Comment by mabshoff created at 2008-06-08 22:57:50

Merged in Sage 3.0.3.alpha2
