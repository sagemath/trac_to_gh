# Issue 4234: typos in programming guide

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2008-10-02 01:41:52

Assignee: tba

CC:  mhansen

Keywords: programming guide, prog.tex

This patch fixes various typos and annoying white spaces in the programming guide, i.e. the file prog.tex. Many .tex files contain trailing white spaces, which I personally find annoying when I view/edit them from within a terminal emulator. If other folks also find trailing white spaces annoying, then this patch fixes that annoyance in prog.tex. Otherwise, just leave those trailing white spaces as is and consider the typos.


---

Attachment


---

Comment by mabshoff created at 2008-10-02 03:29:17

Patch looks good to me. Positive review.

Mike: please make sure to merge the changes into the ReST version of the programming guide. As Minh mentioned a lot of the diff is deleting trailing spaces.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-02 03:32:24

Resolution: fixed


---

Comment by mabshoff created at 2008-10-02 03:32:24

Merged in Sage 3.1.3.alpha3


---

Comment by mhansen created at 2008-10-02 07:59:32

I've made these changes in the ReST documentation.
