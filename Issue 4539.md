# Issue 4539: [with patch, needs work] plural wrapper

Issue created by migration from https://trac.sagemath.org/ticket/4539

Original creator: burcin

Original creation time: 2008-11-17 15:27:31

Assignee: tbd

CC:  saliola mhansen alexanderdreyer oleksandrmotsak polybori malb simonking

During SD10 in Nancy, Michael Brickenstein and I worked on making Plural (the non-commutative extension of Singular) accessible from Sage.

The patches that resulted from this work are attached. They still need to be polished to be included in Sage.

Possible topics that need work are:
 * coercion
 * flag to check degeneracy conditions on init
 * put the files in sage/algebra/ ???
 * make sure element does not export functions it doesn't support (e.g. gcd)

For a full featured wrapper we also need the following (they should be separated into different bugs once this one is done):
 * groebner basis
 * predefined structures from the library


---

Comment by burcin created at 2008-11-17 15:28:49

initial wrapper for plural


---

Attachment

better user interface for plural rings


---

Attachment


---

Attachment


---

Comment by burcin created at 2009-12-30 21:49:46

Changing assignee from tbd to burcin.


---

Comment by burcin created at 2009-12-30 21:49:46

The letterplace interface in attachment:letterplace.py is now at #7797.


---

Attachment

rebased to 4.4.4


---

Comment by burcin created at 2010-07-14 16:46:41

rebased to 4.4.4


---

Attachment

appy on top of 1 and 2, new classes for plural objects which don't inherit from the commutative ones


---

Attachment


---

Comment by PolyBoRi created at 2010-07-15 21:06:58

sorry, for multiple files. Apply patches in this order:

plural_1.sage-4.4.4.patch 
         
plural_2.sage-4.4.4.patch
                         
plural_3.patch Download 
                         
plural_functions.patch


---

Attachment


---

Comment by OleksandrMotsak created at 2010-07-20 14:10:20

i have just folded all the previous patches by Michael & Burcin into plural_folded-4.4.4.patch (should be applied before anything else)


---

Attachment

Part one Olekandr's work in Linz


---

Attachment

Doctest fixes by Alexander


---

Attachment

Doctest fixes by Alexander


---

Attachment

noncommunative ring functionality


---

Attachment


---

Comment by AlexanderDreyer created at 2010-07-22 12:30:26

Changing assignee from burcin to OleksandrMotsak,AlexanderDreyer.


---

Attachment

This folds of the following patches, a crucial subset of the noncommutation fucntionality as well as extensive documentation and  doctests


---

Comment by AlexanderDreyer created at 2010-07-22 12:35:12

We have an first release ready for reviewing! 

Regards, Oleksandr and Alexander


---

Comment by AlexanderDreyer created at 2010-07-22 12:37:52

Changing status from needs_work to needs_review.


---

Comment by PolyBoRi created at 2010-07-22 12:41:34

wow, that sounds awesome.
You make me really happy.
Can you outline in the ticket description, what the patch actually implements and what not.


---

Comment by OleksandrMotsak created at 2010-07-22 13:28:55

what is meant in "predefined structures from the library"?

Need input: what structures / what library?


---

Attachment

Fixed some broken doctests


---

Attachment


---

Comment by AlexanderDreyer created at 2010-07-24 07:23:50

coverage to 100%


---

Comment by SimonKing created at 2010-07-24 14:59:25

How to apply the patches? _All_ and in the given order? Or is one of them a "master patch" that replaces several other patches


---

Comment by AlexanderDreyer created at 2010-07-25 19:30:07

Just the following:
plural-wrapper-2010-07-22.patch 
plural-missing-docu.2.patch 

Regards,
  Alexander


---

Comment by AlexanderDreyer created at 2010-07-27 13:51:07

Accumulated patch for all patches above for Singular/Plural


---

Attachment


---

Comment by AlexanderDreyer created at 2010-07-27 13:52:51

Changing assignee from OleksandrMotsak,AlexanderDreyer to OleksandrMotsak, AlexanderDreyer.


---

Comment by nthiery created at 2010-10-01 07:58:00

Hi!

I have some computations to do with Weyl algebras, and would love to have this cool piece of work at my fingertips! Please keep it up!

For the record: I tried to apply those patches to Sage 4.5.2, and got the following rejects:

```
zephyr-/opt/sage/devel/sage>hg qimport ~/plural-wrapper-2010-07-27.patch
adding plural-wrapper-2010-07-27.patch to series file
zephyr-/opt/sage/devel/sage>hg qpush
applying plural-wrapper-2010-07-27.patch
patching file sage/libs/singular/function.pyx
Hunk #3 succeeded at 96 with fuzz 2 (offset 0 lines).
Hunk #36 FAILED at 1378
1 out of 38 hunks FAILED -- saving rejects to file sage/libs/singular/function.pyx.rej
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #3 succeeded at 218 with fuzz 2 (offset -1 lines).
patching file sage/rings/ideal_monoid.py
Hunk #1 FAILED at 12
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/ideal_monoid.py.rej
patching file sage/rings/polynomial/term_order.py
Hunk #1 FAILED at 419
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/term_order.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh plural-wrapper-2010-07-27.patch
```


Cheers,


---

Comment by AlexanderDreyer created at 2010-10-01 12:07:37

Hi nthiery,
Meanwhile, Burcin did a rebase?  Does it help you?

Regards,
  Alexander


---

Comment by nthiery created at 2010-10-01 12:32:36

Yes, it now applies smoothly on 4.5.2, and compiles. Thanks!


```
zephyr-~sage-main>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<x,dx> = FreeAlgebra(QQ,2)    
sage: F.g_algebra({dx*x: x*dx+1})
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
Same problem with the example taken from the documentation:


```
zephyr-~sage-main>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x,y,z>=FreeAlgebra(QQ,3)
sage: G=A.g_algebra({y*x:-x*y})
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
Should I be using 4.5.3 (being downloaded)?


---

Comment by AlexanderDreyer created at 2010-10-01 12:44:33

Did you rebuild? (`sage -br`)


---

Comment by nthiery created at 2010-10-01 12:47:13

Replying to [comment:24 AlexanderDreyer]:
> Did you rebuild? (`sage -br`)

Yup.


---

Comment by AlexanderDreyer created at 2010-10-01 14:13:26

I could reproduce the issue: `sage -gdb` vields the following;

