# Issue 4257: [with patch, needs review] support for Singular's  'intmat' and 'intvec'

archive/issues_004257.json:
```json
{
    "body": "Assignee: malb\n\nCC:  singular\n\nThis now works:\n\n\n```\nsage: A = random_matrix(ZZ,3,3); A\n[ -8   2   0]\n[  0   1  -1]\n[  2   1 -95]\nsage: As = singular(A); As\n-8     2     0\n 0     1    -1\n 2     1   -95\nsage: As._sage_()\n[ -8   2   0]\n[  0   1  -1]\n[  2   1 -95]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4257\n\n",
    "created_at": "2008-10-09T21:54:29Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] support for Singular's  'intmat' and 'intvec'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4257",
    "user": "malb"
}
```
Assignee: malb

CC:  singular

This now works:


```
sage: A = random_matrix(ZZ,3,3); A
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
sage: As = singular(A); As
-8     2     0
 0     1    -1
 2     1   -95
sage: As._sage_()
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
```


Issue created by migration from https://trac.sagemath.org/ticket/4257





---

archive/issue_comments_030983.json:
```json
{
    "body": "Attachment [singular_intmat.patch](tarball://root/attachments/some-uuid/ticket4257/singular_intmat.patch) by malb created at 2008-10-10 08:46:24",
    "created_at": "2008-10-10T08:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30983",
    "user": "malb"
}
```

Attachment [singular_intmat.patch](tarball://root/attachments/some-uuid/ticket4257/singular_intmat.patch) by malb created at 2008-10-10 08:46:24



---

archive/issue_comments_030984.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-10T16:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30984",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_030985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-11T06:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30985",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030986.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-11T06:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4257#issuecomment-30986",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0
