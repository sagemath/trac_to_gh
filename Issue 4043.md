# Issue 4043: [with patch, needs review] Sage 3.1.2.alpha4: numerical noise in plot.py

archive/issues_004043.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nsage -t  devel/sage/sage/plot/plot.py                       **********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.alpha4/tmp/plot.py\", line 4505:\n    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01)\nExpected:\n    [(0.125000000000000*pi, 0.38268343236508978), (0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 0.707106781186547...), (0.312500000000000*pi, 0.83146961230254524), (0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 0.98078528040323043), (0.500000000000000*pi, 1.0), (0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 0.92387953251128674), (0.687500000000000*pi, 0.831469612302545...), (0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)]\nGot:\n    [(0.125000000000000*pi, 0.38268343236508978), (0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 0.70710678118654746), (0.312500000000000*pi, 0.83146961230254512), (0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 0.98078528040323043), (0.500000000000000*pi, 1.0), (0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), (0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 0.55557023301960218), (0.875000000000000*pi, 0.38268343236508984)]\n**********************************************************************\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4043\n\n",
    "created_at": "2008-09-03T00:13:34Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Sage 3.1.2.alpha4: numerical noise in plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
sage -t  devel/sage/sage/plot/plot.py                       **********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha4/tmp/plot.py", line 4505:
    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01)
Expected:
    [(0.125000000000000*pi, 0.38268343236508978), (0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 0.707106781186547...), (0.312500000000000*pi, 0.83146961230254524), (0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 0.98078528040323043), (0.500000000000000*pi, 1.0), (0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 0.92387953251128674), (0.687500000000000*pi, 0.831469612302545...), (0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)]
Got:
    [(0.125000000000000*pi, 0.38268343236508978), (0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 0.70710678118654746), (0.312500000000000*pi, 0.83146961230254512), (0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 0.98078528040323043), (0.500000000000000*pi, 1.0), (0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), (0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 0.55557023301960218), (0.875000000000000*pi, 0.38268343236508984)]
**********************************************************************
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4043





---

archive/issue_comments_029100.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4043#issuecomment-29100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029101.json:
```json
{
    "body": "Attachment [trac_4043.patch](tarball://root/attachments/some-uuid/ticket4043/trac_4043.patch) by mabshoff created at 2008-09-03 00:31:48",
    "created_at": "2008-09-03T00:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4043#issuecomment-29101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4043.patch](tarball://root/attachments/some-uuid/ticket4043/trac_4043.patch) by mabshoff created at 2008-09-03 00:31:48



---

archive/issue_comments_029102.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-03T00:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4043#issuecomment-29102",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_029103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-03T00:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4043#issuecomment-29103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009242.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-03T00:37:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4043#event-9242"
}
```



---

archive/issue_comments_029104.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-03T00:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4043#issuecomment-29104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0
