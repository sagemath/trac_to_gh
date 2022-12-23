# Issue 6559: Real domain for symbolic variables

Issue created by migration from https://trac.sagemath.org/ticket/6559

Original creator: gmhossain

Original creation time: 2009-07-19 11:10:52

In new symbolics, the default symbolic variables are complex.
However, sometime it is useful/desirable to make the domain of
variables to be real.


Currently, there are no way to specify the domain of variables
in Sage although underlying Ginac allows it.  For example: following
would to be good to have.

```
sage: var('x,y,z', domain='real')
```



---

Comment by mvngu created at 2009-08-22 14:17:46

#6802 is a duplicate of this ticket.


---

Attachment


---

Comment by awebb created at 2009-11-19 17:54:48

How does this relate to pynac 0.1.9 which is in Sage 4.2.1? ~ Adam


---

Comment by rossk created at 2010-01-14 03:56:27

Applied patch and the following errors were returned:


```
applying trac_6559-domain-and-latex_name-for-variable.patch
patching file sage/calculus/var.pyx
Hunk #1 FAILED at 0
Hunk #2 FAILED at 8
Hunk #4 FAILED at 81
3 out of 4 hunks FAILED -- saving rejects to file sage/calculus/var.pyx.rej
patching file sage/symbolic/pynac.pyx
Hunk #1 FAILED at 454
Hunk #2 FAILED at 504
2 out of 2 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej
patching file sage/symbolic/ring.pyx
Hunk #6 succeeded at 769 with fuzz 1 (offset -2 lines).
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6559-domain-and-latex_name-for-variable.patch
```



---

Comment by rossk created at 2010-01-14 03:56:27

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-01-18 02:43:22

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-01-18 02:44:03

Changing status from needs_review to needs_work.


---

Attachment

rebased to 4.3.1.rc0


---

Comment by burcin created at 2010-01-19 14:38:15

Changing keywords from "" to "pynac".


---

Attachment

I uploaded a revised version of Golam's patch at attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch, and a referee patch at attachment:trac_6559-referee.patch.

The changes in the revised patch over Golam's version are
 * rebased to 4.3.rc0
 * removed `sage.symbolic.ring.SR.new_var()` and `sage.symbolic.ring.is_ComplexVariable()` functions. The first is same as `SR.symbol()` and I don't see a use for the second, since all variables are complex. :)
 * removed pickling changes in sage.symbolic.expression.Expression, since unpickling in this case could create a new variable with the same name as an existing one, but with a different domain. This would lead to rather confusing situations.

The referee patch reorganizes the new code a little to make it more efficient. Apparently the new variable creation is an important operation and being sloppy here greatly increases doctest timings. It also adds new methods like `_is_positive()`, `_is_real()` to the expression class to allow querying for more properties.

Only the patches 
 * attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch and
 * attachment:trac_6559-referee.patch 
should be applied.

This ticket depends on the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

which in turns depends on the patches at #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).

The changes here seem to slow down the maxima interface dramatically, so I'm leaving this as needs work for now.


---

Comment by burcin created at 2010-01-20 04:11:21

Changing status from needs_work to needs_review.


---

Attachment

New patches up, ready for review.

Apply only:
 * attachment:trac_6559-domain-and-latex_name-for-variable.take2.3.patch
 * attachment:trac_6559-referee.take2.patch

Depends on the pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

and the tickets #7822, #7876, #7363, #7955, #7957, #7916 and #6465 (in that order).


---

Comment by jason created at 2010-01-21 01:44:14

I applied the patches in this order:


```
$ hg qseries
trac_7999-encoding.patch
trac_6961-psi.patch
trac_7822-py_log.take2.patch
trac_7876-pynac_print.take2.patch
trac_7363-mul_coeff.patch
trac_7955-integrate_latex.patch
trac_7957-pynac_exceptions.patch
trac_7916-same_name_method.take2.patch
trac_6465-chain_rule.take2.patch
trac_6465-moves-integration-into-sfunction-subclass.take2.patch
trac_6465-integral.patch
trac_6559-domain-and-latex_name-for-variable.take2.3.patch
trac_6559-referee.take2.patch
```


There's only one failure (sage -tp, not long) in arith.py, which is a documentation thing and unrelated to this ticket.


---

Comment by kcrisman created at 2010-01-27 19:21:20

