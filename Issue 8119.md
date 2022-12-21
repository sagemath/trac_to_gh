# Issue 8119: Rename change the hash value of some objects

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-01-29 15:22:48

Assignee: tbd

CC:  jason simonking

For many objects the hash value is computed from `__repr__`. This is a bad idea since renaming the object change its hash value.

```
sage: bla = PolynomialRing(ZZ,"x")
sage: hash(bla)
-1525918542791298668
sage: bla.rename("toto")
sage: hash(bla)
2314052222105390764
```



---

Comment by robertwb created at 2010-03-12 09:34:04

For immutable objects, like Parents, the default __hash__ could store the value used the first time it is computed. This doesn't solve the problem of 


```
sage: bla = PolynomialRing(ZZ,"x")
sage: hash(bla['t'])
-1733828288
sage: bla.rename("toto")
sage: hash(bla['t'])
-1924319844
```



---

Attachment


---

Comment by robertwb created at 2010-03-12 09:59:47

This is a partial fix (that won't work for SageObject in general, unless we enforce that mutable objects maintain their own hash, and I don't think we want to put an extra field on all Elements), but resolves the most important case. It's also a performance gain.


---

Comment by robertwb created at 2010-03-12 09:59:47

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-12 22:32:13

Hi Robert,

I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?

If this is not both this patch and #8120 are broken.

Also, after this, do you still need #8506 ?

Florent


---

Comment by robertwb created at 2010-03-13 09:44:33

Replying to [comment:3 hivert]:
> Hi Robert,
> 
> I've one question related to this and I like to have the confirmation from an expert. After your patch, upon pickling/unpickling the hash value can change because it is not pickled and neither is the name, right ? As far as I manage to test this is not harmful to pickle a dict containing a renamed parent. Indeed, trying to read `cPickle.c`, I understood that the dict is reconstructed from it's items and thus even if the hash changed the element is inserted correctly in the dict during unpickling. Can you confirm this ?

That is correct. Hashes in general are not guaranteed to be consistent from run to run, all that really matters is that they satisfy (to the best they can) the equality constraints. 

> If this is not both this patch and #8120 are broken.
> 
> Also, after this, do you still need #8506 ?

Yes, #8506 is still important--in my case I'm reducing a curve mod many, many primes, doing just a bit of stuff on each before throwing them away. I suppose eventually caching the hash value would eventually be a win, but that's a separate optimization.


---

Comment by jason created at 2010-10-02 19:57:48

hivert: do you want to review this ticket?


---

Comment by hivert created at 2011-04-04 17:24:40

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2011-04-04 17:24:40

> hivert: do you want to review this ticket?

Sure ! I completely forgot about this one. Sorry !

They are a few place where we should remove the bad implementation using `__repr__` since they all inherits from `CategoryObject`: 

```
popcorn-*ge-combinat/sage $ grep "hash(self.__repr__())" **/*.py*
groups/group.pyx:        return hash(self.__repr__())
modules/module.pyx:        return hash(self.__repr__())
modules/module.pyx:        return hash(self.__repr__())
rings/polynomial/multi_polynomial_libsingular.pyx:        return hash(self.__repr__())
rings/ring.pyx:        return hash(self.__repr__())
structure/sage_object.pyx:        return hash(self.__repr__())
```

I don't have time to do it right now. I'll do it soon if you don't beat me.


---

Comment by hivert created at 2011-04-04 18:48:36

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2011-04-04 18:48:36

> They are a few place where we should remove the bad implementation using
> `__repr__` since they all inherits from `CategoryObject`:

I just added a review patch which removes the wrong hash methods.

Please review. I'm ok with the original patch, so if my review patch is ok
you can put a positive review on my behalf.


---

Attachment

Florent's review patch looks good. However ``consistant_ should be written ``consistent_ in the first patch. I also did not yet set a positive review because of the ongoing discussion on sage-devel. Please feel free to go ahead and set a positive review once the typo is fixed and if it is decided that the PolynomialRing issue shall be fixed in a follow up patch.

Cheers,
                                   Nicolas


---

Comment by nthiery created at 2011-04-21 01:45:08

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2011-04-21 09:27:06

Changing status from needs_work to positive_review.


---

Attachment

