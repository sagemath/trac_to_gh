# Issue 8386: iet alphabet bug and rebased datatype

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-02-27 13:06:33

Assignee: vdelecroix

CC:  sage-combinat tmonteil

Keywords: iet combinatoric

There was a bug for iet.Permutation comparisons. We have the following

```
sage: p = iet.Permutation('a b','b a')
sage: q = iet.Permutation('b a','a b')
sage: p == q
True
```


The patch correct this feature (we get wrong) and rebased the datatype used for iet.Permutations.


---

Attachment


---

Comment by vdelecroix created at 2010-02-27 22:28:18

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2010-02-27 22:28:18

Changing component from algebra to combinatorics.


---

Comment by ncohen created at 2011-10-02 10:42:39

This patch really needs to be rebased (14 hunk failures) `:-)`


---

Comment by ncohen created at 2011-10-02 10:42:39

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2012-03-09 02:54:25

Changing keywords from "iet combinatoric" to "iet, combinatorics".


---

Comment by vdelecroix created at 2012-03-09 03:09:19

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-03-12 17:55:04

A bunch of doctests are failing with this patch (see patchbot logs)


---

Comment by davidloeffler created at 2012-03-12 17:55:04

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2012-03-13 14:56:03

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-04-06 10:43:45

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-04-06 10:43:45

This seems to work with 4.8 but two doctests consistently fail with recent 5.0 betas:

```
**********************************************************************
File "/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py", line 1348:
    sage: c1 != c2_hyp
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[13]>", line 1, in <module>
        c1 != c2_hyp###line 1348:
    sage: c1 != c2_hyp
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py", line 1364, in __cmp__
        return type.__cmp__(type(self),type(other))
    AttributeError: type object 'type' has no attribute '__cmp__'
**********************************************************************
File "/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py", line 1350:
    sage: c2_hyp != c2_odd
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[14]>", line 1, in <module>
        c2_hyp != c2_odd###line 1350:
    sage: c2_hyp != c2_odd
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py", line 1364, in __cmp__
        return type.__cmp__(type(self),type(other))
    AttributeError: type object 'type' has no attribute '__cmp__'
**********************************************************************
```



---

Attachment

apply only this one


---

Comment by vdelecroix created at 2012-04-29 19:30:20

I modify one line in the __cmp__ method of AbelianStratumComponent in order to make it works.

I suspect an upgrade version of python between sage-4.8 and sage-5.0 as I used the method __cmp__ of 'type' which no longer exists.


---

Comment by vdelecroix created at 2012-04-29 19:30:20

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-07-27 20:42:46

Please fill in your real name as Author.


---

Comment by chapoton created at 2012-08-29 19:16:29

Apply only trac_8386-enhanced_iet.v2.patch


---

Comment by chapoton created at 2012-09-26 13:09:40

The bot is not happy: one doctest is missing in dynamics/interval_exchanges/constructors.py

I also complains about the startup, but I do no know what to do about that..


---

Comment by chapoton created at 2012-09-27 18:29:52

I have added the missing doc.

What about the startup problem ?


---

Comment by chapoton created at 2012-09-28 08:19:47

Apply only trac_8386-enhanced_iet.v2.patch


---

Comment by chapoton created at 2012-11-15 19:30:23

Apply only trac_8386-enhanced_iet.v2.patch

Here is a tentative of lazy_import. Let us see what the bot think of that one.


---

Attachment

Apply only trac_8386-enhanced_iet.v2.patch

another try, even more lazy !


---

Attachment


---

Comment by chapoton created at 2012-12-11 20:16:58

I have rebased on 5.5rc0.

I hope I have not made a mistake in doing that

Apply trac_8386-enhanced_iet.v3.patch


---

Comment by chapoton created at 2013-05-19 13:33:12

Let me try to do something for this ticket.

Here is a new patch, that *only* moves the files from "combinat/iet" to a new folder "dynamics".

This has been done by starting with the code in 5.10.beta3. So there is something lost, which is the refactoring of datatype.

But it pass all tests.


---

Comment by chapoton created at 2013-05-19 13:33:27

for the bot:

apply trac_8386_just_moving-fc.patch


---

Comment by jdemeyer created at 2013-05-19 13:50:47

If you move files, use `hg mv` for that instead of `hg remove` the old and `hg add` the new file.


---

Comment by jdemeyer created at 2013-05-19 13:50:47

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2013-05-19 14:30:24

I am happy for this ticket if it simply moves iet to sage.dynamics (and keep the refactoring for another ticket) ! But as jdemeyer mentioned it should be done with hg mv (which is a one line patch) instead of hg remove/hg add (which is a 2x(length of the file) patch long).

vincent


---

Comment by chapoton created at 2013-05-19 16:30:05

Well, I did not now about hg mv.

I have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.

And I has also taken the opportunity to 
- put all the raise syntax into python3 form
- correct orthographic errors
- make the code much closer to pep8 level
- removed unused import statements
- make the desired separation into interval_exchanges and flat_surfaces

I spent a few *hours* today on that, and I have already spent a lot of time on this ticket some *months* ago, but nobody did react at that time.