```
sage: A.<x,y,z>=FreeAlgebra(QQ,3)
sage: G=A.g_algebra({y*x:-x*y})

Program received signal SIGSEGV, Segmentation fault.
0x00007fffdec7c488 in __pyx_f_4sage_4libs_8singular_8function_call_function (__pyx_v_self=0x459f910, __pyx_v_args=0x4538ab8, __pyx_v_R=0x4676480,
    __pyx_optional_args=<value optimized out>) at sage/libs/singular/function.cpp:11969
11969       currRingHdl->data.uring->ref += 1;
```



---

Comment by burcin created at 2010-10-01 14:27:31

I didn't have a chance to test the rebased patch, I had to leave right after I finished merging the rejected parts. I just wanted to get it out there in case it worked.

I can also reproduce the crash. I'll take a look at it now and try to upload a patch that works.


---

Comment by burcin created at 2010-10-01 14:27:31

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-10-01 14:32:43

rebased to 4.5.3


---

Attachment

It was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.

Nicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.

Though I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases.


---

Comment by nthiery created at 2010-10-03 21:06:26

Replying to [comment:28 burcin]:
> It was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.

It also does for me so far! Thanks a lot for the quick rebase!

> Nicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.

I don't want to promise much at this time because I am already (very) late with a couple other reviews. But since the code is going to very useful for my research right now, I can promise to provide feedback for how it feels in practice!

> Though I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases. 

Sounds good to me!


---

Comment by nthiery created at 2010-10-03 21:06:40

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-10-03 21:08:57

Is it possible at this stage to define non commutative polynomial rings over QQ['q'].fraction_field()?
I got an error with what I tried:


```
sage: K = QQ['q'].fraction_field()
q = K.gen()
F.<x,y,ex,ey> = FreeAlgebra(K,4)
W =  F.g_algebra({ex*x: x*(1+ex),ey*y:y*(1+ey)})

sage: ------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/algebras/free_algebra.py", line 547, in g_algebra
    return NCPolynomialRing_plural(base_ring, n, ",".join([str(g) for g in self.gens()]), c=cmat, d=dmat, order=order, check=check)
  File "plural.pyx", line 223, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__init__ (sage/rings/polynomial/plural.cpp:3772)
  File "matrix0.pyx", line 1520, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:7670)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 405, in __call__
    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 1136, in matrix
    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
  File "matrix_generic_dense.pyx", line 93, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:2321)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 468, in __call__
    c = self.base_ring()(x)
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/fraction_field.py", line 467, in _element_constructor_
    coerce=coerce, reduce = self.is_exact())
  File "fraction_field_element.pyx", line 120, in sage.rings.fraction_field_element.FractionFieldElement.__init__ (sage/rings/fraction_field_element.c:1934)
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.py", line 313, in _element_constructor_
    return C(self, x, check, is_gen, construct=construct, **kwds)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.py", line 656, in __init__
    x = [QQ(z) for z in x]
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "rational.pyx", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)
  File "rational.pyx", line 521, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)
TypeError: Unable to coerce 0 (<class 'sage.algebras.free_algebra_element.FreeAlgebraElement'>) to Rational
```


Thanks!


---

Comment by nthiery created at 2010-10-03 21:22:12

I started playing with ideals. Currently, one creates an ideal I, and
then when one calls I.std() or I.twostd() to create a new left or
twosided ideal, and actually compute the Groebner basis. What about
the following variants:

(A) Take the side decision at the time the ideal is created:

```
    sage: I = W.ideal([...], side=...)
```

(to be documented in ``W.ideal?``).

With that, ``I`` would be well defined as an ideal; otherwise it is
more a ``collection of polynomials'' and the name is misleading.

(B) About computing the Grobner basis:

```
    sage: I.groebner_basis()
```


or:

```
    sage: I.std() 
```

would compute the groebner basis, store it for later calculations, and
return it as a list of polynomials rather than a new ideal.

I haven't actually played with ideals in Sage; so maybe point (B) is
just how things are with commutative ideals in Sage, and consistency
should take precedence.

Cheers,
                    Nicolas


---

Comment by SimonKing created at 2010-10-03 21:58:00

Replying to [comment:32 nthiery]:
> I started playing with ideals. Currently, one creates an ideal I, and
> then when one calls I.std() or I.twostd() to create a new left or
> twosided ideal, and actually compute the Groebner basis. What about
> the following variants:

Currently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.

How to implement it? Well, on could have a base class for ideals over non-commutative rings (let's call it `NCIdeal`), and derive from it `NCIdeal_left`, `NCIdeal_right`, `NCIdeal_twodsided`.

Then, one has to modify the multiplication method for rings so that sidedness is taken care of (there is a method ideal_class(), that probably needs to accept an optional argument "side"). And of course, the one-sided ideal classes need a multiplication method as well.

And then, `NCIdeal_twodsided.groebner_basis()` would yield a two-sided Gröbner basis, while `NCIdeal_left/right.groebner_basis()` would only yield a one-sided Gröbner basis, of course unless a two-sided Gröbner basis is requested by using an optional argument.


---

Comment by nthiery created at 2010-10-12 15:20:52

Replying to [comment:32 nthiery]:
> I started playing with ideals. Currently, one creates an ideal I, and
> then when one calls I.std() or I.twostd() to create a new left or
> twosided ideal, and actually compute the Groebner basis. 

By the way: right ideals are not yet handled yet, right? Would it be a lot of work? It's just that the ideals I am currently playing with are right ideals, and I keep mixing myself up when playing with the "dualized" version I had to write in Sage.


---

Comment by nthiery created at 2010-10-12 15:28:01

Hi Simon!

Replying to [comment:33 SimonKing]:
> Replying to [comment:32 nthiery]:
> > I started playing with ideals. Currently, one creates an ideal I, and
> > then when one calls I.std() or I.twostd() to create a new left or
> > twosided ideal, and actually compute the Groebner basis. What about
> > the following variants:
> 
> Currently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.

+1 for the implementation proposal!

I also like that shorthand syntax for interactive usage. However, in
code, I prefer using something more explicit like R.ideal(L,side=...).
Besides, having an R.ideal method also provides with:

 - a good place for advertising (it appears in R.<tab>), documenting,
   testing the feature and its shorthand
 - an easy way for subclasses of (the class of) R to override this
   method without having to worry about overloading/coercion/...

Cheers,
			Nicolas


---

Comment by SimonKing created at 2011-03-13 10:44:31

Apply plural-wrapper-2010-10-01.patch

(to the patchbot)

If I understand correctly, this patch is the only one, right? So, it would be a good thing to try whether it needs to be rebased again.

Currently, I have a high motivation to have the noncommutative stuff (including letterplace!) in libsingular. So, I hope the work on this ticket and on #7797 can be resumed.


---

Comment by SimonKing created at 2011-03-13 14:13:21

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-03-13 14:13:21

Apply trac4539_libplural.patch

It turned out that the old patch did not apply, since meanwhile the libsingular options are dealt with in a different way. I have rebased the patch, and also adopted the new option syntax.

However, not all is good. Here is one error that I just found:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3) 
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}) 
sage: H.inject_variables() 
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False) 
sage: G = vector(I.gens()); G  
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
/mnt/local/king/SAGE/sage-4.6.2/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6035)()

