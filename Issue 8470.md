# Issue 8470: new documentation categories "FAQ" and "Sage HOWTOs"

Issue created by migration from https://trac.sagemath.org/ticket/8470

Original creator: mvngu

Original creation time: 2010-03-07 02:38:29

Assignee: mvngu

CC:  wdj rlm ncohen rbeezer sage-combinat bump jhpalmieri jason

Keywords: FAQ, HOWTO

This is a meta-ticket that helps in organizing changes and additions to the Sage standard documentation. On [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc), it is proposed that we create two new documentation categories called:

 * FAQ --- a collection of answers to frequently asked questions.
 * Sage HOWTOs --- a collection of in-depth tutorials on specific topics.

For starters, here is a list of tickets with enhancements for those two new documentation categories:

 * #8442 Lie Methods and Related Combinatorics
 * #8464 FAQ
 * #8465 Python Functional Programming for Mathematicians
 * #8466 Sage and Coding Theory
 * #8467 Linear Programming in Sage
 * #8468 Group Theory and Sage: A Primer
 * #8469 Number Theory and the RSA Public Key Cryptosystem

Once all the above tickets are closed, the current ticket can be closed as fixed.


---

Comment by nthiery created at 2010-03-08 10:26:55

This sounds very good! Should the following appear there as well?

 - the category primer (sage.categories.primer)
 - the "implementing a parent" tutorial (sage.categories.tutorial); this needs further work!

For the record, in the Sage-Combinat queue, some work is being done on:

 - A tutorial on iterators
 - A tutorial on combinatorics


---

Comment by mvngu created at 2010-03-09 21:45:47

Changing keywords from "FAQ, HOWTO" to "FAQ, HOWTO, tutorial".


---

Comment by bump created at 2010-03-15 23:34:33

Here is a more complete list of patches that are relevant
to this metaticket:


```
trac_8480-clean-up.patch
trac_8464-faq-general.patch
trac_8464-faq-usage.patch
trac_8464-faq-contribute.patch
trac_8464-ref.patch
trac_8465-functional.patch
trac_8469-rsa.patch
trac_8468-groups.patch
trac_8411_branching_rules.patch
trac_8414_weyl_group_space.patch
trac_8442-lie-rebased.patch
trac_8442-reviewer.patch
trac_8492-ref.patch
```


In addition three .png files from #8442 need to be copied into 
`doc/en/thematic_tutorials/static`.

With this preparation, the pdf and html documentation build and look very good.


---

Comment by rws created at 2014-08-18 05:34:31

All done!


---

Comment by rws created at 2014-08-18 05:34:31

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-08-27 15:44:15

We certainly need better organization of documentation, but this ticket has achieved its purpose, you are right.  Too bad #8533 isn't finished yet, but oh well.


---

Comment by kcrisman created at 2014-08-27 15:44:15

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-29 18:33:49

Resolution: fixed
