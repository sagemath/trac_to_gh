# Issue 2148: [with patch, positive review] PolyBoRi monomial orders are wrong

archive/issues_002148.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @malb\n\nKeywords: polybori\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2),2,order='degrevlex')\nsage: x > y\nTrue\n\nsage: P.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\nsage: x > y\nFalse\n```\n\nThis should be changed because it leads to funny performance figures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2148\n\n",
    "closed_at": "2008-03-18T00:08:24Z",
    "created_at": "2008-02-13T13:06:07Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] PolyBoRi monomial orders are wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2148",
    "user": "https://github.com/malb"
}
```
Assignee: @burcin

CC:  @malb

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

archive/issue_comments_014060.json:
```json
{
    "body": "Attachment [2148-polybori_monomial_order_keywords.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori_monomial_order_keywords.patch) by @burcin created at 2008-02-17 16:51:36\n\nfix monomial order keywords in polybori wrapper",
    "created_at": "2008-02-17T16:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14060",
    "user": "https://github.com/burcin"
}
```

Attachment [2148-polybori_monomial_order_keywords.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori_monomial_order_keywords.patch) by @burcin created at 2008-02-17 16:51:36

fix monomial order keywords in polybori wrapper



---

archive/issue_comments_014061.json:
```json
{
    "body": "Changing assignee from @malb to @burcin.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14061",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @malb to @burcin.



---

archive/issue_comments_014062.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14062",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014063.json:
```json
{
    "body": "attachment:2148-polybori_monomial_order_keywords.patch corrects the monomial order keywords in the `PolyBoRi` wrapper.",
    "created_at": "2008-02-17T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14063",
    "user": "https://github.com/burcin"
}
```

attachment:2148-polybori_monomial_order_keywords.patch corrects the monomial order keywords in the `PolyBoRi` wrapper.



---

archive/issue_comments_014064.json:
```json
{
    "body": "I am not convinced the patch fixes the issue:\n\n'dp' and 'Dp' refer to degrevlex and deglex respectively and in neither of those x < y.\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2),order='degrevlex')\nsage: x > y\nTrue\nsage: P.<x,y> = PolynomialRing(GF(2),order='deglex')\nsage: x > y\nTrue\n```\n\nHowever, there is a deglex with variables inverted ordering ib PolyBoRi which has no Singular/Sage equivalent AFAIK:\n\n```\nsage: B.<x,y> = BooleanPolynomialRing(2,order='deglex')\nsage: x > y\nTrue\nsage: B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\nsage: x > y\nFalse\n```",
    "created_at": "2008-02-17T17:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14064",
    "user": "https://github.com/malb"
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

archive/issue_comments_014065.json:
```json
{
    "body": "You're right, it's not so simple. I'll look at it a bit more.",
    "created_at": "2008-02-17T18:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14065",
    "user": "https://github.com/burcin"
}
```

You're right, it's not so simple. I'll look at it a bit more.



---

archive/issue_comments_014066.json:
```json
{
    "body": "```\nOn Wed, 20 Feb 2008 10:40:09 +0100\nAlexander Dreyer <alexander.dreyer@itwm.fraunhofer.de> wrote:\n\n> PolyBoRi does not implement degrevlex (dp), but a variant, which we\n> called dp_asc. It is adp (not a dlex, as Martin states), but with\n> variables reversed. The reason for this was, that this can be\n> implemented more efficiently on our ZDD-based data structure. So, for\n> correcting the command\n> \n> B.<x,y> = BooleanPolynomialRing(2,order='degrevlex')\n> \n> you have to reverse the variable vector before it is returned to <x, y>.\n> (If there's something like BooleanVariable(idx), it has to be mapped to\n> BooleVariable(n-idx).)\n```",
    "created_at": "2008-02-27T09:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14066",
    "user": "https://github.com/burcin"
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

archive/issue_comments_014067.json:
```json
{
    "body": "reverse variables for degrevlex to dp_asc conversion",
    "created_at": "2008-03-08T13:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14067",
    "user": "https://github.com/burcin"
}
```

reverse variables for degrevlex to dp_asc conversion



---

archive/issue_comments_014068.json:
```json
{
    "body": "Attachment [2148-polybori-fix_degrevlex.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori-fix_degrevlex.patch) by @burcin created at 2008-03-08 13:31:46\n\nattachment:2148-polybori-fix_degrevlex.patch arranges the variable indexes in the Sage - `PolyBoRi` interface to handle the difference between degrevlex and dp_asc orders.\n\nNote that with this patch, printing is reversed when using dp_asc orders:\n\n```\nsage: P.<x,y,z> = BooleanPolynomialRing(3,order='degrevlex')\nsage: x*y*z\nz*y*x\nsage: P.<x,y,z> = BooleanPolynomialRing(3,order='lex')\nsage: x*y*z\nx*y*z\n```",
    "created_at": "2008-03-08T13:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14068",
    "user": "https://github.com/burcin"
}
```

Attachment [2148-polybori-fix_degrevlex.patch](tarball://root/attachments/some-uuid/ticket2148/2148-polybori-fix_degrevlex.patch) by @burcin created at 2008-03-08 13:31:46

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

archive/issue_events_005137.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:02:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2148#event-5137"
}
```



---

archive/issue_comments_014069.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-16T18:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14069",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_014070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T00:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014071.json:
```json
{
    "body": "Merged 2148-polybori-fix_degrevlex.patch in Sage 2.11.alpha0",
    "created_at": "2008-03-18T00:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2148#issuecomment-14071",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2148-polybori-fix_degrevlex.patch in Sage 2.11.alpha0



---

archive/issue_events_005138.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T00:08:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2148",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2148#event-5138"
}
```
