# Issue 1303: Cayley graph class

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 19:45:42

Assignee: mhansen

Keywords: graphs

From Chris Godsil's wishlist and Robert Miller's reply:


```
>>> (b) Cayley graphs: These can be dealt with in GAP, but I think it would be
>>> useful to have a class, with the group and generating set explicit. Cayley
>>> graphs could be directed or undirected. Circulants and Cayley graphs
>>> for Zd (where p is prime) could be useful special cases.
> Cayley graphs are implemented, but most likely not to the extent
> anyone wants. For example, you can call cayley_graph on some groups,
> and get the graph back, but the functionality is very limited. There
> is certainly no CayleyGraph class, which would be a thousand times
> better than the current situation. Definitely create a ticket for
> this.
```



---

Comment by rlm created at 2007-12-17 15:12:17

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:12:17

Changing keywords from "graphs" to "groups".


---

Comment by rlm created at 2007-12-17 15:12:17

Changing component from combinatorics to graph theory.


---

Comment by mvngu created at 2009-09-13 10:05:10

Closing this ticket as fixed, as suggested by Nathann Cohen and Robert Miller:

```
Hello Minh !!!

This is a short conversation about ticket #1303 I had with Robert Miller, who concluded this ticket should be closed. As he says, what we need concerning Cayley graph is but the function Group.cayley_graph which already exists.

Nathann

---------- Forwarded message ----------
From: Robert Miller <rlm`@`rlmiller.org>
Date: 2009/9/2
Subject: Re: Cayley Graphs in Sage
To: Nathann Cohen <nathann.cohen`@`gmail.com>


Nathann,

We should probably get rid of this ticket. The guy who requested it is
essentially happy with what we already have. Cayley graphs are more of
a way of constructing graphs than an object on their own, i.e. a
*constructor,* which is what we already have.

On Sat, Aug 22, 2009 at 9:34 AM, Nathann Cohen<nathann.cohen`@`gmail.com> wrote:
> Hello !!!
>
> I am contacting you about the following ticket :
> http://trac.sagemath.org/sage_trac/ticket/1303
>
> You are writing about the creation of a Cayley Graph class, and it is a
> subject that interests me, even though I do not understand what you expect
> of it.... For me a Cayley Graph is just a group, so could you tell me with
> some details what you would expect for such a class ? I would like to spend
> some time on this :-)
>
> Thank you !
>
> Nathann
```



---

Comment by mvngu created at 2009-09-13 10:05:10

Resolution: fixed
