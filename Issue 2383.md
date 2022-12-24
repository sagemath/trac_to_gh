# Issue 2383: memory leak when converting between GMP-based types and numpy types

archive/issues_002383.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere's a fairly large memory leak that shows up when converting from ZZ and QQ to numpy types. Here's an example:\n\n\n```\nsage: ls = range(50000)\nsage: import numpy\nsage: A.<x> = ZZ[]\nsage: f = x**3-2*x+1\nsage: type(f)\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\n\nsage: def my_func(f):\n    tmp = numpy.atleast_1d(f.list())\n    tmp2 = tmp.astype(float)\n....:     \nsage: get_memory_usage()\n'124M+'\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'133M+'\n\n\nsage: f = f.change_ring(QQ)\nsage: type(f)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>\n\nsage: get_memory_usage()\n'133M+'\n\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'150M+'\n\nsage: f = f.change_ring(RDF)\nsage: get_memory_usage()\n'150M+'\n\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'150M+'\n```\n\n\nThis was first noted in trac #2239, where we use `numpy.roots(f.list())` instead of the above, but I think it ultimately gets traced to the code above. As you can see, it leaks for both `ZZ` and `QQ`, but not for `RDF` -- or most other types one might try. However, since RR uses GMP, it leaks too:\n\n\n```\nsage: ls = range(50000)ent Mercurial branch is: abvar\nsage: import numpy\nsage: B.<x> = RR[]\nsage: f = x**3-2*x+1\nsage: type(f)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>\n\nsage: def my_func(f):\n....:     tmp = numpy.atleast_1d(f.list())\n....:     tmp2 = tmp.astype(float)\n....:     \nsage: def my_func2(f):\n    tmp = numpy.atleast_1d([ RR(a) for a in f.list() ])\n    tmp2 = tmp.astype(float)\n....:     \nsage: get_memory_usage()\n'124M+'\n\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'124M+'\n\nsage: for _ in ls: my_func2(f)\n....: \nsage: get_memory_usage()\n'138M+'\n\n```\n \n\nThere's a known workaround -- don't convert directly between these types. For example:\n\n\n```\nsage: def my_func2(f):\n    tmp = numpy.atleast_1d([ int(a) for a in f.list() ])\n    tmp2 = tmp.astype(float)\n....:     \nsage: get_memory_usage()\n'150M+'\n\nsage: for _ in ls: my_func2(f)\n....: \nsage: get_memory_usage()\n'150M+'\n```\n\n\nSeveral people looked at this during SD8, but didn't come up with a solution. If anyone hits on anything, please let us know!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2383\n\n",
    "created_at": "2008-03-04T10:35:26Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "memory leak when converting between GMP-based types and numpy types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2383",
    "user": "craigcitro"
}
```
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

```
 

There's a known workaround -- don't convert directly between these types. For example:


```
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
```


Several people looked at this during SD8, but didn't come up with a solution. If anyone hits on anything, please let us know!

Issue created by migration from https://trac.sagemath.org/ticket/2383





---

archive/issue_comments_016076.json:
```json
{
    "body": "I looks like it leaks for everything:\n\n\n```\nsage: ls = range(10^4)\nsage: def my_func(f):\n    tmp = numpy.atleast_1d([R(1)..20])\n    tmp2 = tmp.astype(float)\n....:     \nsage: R = RDF\nsage: get_memory_usage()\n'457M'\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'461M'\n```\n",
    "created_at": "2008-03-16T08:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16076",
    "user": "robertwb"
}
```

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

archive/issue_comments_016077.json:
```json
{
    "body": "\n```\nsage: class MyFloat:\n     def __float__(self):\n         return 1\n     \nsage: def my_func(f):\n    tmp = numpy.atleast_1d([MyFloat()]*10)\n    tmp2 = tmp.astype(float)\n\nsage: get_memory_usage()\n'461M'\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n'472M'\nsage: for _ in range(10^4): my_func(f)\n....: \nsage: get_memory_usage()\n'483M'\n```\n",
    "created_at": "2008-03-16T08:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16077",
    "user": "robertwb"
}
```


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

archive/issue_comments_016078.json:
```json
{
    "body": "Attachment [memleak.py](tarball://root/attachments/some-uuid/ticket2383/memleak.py) by robertwb created at 2008-03-16 09:14:12\n\nThe attached pure python file leaks too.",
    "created_at": "2008-03-16T09:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16078",
    "user": "robertwb"
}
```

Attachment [memleak.py](tarball://root/attachments/some-uuid/ticket2383/memleak.py) by robertwb created at 2008-03-16 09:14:12

The attached pure python file leaks too.



---

archive/issue_comments_016079.json:
```json
{
    "body": "Travis O. just posted the following to the numpy mailing list:\n\n```\nSubject: Vectorize leak fixed (and sage-reported leak\tfixed as well).\n\nHello all,\n\nMuch thanks is deserved by the people who have been chasing down and \nfixing reference count problems in NumPy.  Two of them are related to \nobject arrays.  \n\nSo, if you have been having memory leak problems with object arrays \n(vectorize uses object arrays, BTW), you should try out the latest SVN \nof NumPy to see if they fix your problems.   Hopefully, NumPy 1.0.5 will \ncome out sometime next week so that everybody can enjoy a more \nmemory-conscious NumPy.\n\nThe vectorize-related leak was a particularly silly one which led to \ncasting for simple cases actually doing more work instead of less (this \nled inexorably to leaks whenever object arrays were cast to other types).\n\nBest regards,\n\n-Travis\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T03:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16079",
    "user": "mabshoff"
}
```

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

archive/issue_comments_016080.json:
```json
{
    "body": "And since we have updated to numpy-1.1.0 this is fixed:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.alpha2, Release Date: 2008-08-29                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: ls = range(50000)\nsage: import numpy\nsage: B.<x> = RR[]\nsage: f = x**3-2*x+1\nsage: type(f)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field'>\nsage: def my_func(f):\n....:     tmp = numpy.atleast_1d(f.list())\n....:     tmp2 = tmp.astype(float)\n....:     \nsage: def my_func2(f):\n....:     tmp = numpy.atleast_1d([ RR(a) for a in f.list() ])\n....:     tmp2 = tmp.astype(float)\n....:     \nsage: get_memory_usage()\n406.9453125\nsage: for _ in ls: my_func(f)\n....: \nsage: get_memory_usage()\n407.05859375\nsage: for _ in ls: my_func2(f)\n....: \nsage: get_memory_usage()\n407.05859375\nsage: \n```\n",
    "created_at": "2008-08-31T05:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16080",
    "user": "mabshoff"
}
```

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

archive/issue_comments_016081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-31T05:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2383#issuecomment-16081",
    "user": "mabshoff"
}
```

Resolution: fixed
