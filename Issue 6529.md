# Issue 6529: adding doctests to arith.py

archive/issues_006529.json:
```json
{
    "body": "Assignee: somebody\n\narith.py currently has quite a few doctests missing.  I (Marshall Hampton) am planning on bringing this up to 100% coverage soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6529\n\n",
    "created_at": "2009-07-14T04:52:36Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "adding doctests to arith.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6529",
    "user": "mhampton"
}
```
Assignee: somebody

arith.py currently has quite a few doctests missing.  I (Marshall Hampton) am planning on bringing this up to 100% coverage soon.

Issue created by migration from https://trac.sagemath.org/ticket/6529





---

archive/issue_comments_053228.json:
```json
{
    "body": "Brings arith.py coverage to 100%; includes functions from #6509",
    "created_at": "2009-07-14T19:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53228",
    "user": "mhampton"
}
```

Brings arith.py coverage to 100%; includes functions from #6509



---

archive/issue_comments_053229.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-14T19:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53229",
    "user": "mhampton"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_053230.json:
```json
{
    "body": "Attachment [trac_6529_arith_doctests.patch](tarball://root/attachments/some-uuid/ticket6529/trac_6529_arith_doctests.patch) by mhampton created at 2009-07-14 19:07:33\n\nAttached patch has functions from ticket #6509 in it as well.  \n\nI deleted the optional argument \"k=1\" from Euler_Phi, since it didn't seem to be there for any reason.",
    "created_at": "2009-07-14T19:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53230",
    "user": "mhampton"
}
```

Attachment [trac_6529_arith_doctests.patch](tarball://root/attachments/some-uuid/ticket6529/trac_6529_arith_doctests.patch) by mhampton created at 2009-07-14 19:07:33

Attached patch has functions from ticket #6509 in it as well.  

I deleted the optional argument "k=1" from Euler_Phi, since it didn't seem to be there for any reason.



---

archive/issue_comments_053231.json:
```json
{
    "body": "Attachment [trac_6529_reviewer.patch](tarball://root/attachments/some-uuid/ticket6529/trac_6529_reviewer.patch) by davidloeffler created at 2009-07-16 16:55:27",
    "created_at": "2009-07-16T16:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53231",
    "user": "davidloeffler"
}
```

Attachment [trac_6529_reviewer.patch](tarball://root/attachments/some-uuid/ticket6529/trac_6529_reviewer.patch) by davidloeffler created at 2009-07-16 16:55:27



---

archive/issue_comments_053232.json:
```json
{
    "body": "Good work: patch applies fine, and all doctests pass. But I noticed that several docstrings are mis-formatted, including the one for the new four_squares function. Then I had an attack of enthusiasm and decided to clean all that up. Hence the second patch above.\n\nI'm happy with mhampton's changes; so if mhampton (or anyone someone else) could take a quick look at the second patch, then we can call this a positive review.\n\nDavid",
    "created_at": "2009-07-16T17:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53232",
    "user": "davidloeffler"
}
```

Good work: patch applies fine, and all doctests pass. But I noticed that several docstrings are mis-formatted, including the one for the new four_squares function. Then I had an attack of enthusiasm and decided to clean all that up. Hence the second patch above.

I'm happy with mhampton's changes; so if mhampton (or anyone someone else) could take a quick look at the second patch, then we can call this a positive review.

David



---

archive/issue_comments_053233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T17:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53233",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053234.json:
```json
{
    "body": "Thanks David, that was a lot of cleanup work.",
    "created_at": "2009-07-19T13:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6529#issuecomment-53234",
    "user": "mhampton"
}
```

Thanks David, that was a lot of cleanup work.
