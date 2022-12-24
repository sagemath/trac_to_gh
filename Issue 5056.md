# Issue 5056: rename Ideal.reduced_basis to Ideal.interreduced_basis

archive/issues_005056.json:
```json
{
    "body": "Assignee: malb\n\nCC:  john_perry\n\nIt seems like people get confused by the name and assume the function returns the reduced **Gr\u00f6bner** basis. Thus `reduced_basis()` should be deprecated and `interreduced_basis()` should take its place.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5056\n\n",
    "created_at": "2009-01-22T18:34:52Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "rename Ideal.reduced_basis to Ideal.interreduced_basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5056",
    "user": "malb"
}
```
Assignee: malb

CC:  john_perry

It seems like people get confused by the name and assume the function returns the reduced **Gröbner** basis. Thus `reduced_basis()` should be deprecated and `interreduced_basis()` should take its place.

Issue created by migration from https://trac.sagemath.org/ticket/5056





---

archive/issue_comments_038519.json:
```json
{
    "body": "\"patch\", not \"path\"",
    "created_at": "2009-01-22T23:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38519",
    "user": "john_perry"
}
```

"patch", not "path"



---

archive/issue_comments_038520.json:
```json
{
    "body": "Attachment [interreduced_basis_path](tarball://root/attachments/some-uuid/ticket5056/interreduced_basis_path) by malb created at 2009-01-23 02:45:22",
    "created_at": "2009-01-23T02:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38520",
    "user": "malb"
}
```

Attachment [interreduced_basis_path](tarball://root/attachments/some-uuid/ticket5056/interreduced_basis_path) by malb created at 2009-01-23 02:45:22



---

archive/issue_comments_038521.json:
```json
{
    "body": "The patch applies cleanly (in spite of its strange name :) ), there is a deprecation warning, and the doc tests of `multi_polynomial_ideal.py` pass. In other words, the patch does what it is supposed to.\nPositive review!",
    "created_at": "2009-01-24T16:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38521",
    "user": "SimonKing"
}
```

The patch applies cleanly (in spite of its strange name :) ), there is a deprecation warning, and the doc tests of `multi_polynomial_ideal.py` pass. In other words, the patch does what it is supposed to.
Positive review!



---

archive/issue_comments_038522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T02:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38522",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038523.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38523",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael
