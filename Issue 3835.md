# Issue 3835: Make an algebraic closure function

archive/issues_003835.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  ncalexan\n\nIt would be nice to be able to construct the algebraic closure of an object.  For example, QQ.algebraic_closure() should return QQbar.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3835\n\n",
    "created_at": "2008-08-13T15:03:21Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Make an algebraic closure function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3835",
    "user": "jason"
}
```
Assignee: tbd

CC:  ncalexan

It would be nice to be able to construct the algebraic closure of an object.  For example, QQ.algebraic_closure() should return QQbar.

Issue created by migration from https://trac.sagemath.org/ticket/3835





---

archive/issue_comments_027266.json:
```json
{
    "body": "Applies to 4.1.1",
    "created_at": "2009-08-30T20:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27266",
    "user": "cremona"
}
```

Applies to 4.1.1



---

archive/issue_comments_027267.json:
```json
{
    "body": "Attachment [trac_3835-algebraic_closure.patch](tarball://root/attachments/some-uuid/ticket3835/trac_3835-algebraic_closure.patch) by cremona created at 2009-08-30 20:36:33\n\nThe attached patch implements this in the trivial cases now possible:  for a number field (including QQ) return QQbar;  for RR return CC, with the same precision (this was already implemented);  for CC, return the same field;  for finite fields, raise NotImplementedError; else raise NotImplementedError.\n\nI'm not sure if this is what Jason intended, but it would be a major undertaking to implement this in any other cases (finite fields, p-adic fields, function fields. ...)",
    "created_at": "2009-08-30T20:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27267",
    "user": "cremona"
}
```

Attachment [trac_3835-algebraic_closure.patch](tarball://root/attachments/some-uuid/ticket3835/trac_3835-algebraic_closure.patch) by cremona created at 2009-08-30 20:36:33

The attached patch implements this in the trivial cases now possible:  for a number field (including QQ) return QQbar;  for RR return CC, with the same precision (this was already implemented);  for CC, return the same field;  for finite fields, raise NotImplementedError; else raise NotImplementedError.

I'm not sure if this is what Jason intended, but it would be a major undertaking to implement this in any other cases (finite fields, p-adic fields, function fields. ...)



---

archive/issue_comments_027268.json:
```json
{
    "body": "Changing keywords from \"\" to \"fields\".",
    "created_at": "2009-08-30T20:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27268",
    "user": "cremona"
}
```

Changing keywords from "" to "fields".



---

archive/issue_comments_027269.json:
```json
{
    "body": "My use-case at the time was QQ -> QQbar, I think.",
    "created_at": "2009-08-31T13:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27269",
    "user": "jason"
}
```

My use-case at the time was QQ -> QQbar, I think.



---

archive/issue_comments_027270.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-08T03:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27270",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_027271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-08T10:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3835#issuecomment-27271",
    "user": "mvngu"
}
```

Resolution: fixed
