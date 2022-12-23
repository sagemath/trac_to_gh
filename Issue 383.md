# Issue 383: quo_rem in the polynomial rings does not use canonical coercion

Issue created by migration from https://trac.sagemath.org/ticket/383

Original creator: jbmohler

Original creation time: 2007-06-01 15:24:59

Assignee: somebody

I'm looking at the polynomial function quo_rem and I see that it does it's own
coercion manually.  This feels a little wrong to me.  I think it should go
through the standard coercion routines.  Here's a "bug" that results:


```
sage: x=ZZ['x'].0
sage: y=QQ['x'].0
sage: (y+1).quo_rem(1/2*x)
(2, 1)
sage: (x+1).quo_rem(1/2*y)
...
<type 'exceptions.TypeError'>: no coercion of this rational to integer
```


The bug is that I don't see why these two things are treated substantially
differently.  The reason I found this is because the simple "TypeError"
exception did not provide the usual message about parents being
mis-matched -- I think this is a bug in itself

The fix for all that is to make the quo_rem stuff use canonical coercion model.

All of the quo_rem instances in sage/rings/polynomial/polynomial_element_generic.py suffer from some sort of coercion impropriety.


---

Comment by robertwb created at 2010-01-17 08:34:01

Changing status from new to needs_review.


---

Comment by was created at 2010-01-17 10:14:19

Typo:  arithmatic  --> arithmetic


---

Attachment

Oops. Thanks, fixed.


---

Comment by was created at 2010-01-17 10:49:45

I read the code.  Looks AWESOME!

It appears to expose numerous issues:


```

sage -t devel/sage/sage/rings
...

The following tests failed:

        sage -t  devel/sage/sage/rings/finite_field_element.py # 3 doctests failed
        sage -t  devel/sage/sage/rings/tests.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/finite_field_ext_pari.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/fraction_field_element.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/residue_field.pyx # 3 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_zmod_flint.pyx # 5 doctests failed
        sage -t  devel/sage/sage/rings/number_field/number_field_ideal.py # 2 doctests failed
----------------------------------------------------------------------
Total time for all tests: 192.3 seconds

[1]+  Done                    ./sage -tp 10 devel/sage/sage/rings > 383.out
wstein@boxen:~/build/sage-4.3.1.rc0$ pwd
/home/wstein/build/sage-4.3.1.rc0
wstein@boxen:~/build/sage-4.3.1.rc0$ ls
383.out   6207.out~    data   dist      install.log  local     README.txt  sage-python          spkg      tmp
6207.out  COPYING.txt  devel  examples  ipython      makefile  sage        sage-README-osx.txt  test.log
wstein@boxen:~/build/sage-4.3.1.rc0$ pwd
/home/wstein/build/sage-4.3.1.rc0
wstein@boxen:~/build/sage-4.3.1.rc0$
```



---

Attachment


---

Comment by robertwb created at 2010-01-17 11:41:19

OK, I've fixed all the above doctests issues.


---

Comment by was created at 2010-01-19 06:57:19

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-19 06:57:19

Ut oh:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/crypto/classical.py # 14 doctests failed
        sage -t  devel/sage/sage/modular/etaproducts.py # 24 doctests failed
        sage -t  devel/sage/sage/structure/element.pyx # 1 doctests failed
        sage -t  devel/sage/sage/libs/pari/gen.pyx # Segfault
        sage -t  devel/sage/sage/modular/arithgroup/arithgroup_generic.py # 4 doctests failed
        sage -t  devel/sage/sage/modular/arithgroup/congroup_gamma0.py # 2 doctests failed
        sage -t  devel/sage/sage/quadratic_forms/quadratic_form__split_local_covering.py # 2 doctests failed
        sage -t  devel/sage/sage/modular/cusps.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 478.6 seconds
wstein@boxen:~/build/sage-4.3.1.rc0-boxen-x86_64-Linux$
```



---

Attachment

OK, I've doctested the entire sage library this time.


---

Comment by robertwb created at 2010-01-19 12:16:57

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-19 12:44:22

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 20:26:08

Resolution: fixed
