# Issue 6869: [with patch, needs work] LP and MIP Solvers in Sage ( with symbolics )

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-09-02 17:39:06

Assignee: jkantor

CC:  schilly wdj mvngu

Hello everybody !!!

After the work done in #6502 I rewrote the whole class taking into account the fact that some people may want to use this class too, instead of just focusing on the fact I needed it quickly to write Graph-Theoretic functions.

Here is the new numerical.MIP class, using symbolics, I hope sufficiently documented and tested, and everything... Thank you for your help !! This should be the last run ;-)

To use it, you have to install either GLPK from ticket #6867 or Coin-OR CBC from #6868 ( if you have installed a former version, they won't be compatible ! )

The class and the doctests, though, should behave peacefully if none of them is installed ! :-)

Nathann


---

Comment by wdj created at 2009-09-08 14:54:00

This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).

Running more tests...


---

Comment by mvngu created at 2009-09-09 12:17:09

The module `sage/numerical/mip.pyx` should have 100% doctest coverage, given that it's being added to the Sage library:

```
[mvngu`@`sage numerical]$ sage -coverage mip.pyx 
----------------------------------------------------------------------
mip.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE mip.pyx: 62% (18 of 29)

Missing documentation:
         * __init__(self, value):
         * __str__(self):
         * __getitem__(self,i):
         * keys(self):
         * items(self):
         * depth(self):
         * values(self):


Missing doctests:
         * __init__(self,sense=1):
         * _NormalForm(self,exp):
         * _addElementToRing(self):
         * __init__(self,x,f,dim=1):

----------------------------------------------------------------------
```



---

Comment by ncohen created at 2009-09-09 17:52:37

Done !


---

Attachment


---

Comment by mvngu created at 2009-09-09 18:43:38

ncohen asked this question in IRC:

```
10:45 < ncohen> mvngu: do you know what this is ?
10:45 < ncohen> ERROR: Please define a s == loads(dumps(s)) doctest.
```

This is encouraging you to define an equality method `__eq__()` for each of the three classes `MIP`, `MIPSolverException`, and `MIPVariable`. Say you have instantiated two objects of the class `MIPVariable`. How can you test to see whether or not they are the same object? In Python, this is usually implemented in the method `__equ__()` of a class. If a class defines this method, you can compare two objects of that class using the double-equal operator `==`. For example:

```
sage: a1 = AlphabeticStrings()
sage: a2 = AlphabeticStrings()
sage: a1 == a2
True
```

Take the case of writing the method `__eq__()` for the class `MIPVariable`. Are there criteria to tell us that two objects of the class `MIPVariable` are the same? If `m1` and `m2` are two such objects, you can define them to be the same object if their corresponding attributes have the same values. Each object of `MIPVariable` has these attributes: `dim`, `dict`, `x`, `f`. One way to write the `__eq__()` method for `MIPVariable` is this:

```
def __eq__(self, other):
    r"""
    <insert lengthy documentation here, with examples>
    """
    return self.dim == other.dim and self.dict == other.dict and self.x == other.x and self.f == other.f
```

In the "EXAMPLES" section of that method, you should have an example as follows with appropriate values for `x`, `f`, and `dim`:

```
sage: m = MIPVariable(someX, someF, someDim)
sage: m == loads(dumps(m))
True
```

which should return True when you actually doctest the MIP module. Define a similar equality method for the other two classes.



One thing I dislike in code is to see it squashed together. This makes it more difficult to read, taking into account also that other people need to understand what that code does, its logical flow, and they might have been spending all day reading code. Good coding style is a plus here if you want your code to be as easily understandable as possible. Instead of doing this:

```
self.dim=dim 
self.dict={} 
self.x=x 
self.f=f
```

do this:

```
self.dim = dim 
self.dict = {} 
self.x = x 
self.f = f
```




Another issue is global namespace pollution. What I mean is that you should try to avoid as much as possible injecting your module, class, or function names into the global namespace when Sage loads itself. This is what you're currently doing with this code:

```
from sage.numerical.mip import *
```

What this means is that when you load Sage, all the class and function names defined in the module mip.pyx are loaded into the global namespace. An advantage to this is that a user doesn't have to first import the relevant class or function prior to using it. With the above import statement, I can do this

```
sage: m = MIPVariable(x,f)
```

Without the import statement, I would need to do this:

```
sage: from sage.numerical.mip import MIPVariable
sage: m = MIPVariable(x,f)
```

I can see that importing stuff when Sage is being loaded saves a lot of time explicitly importing that stuff. But a downside is that the global namespace is being polluted with module, class or function names that are not really necessary to load at the start. As more names are put into the global namespace, it takes longer and longer to load Sage.


---

Comment by wdj created at 2009-09-09 21:20:58

This applies fine to 4.1.2.a0 on an ubuntu 9.04 machine and passes sage -testall (with no packages, eg glpk, applied). The docstrings look fine (as before).

I then applies glpk and reran sage -testall. All tests passes sage -testall except this:


```

wdj`@`tinah:~/sagefiles/sage-4.1.2.alpha0$ ./sage -t  "devel/sage/sage/server/notebook/cell.py"
sage -t  "devel/sage/sage/server/notebook/cell.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [366.5 s]
exit code: 1024
```


I doubt this is related, so giving this a positive review.


---

Comment by mvngu created at 2009-09-10 11:07:54

See #6913 for a follow-up to this ticket. It addresses the issue of writing those `__eq__()` methods.


---

Comment by mvngu created at 2009-09-10 11:36:16

Resolution: fixed


---

Comment by mhansen created at 2009-09-25 07:42:39

After going through this patch, I think it would be best to revert it before 4.1.2 is released.  There is still a lot of things that need to be done to get it cleaned up.  Some of the things,

1. Almost all of the docstrings are incorrectly formatted.

1. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython.  It just makes Sage slower to compile and things harder to debug.

1. Some of the naming conventions do not match Sage's conventions. (isbinary vs. is_binary).  Also, names like the more explicit MixedIntegerProgram are preferred over the shortened MIP.

1. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk).  This is not the right way to do things and will eventually break.  I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.

I have some code that addresses some of these things that I'll put up shortly.


---

Comment by mvngu created at 2009-09-25 08:08:41

See #7012 for a follow up to this ticket. It addresses mhansen's suggestions.
