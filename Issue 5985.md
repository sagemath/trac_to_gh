# Issue 5985: cPickle: adds support for class pickling customizing  and for nested classes

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-05 05:54:04

Assignee: nthiery

CC:  sage-combinat cwitty saliola burcin craigcitro

Keywords: cPickle, pickling classes




---

Comment by nthiery created at 2009-05-06 23:59:24

I just rebased the first patch upon 3.4.2 final. Please ignore (or better delete) the old version  cPickle-5985-import.patch


---

Comment by nthiery created at 2009-05-07 01:53:00

Note: the cPickle imports in dsage will need to be updated as well.


---

Comment by nthiery created at 2009-05-12 22:32:33

Updated patch:
 - Fixes a trivially failing doctest (don't know why I did not see them earlier)
 - Adds some more doctest


---

Comment by nthiery created at 2009-05-19 06:26:11

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-22 14:19:32

This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work. It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.

Cheers,

Michael


---

Comment by robertwb created at 2009-05-22 23:03:01

Followup at #5986


---

Attachment


---

Comment by nthiery created at 2009-05-23 07:45:00

Replying to [comment:10 mabshoff]:
> This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work.

The updated patch hopefully fixes this (please double check).

> It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.

Oops, fixed. Someone was supposed to give a positive review, but apparently this has not occurred yet.


---

Comment by craigcitro created at 2009-07-08 22:31:31

I've rolled an spkg with the patch by Nicolas incorporated -- it's here:

  http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg

It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 

I should have more time to look at this tonight (and give it a review, assuming it works).


---

Comment by nthiery created at 2009-07-09 10:45:34

Replying to [comment:13 craigcitro]:
> I've rolled an spkg with the patch by Nicolas incorporated -- it's here:
> 
>   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg
> 
> It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 
> 
> I should have more time to look at this tonight (and give it a review, assuming it works).

Thanks for working on this!

The patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)


---

Attachment

Replying to [comment:14 nthiery]:
> Replying to [comment:13 craigcitro]:
> > I've rolled an spkg with the patch by Nicolas incorporated -- it's here:
> > 
> >   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg
> > 
> > It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 
> > 
> > I should have more time to look at this tonight (and give it a review, assuming it works).
> 
> Thanks for working on this!
> 
> The patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)

Oops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.

Luckily enough, the real applications of this patch readily did not use this feature anymore!


---

Comment by nthiery created at 2009-07-11 22:58:27

Replying to [comment:15 nthiery]:
> Oops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.

For the record:

zephyr-/opt/sage-4.0.2>./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat           
sage: class metaclass(type):
....:     def __new__(cls):
....:         return type.__new__(cls, "bla", (object,), dict())
....:
sage: metaclass()                                                                                                     
<class '__main__.bla'>
| Sage Version 4.0.2, Release Date: 2009-06-18                       |
| Type notebook() for the GUI, and license() for information.        |
zephyr-~>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: class metaclass(type):
....:     def __new__(cls):
....:         return type.__new__(cls, "bla", (object,), dict())
....:
sage: metaclass()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
TypeError: type.__init__() takes 1 or 3 arguments
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
Apparently type.__new__ now calls type.__init__. And I assume that can only be a change in python, not in Sage.


---

Comment by craigcitro created at 2009-10-09 08:37:44

I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:

  http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg

This fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`.


---

Comment by nthiery created at 2009-10-11 08:44:06

Changing priority from major to critical.


---

Comment by nthiery created at 2009-10-11 08:44:06

Replying to [comment:17 craigcitro]:
> I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:
> 
>   http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg
> 
> This fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`. 

Sounds good to me! Positive review, up to someone double checking the new patch I attached which imports the test file from the original version of the patch.

Carl, Craig, Robert, please do it soon! William is ok integrating this in 4.1.2 (see IRC).
I set back the release to 4.1.2

For the author / reviewer, I don't know exactly what to do since I wrote the first version, Craig reviewed it, wrote the second version which I reviewed :-) Please set whatever you feel appropriate


---

Comment by craigcitro created at 2009-10-15 06:43:41

I'm happy with Nicolas's patch to test the new python spkg -- let's finally get this merged! Yay!


---

Comment by craigcitro created at 2009-10-15 06:43:41

Changing status from needs_review to positive_review.


---

Attachment

Apply only this patch, after updating the python spkg linked to below


---

Comment by mhansen created at 2009-10-15 06:56:06

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 06:56:06

I updated the patch to do "import cPickle" instead of importing it from sage.misc.  After that, everything passes.
