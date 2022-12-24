# Issue 4600: followup issue on sage -only_optional

archive/issues_004600.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n16:47 < wstein> mabshoff -- there is definitely an \"issue\" with only-optional.\n16:48 < mabshoff> ok\n16:48 < mabshoff> What is it?\n16:48 < wstein> e.g., if you do\n16:48 < wstein> sage: x = 5\n16:48 < wstein> sage: y = x + 2 # optional - gap\n16:48 < wstein> sage: y   # optional -gap\n16:48 < wstein> 7\n16:49 < wstein> Then if you don't include the gap tag it will actually doctest:\n16:49 < wstein> sage: x = 5\n16:49 < wstein> 7\n16:49 < mabshoff> Yes, that is why it should run the block\n16:49 < wstein> which will fail.\n16:49 < mabshoff> ok\n16:49 < wstein> The problem is that it is including output when it shouldn't.\n16:49 < mabshoff> true\n16:49 < wstein> i'll make another ticket.\n16:49 < wstein> I have to fix this to manage working on the magma interface.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4600\n\n",
    "created_at": "2008-11-24T00:52:26Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "followup issue on sage -only_optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4600",
    "user": "was"
}
```
Assignee: mabshoff


```
16:47 < wstein> mabshoff -- there is definitely an "issue" with only-optional.
16:48 < mabshoff> ok
16:48 < mabshoff> What is it?
16:48 < wstein> e.g., if you do
16:48 < wstein> sage: x = 5
16:48 < wstein> sage: y = x + 2 # optional - gap
16:48 < wstein> sage: y   # optional -gap
16:48 < wstein> 7
16:49 < wstein> Then if you don't include the gap tag it will actually doctest:
16:49 < wstein> sage: x = 5
16:49 < wstein> 7
16:49 < mabshoff> Yes, that is why it should run the block
16:49 < wstein> which will fail.
16:49 < mabshoff> ok
16:49 < wstein> The problem is that it is including output when it shouldn't.
16:49 < mabshoff> true
16:49 < wstein> i'll make another ticket.
16:49 < wstein> I have to fix this to manage working on the magma interface.
```


Issue created by migration from https://trac.sagemath.org/ticket/4600





---

archive/issue_comments_034487.json:
```json
{
    "body": "For the referee -- here is a file, and me verifying that the -only_optional and -optional options work correctly.   I don't think this can go into the actual doctest framework for Sage.   However, that isn't really needed since the actual optional doctests in actual code passing is test enough (stuff like below gets or will be used all over in the doctest framework). \n\n```\nwstein@ubuntu:~/sage/tmp$ more a.py\n\"\"\"\nsage: x = 5\nsage: y = x + 2 # optional - gap\nsage: y         # optional - gap\n8\nsage: 2 + 3     # optional - magma\n5\n\"\"\"\nwstein@ubuntu:~/sage/tmp$ sage -t -only_optional=gap a.py\nsage -t -only_optional=gap tmp/a.py                         **********************************************************************\nFile \"/home/wstein/sage/tmp/a.py\", line 4:\n    : y         # optional - gap\nExpected:\n    8\nGot:\n    7\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py\n\t [1.6 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -only_optional=gap tmp/a.py\nTotal time for all tests: 1.6 seconds\nwstein@ubuntu:~/sage/tmp$ sage -t a.py\nsage -t  tmp/a.py                                           \n\t [1.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 1.6 seconds\nwstein@ubuntu:~/sage/tmp$ sage -t -only_optional=magma a.py\nsage -t -only_optional=magma tmp/a.py                       \n\t [1.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 1.6 seconds\nwstein@ubuntu:~/sage/tmp$ sage -t -only_optional=magma,gap a.py\nsage -t -only_optional=magma,gap tmp/a.py                   **********************************************************************\nFile \"/home/wstein/sage/tmp/a.py\", line 4:\n    : y         # optional - gap\nExpected:\n    8\nGot:\n    7\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py\n\t [1.7 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -only_optional=magma,gap tmp/a.py\nTotal time for all tests: 1.7 seconds\nwstein@ubuntu:~/sage/tmp$ sage -t -optional a.py\nsage -t -optional tmp/a.py                                  **********************************************************************\nFile \"/home/wstein/sage/tmp/a.py\", line 4:\n    : y         # optional - gap\nExpected:\n    8\nGot:\n    7\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py\n\t [1.7 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -optional tmp/a.py\nTotal time for all tests: 1.7 seconds\nwstein@ubuntu:~/sage/tmp$ \n```\n",
    "created_at": "2008-11-24T05:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34487",
    "user": "was"
}
```

For the referee -- here is a file, and me verifying that the -only_optional and -optional options work correctly.   I don't think this can go into the actual doctest framework for Sage.   However, that isn't really needed since the actual optional doctests in actual code passing is test enough (stuff like below gets or will be used all over in the doctest framework). 

```
wstein@ubuntu:~/sage/tmp$ more a.py
"""
sage: x = 5
sage: y = x + 2 # optional - gap
sage: y         # optional - gap
8
sage: 2 + 3     # optional - magma
5
"""
wstein@ubuntu:~/sage/tmp$ sage -t -only_optional=gap a.py
sage -t -only_optional=gap tmp/a.py                         **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -only_optional=gap tmp/a.py
Total time for all tests: 1.6 seconds
wstein@ubuntu:~/sage/tmp$ sage -t a.py
sage -t  tmp/a.py                                           
	 [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.6 seconds
wstein@ubuntu:~/sage/tmp$ sage -t -only_optional=magma a.py
sage -t -only_optional=magma tmp/a.py                       
	 [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.6 seconds
wstein@ubuntu:~/sage/tmp$ sage -t -only_optional=magma,gap a.py
sage -t -only_optional=magma,gap tmp/a.py                   **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -only_optional=magma,gap tmp/a.py
Total time for all tests: 1.7 seconds
wstein@ubuntu:~/sage/tmp$ sage -t -optional a.py
sage -t -optional tmp/a.py                                  **********************************************************************
File "/home/wstein/sage/tmp/a.py", line 4:
    : y         # optional - gap
Expected:
    8
Got:
    7
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage/tmp/.doctest_a.py
	 [1.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional tmp/a.py
Total time for all tests: 1.7 seconds
wstein@ubuntu:~/sage/tmp$ 
```




---

archive/issue_comments_034488.json:
```json
{
    "body": "With the attached patch and #4601 applied to sage-3.2.1.alpha0, I get:\n\n```\n$ cd devel/sage/sage/\n$ sage -t -only_optional=magma * \n...\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 207.7 seconds\n```\n",
    "created_at": "2008-11-24T05:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34488",
    "user": "was"
}
```

With the attached patch and #4601 applied to sage-3.2.1.alpha0, I get:

```
$ cd devel/sage/sage/
$ sage -t -only_optional=magma * 
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 207.7 seconds
```




---

archive/issue_comments_034489.json:
```json
{
    "body": "Attachment [scripts-4600.patch](tarball://root/attachments/some-uuid/ticket4600/scripts-4600.patch) by was created at 2008-11-24 05:41:26\n\nthis patch to the scripts repo should fix everything.",
    "created_at": "2008-11-24T05:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34489",
    "user": "was"
}
```

Attachment [scripts-4600.patch](tarball://root/attachments/some-uuid/ticket4600/scripts-4600.patch) by was created at 2008-11-24 05:41:26

this patch to the scripts repo should fix everything.



---

archive/issue_comments_034490.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T21:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34490",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_034491.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-24T22:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34491",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034492.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T22:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4600#issuecomment-34492",
    "user": "mabshoff"
}
```

Resolution: fixed
