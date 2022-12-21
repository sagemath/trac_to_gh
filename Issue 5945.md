# Issue 5945: fastify factorization of inferior integers with flint

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-04-30 06:15:16

Assignee: tbd

CC:  zimmerma

FLINT can factor faster than PARI for integers smaller than 2^50 or so.  So by default, we should use FLINT for this.


---

Comment by boothby created at 2009-04-30 06:20:41

Note, we'll need an upgraded FLINT for this to work.  Among other things, FLINT exports a global variable named "primes".  And so does PARI.  And they don't play well with eachother.

Also, the attached code contains a bug.  And Factorization objects can be made with less overhead.


---

Comment by boothby created at 2009-04-30 07:03:13

The attached fixes aforementioned bug.  New spkg coming soon.


---

Comment by mabshoff created at 2009-04-30 07:08:09

Changing component from algebra to factorization.


---

Comment by mabshoff created at 2009-04-30 07:08:09

Replying to [comment:3 boothby]:
> The attached fixes aforementioned bug.  New spkg coming soon.

What is the plan here? Right now from my end I want to get the latest released upstream into 3.4.2, so it would be nice if you got your code into FLINT and then get Bill to release it. That way the Debian people won't complain ;)

Cheers,

Michael


---

Comment by jason created at 2009-10-06 19:28:01

Changing status from new to needs_work.


---

Comment by aapitzsch created at 2010-11-04 10:58:12

I created a new ticket #10211 for changes in long_extras.pxd, to get this fixed faster.


---

Comment by aapitzsch created at 2010-11-08 09:29:12

Changing status from needs_work to needs_review.


---

Attachment

I decided to move `flint_factor` to `fast_arith.pyx`, so it can be used for `int`, too.
To check the improvements use attachment:5945_check_improvements.patch, attachment:5945_check_improvements.sage and

```
(line(values_p)+line(values_f,color='red')).plot()
(line(values_med_p)+line(values_med_f,color='red')).plot()
```



---

Attachment

apply only this patch; apply after #10211


---

Attachment

only to check improvements, not for release


---

Comment by aapitzsch created at 2010-12-06 15:49:52

patch updated to fix problem buildbot has

```
2010-12-03 10:18:03 -0800
hg qpush trac_5945_factor_flint.patch
applying trac_5945_factor_flint.patch
patching file sage/rings/arith.py
Hunk #2 FAILED at 2076
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_5945_factor_flint.patch
patch queue now empty
None
2010-12-03 10:18:04 -0800
0 seconds
```



---

Comment by aapitzsch created at 2010-12-08 09:20:24

only apply this patch


---

Comment by spancratz created at 2011-01-08 06:49:32

Changing status from needs_review to needs_work.


---

Attachment

Thanks for doing this!

Looking at the source code, the line ``flint_bits = int(FLINT_BITS)`` seems wrong.  You can (and should, I think) simply use FLINT_BITS directly.  Of course, this comment is rather minor.

Sebastian


---

Comment by boothby created at 2011-01-10 06:31:49

Changing status from needs_work to needs_review.


---

Comment by boothby created at 2011-01-10 07:45:14

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2011-01-10 07:45:14

segfault in arith.py


---

Comment by aapitzsch created at 2011-01-10 14:44:56

I tried to apply your patch to 4.6.1 rc1

```
applying /scratch/sage-4.6.1rc1/trac_5945bp.patch
patching file sage/rings/arith.py
Hunk #2 FAILED at 2290
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 3139
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
abort: patch failed to apply
```



---

Comment by spancratz created at 2011-01-10 18:48:15

Hi Andre,

Yes, that was an unfortunate case of Tom and I uploading the patch last night before combining it with another patch it relied on.  I have now uploaded a file ``trac_5945.patch``, which should combine everything and is to be applied on top of #10211.

Sebastian


---

Comment by spancratz created at 2011-01-10 19:16:44

Just in case this wasn't obvious, ``trac_5945.patch`` applies to 4.6 and ``trac_5945_461rc0.patch`` applies to 4.6.1.rc0.  Both of these depend on #10211.

Sebastian


---

Comment by spancratz created at 2011-01-11 00:53:15

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2011-01-11 07:05:16

After some cleaning up, there is now a single patch ``trac_5945.patch`` that can be applied against 4.6.1.rc0 with #10211.

Morally speaking, this should be good to go.  However, sage.math.washington is currently under heavy use by Jeroen and I'll wait until tomorrow before running the complete test suite.

Best wishes,
Sebastian


---

