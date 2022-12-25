# Issue 3382: Compute Newton polytopes without polymake

archive/issues_003382.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: polytope, polyhedra, polynomials\n\nCurrently multivariable polynomials have a newton_polytope method which doesn't work without the optional polymake package installed.  This patch switches this method to using the Sage-native code in geometry/polyhedra.py, which only needs the default cddlib (in the future, this might optionally use lrs as well).  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3382\n\n",
    "created_at": "2008-06-08T12:50:15Z",
    "labels": [
        "component: geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Compute Newton polytopes without polymake",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @mwhansen

Keywords: polytope, polyhedra, polynomials

Currently multivariable polynomials have a newton_polytope method which doesn't work without the optional polymake package installed.  This patch switches this method to using the Sage-native code in geometry/polyhedra.py, which only needs the default cddlib (in the future, this might optionally use lrs as well).  

Issue created by migration from https://trac.sagemath.org/ticket/3382





---

archive/issue_comments_023626.json:
```json
{
    "body": "Attachment [trac_3382_newton_polytope.patch](tarball://root/attachments/some-uuid/ticket3382/trac_3382_newton_polytope.patch) by mabshoff created at 2008-06-08 19:14:00",
    "created_at": "2008-06-08T19:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3382#issuecomment-23626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3382_newton_polytope.patch](tarball://root/attachments/some-uuid/ticket3382/trac_3382_newton_polytope.patch) by mabshoff created at 2008-06-08 19:14:00



---

archive/issue_comments_023627.json:
```json
{
    "body": "Changing keywords from \"polytope, polyhedra, polynomials\" to \"polytope, polyhedra, polynomials, editor_mhansen\".",
    "created_at": "2008-06-15T22:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3382#issuecomment-23627",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "polytope, polyhedra, polynomials" to "polytope, polyhedra, polynomials, editor_mhansen".



---

archive/issue_comments_023628.json:
```json
{
    "body": "Looks good and passes tests for me.",
    "created_at": "2008-06-16T05:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3382#issuecomment-23628",
    "user": "https://github.com/mwhansen"
}
```

Looks good and passes tests for me.



---

archive/issue_events_003598.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-06-23T09:34:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3382#event-3598"
}
```



---

archive/issue_comments_023629.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T09:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3382#issuecomment-23629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0



---

archive/issue_comments_023630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T09:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3382#issuecomment-23630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
