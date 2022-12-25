# Issue 5056: rename Ideal.reduced_basis to Ideal.interreduced_basis

archive/issues_005056.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @johnperry-math\n\nIt seems like people get confused by the name and assume the function returns the reduced **Gr\u00f6bner** basis. Thus `reduced_basis()` should be deprecated and `interreduced_basis()` should take its place.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5056\n\n",
    "created_at": "2009-01-22T18:34:52Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "rename Ideal.reduced_basis to Ideal.interreduced_basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5056",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @johnperry-math

It seems like people get confused by the name and assume the function returns the reduced **Gröbner** basis. Thus `reduced_basis()` should be deprecated and `interreduced_basis()` should take its place.

Issue created by migration from https://trac.sagemath.org/ticket/5056





---

archive/issue_comments_038446.json:
```json
{
    "body": "\"patch\", not \"path\"",
    "created_at": "2009-01-22T23:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38446",
    "user": "https://github.com/johnperry-math"
}
```

"patch", not "path"



---

archive/issue_comments_038447.json:
```json
{
    "body": "Attachment [interreduced_basis_path](tarball://root/attachments/some-uuid/ticket5056/interreduced_basis_path) by @malb created at 2009-01-23 02:45:22",
    "created_at": "2009-01-23T02:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38447",
    "user": "https://github.com/malb"
}
```

Attachment [interreduced_basis_path](tarball://root/attachments/some-uuid/ticket5056/interreduced_basis_path) by @malb created at 2009-01-23 02:45:22



---

archive/issue_comments_038448.json:
```json
{
    "body": "The patch applies cleanly (in spite of its strange name :) ), there is a deprecation warning, and the doc tests of `multi_polynomial_ideal.py` pass. In other words, the patch does what it is supposed to.\nPositive review!",
    "created_at": "2009-01-24T16:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38448",
    "user": "https://github.com/simon-king-jena"
}
```

The patch applies cleanly (in spite of its strange name :) ), there is a deprecation warning, and the doc tests of `multi_polynomial_ideal.py` pass. In other words, the patch does what it is supposed to.
Positive review!



---

archive/issue_comments_038449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T02:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038450.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5056#issuecomment-38450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael
