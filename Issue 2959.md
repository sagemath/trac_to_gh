# Issue 2959: bug in DirichletGroup over a finite base ring

archive/issues_002959.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nsage: G = DirichletGroup(21)\nsage: chi = G.0; chi\n[-1, 1]\nsage: chi.values()\n[0, 1, -1, 0, 1, -1, 0, 0, -1, 0, 1, -1, 0, 1, 0, 0, 1, -1, 0, 1, -1]\n```\n\n\nSo far, so good (similar code is in the tutorial: http://www.sagemath.org/doc/html/tut/node15.html). Now use a different base ring:\n\n\n```\nsage: G = DirichletGroup(21, GF(37))\nsage: chi = G.0; chi\n[36, 1]\nsage: chi.values()\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/<ipython console> in <module>()\n\n/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\nin values(self)\n  1056             ########################\n  1057             # record character value on n\n-> 1058             result_list[n.ivalue] = R_values[value.ivalue]\n  1059             # iterate:\n  1060             #   increase the exponent vector by 1,\n\n<type 'exceptions.IndexError'>: list index out of range\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2959\n\n",
    "created_at": "2008-04-19T21:32:13Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "bug in DirichletGroup over a finite base ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2959",
    "user": "wdj"
}
```
Assignee: was


```

sage: G = DirichletGroup(21)
sage: chi = G.0; chi
[-1, 1]
sage: chi.values()
[0, 1, -1, 0, 1, -1, 0, 0, -1, 0, 1, -1, 0, 1, 0, 0, 1, -1, 0, 1, -1]
```


So far, so good (similar code is in the tutorial: http://www.sagemath.org/doc/html/tut/node15.html). Now use a different base ring:


```
sage: G = DirichletGroup(21, GF(37))
sage: chi = G.0; chi
[36, 1]
sage: chi.values()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/<ipython console> in <module>()

/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
in values(self)
  1056             ########################
  1057             # record character value on n
-> 1058             result_list[n.ivalue] = R_values[value.ivalue]
  1059             # iterate:
  1060             #   increase the exponent vector by 1,

<type 'exceptions.IndexError'>: list index out of range
```



Issue created by migration from https://trac.sagemath.org/ticket/2959





---

archive/issue_comments_020411.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-04-19T23:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20411",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_020412.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T23:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20412",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020413.json:
```json
{
    "body": "Yep, this was a mistake on my part. The attached patch fixes it, adds a few doctests to check the various possibilities (i.e. when the zeta_order of the base_ring is a proper divisor of, is equal to, and is strictly divisible by the modulus for the DirichletGroup).",
    "created_at": "2008-04-19T23:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20413",
    "user": "craigcitro"
}
```

Yep, this was a mistake on my part. The attached patch fixes it, adds a few doctests to check the various possibilities (i.e. when the zeta_order of the base_ring is a proper divisor of, is equal to, and is strictly divisible by the modulus for the DirichletGroup).



---

archive/issue_comments_020414.json:
```json
{
    "body": "Attachment [trac-2959.patch](tarball://root/attachments/some-uuid/ticket2959/trac-2959.patch) by craigcitro created at 2008-04-19 23:54:42",
    "created_at": "2008-04-19T23:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20414",
    "user": "craigcitro"
}
```

Attachment [trac-2959.patch](tarball://root/attachments/some-uuid/ticket2959/trac-2959.patch) by craigcitro created at 2008-04-19 23:54:42



---

archive/issue_comments_020415.json:
```json
{
    "body": "Looks good; works.",
    "created_at": "2008-04-20T00:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20415",
    "user": "was"
}
```

Looks good; works.



---

archive/issue_comments_020416.json:
```json
{
    "body": "Merges in Sage 3.0.rc0",
    "created_at": "2008-04-20T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20416",
    "user": "mabshoff"
}
```

Merges in Sage 3.0.rc0



---

archive/issue_comments_020417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2959#issuecomment-20417",
    "user": "mabshoff"
}
```

Resolution: fixed
