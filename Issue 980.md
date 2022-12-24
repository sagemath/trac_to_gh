# Issue 980: random_element() for multivariate polynomials

archive/issues_000980.json:
```json
{
    "body": "Assignee: dfdeshom\n\nCC:  dfdeshom@gmail.com\n\nThere are 2 quirks about random multivariate polynomials outlined below:\n\n1) Degrees are severely restricted:\n> The maximum degree in every variable\n> is (maximum total degree of resulting polynomial) / (number of\n> varialbes of the polynomial). \n\n2) Too many zero elements. Polynomials generated are too sparse.\n> The second point is about the number of coefficients that are set to\n> 0. This might a point to argue about, but if I create a random\n> polynomial with a  (maximum number of terms to generate) then I expect\n> that the 0 occur\n\nIssue created by migration from https://trac.sagemath.org/ticket/980\n\n",
    "created_at": "2007-10-24T04:42:07Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "random_element() for multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/980",
    "user": "dfdeshom"
}
```
Assignee: dfdeshom

CC:  dfdeshom@gmail.com

There are 2 quirks about random multivariate polynomials outlined below:

1) Degrees are severely restricted:
> The maximum degree in every variable
> is (maximum total degree of resulting polynomial) / (number of
> varialbes of the polynomial). 

2) Too many zero elements. Polynomials generated are too sparse.
> The second point is about the number of coefficients that are set to
> 0. This might a point to argue about, but if I create a random
> polynomial with a  (maximum number of terms to generate) then I expect
> that the 0 occur

Issue created by migration from https://trac.sagemath.org/ticket/980





---

archive/issue_comments_005975.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T22:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5975",
    "user": "dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005976.json:
```json
{
    "body": "I've atached a patch. The individual degree distribution is a little better:\n\n```\nsage: f=ZZ['q,w,e,r,t,y'].random_element(degree=5,terms=9) ;f\n 3*q^5 - q^4*w + 2*q^3*w^2 + q^2*w^3 - q*w^3*e + q^2*w*r*t + 2*q*w*e*r*t + q^2*e*t^2 + 8*r^2*t^2*y\nsage: f=ZZ['q,w,e,r,t,y'].random_element(degree=4,terms=9) ;f\n q^2*w*e + q*w^2*r + q^2*r^2 - 24*w^3*t - 4*q^2*e*t - 5*t^4 - 4*q^3 + 2*q^2*w\n```\n",
    "created_at": "2007-10-24T22:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5976",
    "user": "dfdeshom"
}
```

I've atached a patch. The individual degree distribution is a little better:

```
sage: f=ZZ['q,w,e,r,t,y'].random_element(degree=5,terms=9) ;f
 3*q^5 - q^4*w + 2*q^3*w^2 + q^2*w^3 - q*w^3*e + q^2*w*r*t + 2*q*w*e*r*t + q^2*e*t^2 + 8*r^2*t^2*y
sage: f=ZZ['q,w,e,r,t,y'].random_element(degree=4,terms=9) ;f
 q^2*w*e + q*w^2*r + q^2*r^2 - 24*w^3*t - 4*q^2*e*t - 5*t^4 - 4*q^3 + 2*q^2*w
```




---

archive/issue_comments_005977.json:
```json
{
    "body": "Your patch seems to prefer variables with lower indexes, i.e. the probability that x in x,y,z has the highest degree is quite high because you are making the search space smaller for each variable. Maybe you could permute the exponent tuple randomly afterwards to take care of that bias?",
    "created_at": "2007-10-24T23:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5977",
    "user": "malb"
}
```

Your patch seems to prefer variables with lower indexes, i.e. the probability that x in x,y,z has the highest degree is quite high because you are making the search space smaller for each variable. Maybe you could permute the exponent tuple randomly afterwards to take care of that bias?



---

archive/issue_comments_005978.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-10-25T00:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5978",
    "user": "was"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_005979.json:
```json
{
    "body": "Attachment [rand-poly.txt](tarball://root/attachments/some-uuid/ticket980/rand-poly.txt) by dfdeshom created at 2007-10-25 03:30:56",
    "created_at": "2007-10-25T03:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5979",
    "user": "dfdeshom"
}
```

