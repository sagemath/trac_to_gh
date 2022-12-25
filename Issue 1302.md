# Issue 1302: bug in laurent_series integration

archive/issues_001302.json:
```json
{
    "body": "Assignee: somebody\n\n```\nOn Nov 28, 2007 10:43 AM, Jennifer S. Balakrishnan <> wrote:\n> I'm trying to integrate a list of Laurent series, and it seems that\n> once the list has more than 4 elements, Sage gets upset:\n\nThe problem is:\n\nsage: A.<t> = LaurentSeriesRing(QQ)\nsage: (-2*t^(-4) + O(t^8)).integral()\nTraceback (most recent call last):\n...\nIndexError: list index out of range\n\nThis is because of  this code in rings/laurent_series_ring_element.pyx not\nbeing coded correctly around line 880:\n        if n < 0:\n            v = [a[i]/(n+i+1) for i in range(-1-n)] + [0]\n        else:\n            v = []\n        v += [a[i]/(n+i+1) for i in range(max(-n,0), len(a))]\n\ttry:\n\nSo you should fix that and submit a patch :-).\n\nWilliam\n\n\n\n> \n> sage: A.<t> = LaurentSeriesRing(QQ)\n> sage: B = [-2*t^4 + O(t^16), -2*t^2 + O(t^14), -2 + O(t^12), -2*t^-2 +\n> O(t^10), -2*t^-4 + O(t^8), -2*t^-6 + O(t^6)]\n> sage: for i in range(6):\n> ....:     B[i] = integral(B[i])\n> ....:\n> ---------------------------------------------------------------------------\n> <type 'exceptions.IndexError'>            Traceback (most recent call last)\n> \n> /home/jen/<ipython console> in <module>()\n> \n> /home/jen/sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux/local/lib/python2.5/site-packages/sage/misc/functional.py\n> in integral(x, *args, **kwds)\n>     449     \"\"\"\n>     450     if hasattr(x, 'integral'):\n> --> 451         return x.integral(*args, **kwds)\n>     452     else:\n>     453         from sage.calculus.calculus import SR\n> \n> /home/jen/laurent_series_ring_element.pyx in\n> sage.rings.laurent_series_ring_element.LaurentSeries.integral()\n> \n> <type 'exceptions.IndexError'>: list index out of range\n> sage: B\n> \n> [-2/5*t^5 + O(t^17),\n>  -2/3*t^3 + O(t^15),\n>  -2*t + O(t^13),\n>  2*t^-1 + O(t^11),\n>  -2*t^-4 + O(t^8),        <================== stopped integrating here\n>  -2*t^-6 + O(t^6)]\n> \n> What's going on?\n> \n> Jen\n> \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1302\n\n",
    "created_at": "2007-11-28T19:05:46Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "bug in laurent_series integration",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1302",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
On Nov 28, 2007 10:43 AM, Jennifer S. Balakrishnan <> wrote:
> I'm trying to integrate a list of Laurent series, and it seems that
> once the list has more than 4 elements, Sage gets upset:

The problem is:

sage: A.<t> = LaurentSeriesRing(QQ)
sage: (-2*t^(-4) + O(t^8)).integral()
Traceback (most recent call last):
...
IndexError: list index out of range

This is because of  this code in rings/laurent_series_ring_element.pyx not
being coded correctly around line 880:
        if n < 0:
            v = [a[i]/(n+i+1) for i in range(-1-n)] + [0]
        else:
            v = []
        v += [a[i]/(n+i+1) for i in range(max(-n,0), len(a))]
	try:

So you should fix that and submit a patch :-).

William



