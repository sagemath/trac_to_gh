# Issue 8327: Implement the universal cyclotomic field, using Zumbroich basis

Issue created by migration from https://trac.sagemath.org/ticket/8327

Original creator: nthiery

Original creation time: 2010-02-22 17:48:55

Assignee: davidloeffler

CC:  sage-combinat cwitty

Keywords: Cyclotomic field, Zumbroich basis

Here is a user story for this feature.

We construct the universal cyclotomic field::


```
    sage: F = CyclotomicField()
```


This field contains all roots of unity:


```
    sage: z3 = F.zeta(3)
    sage: z3
    E(3)
    sage: z3^3
    1
    sage: z5 = F.zeta(5)
    sage: z5
    E(5)
    sage: z5^5
    1
```


It comes equipped with a distinguished basis, called the Zumbroich
basis, which consists of a strict subset of all roots of unity::


```
    sage: z9 = F.zeta(9)
    -E(9)^4-E(9)^7
    sage: z3 * z5
    sage: E(15)^8
    sage: z3 + z5
    -E(15)^2-2*E(15)^8-E(15)^11-E(15)^13-E(15)^14
    sage: [z9^i for i in range(0,9)]
    [1, -E(9)^4-E(9)^7, E(9)^2, E(3), E(9)^4, E(9)^5, E(3)^2, E(9)^7, -E(9)^2-E(9)^5 ]
```


Note: we might want some other style of pretty printing.

The following is called AsRootOfUnity in Chevie; we might want instead
to use (z1*z3).multiplicative_order()::


```
    sage: (z1*z3).as_root_of_unity()
    11/18
```


Depending on the progress on #6391 (lib gap), we might want to
implement this directly in Sage or to instead expose GAP's
implementation, creating elements as in::


```
sage: z5 = gap("E(5)")
sage: z3 = gap("E(3)")
sage: z3+z5
-E(15)^2-2*E(15)^8-E(15)^11-E(15)^13-E(15)^14
```



---

Comment by craigcitro created at 2010-02-22 19:03:44

