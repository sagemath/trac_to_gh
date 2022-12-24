# Issue 1104: Ideal() should check arguments better

archive/issues_001104.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: ideal arguments\n\n\n```\nsage: Ideal(3, 5)\nPrincipal ideal (3) of Integer Ring\n```\n\n\nMisleading!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1104\n\n",
    "created_at": "2007-11-05T04:21:16Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Ideal() should check arguments better",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1104",
    "user": "ncalexan"
}
```
Assignee: somebody

Keywords: ideal arguments


```
sage: Ideal(3, 5)
Principal ideal (3) of Integer Ring
```


Misleading!

Issue created by migration from https://trac.sagemath.org/ticket/1104





---

archive/issue_comments_006678.json:
```json
{
    "body": "It actually does exactly what it is supposed to do in the documentation [from Ideal?]:\n\n```\n        Alternatively, one can also call this function with the syntax\n             Ideal(gens)\n        where gens is a nonempty list of generators or a single generator.\n```\n\nFrom Sage 2.9.1.1:\n\n```\nsage: R.<x,y> = QQ[]\nsage: R\nMultivariate Polynomial Ring in x, y over Rational Field\nsage: R.ideal(x^2,x-y)\nIdeal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field\nsage: Ideal([x^2,x-y])\nIdeal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field\nsage: Ideal(x^2,x-y)\nPrincipal ideal (x^2) of Multivariate Polynomial Ring in x, y over Rational Field\n```\n",
    "created_at": "2007-12-26T03:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6678",
    "user": "mabshoff"
}
```

It actually does exactly what it is supposed to do in the documentation [from Ideal?]:

```
        Alternatively, one can also call this function with the syntax
             Ideal(gens)
        where gens is a nonempty list of generators or a single generator.
```

From Sage 2.9.1.1:

```
sage: R.<x,y> = QQ[]
sage: R
Multivariate Polynomial Ring in x, y over Rational Field
sage: R.ideal(x^2,x-y)
Ideal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field
sage: Ideal([x^2,x-y])
Ideal (x^2, x - y) of Multivariate Polynomial Ring in x, y over Rational Field
sage: Ideal(x^2,x-y)
Principal ideal (x^2) of Multivariate Polynomial Ring in x, y over Rational Field
```




---

archive/issue_comments_006679.json:
```json
{
    "body": "The patch fixes the problem pointed out by Nick, and makes Ideal() complain loudly rather than return the wrong thing in other cases.\n\nBefore:\n\n\n```\nsage: Ideal(3,5)\nPrincipal ideal (3) of Integer Ring\nsage: Ideal(ZZ,3,5)\nPrincipal ideal (3) of Integer Ring\n```\n\n\nAfter:\n\n\n```\nsage: Ideal(3,5)\nPrincipal ideal (1) of Integer Ring\nsage: Ideal(ZZ,3,5)\n...\n\n<type 'exceptions.TypeError'>: coerce must be either True or False\n```\n",
    "created_at": "2008-02-16T23:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6679",
    "user": "AlexGhitza"
}
```

The patch fixes the problem pointed out by Nick, and makes Ideal() complain loudly rather than return the wrong thing in other cases.

Before:


```
sage: Ideal(3,5)
Principal ideal (3) of Integer Ring
sage: Ideal(ZZ,3,5)
Principal ideal (3) of Integer Ring
```


After:


```
sage: Ideal(3,5)
Principal ideal (1) of Integer Ring
sage: Ideal(ZZ,3,5)
...

<type 'exceptions.TypeError'>: coerce must be either True or False
```




---

archive/issue_comments_006680.json:
```json
{
    "body": "Sorry this patch doesn't work right. With the patch I get for example:\n\n```\nsage: Ideal(2, 4, 6)\n[...]\n<type 'exceptions.TypeError'>: coerce must be either True or False\n```\n\nwhich is still very confusing.\n\nThe recursive function call is not the right way to do this. Should use the `def func(*x, **kwds)` idiom instead; to see an example, look at\n\n```\nsage: R.<x> = PolynomialRing(ZZ)\nsage: R.ideal??\n```\n",
    "created_at": "2008-02-23T02:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6680",
    "user": "dmharvey"
}
```

Sorry this patch doesn't work right. With the patch I get for example:

```
sage: Ideal(2, 4, 6)
[...]
<type 'exceptions.TypeError'>: coerce must be either True or False
```

which is still very confusing.

The recursive function call is not the right way to do this. Should use the `def func(*x, **kwds)` idiom instead; to see an example, look at

```
sage: R.<x> = PolynomialRing(ZZ)
sage: R.ideal??
```




---

archive/issue_comments_006681.json:
```json
{
    "body": "Changing keywords from \"ideal arguments\" to \"ideal arguments, editor_malb\".",
    "created_at": "2008-06-20T04:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6681",
    "user": "craigcitro"
}
```

Changing keywords from "ideal arguments" to "ideal arguments, editor_malb".



---

archive/issue_comments_006682.json:
```json
{
    "body": "**state of affairs for editorial meeting 26/06/08**\nNo movement on my end, sorry.",
    "created_at": "2008-06-25T11:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6682",
    "user": "malb"
}
```

**state of affairs for editorial meeting 26/06/08**
No movement on my end, sorry.



---

archive/issue_comments_006683.json:
```json
{
    "body": "Change the subject line. \n\nmalb: any hope for this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T22:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6683",
    "user": "mabshoff"
}
```

Change the subject line. 

malb: any hope for this ticket?

Cheers,

Michael



---

archive/issue_comments_006684.json:
```json
{
    "body": "Attachment [1104-Ideal_args.patch](tarball://root/attachments/some-uuid/ticket1104/1104-Ideal_args.patch) by AlexGhitza created at 2008-09-29 23:17:56",
    "created_at": "2008-09-29T23:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6684",
    "user": "AlexGhitza"
}
```

Attachment [1104-Ideal_args.patch](tarball://root/attachments/some-uuid/ticket1104/1104-Ideal_args.patch) by AlexGhitza created at 2008-09-29 23:17:56



---

archive/issue_comments_006685.json:
```json
{
    "body": "I have completely rewritten the patch in a way that I think addresses the objections given above.",
    "created_at": "2008-09-29T23:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6685",
    "user": "AlexGhitza"
}
```

I have completely rewritten the patch in a way that I think addresses the objections given above.



---

archive/issue_comments_006686.json:
```json
{
    "body": "Patch applies cleanly against 3.1.2 and reads good.",
    "created_at": "2008-09-30T10:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6686",
    "user": "malb"
}
```

Patch applies cleanly against 3.1.2 and reads good.



---

archive/issue_comments_006687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-30T11:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6687",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006688.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-30T11:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1104#issuecomment-6688",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
