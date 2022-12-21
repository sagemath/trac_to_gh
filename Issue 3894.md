# Issue 3894: [with patch, needs review] in tutorial, live version, triple dots are not visible

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-08-19 03:25:20

Assignee: tba

Keywords: tutorial

In examples like this in the tutorial:

```
sage: def is_even(n):
...       return n%2 == 0
```

the three dots are not actually visible in the 'live' version of the documentation.  So change the documentation to try to reflect this.  (It would be better to have text printed conditionally, depending on whether it was for the live version, the static version, or the dvi/pdf version, but I don't know how to do that.)




---

Attachment

Looks good.  I've made this change in the ReST version of the tutorial too.


---

Comment by mabshoff created at 2008-09-16 03:50:55

Resolution: fixed


---

Comment by mabshoff created at 2008-09-16 03:50:55

Merged in Sage 3.1.2.rc5
