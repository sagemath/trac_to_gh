# Issue 3031: [with patch] Add zeta_function method for schemes

archive/issues_003031.json:
```json
{
    "body": "Assignee: wstein\n\nCC:  @kedlaya\n\nKeywords: zeta function, schemes, finite fields\n\nThe attached patch (built against 3.0) adds a zeta_function method to the class of schemes over finite fields. It is meant to be a default procedure, to be overridden by something more sensible for particular classes of schemes (e.g., elliptic and hyperelliptic curves).\n\nZeta functions are currently only enabled over prime fields, but it will be trivial to fix that once coercion between nonprime finite fields is supported.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3031\n\n",
    "created_at": "2008-04-26T15:42:49Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch] Add zeta_function method for schemes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3031",
    "user": "https://github.com/kedlaya"
}
```
Assignee: wstein

CC:  @kedlaya

Keywords: zeta function, schemes, finite fields

The attached patch (built against 3.0) adds a zeta_function method to the class of schemes over finite fields. It is meant to be a default procedure, to be overridden by something more sensible for particular classes of schemes (e.g., elliptic and hyperelliptic curves).

Zeta functions are currently only enabled over prime fields, but it will be trivial to fix that once coercion between nonprime finite fields is supported.

Issue created by migration from https://trac.sagemath.org/ticket/3031





---

archive/issue_comments_020817.json:
```json
{
    "body": "Attachment [9610.patch](tarball://root/attachments/some-uuid/ticket3031/9610.patch) by @kedlaya created at 2008-04-26 15:43:28",
    "created_at": "2008-04-26T15:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20817",
    "user": "https://github.com/kedlaya"
}
```

Attachment [9610.patch](tarball://root/attachments/some-uuid/ticket3031/9610.patch) by @kedlaya created at 2008-04-26 15:43:28



---

archive/issue_comments_020818.json:
```json
{
    "body": "Attachment [trac-3031-pt2.patch](tarball://root/attachments/some-uuid/ticket3031/trac-3031-pt2.patch) by @craigcitro created at 2008-04-27 00:52:34",
    "created_at": "2008-04-27T00:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20818",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3031-pt2.patch](tarball://root/attachments/some-uuid/ticket3031/trac-3031-pt2.patch) by @craigcitro created at 2008-04-27 00:52:34



---

archive/issue_comments_020819.json:
```json
{
    "body": "Looks good. Added a patch with a few additional doctests, killed some long lines, and fixed one tiny tiny bug: the code was `return`ing exceptions, instead of `raise`ing them. Merge both patches.",
    "created_at": "2008-04-27T00:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20819",
    "user": "https://github.com/craigcitro"
}
```

Looks good. Added a patch with a few additional doctests, killed some long lines, and fixed one tiny tiny bug: the code was `return`ing exceptions, instead of `raise`ing them. Merge both patches.



---

archive/issue_comments_020820.json:
```json
{
    "body": "Merged both patches in Sage 3.0.1.alpha1",
    "created_at": "2008-04-27T01:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.1.alpha1



---

archive/issue_events_006877.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-27T01:25:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3031#event-6877"
}
```



---

archive/issue_comments_020821.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-27T01:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020822.json:
```json
{
    "body": "I have taken a look at the code.  Some tweaking will be needed to make\nit sensibly compatible with the existing code for point counting of\nelliptic curves.  There, the function cardinality() takes a parameter\nextension_degree with default 1, while you do a base change to get the\ncardinality over extensions.  Secondly, I think having a cardinality()\nmethod is better than calling a rational_points() functioI have taken\na look at the code.  Some tweaking will be needed to make it sensibly\ncompatible with the existing code for point counting of elliptic\ncurves.  There, the function cardinality() takes a n and then taking\nthe len() of the result, since there is little point in creating a\nlist of all the rational points at all if what one needs is their\nnumber.",
    "created_at": "2008-04-27T20:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20822",
    "user": "https://github.com/JohnCremona"
}
```

I have taken a look at the code.  Some tweaking will be needed to make
it sensibly compatible with the existing code for point counting of
elliptic curves.  There, the function cardinality() takes a parameter
extension_degree with default 1, while you do a base change to get the
cardinality over extensions.  Secondly, I think having a cardinality()
method is better than calling a rational_points() functioI have taken
a look at the code.  Some tweaking will be needed to make it sensibly
compatible with the existing code for point counting of elliptic
curves.  There, the function cardinality() takes a n and then taking
the len() of the result, since there is little point in creating a
list of all the rational points at all if what one needs is their
number.



---

archive/issue_comments_020823.json:
```json
{
    "body": "As various people have pointed out there are various problems here. Hence it will be reopened and I will revert the two applied patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-28T02:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

As various people have pointed out there are various problems here. Hence it will be reopened and I will revert the two applied patches.

Cheers,

Michael



---

archive/issue_comments_020824.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-28T02:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020825.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-28T02:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006878.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-28T02:32:31Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3031#event-6878"
}
```



---

archive/issue_comments_020826.json:
```json
{
    "body": "Attachment [trac-3031-pt3.patch](tarball://root/attachments/some-uuid/ticket3031/trac-3031-pt3.patch) by @craigcitro created at 2008-04-28 03:35:17",
    "created_at": "2008-04-28T03:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20826",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3031-pt3.patch](tarball://root/attachments/some-uuid/ticket3031/trac-3031-pt3.patch) by @craigcitro created at 2008-04-28 03:35:17



---

archive/issue_comments_020827.json:
```json
{
    "body": "ncalexan brought up the good point that maybe some users will expect a rational function from zeta_function. After some discussion, it's been renamed to zeta_series. \n\nI also fixed about 10 occurrences of \"the the\" in sage.",
    "created_at": "2008-04-28T03:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20827",
    "user": "https://github.com/craigcitro"
}
```

ncalexan brought up the good point that maybe some users will expect a rational function from zeta_function. After some discussion, it's been renamed to zeta_series. 

I also fixed about 10 occurrences of "the the" in sage.



---

archive/issue_comments_020828.json:
```json
{
    "body": "I prefer the name zeta_series and hope that zeta_function (Returning a rational function!) will be implemented in the near future.",
    "created_at": "2008-04-28T05:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20828",
    "user": "https://github.com/ncalexan"
}
```

I prefer the name zeta_series and hope that zeta_function (Returning a rational function!) will be implemented in the near future.



---

archive/issue_comments_020829.json:
```json
{
    "body": "Remerged the previously reverted patches and merged trac-3031-pt3.patch in Sage 3.0.1.alpha1",
    "created_at": "2008-04-29T00:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Remerged the previously reverted patches and merged trac-3031-pt3.patch in Sage 3.0.1.alpha1



---

archive/issue_events_006879.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-29T00:04:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3031#event-6879"
}
```



---

archive/issue_comments_020830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-29T00:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3031#issuecomment-20830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
