# Issue 4108: [with patch, needs review] disable hmm.pyx and chmm.pyx doctests

Issue created by migration from https://trac.sagemath.org/ticket/4108

Original creator: mabshoff

Original creation time: 2008-09-12 23:23:15

Assignee: mabshoff

Due to a bug in ghmm (tracked at #3984) the doctests in chmm.pyx and hmm.pyx segfault all over the map. So disabled them globally for now until that issue is resolved.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-09-12 23:24:56

Let's get 3.1.2 out!


---

Comment by mabshoff created at 2008-09-12 23:26:05

Resolution: fixed


---

Comment by mabshoff created at 2008-09-12 23:26:05

Merged in Sage 3.1.2.rc2
