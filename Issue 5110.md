# Issue 5110: rewrite diagonal_matrix to be more general

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-27 03:54:59

Assignee: was

See the patches at #3704, which rewrite diagonal_matrix.  On that ticket, however, we finally just went with a basic patch that fixed the specific bug mentioned.  There is good code in the other patches that ought to be used, though.  This ticket is here so that we eventually use the cleaner rewrite contained in the first patches at #3704.


---

Comment by @black-stones created at 2018-05-26 14:00:00

What exactly should be added to diagonal_matrix? I'd be happy to work on this ticket but it looks like the other patches in #3704 add doctests.


---

Comment by kcrisman created at 2018-05-30 17:09:19

I think the idea is to use attachment:trac-3704-diagonal_matrix.patch:ticket:3704 to make a more generally applicable function.

That said, there are probably more important tickets to work on, notably reviewing many in symbolics ...


---

Comment by @black-stones created at 2018-05-30 21:09:57

I did see that patch, but looking at the source code for diagonal_matrix(), the differences seem to be

1. Changing the parameters
2. More comments and doctests
3. Casting to Sequence

1 could be a good fix since the current function uses "arg0, arg1, arg2" which is pretty bad, but in my opinion, 2 and 3 are not necessary (although if we do change 1 we will need to change 2).


---

Comment by slelievre created at 2019-12-14 00:07:10

Changing status from new to needs_review.


---

Comment by slelievre created at 2019-12-14 00:07:10

This is probably solved by #10604 (please check).


---

Comment by tscrim created at 2019-12-27 17:13:27

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2019-12-27 17:13:27

I think so as well.


---

Comment by slelievre created at 2019-12-27 22:09:24

Resolution: duplicate
