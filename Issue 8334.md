# Issue 8334: Improvements to residue fields

Issue created by migration from https://trac.sagemath.org/ticket/8334

Original creator: roed

Original creation time: 2010-02-23 15:16:53

Assignee: AlexGhitza

CC:  was

Moves residue fields to the coercion model, makes the reduction and lifting maps morphisms, prepares the way for 7885 (Tate's algorithm for function fields).


---

Attachment

Apply after other patch


---

Attachment

Fixes various bugs and doctest failures introduced in earlier patches.


---

Attachment

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Comment by roed created at 2010-02-23 17:37:23

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-03-18 17:18:35

FWIW, testing with this and all the prior patches in the series applied under 4.3.4.rc0 brings up exactly 1 doctest failure, in line 321 of sage/rings/finite_rings/finite_field_givaro.py:

```
File "/home/masiao/sage-4.3.4.rc0/devel/sage-working/sage/rings/finite_rings/finite_field_
givaro.py", line 321:
    sage: F81(F9.gen())
Expected:
    Traceback (most recent call last):
    ...
    TypeError: unable to coerce from a finite field other than the prime subfield
Got:
    Traceback (most recent call last):
      File "/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py", line 1231, in run_one_te
st
        self.run_one_example(test, example, filename, compileflags)
      File "/home/masiao/sage-4.3.4.rc0/local/bin/sagedoctest.py", line 38, in run_one_exa
mple
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/masiao/sage-4.3.4.rc0/local/bin/ncadoctest.py", line 1172, in run_one_ex
ample
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[49]>", line 1, in <module>
        F81(F9.gen())###line 321:
    sage: F81(F9.gen())
      File "parent.pyx", line 826, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6232)
      File "parent.pyx", line 1876, in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:12773)
      File "parent.pyx", line 1883, in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:12925)
      File "parent.pyx", line 1740, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:11546)
      File "parent.pyx", line 1791, in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:11946)
      File "parent_old.pyx", line 503, in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:5943)
      File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_givaro.py", line 350, in _coerce_map_from_
        raise NotImplementedError
    NotImplementedError
```



---

Comment by davidloeffler created at 2010-03-18 17:18:35

Changing status from needs_review to needs_work.


---

Attachment

apply instead of 8334_residue_fields.patch -- rebased to apply after #8446


---

Comment by davidloeffler created at 2010-04-20 10:16:39

The patch conflicts with #8446, so I've uploaded a rebased version.


---

Comment by roed created at 2010-09-19 13:17:39

Apply:


```
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch.2
```



---

Comment by roed created at 2010-09-19 13:17:39

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-09-23 14:24:27

It doesn't work. On vanilla 4.6.alpha1, if I apply 

```
7883_ideals.patch
7883_fixes.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.2.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
```

then the first five apply (with minor fuzz) but the last one is completely knackered, with 23 out of 27 hunks failing. I think the problem is caused by #9343/#9400 which both make extensive changes to residue fields.

Just a general observation: you've managed to virtually guarantee that these patches are impossible to review, because they're all linked together in such a way that they fail doctests unless you apply the whole series. So the effect is a huge patch bomb, which is unappealing to review; hence it sits around for ages, and inevitably bitrots. Please, please, please back-port the doctest fixes etc, so each ticket in the series passes doctests on its own. Otherwise this will really never get merged and all of your hard work writing this excellent code (not to mention the work of those who have attempted to review it) will be for nothing.


---

Comment by davidloeffler created at 2010-09-23 14:24:27

Changing status from needs_review to needs_work.


---

Attachment

Rebased against 4.6.alpha1


---

Comment by roed created at 2010-09-23 16:45:31

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-09-23 16:45:31

I'm sorry that this has been so difficult to review.  I've tended to work in chunks: I just start ripping things apart and changing lots of stuff, and then I need to fix it all; by the time I've managed to make all the doctests pass it's turned into a patch-bomb.  I've tried to split things into logically consistent chunks, but it's really frustrating trying to backport fixes.  I also really shouldn't be working on Sage right now: I should be working on my thesis, which has nothing to do with this.

I've tried to get these tickets working against 4.6.alpha1 (in particular, I think they should now).  If they don't get reviewed, I'll try your approach.  In the mean time, the sequence of patches should be 


```
7883_ideals.patch
7883_fixes.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.2.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_9343.patch
7585_12_1_fixes.2.patch
```



---

Comment by roed created at 2010-09-23 16:52:59

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-09-23 16:52:59

gah.  Manual merge doesn't build.  Working on it...


---

Comment by roed created at 2010-09-23 16:56:48

Fixed merge error; apply against 4.6.alpha1


---

Attachment

Forgot to delete 4 lines.  I'm still building, but the build has progressed past `residue_field.pyx`.


---

Comment by roed created at 2010-09-23 17:30:32

I'm getting weird doctest failures, as if some of the changes in 7883_ideals.patch didn't get applied.  Then I switched to my main branch and now Pari segfaults upon sage starting up.

I'm going to install a fresh copy of sage-4.6.alpha1, which will take a few hours, and try to figure out what's going on.


---

Comment by davidloeffler created at 2010-09-23 20:52:04

Would you mind basing your updated patch series on my folded patch at #7883, the one I gave a positive review to, rather than on your original patches (as you seem to have done judging by your comment 8)? Then we can treat the #7883 stuff as finished and fixed.

David


---

Comment by roed created at 2010-09-23 22:46:08

sure


---

Comment by roed created at 2010-09-24 14:27:45

Includes all patches in 8333 and 8334; based on 4.6.alpha1 with 7883


---

Comment by roed created at 2010-09-24 14:30:08

Changing status from needs_work to needs_review.


---

Attachment

You now only need to apply one patch.


---

Comment by roed created at 2010-09-24 14:31:00

All doctests pass for me, though I didn't run -long (it already takes a couple hours on my laptop)


---

Comment by davidloeffler created at 2010-09-24 14:36:36

Sadly this conflicts with the positively-reviewed patch series #9898/#9753/#9764.

I will handle rebasing it past those. You can sit back and relax. Thanks for all your sterling efforts on this particularly frustrating job. I have access to a very fast computer (from Bill Hart's research grant, thanks Bill) which runs long tests in about 10 minutes :-)


---

Comment by roed created at 2010-09-24 14:43:25

Thanks.  That's especially useful since I just broke my mercurial queues trying to switch back to a more finely grained set of patches than `8333_8334_ALL.patch`.  Oh well, I'll just tell Mercurial that there are no patches there and both it and sage will be happy.


---

Attachment

Apply only this patch -- see comment below.


---

Comment by davidloeffler created at 2010-09-24 15:25:18

Right, so I have rebased roed's last patch and uploaded my rebased patch as `8333_8334_ALL-rebased_for_9764.patch`. This patch will apply cleanly to 4.6.alpha1 on top of the folded patch from #7883 and the series #9898/#9753/#9764.

This patch incorporates everything from #8333 as well, so this is the only patch that needs to be applied to close both #8333 and this ticket.


---

Comment by davidloeffler created at 2010-09-24 15:25:18

Changing status from needs_review to positive_review.


---

Comment by roed created at 2010-09-24 15:29:04

Yay!  Thank you for your work on these patches.


---

Comment by davidloeffler created at 2010-09-24 15:39:37

Incidentally, are you running a 32-bit or a 64-bit machine? I don't have access to any 32-bit boxes. If you have access to a 32-bit machine, it would be great if you could do the following:

- Install #9898/#9753/#9764 and test everything in sage/rings.
- Then install #7883 and the combined patch from this ticket, and do sage/rings again.
- Then install #9359 and repeat.

I'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)


---

Comment by roed created at 2010-09-24 15:51:45

In fact, I can think of one hashing doctest which will fail on a 32-bit machine.  Unfortunately I'm running on 64-bit.


---

Comment by jdemeyer created at 2010-09-25 09:58:28

Replying to [comment:20 davidloeffler]:
> - Install #9898/#9753/#9764 and test everything in sage/rings.
> - Then install #7883 and the combined patch from this ticket, and do sage/rings again.
> - Then install #9359 and repeat.
> 
> I'm a little nervous about silly doctest failures coming up from Pari's unpredictable choices of generators of ideals, and this would set my mind at rest a bit :-)

I will do this (and should have done it for my patches).


---

Comment by jdemeyer created at 2010-09-26 10:57:13

I have testing the following chain of patches on a 32-bit PPC machine:

```
trac_7883-ideals-folded.patch
9898_pari_decl.patch
9753.patch
9764_ideal_repr_new.patch
8333_8334_ALL-rebased_for_9764.patch
```


The only failure was in `sage/schemes/generic/toric_divisor.py`, which is a known problem.


---

Comment by mpatel created at 2010-09-28 09:41:08

Could someone please update the commit string of [attachment:8333_8334_ALL-rebased_for_9764.patch] so its first line is a < 80 (or so) character summary that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.


---

Comment by mpatel created at 2010-09-28 09:41:08

Changing status from positive_review to needs_work.


---

Attachment

Version with better commit string.


---

Comment by davidloeffler created at 2010-09-28 10:19:34

Changing status from needs_work to positive_review.


---

Comment by davidloeffler created at 2010-09-28 10:19:34

Done.


---

Comment by mpatel created at 2010-09-28 10:56:59

Resolution: fixed


---

Comment by cremona created at 2010-10-03 16:33:50

This seems to have sorted #9409, which needs a reviewer to verify my check.


---

Comment by zimmerma created at 2011-11-23 09:42:23

David, I'm not very satisfied with the change in `french_book/numbertheory.py` done by this patch, for two reasons:

(1) the previous error message was better. (In the book we wanted to show that the isomorphism
    between two instances of GF(3<sup>2</sup>) is not automatic in Sage.)

(2) this is more serious. We have put this doctest in Sage so that the examples of our book (which
    is now published) still work with future versions of Sage. By changing the error message you
    did break the examples on http://sagebook.gforge.inria.fr/. Moreover you did not even contact
    us to discuss this change.

For (1) is it possible to revert to the previous error message?

For (2) in case you want to change some file in the tests directory, please first inform the
corresponding author.

Paul Zimmermann


---

Comment by davidloeffler created at 2011-11-23 10:12:29

Paul: I'm sorry, I didn't mean to break anything -- I didn't know there was an official policy of not making changes to the tests directory. Can you point me to where this policy is explicitly written down?


---

Comment by zimmerma created at 2011-11-23 10:24:14

David (Loeffler), I didn't write to you, but to David Roe... You are just the reviewer.
This policy is explained in http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :

```

Note that you could also submit a patch to Sage with the code you're doctesting.
I did that with all the tests from both of the books I published, and
I encourage you and many others to do the same with the code from your
article.  The code would go in a file

    devel/sage/sage/tests/

like the file devel/sage/sage/tests/book_stein_modform.py

In fact, I could imagine having dozens of files in that directory, and
when doctests break there, we could notify the authors before
releasing the version of Sage that breaks their doctests for feedback
-- then they could update their papers or Sage.
```


My personal opinion is that "we could notify" should read "we should notify"...

Paul


---

Comment by roed created at 2011-11-25 21:16:00

Sorry for the change to the tests folder.  When I split up a patchbomb into #8334 and #8335 (among others), I changed some errors to `NotImplementedError` for coercions that would soon work in #8335.  Unfortunately that ticket has stagnated.

While I'm working on fixing #8335, I've made a new ticket (#12084) that restores the original `TypeError`.  It's ready for review.  Sorry for the trouble, and I'll be more careful with the `sage/tests` directory in the future.


---

Comment by jdemeyer created at 2014-09-08 20:41:21

What's with all the commented-out doctests added here? See #16946.
