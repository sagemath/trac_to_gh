# Issue 3288: linear_code -- memory errors in doctests -- need to be marked #long or otherwise fixed

archive/issues_003288.json:
```json
{
    "body": "Assignee: rlm\n\nOn a machine with arch linux and 1GB RAM:\n\n```\nsage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************\nFile \"/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py\", line 402:\n    sage: for B in self_orthogonal_binary_codes(7,3):\n       print B\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[1]>\", line 1, in <module>\n        for B in self_orthogonal_binary_codes(Integer(7),Integer(3)):###line 402:\n    sage: for B in self_orthogonal_binary_codes(7,3):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 477, in self_orthogonal_binary_codes\n        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 486, in self_orthogonal_binary_codes\n        for child in BC.generate_children(BinaryCode(parent), nn, d):\n      File \"binary_code.pyx\", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)\n    MemoryError\n**********************************************************************\nFile \"/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py\", line 415:\n    sage: for B in self_orthogonal_binary_codes(7,3,4):\n       print B; print B.gen_mat()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[2]>\", line 1, in <module>\n        for B in self_orthogonal_binary_codes(Integer(7),Integer(3),Integer(4)):###line 415:\n    sage: for B in self_orthogonal_binary_codes(7,3,4):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 477, in self_orthogonal_binary_codes\n        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 486, in self_orthogonal_binary_codes\n        for child in BC.generate_children(BinaryCode(parent), nn, d):\n      File \"binary_code.pyx\", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)\n    MemoryError\n**********************************************************************\nFile \"/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py\", line 429:\n    sage: for B in self_orthogonal_binary_codes(7,2,4):\n       print B; print B.gen_mat()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        for B in self_orthogonal_binary_codes(Integer(7),Integer(2),Integer(4)):###line 429:\n    sage: for B in self_orthogonal_binary_codes(7,2,4):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 477, in self_orthogonal_binary_codes\n        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 486, in self_orthogonal_binary_codes\n        for child in BC.generate_children(BinaryCode(parent), nn, d):\n      File \"binary_code.pyx\", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)\n    MemoryError\n**********************************************************************\nFile \"/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py\", line 439:\n    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):\n        print B; print B.gen_mat()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[4]>\", line 1, in <module>\n        for B in self_orthogonal_binary_codes(Integer(8), Integer(4), equal=True):###line 439:\n    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 477, in self_orthogonal_binary_codes\n        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):\n      File \"/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 486, in self_orthogonal_binary_codes\n        for child in BC.generate_children(BinaryCode(parent), nn, d):\n      File \"binary_code.pyx\", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)\n    MemoryError\n**********************************************************************\n1 items had failures:\n   4 of   6 in __main__.example_6\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.0.2.rc0/tmp/.doctest_linear_code.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3288\n\n",
    "created_at": "2008-05-23T17:33:26Z",
    "labels": [
        "coding theory",
        "blocker",
        "bug"
    ],
    "title": "linear_code -- memory errors in doctests -- need to be marked #long or otherwise fixed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3288",
    "user": "was"
}
```
Assignee: rlm

On a machine with arch linux and 1GB RAM:

```
sage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 402:
    sage: for B in self_orthogonal_binary_codes(7,3):
       print B
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[1]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(3)):###line 402:
    sage: for B in self_orthogonal_binary_codes(7,3):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 415:
    sage: for B in self_orthogonal_binary_codes(7,3,4):
       print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(3),Integer(4)):###line 415:
    sage: for B in self_orthogonal_binary_codes(7,3,4):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 429:
    sage: for B in self_orthogonal_binary_codes(7,2,4):
       print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(7),Integer(2),Integer(4)):###line 429:
    sage: for B in self_orthogonal_binary_codes(7,2,4):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
