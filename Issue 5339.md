# Issue 5339: update README.txt to reflect what platforms we currently supporting building sage with

Issue created by migration from https://trac.sagemath.org/ticket/5339

Original creator: was

Original creation time: 2009-02-22 18:52:08

Assignee: mabshoff

CC:  drkirkby




---

Comment by mabshoff created at 2009-03-01 02:55:06

Better luck in Sage 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 03:55:40

This is also relevant (from David Kirkby):

```
Looking at the top level README.txt in sage-3.4.2.alpha0, there are a
couple of things about Solaris of note. The first is minor - the second
less so.

1) At one point its called Solaris, and another SOLARIS. After finding
'Solaris' at the top, I did a search (using vi as the editor) and found
little reference to it. Later I see the operating system referred to as
SOLARIS. It might be worth using the same case, or at least referring to
it as 'Solaris' in the 'SOLARIS' section, in case someone does a
case-sensitive search.

2) More importantly, one reads:
-----------
    SOLARIS:
      It is reportedly possible, but not recommended yet (see below).
      A fully supported port is planned.
-----------

But there is NOTHING below that point in the README.txt about Solaris -
despite the "see below" in there.

It would be worth either putting what information was planned about
Solaris in the README.txt, or making a 'Solaris.txt' with what
information is needed. Obviously a link to the tool chain would be worth
putting. 
```



---

Comment by mpatel created at 2010-08-07 04:36:11

Should I close this as a "duplicate" of #9487?


---

Comment by drkirkby created at 2010-08-07 10:14:55

Replying to [comment:3 mpatel]:
> Should I close this as a "duplicate" of #9487?

Yes, that seems reasonable. Technically #9487 is a duplicate of this, but there's more useful information on #9487. This has also at least partially been fixed by another ticket, so I would close it. 

Dave


---

Comment by mpatel created at 2010-08-07 10:15:40

Resolution: duplicate
