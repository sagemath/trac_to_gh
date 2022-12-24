# Issue 2844: Polyhedral improvements, round 2

archive/issues_002844.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: polytope, Minkowski sum\n\nI have revamped my new polyhedra module so that it is much, much better.  Minkowski sums are now supported.  This required some minor changes to the 3D rendering in the gfan interface as well.  The module can do just about everything that sage could do through polymake previously - a few more particular polytopes could be predefined.\nAfter this functionality is reviewed, it can be used for making Newton polytopes of multivariable polynomials (and eventually Laurent polynomials as well), but I will put that on a seperate ticket.\nIn the future, I would like to add more 3D support, better 2D rendering, face lattice computations, and more particular cases.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2844\n\n",
    "created_at": "2008-04-07T14:44:39Z",
    "labels": [
        "geometry",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Polyhedral improvements, round 2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2844",
    "user": "mhampton"
}
```
Assignee: somebody

Keywords: polytope, Minkowski sum

I have revamped my new polyhedra module so that it is much, much better.  Minkowski sums are now supported.  This required some minor changes to the 3D rendering in the gfan interface as well.  The module can do just about everything that sage could do through polymake previously - a few more particular polytopes could be predefined.
After this functionality is reviewed, it can be used for making Newton polytopes of multivariable polynomials (and eventually Laurent polynomials as well), but I will put that on a seperate ticket.
In the future, I would like to add more 3D support, better 2D rendering, face lattice computations, and more particular cases.

Issue created by migration from https://trac.sagemath.org/ticket/2844





---

archive/issue_comments_019519.json:
```json
{
    "body": "Attachment [polyhedra.patch](tarball://root/attachments/some-uuid/ticket2844/polyhedra.patch) by mhampton created at 2008-04-07 14:46:11\n\nadds many polyhedral functions not requiring polymake",
    "created_at": "2008-04-07T14:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19519",
    "user": "mhampton"
}
```

Attachment [polyhedra.patch](tarball://root/attachments/some-uuid/ticket2844/polyhedra.patch) by mhampton created at 2008-04-07 14:46:11

adds many polyhedral functions not requiring polymake



---

archive/issue_comments_019520.json:
```json
{
    "body": "Nice work!  Applies to 3.0.alpha2 and passes tests for me.",
    "created_at": "2008-04-07T22:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19520",
    "user": "mhansen"
}
```

Nice work!  Applies to 3.0.alpha2 and passes tests for me.



---

archive/issue_comments_019521.json:
```json
{
    "body": "Attachment [2844.patch](tarball://root/attachments/some-uuid/ticket2844/2844.patch) by mhansen created at 2008-04-07 22:49:10\n\nI added 2844.patch which applies to the current 3.0.alpha3.  Apply it instead.",
    "created_at": "2008-04-07T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19521",
    "user": "mhansen"
}
```

Attachment [2844.patch](tarball://root/attachments/some-uuid/ticket2844/2844.patch) by mhansen created at 2008-04-07 22:49:10

I added 2844.patch which applies to the current 3.0.alpha3.  Apply it instead.



---

archive/issue_comments_019522.json:
```json
{
    "body": "Merged 2844.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-08T00:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19522",
    "user": "mabshoff"
}
```

Merged 2844.patch in Sage 3.0.alpha3



---

archive/issue_comments_019523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T00:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2844#issuecomment-19523",
    "user": "mabshoff"
}
```

Resolution: fixed
