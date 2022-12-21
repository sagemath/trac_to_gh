# Issue 6699: [with spkg; needs review] Update to Maxima 5.19.0 (particularly important for Solaris support).

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-09 07:53:37

Assignee: tbd

I've made a new .spkg file for Maxima based on the latest 5.19.0 release. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg

I gather updates to Maxima have caused some issues in the past in Sage, so I don't know how this will go. 

I've also created a new .spkg file for ECL, based on the latest 9.8.1 source code (despite the fact the web site shows 9.7.1 as the latest, if you go to the downloads page, you can get 9.8.1). 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/ecl-9.8.1.spkg

This updated ECL resolves Trac #6564, as ECL 9.8.1 works on Solaris SPARC, but ECL 9.7.1 does not.  

If the updated ECL is applied (so solving #6564), Maxima *must* be updated, as improved type-check in ECL has found a bug that existed in Maxima for 35 years! (confirmed by Maxima developers). 

So in summary

 * An update to ECL 9.8.1 is needed for Solaris SPARC, as 9.7.1 will not build. (Track #6564)
 * ECL 9.8.1 refuses to build Maxima due to a Maxima bug.
 * This new .spkg for Maxima is necessary in order that Maxima can be used on Solaris. 

This suggests to me that if there are issues in Sage with this latest Maxima, they should be resolved. There is no point staying with an old version of Maxima, which needs an old version of ECL, which will not build on Solaris. 

I appreciate things might not be as simple as that. 

Dave 




---

Comment by AlexGhitza created at 2009-08-16 05:52:26

Changing assignee from tbd to mabshoff.


---

Comment by AlexGhitza created at 2009-08-16 05:52:26

Changing component from algebra to packages.


---

Comment by awebb created at 2009-08-17 09:54:37

Starting from sage 4.1.1, I installed ecl-9.8.3.spkg and maxima-5.19.0.spkg. The following errors occurred.


```
sage -t -long -optional "devel/sage-myver/sage/interfaces/maxima.py"
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 116:
    sage: a.expand()
Expected:
    29*sqrt(2)+41
Got:
    3*2^(7/2)+5*sqrt(2)+41
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 227:
    sage: A.eigenvectors()
Expected:
    [[[0,4],[3,1]],[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3],[1,2,3,4]]
Got:
    [[[0,4],[3,1]],[[[1,0,0,-4],[0,1,0,-2],[0,0,1,-4/3]],[This is the Trac macro *1,2,3,4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,3,4-macro)]]
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 275:
    sage: maxima("laplace(diff(x(t),t),t,s)")
Expected:
    s*?%laplace(x(t),t,s)-x(0)
Got:
    s*'laplace(x(t),t,s)-x(0)
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 280:
    sage: maxima("laplace(diff(x(t),t,2),t,s)")
Expected:
    -?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s
Got:
    -?%at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 426:
    sage: t.limit(Ax=0,dir='above')
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(By^2+Bx^2>0)' before integral or limit evaluation, for example):
    Is By^2+Bx^2  positive or zero?
Got:
    0
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 824:
    sage: maxima._command_runner('describe', 'gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/defsystem.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/cmp.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 845:
    sage: maxima.help('gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/defsystem.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/cmp.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 855:
    sage: maxima.example('arrays')
Expected:
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
Got:
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/defsystem.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/cmp.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/sysfun.lsp"
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
    <BLANKLINE>
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 892:
    sage: sorted(maxima.completions('gc', verbose=False))
Expected:
    ['gc', 'gcd', 'gcdex', 'gcfactor', 'gcprint', 'gctime']
Got:
    ['propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)']
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 907:
    sage: sorted(maxima._commands(verbose=False))
Expected:
    ['Alpha',
     'Beta',
     ...
     'zunderflow']
Got:
    ['propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)', 'propos:Theargumenthastobeastring.--anerror.Todebugthistrydebugmode(true)']
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 926:
    sage: 'gcd' in t
Expected:
    True
Got:
    False
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 1169:
    sage: maxima.version()
Expected:
    '5.16.3'
Got:
    'Loading'
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 1994:
    sage: f.numer()         # I wonder how to get a real number (~1.463)??
Expected:
    -.8862269254527579*%i*erf(%i)
Got:
    1.462651745907182
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 2174:
    sage: 'gcd' in m.trait_names()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 2274:
    sage: m.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/defsystem.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/cmp.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 2285:
    sage: maxima.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/defsystem.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/cmp.fas"
    ;;; Loading #P"/home/adamwebb/local/sage/local/lib/ecl-9.8.3/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/interfaces/maxima.py", line 2667:
    sage: maxima_version()
Expected:
    '5.16.3'
Got:
    'Loading'
**********************************************************************
13 items had failures:
   5 of  95 in __main__.example_0
   1 of   3 in __main__.example_12
   1 of   3 in __main__.example_13
   1 of   3 in __main__.example_14
   1 of   3 in __main__.example_16
   1 of   3 in __main__.example_17
   1 of   5 in __main__.example_18
   1 of   3 in __main__.example_29
   1 of  10 in __main__.example_59
   1 of   4 in __main__.example_68
   1 of   4 in __main__.example_72
   1 of   3 in __main__.example_73
   1 of   4 in __main__.example_93
***Test Failed*** 17 failures.
For whitespace errors, see the file /home/adamwebb/local/sage/tmp/.doctest_maxima.py
	 [17.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -optional "devel/sage-myver/sage/interfaces/maxima.py"
Total time for all tests: 17.9 seconds
```


It appears that the output from maxima has changed in a number of cases and is returning more comments and the like. I don't know if this is the correct/new behaviour of maxima. 

Adam


---

Comment by AlexGhitza created at 2009-08-17 10:06:12

So it seems that a number of doctests need to be fixed.  I'm marking this as "needs work", although the spkg itself seems fine, we just need a patch that fixes the doctests.

Note that interfaces/maxima.py is most likely not the only file affected by this.


---

Comment by drkirkby created at 2009-08-21 05:59:49

After creating this ticket, a newer Maxima was released. The spkg can be found here

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.1/


---

Comment by AlexGhitza created at 2009-08-21 13:03:38

I'm attaching a patch that fixes all but one of the doctest failures observed on sage.math and other Linux machines.

Most of these are very simple fixes due to (a) change of formatting of Maxima output or (b) new functionality in Maxima.  For anything else I have tried to comment on my fix in the corresponding file.  Where new answers appear due to new functionality, I checked these answers against Wolfram Alpha (yes, I know; I feel weird about this).

As far as I know there is one remaining doctest failures:


```
sage -t  "expression.pyx"                                   
**********************************************************************
File "/opt/sage-4.1.1/devel/sage-main/sage/symbolic/expression.pyx", line 5541:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Expected:
    [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
Got:
    [Q == 1/sqrt(sqrt(2) + 1)]
**********************************************************************
```


I think this is due to the fact that Maxima now only returns the real solution, and ignores the complex solution.  I'm not sure what we should do about this.


Note that there are also some timeouts observed by David Kirkby on Solaris, but at least some of them are not Maxima-related so it would be better to deal with them in separate tickets.

Finally, this patch puts together a number of tiny patches on a number of recently-opened tickets.  I've decided that it is quite a bit easier to just referee the whole thing, and definitely easier for me to maintain and make necessary modifications to a single patch rather than a dozen of them.


---

Comment by AlexGhitza created at 2009-08-21 13:03:38

Changing keywords from "" to "maxima".


---

Comment by AlexGhitza created at 2009-08-21 13:06:29

apply after the ecl and maxima spkg's


---

Attachment

Replying to [comment:6 AlexGhitza]:

> {{{
 sage -t  "expression.pyx"                                   
**********************************************************************
 File "/opt/sage-4.1.1/devel/sage-main/sage/symbolic/expression.pyx", line 5541:
     sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
 Expected:
     [Q == 1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
 Got:
     [Q == 1/sqrt(sqrt(2) + 1)]
 **********************************************************************
 }}}
> 
> I think this is due to the fact that Maxima now only returns the real solution, and ignores the complex solution.  I'm not sure what we should do about this.

I think you are right. Maxima treats variables to be real by default. To see that in maxima

```
sage: !maxima
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp ECL 9.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) conjugate(Q);
(%o1)                                  Q
```


So, if maxima is throwing away complex solution then its consistent with its own assumptions. 
Unless someone else has different opinion then we should simply accept what maxima is returning
now.


---

Comment by AlexGhitza created at 2009-08-22 12:03:32

Actually, I was wrong.  This is a bug in Maxima, which used to give the right answer but doesn't any more.  See 

http://www.math.utexas.edu/pipermail/maxima/2009/017632.html

for a discussion of this.


---

Comment by AlexGhitza created at 2009-08-22 12:06:08

We might have to get Maxima's "solutions" and check them before returning them to the user.  This is a pain.


---

Comment by AlexGhitza created at 2009-08-24 01:16:12

OK, I have come up with a workaround for Maxima's bug.  Since we are now patching Maxima 5.19.1, I've made a new spkg with "bumped" version number:

http://sage.math.washington.edu/home/ghitza/maxima-5.19.1.p0.spkg

I will soon explain my workaround here to facilitate reviewing, but I thought I'd first put the spkg up in case people want to test it.


---

Comment by AlexGhitza created at 2009-08-24 03:48:42

Here's a description of the problem and the workaround patched in the latest spkg:

We are calling Maxima's function `to_poly_solve` on the symbolic expression `Q*sqrt(Q^2+2)-1 == 0`.  Maxima takes this expression and turns it into a system of polynomial equations, and possibly some inequalities giving constraints on the variables.  This is done by a function in `share/contrib/topoly.lisp`.  This function behaves differently under Maxima 5.19.1 than it did under Maxima 5.16.3, and that's what is causing Maxima to lose one of the solutions:

Maxima 5.16.3:

```
sage: var('Q');
sage: ex = Q*sqrt(Q^2+2)-1 == 0
sage: m = ex._maxima_()
sage: m.to_poly()
[[%g0*Q-1,Q^2+2=%g0^2],[-%pi/2<carg(%g0),carg(%g0)<=%pi/2]]
```


Maxima 5.19.1:

```
sage: var('Q');
sage: ex = Q*sqrt(Q^2+2)-1 == 0
sage: m = ex._maxima_()
sage: m.to_poly()
[[%g0*Q-1,Q^2+2=%g0^2],[-%pi/2<parg(%g0),parg(%g0)<=%pi/2],[]]
```


The main difference between the two is that `carg` turned into `parg`.  The latter is a new function which is supposed to be a lightweight alternative to `carg`.

The right way to fix this is to properly debug `topoly.lisp` and send a patch to Maxima, but I do not have the time or expertise to do that.  The author knows about the bug (see above link to maxima mailing list), so hopefully this will get sorted out in a future release of Maxima.

For now, I'm patching `topoly.lisp` so that the appropriate occurrences of `parg` are changed back into `carg`.  This solves our doctest failure.


---

Comment by AlexGhitza created at 2009-08-24 08:12:19

Note to the release manager: when this gets merged, the following tickets should be closed as fixed (they are all contained in this patch):

#6782, #6783, #6784, #6785, #6786, #6787, #6789, #6792


---

Comment by awebb created at 2009-08-25 06:28:08

Not to be pedantic but it would be good to add the usual stuff to the SPKG.txt file to make it more like other packages. I don't know if anyone would like to put their name in for the package maintainer.


```
## Description

Maxima is a symbolic computation program.  It is full featured,
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats.  It has a
symbolic debugger source level debugger for maxima code.  Maxima is
based on the original Macsyma developed at MIT in the 1970's.  It is
quite reliable, and has good garbage collection, and no memory leaks.
It comes with hundreds of self tests.

Website: http://maxima.sourceforge.net

## License

 * Maxima is distributed under the GNU General Public License, with some
export restrictions from the U.S. Department of Energy. See the file
COPYING.

## SPKG Maintainers

 * ?

## Upstream Contact

 * the Maxima mailing list - see http://maxima.sourceforge.net/maximalist.html
```


The patch seems quite reasonable to me. Most of it seems to be due to improvements in maxima. Changing parg back to carg will likely have to be looked at in a future update but I think is appropriate at this time. I tested the package on 32 and 64 bit linux and it worked well. I ran 'make testlong' and everything passed. I give it a positive review. Has this been tested on Solaris?

Adam


---

Comment by AlexGhitza created at 2009-08-25 11:40:06

Adam,

Thanks for taking the time to review this.  I have made changes very close to what you suggested in SPKG.txt, and replaced the spkg -- it's in the same place as before.

I also changed the ticket summary in light of your positive review.


---

Comment by mvngu created at 2009-09-02 10:52:22

Merged `maxima-5.19.1.p0.spkg` in the standard packages repository and applied the patch `maxima_doctests.patch`. See my comments at #6564 for test results on various platforms.


---

Comment by mvngu created at 2009-09-02 10:52:22

Resolution: fixed


---

Comment by mvngu created at 2009-09-04 06:40:15

See #6883 for a follow-up to this ticket.
