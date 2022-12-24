# Issue 5719: [with patch, needs review] Corrected a bad deprecation message.

archive/issues_005719.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: Warning message\n\nCurrenctly when calling count on a combinatorial class the deprecation message is:\n   \n   The usage of iterator for combinatorial classes is deprecated. Please use the class itself\n\nWhereas it should be\n\n   The usage of count for combinatorial classes is deprecated. Please use cardinality\n\nCorrected my patch. Apologies for this mistake. Thanks to Daniel Bump for reporting it. \n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/5719\n\n",
    "created_at": "2009-04-08T21:20:05Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Corrected a bad deprecation message.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5719",
    "user": "hivert"
}
```
Assignee: hivert

CC:  sage-combinat

Keywords: Warning message

Currenctly when calling count on a combinatorial class the deprecation message is:
   
   The usage of iterator for combinatorial classes is deprecated. Please use the class itself

Whereas it should be

   The usage of count for combinatorial classes is deprecated. Please use cardinality

Corrected my patch. Apologies for this mistake. Thanks to Daniel Bump for reporting it. 

Florent

Issue created by migration from https://trac.sagemath.org/ticket/5719





---

archive/issue_comments_044688.json:
```json
{
    "body": "Attachment [warning-fix-submitted.patch](tarball://root/attachments/some-uuid/ticket5719/warning-fix-submitted.patch) by hivert created at 2009-04-08 21:21:04",
    "created_at": "2009-04-08T21:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5719#issuecomment-44688",
    "user": "hivert"
}
```

Attachment [warning-fix-submitted.patch](tarball://root/attachments/some-uuid/ticket5719/warning-fix-submitted.patch) by hivert created at 2009-04-08 21:21:04



---

archive/issue_comments_044689.json:
```json
{
    "body": "Looks good to me, I am doctesting this now. Positive review pending passing doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T21:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5719#issuecomment-44689",
    "user": "mabshoff"
}
```

Looks good to me, I am doctesting this now. Positive review pending passing doctests.

Cheers,

Michael



---

archive/issue_comments_044690.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T21:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5719#issuecomment-44690",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-08T21:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5719#issuecomment-44691",
    "user": "mabshoff"
}
```

Resolution: fixed
