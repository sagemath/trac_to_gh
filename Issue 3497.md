# Issue 3497: [with patch, needs review] ignore git

Issue created by migration from https://trac.sagemath.org/ticket/3497

Original creator: ghtdak

Original creation time: 2008-06-23 21:27:35

Assignee: mabshoff

Keywords: git

updated .hgignore and added .gitignore

the rules to determine the specific file cases included may be generalizable



---

Comment by ghtdak created at 2008-06-23 21:29:36

adds .gitignore and updates .hgignore to ignore it and .git directory


---

Attachment


---

Comment by mabshoff created at 2008-07-03 07:10:46

Changing keywords from "git" to "git, editor_mabshoff".


---

Comment by mabshoff created at 2008-07-03 07:10:46

Glenn,

I would prefer if we just added `\.git` and `.gitignore` to .hgignore, i.e. not actually track .gitignore via mercurial or is the a particular reason why we would want to do that?

Cheers,

Michael


---

Comment by ghtdak created at 2008-07-04 06:02:54

The reason I suggested adding it is because I saw support for other VC's in .hgignore (darcs). There is only value to maintaining a specific .gitignore in that some work is required to build up the rules (which .c's etc to be tracked vs those which are derived objects).

OTOH, I am perfectly happy maintaining .gitignore outside the distro and simply posting something on the wiki for those few so inclined (pointer to some git repo)

A general mechanism for determining derived vs source C/C++ objects would be useful should we encounter bzr (others?)...  Perhaps there is a general strategy but I saw a number of specific targets in .hgignore


---

Comment by mabshoff created at 2008-07-31 02:53:17

After rethinking the issue I am find with tracking .gitignore in our repo. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 02:57:54

Merged in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-31 02:57:54

Resolution: fixed
