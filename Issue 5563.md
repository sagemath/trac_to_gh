# Issue 5563: [with patch, needs review] Doctest failure in devel/sage/doc/en/bordeaux_2008/modular_....rst

archive/issues_005563.json:
```json
{
    "body": "Assignee: mabshoff\n\nmodular_forms_and_hecke_operators.rst\ncontains a call to sloane_find() which requires internet access, leading to a failure if you don't\n\nIssue created by migration from https://trac.sagemath.org/ticket/5563\n\n",
    "created_at": "2009-03-18T23:37:35Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Doctest failure in devel/sage/doc/en/bordeaux_2008/modular_....rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5563",
    "user": "GeorgSWeber"
}
```
Assignee: mabshoff

modular_forms_and_hecke_operators.rst
contains a call to sloane_find() which requires internet access, leading to a failure if you don't

Issue created by migration from https://trac.sagemath.org/ticket/5563





---

archive/issue_comments_043298.json:
```json
{
    "body": "Attachment\n\npatch against Sage 3.4",
    "created_at": "2009-03-18T23:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43298",
    "user": "GeorgSWeber"
}
```

Attachment

patch against Sage 3.4



---

archive/issue_comments_043299.json:
```json
{
    "body": "The issue had been reported originally by Minh Nguyen in the thread\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/ce81352fe52292bd/a199ed5de16c81a8#a199ed5de16c81a8",
    "created_at": "2009-03-18T23:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43299",
    "user": "GeorgSWeber"
}
```

The issue had been reported originally by Minh Nguyen in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/ce81352fe52292bd/a199ed5de16c81a8#a199ed5de16c81a8



---

archive/issue_comments_043300.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **sloane_find_optional.patch** applies OK against Sage 3.4. All tests passed, both on machines with and without Internet connection. Just to be on the safe side, I rebuilt the HTML version of the whole reference manual; rebuilding went fine as expected on machines with and without Internet connection. Positive review.",
    "created_at": "2009-03-19T04:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43300",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch **sloane_find_optional.patch** applies OK against Sage 3.4. All tests passed, both on machines with and without Internet connection. Just to be on the safe side, I rebuilt the HTML version of the whole reference manual; rebuilding went fine as expected on machines with and without Internet connection. Positive review.



---

archive/issue_comments_043301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T18:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43301",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043302.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T18:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5563#issuecomment-43302",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
