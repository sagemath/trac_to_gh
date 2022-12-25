# Issue 4720: Numerical noise in test sage/rings/number_field/number_field_morphisms.pyx

archive/issues_004720.json:
```json
{
    "body": "Assignee: tbd\n\nOn Fedora 10, 32 bits in sage-3.2.2.alpha0 the following test failed:\n\n\n\n```\nExpecting:\n     -0.500000000000000 + 0.866025403784439*I\n**********************************************************************\nFile \"/home/jaap/Download/sage-3.2.1.rc0/devel/sage/sage/rings/number_field/number_field_morphisms.pyx\",\nline 210, in __main__.example_10\nFailed example:\n     closest_root(x**Integer(3)-Integer(1), CDF.gen(0))###line\n223:_sage_    >>> closest_root(x^3-1, CDF.0)\nExpected:\n     -0.500000000000000 + 0.866025403784439*I\nGot:\n     -0.500000000000000 + 0.866025403784438*I\n\n\n```\n\n\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4720\n\n",
    "created_at": "2008-12-05T21:57:48Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Numerical noise in test sage/rings/number_field/number_field_morphisms.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4720",
    "user": "https://github.com/jaapspies"
}
```
Assignee: tbd

On Fedora 10, 32 bits in sage-3.2.2.alpha0 the following test failed:



```
Expecting:
     -0.500000000000000 + 0.866025403784439*I
**********************************************************************
File "/home/jaap/Download/sage-3.2.1.rc0/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 210, in __main__.example_10
Failed example:
     closest_root(x**Integer(3)-Integer(1), CDF.gen(0))###line
223:_sage_    >>> closest_root(x^3-1, CDF.0)
Expected:
     -0.500000000000000 + 0.866025403784439*I
Got:
     -0.500000000000000 + 0.866025403784438*I


```



Jaap



Issue created by migration from https://trac.sagemath.org/ticket/4720





---

archive/issue_comments_035533.json:
```json
{
    "body": "Same failure on Fedora 9, 32 bits.\n\nJaap",
    "created_at": "2008-12-05T22:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35533",
    "user": "https://github.com/jaapspies"
}
```

Same failure on Fedora 9, 32 bits.

Jaap



---

archive/issue_comments_035534.json:
```json
{
    "body": "This patch fixes it for me.",
    "created_at": "2008-12-09T18:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35534",
    "user": "https://github.com/jhpalmieri"
}
```

This patch fixes it for me.



---

archive/issue_comments_035535.json:
```json
{
    "body": "Changing keywords from \"\" to \"numerical noise, number_field_morphism\".",
    "created_at": "2008-12-09T18:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35535",
    "user": "https://github.com/jhpalmieri"
}
```

Changing keywords from "" to "numerical noise, number_field_morphism".



---

archive/issue_comments_035536.json:
```json
{
    "body": "Attachment [4720.patch](tarball://root/attachments/some-uuid/ticket4720/4720.patch) by @ncalexan created at 2008-12-09 19:07:21\n\nFine by me.",
    "created_at": "2008-12-09T19:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35536",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4720.patch](tarball://root/attachments/some-uuid/ticket4720/4720.patch) by @ncalexan created at 2008-12-09 19:07:21

Fine by me.



---

archive/issue_comments_035537.json:
```json
{
    "body": "This patch needs to be rebased:\n\n```\nsage-3.2.2.alpha1/devel/sage$ patch -p1 < trac_4720.patch \npatching file sage/rings/number_field/number_field_morphisms.pyx\nHunk #1 FAILED at 221.\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/number_field/number_field_morphisms.pyx.rej\n```\n\nI will look into it.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch needs to be rebased:

```
sage-3.2.2.alpha1/devel/sage$ patch -p1 < trac_4720.patch 
patching file sage/rings/number_field/number_field_morphisms.pyx
Hunk #1 FAILED at 221.
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/number_field/number_field_morphisms.pyx.rej
```

I will look into it.

Cheers,

Michael



---

archive/issue_comments_035538.json:
```json
{
    "body": "Attachment [trac_4720.patch](tarball://root/attachments/some-uuid/ticket4720/trac_4720.patch) by mabshoff created at 2008-12-10 09:17:57\n\nrebased version of John's patch",
    "created_at": "2008-12-10T09:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4720.patch](tarball://root/attachments/some-uuid/ticket4720/trac_4720.patch) by mabshoff created at 2008-12-10 09:17:57

rebased version of John's patch



---

archive/issue_events_004965.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-10T09:19:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4720#event-4965"
}
```



---

archive/issue_comments_035539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-10T09:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035540.json:
```json
{
    "body": "Merged trac_4720.patch in Sage 3.2.2.alpha1.\n\nNote that trac_4276-nf-coerce-fixes3.patch renamed closest_root to matching_root which cause the merge trouble.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T09:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4720#issuecomment-35540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4720.patch in Sage 3.2.2.alpha1.

Note that trac_4276-nf-coerce-fixes3.patch renamed closest_root to matching_root which cause the merge trouble.

Cheers,

Michael
