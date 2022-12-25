# Issue 4634: Sage 3.2.1.a1: numerical noise in sage/schemes/ elliptic_curves/ell_rational_field.py

archive/issues_004634.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jhpalmieri\n\n```\nFile \"/Applications/sage-3.2.1.alpha1/devel/sage/sage/schemes/\nelliptic_curves/ell_rational_field.py\", line 4071:\n   sage: a = E.integral_points([P1,P2,P3], verbose=True)\nExpected:\n   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]\n   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710\n   Minimal eigenvalue of height pairing matrix:  0.63792081458500...\n   x-coords of points on compact component with  -3 <=x<= 1\n   [-3, -2, -1, 0, 1]\n   x-coords of points on non-compact component with  2 <=x<= 6\n   [2, 3, 4]\n   starting search of remaining points using coefficient bound  5\n   x-coords of extra integral points:\n   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]\n   Total number of integral points: 18\nGot:\n   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]\n   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710\n   Minimal eigenvalue of height pairing matrix:  0.637920814585007\n   x-coords of points on compact component with  -3 <=x<= 1\n   [-3, -2, -1, 0, 1]\n   x-coords of points on non-compact component with  2 <=x<= 6\n   [2, 3, 4]\n   starting search of remaining points using coefficient bound  5\n   x-coords of extra integral points:\n   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]\n   Total number of integral points: 18\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4634\n\n",
    "created_at": "2008-11-27T03:43:14Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.1.a1: numerical noise in sage/schemes/ elliptic_curves/ell_rational_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4634",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jhpalmieri

```
File "/Applications/sage-3.2.1.alpha1/devel/sage/sage/schemes/
elliptic_curves/ell_rational_field.py", line 4071:
   sage: a = E.integral_points([P1,P2,P3], verbose=True)
Expected:
   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]
   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710
   Minimal eigenvalue of height pairing matrix:  0.63792081458500...
   x-coords of points on compact component with  -3 <=x<= 1
   [-3, -2, -1, 0, 1]
   x-coords of points on non-compact component with  2 <=x<= 6
   [2, 3, 4]
   starting search of remaining points using coefficient bound  5
   x-coords of extra integral points:
   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
   Total number of integral points: 18
Got:
   Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]
   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
   Minimal eigenvalue of height pairing matrix:  0.637920814585007
   x-coords of points on compact component with  -3 <=x<= 1
   [-3, -2, -1, 0, 1]
   x-coords of points on non-compact component with  2 <=x<= 6
   [2, 3, 4]
   starting search of remaining points using coefficient bound  5
   x-coords of extra integral points:
   [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
   Total number of integral points: 18
```

Issue created by migration from https://trac.sagemath.org/ticket/4634





---

archive/issue_comments_034777.json:
```json
{
    "body": "Attachment [trac_4634.patch](tarball://root/attachments/some-uuid/ticket4634/trac_4634.patch) by mabshoff created at 2008-11-27 04:08:18",
    "created_at": "2008-11-27T04:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34777",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4634.patch](tarball://root/attachments/some-uuid/ticket4634/trac_4634.patch) by mabshoff created at 2008-11-27 04:08:18



---

archive/issue_comments_034778.json:
```json
{
    "body": "The problem is this:\n\n```\n   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710\n   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem is this:

```
   e1,e2,e3:  -3.01243037259331 1.0658205476962... 1.94660982489710
   e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
```

Cheers,

Michael



---

archive/issue_comments_034779.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-27T04:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034780.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-11-27T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34780",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_034781.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha2



---

archive/issue_comments_034782.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4634#issuecomment-34782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010569.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-27T04:19:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4634",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4634#event-10569"
}
```
