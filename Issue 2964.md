# Issue 2964: Improvements to weyl_group.py

archive/issues_002964.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nWeylGroup gets a proper __call__ method that produces a WeylGroup element. Previously if G is a Weyl group then G(m) produced a MatrixRing element. This part is a bugfix.\n\nRoot systems get a method to produce the highest root, relevant to the affine root system. This could be\nimplemented as a case-by-case method and that would be faster, but searching through the roots for\nthe highest weight is of acceptable speed.\n\nWeyl Groups get a method to produce the long element of the Weyl group. Not implemented yet for E7 and E8.\n\nWeyl group also gets a method to produce the identity element as a WeylGroup element. Strictly speaking this is\nnot necessary since W(1) will also produce the unit.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2964\n\n",
    "created_at": "2008-04-20T03:51:15Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "title": "Improvements to weyl_group.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2964",
    "user": "bump"
}
```
Assignee: mhansen

CC:  sage-combinat

WeylGroup gets a proper __call__ method that produces a WeylGroup element. Previously if G is a Weyl group then G(m) produced a MatrixRing element. This part is a bugfix.

Root systems get a method to produce the highest root, relevant to the affine root system. This could be
implemented as a case-by-case method and that would be faster, but searching through the roots for
the highest weight is of acceptable speed.

Weyl Groups get a method to produce the long element of the Weyl group. Not implemented yet for E7 and E8.

Weyl group also gets a method to produce the identity element as a WeylGroup element. Strictly speaking this is
not necessary since W(1) will also produce the unit.

Issue created by migration from https://trac.sagemath.org/ticket/2964





---

archive/issue_comments_020436.json:
```json
{
    "body": "Attachment [9564.patch](tarball://root/attachments/some-uuid/ticket2964/9564.patch) by bump created at 2008-04-20 03:52:32",
    "created_at": "2008-04-20T03:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20436",
    "user": "bump"
}
```

Attachment [9564.patch](tarball://root/attachments/some-uuid/ticket2964/9564.patch) by bump created at 2008-04-20 03:52:32



---

archive/issue_comments_020437.json:
```json
{
    "body": "Attachment [9565.patch](tarball://root/attachments/some-uuid/ticket2964/9565.patch) by bump created at 2008-04-20 03:54:55\n\nThese are patches against 3.0alpha6.",
    "created_at": "2008-04-20T03:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20437",
    "user": "bump"
}
```

Attachment [9565.patch](tarball://root/attachments/some-uuid/ticket2964/9565.patch) by bump created at 2008-04-20 03:54:55

These are patches against 3.0alpha6.



---

archive/issue_comments_020438.json:
```json
{
    "body": "There will be a further patch because I forgot to finish the doctests.",
    "created_at": "2008-04-20T04:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20438",
    "user": "bump"
}
```

There will be a further patch because I forgot to finish the doctests.



---

archive/issue_comments_020439.json:
```json
{
    "body": "Okay, excellent.  I'll review them when you put them up.",
    "created_at": "2008-04-20T04:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20439",
    "user": "mhansen"
}
```

Okay, excellent.  I'll review them when you put them up.



---

archive/issue_comments_020440.json:
```json
{
    "body": "Attachment [9566.patch](tarball://root/attachments/some-uuid/ticket2964/9566.patch) by bump created at 2008-04-20 04:07:51",
    "created_at": "2008-04-20T04:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20440",
    "user": "bump"
}
```

Attachment [9566.patch](tarball://root/attachments/some-uuid/ticket2964/9566.patch) by bump created at 2008-04-20 04:07:51



---

archive/issue_comments_020441.json:
```json
{
    "body": "I added a third patch with doctest for long element and now I think it is OK.\n\nThanks, Dan",
    "created_at": "2008-04-20T04:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20441",
    "user": "bump"
}
```

I added a third patch with doctest for long element and now I think it is OK.

Thanks, Dan



---

archive/issue_comments_020442.json:
```json
{
    "body": "Attachment [2964-review.patch](tarball://root/attachments/some-uuid/ticket2964/2964-review.patch) by mhansen created at 2008-04-20 05:51:07",
    "created_at": "2008-04-20T05:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20442",
    "user": "mhansen"
}
```

Attachment [2964-review.patch](tarball://root/attachments/some-uuid/ticket2964/2964-review.patch) by mhansen created at 2008-04-20 05:51:07



---

archive/issue_comments_020443.json:
```json
{
    "body": "Looks good to me. Apply all four patches.",
    "created_at": "2008-04-20T05:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20443",
    "user": "mhansen"
}
```

Looks good to me. Apply all four patches.



---

archive/issue_comments_020444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T06:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20444",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020445.json:
```json
{
    "body": "Merged all four patches in Sage 3.0.rc0",
    "created_at": "2008-04-20T06:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2964#issuecomment-20445",
    "user": "mabshoff"
}
```

Merged all four patches in Sage 3.0.rc0
