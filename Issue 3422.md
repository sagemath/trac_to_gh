# Issue 3422: Minor typo in docs for zeta_zeros()

archive/issues_003422.json:
```json
{
    "body": "Assignee: tba\n\nMichael Yurko reported in http://groups.google.com/group/sage-devel/t/9300a4480eafd679\n\n```\nIn the reference manual (13.7 Tables of zeros of the Riemann-Zeta\nfunction) it states that zeta_zeros() gives a list of the \"first 10000\nimaginary parts.\" However, it should say \"first 100000 imaginary\nparts\" (add a zero to read 100,000). Also, it might serve to mention\nthat this is an optional package that doesn't come by default.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3422\n\n",
    "created_at": "2008-06-13T23:40:55Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Minor typo in docs for zeta_zeros()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3422",
    "user": "mabshoff"
}
```
Assignee: tba

Michael Yurko reported in http://groups.google.com/group/sage-devel/t/9300a4480eafd679

```
In the reference manual (13.7 Tables of zeros of the Riemann-Zeta
function) it states that zeta_zeros() gives a list of the "first 10000
imaginary parts." However, it should say "first 100000 imaginary
parts" (add a zero to read 100,000). Also, it might serve to mention
that this is an optional package that doesn't come by default.
```



Issue created by migration from https://trac.sagemath.org/ticket/3422





---

archive/issue_comments_024084.json:
```json
{
    "body": "Changing assignee from tba to jwmerrill.",
    "created_at": "2008-09-14T03:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24084",
    "user": "jwmerrill"
}
```

Changing assignee from tba to jwmerrill.



---

archive/issue_comments_024085.json:
```json
{
    "body": "Attachment [3422.patch](tarball://root/attachments/some-uuid/ticket3422/3422.patch) by jwmerrill created at 2008-09-14 03:08:18\n\nThis patch fixes the doc to reflect that there is info about 100,000 zeros, but I do not understand how to install this optional package, so can't write documentation regarding that.",
    "created_at": "2008-09-14T03:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24085",
    "user": "jwmerrill"
}
```

Attachment [3422.patch](tarball://root/attachments/some-uuid/ticket3422/3422.patch) by jwmerrill created at 2008-09-14 03:08:18

This patch fixes the doc to reflect that there is info about 100,000 zeros, but I do not understand how to install this optional package, so can't write documentation regarding that.



---

archive/issue_comments_024086.json:
```json
{
    "body": "Attachment [3422_2.patch](tarball://root/attachments/some-uuid/ticket3422/3422_2.patch) by jwmerrill created at 2008-09-14 03:52:10\n\nThe second patch adds instructions for installing the optional package necessary to make zeta_zeros() work.  I also changed the unusual seealso section into a REFERENCES: section.  If this is accepted, both patches should be applied.",
    "created_at": "2008-09-14T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24086",
    "user": "jwmerrill"
}
```

Attachment [3422_2.patch](tarball://root/attachments/some-uuid/ticket3422/3422_2.patch) by jwmerrill created at 2008-09-14 03:52:10

The second patch adds instructions for installing the optional package necessary to make zeta_zeros() work.  I also changed the unusual seealso section into a REFERENCES: section.  If this is accepted, both patches should be applied.



---

archive/issue_comments_024087.json:
```json
{
    "body": "Nice work. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24087",
    "user": "mabshoff"
}
```

Nice work. Positive review.

Cheers,

Michael



---

archive/issue_comments_024088.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T11:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24088",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_comments_024089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T11:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3422#issuecomment-24089",
    "user": "mabshoff"
}
```

Resolution: fixed
