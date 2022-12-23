# Issue 9906: Move generally usable decorators from plot.misc to misc.decorators

Issue created by migration from https://trac.sagemath.org/ticket/9907

Original creator: jsrn

Original creation time: 2010-09-14 06:28:56

Assignee: tdb

CC:  jason mhansen

Keywords: generality, decorators

In plot.misc there are some generally usable decorators for various nice stuff. These should be moved to a general library so other modules can use them without illogically depending on plot.


---

Comment by jsrn created at 2010-09-14 18:48:06

Changing status from new to needs_review.


---

Comment by jsrn created at 2010-09-15 13:12:25

While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.


---

Comment by rbeezer created at 2010-09-16 04:46:03

I'm not qualified to check out the "work-around" for classes.  But I've cc'ed Mike Hansen and Jason Grout, who I think were in on these in the first place back at #4201.

I am running this through full tests as part of #6094 and a report will go there once concluded.

Commit message on the ticket itself should probably change - there is no "as before" here to compare with, and in the final log it really won't make any sense.


---

Comment by jason created at 2010-09-16 09:11:04

Replying to [comment:2 jsrn]:
> While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.

Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.


---

Comment by jsrn created at 2010-09-16 11:28:29

Replying to [comment:4 jason]:
> Replying to [comment:2 jsrn]:
> > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.
> 
> Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.

That should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?


---

Comment by jsrn created at 2010-09-16 14:28:37

Replying to [comment:5 jsrn]:
> Replying to [comment:4 jason]:
> > Replying to [comment:2 jsrn]:
> > > While trying to use this patch in Trac #6094, I found out that the `@`wraps decorator used internally in all three decorators moved to sage.misc only works for functions in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, I have written a small work-around, which essentially emulates the patched behaviour of wraps. This is in the newest patch.
> > 
> > Do you think you could just add the work-around to the sage_wraps decorator (sage.misc.misc.sage_wraps) and convert the decorators to use it?  There are other functions that use sage_wraps, and it would be nice to have all of that work-around code in one place.
> 
> That should be no problem, I guess; I wasn't aware of sage_wraps. However, that might affect a lot of places outside the original scope of this ticket; should it be a new ticket then? What's the precedence here?

I started Trac #9919 for doing this patch in sage_wraps. I'm also thinking that, when the problems with this patch are identified, we might move sage_wraps and other decorators in sage.misc.misc into sage.misc.decorators as well.


---

Comment by jason created at 2010-09-16 15:54:39

Starting another ticket sounds good.


---

Comment by jsrn created at 2010-09-17 08:19:45

Changing status from needs_review to needs_work.


---

Comment by jsrn created at 2010-09-17 08:19:45

Rob Beezer posted the following problem with the current patch for Trac #6094, but that is actually a problem with the current patch for this trac. When testing the unpickle-function in sage.structure.sage_object, the relocation of the decorators yield problems:


```
rob@wave:/sage/dev$ ./sage -t  devel/sage/sage/structure/sage_object.pyx
sage -t  "devel/sage/sage/structure/sage_object.pyx"        
**********************************************************************
File "/sage/dev/devel/sage/sage/structure/sage_object.pyx", line 1001:
    sage: print "x"; sage.structure.sage_object.unpickle_all(std)
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    ** failed:  _class__sage_plot_misc_options__.sobj
    ** failed:  _class__sage_plot_misc_rename_keyword__.sobj
    Failed:
    _class__sage_plot_misc_options__.sobj
    _class__sage_plot_misc_rename_keyword__.sobj
    Successfully unpickled 584 objects.
    Failed to unpickle 2 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/rob/.sage//tmp/.doctest_sage_object.py
         [5.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/structure/sage_object.pyx"
```


The deprecation-warnings are just garbage from words.py, so the important thing to note is the "** failed"-lines. The problem, as far as I can see, is simply that there is a standard pickle jar which has a pickle for all the functions etc. shipped with sage. This needs to be updated when applying this patch. Does anyone know how this is done and possibly included in the patch?

Cheers, Johan


---

Comment by mhansen created at 2010-09-19 20:44:11

The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at [9907](http://trac.sagemath.org/sage_trac/ticket/9907) as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to sage/plot/misc.py


```
#For backward compatibility -- see #9907.
from sage.misc.decorators import options, suboptions, rename_keyword

```

That way, the old pickles will still work as they will still be able to find the decorators in sage.plot.misc.


---

Comment by jsrn created at 2010-09-20 06:40:34

Replying to [comment:9 mhansen]:
> The pickle jar contains old pickles of objects that we want to ensure work in the future. For example, if you made the changes at [9907](http://trac.sagemath.org/sage_trac/ticket/9907) as the are, then possibly many pickles out in the wild would break. Instead of trying to update the pickle jar, the appropriate thing to do would be to add the following to sage/plot/misc.py
> 
> {{{
> #For backward compatibility -- see #9907.
> from sage.misc.decorators import options, suboptions, rename_keyword
> 
> }}}
> That way, the old pickles will still work as they will still be able to find the decorators in sage.plot.misc.

Ok, thanks -- I will update the patch for #9907. I was actually wondering a bit about backward compatibility, so good to know this is the system. Does the above fix then have a one-year lifetime like for keyword-deprecation? If so, should it be flagged somehow (e.g. with the comment containing the term "backward compatibility") so it can be found and removed one year from now?


---

Comment by jsrn created at 2010-09-23 12:02:35

Changing status from needs_work to needs_review.


---

Comment by jsrn created at 2010-09-23 12:04:46

Changing assignee from tdb to jsrn.


---

Comment by jsrn created at 2010-09-23 12:04:46

Note that the added patch assumes the patch for Trac #9919.


---

Comment by jsrn created at 2010-09-24 06:51:15

Added a comment about when then bug in #9919 was fixed in Python. Accidentally uploaded two.


---

Comment by jsrn created at 2010-09-24 07:05:34

Ok, uploaded a new one, as it seems you can't manually change the patch-files because of some hashes in the top of the file. So this one was done the right way. Remember to use the newest and 
_NOT_ the one called ".2.patch".


---

Comment by jason created at 2010-10-02 04:33:05

Can I delete the .2.patch file, then?


---

Comment by jason created at 2010-10-02 19:44:39

I've opened up #10057 to address an import change that needs to be made in sagenb after this is merged.


---

Comment by jason created at 2010-10-02 19:50:39

apply only this patch; rebased to 4.6.alpha1+some patches


---

Attachment

Replying to [comment:17 jason]:
> Can I delete the .2.patch file, then?
Sure; I just don't have the privileges to do that myself.


---

Comment by mhansen created at 2010-10-09 20:07:41

This needs to be coordinated with #10107.


---

Attachment

Rebased to 4.6. Still requires first applying patch for Trac #9919


---

Comment by rlm created at 2010-11-09 20:21:51

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-11-09 20:21:51

If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.


---

Comment by jdemeyer created at 2010-11-11 16:46:09

Should this be merged in Sage 4.6.1? (if yes, please set the Milestone)


---

Comment by jdemeyer created at 2010-11-16 08:20:15

Resolution: fixed
