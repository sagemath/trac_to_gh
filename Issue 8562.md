# Issue 8562: Categories for IntegerMod rings

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-03-19 21:48:27

Assignee: AlexGhitza

CC:  sage-combinat

Keywords: categories, integer mod rings

After this patch, IntegerModRing's inherit properly from categories:

```
    sage: Z3 = IntegerModRing(3)
    sage: Z3.category()
    Category of fields
    sage: TestSuite(Z3).run(verbose = True)
    running ._test_additive_associativity() . . . pass
    running ._test_an_element() . . . pass
    running ._test_associativity() . . . pass
    running ._test_category() . . . pass
    running ._test_elements() . . . 
      Running the test suite of self.an_element()
      running ._test_category() . . . pass
      running ._test_not_implemented_methods() . . . pass
      running ._test_pickling() . . . pass
      pass
    running ._test_not_implemented_methods() . . . pass
    running ._test_one() . . . pass
    running ._test_pickling() . . . pass
    running ._test_prod() . . . pass
    running ._test_some_elements() . . . pass
    running ._test_zero() . . . pass
```


This is required to use the cool features from #7555.


---

Comment by nthiery created at 2010-03-19 22:29:54

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-03-19 23:08:22

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-03-19 23:08:22

Ok, the tests passed fine up to some trivialities (*_with_category class name changes). I'll fix this and upload an updated patch soon. The review can start in parallel


---

Comment by rbeezer created at 2010-03-20 04:29:21

This applies, builds and limited testing (prime and composite orders) indicates that it plays nicely with "addition tables" at #7555 which rely heavily on the category framework.  Didn't run tests, but witnessed no problems otherwise.

Good to see how easy it is to insert a new object into the category framework.

I'll come back when the patch is completed.


---

Comment by davidloeffler created at 2010-03-21 14:27:54

Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.

David


---

Comment by nthiery created at 2010-03-21 20:40:55

Replying to [comment:4 davidloeffler]:
> Just a heads-up: this looks rather like it might clash with #8218, which is the first of several patches by David Roe which do a substantial amount of work improving finite fields. #8218 has been held up for ages because it moves loads of files around (without substantially changing their content) so even small changes to finite fields will cause conflicts, and there is a lot of really good code waiting on it, so it would be a shame to have to put it off even longer.

Thanks for the notice. There is no urgency for that one, so sure, if there is any conflict, #8218 should go first.

David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.


---

Comment by nthiery created at 2010-03-21 20:55:02

> David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.

Note: I meant David Roe, but any other David is welcome too :-)

Oh: would you agree to take over that patch, and finalize it (or ping me) when it's ripe to get in?

(then I could forget about it).


---

Comment by nthiery created at 2010-03-21 20:55:02

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-03-22 22:11:12

Changing type from defect to enhancement.


---

Comment by nthiery created at 2010-03-22 22:11:12

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-03-22 22:13:34

Replying to [comment:6 nthiery]:
> > David: I won't be touching this patch further. Feel free to update / refactor / merge /... it within the other series of patch whenever it feels right.

Well, actually I did. But I should be done now, unless I notice a test failure.


---

Attachment


---

Comment by jhpalmieri created at 2010-06-21 18:45:30

Here's a rebased patch.  It looks good and all tests pass for me so I'm willing to give it a positive review, but since I made the rebased patch, can someone else (Nicolas, for example) take a look at it also?


---

Comment by nthiery created at 2010-06-21 20:11:37

Hi John!

Thanks much for rebasing the patch. I looked through the changes, and am happy to give my green light, up to three minor comments:

 * Is the convention to use as ticket summary "trac 8562:" or "#8562:"? (I personally prefer the later).
 * With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.
 * I like the options `nodates=1` and `showfunc = 1` of hg :-)

I let you set up the positive review as you feel appropriate.

Thanks again,
                          Nicolas


---

Comment by jhpalmieri created at 2010-06-21 20:36:50

Replying to [comment:10 nthiery]:
 
> Is the convention to use as ticket summary "trac 8562:" or "#8562:"? (I personally prefer the later).

I think either is fine.  I've been using "trac 8562" for a while and have not had any complaints from release managers.

>  * With the updated patch, sage -coverage complains because of the absence of #indirect doctest for create_object in sage/rings/finite_rings/integer_mod_ring.py. Just wanted to check; if this is voluntary, because you consider that this requires better tests, that's all fine with me.

This wasn't voluntary, it was an oversight.  I'll fix it.

>  * I like the options `nodates=1` and `showfunc = 1` of hg :-)

Nice, I didn't know about those.


---

Comment by jhpalmieri created at 2010-06-21 20:37:25

rebased version. apply only this patch.


---

Attachment


---

Comment by jhpalmieri created at 2010-06-21 20:37:58

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:23:50

Resolution: fixed
