# Issue 2383: memory leak when converting between GMP-based types and numpy types

Issue created by migration from https://trac.sagemath.org/ticket/2383

Original creator: craigcitro

Original creation time: 2008-03-04 10:35:26

Assignee: mabshoff

There's a fairly large memory leak that shows up when converting from ZZ and QQ to numpy types. Here's an example:


```
sage: ls = range(50000)
sage: import numpy
sage: A.<x> = ZZ[]
sage: f = x**3-2*x+1
sage: type(f)
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>

sage: def my_func(f):
    tmp = numpy.atleast_1d(f.list())
    tmp2 = tmp.astype(float)
....:     
sage: get_memory_usage()
'124M+'
sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'133M+'


sage: f = f.change_ring(QQ)
sage: type(f)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>

sage: get_memory_usage()
'133M+'

sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'150M+'

sage: f = f.change_ring(RDF)
sage: get_memory_usage()
'150M+'

sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'150M+'
```


This was first noted in trac #2239, where we use `numpy.roots(f.list())` instead of the above, but I think it ultimately gets traced to the code above. As you can see, it leaks for both `ZZ` and `QQ`, but not for `RDF` -- or most other types one might try. However, since RR uses GMP, it leaks too:


```
sage: ls = range(50000)ent Mercurial branch is: abvar
sage: import numpy
sage: B.<x> = RR[]
sage: f = x**3-2*x+1
sage: type(f)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>

sage: def my_func(f):
....:     tmp = numpy.atleast_1d(f.list())
....:     tmp2 = tmp.astype(float)
....:     
sage: def my_func2(f):
    tmp = numpy.atleast_1d([ RR(a) for a in f.list() ])
    tmp2 = tmp.astype(float)
....:     
sage: get_memory_usage()
'124M+'

sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'124M+'

sage: for _ in ls: my_func2(f)
....: 
sage: get_memory_usage()
'138M+'

}}} 

There's a known workaround -- don't convert directly between these types. For example:

{{{
sage: def my_func2(f):
    tmp = numpy.atleast_1d([ int(a) for a in f.list() ])
    tmp2 = tmp.astype(float)
....:     
sage: get_memory_usage()
'150M+'

sage: for _ in ls: my_func2(f)
....: 
sage: get_memory_usage()
'150M+'
}}}

Several people looked at this during SD8, but didn't come up with a solution. If anyone hits on anything, please let us know!


---

Comment by robertwb created at 2008-03-16 08:03:28

I looks like it leaks for everything:


```
sage: ls = range(10^4)
sage: def my_func(f):
    tmp = numpy.atleast_1d([R(1)..20])
    tmp2 = tmp.astype(float)
....:     
sage: R = RDF
sage: get_memory_usage()
'457M'
sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'461M'
```



---

Comment by robertwb created at 2008-03-16 08:52:24


```
sage: class MyFloat:
     def __float__(self):
         return 1
     
sage: def my_func(f):
    tmp = numpy.atleast_1d([MyFloat()]*10)
    tmp2 = tmp.astype(float)

sage: get_memory_usage()
'461M'
sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
'472M'
sage: for _ in range(10^4): my_func(f)
....: 
sage: get_memory_usage()
'483M'
```



---

Attachment

The attached pure python file leaks too.


---

Comment by mabshoff created at 2008-03-22 03:39:37

Travis O. just posted the following to the numpy mailing list:

```
Subject: Vectorize leak fixed (and sage-reported leak	fixed as well).

Hello all,

Much thanks is deserved by the people who have been chasing down and 
fixing reference count problems in NumPy.  Two of them are related to 
object arrays.  

So, if you have been having memory leak problems with object arrays 
(vectorize uses object arrays, BTW), you should try out the latest SVN 
of NumPy to see if they fix your problems.   Hopefully, NumPy 1.0.5 will 
come out sometime next week so that everybody can enjoy a more 
memory-conscious NumPy.

The vectorize-related leak was a particularly silly one which led to 
casting for simple cases actually doing more work instead of less (this 
led inexorably to leaks whenever object arrays were cast to other types).

Best regards,

-Travis
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 05:07:48

And since we have updated to numpy-1.1.0 this is fixed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.alpha2, Release Date: 2008-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: ls = range(50000)
sage: import numpy
sage: B.<x> = RR[]
sage: f = x**3-2*x+1
sage: type(f)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>
sage: def my_func(f):
....:     tmp = numpy.atleast_1d(f.list())
....:     tmp2 = tmp.astype(float)
....:     
sage: def my_func2(f):
....:     tmp = numpy.atleast_1d([ RR(a) for a in f.list() ])
....:     tmp2 = tmp.astype(float)
....:     
sage: get_memory_usage()
406.9453125
sage: for _ in ls: my_func(f)
....: 
sage: get_memory_usage()
407.05859375
sage: for _ in ls: my_func2(f)
....: 
sage: get_memory_usage()
407.05859375
sage: 
```



---

Comment by mabshoff created at 2008-08-31 05:07:48

Resolution: fixed
