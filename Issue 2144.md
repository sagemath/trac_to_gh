# Issue 2144: hex constants do not work as expected

archive/issues_002144.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: preparser hex constants\n\nTrying to use hex constants in SAGE as I usually do in Python, I ran into a small issue: the following should work, but does not:\n\n\n```\nsage: 0x23^0x42\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(0)x23**Integer(0)x42\n                 ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\n\nI was told on #sage-devel that this is due to the preparser. A work around is to use `0rx23^0rx42` instead. However, according to william_stein, 0x23 should work as well and result in an Integer and 0x23r should be treated as an int.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2144\n\n",
    "created_at": "2008-02-12T07:35:29Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "hex constants do not work as expected",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2144",
    "user": "rpw"
}
```
Assignee: somebody

Keywords: preparser hex constants

Trying to use hex constants in SAGE as I usually do in Python, I ran into a small issue: the following should work, but does not:


```
sage: 0x23^0x42
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0)x23**Integer(0)x42
                 ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


I was told on #sage-devel that this is due to the preparser. A work around is to use `0rx23^0rx42` instead. However, according to william_stein, 0x23 should work as well and result in an Integer and 0x23r should be treated as an int.

Issue created by migration from https://trac.sagemath.org/ticket/2144





---

archive/issue_comments_014061.json:
```json
{
    "body": "Attachment [2144-hex-preparse.patch](tarball://root/attachments/some-uuid/ticket2144/2144-hex-preparse.patch) by robertwb created at 2008-02-14 06:05:26",
    "created_at": "2008-02-14T06:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14061",
    "user": "robertwb"
}
```

Attachment [2144-hex-preparse.patch](tarball://root/attachments/some-uuid/ticket2144/2144-hex-preparse.patch) by robertwb created at 2008-02-14 06:05:26



---

archive/issue_comments_014062.json:
```json
{
    "body": "I say apply, but there are no doctests!  Why is the preparser not considered important enough to be tested?",
    "created_at": "2008-02-15T03:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14062",
    "user": "ncalexan"
}
```

I say apply, but there are no doctests!  Why is the preparser not considered important enough to be tested?



---

archive/issue_comments_014063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14063",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014064.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14064",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_014065.json:
```json
{
    "body": "Attachment [trac-2144-doctest.patch](tarball://root/attachments/some-uuid/ticket2144/trac-2144-doctest.patch) by was created at 2008-02-15 10:13:41",
    "created_at": "2008-02-15T10:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14065",
    "user": "was"
}
```

Attachment [trac-2144-doctest.patch](tarball://root/attachments/some-uuid/ticket2144/trac-2144-doctest.patch) by was created at 2008-02-15 10:13:41



---

archive/issue_comments_014066.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-15T10:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14066",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_014067.json:
```json
{
    "body": "> Why is the preparser not considered important enough to be tested?\n\nThe preparse *is* important enough to be doctests.  I certainly don't\nconsider that to not be the case.  Any new code in Sage should get a negative review if there is any reasonable way to test that it fixes the claimed issue, but the patch doesn't actually test this fix explicitly. \n\nSo shis should not have been closed without a doctest.  I've attached \na patch that does that.",
    "created_at": "2008-02-15T10:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14067",
    "user": "was"
}
```

> Why is the preparser not considered important enough to be tested?

The preparse *is* important enough to be doctests.  I certainly don't
consider that to not be the case.  Any new code in Sage should get a negative review if there is any reasonable way to test that it fixes the claimed issue, but the patch doesn't actually test this fix explicitly. 

So shis should not have been closed without a doctest.  I've attached 
a patch that does that.



---

archive/issue_comments_014068.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-02-15T10:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14068",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_014069.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2008-02-15T10:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14069",
    "user": "was"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_014070.json:
```json
{
    "body": "While 2144-hex-preparse.patch has been merged, trac-2144-doctest.patch needs review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T13:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14070",
    "user": "mabshoff"
}
```

While 2144-hex-preparse.patch has been merged, trac-2144-doctest.patch needs review.

Cheers,

Michael



---

archive/issue_comments_014071.json:
```json
{
    "body": "The added doctest looks good -> positive review for trac-2144-doctest.patch",
    "created_at": "2008-02-15T22:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14071",
    "user": "mabshoff"
}
```

The added doctest looks good -> positive review for trac-2144-doctest.patch



---

archive/issue_comments_014072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T22:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14072",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014073.json:
```json
{
    "body": "Merged trac-2144-doctest.patch in Sage 2.10.2.alpha1",
    "created_at": "2008-02-15T22:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14073",
    "user": "mabshoff"
}
```

Merged trac-2144-doctest.patch in Sage 2.10.2.alpha1



---

archive/issue_comments_014074.json:
```json
{
    "body": "It turns out that:\n\n  (1) this is a dupe of #37, and\n\n  (2) it doesn't even work!  I stupidly didn't test with interesting inputs, and with them the patch by robertwb fails.  E.g.,\n\n```\nsage: 0x10\n16\nsage: 0xa\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(0x)a\n                ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\n\nFortunately, I have attached a patch to #37 that really fixes\nthe problem.",
    "created_at": "2008-02-28T04:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2144#issuecomment-14074",
    "user": "was"
}
```

It turns out that:

  (1) this is a dupe of #37, and

  (2) it doesn't even work!  I stupidly didn't test with interesting inputs, and with them the patch by robertwb fails.  E.g.,

```
sage: 0x10
16
sage: 0xa
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)a
                ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


Fortunately, I have attached a patch to #37 that really fixes
the problem.
