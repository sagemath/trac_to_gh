# Issue 3059: notebook -- rewrite notebook(...) function to *not* use SSL by default

archive/issues_003059.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3059\n\n",
    "created_at": "2008-04-30T00:13:03Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "notebook -- rewrite notebook(...) function to *not* use SSL by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3059",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/3059





---

archive/issue_comments_021119.json:
```json
{
    "body": "Attachment [extcode-3059.patch](tarball://root/attachments/some-uuid/ticket3059/extcode-3059.patch) by was created at 2008-04-30 00:36:39",
    "created_at": "2008-04-30T00:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21119",
    "user": "was"
}
```

Attachment [extcode-3059.patch](tarball://root/attachments/some-uuid/ticket3059/extcode-3059.patch) by was created at 2008-04-30 00:36:39



---

archive/issue_comments_021120.json:
```json
{
    "body": "Attachment [sage-3059.patch](tarball://root/attachments/some-uuid/ticket3059/sage-3059.patch) by was created at 2008-04-30 00:37:43\n\nThe two patches turn ssl off by default, make logins required by default no matter what, print a big warning in a worrisome case, use a token to automate the first login, and fill in the admin username if it is the only possible username.",
    "created_at": "2008-04-30T00:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21120",
    "user": "was"
}
```

Attachment [sage-3059.patch](tarball://root/attachments/some-uuid/ticket3059/sage-3059.patch) by was created at 2008-04-30 00:37:43

The two patches turn ssl off by default, make logins required by default no matter what, print a big warning in a worrisome case, use a token to automate the first login, and fill in the admin username if it is the only possible username.



---

archive/issue_comments_021121.json:
```json
{
    "body": "This is mostly to accommodate Firefox 3, right? If two users are running on the same system is it possible to sniff localhost traffic (short of being root, in which case the notebook could be compromised anyways...)? If not, then it looks good (though I have yet to try it out) and if so, is this a risk we're willing to take? (Probably so.)",
    "created_at": "2008-04-30T00:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21121",
    "user": "robertwb"
}
```

This is mostly to accommodate Firefox 3, right? If two users are running on the same system is it possible to sniff localhost traffic (short of being root, in which case the notebook could be compromised anyways...)? If not, then it looks good (though I have yet to try it out) and if so, is this a risk we're willing to take? (Probably so.)



---

archive/issue_comments_021122.json:
```json
{
    "body": "AFAIK, it is impossible to sniff localhost without being root.  This is not necessarily the case in Windows.  We should get a security expert to weigh in on this issue.\n\nFirst patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage.  Specifically, if the second patch is not given a positive review soon, please split the first into a new ticket to avoid bitrot.\n\nSecond patch appears fine (modulo the security discussion) but I haven't tested it and won't until  Wednesday or later.",
    "created_at": "2008-04-30T01:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21122",
    "user": "boothby"
}
```

AFAIK, it is impossible to sniff localhost without being root.  This is not necessarily the case in Windows.  We should get a security expert to weigh in on this issue.

First patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage.  Specifically, if the second patch is not given a positive review soon, please split the first into a new ticket to avoid bitrot.

Second patch appears fine (modulo the security discussion) but I haven't tested it and won't until  Wednesday or later.



---

archive/issue_comments_021123.json:
```json
{
    "body": "Attachment [sage-3059-doc.patch](tarball://root/attachments/some-uuid/ticket3059/sage-3059-doc.patch) by TimothyClemans created at 2008-04-30 04:13:32",
    "created_at": "2008-04-30T04:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21123",
    "user": "TimothyClemans"
}
```

Attachment [sage-3059-doc.patch](tarball://root/attachments/some-uuid/ticket3059/sage-3059-doc.patch) by TimothyClemans created at 2008-04-30 04:13:32



---

archive/issue_comments_021124.json:
```json
{
    "body": "Comments:\n\n1. In UNIX (linux and OS X) one definitely cannot sniff localhost unless one's system is purposely seriously misconfigured.\n\n2. Windows is not relevant at this point, since there is no native notebook server under windows.  \n\n3. Boothby's comment that \"First patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage.\" isn't right.  That patch (1) makes the case change, and (2) adds a template parameter.  Both patches need to be applied.\n\n4. Timothy Clemans did thoroughly test out the patch and found no bugs particularly caused by the patch, according to his remarks on irc.",
    "created_at": "2008-04-30T04:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21124",
    "user": "was"
}
```

Comments:

1. In UNIX (linux and OS X) one definitely cannot sniff localhost unless one's system is purposely seriously misconfigured.

2. Windows is not relevant at this point, since there is no native notebook server under windows.  

3. Boothby's comment that "First patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage." isn't right.  That patch (1) makes the case change, and (2) adds a template parameter.  Both patches need to be applied.

4. Timothy Clemans did thoroughly test out the patch and found no bugs particularly caused by the patch, according to his remarks on irc.



---

archive/issue_comments_021125.json:
```json
{
    "body": "I give sage-3059-doc.patch (the patch added by Timothy) a possitive review.",
    "created_at": "2008-04-30T04:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21125",
    "user": "was"
}
```

I give sage-3059-doc.patch (the patch added by Timothy) a possitive review.



---

archive/issue_comments_021126.json:
```json
{
    "body": "Positive review. Tested on sage.math. I doctested twist.py and no errors. I tried various combinations including \"secure=True, require_login=False\".",
    "created_at": "2008-04-30T04:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21126",
    "user": "TimothyClemans"
}
```

Positive review. Tested on sage.math. I doctested twist.py and no errors. I tried various combinations including "secure=True, require_login=False".



---

archive/issue_comments_021127.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.1.alpha1",
    "created_at": "2008-04-30T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21127",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.0.1.alpha1



---

archive/issue_comments_021128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-30T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3059#issuecomment-21128",
    "user": "mabshoff"
}
```

Resolution: fixed
