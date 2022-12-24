# Issue 2148: PolyBoRi inconsistency

archive/issues_002148.json:
```json
{
    "body": "Assignee: malb\n\nCC:  malb\n\nKeywords: polybori\n\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2),2,order='degrevlex')\nsage: x > y\nTrue\n\nsage: P.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\nsage: x > y\nFalse\n```\n\n\nThis should be changed because it leads to funny performance figures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2148\n\n",
    "created_at": "2008-02-13T13:06:07Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "PolyBoRi inconsistency",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2148",
    "user": "malb"
}
```
Assignee: malb

CC:  malb

Keywords: polybori


```
sage: P.<x,y> = PolynomialRing(GF(2),2,order='degrevlex')
sage: x > y
True

sage: P.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
sage: x > y
False
```


This should be changed because it leads to funny performance figures.

Issue created by migration from https://trac.sagemath.org/ticket/2148





---

archive/issue_comments_014091.json:
```json
{
    "body": "Attachment [2148-polybori_monomial_order_keywords.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori_monomial_order_keywords.patch) by burcin created at 2008-02-17 16:51:36\n\nfix monomial order keywords in polybori wrapper",
    "created_at": "2008-02-17T16:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14091",
    "user": "burcin"
}
```

Attachment [2148-polybori_monomial_order_keywords.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori_monomial_order_keywords.patch) by burcin created at 2008-02-17 16:51:36

fix monomial order keywords in polybori wrapper



---

archive/issue_comments_014092.json:
```json
{
    "body": "Changing assignee from malb to burcin.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14092",
    "user": "burcin"
}
```

Changing assignee from malb to burcin.



---

archive/issue_comments_014093.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14093",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014094.json:
```json
{
    "body": "attachment:2148-polybori_monomial_order_keywords.patch corrects the monomial order keywords in the `PolyBoRi` wrapper.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14094",
    "user": "burcin"
}
```

attachment:2148-polybori_monomial_order_keywords.patch corrects the monomial order keywords in the `PolyBoRi` wrapper.



---

archive/issue_comments_014095.json:
```json
{
    "body": "I am not convinced the patch fixes the issue:\n\n'dp' and 'Dp' refer to degrevlex and deglex respectively and in neither of those x < y.\n\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2),order='degrevlex')\nsage: x > y\nTrue\nsage: P.<x,y> = PolynomialRing(GF(2),order='deglex')\nsage: x > y\nTrue\n```\n\n\nHowever, there is a deglex with variables inverted ordering ib PolyBoRi which has no Singular/Sage equivalent AFAIK:\n\n\n```\nsage: B.<x,y> = BooleanPolynomialRing(2,order='deglex')\nsage: x > y\nTrue\nsage: B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\nsage: x > y\nFalse\n```\n",
    "created_at": "2008-02-17T17:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14095",
    "user": "malb"
}
```

I am not convinced the patch fixes the issue:

'dp' and 'Dp' refer to degrevlex and deglex respectively and in neither of those x < y.


```
sage: P.<x,y> = PolynomialRing(GF(2),order='degrevlex')
sage: x > y
True
sage: P.<x,y> = PolynomialRing(GF(2),order='deglex')
sage: x > y
True
```


However, there is a deglex with variables inverted ordering ib PolyBoRi which has no Singular/Sage equivalent AFAIK:


```
sage: B.<x,y> = BooleanPolynomialRing(2,order='deglex')
sage: x > y
True
sage: B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
sage: x > y
False
```




---

archive/issue_comments_014096.json:
```json
{
    "body": "You're right, it's not so simple. I'll look at it a bit more.",
    "created_at": "2008-02-17T18:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14096",
    "user": "burcin"
}
```

You're right, it's not so simple. I'll look at it a bit more.



---

archive/issue_comments_014097.json:
```json
{
    "body": "\n```\nOn Wed, 20 Feb 2008 10:40:09 +0100\nAlexander Dreyer <alexander.dreyer@itwm.fraunhofer.de> wrote:\n\n> PolyBoRi does not implement degrevlex (dp), but a variant, which we\n> called dp_asc. It is adp (not a dlex, as Martin states), but with\n> variables reversed. The reason for this was, that this can be\n> implemented more efficiently on our ZDD-based data structure. So, for\n> correcting the command\n> \n> B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\n> \n> you have to reverse the variable vector before it is returned to <x, y>.\n> (If there's something like BooleanVariable(idx), it has to be mapped to\n> BooleVariable(n-idx).)\n```\n",
    "created_at": "2008-02-27T09:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14097",
    "user": "burcin"
}
```


```
On Wed, 20 Feb 2008 10:40:09 +0100
Alexander Dreyer <alexander.dreyer@itwm.fraunhofer.de> wrote:

> PolyBoRi does not implement degrevlex (dp), but a variant, which we
> called dp_asc. It is adp (not a dlex, as Martin states), but with
> variables reversed. The reason for this was, that this can be
> implemented more efficiently on our ZDD-based data structure. So, for
> correcting the command
> 
> B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')
> 
> you have to reverse the variable vector before it is returned to <x, y>.
> (If there's something like BooleanVariable(idx), it has to be mapped to
> BooleVariable(n-idx).)
```




---

archive/issue_comments_014098.json:
```json
{
    "body": "reverse variables for degrevlex to dp_asc conversion",
    "created_at": "2008-03-08T13:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14098",
    "user": "burcin"
}
```

reverse variables for degrevlex to dp_asc conversion



---

archive/issue_comments_014099.json:
```json
{
    "body": "Attachment [2148-polybori-fix_degrevlex.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori-fix_degrevlex.patch) by burcin created at 2008-03-08 13:31:46\n\nattachment:2148-polybori-fix_degrevlex.patch arranges the variable indexes in the Sage - `PolyBoRi` interface to handle the difference between degrevlex and dp_asc orders.\n\nNote that with this patch, printing is reversed when using dp_asc orders:\n\n\n```\nsage: P.<x,y,z> = BooleanPolynomialRing(3,order='degrevlex')\nsage: x*y*z\nz*y*x\nsage: P.<x,y,z> = BooleanPolynomialRing(3,order='lex')\nsage: x*y*z\nx*y*z\n```\n",
    "created_at": "2008-03-08T13:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14099",
    "user": "burcin"
}
```

Attachment [2148-polybori-fix_degrevlex.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori-fix_degrevlex.patch) by burcin created at 2008-03-08 13:31:46

attachment:2148-polybori-fix_degrevlex.patch arranges the variable indexes in the Sage - `PolyBoRi` interface to handle the difference between degrevlex and dp_asc orders.

Note that with this patch, printing is reversed when using dp_asc orders:


```
sage: P.<x,y,z> = BooleanPolynomialRing(3,order='degrevlex')
sage: x*y*z
z*y*x
sage: P.<x,y,z> = BooleanPolynomialRing(3,order='lex')
sage: x*y*z
x*y*z
```




---

archive/issue_comments_014100.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-16T18:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14100",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_014101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T00:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14101",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014102.json:
```json
{
    "body": "Merged 2148-polybori-fix_degrevlex.patch in Sage 2.11.alpha0",
    "created_at": "2008-03-18T00:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14102",
    "user": "mabshoff"
}
```

Merged 2148-polybori-fix_degrevlex.patch in Sage 2.11.alpha0
