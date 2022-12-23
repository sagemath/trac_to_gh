# Issue 2512: implement condition number for matrices

archive/issues_002512.json:
```json
{
    "body": "Assignee: was\n\nimplement [condition number (wikipedia)](http://en.wikipedia.org/wiki/Condition_number) for matrices. \n\nsomething like:\n\n```\ndef condition(m,p=2):\n    return norm(m.inverse(),p) * norm(m,p)\n```\n\n\ndepends on #1763\n\nIssue created by migration from https://trac.sagemath.org/ticket/2512\n\n",
    "created_at": "2008-03-13T22:33:26Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "implement condition number for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2512",
    "user": "schilly"
}
```
Assignee: was

implement [condition number (wikipedia)](http://en.wikipedia.org/wiki/Condition_number) for matrices. 

something like:

```
def condition(m,p=2):
    return norm(m.inverse(),p) * norm(m,p)
```


depends on #1763

Issue created by migration from https://trac.sagemath.org/ticket/2512





---

archive/issue_comments_017032.json:
```json
{
    "body": "Condition numbers for any norm can be expensive, since they involve computing the inverse of a matrix. If our matrix is singular, this is even worse. I would propose:\n* Computing the condition number for norms 1,2,inf. This can be done reasonably efficiently in gsl and lapack\n* Computing condition estimators for other norms or when matrices get very large.\n\nIs there any case that we would want compute a condition for norms other than 1,2 and inf? I'm curious",
    "created_at": "2008-03-14T19:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17032",
    "user": "dfdeshom"
}
```

Condition numbers for any norm can be expensive, since they involve computing the inverse of a matrix. If our matrix is singular, this is even worse. I would propose:
* Computing the condition number for norms 1,2,inf. This can be done reasonably efficiently in gsl and lapack
* Computing condition estimators for other norms or when matrices get very large.

Is there any case that we would want compute a condition for norms other than 1,2 and inf? I'm curious



---

archive/issue_comments_017033.json:
```json
{
    "body": "A one-line implementation of the condition number, which computes A.norm()*A.inverse().norm().",
    "created_at": "2011-03-22T23:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17033",
    "user": "spice"
}
```

A one-line implementation of the condition number, which computes A.norm()*A.inverse().norm().



---

archive/issue_comments_017034.json:
```json
{
    "body": "Changing keywords from \"\" to \"matrix, condition number\".",
    "created_at": "2011-03-22T23:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17034",
    "user": "spice"
}
```

Changing keywords from "" to "matrix, condition number".



---

archive/issue_comments_017035.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-22T23:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17035",
    "user": "spice"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_017036.json:
```json
{
    "body": "Attachment\n\nThe patch implements a very simple .condition_number() method, based on a matrix's .norm() method. As such it only works for p = 1,2,Infinity or the Frobenius norm.\n\nSuggestions/comments welcome. Written on sage 4.6.2.",
    "created_at": "2011-03-22T23:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17036",
    "user": "spice"
}
```

Attachment

The patch implements a very simple .condition_number() method, based on a matrix's .norm() method. As such it only works for p = 1,2,Infinity or the Frobenius norm.

Suggestions/comments welcome. Written on sage 4.6.2.



---

archive/issue_comments_017037.json:
```json
{
    "body": "wow, this still exists. The doctest looks fine, is it possible to indent the options for the argument? Apart from that I strongly suggest to use numpy for that. They solve the 2-norm special case via svd and all the others might be faster. They also have a -infinity case.\n\n\n```\nsage: from numpy.linalg.linalg import cond     \nsage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])    \nsage: cond(A)                              \n13.139632629120618\nsage: cond(A, 1)                           \n22.88636363636364\nsage: cond(A, 'fro')                       \n14.21690371493278\nsage: import numpy as np                   \nsage: cond(A, np.inf)                      \n19.090909090909093\nsage: cond(A, -np.inf)                     \n2.5454545454545454\n```\n\n\ncomplex also works\n\n\n```\nsage: A = matrix([[1+2j, 1+3j], [1+1j, 0.5-0.5j]])\nsage: cond(A, np.inf)                             \n4.2200687516284452\nsage: cond(A)        \n3.2255049266776936\n```\n",
    "created_at": "2011-03-23T00:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17037",
    "user": "schilly"
}
```

wow, this still exists. The doctest looks fine, is it possible to indent the options for the argument? Apart from that I strongly suggest to use numpy for that. They solve the 2-norm special case via svd and all the others might be faster. They also have a -infinity case.


```
sage: from numpy.linalg.linalg import cond     
sage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])    
sage: cond(A)                              
13.139632629120618
sage: cond(A, 1)                           
22.88636363636364
sage: cond(A, 'fro')                       
14.21690371493278
sage: import numpy as np                   
sage: cond(A, np.inf)                      
19.090909090909093
sage: cond(A, -np.inf)                     
2.5454545454545454
```


