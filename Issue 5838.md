# Issue 5838: crash in Singular's polynomial gcd

Issue created by migration from https://trac.sagemath.org/ticket/5838

Original creator: cwitty

Original creation time: 2009-04-20 21:07:49

Assignee: malb

CC:  malb

Here's what I type to provoke the crash:

```
std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage.structure.sage_object.unpickle_all(std)
sage.structure.sage_object.unpickle_all(std)
```

(this is the doctest of unpickle_all, plus an extra repetition of the second line)

Here's the output:


```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
/home/cwitty/sage-3.4.1.rc3/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
  exec code_obj in self.user_global_ns, self.user_ns
Successfully unpickled 483 objects.
Failed to unpickle 0 objects.
sage: sage.structure.sage_object.unpickle_all(std)
/home/cwitty/sage-3.4.1.rc3/local/bin/sage-sage: line 198: 22270 Aborted                 sage-ipython "$@" -i
```


The first section of the backtrace is:


```
#0  0x00007fc7c14c2105 in raise () from /lib/libc.so.6
#1  0x00007fc7c14c3623 in abort () from /lib/libc.so.6
#2  0x00007fc7bcedd6d8 in global_NTL_error_callback ()
   from /home/cwitty/sage-3.4.1.rc3/local/lib/libcsage.so
#3  0x00007fc7bc9451ef in NTL::Error (
    s=0x7fc7bc97def1 "InvMod: inverse undefined") at tools.c:38
#4  0x00007fc7bc88ebd9 in NTL::InvMod (a=<value optimized out>, n=244)
    at ZZ.c:351
#5  0x00007fc7bc90545f in NTL::PlainRem (r=@0x7fffca29e230, a=@0x7fffca29e230, 
    b=@0x6) at ../include/NTL/lzz_p.h:278
#6  0x00007fc7bc9140bb in NTL::GCD (d=@0x7fffca29e360, 
    u=<value optimized out>, v=@0x7fffca29e390) at lzz_pX1.c:558
#7  0x00007fc7a963206a in gcd_poly_p (f=@0x7fffca29e9e0, g=@0x7fffca29e9d0)
    at /home/cwitty/sage-3.4.1.rc3/local/include/NTL/lzz_pX.h:696
#8  0x00007fc7a9633835 in gcd_poly (f=<value optimized out>, g=@0x7fffca29ee50)
    at cf_gcd.cc:538
#9  0x00007fc7a963401e in gcd (f=@0x7fffca29ee60, g=@0x7fffca29ee50)
    at cf_gcd.cc:776
#10 0x00007fc7a9634601 in gcd_test_one (f=@0x7fffca29f3b0, g=@0x7fffca29f3c0, 
    swap=true) at cf_gcd.cc:76
#11 0x00007fc7a9631b70 in gcd_poly_p (f=@0x7fffca29f7b0, g=@0x7fffca29f7a0)
    at cf_gcd.cc:353
#12 0x00007fc7a963373d in gcd_poly (f=<value optimized out>, g=@0x7fffca29fbb0)
    at cf_gcd.cc:543
#13 0x00007fc7a9635d89 in chinrem_gcd (FF=<value optimized out>, 
    GG=<value optimized out>) at cf_gcd.cc:1088
#14 0x00007fc7a96337e1 in gcd_poly (f=<value optimized out>, g=@0x7fffca2a0560)
    at cf_gcd.cc:601
#15 0x00007fc7a963401e in gcd (f=@0x7fffca2a0550, g=@0x7fffca2a0560)
    at cf_gcd.cc:776
#16 0x00007fc7a94a69f8 in singclap_gcd (f=0x7fc7a930b198, g=0x7fc7a930b058)
    at clapsing.cc:230
#17 0x00007fc7a992d2f9 in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd (__pyx_v_self=0x5e60830, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:31063
#18 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)
    at Objects/abstract.c:1861
#19 0x00007fc7b3aaf02f in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement_reduce (__pyx_v_self=0x5e5e2d0, unused=<value optimized out>)
    at sage/rings/fraction_field_element.c:2288
#20 0x00000000004187e3 in PyObject_Call (func=0x58ad, arg=0x58ad, kw=0x6)
    at Objects/abstract.c:1861
#21 0x00007fc7b3aa3b2b in __pyx_pf_4sage_5rings_22fraction_field_element_20FractionFieldElement___init__ (__pyx_v_self=0x5e5e2d0, 
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>)
    at sage/rings/fraction_field_element.c:1905
```