Is it likely that the rebase referred to in #6961 might affect other patches than just that one?  Read that before refereeing, in any case.


---

Comment by kcrisman created at 2010-01-27 20:10:50

I can't even begin to say where these are from... but 

```
sage/misc/citation.pyx", line 60:
    sage: get_systems('integrate(x^2, x)')
Expected:
    ['ginac', 'Maxima']
Got:
    ['MPFI', 'ginac', 'Maxima']
```


```
sage/symbolic/random_tests.py", line 206:
    sage: random_expr(5, verbose=True)
Expected:
    About to apply <built-in function add> to [v1, v1]
    About to apply <built-in function div> to [-1/3, 2*v1]
    -1/6/v1
Got:
    About to apply <built-in function add> to [v1, v1]
    About to apply <built-in function div> to [94, 2*v1]
    47/v1
```

seem to be related to just random changes in 4.3.1, while 

```
sage/functions/generalized.py", line 239:
    sage: t.subs(x=1)
Expected:
    2
Got:
    heaviside(x) + 1
```

and a few friends seem to be related to something in pickling changing (I get no other errors with things like that).

In addition, I am getting quite a few segfaults when testing against 4.3.1. 

```
 Desktop/sage-4.3.1/sage -t devel/sage/sage/calculus/calculus.py devel/sage/sage/functions/piecewise.py devel/sage/sage/plot/plot.py devel/sage/sage/symbolic/expression.pyx devel/sage/sage/misc/functional.py devel/sage/sage/symbolic/relation.py devel/sage/sage/symbolic/assumptions.py devel/sage/sage/calculus/wester.py devel/sage/sage/calculus/functional.py 
}}} 
all do. Probably I should not have applied all patches at once, but I was impatient :)


---

Comment by kcrisman created at 2010-01-28 21:12:06

Update: None of the previous errors happen in this symbolics queue until I hit this ticket, so they are definitely due to this one.

More comments:  

1. The original patch only causes the sage/functions/generalized.py doctest errors, not the other two.  It did not appear with all patches up through ticket #6465.

2. The original patch does NOT cause massive slowdown or segfaults in doctesting sage/calculus/calculus.py.

So perhaps the referee patch has changed something weird?


---

Comment by kcrisman created at 2010-01-29 03:05:03

Followup:

Adding the referee patch causes a number of segfaults in things relating to assumptions.  For example, the calculus/calculus.py doctest where it is assumed that abs(q)<1, and the one in calculus/wester.py where it is assumed that x>=y, y>=z, z>=x.    It is not consistent whether the assumption itself or the thing using the assumption causes the hang.  Is it possible that the _is_* methods or the info flags in ginac/decl.pxi are responsible?  This is a question out of ignorance; I don't see how they would interfere with Maxima or the use of it by (e.g.) symbolic_sum, but it's all I can think of.

Also, the citation.pyx and random_tests.py are repeatable.


---

Comment by kcrisman created at 2010-01-29 03:05:03

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-01-31 21:32:32

I can't reproduce these problems on my 64-bit laptop with Sage 4.3.2.alpha0, gcc 4.3.4. I'll try on a 32-bit machine tomorrow.

Note that the rebased patch on #6961 applies without problems to a clean 4.3.2.alpha0 here. Though my patch queue contains `trac_7822-py_log.take2.patch` before `trac_6961-psi.rebased.patch`. I tested the rest of the queue when I rebased the patch for #6961, there weren't any problems.

Is it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?


---

Comment by burcin created at 2010-02-03 11:59:47

I cannot reproduce these problems on a 32-bit Debian Lenny box after applying all the symbolics patches and updating pynac to version 0.11.


---

Comment by kcrisman created at 2010-02-04 03:27:05

> Is it possible that the problems you report might be caused by the fact that your tree got messed up by the git style patches attached to #6465?

Possibly, but wouldn't that have made everything not work, as opposed to just a few weird segfaults related to assumptions and a couple other things? 

Also, when I say I applied them all at once, what I mean is I applied them one after the other using hg_sage.import_patch, which I believe is equivalent to hg import.


---

Comment by burcin created at 2010-02-04 09:25:12

I tried once more with the patches downloaded from trac. I cannot reproduce any problems.

Here is an easier way to test all the patches:

 * Make a fresh clone, called "pynac"
 * go to the source tree for the clone


```
cd $SAGE_ROOT/devel/sage-pynac
```

 * download this tar file


```
wget http://boxen.math.washington.edu/home/burcin/pynac/pynac_patches.tar.bz2
```

 * extract it to the queue repository


```
cd .hg
tar jxvf ../pynac_patches.tar.bz2
cd ..
```

 * apply all the patches


```
hg qpush -a
```


 * if the new pynac package is not already installed download and install it


```
http://boxen.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg
```


 * rebuild Sage


```
./sage -br
```


 * run tests


```
./sage -tp 3 devel/sage-pynac/sage/{symbolic,calculus,functions}
```



---

Comment by burcin created at 2010-02-04 09:25:12

Changing status from needs_work to needs_review.


---

Comment by rossk created at 2010-02-13 05:34:36


```
applying trac_7822-py_log.take2.patch
applying trac_6961-psi.rebased.patch
applying trac_7876-pynac_print.take2.patch
applying trac_7363-mul_coeff.patch
applying trac_7955-integrate_latex.patch
applying trac_7957-pynac_exceptions.patch
applying trac_7916-same_name_method.take2.patch
applying trac_6465-chain_rule.take2.patch
applying trac_6465-moves-integration-into-sfunction-subclass.take2.patch
patching file sage/misc/functional.py
Hunk #1 FAILED at 662
1 out of 2 hunks FAILED -- saving rejects to file sage/misc/functional.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6465-moves-integration-into-sfunction-subclass.take2.patch
```



---

Comment by burcin created at 2010-02-13 10:56:10

See comment:19:ticket:6465. Two patches on that ticket needed to be rebased to 4.3.2. Unfortunately, I didn't have time to update the patch tarball.

You can use `hg qdelete <patch_name>` to remove the offending patches from the queue, and `hg qimport` new ones. The specific list of command to be executed is:


```
cd $SAGE_ROOT/devel/sage-pynac
hg qpop -a
hg qdelete trac_6465-moves-integration-into-sfunction-subclass.take2.patch
hg qdelete trac_6465-integral.take3.patch
hg qgoto trac_6465-chain_rule.take2.patch
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-integral.take4.patch
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch
hg qpush -a
```


Then rebuild sage, and proceed with the tests...

Many thanks for looking at this.


---

Comment by rossk created at 2010-02-13 12:13:56

The hg qgoto didnt work. (And if its easier at any stage to blow away the pynac clone and start again, feel free to suggest that). 

```
rossk@sage:/scratch/rossk/sage-4.3.3.alpha0-sage.math.washington.edu-x86_64-Linux/devel/sage-pynac$ hg qgoto trac_6465-chain_rule.take2.patch
applying trac_7822-py_log.take2.patch
applying trac_6961-psi.rebased.patch
applying trac_7876-pynac_print.take2.patch
applying trac_7363-mul_coeff.patch
applying trac_7955-integrate_latex.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 1710
Hunk #2 FAILED at 1719
Hunk #3 FAILED at 1742
Hunk #4 FAILED at 1771
Hunk #5 FAILED at 1781
Hunk #6 FAILED at 1790
6 out of 6 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7955-integrate_latex.patch
```



---

Comment by burcin created at 2010-02-13 13:26:42

Hi Ross,

The last output you posted doesn't make sense to me. Did you update to 4.3.3.alpha0 since comment:18? In comment:18, the output shows that `trac_7955-integrate_latex.patch` applies cleanly. I don't see any other reason why it would fail now.

I don't have a working copy of 4.3.3.alpha0 yet. Unfortunately, it will take me a couple of days update to that.


---

Comment by rossk created at 2010-02-13 13:44:29

Youre right - made a minor mistake so I had to start again and I could only find a version of 4.3.3.alpha0 easily and I used that (apologies). To get some testing done sooner than later Ill go back to 4.3.3 for now. Thanks.


---

Comment by burcin created at 2010-02-15 00:55:11

:) Ticket #7955 was merged in 4.3.3.alpha0, so it's natural that the patch fails. If you just do


```
hg qdelete trac_7955-integrate_latex.patch
```


the rest of the patches should apply without problems.

Thanks again for your time.


---

Comment by mvngu created at 2010-02-18 21:31:03

Looks good to me. See #6961 for the order in which to merge patches.


---

Comment by mvngu created at 2010-02-18 21:31:03

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 21:53:42

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:53:42

Merged in this order:

 1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch)
 1. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)
