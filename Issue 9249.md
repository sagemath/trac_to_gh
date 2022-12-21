# Issue 9249: Wrong answer in is_hamiltonian if no LP solver available

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-06-16 13:15:47

Assignee: jason, mvngu, ncohen, rlm

CC:  mvngu

is_hamiltonian always returned False when no LP solver was installed.

Fixed !

Nathann


---

Comment by ncohen created at 2010-06-16 13:16:51

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-06-17 10:29:54

Here it is ! We should also take care of updating the Developper's guide concerning the use of this new exceptions in another ticket.

Nathann


---

Comment by wdj created at 2010-06-17 15:11:27

This seems to be installing and passing tests okay but I'm not seeing any new docstring tests that correspond to the new code. Am I missing something? If not, I think more tests should be added (eg, Minh's OP on sage-devel in the thread cited above).


---

Comment by ncohen created at 2010-06-17 15:14:50

Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag "optional CBC", but nothing like "optional NOT CBC" ^^;

Nathann


---

Comment by wdj created at 2010-06-17 15:22:26

Replying to [comment:4 ncohen]:
> Hmmm.... It is a bit hard to test, though. Minh's commands fails when no LP solver is installed. If we make a docstring for it, the docstring will pass when there is no solver installed, but as soon as a solver is, the doctest will fails. The problem is that we have a flag "optional CBC", but nothing like "optional NOT CBC" ^^;
> 
> Nathann

Good point!

I wonder what you think about this idea:

Add a not tested docstring  (I've forgotten how you do that though) which has one
test in the case when the package is loaded and another test in the case when the package is not. There there could be a remark that only one of these will trigger an error exception?


---

Comment by ncohen created at 2010-06-17 15:57:06

What do you think of this ? :-)

Nathann


---

Attachment


---

Comment by rlm created at 2010-06-17 20:27:14

This looks good for now... Applies and passes tests. However, we should use dancing links (exact cover) for is_hamiltonian in general. It may actually turn out to be faster than MILP, I'm not sure. But then it would be a standard feature.


---

Comment by rlm created at 2010-06-17 20:27:14

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-06-17 20:30:09

You think it can be reduced to dancing links ?? O_o

How so ? O_o

I'm *very* interested !!

Nathann


---

Comment by rlm created at 2010-06-17 20:35:59

Replying to [comment:8 ncohen]:
> You think it can be reduced to dancing links ?? O_o
> 
> How so ? O_o
> 
> I'm *very* interested !!
> 
> Nathann

It might be a bit of a challenge. As Tom Boothby points out, bipartite matching can easily be reduced to dancing links. We should use that where we can, instead of using optional packages.


---

Comment by ncohen created at 2010-06-17 20:38:32

Well, I clearly agree for bipartite perfect matching, but for is_hamiltonian ? How the hell could we translate the "connexity" constraint ?

And... Well... :p

I know LP is optional in Sage, but... Well, there are now **many** important functions that use LP, so even if it is optional because of license problems, it is more and more part of Sage's graph library :p

Nathan


---

Comment by rlm created at 2010-06-29 16:46:41

Resolution: fixed


---

Comment by mpatel created at 2010-07-22 02:58:36

The patch here leads to a docbuild warning:

```
Warning: Missing title for sage.misc.exceptions
```

Please see #9571, a blocker for Sage 4.5.2.
