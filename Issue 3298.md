# Issue 3298: Cython warnings for PolyBoRi

archive/issues_003298.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @robertwb @burcin\n\nKeywords: polybori, cython\n\n\n```\npython2.5 `which cython` --embed-positions --incref-local-binop -I/usr/local/sage-3.0/devel/sage-main -opbori.pyx\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:40:56: Function signature does not match previous declaration\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:41:59: Function signature does not match previous declaration\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:200:10: Function signature does not match previous declaration\nFinished updating Cython code (time = 2.520616 seconds)\n```\n\n\nI couldn't figure out what is wrong. Maybe a false positive?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3298\n\n",
    "created_at": "2008-05-25T13:41:31Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Cython warnings for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3298",
    "user": "@malb"
}
```
Assignee: cwitty

CC:  @robertwb @burcin

Keywords: polybori, cython


```
python2.5 `which cython` --embed-positions --incref-local-binop -I/usr/local/sage-3.0/devel/sage-main -opbori.pyx
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:40:56: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:41:59: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:200:10: Function signature does not match previous declaration
Finished updating Cython code (time = 2.520616 seconds)
```


I couldn't figure out what is wrong. Maybe a false positive?

Issue created by migration from https://trac.sagemath.org/ticket/3298





---

archive/issue_comments_022824.json:
```json
{
    "body": "fix cython warnings for pbori.pyx",
    "created_at": "2009-01-24T19:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22824",
    "user": "@burcin"
}
```

fix cython warnings for pbori.pyx



---

archive/issue_comments_022825.json:
```json
{
    "body": "Changing assignee from cwitty to @burcin.",
    "created_at": "2009-01-24T19:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22825",
    "user": "@burcin"
}
```

Changing assignee from cwitty to @burcin.



---

archive/issue_comments_022826.json:
```json
{
    "body": "Attachment [trac_3298-pbori_cython_warnings.patch](tarball://root/attachments/some-uuid/ticket3298/trac_3298-pbori_cython_warnings.patch) by @burcin created at 2009-01-24 19:07:29\n\nThrough a chain of typedefs the parameter expected by these functions was defined to be int, not the enum declared in the .pxi file. With the attached patch, the warnings go away. :)",
    "created_at": "2009-01-24T19:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22826",
    "user": "@burcin"
}
```

Attachment [trac_3298-pbori_cython_warnings.patch](tarball://root/attachments/some-uuid/ticket3298/trac_3298-pbori_cython_warnings.patch) by @burcin created at 2009-01-24 19:07:29

Through a chain of typedefs the parameter expected by these functions was defined to be int, not the enum declared in the .pxi file. With the attached patch, the warnings go away. :)



---

archive/issue_comments_022827.json:
```json
{
    "body": "Looks good.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22827",
    "user": "mabshoff"
}
```

Looks good.

Cheers,

Michael



---

archive/issue_comments_022828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22828",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022829.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T19:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22829",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
