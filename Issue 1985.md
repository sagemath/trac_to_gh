# Issue 1985: is_pseudoprime docstring doesn't wrap

archive/issues_001985.json:
```json
{
    "body": "Assignee: mabshoff\n\nReported by Steve Vonn in https://groups.google.com/group/sage-support/t/ea050f051600e792\n\n```\nis_pseudoprime?\nThe help entry for (is_pseudoprime) has a nonwrapping text bug\n\nINPUT:\n        flag -- int\n                0 (default): checks whether x is a Baillie-Pomerance-Selfridge-Wagstaff pseudo prime (strong Rabin-Miller pseudo prime for base 2, followed by strong Lucas test for the sequence (P,-1), P smallest positive integer such that P^2 - 4 is not a square mod x).\n                > 0: checks whether x is a strong Miller-Rabin pseudo prime for flag randomly chosen bases (with end-matching to catch\nsquare roots of -1). \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1985\n\n",
    "created_at": "2008-01-30T15:01:28Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "is_pseudoprime docstring doesn't wrap",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1985",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Reported by Steve Vonn in https://groups.google.com/group/sage-support/t/ea050f051600e792

```
is_pseudoprime?
The help entry for (is_pseudoprime) has a nonwrapping text bug

INPUT:
        flag -- int
                0 (default): checks whether x is a Baillie-Pomerance-Selfridge-Wagstaff pseudo prime (strong Rabin-Miller pseudo prime for base 2, followed by strong Lucas test for the sequence (P,-1), P smallest positive integer such that P^2 - 4 is not a square mod x).
                > 0: checks whether x is a strong Miller-Rabin pseudo prime for flag randomly chosen bases (with end-matching to catch
square roots of -1). 
```


Issue created by migration from https://trac.sagemath.org/ticket/1985





---

archive/issue_comments_012857.json:
```json
{
    "body": "Attachment [Sage-2.10.1.rc4-fix-is_pseudoprime-docstring-wrapping_trac_1985.patch](tarball://root/attachments/some-uuid/ticket1985/Sage-2.10.1.rc4-fix-is_pseudoprime-docstring-wrapping_trac_1985.patch) by mabshoff created at 2008-01-30 15:16:44",
    "created_at": "2008-01-30T15:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1985#issuecomment-12857",
    "user": "mabshoff"
}
```

Attachment [Sage-2.10.1.rc4-fix-is_pseudoprime-docstring-wrapping_trac_1985.patch](tarball://root/attachments/some-uuid/ticket1985/Sage-2.10.1.rc4-fix-is_pseudoprime-docstring-wrapping_trac_1985.patch) by mabshoff created at 2008-01-30 15:16:44



---

archive/issue_comments_012858.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-30T15:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1985#issuecomment-12858",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_012859.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-01-30T15:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1985#issuecomment-12859",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc4



---

archive/issue_comments_012860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T15:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1985#issuecomment-12860",
    "user": "mabshoff"
}
```

Resolution: fixed
