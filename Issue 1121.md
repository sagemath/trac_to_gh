# Issue 1121: improve point counting for curvers over extension fields

archive/issues_001121.json:
```json
{
    "body": "Assignee: @williamstein\n\nJohn Cremona wrote\n\n\n```\nYou are right of course -- one should always compute the order over\nthe smallest field of definition and then use the easy formula to get\nthe order of E(GF(q^d)) from that of E(GF(q)).\n\nWhile you are at it you should not stop at the smallest field\ncontaining the coefficients of the given curve, it would be enough to\nwork over the field containing the j-invariant, plus a little work\ndeciding which twist your need and all this is as usual a little more\ncomplicated when j=0 or j=1728, or in characteristics 2 and 3.\n\nThis feels like reinventing wheels -- i wonder who has done this already?\n\nAs for implementation, it is *extremely* ugly to work with floating\npoint complex numbers for this (as both Graeme and Alex seem to do.\nIt should be done algebraically!\n\nIf n = #E(GF(q)) then a=1+q-n is the trace of alpha =\n(a+sqrt(a^2-4*q))/2, and then #E(GF(q^d)) = 1+q^d-trace(alpha^d).  The\ntrace of the d'th power of alpha is just a resultant calculation.\n```\n\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/69ebf55ee4f22278/23c61ad57cbff62a\n\n#1119 implements to computing over GF(p) if possible, but it doesn't implement computing over GF(p<sup>m</sup>) if m|n. Also #1119 still relies on floating point arithmetic.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1121\n\n",
    "created_at": "2007-11-07T15:57:31Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "improve point counting for curvers over extension fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1121",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

John Cremona wrote


```
You are right of course -- one should always compute the order over
the smallest field of definition and then use the easy formula to get
the order of E(GF(q^d)) from that of E(GF(q)).

While you are at it you should not stop at the smallest field
containing the coefficients of the given curve, it would be enough to
work over the field containing the j-invariant, plus a little work
deciding which twist your need and all this is as usual a little more
complicated when j=0 or j=1728, or in characteristics 2 and 3.

This feels like reinventing wheels -- i wonder who has done this already?

As for implementation, it is *extremely* ugly to work with floating
point complex numbers for this (as both Graeme and Alex seem to do.
It should be done algebraically!

If n = #E(GF(q)) then a=1+q-n is the trace of alpha =
(a+sqrt(a^2-4*q))/2, and then #E(GF(q^d)) = 1+q^d-trace(alpha^d).  The
trace of the d'th power of alpha is just a resultant calculation.
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/69ebf55ee4f22278/23c61ad57cbff62a

#1119 implements to computing over GF(p) if possible, but it doesn't implement computing over GF(p<sup>m</sup>) if m|n. Also #1119 still relies on floating point arithmetic.

Issue created by migration from https://trac.sagemath.org/ticket/1121





---

archive/issue_comments_006752.json:
```json
{
    "body": "that should be #1120 instead of #1119",
    "created_at": "2007-11-07T15:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6752",
    "user": "https://github.com/malb"
}
```

that should be #1120 instead of #1119



---

archive/issue_comments_006753.json:
```json
{
    "body": "Attachment [8312.patch](tarball://root/attachments/some-uuid/ticket1121/8312.patch) by gmoose05 created at 2008-02-08 01:23:53\n\n8312 just corrects minor thing in documentation\n\nThe Documentation said the cardinality was not cached, but in fact the code does cache.",
    "created_at": "2008-02-08T01:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6753",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoose05"
}
```

Attachment [8312.patch](tarball://root/attachments/some-uuid/ticket1121/8312.patch) by gmoose05 created at 2008-02-08 01:23:53

8312 just corrects minor thing in documentation

The Documentation said the cardinality was not cached, but in fact the code does cache.



---

archive/issue_comments_006754.json:
```json
{
    "body": "Yep, looks good to me.",
    "created_at": "2008-02-14T06:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6754",
    "user": "https://github.com/robertwb"
}
```

Yep, looks good to me.



---

archive/issue_comments_006755.json:
```json
{
    "body": "Applied 8312.patch to Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T09:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Applied 8312.patch to Sage 2.10.2.alpha0



---

archive/issue_comments_006756.json:
```json
{
    "body": "Replying to [comment:2 gmoose05]:\n> 8312 just corrects minor thing in documentation\n> \n> The Documentation said the cardinality was not cached, but in fact the code does cache. \n\nI am confused. Does the patch address the ticket?",
    "created_at": "2008-02-14T09:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6756",
    "user": "https://github.com/malb"
}
```

Replying to [comment:2 gmoose05]:
> 8312 just corrects minor thing in documentation
> 
> The Documentation said the cardinality was not cached, but in fact the code does cache. 

I am confused. Does the patch address the ticket?



---

archive/issue_comments_006757.json:
```json
{
    "body": "I don't think that the patch addresses the ticket, it just corrects the issue about caching. So I am removing the `with positive review` - I guess we should have opened another ticket for the documentation issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T09:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I don't think that the patch addresses the ticket, it just corrects the issue about caching. So I am removing the `with positive review` - I guess we should have opened another ticket for the documentation issue.

Cheers,

Michael



---

archive/issue_comments_006758.json:
```json
{
    "body": "The issues raised here have all been sorted under other tickets.  This one can be closed.",
    "created_at": "2008-04-06T11:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6758",
    "user": "https://github.com/JohnCremona"
}
```

The issues raised here have all been sorted under other tickets.  This one can be closed.



---

archive/issue_comments_006759.json:
```json
{
    "body": "Closing this on the recommendation of John Cremona since the issues have all been fixed.",
    "created_at": "2008-04-06T14:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closing this on the recommendation of John Cremona since the issues have all been fixed.



---

archive/issue_comments_006760.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T14:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1121#issuecomment-6760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
