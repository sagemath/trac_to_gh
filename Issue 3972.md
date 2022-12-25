# Issue 3972: 3.1.2.alpha1: numerical noise in plot.py

archive/issues_003972.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01) \nExpected: \n    [(0.125000000000000*pi, 0.38268343236508978), \n(0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, \n0.707106781186547...), (0.312500000000000*pi, 0.83146961230254524), \n(0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, \n0.98078528040323043), (0.500000000000000*pi, 1.0), \n(0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, \n0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), \n(0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, \n0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)] \nGot: \n    [(0.125000000000000*pi, 0.38268343236508978), \n(0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, \n0.70710678118654746), (0.312500000000000*pi, 0.83146961230254524), \n(0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, \n0.98078528040323043), (0.500000000000000*pi, 1.0), \n(0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, \n0.92387953251128674), (0.687500000000000*pi, 0.83146961230254535), \n(0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, \n0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)] \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3972\n\n",
    "created_at": "2008-08-28T05:24:41Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "3.1.2.alpha1: numerical noise in plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3972",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
    sage: adaptive_refinement(sin, (0,0), (pi,0), adaptive_tolerance=0.01) 
Expected: 
    [(0.125000000000000*pi, 0.38268343236508978), 
(0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 
0.707106781186547...), (0.312500000000000*pi, 0.83146961230254524), 
(0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 
0.98078528040323043), (0.500000000000000*pi, 1.0), 
(0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 
0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), 
(0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 
0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)] 
Got: 
    [(0.125000000000000*pi, 0.38268343236508978), 
(0.187500000000000*pi, 0.55557023301960218), (0.250000000000000*pi, 
0.70710678118654746), (0.312500000000000*pi, 0.83146961230254524), 
(0.375000000000000*pi, 0.92387953251128674), (0.437500000000000*pi, 
0.98078528040323043), (0.500000000000000*pi, 1.0), 
(0.562500000000000*pi, 0.98078528040323043), (0.625000000000000*pi, 
0.92387953251128674), (0.687500000000000*pi, 0.83146961230254535), 
(0.750000000000000*pi, 0.70710678118654757), (0.812500000000000*pi, 
0.55557023301960218), (0.875000000000000*pi, 0.38268343236508989)] 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3972





---

archive/issue_comments_028482.json:
```json
{
    "body": "The problem is after cutting away all the identical output:\n\n```\nExpected:\n0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), \nGot:\n0.92387953251128674), (0.687500000000000*pi, 0.83146961230254535), \n```\n",
    "created_at": "2008-08-29T09:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3972#issuecomment-28482",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem is after cutting away all the identical output:

```
Expected:
0.92387953251128674), (0.687500000000000*pi, 0.83146961230254546), 
Got:
0.92387953251128674), (0.687500000000000*pi, 0.83146961230254535), 
```




---

archive/issue_comments_028483.json:
```json
{
    "body": "Attachment [trac_3972.patch](tarball://root/attachments/some-uuid/ticket3972/trac_3972.patch) by mabshoff created at 2008-08-29 09:10:33",
    "created_at": "2008-08-29T09:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3972#issuecomment-28483",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3972.patch](tarball://root/attachments/some-uuid/ticket3972/trac_3972.patch) by mabshoff created at 2008-08-29 09:10:33



---

archive/issue_comments_028484.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-08-29T09:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3972#issuecomment-28484",
    "user": "https://github.com/craigcitro"
}
```

Looks good.



---

archive/issue_comments_028485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T09:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3972#issuecomment-28485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028486.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T09:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3972#issuecomment-28486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_events_004202.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T09:15:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3972",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3972#event-4202"
}
```
