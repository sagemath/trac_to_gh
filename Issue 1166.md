# Issue 1166: 2D terminal output is inconsistent and corrupted

archive/issues_001166.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: f = (exp(x)-1)/(exp(x/2)+1)\nsage: g = exp(x/2)-1\nsage: print f(10.0), g(10.0)\n                               147.4131591025766                               \\\n 147.4131591025766\nsage: print 1, 2\n1 2\nsage: print f(10), g(10)\n                                     10\n                                    e   - 1\n                                   --------\n                                     5\n                                    e  + 1                                     \\\n  5\n                                     e  - 1\n```\n\n\nThe output of f(10.0), g(10.0) [with many spaces] seems inconsistent with that of 1, 2 [no spaces]. With f(10), g(10) the exponent 5 of g(10) wraps around the terminal line, and is thus\nnot properly aligned with e - 1. (all this in a 80-column xterm)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1166\n\n",
    "created_at": "2007-11-13T22:44:08Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "2D terminal output is inconsistent and corrupted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1166",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein


```
sage: f = (exp(x)-1)/(exp(x/2)+1)
sage: g = exp(x/2)-1
sage: print f(10.0), g(10.0)
                               147.4131591025766                               \
 147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1                                     \
  5
                                     e  - 1
```


The output of f(10.0), g(10.0) [with many spaces] seems inconsistent with that of 1, 2 [no spaces]. With f(10), g(10) the exponent 5 of g(10) wraps around the terminal line, and is thus
not properly aligned with e - 1. (all this in a 80-column xterm)

Issue created by migration from https://trac.sagemath.org/ticket/1166





---

archive/issue_comments_007127.json:
```json
{
    "body": "It looks like a newline at the end of the multi line expression of f(10) would fix the issue:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.9, Release Date: 2007-12-16                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: f = (exp(x)-1)/(exp(x/2)+1)\nsage: g = exp(x/2)-1\nsage: print f(10.0), g(10.0)\n                               147.4131591025766                                147.4131591025766\nsage: print 1, 2\n1 2\nsage: print f(10), g(10)\n                                     10\n                                    e   - 1\n                                   --------\n                                     5\n                                    e  + 1                                       5\n                                     e  - 1\nsage: print f(10)\n                                     10\n                                    e   - 1\n                                   --------\n                                     5\n                                    e  + 1\nsage: print g(10)\n                                      5\n                                     e  - 1\nsage:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T23:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It looks like a newline at the end of the multi line expression of f(10) would fix the issue:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9, Release Date: 2007-12-16                         |
| Type notebook() for the GUI, and license() for information.        |
sage: f = (exp(x)-1)/(exp(x/2)+1)
sage: g = exp(x/2)-1
sage: print f(10.0), g(10.0)
                               147.4131591025766                                147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1                                       5
                                     e  - 1
sage: print f(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1
sage: print g(10)
                                      5
                                     e  - 1
sage:
```


Cheers,

Michael



---

archive/issue_comments_007128.json:
```json
{
    "body": "Attachment [trac-1166.patch](tarball://root/attachments/some-uuid/ticket1166/trac-1166.patch) by @williamstein created at 2008-01-21 11:38:37",
    "created_at": "2008-01-21T11:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7128",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1166.patch](tarball://root/attachments/some-uuid/ticket1166/trac-1166.patch) by @williamstein created at 2008-01-21 11:38:37



---

archive/issue_comments_007129.json:
```json
{
    "body": "[this is my first review, thus please take with care]\n\nI get with this patch applied in 2.10:\n\n```\nsage: f=(exp(x)-1)/(exp(x/2)+1)\nsage: g=exp(x/2)-1\nsage: print f(10.0), g(10.0)\n\n                               147.4131591025766 \n                               147.4131591025766\nsage: print 1, 2\n1 2\nsage: print f(10), g(10)\n\n                                     10\n                                    e   - 1\n                                   --------\n                                     5\n                                    e  + 1 \n                                      5\n                                     e  - 1\n```\n\nThe output is much better, but I would expect:\n\n```\nsage: print f(10.0), g(10.0)\n\n                   147.4131591025766, 147.4131591025766\n```\n\nor\n\n```\nsage: print f(10.0), g(10.0)\n147.4131591025766 147.4131591025766\n```\n\nHowever, since this is an improvement, I give a positive review.",
    "created_at": "2008-01-21T15:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7129",
    "user": "https://github.com/zimmermann6"
}
```

[this is my first review, thus please take with care]

I get with this patch applied in 2.10:

```
sage: f=(exp(x)-1)/(exp(x/2)+1)
sage: g=exp(x/2)-1
sage: print f(10.0), g(10.0)

                               147.4131591025766 
                               147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)

                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1 
                                      5
                                     e  - 1
```

The output is much better, but I would expect:

```
sage: print f(10.0), g(10.0)

                   147.4131591025766, 147.4131591025766
```

or

```
sage: print f(10.0), g(10.0)
147.4131591025766 147.4131591025766
```

However, since this is an improvement, I give a positive review.



---

archive/issue_comments_007130.json:
```json
{
    "body": "The potential solution to the adding an extra newlines in situations like\n\n```\nsage: print f(10.0), g(10.0)\n147.4131591025766 147.4131591025766\n```\n\nmight be that we need to check if the string returned from `f(10.0` contains a newline in which case we need to add the extra newline to separate the the two multiline outputs. If that is doable please open another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T22:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The potential solution to the adding an extra newlines in situations like

```
sage: print f(10.0), g(10.0)
147.4131591025766 147.4131591025766
```

might be that we need to check if the string returned from `f(10.0` contains a newline in which case we need to add the extra newline to separate the the two multiline outputs. If that is doable please open another ticket.

Cheers,

Michael



---

archive/issue_events_001298.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T22:58:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1166#event-1298"
}
```



---

archive/issue_comments_007131.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T22:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_007132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T22:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1166#issuecomment-7132",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