---

Comment by Bouillaguet created at 2013-01-27 08:07:54

Looking a bit further into it, the actual pickles that trigger the problem are those in `sage.combinat.sf.macdonald`. Namely, if these ones are removed from the pickle jar, then the problem disappears...


---

Comment by rws created at 2014-04-14 13:52:47

As an update, because the system changed since, the commands to trigger this are:

```
sage: import os
sage: std = os.environ['SAGE_SHARE'] + '/sage/ext/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
sage: sage.structure.sage_object.unpickle_all(std)
```



---

Comment by rws created at 2014-08-11 06:07:23

The output of the code in comment:4 is now

```
Successfully unpickled 586 objects.
Failed to unpickle 0 objects.
```

which I guess is OK.


---

Comment by rws created at 2014-08-11 06:07:23

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-08-11 11:45:38

Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?


---

Comment by rws created at 2014-08-11 15:26:48

Changing priority from critical to major.


---

Comment by rws created at 2014-08-11 15:26:48

Replying to [comment:8 pbruin]:
> Wouldn't it make sense to add a doctest for this, to make sure that it stays fixed?
Of course, thanks for the hint.
----
New commits:


---

Comment by jakobkroeker created at 2014-08-11 15:38:12

Question: 

why there was a crash in Singular's polynomial gcd and how it got fixed?

It is not obvious for me...( I'm new to sage and do not yet understand everything)


---

Comment by rws created at 2014-08-11 15:45:25

Replying to [comment:11 jakobkroeker]:
> Question: 
> 
> why there was a crash in Singular's polynomial gcd and how it got fixed?
> 
> It is not obvious for me...( I'm new to sage and do not yet understand everything)

The crash was quite old (5 years ago) and presumably happened because of an old Singular version. This triggered an unpickling crash. Pickling is the Python name for serialization, see https://en.wikipedia.org/wiki/Serialization

I admit the doctest tests the unpickling issue, i.e., the symptom not the cause. OTOH it has the potential to catch a lot of other bugs. The bug itself was probably fixed by a newer Singular version.


---

Comment by jakobkroeker created at 2014-08-11 17:49:52

Q: should the tag 'long time' be added to the test?


---

Comment by jdemeyer created at 2014-08-11 18:48:56

You must certainly remove the ` # not tested`, otherwise you are just testing once, not twice...


---

Comment by jdemeyer created at 2014-08-11 18:49:02

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-08-12 07:18:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-08-12 07:19:27

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-08-12 07:19:27

Done, thanks.


---

Comment by pbruin created at 2014-08-12 17:11:14

The new commit moves the new doctest after the existing one testing the plain `unpickle_all()` command, for clarity and to save one run of `unpickle_all()`.  Setting the location of the pickle jar (`std`) probably had to be done by hand in earlier versions, but now one can just omit the `dir` argument.  I also made the explanation slightly more explicit.  If you agree with the changes, you can set it to positive review; if not, you can just put back your branch.


---

Comment by rws created at 2014-08-13 07:01:05

Yes, much clearer, thanks.


---

Comment by rws created at 2014-08-13 07:01:05

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-13 17:06:44

Resolution: fixed


---

Comment by jakobkroeker created at 2014-08-14 09:17:25

Assuming, I understand everything correctly..

 `@`pbruin

 The commit
 http://git.sagemath.org/sage.git/commit/?id=87d608a0d1cb1dc78186e89e46c3c651b6711090

 does not what Ralph Stephan intended,
 namely unpickle the 'pickle_jar.tar.bz2'

 `@`rws did you not notice that?


---

Comment by rws created at 2014-08-14 09:25:14

Hm, I thought the double unpickling was the issue tested but now I'm not sure anymore...


---

Comment by jakobkroeker created at 2014-08-14 09:30:58

I didn't understand everything correctly. 
Unpickling of pickle_jar.tar.bz2 _is_ checked by the doctest
and everyhing is fine.


---

Comment by jakobkroeker created at 2014-08-25 20:44:35

Hello,

this test fails on a dated gentoo(?) install
with error

```
**********************************************************************
File "src/sage/structure/sage_object.pyx", line 1411, in sage.structure.sage_object.unpickle_all
Failed example:
    sage.structure.sage_object.unpickle_all()  # (4s on sage.math, 2011)
Expected:
    doctest:... DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    *** The old options style (`tar fx ...`) is highly discouraged, please use the modern form (leading dash before options).
    *** The standard way (with expanded options; you can still bundle options) for your command would be: tar -f - -x
    doctest:1: DeprecationWarning: OrderedAlphabet is deprecated; use Alphabet instead.
    See http://trac.sagemath.org/8920 for details.
    doctest:843: DeprecationWarning: This class is replaced by Matrix_modn_dense_float/Matrix_modn_dense_double.
    See http://trac.sagemath.org/4260 for details.
    Successfully unpickled 586 objects.
    Failed to unpickle 0 objects.
```

any idea how to fix it ?


---

Comment by leif created at 2016-07-31 21:18:37

The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).

Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).

(Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.


---

Comment by leif created at 2016-08-01 04:46:50

Replying to [comment:25 leif]:
> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).
> 
> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).
> 
> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.
\\

And the winners (apparently) are:

  `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`

(When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)


---

Comment by leif created at 2016-08-01 05:45:05

Don't know yet who's to blame (on Sage's side, perhaps Singular's), but I can pretty well imagine what's happening here; the only difference between MPIR and GMP here being that the latter reuses user-freed memory regions earlier than the former does.

Will investigate later, haven't looked at the code yet.


---

Comment by leif created at 2016-08-01 06:18:34

Replying to [comment:26 leif]:
> And the winners (apparently) are:
> 
>   `_class__sage_combinat_sf_macdonald_MacdonaldPolynomials_*.sobj`
> 
> (When I skip these six, I can successfully `unpickle_all()` as often as I want in a row.)

To no surprise, these objects / classes have been added shortly before Carl Witty reported the issue (for Sage 3.4.1.rc3):

```
type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_ht'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the Ht basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_h'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the H basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_j'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the J basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_p'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the P basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_q'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the Q basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'

type(obj) = <class 'sage.combinat.sf.macdonald.MacdonaldPolynomials_s'>
version = 3.4.rc1
obj =
'Macdonald polynomials in the S basis over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field'
```



---

Comment by leif created at 2016-08-09 15:37:30

Replying to [comment:25 leif]:
> The second attempt to unpickle all crashes with both GMP 5.1.3, the current version in Sage, and GMP 6.1.1, in exactly the same manner as in the ticket description, with GCC 5.4.0, 6.1.0, and also Sage's GCC 4.9.3 (on Linux x86_64 at least).
> 
> Sage version 7.3.rc0 (NTL meanwhile at 9.8.1.p1, Singular still 3.1.7p1.p1).
> 
> (Presumably just incidentally) doesn't happen with Sage's MPIR, currently 2.7.2.

Indeed, since the above failure incidentally vanishes with #21188. (So far only tried with GMP 5.1.3 and GCC 4.9.3 though.)

I.e., when building Sage / Singular with GMP, a `configure` test for FLINT in Singular failed because it used `-lmpir`, such that Singular and libsingular "silently" got built without using FLINT.


---

Comment by leif created at 2016-08-09 15:55:55

Changing keywords from "" to "sage_object unpickle_all() NTL::InvMod abort inverse undefined".


---

Comment by dimpase created at 2017-04-14 16:22:52

I am seeing this doctest (2nd unpickling) failing on FreeBSD (see #22679).

This might be due to some toolchain issues I have there ATM (I see mysterious errors in sympow, depending upon unrecognised compiler options passed, or not...).