Fixed the typo, I don't think the issue with sparse PolynomialRing #11231 should hold this ticket up any longer (it's had a patch sitting on it for over a year...)


---

Comment by jdemeyer created at 2011-04-21 19:36:29

I'm assuming the "apply" should be changed...


---

Comment by jdemeyer created at 2011-04-22 19:38:38

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-04-22 19:38:38

Please change the commit message of [attachment:8119-parent-hash.2.patch] (use hg qrefresh -e for that).


---

Comment by hivert created at 2011-04-23 10:47:52

Changing status from needs_work to needs_review.


---

Attachment

I just re-uploaded roberts patch with a correct log message. I'm not sure I'm allowed to put a positive review though. 

Florent


---

Comment by nthiery created at 2011-04-23 13:12:44

Bonjour Florent!

I am not sure the log message for 8119-parent-hash-review.patch is proper. While you are at it, I'd suggest to just fold it in the other patch. The review history does not bring much information here, so having a single patch will give a better overview to the future reader.

I'll set a positive review right after.


---

Comment by nthiery created at 2011-04-23 13:12:44

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2011-04-23 13:47:11

> I'd suggest to just fold it in the other patch.

Done.


---

Comment by hivert created at 2011-04-23 13:48:51

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2011-04-23 15:18:59

Thanks!

It seems the buildbot is getting confused about which patch to apply though.


---

Comment by nthiery created at 2011-04-23 15:18:59

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2011-04-24 05:05:20

Apply 8119-parent-hash-final.patch

Granted, the patchbot doesn't bother testing positively reviewed tickets (not that anything it's concerned with changed). Thanks for getting to this for me.


---

Comment by jdemeyer created at 2011-05-03 08:46:29

Some of these doctests should be differentiated on 32-bit systems (in particular, all the results of `hash()`).


---

Comment by jdemeyer created at 2011-05-03 08:46:29

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-05-19 08:31:51

*bump*


---

Comment by nborie created at 2012-03-29 14:48:21

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2012-03-29 14:54:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-06 06:19:24

On boxen (Linux x86_64), I get:

```
sage -t  -force_lib devel/sage/sage/structure/category_object.pyx
**********************************************************************
File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 757:
    sage: hash(bla)
Expected:
    -1525918542791298668
Got:
    -5279516879544852222
**********************************************************************
File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 761:
    sage: hash(bla)
Expected:
    -1525918542791298668
Got:
    -5279516879544852222
**********************************************************************
```



---

Comment by jdemeyer created at 2012-04-06 06:19:24

Changing status from positive_review to needs_work.


---

Attachment

Replying to [comment:23 jdemeyer]:
> On boxen (Linux x86_64), I get:
> {{{
> sage -t  -force_lib devel/sage/sage/structure/category_object.pyx
> **********************************************************************
> File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 757:
>     sage: hash(bla)
> Expected:
>     -1525918542791298668
> Got:
>     -5279516879544852222
> **********************************************************************
> File "/padic/scratch/jdemeyer/merger/sage-5.0.beta14/devel/sage-main/sage/structure/category_object.pyx", line 761:
>     sage: hash(bla)
> Expected:
>     -1525918542791298668
> Got:
>     -5279516879544852222
> **********************************************************************
> }}}

Weird, I get here the same result as you on boxen, both with 4.8 and 5.0.beta8. I don't know how a wrong return value ended up in the patch. 

Oh well, I updated the patch to expect the result obtained on boxen.


---

Comment by nthiery created at 2012-04-06 14:51:08

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-04-07 12:04:42

Apply 8119-parent-hash-final-fix32.patch

(for patchbot)


---

Attachment


---

Comment by hivert created at 2012-04-26 22:21:47

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2012-04-26 22:21:47

Hi there,

I'm setting a positive review here but I uploaded a new patch removing a
trailling whitespace which bothered the patchbot. The only difference between
[attachment:8119-parent-hash-final-fix32.patch] and
[attachment:8119-parent-hash-final.patch] is the trailling space (and of course
Mercurials header), so I don't think a new review is needed.

Florent


---

Comment by nthiery created at 2012-04-27 17:43:33

Thanks for the final review!


---

Comment by jdemeyer created at 2012-04-30 09:51:35

Resolution: fixed
