# Issue 2647: [with spkg; needs review] Fixed Debian support for linbox

Issue created by migration from https://trac.sagemath.org/ticket/2647

Original creator: tabbott

Original creation time: 2008-03-22 16:55:32

Assignee: tabbott

Apparently the debian support for linbox didn't make it into the 1.1.5 spkg whenever that was created.  Since the linbox spkg had a bunch of uncommitted changes, I've put the relevant files (with some fixes I needed to do anyway) in a new spkg; the only things changed from the old 1.1.5rc2.p4 spkg should be dist/ and spkg-debian:

http://sage.math.washington.edu/home/tabbott/linbox-1.1.5rc2.p5.spkg


---

Comment by mabshoff created at 2008-03-22 21:01:30

Hi Tim,

the updated SPKG at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha1/linbox-1.1.5rc2.p6.spkg

includes the Debian code, cleans up SPKG.txt and commits all changes to the repo.

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 21:01:49

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-22 21:01:49

Resolution: fixed
