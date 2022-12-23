# Issue 4568: Dangerous doc test of save_session

Issue created by migration from https://trac.sagemath.org/ticket/4568

Original creator: SimonKing

Original creation time: 2008-11-20 20:21:21

Assignee: mabshoff

The doc test of `save_session` does the following:

```
        EXAMPLES:
            sage: a = 5
            sage: save_session('session')
        
        ...
        Clean up the session file we just wrote to disk.
            sage: os.unlink('session.sobj')
```


Hence, if the user happens to have a file `session.sobj` in the current directory then running the doc test would destroy it.

According to a suggestion of Robert Bradshow, using the `tempfile` Python module might help.

Unfortunately I have no idea in what file `save_session` is defined - so, no patch at that point...


---

Comment by SimonKing created at 2008-11-21 11:14:58

Meanwhile I found out that `save_session` is in `sage/misc/session.pyx`. Hence, I produced a patch that modifies three doc tests that had the above dangerous behaviour.


---

Comment by SimonKing created at 2008-11-21 11:14:58

Changing keywords from "" to "save_session temporary file".


---

Comment by mabshoff created at 2008-11-21 11:16:47

Simon,

make sure to assign a milestone when you open a ticket.

Cheers,

Michael


---

Comment by mhansen created at 2008-11-21 17:20:50

Hi Simon,

My concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.

--Mike


---

Comment by SimonKing created at 2008-11-22 11:13:30

Fixing dangerous doc test behaviour in session.pyx (2nd version)


---

Attachment

Replying to [comment:3 mhansen]:
> My concern with the current wording is that it's not entirely clear that the user should NOT save the session to a file in SAGE_TMP.  We only do that for doctesting purposes.

Hi Mike, 

Good point! I changed my patch accordingly - in the new patch I clearly say that for permanent saving SAGE_TMP would be a bad idea.

Cheers
    Simon


---

Comment by mabshoff created at 2008-11-28 20:51:33

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 20:51:33

Merged in Sage 3.2.1.rc0
