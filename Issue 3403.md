# Issue 3403: [with patch; needs review] get doctest coverage for rational up to 100%

archive/issues_003403.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3403\n\n",
    "created_at": "2008-06-12T15:14:25Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch; needs review] get doctest coverage for rational up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3403",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/3403





---

archive/issue_comments_023826.json:
```json
{
    "body": "Attachment [sage-3403.patch](tarball://root/attachments/some-uuid/ticket3403/sage-3403.patch) by @garyfurnish created at 2008-06-15 20:27:14",
    "created_at": "2008-06-15T20:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3403#issuecomment-23826",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [sage-3403.patch](tarball://root/attachments/some-uuid/ticket3403/sage-3403.patch) by @garyfurnish created at 2008-06-15 20:27:14



---

archive/issue_events_003619.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-06-26T03:27:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3403#event-3619"
}
```



---

archive/issue_comments_023827.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3403#issuecomment-23827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3403#issuecomment-23828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023829.json:
```json
{
    "body": "We have one broken doctest:\n\n```\nsage -t  devel/sage/sage/misc/sageinspect.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/sageinspect.py\", line 77:\n    sage: sage_getdoc(sage.rings.rational.make_rational).lstrip()\nExpected:\n    ''\nGot:\n    \"Make a rational number from s (a string in base 32)\\n\\n    INPUT:\\n        s -- string in base 32\\n    OUTPUT:\\n        Rational\\n        \\n    EXAMPLES:\\n        sage: (-7/15).str(32)\\n        '-7/f'\\n        sage: sage.rings.rational.make_rational('-7/f')\\n        -7/15    \\n    \"\n**********************************************************************\n1 items had failures:\n   1 of  26 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/.doctest_sageinspect.py\n\t [2.6 s]\nexit code: 1024\n```\n",
    "created_at": "2008-06-26T04:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3403#issuecomment-23829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We have one broken doctest:

```
sage -t  devel/sage/sage/misc/sageinspect.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/sageinspect.py", line 77:
    sage: sage_getdoc(sage.rings.rational.make_rational).lstrip()
Expected:
    ''
Got:
    "Make a rational number from s (a string in base 32)\n\n    INPUT:\n        s -- string in base 32\n    OUTPUT:\n        Rational\n        \n    EXAMPLES:\n        sage: (-7/15).str(32)\n        '-7/f'\n        sage: sage.rings.rational.make_rational('-7/f')\n        -7/15    \n    "
**********************************************************************
1 items had failures:
   1 of  26 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha1/tmp/.doctest_sageinspect.py
	 [2.6 s]
exit code: 1024
```




---

archive/issue_comments_023830.json:
```json
{
    "body": "Fixed in Sage 3.0.4.alpha1 as discussed with William in person.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T05:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3403#issuecomment-23830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.0.4.alpha1 as discussed with William in person.

Cheers,

Michael
