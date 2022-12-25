# Issue 3850: Sage 3.1.alpha2: matrix_space.py doctest failure (OSX only)

archive/issues_003850.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n********************************************************************* \nFile \"/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py\", \nline 543: \n    sage: l.index(A) \nException raised: \n    Traceback (most recent call last): \n      File \"/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ \npython2.5/doctest.py\", line 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_12[7]>\", line 1, in <module> \n        l.index(A)###line 543: \n    sage: l.index(A) \n    SystemError: error return without exception set \n********************************************************************** \nFile \"/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py\", \nline 545: \n    sage: l.index(B) \nException raised: \n    Traceback (most recent call last): \n      File \"/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ \npython2.5/doctest.py\", line 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_12[8]>\", line 1, in <module> \n        l.index(B)###line 545: \n    sage: l.index(B) \n    SystemError: error return without exception set \n********************************************************************** \nFile \"/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py\", \nline 551: \n    sage: l.index(A) \nException raised: \n    Traceback (most recent call last): \n      File \"/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ \npython2.5/doctest.py\", line 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_12[9]>\", line 1, in <module> \n        l.index(A)###line 551: \n    sage: l.index(A) \n    SystemError: error return without exception set \n********************************************************************** \nFile \"/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py\", \nline 553: \n    sage: l.index(C) \nException raised: \n    Traceback (most recent call last): \n      File \"/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ \npython2.5/doctest.py\", line 1228, in __run \n        compileflags, 1) in test.globs \n      File \"<doctest __main__.example_12[10]>\", line 1, in <module> \n        l.index(C)###line 553: \n    sage: l.index(C) \n    SystemError: error return without exception set \n********************************************************************** \n1 items had failures: \n   4 of  35 in __main__.example_12 \n***Test Failed*** 4 failures. \nFor whitespace errors, see the file /Users/palmieri/Desktop/ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3850\n\n",
    "created_at": "2008-08-14T16:19:07Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Sage 3.1.alpha2: matrix_space.py doctest failure (OSX only)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
********************************************************************* 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 543: 
    sage: l.index(A) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[7]>", line 1, in <module> 
        l.index(A)###line 543: 
    sage: l.index(A) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 545: 
    sage: l.index(B) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[8]>", line 1, in <module> 
        l.index(B)###line 545: 
    sage: l.index(B) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 551: 
    sage: l.index(A) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[9]>", line 1, in <module> 
        l.index(A)###line 551: 
    sage: l.index(A) 
    SystemError: error return without exception set 
********************************************************************** 
File "/Users/palmieri/Desktop/sage-3.1.alpha2/tmp/matrix_space.py", 
line 553: 
    sage: l.index(C) 
Exception raised: 
    Traceback (most recent call last): 
      File "/Users/palmieri/Desktop/sage-3.1.alpha2/local/lib/ 
python2.5/doctest.py", line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[10]>", line 1, in <module> 
        l.index(C)###line 553: 
    sage: l.index(C) 
    SystemError: error return without exception set 
********************************************************************** 
1 items had failures: 
   4 of  35 in __main__.example_12 
***Test Failed*** 4 failures. 
For whitespace errors, see the file /Users/palmieri/Desktop/ 
```


Issue created by migration from https://trac.sagemath.org/ticket/3850





---

archive/issue_comments_027329.json:
```json
{
    "body": "From the OSX 10.5 man page:\n\n```\nRETURN VALUES\n     The memcmp() function returns zero if the two strings are identical, \notherwise returns the difference between the first two differing bytes \n(treated as unsigned char values, so that `\\200' is greater than `\\0', \nfor example).  Zero-length strings are always identical.\n```\n",
    "created_at": "2008-08-15T08:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3850#issuecomment-27329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

From the OSX 10.5 man page:

```
RETURN VALUES
     The memcmp() function returns zero if the two strings are identical, 
otherwise returns the difference between the first two differing bytes 
(treated as unsigned char values, so that `\200' is greater than `\0', 
for example).  Zero-length strings are always identical.
```




---

archive/issue_comments_027330.json:
```json
{
    "body": "Attachment [sage-3850.patch](tarball://root/attachments/some-uuid/ticket3850/sage-3850.patch) by @williamstein created at 2008-08-15 08:51:04\n\nRobert Bradshaw's #3788 caused this (and another failure).    The attached ticket fixes it.",
    "created_at": "2008-08-15T08:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3850#issuecomment-27330",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3850.patch](tarball://root/attachments/some-uuid/ticket3850/sage-3850.patch) by @williamstein created at 2008-08-15 08:51:04

Robert Bradshaw's #3788 caused this (and another failure).    The attached ticket fixes it.



---

archive/issue_comments_027331.json:
```json
{
    "body": "This fixes the problem and also passes doctests. It might be slightly slower, but correctness ought to compensate for that.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T09:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3850#issuecomment-27331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This fixes the problem and also passes doctests. It might be slightly slower, but correctness ought to compensate for that.

Cheers,

Michael



---

archive/issue_comments_027332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T09:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3850#issuecomment-27332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004073.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-15T09:38:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3850#event-4073"
}
```



---

archive/issue_comments_027333.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T09:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3850#issuecomment-27333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0
