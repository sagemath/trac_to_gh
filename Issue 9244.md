# Issue 9244: Number field class group improvements

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-06-15 10:49:08

Assignee: davidloeffler

I was working on doctesting `sage/rings/number_field/class_group.py`, and I was unable to resist the temptation to rewrite it. (There were all sorts of failures and inconsistencies caused by the fact that `ClassGroup` derived from `AbelianGroup`, but `FractionalIdealClass` didn't derive from `AbelianGroupElement`.) 

I have a patch for this, depending on #9242, which I will upload as soon as someone explains how to squash the `_test_category()` error.


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Comment by davidloeffler created at 2010-06-25 08:04:22

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-25 08:04:22

Here's a patch. It doesn't depend on any other patches, contrary to what I wrote in the description.


---

Comment by fwclarke created at 2010-06-26 11:14:42

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2010-06-26 11:14:42

These are definite improvements, well implemented, and doctests pass.  Just one remark:

The eventuality envisaged in the comment at line 95 of the patched `class_group.py` (which should be referring to ideal classes rather ideals) ought to have its own doctest, such as:


```
sage: K.<a> = QuadraticField(-23)
sage: L.<b> = K.extension(x^2 - 2)
sage: CK = K.class_group()
sage: CL = L.class_group()
sage: [CL(I).list() for I in CK]
[[0], [2], [4]]
```



---

Comment by davidloeffler created at 2010-06-26 13:23:58

Good point. Here's a new patch incorporating your suggestion. I also realised that one of the doctests seems to return different output in 4.4.4 than in 4.4.4.alpha0, so I've flagged it with #random.


---

Comment by davidloeffler created at 2010-06-26 13:23:58

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-06-27 01:33:03

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-06-27 01:33:03

Jim and I have looked at this too (we are working on #9332) and think this is nearly good to go.  (We could not see any random doctests!)

This is the only failure (we tested all of sage/rings/number_fields):


```

sage -t  "sage/rings/number_field/class_group.py"           
**********************************************************************
File "/home/john/sage-4.4.4/devel/sage-tests/sage/rings/number_field/class_group.py", line 144:
    sage: C.gen(0)
Expected:
    Fractional ideal class (130, 1/2*a + 137/2)
Got:
    Fractional ideal class (41, a - 10)
**********************************************************************
File "/home/john/sage-4.4.4/devel/sage-tests/sage/rings/number_field/class_group.py", line 146:
    sage: C.gen(1)
Expected:
    Fractional ideal class (7, a)
Got:
    Fractional ideal class (17, a)
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_class_group.py
	 [3.1 s]

```



---

Comment by stankewicz created at 2010-06-27 05:45:37

I've double-checked the failure. It's just a different choice of generators for the class group ( C250 x C2 for those keeping track)


```
sage: i = C(C.number_field().gen(),7)                
sage: j = C(C.number_field().gen(),17)               
sage: k = C((1/2)*C.number_field().gen() + 137/2,130)
sage: l = C(C.number_field().gen() - 10,41)          
sage: i.list()                                       
[0, 1]
sage: j.list()
[125, 1]
sage: k.list()
[1, 0]
sage: l.list()
[88, 1]
sage: l.order()
250
sage: (j*(l^125)).order()
2
```



---

Comment by stankewicz created at 2010-06-27 05:45:37

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-27 08:53:48

My bad, I forgot to qrefresh before exporting. Here's a new patch with the #random flags.


---

Comment by fwclarke created at 2010-06-27 09:15:57

Replying to [comment:8 davidloeffler]:

> Here's a new patch with the #random flags.

Since this sorts out the failure that John and Jim found (but which I can't reproduce), it's a positive review.


---

Comment by fwclarke created at 2010-06-27 09:15:57

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-28 16:03:42

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-06-28 16:03:42

Wait a minute, this causes a doctest failure in William's Bordeaux 2008 examples, because calculating class groups with the optional argument proof=False isn't handled correctly: it still tries to bnfcertify. I will write an updated patch in a moment.


---

Comment by davidloeffler created at 2010-06-28 16:20:50

This patch handles the "proof" argument in a slightly different way in order to make sure that bnfcertify isn't called unnecessarily.


---

Comment by davidloeffler created at 2010-06-28 16:20:50

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-28 16:22:27

Sorry, I made a mess of uploading that. Patches `trac_9244_new.patch` and `trac_9244_new.2.patch` are identical, and both replace the previous `trac_9244.patch`.


---

Comment by fwclarke created at 2010-06-28 18:50:55

Replying to [comment:11 davidloeffler]:
> This patch handles the "proof" argument in a slightly different way in order to make sure that bnfcertify isn't called unnecessarily.

I don't think this is quite right.  I think the last two lines of the code for `_ideal_class_log` need to read

```
            self.__ideal_class_log[proof] = list(v[0])
            return self.__ideal_class_log[proof]
```



---

Comment by fwclarke created at 2010-06-28 18:50:55

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-06-28 20:00:29

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-28 20:00:29

Good point; thanks for spotting that. Here's a third attempt, which corrects the error as fwclarke suggests and also back-ports a doctest from #9359.


---

Comment by fwclarke created at 2010-06-28 21:28:18

Is there something wrong with the new doctest?  Because

```
sage: K.<a> = NumberField(x^3 - x + 1) 
sage: K.class_number()
1
```



---

Comment by davidloeffler created at 2010-06-29 07:51:14

replaces all previous attempts


---

Attachment

Nothing wrong with the code, just my brain, apparently. It should have been

```
K.<a, b> = NumberField([x^3 - x + 1, x^2 + 26])
```

which has class group `C_6 x C_3`, but I copied and pasted the wrong lines, and the #random flag hid that. I've uploaded a fourth attempt with this correction.

Apologies for the complete mess I have been making of this ticket from start to finish.


---

Comment by fwclarke created at 2010-06-29 18:00:20

It's fine now.


---

Comment by fwclarke created at 2010-06-29 18:00:20

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:52:39

Resolution: fixed
