# Issue 2759: [with patch; needs review] SAGE debian/ directory updates

Issue created by migration from https://trac.sagemath.org/ticket/2759

Original creator: tabbott

Original creation time: 2008-04-01 19:02:19

Assignee: tabbott

I'm attaching the changes to the SAGE debian/ directory that were needed to make it actually do Debian builds


---

Attachment

Patch looks good to me. One problem is that it is against some non-existing repo, i.e. one that should be in `data/extcode/dist`. I don't have one there and all the files are check into the repo in `data/extcode/`. I applied the patch via GNU patch and committed in Tim's name. The applied patch is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/trac_2759_sage-debian-build.patch

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 19:28:55

Resolution: fixed


---

Comment by mabshoff created at 2008-04-01 19:28:55

Merged in Sage 3.0.alpha0