NotImplementedError: 
```


So, there remains work to do!


---

Comment by SimonKing created at 2011-03-13 14:13:21

Changing keywords from "" to "libsingular plural wrapper".


---

Comment by SimonKing created at 2011-03-13 14:27:36

The reason of the error was that `FreeModule` tries (among other things) the method `is_integral_domain()`. By default, it raises a `NotImplementedError`, and this is the error we get above.

Proposed solution: Catch that `NotImplementedError` and do as if `is_integral_domain()` had returned `False`.

I don't know if there will be further problems, but I'll put it back to "needs review".


---

Comment by SimonKing created at 2011-03-13 14:27:36

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-03-13 18:25:15

Apply trac4539_libplural.patch


---

Comment by SimonKing created at 2011-03-13 18:27:02

1. I don't know why the patchbot is trying _two_ patches. It is supposed to use only one of them.

2. I get numerous doctest failures. Some of them look like severe errors. So, it needs work.


---

Comment by SimonKing created at 2011-03-13 18:27:02

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2011-03-23 22:16:47

It would be great to have this in Sage!

I'm seeing some problems with the patch.  First, it doesn't apply cleanly to Sage 4.7.alpha1.  I haven't tried applying to 4.6.2.  I rebased it by hand.

Second, the change

```diff
-                    block_name, block_length, _ = re.split(length_pattern,block)
+                    block_name, block_length, _ = re.split(pattern, block.strip())
```

in term_order.py is problematic, because "pattern" is not defined anywhere.  Replacing it by "length_pattern" seems to work.

Third, in multipolynomial_ideal.py, `_groebner_basis_libsingular` is being called with keywords "deg_bound" and "mult_bound", but it doesn't accept those keywords as valid arguments.  Should we add `*args, **kwds` to the argument list?    Or should those keywords be dealt with explicitly?  I tried adding generic `*args` and `**kwds`, but doctesting on that file segfaults.

When I doctest the whole Sage library after making these changes, I get the following failures:

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Killed/crashed
        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/libs/singular/polynomial.pyx # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/plural.pyx # 6 doctests failed
```

On one machine, I also had this failure:

```
	sage -t -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial.pyx # Killed/crashed
```



---

Comment by jhpalmieri created at 2011-03-30 22:36:18

I've rebased the patch to Sage 4.7.  I'm not sure it's worth cluttering up this ticket with more patches, especially ones this big, so I've posted it to [http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch](http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch).  This patch also fixes a few docstrings, and it makes the changes that I described above, although I'm not sure they're the right thing to do.


---

Comment by SimonKing created at 2011-09-26 17:50:36

Changing keywords from "libsingular plural wrapper" to "libsingular plural wrapper sd34".


---

Comment by SimonKing created at 2011-09-26 17:50:36

At sage days 34, we try to rebase the old patch. Burcin and I agree that we should rebase it with respect to #7797 (which, among other things, modernises coercion for free algebras). It also means that we can use one- and two-sided ideals in non-commutative rings, by #11068.

Some hunks of the latest patch fail due to other tickets that meanwhile are merged, such as #11316.

It seems to me that, out of the 5 hunks that fail, only 2 are non-trivial to fix.


---

Comment by AlexanderDreyer created at 2011-09-26 22:29:41

experimental rebasement to 4.7.2alpha3-prerelease


---

Attachment

Can you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?


---

Comment by SimonKing created at 2011-09-26 23:04:56

Replying to [comment:44 AlexanderDreyer]:
> Can you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?

We were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome).

But is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.


---

Comment by AlexanderDreyer created at 2011-09-26 23:15:56

Replying to [comment:45 SimonKing]:

> We were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome). But is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.

Sorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.


---

Comment by AlexanderDreyer created at 2011-09-26 23:57:58

Replying to [comment:46 AlexanderDreyer]:
> Sorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.
Just foudn out, the patch was fine (so far), but my sage/devel directory was corrupted. (Luckily I cloned.)


---

Comment by SimonKing created at 2011-09-27 06:54:46

