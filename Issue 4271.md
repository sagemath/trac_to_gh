# Issue 4271: [with patch, needs review] improve coverage test of ell_generic.py to 100%, and fix typos

archive/issues_004271.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nbash-3.00$ sage -t ell_generic.py\nsage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n         [74.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 74.0 seconds\nbash-3.00$ sage -coverage ell_generic.py\n----------------------------------------------------------------------\nell_generic.py\nSCORE ell_generic.py: 100% (60 of 60)\n----------------------------------------------------------------------\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4271\n\n",
    "created_at": "2008-10-12T20:07:22Z",
    "labels": [
        "component: doctest coverage",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] improve coverage test of ell_generic.py to 100%, and fix typos",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4271",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

```
bash-3.00$ sage -t ell_generic.py
sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
         [74.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 74.0 seconds
bash-3.00$ sage -coverage ell_generic.py
----------------------------------------------------------------------
ell_generic.py
SCORE ell_generic.py: 100% (60 of 60)
----------------------------------------------------------------------
```

Issue created by migration from https://trac.sagemath.org/ticket/4271





---

archive/issue_comments_031119.json:
```json
{
    "body": "Attachment [10553.patch](tarball://root/attachments/some-uuid/ticket4271/10553.patch) by @zimmermann6 created at 2008-10-12 20:07:38",
    "created_at": "2008-10-12T20:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31119",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [10553.patch](tarball://root/attachments/some-uuid/ticket4271/10553.patch) by @zimmermann6 created at 2008-10-12 20:07:38



---

archive/issue_comments_031120.json:
```json
{
    "body": "The patch is good.  It apples cleanly to 3.1.3.alpha3 and works as advertised.  Thanks, Paul -- almost all those typos were due to me!\n\nJohn (in his lunch break in Bordeaux)\n\nMichael: this only affects docstrings so should have no effect outside this one file.",
    "created_at": "2008-10-13T11:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31120",
    "user": "https://github.com/JohnCremona"
}
```

The patch is good.  It apples cleanly to 3.1.3.alpha3 and works as advertised.  Thanks, Paul -- almost all those typos were due to me!

John (in his lunch break in Bordeaux)

Michael: this only affects docstrings so should have no effect outside this one file.



---

archive/issue_comments_031121.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n> Michael: this only affects docstrings so should have no effect outside this one file.\n\n\nHi John,\n\nyou actually beat me to a review and I was also convinced that this patch has 0% risk, so I will merge it into 3.1.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-13T12:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 cremona]:
> Michael: this only affects docstrings so should have no effect outside this one file.


Hi John,

you actually beat me to a review and I was also convinced that this patch has 0% risk, so I will merge it into 3.1.3.

Cheers,

Michael



---

archive/issue_events_009653.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-13T12:40:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4271#event-9653"
}
```



---

archive/issue_events_009654.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-14T12:31:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4271#event-9654"
}
```



---

archive/issue_comments_031122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-14T12:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031123.json:
```json
{
    "body": "Merged in Sage 3.1.3.final",
    "created_at": "2008-10-14T12:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.final
