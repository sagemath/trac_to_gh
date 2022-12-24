# Issue 7537: list(SR('c').iterator()) is empty

archive/issues_007537.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  burcin\n\nThis looks like a bug to me:\n\n\n```\nsage: list(SR('c+1').iterator())\n[c, 1]\nsage: list(SR('c').iterator())\n[]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7537\n\n",
    "created_at": "2009-11-26T17:41:35Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "title": "list(SR('c').iterator()) is empty",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7537",
    "user": "malb"
}
```
Assignee: burcin

CC:  burcin

This looks like a bug to me:


```
sage: list(SR('c+1').iterator())
[c, 1]
sage: list(SR('c').iterator())
[]
```


Issue created by migration from https://trac.sagemath.org/ticket/7537





---

archive/issue_comments_063922.json:
```json
{
    "body": "I don't think this is a bug. :)\n\nIt doesn't make sense to iterate over variables, constants or numeric coefficients. Iterators are only available over `add`, `mul`, and `pow` objects, which correspond to the obvious mathematical operations.\n\nAFAICT, this is also the case in MMA:\n\n\n```\nMathematica 7.0 for Linux x86 (32-bit)\nCopyright 1988-2008 Wolfram Research, Inc.\n\nIn[1]:= T=x+1\nOut[1]= 1 + x\nIn[2]:= T\nOut[2]= 1 + x\nIn[3]:= T[[1]]\nOut[3]= 1\nIn[4]:= X\nOut[4]= X\nIn[5]:= X[[1]]\nPart::partd: Part specification X[[1]] is longer than depth of object.\nOut[5]= X[[1]]\n```\n\n\nWe can raise a `ValueError` if the expression corresponds to a `symbol`, `constant` or `numeric` object. The docstring should also be enhanced to point to the data structure for symbolic expressions here:\n\nhttp://www.ginac.de/tutorial/Internal-representation-of-products-and-sums.html\n\nComments?",
    "created_at": "2010-02-25T13:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63922",
    "user": "burcin"
}
```

I don't think this is a bug. :)

It doesn't make sense to iterate over variables, constants or numeric coefficients. Iterators are only available over `add`, `mul`, and `pow` objects, which correspond to the obvious mathematical operations.

AFAICT, this is also the case in MMA:


```
Mathematica 7.0 for Linux x86 (32-bit)
Copyright 1988-2008 Wolfram Research, Inc.

In[1]:= T=x+1
Out[1]= 1 + x
In[2]:= T
Out[2]= 1 + x
In[3]:= T[[1]]
Out[3]= 1
In[4]:= X
Out[4]= X
In[5]:= X[[1]]
Part::partd: Part specification X[[1]] is longer than depth of object.
Out[5]= X[[1]]
```


We can raise a `ValueError` if the expression corresponds to a `symbol`, `constant` or `numeric` object. The docstring should also be enhanced to point to the data structure for symbolic expressions here:

http://www.ginac.de/tutorial/Internal-representation-of-products-and-sums.html

Comments?



---

archive/issue_comments_063923.json:
```json
{
    "body": "I see your point but why not return `self` in that case?",
    "created_at": "2010-02-25T13:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63923",
    "user": "malb"
}
```

I see your point but why not return `self` in that case?



---

archive/issue_comments_063924.json:
```json
{
    "body": "Do you mean return an iterable which returns `self` when `.next()` is called? \n\nIf you're traversing a symbolic expression, and working with iterators, I can't think of any case where symbols, constants and numeric coefficients don't form a special case which will be treated separately. The usual way to write code to traverse the expression tree should check if `.operator()` returns `None`.\n\nI admit that I don't use this interface often enough to decide on the design though. The recent thread on sage-devel about indexing parts of expressions also shows that this needs work.\n\nDo you have a use case we can work from? How did you run into this?",
    "created_at": "2010-02-25T14:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63924",
    "user": "burcin"
}
```

Do you mean return an iterable which returns `self` when `.next()` is called? 

If you're traversing a symbolic expression, and working with iterators, I can't think of any case where symbols, constants and numeric coefficients don't form a special case which will be treated separately. The usual way to write code to traverse the expression tree should check if `.operator()` returns `None`.

I admit that I don't use this interface often enough to decide on the design though. The recent thread on sage-devel about indexing parts of expressions also shows that this needs work.

Do you have a use case we can work from? How did you run into this?



---

archive/issue_comments_063925.json:
```json
{
    "body": "I am converting boolean polynomials to Integer Programming problems, for this I convert them to symbolic expressions first and then to MIP. Probably not the most natural application.",
    "created_at": "2010-02-25T14:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63925",
    "user": "malb"
}
```

I am converting boolean polynomials to Integer Programming problems, for this I convert them to symbolic expressions first and then to MIP. Probably not the most natural application.



---

archive/issue_comments_063926.json:
```json
{
    "body": "So let's close this bug then?",
    "created_at": "2010-07-14T13:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63926",
    "user": "malb"
}
```

So let's close this bug then?



---

archive/issue_comments_063927.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-26T14:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63927",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063928.json:
```json
{
    "body": "With attachment:trac_7537-iterator.patch we get an error when trying to iterate over symbols, constants or numeric objects:\n\n\n```\nsage: x.iterator()\nTraceback (most recent call last):\n...\nValueError: cannot iterate over numeric, constant or symbol\nsage: pi.iterator()\nTraceback (most recent call last):\n...\nValueError: cannot iterate over numeric, constant or symbol\nsage: SR(5).iterator()\nTraceback (most recent call last):\n...\nValueError: cannot iterate over numeric, constant or symbol\n```\n\n\nThis patch depends on #9989 (not in terms of functionality, but it will fail to apply since the patch there touches the same part of `sage/symbolic/expression.pyx`).",
    "created_at": "2010-09-26T14:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63928",
    "user": "burcin"
}
```

With attachment:trac_7537-iterator.patch we get an error when trying to iterate over symbols, constants or numeric objects:


```
sage: x.iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
sage: pi.iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
sage: SR(5).iterator()
Traceback (most recent call last):
...
ValueError: cannot iterate over numeric, constant or symbol
```


This patch depends on #9989 (not in terms of functionality, but it will fail to apply since the patch there touches the same part of `sage/symbolic/expression.pyx`).



---

archive/issue_comments_063929.json:
```json
{
    "body": "Attachment [trac_7537-iterator.patch](tarball://root/attachments/some-uuid/ticket7537/trac_7537-iterator.patch) by burcin created at 2011-03-23 12:08:20",
    "created_at": "2011-03-23T12:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63929",
    "user": "burcin"
}
```

Attachment [trac_7537-iterator.patch](tarball://root/attachments/some-uuid/ticket7537/trac_7537-iterator.patch) by burcin created at 2011-03-23 12:08:20



---

archive/issue_comments_063930.json:
```json
{
    "body": "I updated the patch with a new error message recommended in #9989.",
    "created_at": "2011-03-23T12:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63930",
    "user": "burcin"
}
```

I updated the patch with a new error message recommended in #9989.



---

archive/issue_comments_063931.json:
```json
{
    "body": "Patch looks good, applies cleanly against 4.7.alpha2 and doctests pass.",
    "created_at": "2011-03-24T14:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63931",
    "user": "malb"
}
```

Patch looks good, applies cleanly against 4.7.alpha2 and doctests pass.



---

archive/issue_comments_063932.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-24T14:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63932",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-28T07:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7537#issuecomment-63933",
    "user": "jdemeyer"
}
```

Resolution: fixed