So, given that all tests pass *now*, it would be great if my work is not lost again.


---

Comment by vdelecroix created at 2013-05-19 17:02:37

Replying to [comment:25 chapoton]:
> Well, I did not now about hg mv.
> 
> I have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.
> 
> And I has also taken the opportunity to 
> - put all the raise syntax into python3 form
> - correct orthographic errors
> - make the code much closer to pep8 level
> - removed unused import statements
> - make the desired separation into interval_exchanges and flat_surfaces
> 
> I spent a few *hours* today on that, and I have already spent a lot of time on this ticket some *months* ago, but nobody did react at that time.
> 
> So, given that all tests pass *now*, it would be great if my work is not lost again.

I will have a closer look *right now* at your patch. Nevertheless patchbot complains (blue color instead of green) because the doctest framework now wants "....:" instead of "..." in multiline doctests.


---

Attachment

for the bot: apply trac_8386_just_moving-fc.patch

here is a patch that should correct the `....:` point

let us see what the patchbot says


---

Comment by nthiery created at 2013-05-19 18:49:35

Replying to [comment:25 chapoton]:
> Well, I did not now about hg mv.
> ...
> So, given that all tests pass *now*, it would be great if my work is not lost again.

You can quickly recreate your patch using `hg mv` as follow:

- With your patch applied, backup the files that have been moved/modified
- Unapply the patch
- Replay the moving the files using `hg mv`
- Reinstate the backed-up files on top of it.
- hg qnew a new patch with those, and discard the other one.

You might want to actually do two patches, one with just the moving,
and the other with the changes.

Btw: thanks Frédéric for all the hard work you are doing lately
(cleaning, reviewing and more ...)!

Cheers,
                                 Nicolas


---

Comment by chapoton created at 2013-05-19 19:27:22

Thanks Nicolas for this good advice. I am doing that, and I will upload 2 patches


---

Comment by jdemeyer created at 2013-05-19 19:55:29

There is even an option

```
hg mv --after
```

which allows one to mark the move after it has happened. But it doesn't work well with queues, as a patch which has been `qrefresh`ed is considered committed. So you need a non-committed version of the patch: apply the patch "by hand" using `patch -p1 <x.patch`, then `hg mv --after`, then `hg commit` should work (but I haven't really tried).


---

Attachment

ok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.

for the bot:

apply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch


---

Comment by vdelecroix created at 2013-05-19 20:27:54

Replying to [comment:31 chapoton]:
> ok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.

It also happens for me. After removing the directory doc/output it works fine again (but you need to rebuild everything with "sage -docbuild all html"). If there is a less extremal solution then I would be happy to know.

apply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch


---

Comment by chapoton created at 2013-05-24 11:57:58

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2013-06-03 20:45:26

Thanks Frederic.

I put you as an author and me as a reviewer as it is more like that now. I postponed the modification of the implementation to #14683.


---

Comment by vdelecroix created at 2013-06-03 20:45:26

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-04 06:55:40

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-06-04 06:55:40

Needs to be rebased to #14669.


---

Attachment


---

Comment by chapoton created at 2013-06-13 18:12:08

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-06-13 18:12:08

rebased on top of #14669


---

Comment by vdelecroix created at 2013-06-18 14:26:50

Great !


---

Comment by vdelecroix created at 2013-06-18 14:26:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-18 17:11:31

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-06-18 17:11:31

Never use `assert` to check user input, use `raise TypeError()` or other exceptions for that.
An `AssertionError` appearing in a public function is by definition a bug.

Example:

```
sage: QuadraticStratum("foo")
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-ba2d4d1c0bfc> in <module>()
----> 1 QuadraticStratum("foo")

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/dynamics/flat_surfaces/quadratic_strata.pyc in __init__(self, *l)
     30         else:
     31             for i in l:
---> 32                 assert(isinstance(i, (int, Integer)))
     33             self._zeroes = sorted(list(l), reverse=True)
     34 

AssertionError: 
```



---

Attachment


---

Comment by chapoton created at 2013-06-18 19:53:34

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-06-18 19:53:34

here is patch that

* removes all "assert" statements, using some "raise xxxError()" instead

* makes an effort to doctest more of the "raise xxxError()"

There remains to make sure all "raise" are doctested, but I would prefer to keep that for another ticket, given the age of this one.

Needs review


---

Comment by jdemeyer created at 2013-06-18 20:57:47

I haven't checked in detail (Vincent: can you do that please), but it looks good on first sight. Excellent work!


---

Comment by nthiery created at 2013-06-19 05:47:29

Sounds good to me too. Thanks Frédéric!

Btw: I noticed a __repr__; but that's probably for another ticket.


---

Comment by tscrim created at 2013-06-28 16:41:30

Vincent, are you able to do the re-review in the next few days? #14772 depends on this ticket because there are two instances in iet which use `Permutation_class`.


---

Comment by vdelecroix created at 2013-07-04 11:52:57

Good to go! Thanks Frederic.


---

Comment by vdelecroix created at 2013-07-04 11:52:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-02 14:14:06

Resolution: fixed
