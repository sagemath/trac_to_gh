# Issue 4540: Symmetrica segfault converting Schur functions to k-Schurs

archive/issues_004540.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: kschur, symmetrica, segfault\n\nExample:\n\n\n```\nsage: ks3 = kSchurFunctions(QQ,3,1)  # k-Schur functions without a 't' variable\nsage: s = SFASchur(base_ring())\nsage: ks3(s([3]))\n\nException exceptions.TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored\nfunction: mult(1) \npython: mult(1): Unknown error 3052408646\n```\n\n\nI don't know if the definition of ks3 above was ever intended to be supported.  I just tried it because I wanted k-Schur functions without a 't' and it seemed the natural thing to do.  Conversions the other way (i.e., s(ks3([3])) ) do seem to work.  And, whether it's intended to be supported or not, segfaults are bad.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4540\n\n",
    "created_at": "2008-11-17T19:01:51Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Symmetrica segfault converting Schur functions to k-Schurs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4540",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: kschur, symmetrica, segfault

Example:


```
sage: ks3 = kSchurFunctions(QQ,3,1)  # k-Schur functions without a 't' variable
sage: s = SFASchur(base_ring())
sage: ks3(s([3]))

Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult(1) 
python: mult(1): Unknown error 3052408646
```


I don't know if the definition of ks3 above was ever intended to be supported.  I just tried it because I wanted k-Schur functions without a 't' and it seemed the natural thing to do.  Conversions the other way (i.e., s(ks3([3])) ) do seem to work.  And, whether it's intended to be supported or not, segfaults are bad.

Issue created by migration from https://trac.sagemath.org/ticket/4540





---

archive/issue_comments_033944.json:
```json
{
    "body": "Attachment [4540.patch](tarball://root/attachments/some-uuid/ticket4540/4540.patch) by @jbandlow created at 2008-11-18 04:03:36",
    "created_at": "2008-11-18T04:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33944",
    "user": "https://github.com/jbandlow"
}
```

Attachment [4540.patch](tarball://root/attachments/some-uuid/ticket4540/4540.patch) by @jbandlow created at 2008-11-18 04:03:36



---

archive/issue_comments_033945.json:
```json
{
    "body": "Segfaults are bad, so make this a blocker.\n\nMike: Can you have a look?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T09:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Segfaults are bad, so make this a blocker.

Mike: Can you have a look?

Cheers,

Michael



---

archive/issue_comments_033946.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-21T09:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_033947.json:
```json
{
    "body": "Good work Jason!",
    "created_at": "2008-11-21T14:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33947",
    "user": "https://github.com/mwhansen"
}
```

Good work Jason!



---

archive/issue_comments_033948.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-21T14:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33948",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033949.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T23:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33949",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_033950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T23:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4540#issuecomment-33950",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
