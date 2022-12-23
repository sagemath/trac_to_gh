# Issue 7557: conversion of complex numbers in symbolic expressions to maxima broken

Issue created by migration from https://trac.sagemath.org/ticket/7557

Original creator: burcin

Original creation time: 2009-11-30 09:58:16

Assignee: burcin

CC:  kcrisman

Reported on sage-support:


```
var('y', domain='real')
assume(y, 'real')

abs(exp(y*I)).simplify()
    1

abs(exp(1.1*y*I)).simplify()
    e^(1.1*I*y)

The last result is incorrect. It seems simplify() doesn't like
floating point?
```


In this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/c6d4c757cef8cc4a


More evidence:


```
sage: t = abs(exp(y*I)); t
abs(e^(I*y))
sage: t._maxima_init_()
'abs(exp((y)*(0+%i*1)))'

sage: u = abs(exp(1.1*y*I)); u
abs(e^(1.10000000000000*I*y))
sage: u._maxima_init_()
'abs(exp((y)*(1.1000000000000001*I)))'
```


This might be the reason:


```
sage: t.operands()[0].operands()[0].operands()[1].pyobject()
I
sage: type(t.operands()[0].operands()[0].operands()[1].pyobject())
<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>

sage: u.operands()[0].operands()[0].operands()[1].pyobject()
1.10000000000000*I
sage: type(u.operands()[0].operands()[0].operands()[1].pyobject())
<type 'sage.rings.complex_number.ComplexNumber'>
```



---

Comment by kcrisman created at 2011-02-08 17:28:20

The thread [here](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/a6cbc2743ca47948) suggests perhaps this is fixed in Maxima 5.23.


---

Comment by kcrisman created at 2012-02-27 13:56:30

