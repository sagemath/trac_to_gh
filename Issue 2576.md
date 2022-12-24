# Issue 2576: preserve docstrings of decorated methods

archive/issues_002576.json:
```json
{
    "body": "Assignee: tba\n\n\n```\n\nHi,\n\nHow does one preserve the behavior of docstrings when using\ndecorators?  I just noticed, for example, that I couldn't easily\naccess the docstring of various things in rings/polynomial/\nmulti_polynomial_ideal.py because they have been decorated.  It is\nunclear to me how to easily fix that - does anyone know a simple\nsolution?\n\nThanks,\nM. Hampton\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2576\n\n",
    "created_at": "2008-03-17T18:50:10Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "preserve docstrings of decorated methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2576",
    "user": "@williamstein"
}
```
Assignee: tba


```

Hi,

How does one preserve the behavior of docstrings when using
decorators?  I just noticed, for example, that I couldn't easily
access the docstring of various things in rings/polynomial/
multi_polynomial_ideal.py because they have been decorated.  It is
unclear to me how to easily fix that - does anyone know a simple
solution?

Thanks,
M. Hampton
```


Issue created by migration from https://trac.sagemath.org/ticket/2576





---

archive/issue_comments_017607.json:
```json
{
    "body": "this fixes one particular instance of the problem",
    "created_at": "2008-03-17T18:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17607",
    "user": "@williamstein"
}
```

this fixes one particular instance of the problem



---

archive/issue_comments_017608.json:
```json
{
    "body": "Attachment [sage-2576.patch](tarball://root/attachments/some-uuid/ticket2576/sage-2576.patch) by @williamstein created at 2008-03-17 18:52:06\n\nTo test the attached:\n\n```\nR.<x,y,z> = PolynomialRing(QQ, 3, order='lex')\np = z^2 + 1; q = z^3 + 2\nI = (p*q^2, y-z^2)*R\npd = I.complete_primary_decomposition?\n```\n",
    "created_at": "2008-03-17T18:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17608",
    "user": "@williamstein"
}
```

Attachment [sage-2576.patch](tarball://root/attachments/some-uuid/ticket2576/sage-2576.patch) by @williamstein created at 2008-03-17 18:52:06

To test the attached:

```
R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
p = z^2 + 1; q = z^3 + 2
I = (p*q^2, y-z^2)*R
pd = I.complete_primary_decomposition?
```




---

archive/issue_comments_017609.json:
```json
{
    "body": "Michael Brickenstein on [sage-devel]:\n\n```\nBy the way\nwrapper.__name__=func.__name__\nis usually also a good practice.\n```\n",
    "created_at": "2008-03-17T23:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17609",
    "user": "@malb"
}
```

Michael Brickenstein on [sage-devel]:

```
By the way
wrapper.__name__=func.__name__
is usually also a good practice.
```




---

archive/issue_comments_017610.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> To test the attached:\n> {{{\n> R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')\n> p = z^2 + 1; q = z^3 + 2\n> I = (p*q^2, y-z^2)*R\n> pd = I.complete_primary_decomposition?\n> }}}\n\nTo test you need \n\n```\nR.<x,y,z> = PolynomialRing(QQ, 3, order='lex')\np = z^2 + 1; q = z^3 + 2\nI = (p*q^2, y-z^2)*R\nI.complete_primary_decomposition?\n```\n \nAt least I did. Anyway, the patch applies and does what it is supposed to do. Positive review.",
    "created_at": "2008-03-18T00:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17610",
    "user": "mabshoff"
}
```

Replying to [comment:1 was]:
> To test the attached:
> {{{
> R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
> p = z^2 + 1; q = z^3 + 2
> I = (p*q^2, y-z^2)*R
> pd = I.complete_primary_decomposition?
> }}}

To test you need 

```
R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
p = z^2 + 1; q = z^3 + 2
I = (p*q^2, y-z^2)*R
I.complete_primary_decomposition?
```
 
At least I did. Anyway, the patch applies and does what it is supposed to do. Positive review.



---

archive/issue_comments_017611.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T00:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17611",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017612.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-18T00:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2576#issuecomment-17612",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