So this seems interesting (I'd never heard of the Zumbrioch basis before). I don't have anything useful to say about the utility of this, or implementing it.

However, I'd like to suggest we might want to use a different convention for the constructor -- I don't like the idea of `CyclotomicField()` working. That seems like something that's too easy for a user to accidentally do (leave out the `n` they intended to use), and I'd much rather they see an error than have it quietly succeed, only to discover that their cyclotomic field isn't quite what they expected (and likely slower to boot). Maybe something like `F = CyclotomicField(n=Infinity)`?


---

Comment by nthiery created at 2010-02-22 21:46:41

Replying to [comment:2 craigcitro]:
> So this seems interesting (I'd never heard of the Zumbrioch basis before). I don't have anything useful to say about the utility of this, or implementing it.
> 
> However, I'd like to suggest we might want to use a different convention for the constructor -- I don't like the idea of `CyclotomicField()` working. That seems like something that's too easy for a user to accidentally do (leave out the `n` they intended to use), and I'd much rather they see an error than have it quietly succeed, only to discover that their cyclotomic field isn't quite what they expected (and likely slower to boot). Maybe something like `F = CyclotomicField(n=Infinity)`?

I indeed take any better suggestion! In Gap that would be Cyclotomics, but it does sound good in Field in the name. n=infinity might be misleading, since it's not about infinite roots of unity.


---

Comment by craigcitro created at 2010-02-22 21:48:39

Replying to [comment:3 nthiery]:
> I indeed take any better suggestion! In Gap that would be Cyclotomics, but it does sound good in Field in the name. n=infinity might be misleading, since it's not about infinite roots of unity.

True. Maybe it's a bit too "cutesy," but using `n=0` might be nice -- after all, the `n`th cyclotomic field has roots of unity for all divisors of `n`, so this would still hold for the universal cyclotomic field and `n=0`.


---

Comment by nthiery created at 2010-03-08 14:11:14

Replying to [comment:4 craigcitro]:
> True. Maybe it's a bit too "cutesy," but using `n=0` might be nice -- after all, the `n`th cyclotomic field has roots of unity for all divisors of `n`, so this would still hold for the universal cyclotomic field and `n=0`.

Mmm, any complex number is a 0-th root of unity, isn't it?


---

Comment by stumpc5 created at 2010-06-04 13:04:33

Does anyone have a pdf copy of Zumbroich's thesis where the algorithms are described?

There is a nice version of a modified Zumbroich basis in the article I used (both are implemented in the attached file) but I don't see how the author expresses any root of unity in terms of the basis (probably just due to my lack of knowledge). But Zumbroich should describe it in more detail in his thesis.


---

Comment by stumpc5 created at 2010-06-04 13:04:33

Changing status from new to needs_work.


---

Comment by stumpc5 created at 2010-06-07 01:50:37

The attached class NewCyclotomicField uses the modified Zumbroich basis and behaves already somehow as it should (beside pretty printing).

If people think the Zumbroich basis itself is nicer, it's easy to change. I personally think the modified version as defined in Breuer - "Integral bases for subfields of cyclotomic fields" AAECC8, 279--289 (1997) has nicer properties (see the definition of the set S_n and Remark 1).

Here are some implementation problems I have:

    - how can I replace CombinatorialAlgebra by a new field constructor (I haven't found a description how to define a field)?

    - how can I embed a CombinatorialAlgebra into another one (here: NewCyclotomicField(m) into NewCyclotomicField(n) for m | n)?

    - how can I define a new class UniversalCyclotomicField containing all cyclotomic fields?

    - how can I define the attribute self._one in the constructor of NewCyclotomicField properly?


---

Comment by stumpc5 created at 2010-09-19 23:55:42

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2011-01-19 15:54:12

Apply trac_8327_universal_cyclotomic_field-cs.2.patch

(for patchbot -- I hope that's right!). 

This doesn't quite look ready to me. I haven't tried applying the patch, but just on a visual check, I can see that lots of methods aren't documented or have no tests (*every* function added to Sage must be doctested, even those whose entire body is `"raise NotImplementedError"`). Also, the new module should be added to the reference manual, and the formatting should be valid ReST markup. 

I very much hope you can get this code into shape -- it'd be a great thing to have in Sage -- but for now I'm afraid it's a thumbs down.


---

Comment by davidloeffler created at 2011-01-19 15:54:12

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2011-01-19 15:56:19

I've looked at the patchbot logs, and it gets worse -- the Cython code isn't valid apparently.


---

Comment by stumpc5 created at 2011-01-26 03:15:26

Replying to [comment:13 davidloeffler]:
> I've looked at the patchbot logs, and it gets worse -- the Cython code isn't valid apparently.

This was only as cython booleans changed in the meantime. Beside that, the code was always working properly. I changed this minor problem, and it should be working now again.

I improved the documentation but there are still some things to be done...


---

Comment by stumpc5 created at 2011-02-22 18:08:23

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2011-02-22 18:08:23

For the buildbot:

Apply trac_8327_universal_cyclotomic_field-cs.patch

All other files are obsolete, but I cannot delete them. Some documentation is still missing, but only for methods which are helper functions for others.

Would be nice to get some feedback!


---

Comment by stumpc5 created at 2011-02-24 17:39:35

Can some delete all but the youngest attached patch, the buildbot gets confused.

Thanks, Christian


---

Comment by davidloeffler created at 2011-03-18 12:19:50

Apply trac_8327_universal_cyclotomic_field-cs.patch


---

Comment by stumpc5 created at 2011-03-23 22:13:45

Apply only trac_8327_universal_cyclotomic_field-cs.patch


---

Comment by stumpc5 created at 2011-04-18 18:53:06

Apply only trac_8327_universal_cyclotomic_field-cs.patch


---

Comment by stumpc5 created at 2011-04-24 19:22:22

Apply only trac_8327_universal_cyclotomic_field-cs.patch


---

Comment by chapoton created at 2011-06-10 10:13:32

Apply trac_8327_universal_cyclotomic_field-cs.patch


---

Comment by stumpc5 created at 2011-06-10 11:52:30

Remove assignee davidloeffler.


---

Comment by nthiery created at 2011-11-15 09:28:09

When applying the sage-combinat queue on sage 4.8.alpha0, we got a compilation error on universal_cyclotomic_field_c.pyx, most likely due to the updated cython (#11761)


---

Comment by nthiery created at 2011-11-15 09:28:09

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-11-15 20:40:54

Replying to [comment:26 nthiery]:
> When applying the sage-combinat queue on sage 4.8.alpha0, we got a compilation error on universal_cyclotomic_field_c.pyx, most likely due to the updated cython (#11761)

My patch seems to fix the problem. At least, when one uses the new Cython spkg and applies the combinat queue up to and including Christian's patch and adds my patch as well (which is also in the combinat queue, I think), then sage builds and starts.

Note that the my patch does not add the new  Cython as a dependency - it should run with the old Cython as well.

However, I already get a doctest error in `devel/sage-combinat/doc/en/thematic_tutorials/sandpile.rst`. Now it is needed to test whether this error is due to the patches from here, or due to some other patch in the combinat queue.

Since it is not sure whether THIS ticket is the culprit, and since it builds with the new cython, I am promiting it to "needs review".


Apply trac_8327_universal_cyclotomic_field-cs.patch trac_8327_universal_cyclotomic_field_new_cython-sk.patch


---

Comment by SimonKing created at 2011-11-15 20:40:54

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-11-15 20:43:28

Sorry, I forgot to change the ticket description.


---

Comment by SimonKing created at 2011-11-15 20:50:05

Note that the first patch does not apply on a clean sage-4.8.alpha0: The hunk that adds `from sage.misc.lazy_import import lazy_import` to sage/categories/all.py does not match.

But is importing lazy_import really needed? If I see that correctly, it is not used in sage/categories/all.py


---

Comment by SimonKing created at 2011-11-15 20:50:05

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-11-15 20:52:38

Gosh. And my patch fails to apply as well, in both hunks.

So, apparently there is a dependency in the combinat queue. It should be named as a dependency for this ticket.


---

Comment by SimonKing created at 2011-11-15 20:56:03

Replying to [comment:30 SimonKing]:
> Gosh. And my patch fails to apply as well, in both hunks.

O dear, where is my mind? I had accidentally reverted the order of the patches when I tried to apply my patch.

So, for the record: The first patch does need to be rebased (or a dependency must be given). The second patch applies cleanly.


---

Comment by SimonKing created at 2011-11-15 21:47:40

There are several doctest errors, even when one just has

```
11761-cython-0.15-rebased.patch
trac12029_clonable_int_array_2_list.patch
trac_8327_universal_cyclotomic_field-cs.patch
trac_8327_universal_cyclotomic_field_new_cython-sk.patch
```

with the obvious modification on `trac_8327_universal_cyclotomic_field-cs.patch`.

Namely:

```
        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # 25 doctests failed
        sage -t  devel/sage-main/sage/modules/free_module.py # 2 doctests failed
        sage -t  devel/sage-main/sage/modular/modsym/p1list_nf.py # 5 doctests failed
        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field_c.pyx # 1 doctests failed
```


This one here

```
File "/mnt/local/king/SAGE/rebase/sage-4.8.alpha0/devel/sage-main/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field_c.pyx", line 239:
    sage: ZumbroichDecomposition_list( 6, 1 )
Expected:
    array([1, 1])
Got:
    [1, 1]
```

could be caused by my patch, which touches `ZumbroichDecomposition`. However, I have no idea about the other errors.


---

Comment by stumpc5 created at 2011-11-16 07:01:21

Thanks for working in this patch -- I will have a look at it this morning and see what the issues are...

Best, Christian


---

Comment by stumpc5 created at 2011-11-16 07:11:21

Replying to [comment:33 stumpc5]:
> Thanks for working in this patch -- I will have a look at it this morning and see what the issues are...

I guess, I should first compile 4.7.2; that will take a while first...


---

Comment by nthiery created at 2011-11-16 07:39:38

> > Thanks for working in this patch -- I will have a look at it this morning and see what the issues are...

Cool!

> I guess, I should first compile 4.7.2; that will take a while first...

4_8 alpha0 actually

Cheers,


---

Comment by stumpc5 created at 2011-11-16 08:22:06

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2011-11-16 08:22:06

I found the bug and fixed it, all the above doctests now work (but only on 4.7.1, the other version is still building and will take more time).

What about "needs more doctests and Sphinxified docstrings"? I agree that the cython part is still not well documented. Could you be specific where I should explain better what's going on? Part of the problem is that computing the Zumbroich basis is something that is not simple to understand without really looking at the paper. And even after understanding that, everything becomes unreadable after implementing it in a (hopefully fairly) fast way in cython...


---

Comment by SimonKing created at 2011-11-16 09:19:02

Replying to [comment:36 stumpc5]:
> I found the bug and fixed it, all the above doctests now work (but only on 4.7.1, the other version is still building and will take more time).

Good! I'll test it a bit later.

> What about "needs more doctests and Sphinxified docstrings"? I agree that the cython part is still not well documented. Could you be specific where I should explain better what's going on?

If by "you" you mean me, then I can't: The statement "needs more doctests ..." has been there before and is due to David Loeffler. I didn't come that far in reading the patch, I was first testing whether it applies, builds and passes tests.


---

Comment by davidloeffler created at 2011-11-16 09:46:56

Replying to [comment:37 SimonKing]:

> If by "you" you mean me, then I can't: The statement "needs more doctests ..." has been there before and is due to David Loeffler. I didn't come that far in reading the patch, I was first testing whether it applies, builds and passes tests.
> 

(That was 10 months ago and applied to a much earlier version of the patch.)


---

Comment by stumpc5 created at 2011-11-16 09:50:38

> (That was 10 months ago and applied to a much earlier version of the patch.)

I now remember seeing it back then, the patch indeed changed substantially since then. So I guess it simply needs a new review.


---

Comment by davidloeffler created at 2011-11-16 09:53:51

It's perfectly permissible, and indeed a good idea, to clear the "work issues" field when uploading a new patch.


---

Comment by SimonKing created at 2011-11-16 10:42:24

When starting with sage-4.8.alpha0 plus the stuff from #11761 (new cython), one quite big hunk of your new patch fails to apply. It concerns sage/categories/fields.py.

I found at least one reason for the mismatch: By trac ticket #10771 (sorry, it's one of mine...), `Fields()` has some `ElementMethods` (your patch assumes that there are none). Since #10771 has been merged in sage-4.7.2, I make this a dependency.

Well, I understand that you are building 4.7.2 anyway, aren't you?


---

Comment by SimonKing created at 2011-11-16 10:42:24

Changing status from needs_review to needs_work.


---

Comment by stumpc5 created at 2011-11-16 11:34:35

Replying to [comment:41 SimonKing]:
> When starting with sage-4.8.alpha0 plus the stuff from #11761 (new cython), one quite big hunk of your new patch fails to apply. It concerns sage/categories/fields.py.
> 
> I found at least one reason for the mismatch: By trac ticket #10771 (sorry, it's one of mine...), `Fields()` has some `ElementMethods` (your patch assumes that there are none). Since #10771 has been merged in sage-4.7.2, I make this a dependency.
> 
> Well, I understand that you are building 4.7.2 anyway, aren't you

I am building 4.7.2 and 4.8, but te later just failed to build... l will do the rebase after 4.7.2 has finished (or you do it, if 
you want to, it will basically take the whole day until the building is done)


---

Comment by SimonKing created at 2011-11-16 11:44:14

Replying to [comment:42 stumpc5]:
> I am building 4.7.2 and 4.8, but te later just failed to build...

What, 4.8.alpha0 (or alpha1) failed to build?? That should not happen. Perhaps you can report on sage-release?


---

Comment by nthiery created at 2011-11-16 12:51:59

Replying to [comment:41 SimonKing]:
> When starting with sage-4.8.alpha0 plus the stuff from #11761 (new cython), one quite big hunk of your new patch fails to apply. It concerns sage/categories/fields.py.
> 
> I found at least one reason for the mismatch: By trac ticket #10771 (sorry, it's one of mine...), `Fields()` has some `ElementMethods` (your patch assumes that there are none). Since #10771 has been merged in sage-4.7.2, I make this a dependency.

IIRC, this patch already applies on 4.7.2: I already rebased it last week upon 10771. Ah ah, I was in a hurry, and probably forgot to upload it on trac, sorry. Please take the latest version from the sage-combinat patch server.


---

Comment by stumpc5 created at 2011-11-16 13:27:48

Replying to [comment:44 nthiery]:
> Replying to [comment:41 SimonKing]:
> > When starting with sage-4.8.alpha0 plus the stuff from #11761 (new cython), one quite big hunk of your new patch fails to apply. It concerns sage/categories/fields.py.
> > 
> > I found at least one reason for the mismatch: By trac ticket #10771 (sorry, it's one of mine...), `Fields()` has some `ElementMethods` (your patch assumes that there are none). Since #10771 has been merged in sage-4.7.2, I make this a dependency.
> 
> IIRC, this patch already applies on 4.7.2: I already rebased it last week upon 10771. Ah ah, I was in a hurry, and probably forgot to upload it on trac, sorry. Please take the latest version from the sage-combinat patch server.

I did the same mistake the other way round: I did changes about 5 weeks ago, and only putted it on trac but not on the combinat queue...

I just merged both versions, and the doctest should pass now, and it should be rebased (both only if I didn't do any mistakes...).


---

Comment by SimonKing created at 2011-11-16 14:41:53

The new patch does not apply, because of the hunk

```
--- all.py
+++ all.py
@@ -1,3 +1,5 @@
+from sage.misc.lazy_import import lazy_import
+
 from category import    is_Category, Category, HomCategory

```


The point is that this hunk shold be totally removed, because lazy import is not needed in sage/categories/all.py.

For testing, I'm doing this change myself. But please post a patch without that hunk


---

Comment by SimonKing created at 2011-11-16 14:53:30

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-11-16 14:53:30

Sorry, lazy_import _is_ used. So, don't delete the patch. However, it does not apply. Reason: The first line of sage/categories/all.py currently is

```
from category import    is_Category, Category, HomCategory, AbstractCategory
```

My guess is that you worked on top of Nicolas's "multiple realizations" patch.

So, either submit a patch on trac that differs from the one in the combinat queue, or name #7980 as a dependency.

Suggestion: I can manually rebase your patch, so that I can test (and review) it now. The merge conflict is trivial and can be sorted out later.


---

Comment by stumpc5 created at 2011-11-16 14:57:03

Replying to [comment:47 SimonKing]:
> Suggestion: I can manually rebase your patch, so that I can test (and review) it now. The merge conflict is trivial and can be sorted out later.

I am a little lost now: you don't want the current patch but the one I
had before without Nicolas' rebase?


---

Comment by SimonKing created at 2011-11-16 15:33:54

Replying to [comment:48 stumpc5]:
> I am a little lost now: you don't want the current patch but the one I
> had before without Nicolas' rebase?

The patch that is attached here does not apply on pure sage-4.7.2 or sage-4.8.alpha0. The reason is that this patch depends on Nicolas's patch from #7980.

So, at some point, the merge conflict has to be sorted out. However, for my review I don't need that you rebase it now.


---

Comment by SimonKing created at 2011-11-16 16:01:07

I get one error in startup.py:

```
File "/mnt/local/king/SAGE/rebase/sage-4.8.alpha0/devel/sage-main/sage/tests/startup.py", line 13:
    sage: sage0("'numpy' in sys.modules")
Expected:
    False
Got:
    True
```


Do you import numpy at startup? Nicolas has just found that ticket #11714 explicitly avoids numpy being loaded at startup.


---

Comment by SimonKing created at 2011-11-16 16:04:40

You import and cimport numpy. Nicolas suggest to try and lazy_import numpy instead of import (cimport should be fine).


---

Comment by SimonKing created at 2011-11-16 16:16:41

... or lazy-import the stuff from sage/rings/universal_cyclotomic_field/all.py? I'm preparing a patch that does this.


---

Comment by SimonKing created at 2011-11-16 16:21:44

OK, done.

When applying both patches, one gets

```
sage: 'numpy' in sys.modules
False
sage: sage0("'numpy' in sys.modules")
False
sage: UCF
Universal Cyclotomic Field endowed with the Zumbroich basis
sage: 'numpy' in sys.modules
True
sage: sage0("'numpy' in sys.modules")
False
```

So, numpy is only imported when needed, and this is what #11714 was about.

Apply trac_8327_universal_cyclotomic_field-cs.patch trac8327_lazy_import_UCF.patch


---

Comment by SimonKing created at 2011-11-16 22:02:11

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-11-16 22:02:11

Starting with sage-4.8.alpha0 plus the new Cython plus your patch (rebased in the obvious way) plus the lazy_import patch, we are down to one error:

```
sage -t  "devel/sage-main/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field.py"
**********************************************************************
File "/mnt/local/king/SAGE/rebase/sage-4.8.alpha0/devel/sage-main/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field.py", line 274:
    sage: UCF.is_subring(UCF)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /mnt/local/king/.sage/tmp/universal_cyclotomic_field_4421.py
         [3.3 s]
```

Any idea why that occurs?


---

Comment by stumpc5 created at 2011-11-17 08:34:36

Replying to [comment:54 SimonKing]:
>     sage: UCF.is_subring(UCF)
> Expected:
>     True
> Got:
>     False

UCF.is_subring(UCF) just returns

```
sage: UCF is UCF
```

and as `UniversalCyclotomicField` inherits from `UniqueRepresentation`, this should return `True`. I don't know if this error might come from some lazy import which makes UCF not unique, or if something changed in `UniqueRepresentation`? Nicolas might know...


---

Comment by nthiery created at 2011-11-17 13:42:49

Replying to [comment:55 stumpc5]:
> UCF.is_subring(UCF) just returns
> {{{
> sage: UCF is UCF
> }}}
> and as `UniversalCyclotomicField` inherits from `UniqueRepresentation`, this should return `True`.

That's independent of UniqueRepresentation: ``X is X`` is true for any
Python object X.

So the test above breaks, my best bet is that the is_ring method that
gets called is the wrong one.

Good chase!
				Nicolas


---

Comment by stumpc5 created at 2011-11-18 11:21:30

Replying to [comment:56 nthiery]:
> Replying to [comment:55 stumpc5]:
> So the test above breaks, my best bet is that the is_ring method that
> gets called is the wrong one.

I found the problem with building sage (see #11970).

4.7.2 has finished, and I now build 4.8.alpha1. I will investigate the above problem as soon as it is finished...


---

Comment by stumpc5 created at 2011-11-18 17:15:15

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2011-11-18 17:15:15

It is rebased and applies now on a new 4.8.alpha1 (NOT alpha0, but alpha1!)

There was a syntax error on the plain 4.8.alpha1, which I first had to get rid off.

Concerning the is_subring method, I get the following behaviour:


```
sage: UCF is UCF
True

sage: UCF.is_subring??
    def is_subring(self,other):
        r"""
        Returns currently True if ``self`` and ``other`` coincide.

        EXAMPLES::

            sage: UCF.is_subring(UCF)
            True
        """
        return other is self

sage: UCF.is_subring(UCF)
False
```


This behaviour seems to be wired! But when replacing the lazy import of the UCF by a proper import in sage.rings.all, the wired behaviour disappears, so the problem must be something with the lazy import!


---

Comment by nthiery created at 2011-11-18 22:42:58

Replying to [comment:58 stumpc5]:
> {{{
> sage: UCF.is_subring(UCF)
> False
> }}}
> 
> This behaviour seems to be wired! But when replacing the lazy import of the UCF by a proper import in sage.rings.all, the wired behaviour disappears, so the problem must be something with the lazy import!

Ach ja! Sorry, I should have thought about this: it is an instance of
#10906: "lazy import can break unique representation". So UCF should
not be lazy imported. One probably can't lazy cimport numpy in
universal_cyclotomic_field_c.pyx. Hopefully one could replace, in
universal_cyclotomic_field.py:


```
from sage.rings.universal_cyclotomic_field.universal_cyclotomic_field_c import * 
```


by explicit lazy imports of the various functions:


```
lazy_import('sage.rings.universal_cyclotomic_field.universal_cyclotomic_field_c', 'ZumbroichBasis...')
```


or maybe just lazy import that module as, say, ucfc, and qualify all
its functions with it.

I don't have a working Sage in which I could insert the UCF patch
right now. But let me know if you need help!

Cheers,
				Nicolas


---

Comment by stumpc5 created at 2011-11-18 23:45:58

Replying to [comment:59 nthiery]:
> Replying to [comment:58 stumpc5]:
> {{{
> lazy_import('sage.rings.universal_cyclotomic_field.universal_cyclotomic_field_c', 'ZumbroichBasis...')
> }}}

I now do that, and all tests pass -- but I somehow missed why we want to lazy import anything; is it about importing numpy?


---

Comment by SimonKing created at 2011-11-18 23:57:18

Replying to [comment:60 stumpc5]:
> I now do that, and all tests pass -- but I somehow missed why we want to lazy import anything; is it about importing numpy?

Apparently, there was a patch recently merged that explicitly had the purpose of "do not import numpy at startup". SO, I guess it would be better to not re-introduce the numpy import, unless we _really_ need it.


---

Comment by stumpc5 created at 2011-11-19 08:29:35

Replying to [comment:61 SimonKing]:
> Replying to [comment:60 stumpc5]:
> Apparently, there was a patch recently merged that explicitly had the purpose of "do not import numpy at startup". SO, I guess it would be better to not re-introduce the numpy import, unless we _really_ need it.

I see -- I made some mistake last night, but now, the cython part is lazy imported, and all tests pass...


---

Comment by nthiery created at 2011-11-19 09:11:44

Replying to [comment:62 stumpc5]:
> I see -- I made some mistake last night, but now, the cython part is lazy imported, and all tests pass...

Cool. Thanks! This is as much saved for Sage's startup.

Cheers,
                     Nicolas


---

Comment by mhansen created at 2011-12-18 13:19:40

Ping.  I think we should try to get this in shortly.


---

Comment by stumpc5 created at 2011-12-18 13:24:42

Replying to [comment:64 mhansen]:
> Ping.  I think we should try to get this in shortly.

+1.

Simon, are you planning to review it? Or anyone else volunteering?

Christian


---

Comment by SimonKing created at 2011-12-18 14:13:57

I'm a bit lost. I am listed as an author, and some comments mention a patch of mine. But where is that patch? I'm talking about trac_8327_universal_cyclotomic_field_new_cython-sk.patch 

Similarly, where is trac8327_lazy_import_UCF.patch ?

I thought it is impossible (unless for administrators) to remove an attachment from trac?

Also, there are two work issues mentioned. Are these fixed? I.e., is it really "needs review", or is it "needs work"?


---

Comment by stumpc5 created at 2011-12-18 14:26:31

Replying to [comment:66 SimonKing]:
> I'm a bit lost. I am listed as an author, and some comments mention a patch of mine. But where is that patch? I'm talking about trac_8327_universal_cyclotomic_field_new_cython-sk.patch 
> 
> Similarly, where is trac8327_lazy_import_UCF.patch ?

As your patches were only a few lines, I folded them into mine so the whole ticket is easier to handle (and then deleted your patches to not confuse the patchbot).

> I thought it is impossible (unless for administrators) to remove an attachment from trac?

I guess, I have admin rights then.

> Also, there are two work issues mentioned. Are these fixed? I.e., is it really "needs review", or is it "needs work"?

sorry for not deleting them, I fixed both 4 weeks ago (though I don't know if there is another rebase needed for 
sage-4.8.alpha4).

Best, Christian


---

Comment by davidloeffler created at 2011-12-18 14:38:06

Replying to [comment:67 stumpc5]:
> (though I don't know if there is another rebase needed for sage-4.8.alpha4).

No need -- patch applies fine to 4.8.alpha4. The new files pass their doctests (I haven't run a full doctest cycle).


---

Comment by SimonKing created at 2011-12-18 14:42:50

Replying to [comment:67 stumpc5]:
> > I thought it is impossible (unless for administrators) to remove an attachment from trac?
> 
> I guess, I have admin rights then.

If you just didn't want to confuse the patchbot, you should insert a line in some comment, stating what patches have to be applied in what order:

Apply trac_8327_universal_cyclotomic_field-cs.patch

But then, what is the status of your "syntax error" patch?


---

Comment by stumpc5 created at 2011-12-18 14:54:17

Replying to [comment:69 SimonKing]:
> But then, what is the status of your "syntax error" patch?

I wasn't able to run 4.8.alpha1 due to a non-ascii character in /rings/arith.py. The patch only deletes this character -- I don't know if it is still present in 4.8.alpha4, but I will check after it has finished building.


---

Comment by davidloeffler created at 2012-03-10 14:41:25

Apply trac_8327-rebased_for_v5.patch

(for the patchbot).

The previous patch conflicts with #4539, so I have done a new rebased patch. There was one change in `free_module.py` which was rejected, and whose purpose was not at all clear to me, so I didn't include it in the rebased patch -- all doctests seem to pass without it.


---

Comment by davidloeffler created at 2012-03-29 12:16:45

And now it's failing to apply again with the latest beta (5.0.beta11), due to a conflict in sage/categories/all.py coming from with #7980.


---

Comment by davidloeffler created at 2012-03-29 12:16:45

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-30 07:57:20

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-03-30 07:57:20

I've re-rebased the patch.


---

Comment by davidloeffler created at 2012-03-30 08:44:36

Apply trac_8327-rebased_for_v5.patch, trac_8327-docfix.patch

(I got some error messages building the documentation -- the above patch fixes them.)


---

Comment by davidloeffler created at 2012-03-30 08:55:03

Apply trac_8327-rebased_for_v5.patch, trac_8327-docfix.patch

(patchbot's confused again)


---

Comment by nthiery created at 2012-03-30 09:04:14

Hi guys,

Just my 2 cents, but Christian did an awfull amount of work on this patch; I really appreciate your efforts to help him get this in (I should participate to that too!), and I know you added yourself to share the blame in case of trouble later; still I feel he deserves to be single author. What do you think?

Cheers,
                           Nicolas


---

Comment by davidloeffler created at 2012-03-30 09:06:58

Sure -- my contribution was just rebasing + reformatting some docstrings. I've removed myself as author (but added myself as reviewer).


---

Comment by stumpc5 created at 2012-03-30 10:25:12

Hi,

Thanks for pushing the patch forward - I actually don't care whose name appears in the authors field, but I would appreciate if we can get the patch ready soon (maybe even for 5.0)!

I have a slightly newer version of the patch locally containing some missing docstrings and stuff. Do you mind if I delete all 4 attached patches and push one patch containing

+ all my new docstrings

+ rebased for 5.0.beta6 (is that recent enough? I haven't build anything newer, so I cannot rebase the patch for beta11; I could do that tomorrow after building.)

+ David's improvements in the docstrings

?

Best, Christian


---

Comment by davidloeffler created at 2012-03-30 10:34:19

I think it would be rather counterproductive to erase a patch that applies to the current beta, and replace it with one that almost certainly wouldn't. The most recent bout of conflicts was caused by #7980, which was only merged in beta11. So please build a copy of beta11 before you do any further work on this.


---

Comment by stumpc5 created at 2012-03-30 10:42:51

Replying to [comment:81 davidloeffler]:
> I think it would be rather counterproductive to erase a patch that applies to the current beta, and replace it with one that almost certainly wouldn't. The most recent bout of conflicts was caused by #7980, which was only merged in beta11. So please build a copy of beta11 before you do any further work on this.

Alright, I will then first build and do attach another version tomorrow then.


---

Comment by nthiery created at 2012-03-30 16:02:34

Replying to [comment:82 stumpc5]:
> Replying to [comment:81 davidloeffler]:
> > I think it would be rather counterproductive to erase a patch that applies to the current beta, and replace it with one that almost certainly wouldn't. The most recent bout of conflicts was caused by #7980, which was only merged in beta11. So please build a copy of beta11 before you do any further work on this.
> 
> Alright, I will then first build and do attach another version tomorrow then.

For the record: if Christian's latest version is that on the sage-combinat patch server, then it should be already based on #7980 and likely to apply smoothly.


---

Comment by stumpc5 created at 2012-03-30 18:24:24

I attached a new version that contains everything I have, which is rebased for 5.0.beta11, and also contains David's docfixes.


---

Comment by davidloeffler created at 2012-03-30 20:06:25

Apply trac_8327_universal_cyclotomic_field-cs.patch 

(for patchbot)


---

Comment by davidloeffler created at 2012-03-30 20:53:03


```
sage -t  -force_lib devel/sage-8327/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field_c.pyx
**********************************************************************
File "/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8327/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field_c.pyx", line 239:
    sage: ZumbroichDecomposition_list( 6, 1 )
Expected:
    array([1, 1])
Got:
    [1, 1]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage/tmp/fermat-21656/universal_cyclotomic_field_c_22797.py
	 [1.7 s]
sage -t  -force_lib devel/sage-8327/sage/rings/polynomial/polynomial_quotient_ring.py
**********************************************************************
File "/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8327/sage/rings/polynomial/polynomial_quotient_ring.py", line 262:
    sage: [s for s in dir(Q.category().element_class) if not s.startswith('_')]
Expected:
    ['cartesian_product', 'gcd', 'is_idempotent', 'is_one', 'lcm', 'lift']
Got:
    ['cartesian_product', 'gcd', 'is_idempotent', 'is_one', 'is_unit', 'lcm', 'lift']
**********************************************************************
1 items had failures:
   1 of  30 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage/tmp/fermat-21656/polynomial_quotient_ring_22987.py
	 [42.5 s]
sage -t  -force_lib devel/sage-8327/sage/tests/startup.py
**********************************************************************
File "/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8327/sage/tests/startup.py", line 13:
    sage: sage0("'numpy' in sys.modules")
Expected:
    False
Got:
    True
**********************************************************************
```


(All three of these failures had already been reported, and fixed, before this latest patch re-broke them.)


---

Comment by davidloeffler created at 2012-03-30 20:53:03

Changing status from needs_review to needs_work.


---

Comment by stumpc5 created at 2012-03-31 07:19:51

Replying to [comment:87 davidloeffler]:
> (All three of these failures had already been reported, and fixed, before this latest patch re-broke them.)

These were not fixed in the docfix patch but in the rebase patch, so I didn't see them. (I actually fixed the first, but forgot to refresh the patch afterwards.)

I now attached the new version that should have the issues fixed. including the last which seems to me like not related to this patch, is it?


---

Comment by davidloeffler created at 2012-03-31 08:20:04

Replying to [comment:88 stumpc5]:
>
> I now attached the new version that should have the issues fixed. including the last which seems to me like not related to this patch, is it?

It is related to your patch, as discussed in the comment thread above. It is important that Sage *must not* import numpy at startup, because it takes a very long time to load (cf. tickets #11714, #6494, and several others I think). Your patch causes numpy to be imported at startup; Nicolas and Simon put in a fair bit of work using `lazy_import` to stop this happening (see comments 50-53). You will see that [attachment:trac_8327-rebased_for_v5.patch] does not need to disable this test in startup.py as you have done.


---

Comment by stumpc5 created at 2012-03-31 08:56:25

Replying to [comment:89 davidloeffler]:
> Replying to [comment:88 stumpc5]:

> It is related to your patch, as discussed in the comment thread above. It is important that Sage *must not* import numpy at startup, because it takes a very long time to load (cf. tickets #11714, #6494, and several others I think). Your patch causes numpy to be imported at startup; Nicolas and Simon put in a fair bit of work using `lazy_import` to stop this happening (see comments 50-53). You will see that [attachment:trac_8327-rebased_for_v5.patch] does not need to disable this test in startup.py as you have done.

Were is my mind, thanks for telling me again! -- The patch attached here and the one I had on the combinat queue were both changed, I now made numpy got lazy imported again. I will post the patch as soon as there are no further test failures.


---

Comment by stumpc5 created at 2012-03-31 09:19:18

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2012-03-31 09:19:18

numpy is now lazy imported:


```
sage: 'numpy' in sys.modules
False
sage: sage0("'numpy' in sys.modules")
False
sage: UCF
Universal Cyclotomic Field endowed with the Zumbroich basis
sage: 'numpy' in sys.modules
False
sage: E(5)
E(5)
sage: 'numpy' in sys.modules
True
sage: sage0("'numpy' in sys.modules")
False
```


I hope I haven't forgotten any further things!


---

Comment by davidloeffler created at 2012-03-31 11:00:01

Apply trac_8327_universal_cyclotomic_field-cs.patch

(for patchbot)


---

Comment by davidloeffler created at 2012-03-31 16:02:00

Right, so now we have a patch which actually works, we can start testing it. And we find the following bug:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: z1 = E(3)
sage: z2 = UCF(CyclotomicField(3).gen())
sage: z1 == z2
False
sage: z1 + z2 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
| Sage Version 5.0.beta11, Release Date: 2012-03-28                  |
| Type notebook() for the GUI, and license() for information.        |
/home/masiao/<ipython console> in <module>()

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11990)()

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement._add_ (sage/structure/element.c:8612)()

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field.pyc in _add_(self, other)
    890                 E(12)^4 - E(12)^7 - E(12)^11
    891             """
--> 892             n,m = self.field_order(),other.field_order()
    893             l = cached_lcm( [ n, m ] )
    894 

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field.pyc in field_order(self)
   1020                 3
   1021             """
-> 1022             if bool(self.value._monomial_coefficients):
   1023                 return iter(self.value._monomial_coefficients).next()[0]
   1024             else:

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2919)()

/storage/masiao/sage-5.0.beta11/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:3329)()

AttributeError: 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic' object has no attribute '_monomial_coefficients'
```


This is even worse, since the element involved isn't cyclotomic in the first place:

```
sage: K.<a> = NumberField(x^3 - 7)
sage: UCF(a)                      
a
sage: UCF(a) in UCF
True
```


In fact UCF will attempt to construct an element from anything whatsoever:

```
sage: UCF(None)
None
sage: UCF(QQ)
Rational Field
sage: UCF('hello')
'hello'
```


The following are not great either:

```
sage: UCF.has_coerce_map_from(CyclotomicField(3))
False
sage: QQbar.has_coerce_map_from(UCF)
False
```



---

Comment by davidloeffler created at 2012-03-31 16:02:00

Changing status from needs_review to needs_work.


---

Comment by stumpc5 created at 2012-03-31 17:36:48

Replying to [comment:93 davidloeffler]:

> In fact UCF will attempt to construct an element from anything whatsoever:
> {{{
> sage: UCF(None)
> None
> sage: UCF(QQ)
> Rational Field
> sage: UCF('hello')
> 'hello'
> }}}

I didn't implement the `__call__` method - what is the behaviour you would expect here?

> The following are not great either:
> {{{
> sage: UCF.has_coerce_map_from(CyclotomicField(3))
> False
> }}}

how can I get a coerce from `CyclotomicField(n)` for all `n`?

> {{{
> sage: QQbar.has_coerce_map_from(UCF)
> False
> }}}

I fixed this.


---

Comment by davidloeffler created at 2012-04-01 11:28:11

Replying to [comment:94 stumpc5]:
> 
> I didn't implement the `__call__` method - what is the behaviour you would expect here?

Oh, I don't know, maybe the same behaviour as every other parent object in the Sage library? The default ` __call__ ` calls ` _element_constructor_ `, which you should override, in order to create an element of self from the given arguments. This includes checking whether the given arguments are reasonable, and raising a TypeError otherwise.

You should also set the attribute wrapped_class for your element class to something other than the default (which is "object"), so the ` __init__` it inherits from ElementWrapper knows what it's supposed to be wrapping and doesn't wrap obviously bogus objects as in the examples above.

> 
> how can I get a coerce from `CyclotomicField(n)` for all `n`?
>

I don't quite understand the question, but if you're going to implement a class and call it "universal cyclotomic field", surely it had better satisfy a universal property with respect to cyclotomic fields? If your question is "how do I recognise a cyclotomic field", you might find ` isinstance(K, sage.rings.number_field.number_field.NumberField_cyclotomic) ` or perhaps ` sage.rings.number_field.number_field.is_CyclotomicField(K) ` helpful. You should also check ` K.coerce_embedding`, since it's possible to create cyclotomic fields with complex embeddings other than the standard one.


---

Comment by stumpc5 created at 2012-04-01 12:34:48

Replying to [comment:95 davidloeffler]:
> Replying to [comment:94 stumpc5]:
> Oh, I don't know, maybe the same behaviour as every other parent object in the Sage library? The default ` __call__ ` calls ` _element_constructor_ `, which you should override, in order to create an element of self from the given arguments. This includes checking whether the given arguments are reasonable, and raising a TypeError otherwise.

The idea is that one should *not* construct elements of the universal cyclotomic field using `UCF(arg)` but only through the function `E`, e.g., `E(5)`. So `UCF(arg)` should only be called for coercion.

I could overwrite `_element_constructor_` by


```
def _element_constructor_(self,arg):
    raise TypeError, "No coercion found for %s"%str(arg)
```


This would prevent `UCF` from ever constructing any element, and only using the coercion model to coerce objects if possible.

> You should also set the attribute wrapped_class for your element class to something other than the default (which is "object"), so the ` __init__` it inherits from ElementWrapper knows what it's supposed to be wrapping and doesn't wrap obviously bogus objects as in the examples above.

Do I see it right that this would then also be obsolete?

> > 
> > how can I get a coerce from `CyclotomicField(n)` for all `n`?
> >
> 
> I don't quite understand the question, but if you're going to implement a class and call it "universal cyclotomic field", surely it had better satisfy a universal property with respect to cyclotomic fields?

Let me define one coercion:


```
sage: from sage.rings.number_field.number_field_morphisms import NumberFieldEmbedding
sage: n = 5
sage: X = CyclotomicField(n)
sage: f = NumberFieldEmbedding(X,UCF,E(n))
sage: UCF.register_coercion(f)
sage: x = X.gen()
sage: UCF(x)
E(5)
```


First, how can I register this coercion for all `n`? Second, are there further number fields I should have a coercion from?


---

Comment by davidloeffler created at 2012-04-01 13:19:35

Aargh! This is so disastrously wrong I don't even know where to start. For heavens' sake, go and read the Sage reference manual -- there's a whole huge tutorial on how to implement coercions properly. 

I think I've had enough of this ticket; perhaps someone else can take over "reviewing" it from here onwards.


---

Comment by stumpc5 created at 2012-04-01 14:02:56

Replying to [comment:97 davidloeffler]:
> Aargh! This is so disastrously wrong I don't even know where to start. For heavens' sake, go and read the Sage reference manual -- there's a whole huge tutorial on how to implement coercions properly. 
> 
> I think I've had enough of this ticket; perhaps someone else can take over "reviewing" it from here onwards.

First, I consider this strongly unfriendly.

Second, after looking again at the coercion section of the reference manual, I still don't see what is so disastrously wrong (which obviously doesn't mean that it is not wrong), and how to tell a parent to register coercion from an infinite family of other parents.


---

Comment by davidloeffler created at 2012-04-01 14:21:53

I'm sorry, please pardon my earlier outburst -- it was uncalled for, your message just caught me at a bad time.

See [http://www.sagemath.org/doc/reference/coercion.html#methods-to-implement](http://www.sagemath.org/doc/reference/coercion.html#methods-to-implement). The magic routines here are ` _element_constructor_` and ` _coerce_map_from_ `. In this case, you can make ` UCF._coerce_map_from_(K) ` return the natural morphism from K to self whenever K is a cyclotomic field (but you need to watch out for cyclotomic fields with non-standard embeddings).


---

Comment by stumpc5 created at 2012-04-01 19:00:13

Replying to [comment:99 davidloeffler]:
> See [http://www.sagemath.org/doc/reference/coercion.html#methods-to-implement](http://www.sagemath.org/doc/reference/coercion.html#methods-to-implement). The magic routines here are

` _coerce_map_from_ `

Thanks, I now see how I can do the coercion here - except that I do not know how to handle non-standard embeddings. I do not know how to test if a non-standard embedding is used, and if so, I also do not know how to coerce then into the `UCF`.

` _element_constructor_`

I want that an element of `UCF` is never constructed using the `__call__` method but only using the function `E`. In the 4 steps in http://www.sagemath.org/doc/reference/coercion.html#provided-methods `__call__`, I want the first 3 to proceed, and if no coercion is found, that an error is raised. The idea here is that `UCF` has an infinite number of generators, and the easiest to play with them seems to be the same way this is done in `GAP`; simply doing things like

```
sage: E(3)     
E(3)
sage: E(3)+E(4)
E(12)^4 - E(12)^7 - E(12)^11
```


Also, I want to see

```
sage: UCF(5)
5
sage: UCF(5).parent()
Universal Cyclotomic Field endowed with the Zumbroich basis
sage: X = CyclotomicField(6)
sage: UCF(X.gen())
-E(3)^2
```


Is this generally wrong, or is the way I proposed to define `_element_constructor_` in my last comment just not the way to do that?


---

Comment by chapoton created at 2012-11-20 09:20:04

Ok, I am willing to try a review. I am not sure to be competent enough. We will see.

Let us first try to get a full green light from the bot. Could you please upload the latest version, rebased on a recent copy of sage ?


---

Comment by stumpc5 created at 2012-11-20 09:22:35

Replying to [comment:101 chapoton]:
> Ok, I am willing to try a review. I am not sure to be competent enough. We will see.
> 
> Let us first try to get a full green light from the bot. Could you please upload the latest version, rebased on a recent copy of sage ?

That would be really great! I will do that now (and also get the documentation into a good state-of-the-art shape), and let you know once the patch is ready for you to look at.


---

Comment by stumpc5 created at 2012-11-20 10:30:41

Replying to [comment:103 stumpc5]:

For a little better readability, I started by extracting two minor changes in other parts of Sage into two new tickets, #13727 and #13728.


---

Comment by stumpc5 created at 2012-11-20 11:57:49

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2012-11-20 12:04:40

I uploaded a new version of the patch - let's see what the patchbot says.

`@`Fred: when you start reviewing the patch, please don't try to understand what happens in `sage/rings/universal_cyclotomic_field/universal_cyclotomic_field_c.pyx`. All actual arithmetic is done there, but very low-level (and I was - and still am - not at all an expert in implementing in cython). I hope it is convincing if the front end behaves as you expect and want it to behave, and is fairly quick.


---

Comment by stumpc5 created at 2012-11-20 12:08:10

Replying to [comment:107 stumpc5]:
> I uploaded a new version of the patch - let's see what the patchbot says.

I don't quite understand what it is complaining about; some files that get rejected are not even contained in the patch. Any ideas what I do wrong?


---

Comment by SimonKing created at 2012-11-20 12:24:59

Really strange. For the record: The patchbot says

```
applying trac_8327_universal_cyclotomic_field-cs.patch
patching file doc/en/reference/categories.rst
Hunk #1 FAILED at 9
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/categories.rst.rej
patching file doc/en/reference/rings_numerical.rst
Hunk #1 FAILED at 26
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/rings_numerical.rst.rej
patching file sage/categories/fields.py
```

but if you search the string ".rst" in attachment:trac_8327_universal_cyclotomic_field-cs.patch, you only find that `doc/en/reference/rings_standard.rst` is touched.


---

Comment by chapoton created at 2012-11-20 14:30:53

well, looks like a strange problem in the building of the doc. Maybe one could try a patch which does not touch the doc at all, just to see.


---

Comment by stumpc5 created at 2012-11-21 08:47:19

Replying to [comment:110 chapoton]:
> well, looks like a strange problem in the building of the doc. Maybe one could try a patch which does not touch the doc at all, just to see.

I now divides the patch in three parts, only the last touching the documentation...


---

Comment by stumpc5 created at 2012-11-21 09:11:58

Replying to [comment:111 stumpc5]:
> Replying to [comment:110 chapoton]:
> > well, looks like a strange problem in the building of the doc. Maybe one could try a patch which does not touch the doc at all, just to see.
> 
> I now divides the patch in three parts, only the last touching the documentation...

Okay, it seems to work now -- I will take care now of the startup modules and the trailing whitespaces. Getting the coverage and no test failures will take a little longer (due to nasty cython functions that I can only test indirectly).


---

Comment by stumpc5 created at 2012-11-21 14:38:23

Replying to [comment:112 stumpc5]:

> it seems to work now

The patch is finally ready for review. The only issue with the patchbot is currently that I do load the module at startup - which is what I'd prefer (as long as no one else has a better idea of how to handle it).

Beside that, I added 100% coverage everywhere, and excluded 4 very small side tickets to be reviewed directly.

Cheers, Christian


---

Comment by chapoton created at 2012-11-21 16:52:06

let me start with a few simple remarks

- why are we changing the import of hecke_modules in this patch ?

- the doc of prime_subfield has a mistake : ZZ should be QQ

- in from_dict, only one parameter is documented

- the docs of _eq_ and _ne_ are strange, and look like a copy and paste

- is_unit should be removed, as already implemented in the class of Field elements

- it would be worth adding some of the methods of QQbar elements : minpoly and abs maybe

- maybe consider a coercion of real elements to the field AA ?

- somewhere near the beginning of the doc, it should be explained the following important points

  1 the field UCF is contained in the complex field
  
  2 how to coerce z to QQbar : QQbar(z)

  3 how to coerce z to the minimal cyclotomic field containing it : z.to_cyclotomic_field()

That's all for today.


---

Comment by stumpc5 created at 2012-11-21 19:11:31

Replying to [comment:115 chapoton]:

Thanks for your first look!

- I deleted the two later dependencies, since they are not really necessary (I only needed them at some point to work with the universal cyclotomics).

- I took your remarks into account:

> - why are we changing the import of hecke_modules in this patch ?

because the import of hecke_modules and of universal_cyclotomic_field causes an import loop. Since we want to use `UCF`, it was easier and cleaner to lazily import hecke_modules.

> - is_unit should be removed, as already implemented in the class of Field elements

the inherited `is_unit` method is not capturing the situation. It's implementation is

```
    def is_unit(self):
        if self == 1 or self == -1:
            return True
        raise NotImplementedError
```


> - it would be worth adding some of the methods of QQbar elements : minpoly and abs maybe

not yet done!

> - maybe consider a coercion of real elements to the field AA ?

This is impossible, isn't it? Here is a quote from the documentation:

"Another consequence of the consistency condition is that coercions can only go from exact rings (e.g., the rationals QQ) to inexact rings (e.g., real numbers with a fixed precision RR), but not the other way around."

Or am I misunderstanding something?

>   1 the field UCF is contained in the complex field

This coercion is going through QQbar, so I only documented the later.

Best, Christian


---

Comment by chapoton created at 2012-11-21 20:02:54

> > - is_unit should be removed, as already implemented in the class of Field elements
> 
> the inherited `is_unit` method is not capturing the situation. It's implementation is
> {{{
>     def is_unit(self):
>         if self == 1 or self == -1:
>             return True
>         raise NotImplementedError
> }}}

I do not understand : if one look at Ticket #13728, the method is_unit does check that an element is not zero ! 
 
> > - maybe consider a coercion of real elements to the field AA ?
> 
> This is impossible, isn't it? Here is a quote from the documentation:
> 
> "Another consequence of the consistency condition is that coercions can only go from exact rings (e.g., the rationals QQ) to inexact rings (e.g., real numbers with a fixed precision RR), but not the other way around."
> 
> Or am I misunderstanding something?

Well, I do not know. The point is that we can currently use QQbar(z) for z in UCF. I wonder wether one could do AA(z) for z in UCF and real, because AA is just the set of real elements of QQbar. But maybe I do not understand something..


```
sage: toto=E(6)
sage: QQbar(toto)
0.500000000000000? + 0.866025403784439?*I
sage: riri=QQbar(toto)
sage: riri in AA
False
sage: riri+riri.conjugate() in AA
True
sage: QQbar(toto+toto.conjugate()) in AA
True
sage: AA(riri+riri.conjugate()).parent()
Algebraic Real Field
```



> >   1 the field UCF is contained in the complex field
> 
> This coercion is going through QQbar, so I only documented the later.

Yes, But I rather meant the mathematical point : the field is defined as an embedded field, not as an abstract field..


---

Comment by stumpc5 created at 2012-11-21 20:27:12

Replying to [comment:117 chapoton]:

> I do not understand : if one look at Ticket #13728, the method is_unit does check that an element is not zero ! 

That's right, but even though UCF knows that it is a field, its elements do not know that they are field elements. Do you happen to know how to solve that?

> Well, I do not know. The point is that we can currently use QQbar(z) for z in UCF. I wonder wether one could do AA(z) for z in UCF and real, because AA is just the set of real elements of QQbar. But maybe I do not understand something..

(I thought you meant the other way round...) It was easy to implement the conversion to QQ and ZZ, and to set the coercion to QQbar. But I don't quite know how to do conversion to AA.

```
sage: AA(QQbar(E(5) + E(5)^4))  
0.618033988749895?
```

works, but one currently has to pass through QQbar.

> Yes, But I rather meant the mathematical point : the field is defined as an embedded field, not as an abstract field..

Okay, I will add a sentence in the beginning.


---

Comment by nthiery created at 2012-11-21 21:56:11

Thanks so much Frédéric for taking over the review! (and in general for all your reviewing work!)

As a general comment: we have been discussing the overall design with Christian quite some and it looked good. So you can focus on the details.


---

Comment by stumpc5 created at 2012-11-22 08:58:10

Replying to [comment:115 chapoton]:

> - it would be worth adding some of the methods of QQbar elements : minpoly and abs maybe

I added implementations of those, and I also improved the documentation here and there a bit.


---

Comment by chapoton created at 2012-11-22 20:41:34

A few more comments

* this import is apparently not used :

from sage.rings.complex_field import ComplexField 

* the sort of elements is backwards compared to the order for cyclotomic fields

```
sage: v=UCF.random_element(7);v
-5*E(7) - 4*E(7)^3 + 4*E(7)^4 + E(7)^5
sage: v.to_cyclotomic_field()
zeta7^5 + 4*zeta7^4 - 4*zeta7^3 - 5*zeta7
```

maybe it would be better to go the same way ? but maybe this is the same as gap ?

* Is the is_subring method necessary ? it is almost empty !

* in the element constructor, maybe one could answer by something like

"no coercion found for elements of XXX"

with XXX the parent of the argument ? It would be more informative, no ?

* maybe zumbroich_basis should be called zumbroich_basis_indices ? I would expect that something called zumbroich_basis would return elements of the field, which is not really the case. Well, this is not that important..

* why is the hash function test tagged with random ? does it depend on the computer or something like that ?

* in _invert_, one should rather raise a ZeroDivisionError when trying to invert 0 ?

* more generally, maybe one could try to avoid using assert, and better raise precise Exceptions ?

* I have not read seriously the cython part, but found a typo :

inverse for the univeral

That's all for today


---

Comment by stumpc5 created at 2012-11-23 08:16:35

Replying to [comment:121 chapoton]:
> A few more comments

Thanks a lot!

> * the sort of elements is backwards compared to the order for cyclotomic fields
> maybe it would be better to go the same way ? but maybe this is the same as gap ?

I used the same order as gap (the increasing ordering on the exponents). I think I would prefer this ordering...

> * Is the is_subring method necessary ? it is almost empty !

I don't quite remember where but I needed this (indeed trivially implemented) method at some point to not catch an error. Maybe it was when working with matrices over UCF?

> "no coercion found for elements of XXX"

done, I had to distinguish between objects having a parent and those not having one.

> * maybe zumbroich_basis should be called zumbroich_basis_indices ? I would expect that something called zumbroich_basis would return elements of the field, which is not really the case. Well, this is not that important..

done

> * why is the hash function test tagged with random ? does it depend on the computer or something like that ?

If I am not mistaken, the hash is only unique in a given Sage session.

> * in _invert_, one should rather raise a ZeroDivisionError when trying to invert 0 ?
> * more generally, maybe one could try to avoid using assert, and better raise precise Exceptions ?

good point, done!

Best, Christian


---

Comment by nthiery created at 2012-11-23 08:40:16

Replying to [comment:122 stumpc5]:
> > * why is the hash function test tagged with random ? does it depend on the computer or something like that ?
> 
> If I am not mistaken, the hash is only unique in a given Sage session.

It is not required that the hash value of an object be unique across
Sage session. However the implementation usually guarantees this,
which is a good feature. In fact, most of the time in Sage, the hash
value only depends on the architecture (32bits/64bits) and when this
is the case, it is good to test it explicitly in order to get noticed
in case the hash value would change for some reason (which could be a
bug or a long distance consequence of something else), as in:

            sage: e = RootSystem(['A',2]).ambient_space()
            sage: hash(e.simple_root(0))
            -4601450286177489034          # 64-bit
            549810038                     # 32-bit 

Cheers,
					Nicolas


---

Comment by nthiery created at 2012-11-23 08:44:55

Replying to [comment:121 chapoton]:
> * more generally, maybe one could try to avoid using assert, and better raise precise Exceptions ?

Just a side note: as discussed on sage-combinat-devel, assertions are
preferable in the following situations:

- For checking the internal state of the program
- When the caller should *not* catch the exception
- In time critical locations

Beside, nothing prevents from writing a meaningful message in an
assertion check.

Cheers,
                      Nicolas


---

Comment by stumpc5 created at 2012-11-23 08:48:28

Replying to [comment:123 nthiery]:
> Replying to [comment:122 stumpc5]:
> > > * why is the hash function test tagged with random ? does it depend on the computer or something like that ?
> > 
> > If I am not mistaken, the hash is only unique in a given Sage session.
> 
> It is not required that the hash value of an object be unique across
> Sage session. However the implementation usually guarantees this,
> which is a good feature. In fact, most of the time in Sage, the hash
> value only depends on the architecture (32bits/64bits) and when this
> is the case, it is good to test it explicitly in order to get noticed
> in case the hash value would change for some reason

Thanks for the clarification!

Do you also happen to know how to handle the real conversion as in `AA(QQbar(E(5) + E(5)^4))` in comment:118 ?


---

Comment by nthiery created at 2012-11-23 09:41:09

Replying to [comment:125 stumpc5]:
> Replying to [comment:123 nthiery]:
> > Replying to [comment:122 stumpc5]:
> > > > * why is the hash function test tagged with random ? does it depend on the computer or something like that ?
> > > 
> > > If I am not mistaken, the hash is only unique in a given Sage session.
> > 
> > It is not required that the hash value of an object be unique across
> > Sage session. However the implementation usually guarantees this,
> > which is a good feature. In fact, most of the time in Sage, the hash
> > value only depends on the architecture (32bits/64bits) and when this
> > is the case, it is good to test it explicitly in order to get noticed
> > in case the hash value would change for some reason
> 
> Thanks for the clarification!
> 
> Do you also happen to know how to handle the real conversion as in `AA(QQbar(E(5) + E(5)^4))` in comment:118 ?

Did you try implementing the (partial) morphism from UCF to AA (using SetMorphism and the category of SetsWithPartialMaps), and register it as a conversion?

If yes, this could possibly be done during the initialization of UCF.


---

Comment by stumpc5 created at 2012-11-23 10:06:11

Replying to [comment:126 nthiery]:

> Did you try implementing the (partial) morphism from UCF to AA (using SetMorphism and the category of SetsWithPartialMaps), and register it as a conversion?

Good call, it works now! Thanks!

Btw: It would be nice to include this in the documentation, if not already done. At least if I google for `"sage SetMorphism SetsWithPartialMaps"`, I only get the file `root_space.py` which is perfectly fine to explain how to do it, but I only found it after you telling me what to look for.


---

Comment by stumpc5 created at 2012-11-23 10:18:05

Replying to [comment:127 stumpc5]:

> Replying to [comment:126 nthiery] :

> Good call, it works now! Thanks!

One more thing: do you also know how to do the same for the cyclotomic fields ? What I would need is something like


```
        SetMorphism(
                Hom(self, CyclotomicField(n), SetsWithPartialMaps()),
                lambda elem: elem.to_cyclotomic_field()
            ).register_as_conversion()
```


The problem is that the parameter `n` is not determined a priori, and I want the conversion to exist for any `n`.


---

Comment by chapoton created at 2012-11-23 10:21:42

two minor suggestions :

* I would write "smallest subfield of the complex field" instead of "smallest subfield of the complex plane"

* I think one should explain somewhere at the beginning of the doc of E that the constant exp(1) can be found as the lowercase letter 'e'

This is great that you managed to coerce to AA !


---

Comment by nthiery created at 2012-11-23 10:23:47

I am glad that it worked out!


> Btw: It would be nice to include this in the documentation, if not already done. At least if I google for `"sage SetMorphism SetsWithPartialMaps"`, I only get the file `root_space.py` which is perfectly fine to explain how to do it, but I only found it after you telling me what to look for.

Indeed! A good spot might be Simon's tutorial worksheet on coercion:

https://groups.google.com/forum/#!topic/sage-devel/CJEUEghnQx8

Simon?


---

Comment by nthiery created at 2012-11-23 10:26:17

Replying to [comment:128 stumpc5]:
> One more thing: do you also know how to do the same for the cyclotomic fields ? What I would need is something like
> 
> {{{
>         SetMorphism(
>                 Hom(self, CyclotomicField(n), SetsWithPartialMaps()),
>                 lambda elem: elem.to_cyclotomic_field()
>             ).register_as_conversion()
> }}}
> 
> The problem is that the parameter `n` is not determined a priori, and I want the conversion to exist for any `n`.

There is no perfect support for this. But I guess you could change the initializtion of CyclotomicField so that, when the n-th Cyclotomic field F is constructed, the partial conversion UCF->F is constructed and registered as a conversion (and possibly the reverse coercion as well).


---

Comment by stumpc5 created at 2012-11-23 14:18:12

Hi --

I think we are now some big steps forward!

- I took care of everything Fred was asking for, in particular the partial conversion to `AA`.

and

- I implemented conversion to the cyclotomic field ! There is still an issue left, which I cannot take care off. Namely, the embedding of the cyclotomic field into the complex numbers can be given in the constructor. But I didn't find a way to capture this embedding to send an element of the universal cyclotomics into the cyclotomic field AND preserve the embedding.

Ready for another review!

Best, Christian


---

Comment by chapoton created at 2012-11-23 14:32:22

Hum, the patch has become so much bigger, and the html preview does no longer work. It seems that you are now touching many more files. This will make my work much more difficult. There seem to be a huge number of whitespace-removal, which is a bit perturbing. I am not happy with this latest version, indeed..


---

Comment by nthiery created at 2012-11-23 14:34:08

Replying to [comment:132 stumpc5]:
> Hi --
> 
> I think we are now some big steps forward!
> 
> - I took care of everything Fred was asking for, in particular the partial conversion to `AA`.
> 
> and
> 
> - I implemented conversion to the cyclotomic field ! There is still an issue left, which I cannot take care off. Namely, the embedding of the cyclotomic field into the complex numbers can be given in the constructor. But I didn't find a way to capture this embedding to send an element of the universal cyclotomics into the cyclotomic field AND preserve the embedding.

Cool!

I guess it's fair if you only provide conversions to-from those cyclotomic field that use the default embedding.


---

Comment by stumpc5 created at 2012-11-23 14:45:01

Replying to [comment:133 chapoton]:
> Hum, the patch has become so much bigger, and the html preview does no longer work. It seems that you are now touching many more files. This will make my work much more difficult. There seem to be a huge number of whitespace-removal, which is a bit perturbing. I am not happy with this latest version, indeed..
> 

I do agree, I didn't check that carefully. All I did was to add a 5 line method to `rings/number_field/number_field.py` that does the conversion from UCF to CF.

In order to not get trailing white space errors, I removed them all (and this did in the end modify the complete file, unfortunately). Should I just leave the white spaces in order to keep the readability of the patch?


---

Comment by chapoton created at 2012-11-23 14:48:52

yes, please try to make a cleaner/shorter patch. I think it is good to never introduce new trailing whitespaces, but bad to remove them everywhere else in the files you touch, as this makes ugly patches. Maybe you can without much work restart from an untouched file rings/number_field/number_field.py ?


---

Comment by stumpc5 created at 2012-11-23 14:58:48

Replying to [comment:136 chapoton]:
> yes, please try to make a cleaner/shorter patch. I think it is good to never introduce new trailing whitespaces, but bad to remove them everywhere else in the files you touch, as this makes ugly patches. Maybe you can without much work restart from an untouched file rings/number_field/number_field.py ?

Do you accept it now as only a little change (which I actually consider a bit improvement), see my changes in `number_field.py` ?


---

Comment by chapoton created at 2012-11-23 15:04:43

yes, much better. 

* there is still the typo "the univeral cyclotomic"


---

Comment by stumpc5 created at 2012-11-23 15:08:17

Replying to [comment:138 chapoton]:
> yes, much better. 
> 
> * there is still the typo "the univeral cyclotomic"

Oh, I wasn't seeing this typo when you pointed at it in your comment. So I thought you were disliking the wordings, which I then changed.

It's fixed now and will be in the next version of the patch as soon as I have more things to change.


---

Comment by stumpc5 created at 2012-11-23 16:05:34

Replying to [comment:139 stumpc5]:
> Replying to [comment:138 chapoton]:

> It's fixed now and will be in the next version of the patch as soon as I have more things to change.

Okay, done -- I fixed this and added more documentation on getting to the cyclotomics.


---

Comment by chapoton created at 2012-11-23 16:25:15

Well, I think I do not have much more to say. I have not yet tested the new conversions, but I am confident that they work and will try them soon.

I think we can leave further improvements for later tickets. I have noted an error occuring when doing FractionField(PolynomialRing(UCF,'x')), which may need investigation. There is also the annoying fact that the elements do not know that they belong to a field. Given that the ticket has been waiting for a long time, I propose to postpone these minor questions to later tickets.

If the bot gives a green light, except for the startup module, I will give a positive review. This may have to wait for one week, as I am traveling next week.

One last thing : the following lines have to be modified, as this has been implemented :

  .. TODO::            modify CyclotomicField to add a (partial) conversion from UCF


---

Comment by stumpc5 created at 2012-11-23 16:46:46

Replying to [comment:141 chapoton]:

Thanks a lot for doing the final review!

I don't see how my patch might have influenced the doc failure on `sage/schemes/elliptic_curves/ell_number_field.py`, its tests pass on my machine (in roughly 45 sec, independent of my patch being applied or not).


---

Comment by chapoton created at 2012-11-24 15:33:18

Well, I do indeed have this failing test :

sage -t -force_lib "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
Segmentation fault (core dumped)

with the patch applied, and it disappears when the patch is removed.

So I guess there *is* a problem somewhere..


---

Comment by chapoton created at 2012-11-24 15:53:24

I suspect (without a really good reason) that the choice of the letter E, which is a traditional name for elliptic curves, may be involved.. By the way, is it reasonable to use a single letter ? I myself do not like the fact that the letter R stands for something I do not care about.. Maybe one could ask the question on sage-devel : can we use the name E for the generators of the universal cyclotomic field ?


---

Comment by nthiery created at 2012-11-24 18:54:20

Replying to [comment:144 chapoton]:
> I suspect (without a really good reason) that the choice of the letter E, which is a traditional name for elliptic curves, may be involved.. 

Possibly, if E occurs explicitly in the doctest. Otherwise it should not interfer, as it is only imported by default in the intepreter and not in the sage sources. An alternative possibility is that some coercion involving cyclotomic fields now goes through UCF and causes trouble. You could rerun the failing tests with all the UCF coercions disabled.

> By the way, is it reasonable to use a single letter ? I myself do not like the fact that the letter R stands for something I do not care about.. Maybe one could ask the question on sage-devel : can we use the name E for the generators of the universal cyclotomic field ?

That's a good point. The average Sage user is indeed different from the average GAP user. An alternative would be to use UCF.E, and to implement:

```
    sage: UCF.inject_shorthands()
    sage: E(3)
```

(as for symmetric functions)


---

Comment by stumpc5 created at 2012-11-25 18:53:16

Replying to [comment:143 chapoton]:
> sage -t -force_lib "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
> Segmentation fault (core dumped)
> 
> with the patch applied, and it disappears when the patch is removed.

I just rechecked on my machine, and I get `All tests passed!` in both cases. So, what might be the difference between Frédérics and my machine? I am running 5.5.rc0 on a 64bit Linux machine.

I forwarded the question on the point of entry to the sage-devel mailing list, see https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/rJ6Y_-a__d8.


---

Comment by stumpc5 created at 2012-11-27 13:59:35

Replying to [comment:146 stumpc5]:
> I forwarded the question on the point of entry to the sage-devel mailing list, see https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/rJ6Y_-a__d8.

I updated the patch according to changes discussed at sage-devel. The only thing missing is to decide how to handle possible embeddings.


---

Comment by stumpc5 created at 2012-11-30 09:44:20

The patchbot gives a green light (for the very first time!), and the ticket is again for review. I did quite some changes since Frédéric looked at it, which were requested in the discussion on sage-devel. It would be nice if someone else would look at the changes as well!

Thanks, Christian


---

Comment by nbruin created at 2012-11-30 22:15:21

It looks like you have a memory leak in `cached_lcm`: that cache never gets cleared out. Can you argue that it will only be called with a limited variety of arguments so that you know the cache won't grow indefinitely?

Also, you should cache by set, not by tuple, since lcm isn't dependent on order or multiplicity. That can already save you a factor _n_! of memory.

(but really, unless you can argue the argument set here is going to be very limited, I don't think you can afford to build this cache)


---

Comment by robertwb created at 2012-12-01 05:28:44

Lots of good code here!

Some comments:

* Why is get_parent_of_embedding in the pyx file when it's only used in the py file?

* No need to lazily import universal_cyclotomic_field_c, it's already behind another lazy import.

* CyclotomicField._coerce_map_from_ # TODO: use the embedding of other properly: you could use the method introduced in #13765, but if you don't want to do that then at least check it has the "standard" embedding sending the generator to the primitive root of unity CC or return None rather than silently producing wrong answers.

* Shouldn't _coerce_map_from_ accept QQ?

* Does "endowed with the Zumbroich basis" need to be part of the printed name? Also, what about a nice _latex_ representation?

* Using `<>` for != is deprecated, and I think goes away in python 3.

* Any reason not to inherit from Field?

* The `if bracket == ...` list might be better done with a dictionary mapping left to right, with a good exception on KeyError. Even better, IMHO, is to accept any even-character string (so one would pass "" or "[]" or "<<>>" or whatever one wanted). 

* `_gap_init = _repr_`  Not now that we've allowed different printing options.

* `__hash__` will fail on a 32-bit machine. Instead, test making a dict with UCF items then retrieving one.

* is ZumbroichBasisIndices really a Parent?

* I agree with nbruin, there's a lot of caching going on that never gets freed. I would suggest having capped size caches, if you determine that you really need them. (Also, for CyclotomicFieldCached, better to fix this to make CyclotomicField faster, possibly using a weakref cache or one of the unique parent factories.)


---

Comment by SimonKing created at 2012-12-01 08:07:30

Replying to [comment:151 robertwb]:
> * ... (Also, for CyclotomicFieldCached, better to fix this to make CyclotomicField faster, possibly using a weakref cache or one of the unique parent factories.)

Small remark: `UniqueRepresentation` currently uses a permanent cache, but will hopefully use a weak cache at some point in the future - see #12215. I think the `UniqueFactory` already has a weak cache - but please verify.


---

Comment by nthiery created at 2012-12-01 12:57:22

Hi Robert,

Replying to [comment:151 robertwb]:
> * Any reason not to inherit from Field?

I told him to :-)

We want to move away from the static class hierarchy (Monoid, Field,
...) when there is not a strong compelling reason to use it (i.e. it
makes a difference speed wise, e.g. for element arithmetic), since
that duplicates the far more flexible category hierarchy.

Cheers,
                                 Nicolas


---

Comment by robertwb created at 2012-12-01 18:07:09

Replying to [comment:153 nthiery]:
> 	Hi Robert,
> 
> Replying to [comment:151 robertwb]:
> > * Any reason not to inherit from Field?
> 
> I told him to :-)
> 
> We want to move away from the static class hierarchy (Monoid, Field,
> ...) when there is not a strong compelling reason to use it (i.e. it
> makes a difference speed wise, e.g. for element arithmetic), since
> that duplicates the far more flexible category hierarchy.

+1 to this. Then why is is_Field not obtained by default?  I think there's performance benefit in moving to Ring at least, for multiplication (but I'd have to check that this is still the case).


---

Comment by stumpc5 created at 2012-12-02 19:47:15

Thanks for your comments!

Replying to [comment:150 nbruin]:
> (but really, unless you can argue the argument set here is going to be very limited, I don't think you can afford to build this cache)

I removed this cache (and also some of the others)

Replying to [comment:151 robertwb]:
> Lots of good code here!

some positive words are always appreciated, thanks!

> * Why is get_parent_of_embedding in the pyx file when it's only used in the py file?

done

> * No need to lazily import universal_cyclotomic_field_c, it's already behind another lazy import.

done

> * CyclotomicField._coerce_map_from_ # TODO: use the embedding of other properly: you could use the method introduced in #13765, but if you don't want to do that then at least check it has the "standard" embedding sending the generator to the primitive root of unity CC or return None rather than silently producing wrong answers.

What I now do is to take embeddings of CyclotomicFields into account, but do not coerce if the UCF doesn't have the standard embedding. Please recheck that it does what it properly...

> * Shouldn't _coerce_map_from_ accept QQ?

This is captured in `_from_base_ring`.

> * Does "endowed with the Zumbroich basis" need to be part of the printed name?

removed.

> Also, what about a nice _latex_ representation?

still open.

> * Using `<>` for != is deprecated, and I think goes away in python 3.

done.

> * Any reason not to inherit from Field?

I now do inherit from Field and from FieldElement. This way, I got rid of several almost empty methods. If Nicolas prefers to have it again the other way round, we can as well undo that.

> * The `if bracket == ...` list might be better done with a dictionary mapping left to right, with a good exception on KeyError. Even better, IMHO, is to accept any even-character string (so one would pass "" or "[]" or "<<>>" or whatever one wanted). 

done.

> * `_gap_init = _repr_`  Not now that we've allowed different printing options.

done.

> * `__hash__` will fail on a 32-bit machine. Instead, test making a dict with UCF items then retrieving one.

still open.

> * is ZumbroichBasisIndices really a Parent?

I am not the specialist here, so feel free to modify this. Now, ZBI is a parent, and the tuples `(n,k)` are indeed elements thereof.

> * I agree with nbruin, there's a lot of caching going on that never gets freed. I would suggest having capped size caches, if you determine that you really need them. (Also, for CyclotomicFieldCached, better to fix this to make CyclotomicField faster, possibly using a weakref cache or one of the unique parent factories.)

done.

Best, Christian


---

Comment by nthiery created at 2012-12-02 20:23:41

Replying to [comment:156 stumpc5]:
> I now do inherit from Field and from FieldElement. This way, I got rid of several almost empty methods. If Nicolas prefers to have it again the other way round, we can as well undo that.

It would be best to move those almost empty methods to the Fields
category. That being said, I totally understand if you prefer to get
done with this patch without risking conflicts with ongoing category
development. Can you just leave a quick note in the code like:


```
    .. TODO::

       Remove the inheritance from Field and FieldElement as soon as
       the methods X,Y,Z are implemented in the Fields category.
```


Ideally you would also make a quick benchmark to check my guess that
inheriting from FieldElement does not make a speed difference.

Thanks!

                               Nicolas


---

Comment by stumpc5 created at 2012-12-03 16:42:58

> * Does "endowed with the Zumbroich basis" need to be part of the printed name? Also, what about a nice _latex_ representation?

This is actually taken care of in #13734

> `__hash__` will fail on a 32-bit machine. Instead, test making a dict with UCF items then retrieving one.

??? What do you want me to do here? Are you talking about the hash for the parent of the elements?


---

Comment by nbruin created at 2012-12-03 17:13:06

Replying to [comment:158 stumpc5]:
> ??? What do you want me to do here? Are you talking about the hash for the parent of the elements?
I only found hashes for elements in your patch. Hash values are supposed to be machine-length integers associated to an object, consistent within one session, equal for objects that compare as equal (and preferably not equal to much else) [sage has to violate this due to equality being too lax and not transitive in the presence of coercion] and very little structure otherwise. In particular, the actual numerical values returned don't matter. It's better to check the properties that actually matter than particular values that are produced (which should be dependent on 32/64 bits because otherwise you're creating unnecessarily weak hashes on 64 bit)

Don't test the actual value returned by hash, but test its functionality. Something like (do we have some example that exercises hashes appropriately?):

```
sage: a = ...
sage: b = ...
sage: c = ...
sage: V = set([a,b])
sage: <definition for a> in V
true
sage: b in V
true
sage: c in V
false
```

and perhaps test your hash function is not the constant function and has a reasonable distribution:

```
sage: L = [<object> for i in [1..100]]
sage: set(hash(x) for x in L).len() >= 98
true
```

You did mark the tests as `64 bit` which may or may not elicit the right action from the doctesting framework, but it would be way better if your test actually did work (and did test) on 32 bit as well, which you can do by testing functionality, not value.


---

Comment by stumpc5 created at 2012-12-03 18:25:19

Replying to [comment:159 nbruin]:
> Replying to [comment:158 stumpc5]:

Thanks for the clarification!

> I only found hashes for elements in your patch.

Right, but there is a `__hash__` function returning the id, that's why I wasn't quite sure... I now do test the hash by functionality, do you think it's better now?

Btw: As with the hash for elements in the CyclotomicField, it does not depend on the embedding of the parent. Do you think this might cause problems?

Finally, some functionalities become slower (e.g. matrix multiplication where addition or multiplication of UCF elements are done multiple times). Do you think, it is appropriate to cache (in the parent) the multipliciation or addition in UCF.Elements ?


---

Comment by nbruin created at 2012-12-03 18:56:38

Replying to [comment:160 stumpc5]:
> Right, but there is a `__hash__` function returning the id, that's why I wasn't quite sure... I now do test the hash by functionality, do you think it's better now?

I guess for parents that would be OK, because they are unique. Otherwise, most elements in sage can be equal to non-identical elements, so `id` doesn't make for a valid hash on them. Using `id` as a hash isn't consistent across sessions and won't survive pickling, but I'd hope that's OK.

> Btw: As with the hash for elements in the CyclotomicField, it does not depend on the embedding of the parent. Do you think this might cause problems?

No. The constant function would make a valid hash function. It would just lead to horrible performance on dictionaries and sets.

> Finally, some functionalities become slower (e.g. matrix multiplication where addition or multiplication of UCF elements are done multiple times). Do you think, it is appropriate to cache (in the parent) the multipliciation or addition in UCF.Elements ?

??? I hope you're not proposing caching by essentially building up addition and multiplication tables. That'll be horrible on memory and rarely result in speedup.

I'd say this is all optimization. First you want to have the functionality in (that'll already be great!). Once you have a stable platform, you can test where the bottlenecks are and optimize those, if required (with a minimum of caching).


---

Comment by nthiery created at 2012-12-03 20:31:26

Replying to [comment:159 nbruin]:
> Don't test the actual value returned by hash, but test its functionality. Something like (do we have some example that exercises hashes appropriately?):
> {{{
> sage: a = ...
> sage: b = ...
> sage: c = ...
> sage: V = set([a,b])
> sage: <definition for a> in V
> true
> sage: b in V
> true
> sage: c in V
> false
> }}}
> and perhaps test your hash function is not the constant function and has a reasonable distribution:
> {{{
> sage: L = [<object> for i in [1..100]]
> sage: set(hash(x) for x in L).len() >= 98
> true
> }}}

Just a remark: those would make good candidates for a generic _test_hash method for parents.


---

Comment by nthiery created at 2012-12-03 20:33:41

Replying to [comment:160 stumpc5]:

> > I only found hashes for elements in your patch.
> 
> Right, but there is a `__hash__` function returning the id, that's why I wasn't quite sure... I now do test the hash by functionality, do you think it's better now?

That hash function for the parent, you inherit from UniqueRepresentation, right? In that case, there is no real need to retest it here.

Cheers,
                    Nicolas


---

Comment by nbruin created at 2012-12-03 20:54:25

Hi Christian,

Sorry that your code review is devolving into a kind of "how to vet newly introduced parents" experiment. Please don't take it personally! I think we're still getting useful contributions to Sage at large from this for now, though.

For doing good (generic) tests for how hash performs:

```
sage: any( E(n) in L for n in [1001..2000] ) 
False
```

This test doesn't really test the non-constantness of hashes. This code would still work if `hash(E(n))==0` would hold for all `n`. After equality of hash value, `in` will still fall back on `__eq__`, with one exception: identical objects will be found with `in`:

```
sage: n = float(NaN)
sage: n == n
False
sage: n in set([n])
True
sage: m = float(NaN)
sage: m in set([n])
False
```

It's an optimization that is necessary for python to have reasonable performance that leads to nasty consequences for objects that are not equal to themselves (which is really an odd edgecase anyway)


---

Comment by stumpc5 created at 2012-12-03 21:04:27

Replying to [comment:164 nbruin]:
> {{{
> sage: any( E(n) in L for n in [1001..2000] ) 
> False
> }}}

Thanks, I deleted it...


---

Comment by chapoton created at 2012-12-05 13:39:50

Hello Christian,

in the file number_field.py, the documentation of the parameter bracket is wrong : you say

Can be ``None``, ``"("``, or ``"["``, with 

this is not consistent with the documentation in UCF, where it is an even-length chain

Do you think there are still important problems that need to be solved ? Maybe some caching questions ? And of course the patchbot is not happy with latest version.

Fred


---

Comment by stumpc5 created at 2012-12-05 13:44:02

Replying to [comment:166 chapoton]:

Hi Fred,

> Can be ``None``, ``"("``, or ``"["``, with 
> this is not consistent with the documentation in UCF, where it is an even-length chain

Thanks for pointing this out!

> Do you think there are still important problems that need to be solved ?

I fixed everything people were complaining about (or, to say it differently, where they saw possible improvements). I don't know if someone is still not happy with the current state...

> Maybe some caching questions ? And of course the patchbot is not happy with latest version.

This is just a patchbot issue, I hope -- it says that 0 tests failed in several files.

I will update and upload the patch,

Christian


---

Comment by SimonKing created at 2012-12-05 14:21:28

Replying to [comment:167 stumpc5]:
> This is just a patchbot issue, I hope -- it says that 0 tests failed in several files.

That could be a severe and difficult-to-debug problem. On a different ticket, I also had "0 tests failed", and the problem was that Sage crashed while quitting: No test broke, but the test _framework_ broke. It would make sense to repeat the failing tests, both "normally" and in verbose mode, and on different platforms.


---

Comment by nbruin created at 2012-12-07 20:31:21

Replying to [comment:167 stumpc5]:
> This is just a patchbot issue, I hope -- it says that 0 tests failed in several files.

In those cases, don't just look at the summary at the bottom.
There is a bit more info in the log file (use text search on the file name to find the relevant locations. The errors that arise are of the form:

```
  File "/mnt/storage2TB/patchbot/Sage/sage-5.5.rc0/local/lib/python/site-packages/sage/rings/all.py", line 169, in <module>
    lazy_import("sage.rings.universal_cyclotomic_field.all","*")
  File "lazy_import.pyx", line 850, in sage.misc.lazy_import.lazy_import (sage/misc/lazy_import.c:5168)
  File "lazy_import.pyx", line 900, in sage.misc.lazy_import.get_star_imports (sage/misc/lazy_import.c:5924)
EOFError
```

so apparently the lazy import fails for some reason. If it's a real issue, perhaps it's due to the order in which the lazy imports get triggered? Otherwise it might just be a temporary issue with that particular patchbot.


---

Comment by stumpc5 created at 2012-12-08 13:31:19

Replying to [comment:169 nbruin]:
> so apparently the lazy import fails for some reason. If it's a real issue, perhaps it's due to the order in which the lazy imports get triggered? Otherwise it might just be a temporary issue with that particular patchbot.

And am I able to figure out if this is an issue which I can solve?


---

Comment by nbruin created at 2012-12-09 17:48:25

Replying to [comment:170 stumpc5]:
> And am I able to figure out if this is an issue which I can solve?
Well, given that you can't reproduce the errors (you have tried?) and that the patchbot reports errors in different tests each time, I'd assume a problem with the bot, unless evidence otherwise is supplied. Random `EOFError`s smell more like an I/O problem than an issue with the code.


---

Comment by stumpc5 created at 2012-12-10 08:28:20

Replying to [comment:171 nbruin]:
> Replying to [comment:170 stumpc5]:
> > And am I able to figure out if this is an issue which I can solve?
> Well, given that you can't reproduce the errors (you have tried?)

Sorry for still being (maybe too) ignorant concerning these things: can I do anything other than starting sage and running the doctests?


---

Comment by chapoton created at 2012-12-11 20:58:39

What a boring problem, we are so close to finishing this patch ! And there is apparently only one patchbot around ! Nicolas, would it be possible to have a patchbot running for the combinat patches on one server somewhere ?

Some stupid ideas :

* Maybe you could try to put back dependencies to #13727 and #13728 ? probably not a good idea, as they now also fail..

* try to trigger another run of the bot. I do not know how to do that. A priori, just asking by the following line is not enough.

apply trac_8327-universal_cyclotomic_field-cs.patch


---

Comment by nbruin created at 2012-12-11 21:52:06

You can "kick" the patchbot by putting `?kick` after the URL of the ticket page at the patchbot. This has already happened and the errors keep shifting (look at the last couple of reports).

I suspect it's due to the lazy import (that's where the error occurs). I have no idea whether the lazy import here is done inappropriately, whether there's a subtle bug in lazy import that gets triggered here, or whether the patchbot has troubles that just happen to be triggered by this patch (sounds unlikely).

Since two of these three can be avoided by not doing a lazy import, that's probably the way to go if you want the ticket merged ASAP. Then "lazification" can be done on a separate ticket. That or someone referees the ticket with "works for me" and puts on a positive review, ignoring the bot.


---

Comment by nbruin created at 2012-12-12 19:04:32

See issue #13826. I'd recommend to just ignore the intermittent patchbot failures. Presently, "parallel doctesting with .sage and tmp on different filesystems is not supported". The linked ticket will fix that. I don't think there is a need to make this ticket dependent on it. Someone should review this ticket, since it seems to be good to go for the rest.


---

Comment by vbraun created at 2012-12-12 19:18:08

I just want to test #13826. Feel free to give this ticket a positive review. Human intelligence still trumps automated tests, you know ;-)


---

Comment by nthiery created at 2012-12-13 09:06:55

Replying to [comment:173 chapoton]:
> Nicolas, would it be possible to have a patchbot running for the combinat patches on one server somewhere ?

Yes, that's indeed the plan and the purpose of the combinat server!  I
wanted to work on it but it's buried in my todo pile; so please anyone
take over the task! Volker has posted instructions recently and it
seemed fairly straightforward.

Cheers,
                          Nicolas


---

Comment by vbraun created at 2012-12-13 14:01:35

Robert Bradshaw wrote the patchbot and posted instructions, not me. Everybody can run their own patchbot, its easy...


---

Comment by stumpc5 created at 2013-01-07 12:35:38

Could someone please investigate what is going wrong now? I do

```
lazy_import("sage.rings.universal_cyclotomic_field.all","*")
```

in `sage.rings.all` but nevertheless, it seems that the UCF and also all the numpy stuff in the pyx file is imported at startup. When I do the import of `sage.rings.universal_cyclotomic_field.all` directly but then do the lazy import of `UniversalCyclotomicField` in there, everything runs as expected.

Is this something not treated properly in #13826 ?

Thanks, Christian


---

Comment by vbraun created at 2013-01-07 13:22:39

What is your problem, precisely? The lazy import does work:

```
sage: type(UniversalCyclotomicField)
<type 'sage.misc.lazy_import.LazyImport'>
```

I also don't see any instances being created elsewhere during Sage startup.


---

Comment by stumpc5 created at 2013-01-07 14:04:47

Replying to [comment:181 vbraun]:
> What is your problem, precisely?

When I do the lazy import of `sage.rings.universal_cyclotomic_field.all.*` in `sage.rings.all` (as in the current version of the patch on trac), I get


```
$ sage -t sage/tests/startup.py 
sage -t  "devel/sage-UCF/sage/tests/startup.py"             
**********************************************************************
File "/home/stumpc5/progs/sage-5.5.rc0/devel/sage-UCF/sage/tests/startup.py", line 17:
    sage: sage0("'numpy' in sys.modules")
Expected:
    False
Got:
    True
**********************************************************************
```


and this test doesn't fail if I do the lazy import of `UniversalCyclotomicField` within `sage.rings.universal_cyclotomic_field.all`. Numpy is imported in the cython file for the UCF, and seems to be imported on startup when doing 


```
lazy_import("sage.rings.universal_cyclotomic_field.all","*")
```


but not when doing


```
lazy_import("sage.rings.universal_cyclotomic_field.universal_cyclotomic_field","UniversalCyclotomicField")
```

Do you know what goes wrong there?


---

Comment by nbruin created at 2013-01-07 17:24:48

Replying to [comment:182 stumpc5]:
> Numpy is imported in the cython file for the UCF, and seems to be imported on startup when doing 
> 
> {{{
> lazy_import("sage.rings.universal_cyclotomic_field.all","*")
> }}}
> 
> but not when doing
> 
> {{{
> lazy_import("sage.rings.universal_cyclotomic_field.universal_cyclotomic_field","UniversalCyclotomicField")
> }}}

Have you taken into account that the first time running, lazy star imports are not lazy at all? It executes the actual import to cache which symbols get defined by the star import (the files in `.sage/cache`). I think this cache presently always gets deleted after `sage -b`. If testing `startup.py` is the first sage run after that, you cannot expect lazy behaviour.

This caching strategy has its flaws, but presently we'll have to live with it.


---

Comment by stumpc5 created at 2013-01-07 17:50:20

Replying to [comment:183 nbruin]:
> Replying to [comment:182 stumpc5]:

> Have you taken into account that the first time running, lazy star imports are not lazy at all? It executes the actual import to cache which symbols get defined by the star import (the files in `.sage/cache`). I think this cache presently always gets deleted after `sage -b`. If testing `startup.py` is the first sage run after that, you cannot expect lazy behaviour.
> 
> This caching strategy has its flaws, but presently we'll have to live with it.

Thanks for the explanation -- what am I now supposed to do to get things in order? Should I keep the lazy star import and change doctest in startup.py, or should I rather not do the star import?


---

Comment by nbruin created at 2013-01-07 18:39:11

Replying to [comment:184 stumpc5]:
> Thanks for the explanation -- what am I now supposed to do to get things in order? Should I keep the lazy star import and change doctest in startup.py, or should I rather not do the star import?

Well, if two consecutive runs still show the same behaviour, it's not the caching. Anyway, if you can avoid star-import altogether, caching doesn't come into play at all. I think it's more likely anyway that after the lazy import, something investigates the namespace in which the lazy import was done to such detail that it triggers the actual import, e.g., a `from module.name import *` when `module.name` contains a lazy import may well trigger actual importation (I haven't checked).

You'll have to avoid importing numpy on startup, since that has caused big startup delays previously (hence that doctest).

I think the main thing you're finding now is that we don't have much experience in how to use lazy import in more complicated scenarios, in particular in the whole `from ...all import *` scenarios that sage seems to use everywhere upon startup.


---

Comment by chapoton created at 2013-01-10 20:44:52

Ok, the bot is happy at last.

I am giving a positive review.

Cheers !


---

Comment by chapoton created at 2013-01-10 20:44:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-10 21:26:38

Please fill in the Reviewer field.


---

Comment by stumpc5 created at 2013-01-11 08:10:28

Replying to [comment:189 chapoton]:

Thanks a lot, Fred, and also to the others for all the contributions!


---

Comment by jdemeyer created at 2013-01-30 17:38:55

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-01-30 17:38:55

There is a lot of

```
except:
```

in the patch.  Don't use this, as it will catch all exceptions, including stuff like `KeyboardInterrupt`.  If you really want a catch-all, use

```
except StandardError:
```

but try to use specific exceptions where applicable.


---

Comment by stumpc5 created at 2013-01-30 21:22:09

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2013-01-30 21:22:09

Replying to [comment:192 jdemeyer]:
> There is a lot of
> {{{
> except:
> }}}
> in the patch.

Thanks for the comment, I fixed this by removing some of the `except`'s, and used `KeyError`'s in two remaining places. I also fixed a bug, namely

```
sage: UCF(0).is_rational()
False
```

and added the doctests rechecking this. Since the patchbot doesn't like to apply #13765 (which was merged in 5.7.beta2), I wonder if you could have another look and either rebase the patch, or - if you don't plan to merge it - to wait until I have a new version compiled to rebase it myself.

Thanks, Christian


---

Comment by jdemeyer created at 2013-01-30 21:28:35

Replying to [comment:193 stumpc5]:
> I wonder if you could have another look and either rebase the patch
Why should it be rebased?  The fact that the patchbot is struggling is a bug with the patchbot, I don't think this ticket is to blame.

Anyway, I don't want to review this ticket (simply because I cannot review every ticket that I put to needs_work), but it should be easy for the original reviewer.  Frédéric, can you do it?


---

Comment by stumpc5 created at 2013-01-30 21:37:11

Replying to [comment:194 jdemeyer]:
> Replying to [comment:193 stumpc5]:
> Anyway, I don't want to review this ticket (simply because I cannot review every ticket that I put to needs_work)

Sorry, I didn't want to say you should actually review the patch again (though my message sounded like that), but only to possibly rebase it in case this would be the only modification needed to finally get this patch merged...


---

Comment by chapoton created at 2013-01-31 09:18:54

There remains 2 raise with the old syntax


```
raise ValueError, "n (=%s) must be a positive integer"%n 
```




```
raise TypeError, "Embedding (type %s) must be an element." % type(embedding) 
```


Please convert them to the Python 3 syntax.


---

Comment by vbraun created at 2013-01-31 09:34:36

On the topic of raising exceptions: start lower-case (and don't form complete sentences). Moreover, the coercion system will often feed you with invalid data to figure out what you can and cannot do. Hence it is best to avoid unnecessary work like creating string representations and concatenating them to form an exception message. Just raise `TypeError('x must be an element')`.


---

Comment by jdemeyer created at 2013-01-31 09:53:27

Another possible complaint about this patch is that it uses quite some Cython code but always without [sig_on()/sig_off()](http://sagemath.org/doc/developer/coding_in_cython.html#interrupt-and-signal-handling).  As a consequence, this code might not be interruptible on CTRL-C.  I don't know to what extent this is a problem, I'm just pointing it out.  Anyway, it can't hurt to put some `sig_check()` calls inside the loops.


---

Comment by stumpc5 created at 2013-01-31 20:08:50

A general comment concerning several complaints on this ticket from various directions: If you ask mathematicians to contribute to Sage, you get mathematicians writing code and code that is not necessarily perfect. This does have disadvantages! But please don't blame them (i.e. me here) for not being perfect programmers!

Beside that, I fixed the complaint concerning error messages and their Python 3 syntax, but I am not going to go into interruption handling in cython. This can be handled in another ticket by someone more advanced.

Finally: I already spent much too much time on this ticket (i.e., I implemented the stuff I actually needed for my research 2 years ago, all further hours and days were not spent anymore for my primary research). I would very much appreciate if we could get this ticket into Sage, and then solve further issues in other patches.


---

Comment by jdemeyer created at 2013-01-31 20:16:20

Set assignee to jdemeyer.


---

Comment by jdemeyer created at 2013-01-31 20:16:20

Replying to [comment:199 stumpc5]:
> I am not going to go into interruption handling in cython.
No problem, note that I purposely did not set the status to needs_work for this.  Your code is certainly not the only part of Sage with this problem.

> Finally: I already spent much too much time on this ticket (i.e., I implemented the stuff I actually needed for my research 2 years ago, all further hours and days were not spent anymore for my primary research).
It's simply a fact that going from proof-of-concept-research-code to actual good code to be included in Sage is a non-trivial step.  You could say it's unfortunate, but that's the way it is.


---

Comment by vbraun created at 2013-01-31 21:18:35

I actually do think the code here is pretty good, so please don't take everything as a criticism. I think this ticket is good to go, I just wanted to wait and see if the recently updated patchbot fares better at running it...


---

Comment by jdemeyer created at 2013-02-01 07:07:45

Now that you have changed the exceptions, also the doctests for the exceptions need to changed.  I see various failures along the lines of

```
**********************************************************************
File "/release/merger/sage-5.7.beta3/devel/sage-main/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field.py", line 1755:
    sage: E(6).galois_conjugates(5)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: the given integer (5) is not a multiple of the field order of -E(3)^2
Got:
    Traceback (most recent call last):
      File "/release/merger/sage-5.7.beta3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/release/merger/sage-5.7.beta3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/release/merger/sage-5.7.beta3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_61[10]>", line 1, in <module>
        E(Integer(6)).galois_conjugates(Integer(5))###line 1755:
    sage: E(6).galois_conjugates(5)
      File "/release/merger/sage-5.7.beta3/local/lib/python/site-packages/sage/rings/universal_cyclotomic_field/universal_cyclotomic_field
.py", line 1765, in galois_conjugates
        raise ValueError("The given integer (%s) is not a multiple of the field order of %s"%(m,self))
    ValueError: The given integer (5) is not a multiple of the field order of -E(3)^2
**********************************************************************
```



---

Comment by jdemeyer created at 2013-02-01 07:07:45

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by stumpc5 created at 2013-02-01 08:33:33

Replying to [comment:202 jdemeyer]:
> Now that you have changed the exceptions, also the doctests for the exceptions need to changed.

Sorry, I exported the patch before qrefreshing...


---

Comment by chapoton created at 2013-02-01 09:10:57

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-02-01 09:51:48

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2013-02-01 09:51:48

ok, bot is happy again. Positive review once more.


---

Comment by jdemeyer created at 2013-02-05 08:16:37

Resolution: fixed


---

Comment by nthiery created at 2013-02-05 17:11:45

Yippee! Congratulations Christian!

And thanks so much for going the extra mile! I agree that all the extra work you did for getting this ticket into Sage involved not only necessary cleanup but also extra features that could have been left aside in a first round!

Thanks!
                                        Nicolas


---

Comment by stumpc5 created at 2013-02-06 09:36:38

Replying to [comment:207 nthiery]:
> Yippee!

+1!!!


---

Comment by kcrisman created at 2013-02-15 03:26:01

Just fyi, #14118 had to be opened regarding this, not that Cygwin is currently supported (yet!).  Hopefully this will make it more portable in the long run anyway.
