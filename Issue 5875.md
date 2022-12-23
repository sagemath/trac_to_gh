# Issue 5875: [with patch, needs review] Support tachyon on FreeBSD

archive/issues_005875.json:
```json
{
    "body": "Assignee: mabshoff\n\ntachyon does include BSD support (though the code advises that it hasn't been tested for a while). Looking though the source code, there's no obvious bitrot so add FreeBSD support to the spkg-install script.\n\nThis patch does not include support for either threaded or 64-bit tachyon. The former shouldn't be too difficult to add and the MacOS-X port implies it is optional. The 64-bit support is solely an optimisation - a test to detect wrap-around of long integers is removed since wrap-around isn't possible with 64-bit longs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5875\n\n",
    "created_at": "2009-04-23T08:50:16Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Support tachyon on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5875",
    "user": "pjeremy"
}
```
Assignee: mabshoff

tachyon does include BSD support (though the code advises that it hasn't been tested for a while). Looking though the source code, there's no obvious bitrot so add FreeBSD support to the spkg-install script.

This patch does not include support for either threaded or 64-bit tachyon. The former shouldn't be too difficult to add and the MacOS-X port implies it is optional. The 64-bit support is solely an optimisation - a test to detect wrap-around of long integers is removed since wrap-around isn't possible with 64-bit longs.

Issue created by migration from https://trac.sagemath.org/ticket/5875





---

archive/issue_comments_046408.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-23T08:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5875#issuecomment-46408",
    "user": "pjeremy"
}
```

Attachment



---

archive/issue_comments_046409.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p9.spkg",
    "created_at": "2009-06-20T02:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5875#issuecomment-46409",
    "user": "mhansen"
}
```

Looks good to me.

The spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p9.spkg



---

archive/issue_comments_046410.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5875#issuecomment-46410",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046411.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T02:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5875#issuecomment-46411",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046412.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T23:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5875#issuecomment-46412",
    "user": "rlm"
}
```

Resolution: fixed
