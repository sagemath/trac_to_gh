# Issue 7084: Make assumption comparison work for GenericDeclarations

archive/issues_007084.json:
```json
{
    "body": "On Sep 30, 11:07 am, lutusp <lut...`@`gmail.com> wrote:\n> I find I cannot make more than one of a certain kind of assume\n> statement:\n> \n> sage: assume(a,'real')\n> sage: assume(b,'real')\n> \n> If I do, I get an error message:\n> \n> AttributeError: 'GenericDeclaration' object has no attribute\n> 'variables'\n\nIt's comparing your second assumption with the first one, presumably to make sure it doesn't conflict (?) ... but it is strange that it is talking about an attribute variables, since the attribute _var is being called, and b is real has that.\n\nThe problem is in symbolic/expression.pyx, where __nonzero__ tries to find the variable of  \"a is real\" - but it only has a _var, not variables like \"t>0\", which is a symbolic expression.\n\n> \n> One such assumption is accepted, but not two. But more typical\n> assumptions are accepted:\n> \n> sage: forget()\n> sage: assume(a > 0)\n> sage: assume(b > 0)\n> sage: assume(c > 0)\n> sage: assumptions()\n> \n> [a > 0, b > 0, c > 0]\n> \n> Am I using the wrong syntax or is this a bug?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7084\n\n",
    "created_at": "2009-09-30T15:30:46Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Make assumption comparison work for GenericDeclarations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7084",
    "user": "kcrisman"
}
```
On Sep 30, 11:07 am, lutusp <lut...`@`gmail.com> wrote:
> I find I cannot make more than one of a certain kind of assume
> statement:
> 
> sage: assume(a,'real')
> sage: assume(b,'real')
> 
> If I do, I get an error message:
> 
> AttributeError: 'GenericDeclaration' object has no attribute
> 'variables'

It's comparing your second assumption with the first one, presumably to make sure it doesn't conflict (?) ... but it is strange that it is talking about an attribute variables, since the attribute _var is being called, and b is real has that.

The problem is in symbolic/expression.pyx, where __nonzero__ tries to find the variable of  "a is real" - but it only has a _var, not variables like "t>0", which is a symbolic expression.

> 
> One such assumption is accepted, but not two. But more typical
> assumptions are accepted:
> 
> sage: forget()
> sage: assume(a > 0)
> sage: assume(b > 0)
> sage: assume(c > 0)
> sage: assumptions()
> 
> [a > 0, b > 0, c > 0]
> 
> Am I using the wrong syntax or is this a bug?

Issue created by migration from https://trac.sagemath.org/ticket/7084





---

archive/issue_comments_058555.json:
```json
{
    "body": "This should fix it.",
    "created_at": "2009-09-30T18:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7084#issuecomment-58555",
    "user": "kcrisman"
}
```

This should fix it.



---

archive/issue_comments_058556.json:
```json
{
    "body": "Attachment [trac_7084-assumptions.patch](tarball://root/attachments/some-uuid/ticket7084/trac_7084-assumptions.patch) by kcrisman created at 2009-09-30 18:16:01\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-09-30T18:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7084#issuecomment-58556",
    "user": "kcrisman"
}
```

Attachment [trac_7084-assumptions.patch](tarball://root/attachments/some-uuid/ticket7084/trac_7084-assumptions.patch) by kcrisman created at 2009-09-30 18:16:01

Based on 4.1.2.alpha4



---

archive/issue_comments_058557.json:
```json
{
    "body": "Tests look good. Doctests run perfectly. Positive review.",
    "created_at": "2009-10-01T03:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7084#issuecomment-58557",
    "user": "timdumol"
}
```

Tests look good. Doctests run perfectly. Positive review.



---

archive/issue_comments_058558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7084#issuecomment-58558",
    "user": "mhansen"
}
```

Resolution: fixed
