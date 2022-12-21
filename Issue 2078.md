# Issue 2078: programming guide: section "quick Mercurial tutorial for Sage" is wrong/misleading

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-02-07 04:23:52

Assignee: tba

It says:

1. clone the main branch
2. implement new functionality in the clone, test
3. commit changes to clone
4. pull changes into main branch
5. export patch or bundle, and contribute it

There are good reasons why one shouldn't do step 4, since it taints the main branch with code that hasn't been reviewed, etc.


---

Comment by mabshoff created at 2008-08-25 21:32:05

This ticket can be closed once #3905 has been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 07:58:49

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 07:58:49

Since #3905 has been merged this can be closed. In case you want improvements please open a specific followup ticket.

Cheers,

Michael