Robert Dodier of Maxima suggests in [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/d8db720220ee3508?show_docid=d8db720220ee3508#) that this should now be fixed.


---

Comment by kcrisman created at 2012-02-27 15:46:30

Oops, those were the same thread!


---

Comment by burcin created at 2012-11-20 09:53:33

Changing keywords from "" to "interfaces".


---

Comment by burcin created at 2012-11-20 09:53:33

[This sage-support thread](https://groups.google.com/d/topic/sage-support/mua3IYmrAWc/discussion) is also about the same problem. Patch coming up.


---

Comment by burcin created at 2012-11-20 10:27:49

Patch up. Please review.


---

Comment by burcin created at 2012-11-20 10:27:49

Changing status from new to needs_review.


---

Comment by burcin created at 2012-11-20 10:45:42

I updated the patch with a minor doctest correction in `expression.pyx`.


---

Comment by vbraun created at 2012-11-20 13:21:12

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2012-11-20 13:21:12

Looks good to me!


---

Comment by pipedream created at 2012-11-20 15:47:57

Am I testing this correctly? I don't see any change:


```
0 jan@osprey:~/sage/sage-5.4/devel$hg qpush 
applying trac_7557-maxima_complex_number_conversion.patch
now at: trac_7557-maxima_complex_number_conversion.patch
0 jan@osprey:~/sage/sage-5.4/devel$hg qapplied
trac_7557-maxima_complex_number_conversion.patch
0 jan@osprey:~/sage/sage-5.4/devel$mysage -b complexbug

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Executing 0 commands (using 1 thread)
Time to execute 0 commands: 0.0179660320282 seconds
Finished compiling Cython code (time = 0.490197181702 seconds)
running install
running build
running build_py
running build_ext
Executing 0 commands (using 1 thread)
Time to execute 0 commands: 0.00303983688354 seconds
Total time spent compiling C/C++ extensions:  0.0404081344604 seconds.
running install_lib
running install_egg_info
Removing /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Writing /home/jan/sage/sage-5.4/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info

real	0m1.531s
user	0m1.112s
sys	0m0.240s
0 jan@osprey:~/sage/sage-5.4/devel$mysage
----------------------------------------------------------------------
----------------------------------------------------------------------
^[[ALoading Sage library. Current Mercurial branch is: complexbug
sage: u=1.2; m=0.5; jacobi('sn',u,m)          
0.887715488619
sage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   
jacobi_sn(1.2 + 3.7081493546*I, 0.500000000000000)
sage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))
| Sage Version 5.4, Release Date: 2012-11-09                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
```


(Hangs, I interrupted it after 30 seconds. Running this calculation directly in maxima takes one second)


---

Comment by vbraun created at 2012-11-20 21:00:21

You need the latest Sage version. On Sage-5.5.rc0 + the patch from this ticket I get the following:

```
sage: u=1.2; m=0.5; jacobi('sn',u,m)
0.887715488619
sage: jacobi('sn',u+2*I*elliptic_kc(1-m),m)   
0.887715488619 - 1.79195288805e-15*I
sage: n(jacobi('sn',u+2*I*elliptic_kc(1-m),m))
0.887715488619280 - 1.79195288804672e-15*I
```

so it works as it should.


---

Comment by kcrisman created at 2012-11-20 21:30:44

Great work, Burcin!


---

Comment by jdemeyer created at 2012-12-18 14:56:43

The documentation isn't properly formatted:

```
docstring of sage.symbolic.expression.Expression.abs:24: WARNING: Literal block expected; none found.
```



---

Comment by jdemeyer created at 2012-12-18 14:56:43

Changing status from positive_review to needs_work.


---

Attachment

Use this patch


---

Comment by kcrisman created at 2012-12-18 15:03:16

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2012-12-18 15:03:16

I think this one should work?

Patchbot, apply trac_7557-maxima_complex_number_conversion.2.patch


---

Comment by jdemeyer created at 2012-12-19 21:12:04

On arando (32-bit Linux i686) and possibly all 32-bit systems:

```
sage -t  --long -force_lib devel/sage/sage/functions/special.py
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py", line 481:
    sage: t._maxima_init_(maxima)
Expected:
    '0.88771548861927996 - 1.7919528880467190e-15*%i'
Got:
    '0.88771548861927740 - 4.3254035228713778e-16*%i'
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.6.beta1/devel/sage-main/sage/functions/special.py", line 483:
    sage: t.n()
Expected:
    0.887715488619280 - 1.79195288804672e-15*I
Got:
    0.887715488619277 - 4.32540352287138e-16*I
**********************************************************************
```



---

Comment by jdemeyer created at 2012-12-19 21:12:04

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-01-10 15:38:58

** ping **

Using `# abs tol` should fix these.


---

Comment by burcin created at 2013-01-10 16:06:05

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2013-01-10 16:06:05

Thanks for the reminder Jeroen.


---

Comment by kcrisman created at 2013-01-10 16:49:20

I get 

```

sage -t  "devel/sage-main/sage/functions/special.py"        
    ... ''', res, 1e-13, 'ab
    ^
SyntaxError: invalid syntax

	 [0.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/functions/special.py"
Total time for all tests: 0.2 seconds
```

Not sure what happened here.  This is on 64-bit, apparently - I get the old answer.


---

Comment by kcrisman created at 2013-01-10 16:52:30

Here's the relevant part from the tmp file.

```

        TESTS:

        Check if complex numbers in the arguments are converted to maxima
        correctly :trac:`7557`::

            >>> t = jacobi('sn',RealNumber('1.2')+Integer(2)*I*elliptic_kc(Integer(1)-RealNumber('.5')),RealNumber('.5'))###line 480:_sage_    >>> t = jacobi($
            >>> t._maxima_init_(maxima)###line 481:_sage_    >>> t._maxima_init_(maxima)
            '0.88771548861927...*%i'
>>> res = Exception
>>> res =  t.n() # abs tol 1e-13###line 483:_sage_    >>> t.n() # abs tol 1e-13
>>> check_with_tolerance('''
...             0.887715488619280 - 1.79195288804672e-15*I
...         """
... ''', res, 1e-13, 'ab
>>> sig_on_count()
0
"""
```

So this might be something that only works with a working abs tol, which I may not yet have - is this based on beta3 or beta2?  I haven't compiled beta3 yet since I can't upgrade it ;-)


---

Attachment


---

Comment by burcin created at 2013-01-11 13:23:13

Replying to [comment:16 kcrisman]:
> {{{
> 
> sage -t  "devel/sage-main/sage/functions/special.py"        
>     ... ''', res, 1e-13, 'ab
>     ^
> SyntaxError: invalid syntax
> }}}

This seems to be a problem with the `sage-doctest` script. If the triple-quotes immediately follow the doctest result, it generates a temporary file with a syntax error. I cleaned up the patch before submitting, but didn't realize deleting empty lines could cause doctest failures.

I uploaded a new patch with the same name. It should work now.

I don't have time to open a ticket for the `sage-doctest` bug right now.


---

Comment by kcrisman created at 2013-01-11 17:11:05

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-01-11 17:11:05

Seems fine now, thanks.  I don't have a 32-bit system to test this on, though.

Patchbot, apply trac_7557-maxima_complex_number_conversion.2.patch and trac_7557-fix_doctest_precision.patch


---

Comment by jdemeyer created at 2013-01-21 21:07:48

Resolution: fixed