Attachment [rand-poly.txt](tarball://root/attachments/some-uuid/ticket980/rand-poly.txt) by dfdeshom created at 2007-10-25 03:30:56



---

archive/issue_comments_005980.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Your patch seems to prefer variables with lower indexes, i.e. the probability that x in x,y,z has the highest degree is quite high because you are making the search space smaller for each variable. Maybe you could permute the exponent tuple randomly afterwards to take care of that bias?\n>  \n\nThanks. This also takes care of too many nonzero terms being generated. I've updated the patch",
    "created_at": "2007-10-25T03:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5980",
    "user": "dfdeshom"
}
```

Replying to [comment:2 malb]:
> Your patch seems to prefer variables with lower indexes, i.e. the probability that x in x,y,z has the highest degree is quite high because you are making the search space smaller for each variable. Maybe you could permute the exponent tuple randomly afterwards to take care of that bias?
>  

Thanks. This also takes care of too many nonzero terms being generated. I've updated the patch



---

archive/issue_comments_005981.json:
```json
{
    "body": "the attached file `random_element.py` implements my proposal for this method. It is supposed to guarantee uniformly randomly chosen monomials per default and also supports to choose the degree randomly before choosing a monomial of that given degree.\n\nNOTE: `random_element.py` is not a patch but a `py` file to load/attach into SAGE to test it. I will provide a proper patch if we agree on the strategy.",
    "created_at": "2007-11-07T13:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5981",
    "user": "malb"
}
```

the attached file `random_element.py` implements my proposal for this method. It is supposed to guarantee uniformly randomly chosen monomials per default and also supports to choose the degree randomly before choosing a monomial of that given degree.

NOTE: `random_element.py` is not a patch but a `py` file to load/attach into SAGE to test it. I will provide a proper patch if we agree on the strategy.



---

archive/issue_comments_005982.json:
```json
{
    "body": "Attachment [random_monomial.py](tarball://root/attachments/some-uuid/ticket980/random_monomial.py) by malb created at 2007-11-07 13:27:05",
    "created_at": "2007-11-07T13:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5982",
    "user": "malb"
}
```

Attachment [random_monomial.py](tarball://root/attachments/some-uuid/ticket980/random_monomial.py) by malb created at 2007-11-07 13:27:05



---

archive/issue_comments_005983.json:
```json
{
    "body": "Whoops, it is called `random_monomial.py` instead of `random_element.py`",
    "created_at": "2007-11-07T13:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5983",
    "user": "malb"
}
```

Whoops, it is called `random_monomial.py` instead of `random_element.py`



---

archive/issue_comments_005984.json:
```json
{
    "body": "Replying to [comment:7 malb]:\n> the attached file `random_element.py` implements my proposal for this method. It is supposed to guarantee uniformly randomly chosen monomials per default and also supports to choose the degree randomly before choosing a monomial of that given degree.\n\nThe general strategy is OK with me. One minor implementation nitpick: I would use ZZ.random_element() instead of randint() because it is faster.",
    "created_at": "2007-11-07T15:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5984",
    "user": "dfdeshom"
}
```

Replying to [comment:7 malb]:
> the attached file `random_element.py` implements my proposal for this method. It is supposed to guarantee uniformly randomly chosen monomials per default and also supports to choose the degree randomly before choosing a monomial of that given degree.

The general strategy is OK with me. One minor implementation nitpick: I would use ZZ.random_element() instead of randint() because it is faster.



---

archive/issue_comments_005985.json:
```json
{
    "body": "Replying to [comment:7 malb]:\n> NOTE: `random_element.py` is not a patch but a `py` file to load/attach into SAGE to test it. I will provide a proper patch if we agree on the strategy.\nIf you don't mind, I've attached a patch against 2.8.11 for this. The patch is named random-malb.txt",
    "created_at": "2007-11-09T15:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5985",
    "user": "dfdeshom"
}
```

Replying to [comment:7 malb]:
> NOTE: `random_element.py` is not a patch but a `py` file to load/attach into SAGE to test it. I will provide a proper patch if we agree on the strategy.
If you don't mind, I've attached a patch against 2.8.11 for this. The patch is named random-malb.txt



---

archive/issue_comments_005986.json:
```json
{
    "body": "Attachment [random-malb.txt](tarball://root/attachments/some-uuid/ticket980/random-malb.txt) by mabshoff created at 2007-11-16 11:55:45",
    "created_at": "2007-11-16T11:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5986",
    "user": "mabshoff"
}
```

Attachment [random-malb.txt](tarball://root/attachments/some-uuid/ticket980/random-malb.txt) by mabshoff created at 2007-11-16 11:55:45



---

archive/issue_comments_005987.json:
```json
{
    "body": "Unfortunately, random-malb.txt no longer applies against sage-2.8.14.",
    "created_at": "2007-11-27T05:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5987",
    "user": "cwitty"
}
```

Unfortunately, random-malb.txt no longer applies against sage-2.8.14.



---

archive/issue_comments_005988.json:
```json
{
    "body": "Attachment [random-malb.hg](tarball://root/attachments/some-uuid/ticket980/random-malb.hg) by dfdeshom created at 2007-11-28 16:29:55",
    "created_at": "2007-11-28T16:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5988",
    "user": "dfdeshom"
}
```

Attachment [random-malb.hg](tarball://root/attachments/some-uuid/ticket980/random-malb.hg) by dfdeshom created at 2007-11-28 16:29:55



---

archive/issue_comments_005989.json:
```json
{
    "body": "I've added an hg bundle against 2.8.14",
    "created_at": "2007-11-28T16:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5989",
    "user": "dfdeshom"
}
```

I've added an hg bundle against 2.8.14



---

archive/issue_comments_005990.json:
```json
{
    "body": "Uploaded bundle which applies against 2.9.alpha7 and doctests pass.",
    "created_at": "2007-12-16T15:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5990",
    "user": "malb"
}
```

Uploaded bundle which applies against 2.9.alpha7 and doctests pass.



---

archive/issue_comments_005991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-20T23:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5991",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_005992.json:
```json
{
    "body": "`random_element.hg` merged in 2.9.1 alpha2",
    "created_at": "2007-12-20T23:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5992",
    "user": "rlm"
}
```

`random_element.hg` merged in 2.9.1 alpha2



---

archive/issue_comments_005993.json:
```json
{
    "body": "unmerged.",
    "created_at": "2007-12-21T00:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5993",
    "user": "rlm"
}
```

unmerged.



---

archive/issue_comments_005994.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-21T00:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5994",
    "user": "rlm"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_005995.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-21T00:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5995",
    "user": "rlm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_005996.json:
```json
{
    "body": "Robert Bradshaw is currently reviewing this",
    "created_at": "2007-12-22T04:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5996",
    "user": "rlm"
}
```

Robert Bradshaw is currently reviewing this



---

archive/issue_comments_005997.json:
```json
{
    "body": "For the most part, this looks good, but it seems that your algorithm is flawed in some cases (e.g more than two variables?). For example: \n\n\n```\nsage: [QQ['x,y,z'].random_element() for _ in range(10)]\n[-2/3, 1/6, 2, -2/11, 1, 11/2, 1/3, -5, 1/3, 3]\nsage: [ZZ['x,y,z,w'].random_element() for _ in range(10)]\n[-1, -10, -1, -8, 1, 4, -32, 1, 1, -1]\n```\n\n\nIt also has a bias against repeating variables in a monomial. None of these are of degree 7...\n\n\n```\nsage: [ZZ['x,y,z,w'].random_element(7,1) for _ in range(10)]\n[-1*w, y*z, -2*x*z*w, -22*x*y*w, -1*z, -5*x*y*w, 7*y*w, x*w, -2*y*z, 2*y*w]\n```\n",
    "created_at": "2008-01-02T17:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5997",
    "user": "robertwb"
}
```

For the most part, this looks good, but it seems that your algorithm is flawed in some cases (e.g more than two variables?). For example: 


```
sage: [QQ['x,y,z'].random_element() for _ in range(10)]
[-2/3, 1/6, 2, -2/11, 1, 11/2, 1/3, -5, 1/3, 3]
sage: [ZZ['x,y,z,w'].random_element() for _ in range(10)]
[-1, -10, -1, -8, 1, 4, -32, 1, 1, -1]
```


It also has a bias against repeating variables in a monomial. None of these are of degree 7...


```
sage: [ZZ['x,y,z,w'].random_element(7,1) for _ in range(10)]
[-1*w, y*z, -2*x*z*w, -22*x*y*w, -1*z, -5*x*y*w, 7*y*w, x*w, -2*y*z, 2*y*w]
```




---

archive/issue_comments_005998.json:
```json
{
    "body": "Trying to understand why the good-looking code produced such bad results, I figured out that I had forgotten to merge, so ignore the previous comments. \n\nThere are only two things I'd change:\n\n1. (Minor) There are multiple uses of ZZ.random_element(min,max), especially used to compute degrees in the monomials. I would highly recommend using Python's randint from http://docs.python.org/lib/module-random.html for speed. \n\n2. (Blocker) Not having default arguments for random_element means it can't be used generically. For example: \n\n\n```\nsage: random_matrix(QQ['x,y,z'], 2, 2)\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/matrix/constructor.py\", line 503, in random_matrix\n    A.randomize(density=density, *args, **kwds)\n  File \"matrix2.pyx\", line 2752, in sage.matrix.matrix2.Matrix.randomize\n<type 'exceptions.TypeError'>: function takes at least 2 arguments (0 given)\n```\n\n\nIt should not be necessary to special-case the basering being a multipolynomial element before calling random_element on it. Some default should be specified, even if it's degree and terms = 1+abs(ZZ.random_element()). \n\nEven worse\n\n\n```\nsage: R = QQ['x,y']\nsage: S = R['t,u']\nsage: S.random_element(d=2, t=3) # BOOM \n```\n\n\nIt is impossible to pass the required degree/number of terms arguments on to the basering of S.",
    "created_at": "2008-01-02T18:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5998",
    "user": "robertwb"
}
```

Trying to understand why the good-looking code produced such bad results, I figured out that I had forgotten to merge, so ignore the previous comments. 

There are only two things I'd change:

1. (Minor) There are multiple uses of ZZ.random_element(min,max), especially used to compute degrees in the monomials. I would highly recommend using Python's randint from http://docs.python.org/lib/module-random.html for speed. 

2. (Blocker) Not having default arguments for random_element means it can't be used generically. For example: 


```
sage: random_matrix(QQ['x,y,z'], 2, 2)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 503, in random_matrix
    A.randomize(density=density, *args, **kwds)
  File "matrix2.pyx", line 2752, in sage.matrix.matrix2.Matrix.randomize
