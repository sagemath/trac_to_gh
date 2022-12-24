# Issue 5053: If the hostname of the computer has a "-" in it, then no tempfiles will ever be deleted from $DOT_SAGE/temp!

archive/issues_005053.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is because host-name and host_name get confused.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5053\n\n",
    "created_at": "2009-01-22T11:23:30Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "If the hostname of the computer has a \"-\" in it, then no tempfiles will ever be deleted from $DOT_SAGE/temp!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5053",
    "user": "was"
}
```
Assignee: cwitty

This is because host-name and host_name get confused.

Issue created by migration from https://trac.sagemath.org/ticket/5053





---

archive/issue_comments_038499.json:
```json
{
    "body": "Attachment [cleaner.patch](tarball://root/attachments/some-uuid/ticket5053/cleaner.patch) by SimonKing created at 2009-01-24 21:02:45\n\nFor being consistent, replace '-' with '_'. This yields a proper cleaning of temp-files",
    "created_at": "2009-01-24T21:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38499",
    "user": "SimonKing"
}
```

Attachment [cleaner.patch](tarball://root/attachments/some-uuid/ticket5053/cleaner.patch) by SimonKing created at 2009-01-24 21:02:45

For being consistent, replace '-' with '_'. This yields a proper cleaning of temp-files



---

archive/issue_comments_038500.json:
```json
{
    "body": "Apparently, the pid of any sub process is written in a temporary file, in a folder whose name is derived from the hostname.\n\nAnd apparently, when writing these files, any '-' in the hostname will be replaced by '_'. But this replacement is ignored in the `sage-cleaner` script.\n\nSo, the obvious solution is to replace '-' by '_' in the `sage-cleaner`. This is what my patch does.\n\nI tested the following: \n* change the hostname into 'test-test_test'\n* before applying the patch, folders 'test_test_test' (sic!) are created in SAGE_TMP. But the `sage-cleaner` does not clean them\n* after applying the patch, the same folders are created, but this time they are removed after leaving sage.\n* don't forget to change back to your original hostname ;-)",
    "created_at": "2009-01-24T21:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38500",
    "user": "SimonKing"
}
```

Apparently, the pid of any sub process is written in a temporary file, in a folder whose name is derived from the hostname.

And apparently, when writing these files, any '-' in the hostname will be replaced by '_'. But this replacement is ignored in the `sage-cleaner` script.

So, the obvious solution is to replace '-' by '_' in the `sage-cleaner`. This is what my patch does.

I tested the following: 
* change the hostname into 'test-test_test'
* before applying the patch, folders 'test_test_test' (sic!) are created in SAGE_TMP. But the `sage-cleaner` does not clean them
* after applying the patch, the same folders are created, but this time they are removed after leaving sage.
* don't forget to change back to your original hostname ;-)



---

archive/issue_comments_038501.json:
```json
{
    "body": "To be applied after the first patch: Allow hostnames containing '/' and '\\'",
    "created_at": "2009-01-25T07:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38501",
    "user": "SimonKing"
}
```

To be applied after the first patch: Allow hostnames containing '/' and '\'



---

archive/issue_comments_038502.json:
```json
{
    "body": "Attachment [hostnameSCRIPTS.patch](tarball://root/attachments/some-uuid/ticket5053/hostnameSCRIPTS.patch) by SimonKing created at 2009-01-25 08:00:14\n\nTo be applied after the first patch. Allows hostnames that contain '/' or '\\'",
    "created_at": "2009-01-25T08:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38502",
    "user": "SimonKing"
}
```

Attachment [hostnameSCRIPTS.patch](tarball://root/attachments/some-uuid/ticket5053/hostnameSCRIPTS.patch) by SimonKing created at 2009-01-25 08:00:14

To be applied after the first patch. Allows hostnames that contain '/' or '\'



---

archive/issue_comments_038503.json:
```json
{
    "body": "I had a short discussion with William: \n\nA related issue occurs when the hostname contains a slash '/'. Namely, the file name obtained from the hostname would be interpreted as a *path* name, yielding an error! Again, a possible solution is to replace '/' by '_', both in `sage/misc/misc.py` and in the `sage-cleaner`. Since the reason is more or less the same, William suggested to discuss this on the same ticket.\n\nAnd similarly, there may be problems when the hostname contains a backslash '\\'. So, I did the according replacement.\n\nThere is only one situation in which this idea might be a problem:\n* There are two hosts whose names coincide after the replacements\n* These hosts share DOT_SAGE\n* By coincidence, two Sage processes running on these two hosts have the same `pid`.\n\nThis situation would yield a collision, but it seems to be **extremely unlikely**.\n\n**Conclusion**\n There are hostnames containing a slash (I think I have seen one in nature...). So, in the current setting, a bug would occur. My patches (all three together) fix this bug. \n The price to pay is another bug that would occur in an extremely unlikely setting.\n\nI tested my patches with the hostnames `test-test_test`, `test/test` and `test\\test`.",
    "created_at": "2009-01-25T08:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38503",
    "user": "SimonKing"
}
```

I had a short discussion with William: 

A related issue occurs when the hostname contains a slash '/'. Namely, the file name obtained from the hostname would be interpreted as a *path* name, yielding an error! Again, a possible solution is to replace '/' by '_', both in `sage/misc/misc.py` and in the `sage-cleaner`. Since the reason is more or less the same, William suggested to discuss this on the same ticket.

And similarly, there may be problems when the hostname contains a backslash '\'. So, I did the according replacement.

There is only one situation in which this idea might be a problem:
* There are two hosts whose names coincide after the replacements
* These hosts share DOT_SAGE
* By coincidence, two Sage processes running on these two hosts have the same `pid`.

This situation would yield a collision, but it seems to be **extremely unlikely**.

**Conclusion**
 There are hostnames containing a slash (I think I have seen one in nature...). So, in the current setting, a bug would occur. My patches (all three together) fix this bug. 
 The price to pay is another bug that would occur in an extremely unlikely setting.

I tested my patches with the hostnames `test-test_test`, `test/test` and `test\test`.



---

archive/issue_comments_038504.json:
```json
{
    "body": "cwitty pointed out in IRC that `/` and `\\` probably aren't even legal for hostnames, but what the heck: positive review.\n\nI am curious how the problem about those two characters come up.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T03:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38504",
    "user": "mabshoff"
}
```

cwitty pointed out in IRC that `/` and `\` probably aren't even legal for hostnames, but what the heck: positive review.

I am curious how the problem about those two characters come up.

Cheers,

Michael



---

archive/issue_comments_038505.json:
```json
{
    "body": "Merged all three patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T03:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38505",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T03:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5053#issuecomment-38506",
    "user": "mabshoff"
}
```

Resolution: fixed
