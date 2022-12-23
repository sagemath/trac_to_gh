# Issue 3027: [with patches; needs review] Debian lintian fixes

Issue created by migration from https://trac.sagemath.org/ticket/3027

Original creator: tabbott

Original creation time: 2008-04-26 01:30:09

Assignee: tabbott

I ran lintian (the Debian packaging error checking tool) on all my packages, and found a bunch of bugs.  I guess the Debian build system is too automated for me to notice these normally.  I've attached a bunch of patches to fix many of these bugs (some others I reported upstream).


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-26 02:45:37

Patches look good to me. I have slipped them all into their respective spkg without bumping the patch level to avoid forces rebuilds on upgrade. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 02:45:49

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 02:45:49

Merged in Sage 3.0.1.alpha0