<type 'exceptions.TypeError'>: function takes at least 2 arguments (0 given)
```


It should not be necessary to special-case the basering being a multipolynomial element before calling random_element on it. Some default should be specified, even if it's degree and terms = 1+abs(ZZ.random_element()). 

Even worse


```
sage: R = QQ['x,y']
sage: S = R['t,u']
sage: S.random_element(d=2, t=3) # BOOM 
```


It is impossible to pass the required degree/number of terms arguments on to the basering of S.



---

archive/issue_comments_005999.json:
```json
{
    "body": "Replying to [comment:20 robertwb]:\n> 1. (Minor) There are multiple uses of ZZ.random_element(min,max), especially used\n> to compute degrees in the monomials. I would highly recommend using Python's \n> randint from http://docs.python.org/lib/module-random.html for speed.\n\nI cannot confirm this:\n\nSage Integers:\n\n\n```\nsage: l = 0\nsage: u = 5\nsage: %timeit randint(l,u)\n10000 loops, best of 3: 31.1 \u00b5s per loop\nsage: %timeit ZZ.random_element(l,u)\n100000 loops, best of 3: 2.63 \u00b5s per loop\n```\n\n\nPython Integers:\n\n\n```\nsage: l = int(0)\nsage: u = int(5)\nsage: %timeit randint(l,u)\n100000 loops, best of 3: 7.65 \u00b5s per loop\nsage: %timeit ZZ.random_element(l,u)\n100000 loops, best of 3: 7.25 \u00b5s per loop\n```\n\n\nWhat am I missing?",
    "created_at": "2008-01-06T15:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-5999",
    "user": "malb"
}
```

Replying to [comment:20 robertwb]:
> 1. (Minor) There are multiple uses of ZZ.random_element(min,max), especially used
> to compute degrees in the monomials. I would highly recommend using Python's 
> randint from http://docs.python.org/lib/module-random.html for speed.

I cannot confirm this:

Sage Integers:


```
sage: l = 0
sage: u = 5
sage: %timeit randint(l,u)
10000 loops, best of 3: 31.1 µs per loop
sage: %timeit ZZ.random_element(l,u)
100000 loops, best of 3: 2.63 µs per loop
```


Python Integers:


```
sage: l = int(0)
sage: u = int(5)
sage: %timeit randint(l,u)
100000 loops, best of 3: 7.65 µs per loop
sage: %timeit ZZ.random_element(l,u)
100000 loops, best of 3: 7.25 µs per loop
```


What am I missing?



---

archive/issue_comments_006000.json:
```json
{
    "body": "new bundle against 2.9.2 which fixes the default parameter remark by robertwb",
    "created_at": "2008-01-06T16:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6000",
    "user": "malb"
}
```

new bundle against 2.9.2 which fixes the default parameter remark by robertwb



---

archive/issue_comments_006001.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-01-06T16:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6001",
    "user": "malb"
}
```

Changing priority from minor to major.



---

archive/issue_comments_006002.json:
```json
{
    "body": "Attachment [random_element.hg](tarball://root/attachments/some-uuid/ticket980/random_element.hg) by malb created at 2008-01-06 16:25:16",
    "created_at": "2008-01-06T16:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6002",
    "user": "malb"
}
```

Attachment [random_element.hg](tarball://root/attachments/some-uuid/ticket980/random_element.hg) by malb created at 2008-01-06 16:25:16



---

archive/issue_comments_006003.json:
```json
{
    "body": "Looks good to me!  doctests pass, Robert's issues with default arguments have been fixed.",
    "created_at": "2008-01-27T02:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6003",
    "user": "cwitty"
}
```

Looks good to me!  doctests pass, Robert's issues with default arguments have been fixed.



---

archive/issue_comments_006004.json:
```json
{
    "body": "Merged random_element.hg  in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T02:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6004",
    "user": "mabshoff"
}
```

Merged random_element.hg  in Sage 2.10.1.rc1



---

archive/issue_comments_006005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T02:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/980#issuecomment-6005",
    "user": "mabshoff"
}
```

Resolution: fixed
