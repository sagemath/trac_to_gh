# Issue 6763: [with patch, needs review]  Bin Packing (uses Linear Programming)

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-16 16:14:34

Assignee: jkantor

This patch implements a solver for the Bin Packing problem using Linear Programming.. Sorry again, but to test this you will have to first install GLPK (just type sage -i glpk 4.38) and the patch AllMIP #6502 ;-)

I hope you will like the documentation, I tried to make it clean ;-)


---

Comment by ncohen created at 2009-08-31 15:55:23

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-06 16:56:04

New version, ready for review !!!!

Nathann


---

Comment by robertwb created at 2010-01-20 10:13:23

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-01-20 10:13:23

What is the output format? You should include several more examples. Also, unless success returns True, it's better to raise an error on failure than return False.


---

Comment by ncohen created at 2010-01-21 14:27:38

updated... This patch was 5 months old and was not working anymore ;-)

Nathann


---

Comment by ncohen created at 2010-01-21 14:27:38

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-21 20:07:59

Thanks, that clarifies things more. I would raise a ValueError rather than a generic exception. Also, you still need more examples. (You never actually even show the output.)


---

Comment by ncohen created at 2010-01-22 06:59:19

Well, maybe you can help me for the output : I deliberately avoided to show it as a valid solution [A,B] could be returned [B, A], for example... It depends on the solvers you use, but also on the platform (hashing functions depend on it, I learnt that recently from William and it was breaking som eof my docstring). How do you think we could avoid it ? :-)

Nathann


---

Comment by robertwb created at 2010-01-22 07:28:04

Sort the result before printing.


---

Comment by ncohen created at 2010-01-22 08:59:37

Done


---

Comment by jsyri created at 2010-05-11 09:49:26

Changing status from needs_review to needs_work.


---

Attachment

I think check should be added to make sure all weights are <= max. At the moment


```
binpacking([1,2,3],2)
```

causes infinite loop. Otherwise code seems fine.


---

Comment by ncohen created at 2010-05-11 21:00:39

Patch updated !! With a few other modifications, as this patch is one of the first LP patches Trac received, and is even older than the 8 months this ticket indicates... I'm not sorry to see it finally reviewed ! :-)

By the way, if you like Linear Programming and have some time to spend on trac tickets... I desperately need some help with LP patches in the Graph Theory section ;-)

Thank you very much !

Nathann


---

Comment by ncohen created at 2010-05-11 21:00:39

Changing status from needs_work to needs_review.


---

Comment by jsyri created at 2010-05-12 11:07:03

Changing status from needs_review to needs_work.


---

Comment by jsyri created at 2010-05-12 11:07:03

One last thing, I'm sorry I didn't catch it first time around. Documentation for the parameter 'k'  claims function will return false if solution doesn't exist. Instead exception is raised if no solution exists.


---

Comment by ncohen created at 2010-05-12 17:39:38

Fixed.


---

Comment by ncohen created at 2010-05-12 17:39:38

Changing status from needs_work to needs_review.


---

Comment by jsyri created at 2010-05-12 18:03:38

Changing status from needs_review to positive_review.


---

Attachment

Everything seems to be in order. Positive review.


---

Comment by ncohen created at 2010-05-12 18:09:03

Thank youuuuuuuuu :-)

Nathann


---

Comment by mhansen created at 2010-06-07 04:52:17

Resolution: fixed
