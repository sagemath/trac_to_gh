# Issue 4031: Callable symbolic expressions should allow keyword args

archive/issues_004031.json:
```json
{
    "body": "Assignee: tbd\n\nFor consistency with symbolic expressions, callable symbolic expressions should accept keyword arguments.\n\n\n```\nsage: x, y = var('x,y')\nsage: f = x^2 + y^2\nsage: type(f)\n<class 'sage.calculus.calculus.SymbolicArithmetic'>\nsage: f(3,2)\n13\nsage: f(x=3,y=2)\n13\n\nThe desired behavior is\n\nsage: f(x,y) = x^2 + y^2\nsage: type(f)\n<class 'sage.calculus.calculus.CallableSymbolicExpression'>\nsage: f(3,2)\n13\nsage: f(x=3, y=2)\n13\n\nBut the current behavior is\n\nsage: f(x=3, y=2)\nTraceback (most recent call last):\n...\nTypeError: __call__() got an unexpected keyword argument 'y'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4031\n\n",
    "created_at": "2008-09-01T06:25:55Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Callable symbolic expressions should allow keyword args",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4031",
    "user": "jwmerrill"
}
```
Assignee: tbd

For consistency with symbolic expressions, callable symbolic expressions should accept keyword arguments.


```
sage: x, y = var('x,y')
sage: f = x^2 + y^2
sage: type(f)
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: f(3,2)
13
sage: f(x=3,y=2)
13

The desired behavior is

sage: f(x,y) = x^2 + y^2
sage: type(f)
<class 'sage.calculus.calculus.CallableSymbolicExpression'>
sage: f(3,2)
13
sage: f(x=3, y=2)
13

But the current behavior is

sage: f(x=3, y=2)
Traceback (most recent call last):
...
TypeError: __call__() got an unexpected keyword argument 'y'
```



Issue created by migration from https://trac.sagemath.org/ticket/4031





---

archive/issue_comments_029082.json:
```json
{
    "body": "Attachment [add_kwargs.patch](tarball://root/attachments/some-uuid/ticket4031/add_kwargs.patch) by jwmerrill created at 2008-09-01 06:27:23",
    "created_at": "2008-09-01T06:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29082",
    "user": "jwmerrill"
}
```

Attachment [add_kwargs.patch](tarball://root/attachments/some-uuid/ticket4031/add_kwargs.patch) by jwmerrill created at 2008-09-01 06:27:23



---

archive/issue_comments_029083.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-09-01T06:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29083",
    "user": "jwmerrill"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_029084.json:
```json
{
    "body": "The attached patch implements keyword args for callable symbolic expressions, along with doctests.",
    "created_at": "2008-09-01T06:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29084",
    "user": "jwmerrill"
}
```

The attached patch implements keyword args for callable symbolic expressions, along with doctests.



---

archive/issue_comments_029085.json:
```json
{
    "body": "Changing component from algebra to calculus.",
    "created_at": "2008-09-01T06:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29085",
    "user": "jwmerrill"
}
```

Changing component from algebra to calculus.



---

archive/issue_comments_029086.json:
```json
{
    "body": "Changing assignee from tbd to jwmerrill.",
    "created_at": "2008-09-01T06:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29086",
    "user": "jwmerrill"
}
```

Changing assignee from tbd to jwmerrill.



---

archive/issue_comments_029087.json:
```json
{
    "body": "Opps :)",
    "created_at": "2008-09-01T12:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29087",
    "user": "mabshoff"
}
```

Opps :)



---

archive/issue_comments_029088.json:
```json
{
    "body": "Attachment [trac_4031.patch](tarball://root/attachments/some-uuid/ticket4031/trac_4031.patch) by mhansen created at 2008-09-01 22:38:24",
    "created_at": "2008-09-01T22:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29088",
    "user": "mhansen"
}
```

Attachment [trac_4031.patch](tarball://root/attachments/some-uuid/ticket4031/trac_4031.patch) by mhansen created at 2008-09-01 22:38:24



---

archive/issue_comments_029089.json:
```json
{
    "body": "Hello,\n\nI agree with patch, but I tweaked the implementation a bit.  Do you agree with the change jwmerrill?\n\n--Mike",
    "created_at": "2008-09-01T22:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29089",
    "user": "mhansen"
}
```

Hello,

I agree with patch, but I tweaked the implementation a bit.  Do you agree with the change jwmerrill?

--Mike



---

archive/issue_comments_029090.json:
```json
{
    "body": "Also, I forgot to mention that this patch fixes the issue at #4030.",
    "created_at": "2008-09-01T22:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29090",
    "user": "mhansen"
}
```

Also, I forgot to mention that this patch fixes the issue at #4030.



---

archive/issue_comments_029091.json:
```json
{
    "body": "mhansen, I think your implementation is better.  Only trac_4031.patch should be applied.",
    "created_at": "2008-09-01T22:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29091",
    "user": "jwmerrill"
}
```

mhansen, I think your implementation is better.  Only trac_4031.patch should be applied.



---

archive/issue_comments_029092.json:
```json
{
    "body": "\n```\nmhansen: Nope, if you think my patch is good and it works, give the ticket a positive review.\n```\n\n\nwith mhansen's patch, all tests pass.",
    "created_at": "2008-09-01T23:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29092",
    "user": "jwmerrill"
}
```


```
mhansen: Nope, if you think my patch is good and it works, give the ticket a positive review.
```


with mhansen's patch, all tests pass.



---

archive/issue_comments_029093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T10:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29093",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029094.json:
```json
{
    "body": "Merged trac_4031.patch in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T10:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4031#issuecomment-29094",
    "user": "mabshoff"
}
```

Merged trac_4031.patch in Sage 3.1.2.alpha4
