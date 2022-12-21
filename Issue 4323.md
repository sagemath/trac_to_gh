# Issue 4323: sage-coverage expects doctests for closures

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-10-19 05:41:59

Assignee: tbd

CC:  zimmerma

Unfortunately, there is often no way to doctest such functions directly, and for some re-writing them as lambda functions is impossible or reduces readability. 


---

Comment by robertwb created at 2008-10-19 05:42:20

Changing assignee from tbd to mabshoff.


---

Comment by robertwb created at 2008-10-19 05:42:20

Changing component from algebra to doctest.


---

Comment by jhpalmieri created at 2009-02-09 23:45:03

Is this the same as #877?

  John (who's not quite sure what "closures" are)

P.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)


---

Comment by mabshoff created at 2009-02-09 23:47:54

Replying to [comment:4 jhpalmieri]:
> Is this the same as #877?
> 
>   John (who's not quite sure what "closures" are)

Not sure.

> P.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)

Yes, this certainly registered rather strongly on my irony meter, but right now there is no coverage for the scripts in local/bin, even though most people agreed that it would be a pretty good idea. This will hopefully happen sooner or later.

Cheers,

Michael


---

Comment by zimmerma created at 2009-02-10 07:16:38

> Is this the same as #877?

yes.


---

Comment by mabshoff created at 2009-02-10 07:19:08

Resolution: duplicate


---

Comment by mabshoff created at 2009-02-10 07:19:08

Since this is a dupe of #877 I am closing this ticket as a dupe. 

If someone disagrees please reopen.

Cheers,

Michael
