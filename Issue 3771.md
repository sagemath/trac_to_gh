# Issue 3771: [with patch; needs review] make it so typing "sage -br" for new binary sage installs doesn't require rebuilding everything

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-04 00:35:32

Assignee: mabshoff

Hundreds of times people have been very annoyed when the install a fresh binary sage install, change something in the core library and type

```
  sage -br
```

only to find that everything has to be built.   It turns out there is a trivial 2-line fix to make this not be the case.  That's attached to this ticket.


---

Attachment

This is fantastic! I'm really excited that you sat down and fixed this.


---

Comment by mabshoff created at 2008-08-09 00:56:11

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-09 00:56:11

Resolution: fixed
