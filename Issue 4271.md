# Issue 4271: [with patch, needs review] improve coverage test of ell_generic.py to 100%, and fix typos

archive/issues_004271.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nbash-3.00$ sage -t ell_generic.py\nsage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n         [74.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 74.0 seconds\nbash-3.00$ sage -coverage ell_generic.py\n----------------------------------------------------------------------\nell_generic.py\nSCORE ell_generic.py: 100% (60 of 60)\n----------------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4271\n\n",
    "created_at": "2008-10-12T20:07:22Z",
    "labels": [
        "doctest coverage",
        "trivial",
        "enhancement"
    ],
    "title": "[with patch, needs review] improve coverage test of ell_generic.py to 100%, and fix typos",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4271",
    "user": "zimmerma"
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

archive/issue_comments_031181.json:
```json
{
    "body": "Attachment [10553.patch](tarball://root/attachments/some-uuid/ticket4271/10553.patch) by zimmerma created at 2008-10-12 20:07:38",
    "created_at": "2008-10-12T20:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31181",
    "user": "zimmerma"
}
```

Attachment [10553.patch](tarball://root/attachments/some-uuid/ticket4271/10553.patch) by zimmerma created at 2008-10-12 20:07:38



---

archive/issue_comments_031182.json:
```json
{
    "body": "The patch is good.  It apples cleanly to 3.1.3.alpha3 and works as advertised.  Thanks, Paul -- almost all those typos were due to me!\n\nJohn (in his lunch break in Bordeaux)\n\nMichael: this only affects docstrings so should have no effect outside this one file.",
    "created_at": "2008-10-13T11:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31182",
    "user": "cremona"
}
```

The patch is good.  It apples cleanly to 3.1.3.alpha3 and works as advertised.  Thanks, Paul -- almost all those typos were due to me!

John (in his lunch break in Bordeaux)

Michael: this only affects docstrings so should have no effect outside this one file.



---

archive/issue_comments_031183.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n> Michael: this only affects docstrings so should have no effect outside this one file.\n\nHi John,\n\nyou actually beat me to a review and I was also convinced that this patch has 0% risk, so I will merge it into 3.1.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-13T12:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31183",
    "user": "mabshoff"
}
```

Replying to [comment:1 cremona]:
> Michael: this only affects docstrings so should have no effect outside this one file.

Hi John,

you actually beat me to a review and I was also convinced that this patch has 0% risk, so I will merge it into 3.1.3.

Cheers,

Michael



---

archive/issue_comments_031184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-14T12:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31184",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031185.json:
```json
{
    "body": "Merged in Sage 3.1.3.final",
    "created_at": "2008-10-14T12:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4271#issuecomment-31185",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.final
