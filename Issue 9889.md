# Issue 9889: A proper random_element() method for PerfectMatchings

Issue created by migration from https://trac.sagemath.org/ticket/9890

Original creator: ncohen

Original creation time: 2010-09-10 15:44:15

Assignee: sage-combinat

CC:  nthiery fhivert

At the moment, the method `random_element()` from PerfectMatchings computes a random matching by picking a random integer between 0 and the number of matchings on n elements, then (I presume) enumerating all the matchings according to some ordering until the `k`th has been computed. This is impressively useless.


```
sage: %timeit PerfectMatchings(12).random_element()
5 loops, best of 3: 1.5 s per loop
```


By the way, I was not able to write a method to obtain the list of pairs describing the matching from an PerfectMatching object.. I don't understand how this class is written, and I have no idea why it needs to be so complicated (but it would be nice to add it to this ticket during the review, if someone gets how it works).

The method random_element (and also an_element) both raise an exception when the set of elements is EMPTY. I also fixed the doctests.

(I don't even get why you can build a PerfectMatchings class on an odd number of elements in the first place)

I expect this ticket could be heavily modified during review, but there is a problem with these classes at the moment.

Nathann


---

Comment by ncohen created at 2013-03-23 11:21:42

I forgot to click on `needs_review` three years ago `T_T`

Nathann


---

Comment by ncohen created at 2013-03-23 11:33:36

Changing status from new to needs_review.


---

Comment by ncohen created at 2013-03-23 11:33:36

Patch updated ! On the way, I also fixed this "small problem" :


```
sage: PerfectMatchings(3).an_element()
[(1, 2)]
```


Nathann


---

Attachment


---

Comment by chapoton created at 2013-05-17 19:22:32

hello,

looks good to me.

I have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)

if my review patch is ok for you, you can set a positive review


---

Comment by ncohen created at 2013-05-18 10:14:47

Changing status from needs_review to positive_review.


---

Attachment

> I have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)
> 
> if my review patch is ok for you, you can set a positive review

Okayyyyyyy ! Good to go, then `:-)`

By the way, how do you use pep8 and pyflakes ? Do you run them externally on files or do you have a way to use them ?

Nathann


---

Comment by chapoton created at 2013-05-18 18:36:27

Yes, I just run them on the *.py files. Pyflakes is more important, as it finds missing imports and unused variables. Pep8 is much more for the cosmetic, but can check that raise statements are in python3 syntax and find other deprecated syntax.


---

Comment by jdemeyer created at 2013-05-22 08:18:32

Resolution: fixed
