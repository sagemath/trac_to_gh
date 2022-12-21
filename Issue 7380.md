# Issue 7380: Replace Graph.vertices() by Graph.vertex_iterator when possible

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-03 11:25:56

Assignee: rlm

As the title says, there are many places where Graph.vertices() is used when Graph.vertex_iterator ( or even self ) would be better. The same goes for edges.

Nathann


---

Comment by ncohen created at 2010-02-28 18:03:10

Useless.


---

Comment by ncohen created at 2010-02-28 18:03:10

Resolution: wontfix


---

Comment by mvngu created at 2010-02-28 20:00:54

Read [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) before closing tickets. Can you explain why you want to close this ticket?


---

Comment by ncohen created at 2010-02-28 20:07:29

Well, as I created it I thought it would not be so bad to close it too ^^;

The thing is that I do not feel anymore that this should be done, or just useful in any way. It would just slow down most functions as creating an iterator has no real sense when the whole set is already stored in memory, and it would make the code harder to read for no real purpose :p

Nathann


---

Comment by mvngu created at 2010-02-28 21:06:10

Replying to [comment:3 ncohen]:
> Well, as I created it I thought it would not be so bad to close it too ^^;

As long as you provide a good reason to close the ticket. Don't just close a ticket without any good reasons.


---

Comment by ylchapuy created at 2010-03-01 06:45:27

Sorry for commenting a closed ticket, but...

If I look at the docstring for `vertices` I see (in the default case):

```
return sorted(list(self.vertex_iterator()))
```


A new list is created, doubling the memory needed, and this list is sorted which might take time too.

I still think it might make sense to replace `vertices` with `vertex_iterator` when possible.


---

Comment by ncohen created at 2010-03-01 07:24:03

Changing status from closed to new.


---

Comment by ncohen created at 2010-03-01 07:24:03

Resolution changed from wontfix to 


---

Comment by ncohen created at 2010-03-01 07:24:03

oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...


---

Comment by mvngu created at 2010-03-01 10:53:11

Replying to [comment:6 ncohen]:
> oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...
*Do not* reopen this ticket. Let it die and open a new ticket.


---

Comment by mvngu created at 2010-03-01 10:53:11

Resolution: worksforme
