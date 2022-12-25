# Issue 5714: Mod-2 matrix output does not show subdivisions

archive/issues_005714.json:
```json
{
    "body": "Assignee: tbd\n\nThis was reported on sage-support.  The following shows what's going on:\n\n```\nsage: MS7=MatrixSpace(Integers(7),4,4)\nsage: M=MS7.random_element()\nsage: M.subdivide([2],[2])\nsage: M\n\n[6 1|3 4]\n[4 4|0 5]\n[---+---]\n[4 2|2 6]\n[5 6|3 3]\nsage: MS2=MatrixSpace(Integers(2),4,4)\nsage: N=MS2.random_element()\nsage: N.subdivide([2],[2])\nsage: N\n\n[1 0 1 0]\n[1 1 0 0]\n[1 1 1 0]\n[0 0 0 1]\n```\n\nSee also #5716 for another issue and #5717 for another example. #5715 is a duplicate of this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5714\n\n",
    "closed_at": "2009-04-09T10:40:24Z",
    "created_at": "2009-04-08T19:06:54Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "title": "Mod-2 matrix output does not show subdivisions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5714",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: tbd

This was reported on sage-support.  The following shows what's going on:

```
sage: MS7=MatrixSpace(Integers(7),4,4)
sage: M=MS7.random_element()
sage: M.subdivide([2],[2])
sage: M

[6 1|3 4]
[4 4|0 5]
[---+---]
[4 2|2 6]
[5 6|3 3]
sage: MS2=MatrixSpace(Integers(2),4,4)
sage: N=MS2.random_element()
sage: N.subdivide([2],[2])
sage: N

[1 0 1 0]
[1 1 0 0]
[1 1 1 0]
[0 0 0 1]
```

See also #5716 for another issue and #5717 for another example. #5715 is a duplicate of this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/5714





---

archive/issue_comments_044571.json:
```json
{
    "body": "As I mentioned on the list, the Matrix_mod2_dense class has its own str() method that just returns a string representation of the matrix without  taking subdivisions into account.\n\nRemoving that method seems to be benign, and lets the common print method for matrices take over, printing with subdivisions.\n\nI have doctested the matrix directory without a problem.  Someone involved in the initial implementations might want to comment.\n\nI'll attach a patch when the testing is complete (or try again if testing fails).",
    "created_at": "2009-04-08T19:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5714#issuecomment-44571",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

As I mentioned on the list, the Matrix_mod2_dense class has its own str() method that just returns a string representation of the matrix without  taking subdivisions into account.

Removing that method seems to be benign, and lets the common print method for matrices take over, printing with subdivisions.

I have doctested the matrix directory without a problem.  Someone involved in the initial implementations might want to comment.

I'll attach a patch when the testing is complete (or try again if testing fails).



---

archive/issue_comments_044572.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-09T10:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5714#issuecomment-44572",
    "user": "https://github.com/robertwb"
}
```

Resolution: duplicate



---

archive/issue_events_013414.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2009-04-09T10:40:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5714",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5714#event-13414"
}
```
