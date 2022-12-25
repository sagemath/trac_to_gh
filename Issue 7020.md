# Issue 7020: Fix 32-bit versus 64-bit boolean_function issue in crypto

archive/issues_007020.json:
```json
{
    "body": "Assignee: tbd\n\nSee #6870 for some discussion.  A random test behaves differently in 32/64 cases:\n\n```\nsage -t -long devel/sage/sage/crypto/boolean_function.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx\", line 1013:\n    sage: B.nonlinearity()\nExpected:\n    217\nGot:\n    222\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_36\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py\n\t [5.3 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7020\n\n",
    "created_at": "2009-09-27T00:52:13Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Fix 32-bit versus 64-bit boolean_function issue in crypto",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7020",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tbd

See #6870 for some discussion.  A random test behaves differently in 32/64 cases:

```
sage -t -long devel/sage/sage/crypto/boolean_function.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    217
Got:
    222
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py
	 [5.3 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/7020





---

archive/issue_comments_058012.json:
```json
{
    "body": "Either this patch or an identical one but with the other # (217 or 222) in the - line should apply and fix this.  Probably it should be renamed as well!",
    "created_at": "2009-09-27T00:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7020#issuecomment-58012",
    "user": "https://github.com/kcrisman"
}
```

Either this patch or an identical one but with the other # (217 or 222) in the - line should apply and fix this.  Probably it should be renamed as well!



---

archive/issue_comments_058013.json:
```json
{
    "body": "based on Sage 4.1.2.alpha4",
    "created_at": "2009-09-28T03:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7020#issuecomment-58013",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.2.alpha4



---

archive/issue_comments_058014.json:
```json
{
    "body": "Attachment [trac_7020-bitness-issue.patch](tarball://root/attachments/some-uuid/ticket7020/trac_7020-bitness-issue.patch) by mvngu created at 2009-09-28 03:55:17",
    "created_at": "2009-09-28T03:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7020#issuecomment-58014",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7020-bitness-issue.patch](tarball://root/attachments/some-uuid/ticket7020/trac_7020-bitness-issue.patch) by mvngu created at 2009-09-28 03:55:17



---

archive/issue_comments_058015.json:
```json
{
    "body": "Works for me on Fedora 11, 32 bit:\n\n\n\n```\n[jaap@paix sage-4.1.2.alpha4]$ ./sage -t  \"devel/sage/sage/crypto/boolean_function.pyx\"\nsage -t  \"devel/sage/sage/crypto/boolean_function.pyx\"      \n\t [8.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 8.9 seconds\n\n```\n",
    "created_at": "2009-09-28T09:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7020#issuecomment-58015",
    "user": "https://github.com/jaapspies"
}
```

Works for me on Fedora 11, 32 bit:



```
[jaap@paix sage-4.1.2.alpha4]$ ./sage -t  "devel/sage/sage/crypto/boolean_function.pyx"
sage -t  "devel/sage/sage/crypto/boolean_function.pyx"      
	 [8.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.9 seconds

```




---

archive/issue_events_007242.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-29T11:37:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7020#event-7242"
}
```



---

archive/issue_comments_058016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T11:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7020#issuecomment-58016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
