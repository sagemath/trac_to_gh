# Issue 239: x^(3/4) powering/coercion issue

archive/issues_000239.json:
```json
{
    "body": "Assignee: somebody\n\n\n\n```\n> Can someone please add support for evaluating say 2^(3/4) or 7^(5/3).\n>  \n> > \n>  \n \nAbout this I just found this bug:\n \nsage: x=maxima('x')\n \nsage: x^(3/4)\n x^3/4\n \nsage: x=maxima('2')\n \nsage: x^150\n 1427247692705959881058285969449495136382746624\n \nsage: x^(3/4)\n 2\n \nsage: maxima(3/4)\n 3/4\n \nGreg\n```\n\nGreg's problem is that the exponent is rounded maybe, since `x^(3/4)` should be the same as `x^(maxima('3/4'))`. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/239\n\n",
    "closed_at": "2007-02-03T17:33:16Z",
    "created_at": "2007-02-03T10:13:33Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "x^(3/4) powering/coercion issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/239",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody



```
> Can someone please add support for evaluating say 2^(3/4) or 7^(5/3).
>  
> > 
>  
 
About this I just found this bug:
 
sage: x=maxima('x')
 
sage: x^(3/4)
 x^3/4
 
sage: x=maxima('2')
 
sage: x^150
 1427247692705959881058285969449495136382746624
 
sage: x^(3/4)
 2
 
sage: maxima(3/4)
 3/4
 
Greg
```

Greg's problem is that the exponent is rounded maybe, since `x^(3/4)` should be the same as `x^(maxima('3/4'))`. 


Issue created by migration from https://trac.sagemath.org/ticket/239





---

archive/issue_comments_001065.json:
```json
{
    "body": "```\nIs this the same bug?  The types involved seem very diverse, but the strange \nresult appears remarkably similar.\n \nsage: CF=CyclotomicField(3)\nsage: two=CF(2)\nsage: two^(1/3)\n1\nsage: me=two^(1/3)\nsage: me.parent()\nCyclotomic Field of order 3 and degree 2\n \n--\n```",
    "created_at": "2007-02-03T16:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/239#issuecomment-1065",
    "user": "https://github.com/williamstein"
}
```

```
Is this the same bug?  The types involved seem very diverse, but the strange 
result appears remarkably similar.
 
sage: CF=CyclotomicField(3)
sage: two=CF(2)
sage: two^(1/3)
1
sage: me=two^(1/3)
sage: me.parent()
Cyclotomic Field of order 3 and degree 2
 
--
```



---

archive/issue_comments_001066.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-03T17:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/239#issuecomment-1066",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000498.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-02-03T17:33:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/239",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/239#event-498"
}
```



---

archive/issue_comments_001067.json:
```json
{
    "body": "This is now fixed for sage 2.1.   The fix involved making __pow__ more careful (to raise an error in many cases).",
    "created_at": "2007-02-03T17:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/239#issuecomment-1067",
    "user": "https://github.com/williamstein"
}
```

This is now fixed for sage 2.1.   The fix involved making __pow__ more careful (to raise an error in many cases).
