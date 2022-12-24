# Issue 7055: Fix 32-bit versus 64-bit in pbori.pyx doctest

archive/issues_007055.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nWith Sage-4.1.2.alpha4 on a 32-bit machine:\n\n```\nsage -t -long \"devel/sage/sage/rings/polynomial/pbori.pyx\"  \n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx\", line 3940:\n    sage: x.stable_hash()\nExpected:\n    173100285919\nGot:\n    -845955105\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx\", line 4849:\n    sage: s.stable_hash()\nExpected:\n    173100285919\nGot:\n    -845955105\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx\", line 1976:\n    sage: m.stable_hash()\nExpected:\n    173100285919\nGot:\n    -845955105\n**********************************************************************\n3 items had failures:\n   1 of   4 in __main__.example_128\n   1 of   5 in __main__.example_165\n   1 of   5 in __main__.example_48\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_pbori.py\n         [9.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/rings/polynomial/pbori.pyx\"\nTotal time for all tests: 9.4 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7055\n\n",
    "created_at": "2009-09-28T18:59:24Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Fix 32-bit versus 64-bit in pbori.pyx doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7055",
    "user": "GeorgSWeber"
}
```
Assignee: GeorgSWeber

With Sage-4.1.2.alpha4 on a 32-bit machine:

```
sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"  
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 3940:
    sage: x.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 4849:
    sage: s.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
File "/Users/Shared/sage/sage-4.1.2.alpha4/devel/sage/sage/rings/polynomial/pbori.pyx", line 1976:
    sage: m.stable_hash()
Expected:
    173100285919
Got:
    -845955105
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_128
   1 of   5 in __main__.example_165
   1 of   5 in __main__.example_48
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_pbori.py
         [9.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"
Total time for all tests: 9.4 seconds
```


Issue created by migration from https://trac.sagemath.org/ticket/7055





---

archive/issue_comments_058398.json:
```json
{
    "body": "Attachment [trac_7055-bitness-issue.patch](tarball://root/attachments/some-uuid/ticket7055/trac_7055-bitness-issue.patch) by GeorgSWeber created at 2009-09-28 19:02:38\n\ntested against 4.1.2.alpha4",
    "created_at": "2009-09-28T19:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7055#issuecomment-58398",
    "user": "GeorgSWeber"
}
```

Attachment [trac_7055-bitness-issue.patch](tarball://root/attachments/some-uuid/ticket7055/trac_7055-bitness-issue.patch) by GeorgSWeber created at 2009-09-28 19:02:38

tested against 4.1.2.alpha4



---

archive/issue_comments_058399.json:
```json
{
    "body": "OK for me in Fedora 11, 32 bit\n\n\n\n```\n./sage -t  \"devel/sage/sage/rings/polynomial/pbori.pyx\"\nsage -t  \"devel/sage/sage/rings/polynomial/pbori.pyx\"       \n\t [15.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 15.3 seconds\n[jaap@paix sage-4.1.2.alpha4]$ \n\n```\n",
    "created_at": "2009-09-28T19:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7055#issuecomment-58399",
    "user": "@jaapspies"
}
```

OK for me in Fedora 11, 32 bit



```
./sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"
sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"       
	 [15.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.3 seconds
[jaap@paix sage-4.1.2.alpha4]$ 

```




---

archive/issue_comments_058400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T11:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7055#issuecomment-58400",
    "user": "mvngu"
}
```

Resolution: fixed
