# Issue 5781: [with patch, need review] The empty standard tableau exists ! :-)

archive/issues_005781.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: tableau\n\nBefore my patch:\n\n```\nsage: [] in StandardTableaux()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/averell/.sage/temp/tomahawk/19026/_home_averell__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/sage/local/lib/python2.5/site-packages/sage/combinat/tableau.pyc in __contains__(self, x)\n   1740             fillings += row\n   1741         fillings.sort()\n-> 1742         if fillings != range(1, max(fillings)+1):\n   1743             return False\n   1744\n\nValueError: max() arg is an empty sequence\n```\n\n\nNow:\n\n```\nsage: [] in StandardTableaux()\nTrue\n```\n\n\nFlorent, the specialist of the empty objects !!!\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5781\n\n",
    "created_at": "2009-04-13T22:03:38Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, need review] The empty standard tableau exists ! :-)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5781",
    "user": "@hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: tableau

Before my patch:

```
sage: [] in StandardTableaux()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/averell/.sage/temp/tomahawk/19026/_home_averell__sage_init_sage_0.py in <module>()

/usr/local/sage/sage/local/lib/python2.5/site-packages/sage/combinat/tableau.pyc in __contains__(self, x)
   1740             fillings += row
   1741         fillings.sort()
-> 1742         if fillings != range(1, max(fillings)+1):
   1743             return False
   1744

ValueError: max() arg is an empty sequence
```


Now:

```
sage: [] in StandardTableaux()
True
```


Florent, the specialist of the empty objects !!!


Issue created by migration from https://trac.sagemath.org/ticket/5781





---

archive/issue_comments_045256.json:
```json
{
    "body": "Attachment [empty_standard_tableau-fh-final.patch](tarball://root/attachments/some-uuid/ticket5781/empty_standard_tableau-fh-final.patch) by @hivert created at 2009-04-13 22:04:07",
    "created_at": "2009-04-13T22:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5781#issuecomment-45256",
    "user": "@hivert"
}
```

Attachment [empty_standard_tableau-fh-final.patch](tarball://root/attachments/some-uuid/ticket5781/empty_standard_tableau-fh-final.patch) by @hivert created at 2009-04-13 22:04:07



---

archive/issue_comments_045257.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-13T22:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5781#issuecomment-45257",
    "user": "@hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045258.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T23:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5781#issuecomment-45258",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045259.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T23:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5781#issuecomment-45259",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
