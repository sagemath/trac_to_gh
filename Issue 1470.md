# Issue 1470: upgrade maxima.spkg to 5.14.0

Issue created by migration from https://trac.sagemath.org/ticket/1470

Original creator: mabshoff

Original creation time: 2007-12-12 09:27:32

Assignee: was

Maxima is currently at 5.14.rc1. Once it is release update the spkg.

Cheers,

Michael


---

Comment by jmbr created at 2008-01-08 20:28:17

Changing assignee from was to jmbr.


---

Comment by was created at 2008-03-10 03:18:12

Here's another reason to do this:

```
from steve vonn:

The Maxima command 'mnewton' has a bug.
The problem may be solved by updating to the most recent build of Maxima.
{{{
sage: mnewton([x1+3*log(x1)-x2^2, 2*x1^2-x1*x2-5*x1+1], [x1, x2], [5, 5])
[[x1=3.756834008012769,x2=2.779849592817897]]

sage: mnewton([2*a^a-5],[a],[1])
[[a=1.70927556786144]]

sage: mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
Traceback (most recent call last):
...
TypeError: error evaluating "mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);":
Error executing code in Maxima
CODE:
 mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
Maxima ERROR:

Unable to convert 18.0*log(3)+0.5 to a complex double float
#0: solve_by_lu(eqs=[h[1]*(18.0*log(3)+0.5)-0.5*h[2]+12.0,4.0*h[2]*log(2)+h[1]+2.0],vars=[h[1],h[2]],field=complexfield)
#1: mnewton(funclist=[-v/u+2*3^u-5,2^v+u-4],varlist=[u,v],guesslist=[2,2])(mnewton.mac
line 106)

sage: build_info()$
Maximaversion:5.13.0Maximabuilddate:18:511/18/2008hosttype:x86_64-unknown-linux-gnulisp-implementation-type:CLISP
lisp-implementation-version:2.41(2006-10-13)(built3409699542)(memory3409699897)
}}}

The build_info() command indicates Sage is using Maxima 5.13.
I submitted the problem to Maxima Support and they said it works for
Maxima 5.14.
http://sourceforge.net/tracker/index.php?func=detail&atid=104933&aid=1909488&group_id=4933
{{{
Date: 2008-03-07 15:21
Sender: willisbl
Logged In: YES
user_id=895922
Originator: NO

It works for me; maybe you have an old version.

(%i2) mnewton([2*3^u-v/u-5, u+2^v-4], [u, v], [2, 2]);
(%o2) [[u=1.066618389595407,v=1.552564766841786]]

(%i8) build_info();
Maxima version: 5.14.0
Maxima build date: 21:46 12/27/2007
host type: i686-pc-mingw32
lisp-implementation-type: GNU Common Lisp (GCL)
lisp-implementation-version: GCL 2.6.8
}}}

Peace
```



---

Comment by mabshoff created at 2008-03-22 07:06:55

Changing assignee from jmbr to mabshoff.


---

Comment by mabshoff created at 2008-03-22 07:06:55

The updated SPKG at

http://sage.math.washington.edu/home/mabshoff/SPKG/maxima-5.14.0.spkg

contains Maxima 5.14.0. It builds fine, but we have a number of doctest failures:

```
sage -t -long devel/sage/sage/interfaces/maxima.py
**********************************************************************
File "maxima.py", line 903:
    sage: maxima.version()
Expected:
    '5.13.0'
Got:
    '5.14.0'
**********************************************************************
```

This one is trivial to fix :)

```
sage -t -long devel/sage/sage/combinat/combinat.py
**********************************************************************
File "combinat.py", line 1446:
    sage: hurwitz_zeta(1.1,1/2,50)
Expected:
    12.103813495683744469025853545548130581952676591199
Got:
    12.10381349568374531600056798197329044342041015625
**********************************************************************
```

A numerically different result - somebody needs to check what is correct.

```
sage -t -long devel/sage/sage/calculus/tests.py
**********************************************************************
File "tests.py", line 109:
    sage: integrate(log(1-x^2)/x, x)
Expected:
    log(x)*log(1 - x^2) + polylog(2, 1 - x^2)/2
Got:
    1*log(x)*log(1 - x^2) - 1*(-2*-log(1 - x^2)/2*log(x) - 2*(log(x)*log(1 - x^2) + polylog(2, 1 - x^2)/2)/2)
**********************************************************************
```

Hmm, not sure what to make of this one.

