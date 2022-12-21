# Issue 3367: rename CachedFunction to cached_function

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-06-04 21:06:05

Assignee: cwitty

CC:  mhansen

I wrote over at #3254:
Is CachedFunction the right name though? Shouldn't it be cached_function? I think there is a different style convention for the persistent and the cached functions which is a bummer.


---

Comment by mhansen created at 2008-06-04 22:04:00

Yep, I think it should be cached_function (in fact, I import it as cached_function in my code).  CachedFunction should be deprecated.


---

Comment by malb created at 2008-09-20 15:58:15

This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.


---

Comment by mabshoff created at 2008-09-20 20:51:22

Replying to [comment:2 malb]:
> This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.

I thought so, too, but cached_function is just an alias for CachedFunction in the code. To close this ticket the code should be moved to cached_function and CachedFunction should be officially deprecated.

Cheers,

Michael


---

Comment by malb created at 2008-09-28 14:21:14

CCing Mike as he wrote the code in question.


---

Comment by malb created at 2009-01-21 02:39:20

Does it actually hurt to have the alias? I vote for closing the ticket.


---

Comment by mhansen created at 2009-01-21 02:40:54

I think the alias is fine too.  Since CachedFunction is a class, it conforms to the naming convention for classes.


---

Comment by malb created at 2009-02-04 21:35:04

Resolution: wontfix
