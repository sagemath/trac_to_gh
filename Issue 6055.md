# Issue 6055: Top level README.txt is wrong reguarding Solaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-05-17 08:38:17

Assignee: mabshoff

CC:  david.kirkby@onetel.net

The top level README.txt has a few problems reguarding Solaris.

1) It says:
----------------------------
  SOLARIS:
     It is reportedly possible, but not recommended yet (see below).
     A fully supported port is planned.
----------------------------

But there is nothing below that. 

2) The OS is spelled as Solaris and SOLARIS. Makes searching more difficult. If you must use SOLARIS, then put 'Solaris' in a word close by. i.e, something like:

----------------------------
  SOLARIS:
     It is reportedly possible to build Sage on Solaris, but not recommended yet (see below).
     A fully supported port is planned.
----------------------------




---

Comment by mpatel created at 2010-08-07 04:29:29

Should I close this ticket as a "duplicate" of #9226?


---

Comment by drkirkby created at 2011-04-02 12:49:37

Replying to [comment:3 mpatel]:
> Should I close this ticket as a "duplicate" of #9226?

This should indeed be closed now. It can be considered fixed by #9226 in sage-4.5.2 , though I would not call it a duplicate, as #9226 was created long after this ticket. 

Dave


---

Comment by jdemeyer created at 2011-04-05 15:55:08

Resolution: duplicate
