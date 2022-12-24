# Issue 4386: Sage 3.1.4: optional doctest failure in sage/rings/number_field/totallyreal_phc.py

archive/issues_004386.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  craigcitro jvoight\n\n\n```\nsage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 86:\n    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 86:\n    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional\n    NameError: name '__lagrange_bounds_phc' is not defined\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 89:\n    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 89:\n    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional\n    NameError: name '__lagrange_bounds_phc' is not defined\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 92:\n    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[4]>\", line 1, in <module>\n        __lagrange_bounds_phc(Integer(3),Integer(1),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 92:\n    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional\n    NameError: name '__lagrange_bounds_phc' is not defined\n**********************************************************************\n1 items had failures:\n   3 of   5 in __main__.example_2\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py\n\t [2.0 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4386\n\n",
    "created_at": "2008-10-30T04:19:15Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.1.4: optional doctest failure in sage/rings/number_field/totallyreal_phc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4386",
    "user": "mabshoff"
}
```
Assignee: mhampton

CC:  craigcitro jvoight


```
sage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 86:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 86:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 89:
    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 89:
    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 92:
    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(1),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 92:
    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
1 items had failures:
   3 of   5 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py
	 [2.0 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/4386





---

archive/issue_comments_032283.json:
```json
{
    "body": "Craig's patch exposes the next problem:\n\n```\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 87:\n    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 87:\n    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal_phc.py\", line 118, in __lagrange_bounds_phc\n        for P in sage.combinat.combinat.partitions_list(n-1,m-1):\n    AttributeError: 'module' object has no attribute 'partitions_list'\n**********************************************************************\n```\n\nmhansen pointed out in IRC:\n\n```\n[9:13pm] mhansen: partitions_list should be deprecated.  Partitions(n).list() \nshould be used if you want a list otherwise Partitions(n) provides an __iter__\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T05:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32283",
    "user": "mabshoff"
}
```

Craig's patch exposes the next problem:

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 87:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 87:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal_phc.py", line 118, in __lagrange_bounds_phc
        for P in sage.combinat.combinat.partitions_list(n-1,m-1):
    AttributeError: 'module' object has no attribute 'partitions_list'
**********************************************************************
```

mhansen pointed out in IRC:

```
[9:13pm] mhansen: partitions_list should be deprecated.  Partitions(n).list() 
should be used if you want a list otherwise Partitions(n) provides an __iter__
```


Cheers,

Michael



---

archive/issue_comments_032284.json:
```json
{
    "body": "Attachment [trac-4386.patch](tarball://root/attachments/some-uuid/ticket4386/trac-4386.patch) by craigcitro created at 2008-10-30 07:24:43",
    "created_at": "2008-10-30T07:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32284",
    "user": "craigcitro"
}
```

Attachment [trac-4386.patch](tarball://root/attachments/some-uuid/ticket4386/trac-4386.patch) by craigcitro created at 2008-10-30 07:24:43



---

archive/issue_comments_032285.json:
```json
{
    "body": "Much better patch attached.",
    "created_at": "2008-10-30T07:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32285",
    "user": "craigcitro"
}
```

Much better patch attached.



---

archive/issue_comments_032286.json:
```json
{
    "body": "Changing assignee from mhampton to craigcitro.",
    "created_at": "2008-10-30T07:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32286",
    "user": "craigcitro"
}
```

Changing assignee from mhampton to craigcitro.



---

archive/issue_comments_032287.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-30T07:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32287",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032288.json:
```json
{
    "body": "Better patch, but still some trouble:\n\n```\nsage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 91:\n    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[4]>\", line 1, in <module>\n        x, y = __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)]) # optional###line 91:\n    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional\n    ValueError: need more than 0 values to unpack\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 92:\n    e: x # optional\nExpected:\n    -1.3333333333333299\nGot:\n    x\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py\", line 94:\n    e: y < 0.00000001 # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[6]>\", line 1, in <module>\n        y < RealNumber('0.00000001') # optional###line 94:\n    e: y < 0.00000001 # optional\n    NameError: name 'y' is not defined\n**********************************************************************\n1 items had failures:\n   3 of   8 in __main__.example_2\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py\n\t [2.4 s]\nexit code: 1024\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T07:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32288",
    "user": "mabshoff"
}
```

Better patch, but still some trouble:

```
sage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 91:
    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        x, y = __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)]) # optional###line 91:
    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional
    ValueError: need more than 0 values to unpack
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 92:
    e: x # optional
Expected:
    -1.3333333333333299
Got:
    x
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 94:
    e: y < 0.00000001 # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[6]>", line 1, in <module>
        y < RealNumber('0.00000001') # optional###line 94:
    e: y < 0.00000001 # optional
    NameError: name 'y' is not defined
**********************************************************************
1 items had failures:
   3 of   8 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py
	 [2.4 s]
exit code: 1024
```


Cheers,

Michael



---

archive/issue_comments_032289.json:
```json
{
    "body": "Attachment [trac-4386-pt2.patch](tarball://root/attachments/some-uuid/ticket4386/trac-4386-pt2.patch) by craigcitro created at 2008-10-31 04:49:59",
    "created_at": "2008-10-31T04:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32289",
    "user": "craigcitro"
}
```

Attachment [trac-4386-pt2.patch](tarball://root/attachments/some-uuid/ticket4386/trac-4386-pt2.patch) by craigcitro created at 2008-10-31 04:49:59



---

archive/issue_comments_032290.json:
```json
{
    "body": "Second patch added, which **should** fix the issue.",
    "created_at": "2008-10-31T04:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32290",
    "user": "craigcitro"
}
```

Second patch added, which **should** fix the issue.



---

archive/issue_comments_032291.json:
```json
{
    "body": "Positive review. With both patches applied the issue is resolved:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py\nsage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py\n\t [2.4 s]\n \n----------------------------------------------------------------------\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T05:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32291",
    "user": "mabshoff"
}
```

Positive review. With both patches applied the issue is resolved:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py
sage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py
	 [2.4 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael



---

archive/issue_comments_032292.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha2",
    "created_at": "2008-10-31T05:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32292",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha2



---

archive/issue_comments_032293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T05:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4386#issuecomment-32293",
    "user": "mabshoff"
}
```

Resolution: fixed
