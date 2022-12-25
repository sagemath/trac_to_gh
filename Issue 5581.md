# Issue 5581: Face lattices and f-vectors for polytopes; bug fixes for polyhedra.py

archive/issues_005581.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: polyhedra, face lattice, geometry\n\nThis patch adds the important functionality of computing face lattices and f-vectors of polytopes.  In the course of adding these, I found a number of bugs that occur for polyhedra of lower dimensions that are embedded in higher dimensions, which I believe I have fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5581\n\n",
    "created_at": "2009-03-21T17:12:27Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Face lattices and f-vectors for polytopes; bug fixes for polyhedra.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: polyhedra, face lattice, geometry

This patch adds the important functionality of computing face lattices and f-vectors of polytopes.  In the course of adding these, I found a number of bugs that occur for polyhedra of lower dimensions that are embedded in higher dimensions, which I believe I have fixed.

Issue created by migration from https://trac.sagemath.org/ticket/5581





---

archive/issue_comments_043422.json:
```json
{
    "body": "Attachment [trac_5581_face_lattice.patch](tarball://root/attachments/some-uuid/ticket5581/trac_5581_face_lattice.patch) by mhampton created at 2009-03-21 17:15:00\n\nadds face lattices and f-vectors to polytopes",
    "created_at": "2009-03-21T17:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5581#issuecomment-43422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_5581_face_lattice.patch](tarball://root/attachments/some-uuid/ticket5581/trac_5581_face_lattice.patch) by mhampton created at 2009-03-21 17:15:00

adds face lattices and f-vectors to polytopes



---

archive/issue_comments_043423.json:
```json
{
    "body": "rebased against 3.4.2 and improved doctests.",
    "created_at": "2009-05-20T18:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5581#issuecomment-43423",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

rebased against 3.4.2 and improved doctests.



---

archive/issue_comments_043424.json:
```json
{
    "body": "Attachment [trac_5581_rebase.patch](tarball://root/attachments/some-uuid/ticket5581/trac_5581_rebase.patch) by dperkinson created at 2009-05-20 19:22:38\n\nI applied trac_5581_rebase.patch to Sage Version 4.0.alpha0, Release Date: 2009-05-15.  All doctests in sage/geometry passed, and I tried several other examples.  \n\nThis patch works with trac_4875_1.patch: the two work together regardless of the order in which they are applied.",
    "created_at": "2009-05-20T19:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5581#issuecomment-43424",
    "user": "https://trac.sagemath.org/admin/accounts/users/dperkinson"
}
```

Attachment [trac_5581_rebase.patch](tarball://root/attachments/some-uuid/ticket5581/trac_5581_rebase.patch) by dperkinson created at 2009-05-20 19:22:38

I applied trac_5581_rebase.patch to Sage Version 4.0.alpha0, Release Date: 2009-05-15.  All doctests in sage/geometry passed, and I tried several other examples.  

This patch works with trac_4875_1.patch: the two work together regardless of the order in which they are applied.



---

archive/issue_comments_043425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T02:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5581#issuecomment-43425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043426.json:
```json
{
    "body": "Merged trac_5581_rebase.patch only in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T02:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5581#issuecomment-43426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5581_rebase.patch only in Sage 4.0.rc0.

Cheers,

Michael
