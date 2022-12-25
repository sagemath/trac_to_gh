# Issue 4988: major easy-to-fix but STUPID bug in gcd

archive/issues_004988.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is stupid:\n\n\n```\nsage: gcd(3,6,2)\n3\n```\n\n\nThe problem is that there is an undocumented mysterious and not even used integer third input!\n\n```\nFile:        /Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py\nType:        <type 'function'>\nDefinition:  gcd(a, b, integer, **kwargs)\nDocstring: \n\n    The greatest common divisor of a and b, or if a is a list and b is\n    omitted the greatest common divisor of all elements of a.\n\n    INPUT:\n        a,b -- two elements of a ring with gcd\n    or\n        a -- a list or tuple of elements of a ring with gcd\n\n    Additional keyword arguments are passed to the respectively called\n    methods.\n\n    EXAMPLES:\n        sage: GCD(97,100)\n        1\n        sage: GCD(97*10^15, 19^20*97^2)\n        97\n        sage: GCD(2/3, 4/3)\n        2/3\n        sage: GCD([2,4,6,8])\n        2\n        sage: GCD(srange(0,10000,10))  # fast  !!\n        10\n```\n\n\nThis caused me a ton of confusion just now.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4988\n\n",
    "created_at": "2009-01-16T21:12:25Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "major easy-to-fix but STUPID bug in gcd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4988",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is stupid:


```
sage: gcd(3,6,2)
3
```


The problem is that there is an undocumented mysterious and not even used integer third input!

```
File:        /Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py
Type:        <type 'function'>
Definition:  gcd(a, b, integer, **kwargs)
Docstring: 

    The greatest common divisor of a and b, or if a is a list and b is
    omitted the greatest common divisor of all elements of a.

    INPUT:
        a,b -- two elements of a ring with gcd
    or
        a -- a list or tuple of elements of a ring with gcd

    Additional keyword arguments are passed to the respectively called
    methods.

    EXAMPLES:
        sage: GCD(97,100)
        1
        sage: GCD(97*10^15, 19^20*97^2)
        97
        sage: GCD(2/3, 4/3)
        2/3
        sage: GCD([2,4,6,8])
        2
        sage: GCD(srange(0,10000,10))  # fast  !!
        10
```


This caused me a ton of confusion just now.  

Issue created by migration from https://trac.sagemath.org/ticket/4988





---

archive/issue_comments_037997.json:
```json
{
    "body": "Attachment [trac_4988.patch](tarball://root/attachments/some-uuid/ticket4988/trac_4988.patch) by @JohnCremona created at 2009-01-18 18:39:27",
    "created_at": "2009-01-18T18:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4988#issuecomment-37997",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4988.patch](tarball://root/attachments/some-uuid/ticket4988/trac_4988.patch) by @JohnCremona created at 2009-01-18 18:39:27



---

archive/issue_comments_037998.json:
```json
{
    "body": "Patch attached.  I deleted the now redundant integer parameter (which once was used to tell the function to use integer-specific code and is now redundant).  I added a relevant doctest and some more so hopefully William's confusion will never again occur (in someone else, I mean ;)).  I discovered some places which still had \"integer=True\" in gcd calls and fixed those.  I tested all rings/ and used search_src() to find any other places where \"integer=True\" might have been used, and found that search_src(\"integer=True\") runs for ever while producing no output.",
    "created_at": "2009-01-18T18:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4988#issuecomment-37998",
    "user": "https://github.com/JohnCremona"
}
```

Patch attached.  I deleted the now redundant integer parameter (which once was used to tell the function to use integer-specific code and is now redundant).  I added a relevant doctest and some more so hopefully William's confusion will never again occur (in someone else, I mean ;)).  I discovered some places which still had "integer=True" in gcd calls and fixed those.  I tested all rings/ and used search_src() to find any other places where "integer=True" might have been used, and found that search_src("integer=True") runs for ever while producing no output.



---

archive/issue_comments_037999.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-01-21T07:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4988#issuecomment-37999",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_038000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4988#issuecomment-38000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011545.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:54:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4988#event-11545"
}
```



---

archive/issue_comments_038001.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4988#issuecomment-38001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1