File "/home/was/build/sage-3.0.2.rc0/tmp/linear_code.py", line 439:
    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):
        print B; print B.gen_mat()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        for B in self_orthogonal_binary_codes(Integer(8), Integer(4), equal=True):###line 439:
    sage: for B in self_orthogonal_binary_codes(8, 4, equal=True):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 477, in self_orthogonal_binary_codes
        for N in self_orthogonal_binary_codes(n, k, d, M, BC, in_test=in_test):
      File "/home/was/build/sage-3.0.2.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 486, in self_orthogonal_binary_codes
        for child in BC.generate_children(BinaryCode(parent), nn, d):
      File "binary_code.pyx", line 3797, in sage.coding.binary_code.BinaryCodeClassifier.generate_children (sage/coding/binary_code.c:24498)
    MemoryError
**********************************************************************
1 items had failures:
   4 of   6 in __main__.example_6
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.2.rc0/tmp/.doctest_linear_code.py
```


Issue created by migration from https://trac.sagemath.org/ticket/3288





---

archive/issue_comments_022753.json:
```json
{
    "body": "According to top none of the coding style doctests use more than 400MB of RAM on a 64 bit box, so I am assuming this is caused by the issues from #3289 and #3285.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-24T00:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22753",
    "user": "mabshoff"
}
```

According to top none of the coding style doctests use more than 400MB of RAM on a 64 bit box, so I am assuming this is caused by the issues from #3289 and #3285.

Cheers,

Michael



---

archive/issue_comments_022754.json:
```json
{
    "body": "This is not fixed by applying the patch from #3285 - I am valgrinding now.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-24T00:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22754",
    "user": "mabshoff"
}
```

This is not fixed by applying the patch from #3285 - I am valgrinding now.

Cheers,

Michael



---

archive/issue_comments_022755.json:
```json
{
    "body": "Attachment [trac-3288-fix.patch](tarball://root/attachments/some-uuid/ticket3288/trac-3288-fix.patch) by rlm created at 2008-05-24 01:52:42\n\noops!",
    "created_at": "2008-05-24T01:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22755",
    "user": "rlm"
}
```

Attachment [trac-3288-fix.patch](tarball://root/attachments/some-uuid/ticket3288/trac-3288-fix.patch) by rlm created at 2008-05-24 01:52:42

oops!



---

archive/issue_comments_022756.json:
```json
{
    "body": "The patch is the correct fix. On the affected box doctests now pass:\n\n```\nsage -t -long devel/sage/sage/coding/all.py\n         [1.9 s]\nsage -t -long devel/sage/sage/coding/binary_code.pyx\n         [12.9 s]\nsage -t -long devel/sage/sage/coding/code_bounds.py\n         [3.7 s]\nsage -t -long devel/sage/sage/coding/code_constructions.py\n         [7.0 s]\nsage -t -long devel/sage/sage/coding/guava.py\n         [2.9 s]\nsage -t -long devel/sage/sage/coding/linear_code.py\n         [24.5 s]\nsage -t -long devel/sage/sage/coding/sd_codes.py\n         [1.9 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 54.8 seconds\n```\n\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-24T01:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22756",
    "user": "mabshoff"
}
```

The patch is the correct fix. On the affected box doctests now pass:

```
sage -t -long devel/sage/sage/coding/all.py
         [1.9 s]
sage -t -long devel/sage/sage/coding/binary_code.pyx
         [12.9 s]
sage -t -long devel/sage/sage/coding/code_bounds.py
         [3.7 s]
sage -t -long devel/sage/sage/coding/code_constructions.py
         [7.0 s]
sage -t -long devel/sage/sage/coding/guava.py
         [2.9 s]
sage -t -long devel/sage/sage/coding/linear_code.py
         [24.5 s]
sage -t -long devel/sage/sage/coding/sd_codes.py
         [1.9 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 54.8 seconds
```


Positive review.

Cheers,

Michael



---

archive/issue_comments_022757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-24T01:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22757",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022758.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc3",
    "created_at": "2008-05-24T01:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3288#issuecomment-22758",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc3