> 
> sage: A.<t> = LaurentSeriesRing(QQ)
> sage: B = [-2*t^4 + O(t^16), -2*t^2 + O(t^14), -2 + O(t^12), -2*t^-2 +
> O(t^10), -2*t^-4 + O(t^8), -2*t^-6 + O(t^6)]
> sage: for i in range(6):
> ....:     B[i] = integral(B[i])
> ....:
> ---------------------------------------------------------------------------
> <type 'exceptions.IndexError'>            Traceback (most recent call last)
> 
> /home/jen/<ipython console> in <module>()
> 
> /home/jen/sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux/local/lib/python2.5/site-packages/sage/misc/functional.py
> in integral(x, *args, **kwds)
>     449     """
>     450     if hasattr(x, 'integral'):
> --> 451         return x.integral(*args, **kwds)
>     452     else:
>     453         from sage.calculus.calculus import SR
> 
> /home/jen/laurent_series_ring_element.pyx in
> sage.rings.laurent_series_ring_element.LaurentSeries.integral()
> 
> <type 'exceptions.IndexError'>: list index out of range
> sage: B
> 
> [-2/5*t^5 + O(t^17),
>  -2/3*t^3 + O(t^15),
>  -2*t + O(t^13),
>  2*t^-1 + O(t^11),
>  -2*t^-4 + O(t^8),        <================== stopped integrating here
>  -2*t^-6 + O(t^6)]
> 
> What's going on?
> 
> Jen
> 
```

Issue created by migration from https://trac.sagemath.org/ticket/1302





---

archive/issue_events_003408.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-26T03:14:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1302#event-3408"
}
```



---

archive/issue_comments_008160.json:
```json
{
    "body": "Certainly Bug Day material.",
    "created_at": "2007-12-26T03:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Certainly Bug Day material.



---

archive/issue_comments_008161.json:
```json
{
    "body": "Changing assignee from somebody to @rishikesha.",
    "created_at": "2008-01-02T22:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8161",
    "user": "https://github.com/rishikesha"
}
```

Changing assignee from somebody to @rishikesha.



---

archive/issue_comments_008162.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-02T22:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8162",
    "user": "https://github.com/rishikesha"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008163.json:
```json
{
    "body": "IndexError occurs when the highest power in the Laurent series is less than -2. The two lines in the patch add appropriate number of zero coefficients so that this does not happen. I consider this a bandaid solution, but at least it works.",
    "created_at": "2008-01-03T01:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8163",
    "user": "https://github.com/rishikesha"
}
```

IndexError occurs when the highest power in the Laurent series is less than -2. The two lines in the patch add appropriate number of zero coefficients so that this does not happen. I consider this a bandaid solution, but at least it works.



---

archive/issue_comments_008164.json:
```json
{
    "body": "Attachment [ticket_1302.patch](tarball://root/attachments/some-uuid/ticket1302/ticket_1302.patch) by @rishikesha created at 2008-01-04 08:36:00",
    "created_at": "2008-01-04T08:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8164",
    "user": "https://github.com/rishikesha"
}
```

Attachment [ticket_1302.patch](tarball://root/attachments/some-uuid/ticket1302/ticket_1302.patch) by @rishikesha created at 2008-01-04 08:36:00



---

archive/issue_comments_008165.json:
```json
{
    "body": "I changed the patch. This is much better than previous solution.",
    "created_at": "2008-01-04T08:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8165",
    "user": "https://github.com/rishikesha"
}
```

I changed the patch. This is much better than previous solution.



---

archive/issue_comments_008166.json:
```json
{
    "body": "Yep, works great.",
    "created_at": "2008-01-04T22:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8166",
    "user": "https://github.com/robertwb"
}
```

Yep, works great.



---

archive/issue_comments_008167.json:
```json
{
    "body": "We should add doctests to verify that the patch works. I am still willing to merge this patch for 2.9.2, but then I would open a new ticket to add doctests to test this.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T22:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We should add doctests to verify that the patch works. I am still willing to merge this patch for 2.9.2, but then I would open a new ticket to add doctests to test this.

Cheers,

Michael



---

archive/issue_comments_008168.json:
```json
{
    "body": "Attachment [trac-1302-example.patch](tarball://root/attachments/some-uuid/ticket1302/trac-1302-example.patch) by @williamstein created at 2008-01-05 02:19:26",
    "created_at": "2008-01-05T02:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8168",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1302-example.patch](tarball://root/attachments/some-uuid/ticket1302/trac-1302-example.patch) by @williamstein created at 2008-01-05 02:19:26



---

archive/issue_comments_008169.json:
```json
{
    "body": "Merged in 2.9.2.rc1.",
    "created_at": "2008-01-05T02:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.2.rc1.



---

archive/issue_events_003409.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-05T02:32:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1302#event-3409"
}
```



---

archive/issue_comments_008170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-05T02:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1302#issuecomment-8170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