complex also works


```
sage: A = matrix([[1+2j, 1+3j], [1+1j, 0.5-0.5j]])
sage: cond(A, np.inf)                             
4.2200687516284452
sage: cond(A)        
3.2255049266776936
```




---

archive/issue_comments_017038.json:
```json
{
    "body": "Hi Simon,\n\nCould you compare timings against #10837?  (I didn't know #2512 existed.)\n\nRob",
    "created_at": "2011-03-23T00:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17038",
    "user": "rbeezer"
}
```

Hi Simon,

Could you compare timings against #10837?  (I didn't know #2512 existed.)

Rob



---

archive/issue_comments_017039.json:
```json
{
    "body": "Turns out Rob Beezer has implemented condition numbers by directly wrapping the NumPy cond() command in patch #10837.\n\nSome timings:\n\nPatch 2512:\n\n\n```\nsage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])\nsage: timeit('A.condition_number(2)')\n125 loops, best of 3: 1.96 ms per loop\nsage: timeit('A.condition_number(Infinity)')\n625 loops, best of 3: 1.31 ms per loop\nsage: timeit('A.condition_number(\"frob\")')\n625 loops, best of 3: 949 \u00b5s per loop\n\nsage: A = MatrixSpace(CC,50).random_element()\nsage: timeit('A.condition_number(2)')\n5 loops, best of 3: 389 ms per loop\nsage: timeit('A.condition_number(1)')\n5 loops, best of 3: 380 ms per loop\nsage: timeit('A.condition_number(\"frob\")')\n5 loops, best of 3: 358 ms per loop\n```\n\n\nPatch 10837:\n\n\n```\nsage: A = matrix(RDF,[[1,2,4],[5,3,9],[7,8,6]])\nsage: timeit('A.condition(2)')\n625 loops, best of 3: 282 \u00b5s per loop\nsage: timeit('A.condition(Infinity)')\n625 loops, best of 3: 123 \u00b5s per loop\nsage: timeit('A.condition(\"frob\")')\n625 loops, best of 3: 203 \u00b5s per loop\n\nsage: A = MatrixSpace(CDF,50).random_element()\nsage: timeit('A.condition(1)')\n625 loops, best of 3: 968 \u00b5s per loop\nsage: timeit('A.condition(2)')\n125 loops, best of 3: 2.97 ms per loop\nsage: timeit('A.condition(\"frob\")')\n625 loops, best of 3: 942 \u00b5s per loop\n```\n\n\nI vote we go for Rob's patch.",
    "created_at": "2011-03-23T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17039",
    "user": "spice"
}
```

Turns out Rob Beezer has implemented condition numbers by directly wrapping the NumPy cond() command in patch #10837.

Some timings:

Patch 2512:


```
sage: A = matrix([[1,2,4],[5,3,9],[7,8,6]])
sage: timeit('A.condition_number(2)')
125 loops, best of 3: 1.96 ms per loop
sage: timeit('A.condition_number(Infinity)')
625 loops, best of 3: 1.31 ms per loop
sage: timeit('A.condition_number("frob")')
625 loops, best of 3: 949 µs per loop

sage: A = MatrixSpace(CC,50).random_element()
sage: timeit('A.condition_number(2)')
5 loops, best of 3: 389 ms per loop
sage: timeit('A.condition_number(1)')
5 loops, best of 3: 380 ms per loop
sage: timeit('A.condition_number("frob")')
5 loops, best of 3: 358 ms per loop
```


Patch 10837:


```
sage: A = matrix(RDF,[[1,2,4],[5,3,9],[7,8,6]])
sage: timeit('A.condition(2)')
625 loops, best of 3: 282 µs per loop
sage: timeit('A.condition(Infinity)')
625 loops, best of 3: 123 µs per loop
sage: timeit('A.condition("frob")')
625 loops, best of 3: 203 µs per loop

sage: A = MatrixSpace(CDF,50).random_element()
sage: timeit('A.condition(1)')
625 loops, best of 3: 968 µs per loop
sage: timeit('A.condition(2)')
125 loops, best of 3: 2.97 ms per loop
sage: timeit('A.condition("frob")')
625 loops, best of 3: 942 µs per loop
```


I vote we go for Rob's patch.



---

archive/issue_comments_017040.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-03-23T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17040",
    "user": "spice"
}
```

Resolution: duplicate



---

archive/issue_comments_017041.json:
```json
{
    "body": "> I vote we go for Rob's patch.\n\nYep, looks like 3 to 10 times faster.  I might steal your code for a verification doctest on #10837.\n\nThanks for the timing tests.",
    "created_at": "2011-03-23T01:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2512#issuecomment-17041",
    "user": "rbeezer"
}
```

> I vote we go for Rob's patch.

Yep, looks like 3 to 10 times faster.  I might steal your code for a verification doctest on #10837.

Thanks for the timing tests.
