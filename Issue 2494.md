# Issue 2494: bugs in evaluation of spherical bessel function

Issue created by migration from https://trac.sagemath.org/ticket/2494

Original creator: was

Original creation time: 2008-03-12 14:44:25

Assignee: jkantor


```
BUG 1:

Hi,
I was just trying to calculate some stuff with spherical Bessel
functions and got this error message:

sage: spherical_bessel_J(3,.1)


....
6823         return x
  6824     except SyntaxError:
-> 6825         raise TypeError, "unable to make sense of Maxima
expression '%s' in SAGE"%s
  6826     finally:
  6827         is_simplified = False

<type 'exceptions.TypeError'>: unable to make sense of Maxima
expression '9.5185197208655641L-6' in SAGE
sage:
KeyboardInterrupt

I checked it, it happens for small values of the argument x.
Does anyone has a solution or work around?

Greets,

schorsch
```


BUG2

```
sage: spherical_bessel_J(3,.1, algorithm='scipy')
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/was/Downloads/z/<ipython console> in <module>()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/functions/special.py in spherical_bessel_J(n, var, algorithm)
    782         ans = ans.replace(")","")
    783         ans = ans.replace("j","*I")
--> 784         return sage_eval(ans)
    785     elif algorithm == 'maxima':
    786         _init()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/sage_eval.py in sage_eval(source, locals)
    108     p = preparse(source)
    109     try:
--> 110         return eval(p, sage.all.__dict__, locals)
    111     except SyntaxError, msg:
    112         raise SyntaxError, "%s\nError using SAGE to evaluate '%s'"%(msg, p)

/Users/was/Downloads/z/<string> in <module>()

<type 'exceptions.NameError'>: name 'array' is not defined
```


Probably many of the special functions in functions/special.py have similar bugs. 


---

Comment by mhansen created at 2009-06-04 21:25:09

Changing assignee from jkantor to mhansen.


---

Comment by mhansen created at 2009-06-04 21:25:09

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-08-24 09:13:21

Note that BUG 1 has disappeared in sage-4.1.1:


```
sage: spherical_bessel_J(3,.1)
9.51851972087e-06
```


BUG 2 is still there.


---

Attachment


---

Comment by mhansen created at 2010-01-17 06:08:48

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-23 02:07:49

Looks good and passes tests.


---

Comment by AlexGhitza created at 2010-01-23 02:07:49

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 12:01:57

Resolution: fixed