Comment by aapitzsch created at 2011-01-11 12:19:45

You should use the variable `flint_depends` in *module_list.py* and

```
SAGE_LOCAL+'include/FLINT/'
```

or

```
SAGE_INC+'FLINT/'
```

instead of

```
SAGE_ROOT+'/local/include/FLINT/'
```


*arith.py*:
remove

```
if proof is None:
    proof = True
```

and let `n.factor` handle `proof=None`.

*integer.pyx*: I suggest using the global default for _proof_ in factor()

Change

```
F = [(Integer(f.p[i]), f.exp[i]) for i from 0 <= i < f.num]
```

to

```
F = [(Integer(f.p[i]), int(f.exp[i])) for i from 0 <= i < f.num]
```

then only following doctests fail (otherwise even more would fail, e.g. arith.py):

```
sage/misc/sageinspect.py
sage/structure/factorization.py
```



---

Comment by spancratz created at 2011-01-11 16:33:44

Hi Andre,

Thank you for the quick comments.  All of these are very sensible!  The only one I am not quite sure about is the last, where I thought the underlying FLINT structure already had f.exp[i] of the right type to that calling int(-) on it would not be necessary, but I might be wrong.

(I'm not quite sure which time zone you are working in right now, so this comment might be more for Tom.)  I'm off to the gym now, but I'll have fixed this in time for lunch,

Sebastian


---

Attachment

I'm sorry for adding the duplicate file ``trac_5945.2.patch``, this can be deleted from here.  The other file ``trac_5945.patch`` should now apply cleanly to 4.6.1.rc0 and pass all tests.

Sebastian


---

Comment by aapitzsch created at 2011-01-12 13:50:08

trac_5945.patch seems to be incomplete, e.g. `class IntegerFactorization(Factorization)` and comment changes are missing, thus I couldn't finish review.

Anyway.

_arith.py_:
Maybe you should also pass `**kwds` to n.factor() if n is Integer, int or long, so `limit` can be used: `factor(8*49,limit=5)`


---

Comment by aapitzsch created at 2011-01-12 17:00:34

Can you also fix #10602 for Integer.factor(). I only mention this because it's fixed in none of the last two patches.


---

Attachment

Version for 4.6.0


---

Attachment

Version for 4.6.1.rc0


---

Comment by spancratz created at 2011-01-12 20:05:13

Fix for a remaining doctest failure in sageinspect.py


---

Attachment

Hi Andre,

I'm sorry for the earlier patch not including the IntegerFactorization class, I don't know how that happened.  Now, there are three things to do:

    - Apply #10211
    - Apply either trac_5945.patch or trac_5945-461rc0.patch, depending on the Sage version
    - Apply trac_5945_fix.patch

Tom, could you perhaps clean up this ticket and remove all other files that I or we added?

Sebastian


---

Comment by aapitzsch created at 2011-01-13 11:13:46

Changing status from needs_review to positive_review.


---

Attachment

Apply trac_5945_reviewer.patch after trac_5945_fix.patch

Version rc0 reviewed.

Attached trac_5945_reviewer.patch handles doctest failure in _factorization.py_. I only changed the expected result but actually it should be a new test with old result.

_sage/libs/flint/long_extras.pxd_ contained `ctypedef struct factor_t:`... twice so I removed one.

Everything else is okay.


---

Comment by spancratz created at 2011-01-13 18:58:46

Hi Andre,

Great, thank you for doing this!

Sebastian


---

Attachment


---

Comment by aapitzsch created at 2011-01-17 13:15:45

Merged patches into trac_5945-462a0.patch. So you only need to apply this one. Based on 4.6.2.alpha0.


---

Comment by jdemeyer created at 2011-01-17 20:40:11

There are a few doctest failures:

```
The following tests failed:

        sage -t  -force_lib devel/sagenb-main/sagenb/misc/sageinspect.py # 1 doctests failed
        sage -t  -force_lib devel/sage/doc/en/tutorial/programming.rst # 1 doctests failed
        sage -t  -force_lib devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed
```



---

Comment by jdemeyer created at 2011-01-17 20:40:11

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by aapitzsch created at 2011-01-18 09:29:23

Apply trac_5945_sagenb.patch and trac_5945_doc_fix.patch after trac_5945-462a0.patch


---

Comment by aapitzsch created at 2011-01-18 09:29:23

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-01-19 01:40:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 01:40:52

Doctests are fixed.


---

Comment by jdemeyer created at 2011-01-19 22:19:17

Resolution: fixed