```
sage -t -long devel/sage/sage/calculus/calculus.py
**********************************************************************
File "calculus.py", line 2134:
    sage: lim(-e^x/x, x = oo)
Expected:
    -Infinity
Got:
    +Infinity
**********************************************************************
File "calculus.py", line 2148:
    sage: forget(); assume(x<-2); lim(f, x=0, taylor=True)
Expected:
    und
Got:
    limit(log(log(x))/log(x), x, 0)
**********************************************************************
```

Mhh, did the parser change? 

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 07:06:55

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-22 21:22:13

The integral with polylog should be the same:

```
(%i28) ratsimp(integrate(log(1-x^2)/x, x));
(%o28) (2*log(x)*log(1-x^2)+li[2](1-x^2))/2
```


The +/-Infinity one is a bug in Maxima.  I'm sending a note to the maxima list.

```
(%i15) limit( -%e^x/x, x, inf);
(%o15)                                inf
```


The doctest for the Hurwitz zeta is correct.  Maxima is doing some float - bigfloat trickery behind the scenes:

```
(%i29) bfhzeta(1.1b0,1/2,50);
(%o29) 1.2103813495683754558667560862969910437753328504699b1
(%i30) bfhzeta(1.1,1/2,50);
(%o30) 1.210381349568374531600056798197329044342041015625b1
```


All of the above examples were done with Maxima 5.14.0


---

Comment by mabshoff created at 2008-03-22 21:42:43

For Mike Hansen's email to the Maxima list see

http://www.math.utexas.edu/pipermail/maxima/2008/010554.html

Cheers,

Michael


---

Comment by mhansen created at 2008-04-20 17:07:30

It looks like the issues with 5.14 have been fixed in 5.15.


---

Comment by mabshoff created at 2008-04-21 09:02:28

I will be rolling an updated 5.15.0.spkg for Sage 3.0.1.

Cheers,

Michael


---

Comment by gfurnish created at 2008-06-18 22:56:05

There is a new maxima spkg available at http://sage.math.washington.edu/home/gfurnish/spkg/maxima-5.15.0.spkg

The doctest errors are the following:

