# Issue 2451: plotting -- contour_plot and plot_vector_field are REALLY SLOW but it's easy to get a million times speedup

archive/issues_002451.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere are two problems:\n\n1. neither use _fast_float\n\n2. Even worse, they don't coerce their endpoints to floats.  This is a killer.\n\nTo illustrate:\n\n```\nvar('x,y')\nsage: time contour_plot(x^2+y^2, (-pi,pi),(-pi,pi))\ntakes forever\nsage: time contour_plot(x^2+y^2, (-float(pi),float(pi)),(-float(pi),float(pi)))\ntakes forever\nsage: f = (x^2+y^2)._fast_float_('x','y')\nsage: time contour_plot(f, (-float(pi),float(pi)),(-float(pi),float(pi)))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2451\n\n",
    "created_at": "2008-03-10T01:06:45Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "plotting -- contour_plot and plot_vector_field are REALLY SLOW but it's easy to get a million times speedup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2451",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

There are two problems:

1. neither use _fast_float

2. Even worse, they don't coerce their endpoints to floats.  This is a killer.

To illustrate:

```
var('x,y')
sage: time contour_plot(x^2+y^2, (-pi,pi),(-pi,pi))
takes forever
sage: time contour_plot(x^2+y^2, (-float(pi),float(pi)),(-float(pi),float(pi)))
takes forever
sage: f = (x^2+y^2)._fast_float_('x','y')
sage: time contour_plot(f, (-float(pi),float(pi)),(-float(pi),float(pi)))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
```


Issue created by migration from https://trac.sagemath.org/ticket/2451





---

archive/issue_comments_016531.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T05:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16531",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016532.json:
```json
{
    "body": "part 1.  there may be a part 2...",
    "created_at": "2008-03-10T06:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16532",
    "user": "https://github.com/williamstein"
}
```

part 1.  there may be a part 2...



---

archive/issue_comments_016533.json:
```json
{
    "body": "Attachment [sage-2451.patch](tarball://root/attachments/some-uuid/ticket2451/sage-2451.patch) by @williamstein created at 2008-03-10 06:23:09",
    "created_at": "2008-03-10T06:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16533",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2451.patch](tarball://root/attachments/some-uuid/ticket2451/sage-2451.patch) by @williamstein created at 2008-03-10 06:23:09



---

archive/issue_comments_016534.json:
```json
{
    "body": "Positive review pending patch of redundant line 4239.",
    "created_at": "2008-03-10T06:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16534",
    "user": "https://github.com/garyfurnish"
}
```

Positive review pending patch of redundant line 4239.



---

archive/issue_comments_016535.json:
```json
{
    "body": "I did remove the offending line after merging the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-10T07:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I did remove the offending line after merging the patch.

Cheers,

Michael



---

archive/issue_comments_016536.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T07:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc4



---

archive/issue_comments_016537.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T07:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016538.json:
```json
{
    "body": "works as advertised in my limited testing. \n\ngfurnish indicates that line 4239 is redundant",
    "created_at": "2008-03-10T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16538",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```

works as advertised in my limited testing. 

gfurnish indicates that line 4239 is redundant



---

archive/issue_comments_016539.json:
```json
{
    "body": "oops, missed previous comments",
    "created_at": "2008-03-10T07:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2451#issuecomment-16539",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```

oops, missed previous comments