I have attached my experimental rebasement (relative to #7797 on top of sage-4.7.2.alpha3), but not all is good.

There are quite a lot of doctest failures, including some very wrong arithmetical results in plural.pyx.

Less dramatic: There are some zero division errors (for example in doctests of mul
ti_polynomial_libsingular.pyx) where the expected error message was "rational division by zero", but now there is _no_ error message (but there is a `ZeroDivisionError`, at least).

There is a segment fault in the tests of multi_polynomial_ideal.py. I guess it is the same segfault that also occurs in some elliptic curves tests.

Alexander, when you said that your broken Sage installation was to blame: Do you mean that the tests are mostly passing with your patch?


---

Comment by SimonKing created at 2011-09-27 08:12:14

I am now testing Alexander's patch. First good news: It applies without fuzz, even when #7797 is applied. Let's see how the doc tests work!


---

Comment by SimonKing created at 2011-09-27 08:21:51

I started with "manually" testing against three of the doc test errors that I got with my patch. Two of them fail with Alexander's patch as well:

```
sage: P.<x,y,z> = QQ[]
sage: x/0
Traceback (most recent call last):
...
ZeroDivisionError:
```

 --> The old error message "rational division by zero" has gone.


```
sage: (x*y).is_monomial()
True
sage: (2*y).is_monomial()
False
```

 --> That's better than my patch, where these return 1 and 0.


```
sage: (x+y^2^30)^10
x^10
```

 --> That should result in an overflow error.

I didn't analyse the segmentation faults.


---

Comment by SimonKing created at 2011-09-27 08:22:30

PS: Note that all these problems concern _commutative_ polynomials.


---

Comment by SimonKing created at 2011-09-27 14:16:42

Replying to [comment:50 SimonKing]:
> sage: P.<x,y,z> = QQ[]
> sage: x/0
> Traceback (most recent call last):
> ...
> ZeroDivisionError:

Here is the explanation:

Let `P = QQ[x,y,z]`. Since coercion is now done properly, x/0 is first converting 0 into P and tries to invert it there. The result is a naked `ZeroDivisionError` in
sage.libs.singular.polynomial.singular_polynomial_div_coeff.
Before, it used to invert 0 as a rational number, resulting in a `ZeroDivisionError` with some error message.

Burcin and I agree that it is ok to have the `ZeroDivisionError` without a message: What else could it state but "don't divide by zero"?

So, it is not an issue.

> {{{
> sage: (x*y).is_monomial()
> True
> sage: (2*y).is_monomial()
> False

I don't know why it has occured in the first place, but now it seems alright, even with my patch.

> {{{
> sage: (x+y<sup>2</sup>30)^10
> x^10
> }}}
>  --> That should result in an overflow error.

It turns out that one gets the _same_ stupid result with an unpatched sage-4.7.2.alpha2. Burcin told me that this patch is supposed to fix it. Apparently it fails, and we need to understand why it fails.

> I didn't analyse the segmentation faults.

That will be next...


---

Comment by SimonKing created at 2011-09-27 14:38:29

I created a new ticket #11856 for the (missing) overflow error.


---

Comment by SimonKing created at 2011-09-27 14:39:03

Replying to [comment:53 SimonKing]:
> I created a new ticket #11856 for the (missing) overflow error.

Sorry, I forgot: It should be a dependency.


---

Attachment

Experimental rebasement wrt sage-4.7.2.alpha3 plus #7797 plus #11856


---

Comment by SimonKing created at 2011-09-27 16:13:37

It seems that I was able to get the missing overflow error in #11856, which I added as a dependency. I had to update my patch (and Alexander will need to update his as well), because the function overflow_check is now expecting two arguments (a long and a ring), not one.

Tests are still missing, of course, and I have still no idea about the segfault.


---

Comment by AlexanderDreyer created at 2011-09-27 22:07:40

fixes at least some segfault (updated patch) - needs main patch applied before


---

Attachment

I found out that the intended lmul implementation, namely using rmul _and_ reverting left and right hand side, is an illegal for some right hand side objects. Up to now, this is only verified for schemes/elliptic_curves/ell_curve_isogeny.py More extensive tests follow.


---

Comment by SimonKing created at 2011-09-28 06:16:41

Hi Alexander, the description of your lmul patch says "needs main patch applied before". Which of the two main patches are you referring to?


---

Attachment

fixes "keyword not found" issue (revert unnecessary path of the big patch)


---

Comment by AlexanderDreyer created at 2011-09-28 09:01:19

Here another small patch reverts an unnecessary part of the big patch. It fixes the keyword argument not found issue.


---

Attachment

Patch for using trac4539_libplural-2011-09-27-untested.patch together with #11856 (not needed for trac4539_libplural_todo.patch)


---

Attachment

monomial_quotient should throw instead of return nonsense


---

Attachment

Concerning [attachment:trac4539_monomial_quotient.patch]: I am not sure if it is the right thing to do. I think that monomial_quotient is a method that should be as fast as possible, since in some situations it is used very frequently. In these situations, it is always the case that one monomial _does_ divide the other. Hence, for the application, it is a bad idea to have a redundant sanity test in monomial_quotient. I'd rather have it return a wrong result when using it in a wrong way.

Note that [attachment:trac4539_kwds.patch] is not needed for my patch - I already have *args in it.

We have already briefly discussed why I think that [attachment:trac4539_lmul.patch] probably is not a good approach: x._rmul_(c) and x._lmul_(c) (by specification of the coercion model) can assume that the argument c belongs to x.parent().base_ring(). In particular, I don't believe that c can actually be a non-commutative polynomial.

Can you please provide an example that was segfaulting without the lmul-patch?


---

Comment by SimonKing created at 2011-09-28 13:38:19

At least, when I use [attachment:trac4539_libplural_todo.patch] plus [attachment:trac4539_lmul.patch] on top of sage-4.7.3.alpha3-prerelease, then all tests in sage/rings/polynomial pass (except those that fail in the unpatched version as well).

Since I believe that the monomial quotient patch does not do the right thing, I'd prefer to work on top of [attachment:trac4539_libplural_todo.patch] and [attachment:trac4539_lmul.patch], and concentrate on getting the lmul business right.


---

Comment by SimonKing created at 2011-09-28 13:40:21

I can already confirm that ther _is_ a segfault without the lmul patch. So, I'll try to analyse what arguments are passed to _rmul_ / _lmul_. If I remember correctly, polynomial rings do not use the current coercion model. Hence, it is perhaps no surprise that _rmul_ and _lmul_ do not do what we expect.


---

Comment by SimonKing created at 2011-09-28 13:51:50

It is very strange: Apparently, a different lmul method fixes the segfault. However, when I insert a print statement in the unpatched lmul method, then I find that it is actually not executed directly before segfaulting.

Alexander, how did you found that a change in lmul could fix it?


---

Comment by SimonKing created at 2011-09-28 14:07:50

Alexander has just explained the lmul problem to me. It was an oversight in the original patch, where self._lmul_(right) was calling right._rmul_(self), which is of course wrong, since the argument to _rmul_ must be an element of the base ring. It should correctly be self._rmul_(right).

Alexander just told me that he agrees in dropping the (redundant) test in monomial_quotient.


---

Attachment

Combined patch relative to sage-4.7.2.alpha3 plus #7797 plus #11856


---

Comment by SimonKing created at 2011-09-28 14:14:47

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-09-28 14:14:47

The new [attachment:trac4539_libplural.2.patch] is stand-alone and is supposed to summarise the discussion we had here. I think it is ready to be reviewed (but as usual I didn't run the tests yet...).

Apply trac4539_libplural.2.patch


---

Comment by SimonKing created at 2011-09-28 15:33:47

I get a doctest failure in sage/rings/polynomial/multi_polynomial_ideal.py. There, a protocol of a Gröbner basis computation is printed where we do not expect it.

The problem: If one runs the test separately, it works fine:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
sage: G = vector(I.gens()); G
/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:366: UserWarning: You are constructing a free module   over a noncommutative ring. Sage does
             not have a concept of left/right and both sided modules, so be careful. It's also
             not guaranteed that all multiplications are done from the right side.
  not guaranteed that all multiplications are done from the right side.""")
/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:584: UserWarning: You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.
  warn("""You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.""")
(y^2, x^2, z^2 - 1)
```


But the same doctest executed as part of the doctest suite has a 

```
std in (0),(x,y),(dp(2),C)
[4294967295:2]3ss4s6
(S:2)--
product criterion:1 chain criterion:0
```

printed after (!!) the result.

So, apparently another test has a side effect. I tried to identify it (e.g., a test that sets verbosity and forgets to reset it), but I did not succeed.  Also I wonder why one first sees the result and only later sees the protocol.


---

Comment by SimonKing created at 2011-09-28 15:33:47

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-09-28 17:09:21

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-09-28 17:09:21

It turned out that I misinterpreted the error: The actual error was wrong line breaks in the expected warning message. The protocol from Singular is printed to stdout, and apparently it was just by accident (though reproducible) that I saw it in the test log.

Note that the warning message misspells the word "guaranteed" (namely "guarantied"). I fixed that misspelling as well, and I also introduced nicer (I think) line breaks for the warning.

Glad that this is fixed. I hope the tests pass by now.

Apply trac4539_libplural.patch


---

Comment by SimonKing created at 2011-09-28 17:09:21

Changing keywords from "libsingular plural wrapper sd34" to "libsingular plural wrapper sd10 sd23.5 sd24 sd34".


---

Comment by SimonKing created at 2011-09-28 17:48:58

FWIW, all doctests pass for me, except those that fail with unpatched sage-4.7.2.alpha3-prerelease.

By the way: How should reviewing be done in this case? I have no overview who wrote what (i.e., who can _review_ what), and I think many people contributed to it.

In [attachment:trac4539_libplural.patch], I added an author list. But is it exhaustive?


---

Comment by SimonKing created at 2011-09-28 18:19:51

Concerning reviewing: Would it be OK that we all comment whether we are happy with the current patch, and that it constitutes a positive review if all are happy with it and nobody has a veto? Martin seems to agree.


---

Comment by SimonKing created at 2011-09-28 18:33:59

I am writing a reviewer patch, since several doc strings needs reformatting.

Question:

In sage/algebras/free_algebra.py in the method g_algebra, I find the statement:
"By default is assumed, that two variables commute." I don't understand that statement. Is it meant "If there are only two variables then they commute"? Or "Any two variables commute" (hopefully not)? Or "There are two variables that commute" (but which)? Can you provide an example for that default, and also show how (if possible) the default can be overridden?


---

Comment by SimonKing created at 2011-09-28 18:39:16

PS: The other statements

```
        - Coercion doesn't work yet, there is some cheating about assumptions
        - The optional argument ``check`` controls checking the degeneracy conditions.
          Furthermore, the default values interfere with non-degeneracy conditions.
```

aren't clear to  me either. 

 * What does "cheating about assumptions" mean (what are the assumptions)?
 * What exactly does not work in coercion (perhaps I can fix it?)?
 * What are "the default values" (the only default is `order="degrevlex"`)?
 * How do they interfere with non-degeneracy conditions? What are these conditions?


---

Comment by SimonKing created at 2011-09-28 18:39:16

Changing status from needs_review to needs_info.


---

Comment by SimonKing created at 2011-09-28 18:57:44

Too bad. I forgot to apply my "combined" patch relative to #7797 (or at least to #11068). Needs work.


---

Comment by SimonKing created at 2011-09-28 19:03:17

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2011-09-28 19:03:17

I think that it would be better to just have #11068 as a dependency: We should use it (because it implements one- and twosided ideals), and in contrast to #7797 it has a positive review.


---

Comment by SimonKing created at 2011-09-28 19:03:52

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-09-29 00:06:58

Here's a report on features that I implemented today (not posted yet), missing features, and I also have some questions for you:

__Sidedness of ideals__

By #11068, we can have one- and two-sided ideals. Oleksander told me that Singular can only compute left or twosided Gröbner bases. Therefore, I think non-commutative polynomial ideals should refuse to be right-sided. The default should be left ideal. If the ideal is defined as a two-sided ideal, then std should return the same as twostd. Here is an example:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: JL = H.ideal([x^3, y^3, z^3 - 4*z])
sage: JL
Left Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JL.std()
Left Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')
sage: JT
Twosided Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT.std()
Twosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT.std() == JL.twostd()
True
```


I think that's a good solution.

__Cache__

I added a cached_method decorator to std and twostd - I guess it is obvious that the result of a GB computation should be cached.

*Question:* Should g-algebras be unique parents? If you agree that they should be, then I can try to implement it.

__Category__

A proper initialisation of non-commutative polynomial rings in the category of algebras was missing and is now added:

```
sage: H._is_category_initialized()
True
sage: H.category()
Category of algebras over Rational Field
```


__Pickling__

The test suite does not pass. Among other things, pickling of g-algebras has simply been forgotten. This certainly must be fixed:

```
sage: dumps(H)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: expected string or Unicode object, NoneType found
```

It could be that, by using a `UniqueFactory` or `UniqueRepresentation`, the pickling problem automatically vanishes. Otherwise, a `__reduce__` method must be implemented.

__Generator names for g-algebras__

It should be possible to choose names in the `g_algebra()` method.

__Quotients__

There is a custom `quotient()` method for g-algebras (not using #11068). The question is: Is that really a quotient? It isn't printed as such, and the quotient relations are not used in arithmetic nor in comparison:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
sage: Q = H.quotient(I); Q
Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: Q.relations()
{y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: I.twostd()
Twosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: Q.2^2
z^2
sage: Q.2^2 == Q.one_element()
False
```

*Question:* Did I misinterprete it? Hence, is there a way to make Q show that `Q.2^2` is equal to one?

Otherwise, the custom `quotient()` should be dropped. #11068 provides the framework for nc-quotient rings; one just needs to add a `I.reduce(p)` method to our ideals (which is missing anyway).

__Doc strings__

I fixed various wrong doc string formats. Of course, after the changes mentioned above, some doc tests need to be modified.


---

Attachment

Combined patch relative to sage-4.7.2.alpha3 plus #11068 plus #11856


---

Comment by SimonKing created at 2011-09-29 08:11:46

New patch posted! It does what I have announced above. I suggest that the next step should be to provide pickling, possibly by using `UniqueRepresentation`.


---

Comment by SimonKing created at 2011-09-29 10:38:07

The patch that I have just attached provides uniqueness of the parent (using a `UniqueFactory`) and pickling for nc rings and polynomials.

In short:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H is loads(dumps(H))
True
sage: TestSuite(H).run()
```


Doc tests still need to be updated, though. I also think that normal form computation should be easy to implement.

Apply trac4539_libplural.patch trac4539_pickling.patch


---

Attachment

Pickling of nc rings and polynomials


---

Comment by SimonKing created at 2011-09-29 12:35:07

I have updated the second patch (adding a commit message), and I added a third patch. It provides a non-commutative "Gröbner strategy", normal form computation, and thus quotient rings of g-algebras.

Note that the quotients use the general framework from #11068. They _should_ simply be g-algebras as well. But I suggest that this will be done on a different ticket.

With the new patch, one can do:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False, side='twosided')
sage: Q = H.quotient(I); Q
Quotient of Noncommutative Multivariate Polynomial Ring in x, y, z
over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y,
z*x: x*z + 2*x} by the ideal (y^2, x^2, z^2 - 1)
sage: Q.2^2 == Q.one_element()   # indirect doctest
True
```

Here, we see that the relation that we just found in the quotient is actually a consequence of the given relations:

```
sage: I.twostd()
Twosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2)
of Noncommutative Multivariate Polynomial Ring in x, y, z over
Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
```


Note that reduction of polynomials by a list of polynomials is, in general, not a normal form. However, reduction of a polynomial by an ideal uses a two-sided Gröbner basis and is thus a normal form.

I just thought that it would better be reduction by a left Gröbner basis, if the ideal is just a left ideal. OK, doing it soon...

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch


---

Comment by SimonKing created at 2011-09-29 12:39:43

The third patch is now modified, so that reduction wrt a left ideal is computed with a left (not a two-sided) Gröbner basis.

It needs work, since the documentation is not complete and since certainly several doc tests need to be modified. But feel free to test the new patches...


---

Comment by SimonKing created at 2011-09-29 12:53:08

Normal forms, quotient rings, and ideal containment


---

Attachment

Sorry, I couldn't resist to add one more feature: Ideal containment, which is a direct application of normal form computation.

With the new version of the third patch, we have:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: JL = H.ideal([x^3, y^3, z^3 - 4*z])
sage: JL.std()
Left Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')
sage: JT.std()
Twosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
```

Apparently, ``x*y^2-y*z`` should be in the two-sided, but not in the left ideal. And that is indeed what we get:

```
sage: x*y^2-y*z in JL
False
sage: x*y^2-y*z in JT
True
```


Docs are still to fix. And I promise to focus on it - no new features...

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch


---

Comment by SimonKing created at 2011-09-29 15:19:00

The fourth patch does not provide a new feature, but only fixes of bugs, of the doc string formatting, and of the doc tests.

Since I do not have Sage locally, I'd appreciate if one of you could build the documentation and see if it looks nice.

Not a feature, but a fix concerns the hash: If one constructs a g-algebra as one is supposed to (`g_algeba` method resp. unique factory) then the g-algebra is a unique parent. Hence, `id(self)` is a good hash for it, and `__cmp__` can be removed.

Note that the hash in Sage is allowed to change from session to session, so, `id(self)` is fine - see `UniqueRepresentation.__hash__`. Of course, one can destroy the uniqueness on purpose, but that's  not our problem.

Tests in sage/libs/singular, multi_polynomial_ideal.py and plural.pyx pass. I am now running all doc tests, but I think it is OK to put it as "needs review".

Concerning review: I think we should review each other's code. So, in particular, one of you should please review my last three patches.

Please verify if I got the credits (author list) right.

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch


---

Comment by SimonKing created at 2011-09-29 15:19:00

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-09-29 15:45:02

Hoorray, only three errors, in sage/rings/noncommutative_ideal.pyx! That should be doable before dinner.


---

Comment by SimonKing created at 2011-09-29 15:45:02

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-09-29 16:29:25

Fixing doc strings and doc tests


---

Comment by SimonKing created at 2011-09-29 16:32:53

Changing status from needs_work to needs_review.


---

Attachment

It turned out that the element constructor of ideal monoids changed a left ideal into a twosided ideal, which (together with the missing uniqueness of ideal monoids) led to errors in a `loads(dumps(...)==...` test.

I hope all tests will pass by now!

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch


---

Comment by SimonKing created at 2011-09-29 20:52:27

Replying to [comment:83 SimonKing]:
> I hope all tests will pass by now!

They do!


---

Comment by AlexanderDreyer created at 2011-09-29 21:38:00

I checked the patches, the look good indeed. So a positive review for the mathematical part. I'm starting doc tests now.


---

Comment by AlexanderDreyer created at 2011-09-29 22:10:16

Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?
`hg qseries`


---

Comment by SimonKing created at 2011-09-30 06:16:13

Replying to [comment:86 AlexanderDreyer]:
> Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?

```
hg qseries
trac11815_format_must_preserve_embedding.patch
trac11817_question_mark_using_sage_getdoc.patch
trac11768_source_of_dynamic_class.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac11791_dynamic_metaclass_introspection.patch
trac11780_unique_auxiliar_polyring.patch
trac11856_exponent_overflow.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac4539_libplural.patch
trac4539_pickling.patch
trac4539_normal_forms.patch
trac4539_fix_docs.patch
```


So, as you can see, I indeed have more stuff applied in front of the plural patches. I will try to see what went wrong.


---

Comment by SimonKing created at 2011-09-30 08:13:26

I can not confirm Alexander's statement that some patch does not apply.

I cleaned my patch queue, so that I only use the patches that are dependencies. Now, I have

```
$ hg qapplied
trac11815_format_must_preserve_embedding.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac11856_exponent_overflow.patch
trac4539_libplural.patch
trac4539_pickling.patch
trac4539_normal_forms.patch
trac4539_fix_docs.patch
```

on top of sage-4.7.2.alpha3-prerelease.

One remark: It happened to me recently that I tried to qimport a patch from trac, but my university had a proxy, and for some reason it thought that the patch is cached. I therefore switched the cache off, for the computer in my office. That is where I test the patches.

But Burcin just told me that they have a proxy here as well. So, could it be that you tried to download the latest patch version, but your proxy only provided you with a cached but outdated version of the patches?

The other possibility is that I thought I have posted the patch version that I have on my computer in my office, but in fact posted an outdated version that I have on my netbook here. Testing it now.


---

Comment by SimonKing created at 2011-09-30 09:34:11

See #11878 for quotients of g-algebras.


---

Comment by AlexanderDreyer created at 2011-09-30 10:44:29

Replying to [comment:88 SimonKing]:
> I can not confirm Alexander's statement that some patch does not apply.
Yeah, I just mixed up the order of the following patches:
> trac4539_pickling.patch
> trac4539_normal_forms.patch
Already the first didn't apply cleanly, but I overlooked. It built fine and the tests are running.


---

Comment by SimonKing created at 2011-09-30 12:06:54

Changing status from needs_review to needs_info.


---

Comment by SimonKing created at 2011-09-30 12:06:54

I found that the function `new_NRing`, that is supposed to return a valid `NCPolynomialRing_plural` out of a ring wrap, is broken. Important data, namely the matrices c and d, are left as `None`. Hence, for a ring produced with `new_NRing`, pickling won't work at all.

The question is whether we can leave it broken for now, and fix it separately, or leave this ticket open and "needs work". How shall we proceed?


---

Comment by SimonKing created at 2011-09-30 12:08:47

PS: Even _if_ it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.


---

Comment by SimonKing created at 2011-09-30 12:12:09

Replying to [comment:92 SimonKing]:
> PS: Even _if_ it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.

It concerncs the `SCA` function and the original approach towards quotients.


---

Comment by SimonKing created at 2011-09-30 14:44:01

I suggest that we leave stuff as it is now, so that it can be merged and we can build on top of it. Therefore, I revert it to "needs review".

If I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).

I believe that there should be a sub-class of `NCPolynomialRing_plural` for general quotients of g-algebras, and then a sub-sub-class for SCA that uses the specialised implementation from Singular. But that should be on #11878.


---

Comment by SimonKing created at 2011-09-30 14:44:01

Changing status from needs_info to needs_review.


---

Comment by OleksandrMotsak created at 2011-09-30 15:05:17

Replying to [comment:94 SimonKing]:
> If I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).

SCA structure is _autodetected_ upon creation of a GR-algebra (`qring`) in runtime. Therefore one should not use an extra method for this: just create a GRing and its quotient by correct twosided ideal there.

Test: if SCA implementation is used then `y*y == 0;` for each non-commutative (odd degree) variable `y`.


---

Attachment

Fixed one doc test which faild in 32 bit


---

Comment by AlexanderDreyer created at 2011-09-30 21:58:06

One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch. Since we postponed the quotient issue, I think I can give a positive review for Simon's work as well as for Michael's, Burcin's and Oleksandr's part , which I reviewed on SD24.

`@`Simon: If you accept my part we would have a positive review now.


---

Comment by SimonKing created at 2011-10-01 09:02:35

Replying to [comment:96 AlexanderDreyer]:
> One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.

It looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.

> `@`Simon: If you accept my part we would have a positive review now.

The "big" patch merely combines work of y'all, and I certainly give the stuff there a positive review. However, the question on #11856 should first be answered.


---

Comment by SimonKing created at 2011-10-01 09:02:35

Changing status from needs_review to needs_info.


---

Comment by AlexanderDreyer created at 2011-10-01 22:28:03

Replying to [comment:97 SimonKing]:
> Replying to [comment:96 AlexanderDreyer]:
> > One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.
> 
> It looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.
Indeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.


---

Comment by SimonKing created at 2011-10-02 06:38:31

Replying to [comment:98 AlexanderDreyer]:
> Indeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.

OK, then [attachment:trac4539_fix_docs_32bit.patch] should better be moved to #11856 - since it only concerns doctests in the obvious way, but does not change the code, I think that your patch can be a reviewer patch for #11856, thus, preserving the positive review that Martin gave (but then add your name in the "Reviewer" field of #11856).

If that's done, then I'll try the stuff from here again, and then hopefully it can be turned into a positive review.


---

Comment by AlexanderDreyer created at 2011-10-02 21:23:30

Changing status from needs_info to needs_review.


---

Comment by AlexanderDreyer created at 2011-10-02 21:25:30

Now 32 bit issue was solved in #11856 (and has positive review again).


---

Comment by AlexanderDreyer created at 2011-10-02 21:25:30

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-10-04 17:46:15

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-10-04 17:46:15

Too bad. I was asked to rebase #11586 and #11068 with respect  to #11339/#10903. By consequence, the patches from here need to be rebase as well. Needs work...


---

Comment by SimonKing created at 2011-10-04 18:17:11

It is not going to be easy. #11339 and #10903 have removed some functions (eg., `n_IsOne`) that are needed here. So, I need to find out where it was imported from.


---

Comment by malb created at 2011-10-04 18:25:58

`n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)


---

Comment by SimonKing created at 2011-10-04 18:31:07

Replying to [comment:105 malb]:
> `n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)

Yep, I already found the replacement (by doing a grep for `n_IsOne` in my `.hg/patches`, when I wanted to find out where that function came from).


---

Comment by SimonKing created at 2011-10-05 08:04:06

I didn't post my rebased patches yet, since I need to fix a few doctest errors.

Actually, the first error is a clear improvement. We have the following doctest:

```
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: H.inject_variables()
            Defining x, y, z
            sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
            sage: G = vector(I.gens()); G
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            (y^2, x^2, z^2 - 1)
            sage: M = I.syzygy_module()
```


With #10903 applied, one gets 9 Syzygies:

```
sage: M[0]
(-z^2 - 8*z - 15, 0, y^2)
sage: M[1]
(0, -z^2 + 8*z - 15, x^2)
sage: M[2]
(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)
sage: M[3]
(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)
sage: M[4]
(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)
sage: M[5]
(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)
sage: M[6]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[7]
(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)
sage: M[8]
(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)
sage: M[9]
Traceback (most recent call last):
...
IndexError: matrix index out of range
```


However, without #10903 (and with the original patches applied), one gets what is expected in the doc tests, namely 10 Syzygies -- but two of them are identical:

```
sage: M[0]
(-z^2 - 8*z - 15, 0, y^2)
sage: M[1]
(0, -z^2 + 8*z - 15, x^2)
sage: M[2]
(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)
sage: M[3]
(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)
sage: M[4]
(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)
sage: M[5]
(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)
sage: M[6]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[7]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[8]
(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)
sage: M[9]
(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)
sage: M[7]==M[6]
True
```


So, the old Singular version forgot to remove a redundant Syzygy.


---

Attachment

Combined patch relative to sage-4.7.2.alpha3 plus #11068, #11856 and #10903


---

Comment by SimonKing created at 2011-10-05 08:13:10

Pickling of nc rings and polynomials, rel #10903


---

Attachment

Normal forms, quotient rings, and ideal containment, rel #10903


---

Comment by SimonKing created at 2011-10-05 08:20:46

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-10-05 08:20:46

Hoorray! The other doctest error was even easier to fix: It has been a new test, and I simply had a typo in it.

Because of #11339 and #10903, I had to change some lines in the code. In order to make the changes more easily visible, I attached the new patches under a new name, so that you can compare them with the old patches.

Could you please have a look whether we can return to the positive review?

Apply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch


---

Comment by AlexanderDreyer created at 2011-10-05 09:02:00

The patches look sane. I'll test them now (setting up 4.7.2alph3 will last some time).


---

Comment by SimonKing created at 2011-10-05 09:04:35

FWIW, all tests pass for me (starting with the "official version" of sage-4.7.3.alpha3).


---

Comment by AlexanderDreyer created at 2011-10-05 09:13:15

Can you just post the output of `hg qapplied`? this would simplify things for me.


---

Comment by SimonKing created at 2011-10-05 09:19:23

Replying to [comment:111 AlexanderDreyer]:
> Can you just post the output of `hg qapplied`? this would simplify things for me. 

Starting with sage-4.7.2.alpha3 (no prerelease this time):

```
$ hg qapplied
trac_11339_refcount_singular_rings.patch
trac_11339_refcount_singular_polynomials.patch
trac_10903_singular-3-1-3-3.patch
trac_10903_singular-fixes.patch
trac11856_exponent_overflow.patch
trac11856_fix_docs_32bit.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac_11115_reviewer.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac4539_libplural_rel10903.patch
trac4539_pickling_rel10903.patch
trac4539_normal_forms_rel10903.patch
trac4539_fix_docs_rel10903.patch
```



---

Comment by SimonKing created at 2011-10-05 10:36:10

Sorry, I had to produce a new version of the last patch: The first patch has introduced a wrong instance of the `..todo::` markup. The docbuilder complained about it. Since [attachment:trac4539_fix_docs_rel10903.patch] is responsible for fixing the doc strings, I fixed it there.

So, please replace the last patch with the new version, and also try to build the documentation (`sage -docbuild reference html`).


---

Comment by SimonKing created at 2011-10-05 10:40:23

OMG. It seems that I managed to destroy the patch that I have just attached by a patch that I had prepared for #10903. Needs work, for now.


---

Comment by SimonKing created at 2011-10-05 10:40:23

Changing status from needs_review to needs_work.


---

Attachment

Fixing doc strings and doc tests , rel #10903


---

Attachment

Fixing doc strings and doc tests , rel #10903


---

Attachment

Fixing doc strings and doc tests , rel #10903


---

Comment by SimonKing created at 2011-10-05 10:57:59

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-10-05 10:57:59

I urgently need a break. It is unbelievable how many errors I made in the past 30 minutes.

Anyway.

I have now updated the patch (after first attaching a wrong file, followed by the correct file under a wrong name, and those things).

Note that there is now a new patch at #10903 - without that patch, building the documentation would fail.

The new version of [attachment:trac4539_fix_docs_rel10903.patch] fixes one wrongly formatted `.. todo::` directive.

Please test whether the documentation builds fine for you.

Apply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch


---

Comment by AlexanderDreyer created at 2011-10-05 18:18:18

Everything is fine, but one issue: Unfortunately the docbuild contains one uncaught exception (on SuSE 11):


```
sphinx-build -b html -d /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/doctrees/en/reference    /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/en/reference /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference
Running Sphinx v1.0.4
loading pickled environment... done
building [html]: targets for 152 source files that are out of date
updating environment: 1 added, 152 changed, 0 removed
reading sources... [ 99%] sage/symbolic/expression
Exception occurred:
  File "/p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/common/conf.py", line 378, in skip_member
    if (hasattr(obj, '__name__') and obj.__name__.find('.') != -1 and
AttributeError: 'NoneType' object has no attribute 'find'
The full traceback has been saved in /tmp/sphinx-err-RJnoHz.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
Either send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,
or report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!
Build finished.  The built documents can be found in /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference
```


I suggested the reviewer patch: [attachment:trac4539_docbuild_reviewer.patch]

With that patch we are close to a positive review: I'm also running tests on OS X.


---

Attachment

Hi Alexander,

Note that there is a new patch at #10903 (where the docbuild crash was introduced), and it fixes the problem in a more satisfying way. The problem was that under certain circumstances the name of a deprecated Cython method could not be determined - but with the new patch from #10903 (actually there are TWO new patches) the problem is fixed.

So, the docbuild reviewer patch is not needed.


---

Comment by AlexanderDreyer created at 2011-10-06 07:59:16

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2011-10-06 07:59:16

Building, installing and testing succeeded on SuSE 11 Enterprise amd64 and OS X 10.5 ppc. So we can switch back to positive review.


---

Attachment


---

Comment by SimonKing created at 2011-11-08 15:15:44

It could be that we need some work here. The first patch does not apply when we start with sage-4.8.alpha0. Namely, in sage/libs/singular/function.pyx, it expects the line

```
       ring2 = None
```

but this line has been removed. I don't know in which ticket that has happened. By consequence, a rather complicated chunk of the patch does not apply.

What shall we do? In order to avoid premature work, it would be an option to wait until finally all the dependencies got a positive review.


---

Comment by SimonKing created at 2011-11-08 15:15:44

Changing status from positive_review to needs_info.


---

Comment by AlexanderDreyer created at 2011-11-08 22:34:16

That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.) That patch was not merged in alpha0.


---

Comment by SimonKing created at 2011-11-08 23:00:01

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2011-11-08 23:00:01

Replying to [comment:123 AlexanderDreyer]:
> That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.)

Yes, now I see it: #11761 is a dependency! So, sorry for the noise, and back to a positive review - which needs two steps. One...


---

Comment by SimonKing created at 2011-11-08 23:00:31

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-11-08 23:00:31

... and two.


---

Comment by jdemeyer created at 2012-01-21 23:39:13

Resolution: fixed