```
----------------------------------------------------------------------
sage -t  devel/sage-dsage3/sage/calculus/predefined.py
	 [5.9 s]
sage -t  devel/sage-dsage3/sage/calculus/functions.py
	 [7.7 s]
sage -t  devel/sage-dsage3/sage/calculus/var.pyx
	 [7.7 s]
sage -t  devel/sage-dsage3/sage/calculus/test_sympy.py
	 [9.6 s]
sage -t  devel/sage-dsage3/sage/calculus/desolvers.py
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/desolvers.py", line 134:
    sage: desolve_laplace(de(f(x)),["x","f"])
Expected:
    "x*%e^x*(?%at('diff(f(x),x,1),x=0))-f(0)*x*%e^x+f(0)*%e^x"
Got:
    "x*%e^x*('at('diff(f(x),x,1),x=0))-f(0)*x*%e^x+f(0)*%e^x"
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/gfurnish/sage-3.0.3.rc0/tmp/.doctest_desolvers.py

	 [9.9 s]
sage -t  devel/sage-dsage3/sage/calculus/functional.py
	 [15.1 s]
sage -t  devel/sage-dsage3/sage/calculus/wester.py
	 [17.0 s]
sage -t  devel/sage-dsage3/sage/calculus/tests.py
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/tests.py", line 198:
    sage: f.nintegral(x, 0, 999)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[75]>", line 1, in <module>
        f.nintegral(x, Integer(0), Integer(999))###line 198:
    sage: f.nintegral(x, 0, 999)
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2622, in nintegral
        raise ValueError, "Maxima (via quadpack) cannot compute the integral to that precision"
    ValueError: Maxima (via quadpack) cannot compute the integral to that precision
**********************************************************************
1 items had failures:
   1 of  83 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/gfurnish/sage-3.0.3.rc0/tmp/.doctest_tests.py

	 [17.3 s]
sage -t  devel/sage-dsage3/sage/calculus/equations.py
	 [32.9 s]
sage -t  devel/sage-dsage3/sage/calculus/calculus.py
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/calculus.py", line 766:
    sage: print f
Expected:
                                                 (sqrt(2)  I + sqrt(2)) x
           sqrt( pi) ((sqrt(2)  I + sqrt(2)) erf(------------------------)
                                                            2
                                                       (sqrt(2)  I - sqrt(2)) x
                          + (sqrt(2)  I - sqrt(2)) erf(------------------------))/8
                                                                  2
Got:
    <BLANKLINE>
                                                    (sqrt(2)  I + sqrt(2)) x
             (sqrt( pi) ((sqrt(2)  I + sqrt(2)) erf(------------------------)
                                                               2
                                                      (sqrt(2)  I - sqrt(2)) x
                         + (sqrt(2)  I - sqrt(2)) erf(------------------------)))/8
                                                                 2
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/calculus.py", line 2169:
    sage: forget(); assume(x<-2); lim(f, x=0, taylor=True)
Expected:
    und
Got:
    limit(log(log(x))/log(x), x, 0)
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/calculus.py", line 2442:
    sage: print f.integral(x)
Expected:
          z                                         (sqrt(2)  I + sqrt(2)) x
       x y  + sqrt( pi) ((sqrt(2)  I + sqrt(2)) erf(------------------------)
                                                               2
                                                   (sqrt(2)  I - sqrt(2)) x
                      + (sqrt(2)  I - sqrt(2)) erf(------------------------))/8
                                                              2
Got:
    <BLANKLINE>
                z
             x y  + (sqrt( pi) ((sqrt(2)  I + sqrt(2))
         (sqrt(2)  I + sqrt(2)) x
     erf(------------------------) + (sqrt(2)  I - sqrt(2))
                    2
         (sqrt(2)  I - sqrt(2)) x
     erf(------------------------)))/8
                    2
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/calculus.py", line 2568:
    sage: f.nintegral(x, 0, 1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_68[4]>", line 1, in <module>
        f.nintegral(x, Integer(0), Integer(1))###line 2568:
    sage: f.nintegral(x, 0, 1)
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2622, in nintegral
        raise ValueError, "Maxima (via quadpack) cannot compute the integral to that precision"
    ValueError: Maxima (via quadpack) cannot compute the integral to that precision
**********************************************************************
File "/scratch/gfurnish/sage-3.0.3.rc0/tmp/calculus.py", line 2596:
    sage: f.nintegrate(x,0,1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_68[10]>", line 1, in <module>
        f.nintegrate(x,Integer(0),Integer(1))###line 2596:
    sage: f.nintegrate(x,0,1)
      File "/scratch/gfurnish/sage-3.0.3.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2622, in nintegral
        raise ValueError, "Maxima (via quadpack) cannot compute the integral to that precision"
    ValueError: Maxima (via quadpack) cannot compute the integral to that precision
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_23
   1 of  23 in __main__.example_63
   1 of  32 in __main__.example_67
   2 of  15 in __main__.example_68
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/gfurnish/sage-3.0.3.rc0/tmp/.doctest_calculus.py
```



---

Comment by mabshoff created at 2008-08-11 07:02:38

The second release candidate, i.e. 5.16.1 was just released.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-21 23:02:07

With Mike's patch applied there are three new failures:

```
sage -t  devel/sage/sage/functions/piecewise.py             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/piecewise.py", line 512:
    sage: f.critical_points()
Expected:
    [5.0, 12.000000000000171, 12.9999999999996, 14.000000000000229]
Got:
    [5.0, 11.99999999999975, 13.00000000000057, 13.99999999999967]
**********************************************************************
```

And

```
sage -t  devel/sage/sage/combinat/combinat.py               
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/combinat.py", line 1433:
    sage: hurwitz_zeta(1.1,1/2,50)
Expected:
    12.103813495683744469025853545548130581952676591199
Got:
    12.10381349568374531600056798197329044342041015625
**********************************************************************
```

And finally:

```
sage -t  devel/doc/const/const.tex                          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/const.py", line 610:
    : f
Expected:
    f(x)=x*%e^x*(?%at('diff(f(x),x,1),x=0))-f(0)*x*%e^x+f(0)*%e^x
Got:
    f(x)=x*%e^x*('at('diff(f(x),x,1),x=0))-f(0)*x*%e^x+f(0)*%e^x
**********************************************************************
```



---

Attachment

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/maxima-5.16.2.spkg

Cheers,

Michael


---

Comment by mhansen created at 2008-08-22 18:20:58

+1 on the spkg


---

Comment by mabshoff created at 2008-08-22 18:26:27

Positive review on Mike's two patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 18:27:03

Resolution: fixed


---

Comment by mabshoff created at 2008-08-22 18:27:03

Merged in Sage 3.1.2.alpha0
