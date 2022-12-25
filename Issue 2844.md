# Issue 2844: Polyhedral improvements, round 2

archive/issues_002844.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: polytope, Minkowski sum\n\nI have revamped my new polyhedra module so that it is much, much better.  Minkowski sums are now supported.  This required some minor changes to the 3D rendering in the gfan interface as well.  The module can do just about everything that sage could do through polymake previously - a few more particular polytopes could be predefined.\nAfter this functionality is reviewed, it can be used for making Newton polytopes of multivariable polynomials (and eventually Laurent polynomials as well), but I will put that on a seperate ticket.\nIn the future, I would like to add more 3D support, better 2D rendering, face lattice computations, and more particular cases.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2844\n\n",
    "created_at": "2008-04-07T14:44:39Z",
    "labels": [
        "component: geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Polyhedral improvements, round 2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: somebody

Keywords: polytope, Minkowski sum

I have revamped my new polyhedra module so that it is much, much better.  Minkowski sums are now supported.  This required some minor changes to the 3D rendering in the gfan interface as well.  The module can do just about everything that sage could do through polymake previously - a few more particular polytopes could be predefined.
After this functionality is reviewed, it can be used for making Newton polytopes of multivariable polynomials (and eventually Laurent polynomials as well), but I will put that on a seperate ticket.
In the future, I would like to add more 3D support, better 2D rendering, face lattice computations, and more particular cases.

Issue created by migration from https://trac.sagemath.org/ticket/2844





---

archive/issue_comments_019478.json:
```json
{
    "body": "Attachment [polyhedra.patch](tarball://root/attachments/some-uuid/ticket2844/polyhedra.patch) by mhampton created at 2008-04-07 14:46:11\n\nadds many polyhedral functions not requiring polymake",
    "created_at": "2008-04-07T14:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [polyhedra.patch](tarball://root/attachments/some-uuid/ticket2844/polyhedra.patch) by mhampton created at 2008-04-07 14:46:11

adds many polyhedral functions not requiring polymake



---

archive/issue_comments_019479.json:
```json
{
    "body": "Nice work!  Applies to 3.0.alpha2 and passes tests for me.",
    "created_at": "2008-04-07T22:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19479",
    "user": "https://github.com/mwhansen"
}
```

Nice work!  Applies to 3.0.alpha2 and passes tests for me.



---

archive/issue_comments_019480.json:
```json
{
    "body": "Attachment [2844.patch](tarball://root/attachments/some-uuid/ticket2844/2844.patch) by @mwhansen created at 2008-04-07 22:49:10\n\nI added 2844.patch which applies to the current 3.0.alpha3.  Apply it instead.",
    "created_at": "2008-04-07T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19480",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2844.patch](tarball://root/attachments/some-uuid/ticket2844/2844.patch) by @mwhansen created at 2008-04-07 22:49:10

I added 2844.patch which applies to the current 3.0.alpha3.  Apply it instead.



---

archive/issue_comments_019481.json:
```json
{
    "body": "Merged 2844.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-08T00:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19481",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2844.patch in Sage 3.0.alpha3



---

archive/issue_comments_019482.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T00:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19482",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006523.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-08T00:28:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2844#event-6523"
}
```
