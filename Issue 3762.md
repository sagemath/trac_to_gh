# Issue 3762: remove quaddouble from sage -- not used, source of pain, mpfr is better

archive/issues_003762.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cwitty\n\nNote -- also close #3079.\n\nI wonder -- should quaddouble should be moved to be an optional spkg?  That will be weird, since the actual support for quaddouble is all over the sage install (in all the coercions code, etc.). \n\nIssue created by migration from https://trac.sagemath.org/ticket/3762\n\n",
    "created_at": "2008-08-02T20:16:11Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "remove quaddouble from sage -- not used, source of pain, mpfr is better",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3762",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  cwitty

Note -- also close #3079.

I wonder -- should quaddouble should be moved to be an optional spkg?  That will be weird, since the actual support for quaddouble is all over the sage install (in all the coercions code, etc.). 

Issue created by migration from https://trac.sagemath.org/ticket/3762





---

archive/issue_comments_026689.json:
```json
{
    "body": "\n```\n\nMy real_roots.pyx uses a couple of functions from quaddouble:\nfpu_fix_start and fpu_fix_end.  (partitions_c.cc also uses these\nfunctions.)  These are found in the quaddouble source in src/fpu.cpp\nand include/fpu.h\n\nProbably the right fix is to copy only those two files into c_lib/.  I\ncan do that, but I'll need some help with configuration.  (The main\nthing is that the files want a preprocessor symbol X86 to be defined\niff we're using an x86-family processor.)\n\nCarl\n```\n",
    "created_at": "2008-08-02T21:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26689",
    "user": "https://github.com/williamstein"
}
```


```

My real_roots.pyx uses a couple of functions from quaddouble:
fpu_fix_start and fpu_fix_end.  (partitions_c.cc also uses these
functions.)  These are found in the quaddouble source in src/fpu.cpp
and include/fpu.h

Probably the right fix is to copy only those two files into c_lib/.  I
can do that, but I'll need some help with configuration.  (The main
thing is that the files want a preprocessor symbol X86 to be defined
iff we're using an x86-family processor.)

Carl
```




---

archive/issue_comments_026690.json:
```json
{
    "body": "Attachment [3762-partitions-tests.patch](tarball://root/attachments/some-uuid/ticket3762/3762-partitions-tests.patch) by @robertwb created at 2009-01-22 09:47:11\n\nadds a test code wrapper for sage",
    "created_at": "2009-01-22T09:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26690",
    "user": "https://github.com/robertwb"
}
```

Attachment [3762-partitions-tests.patch](tarball://root/attachments/some-uuid/ticket3762/3762-partitions-tests.patch) by @robertwb created at 2009-01-22 09:47:11

adds a test code wrapper for sage



---

archive/issue_comments_026691.json:
```json
{
    "body": "Attachment [3762-partitions-qd.patch](tarball://root/attachments/some-uuid/ticket3762/3762-partitions-qd.patch) by @robertwb created at 2009-01-22 09:47:50\n\nmakes qd dependance of partitions optional",
    "created_at": "2009-01-22T09:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26691",
    "user": "https://github.com/robertwb"
}
```

Attachment [3762-partitions-qd.patch](tarball://root/attachments/some-uuid/ticket3762/3762-partitions-qd.patch) by @robertwb created at 2009-01-22 09:47:50

makes qd dependance of partitions optional



---

archive/issue_comments_026692.json:
```json
{
    "body": "I removed the quad-double dependancy from the partitions counting code, but there seems to be a significant speed regression :(.",
    "created_at": "2009-01-22T09:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26692",
    "user": "https://github.com/robertwb"
}
```

I removed the quad-double dependancy from the partitions counting code, but there seems to be a significant speed regression :(.



---

archive/issue_comments_026693.json:
```json
{
    "body": "Attachment [3762-remove-qd.patch](tarball://root/attachments/some-uuid/ticket3762/3762-remove-qd.patch) by @robertwb created at 2009-01-23 02:37:58",
    "created_at": "2009-01-23T02:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26693",
    "user": "https://github.com/robertwb"
}
```

Attachment [3762-remove-qd.patch](tarball://root/attachments/some-uuid/ticket3762/3762-remove-qd.patch) by @robertwb created at 2009-01-23 02:37:58



---

archive/issue_comments_026694.json:
```json
{
    "body": "Attachment [3762-qd-real-roots.patch](tarball://root/attachments/some-uuid/ticket3762/3762-qd-real-roots.patch) by @robertwb created at 2009-01-23 03:44:43\n\nThis removes all sage dependancies on quaddouble, but leaves it in to be deprecated for a while. \n\nSome issues that need to be dealt with are (1) the speed regression in partitions and (2) whether the fix for real_roots would better be extracting fpu_fix from the qd autoconf script. Perhaps if qd is present, we could detect it and compile the above with the qd routines.",
    "created_at": "2009-01-23T03:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26694",
    "user": "https://github.com/robertwb"
}
```

Attachment [3762-qd-real-roots.patch](tarball://root/attachments/some-uuid/ticket3762/3762-qd-real-roots.patch) by @robertwb created at 2009-01-23 03:44:43

This removes all sage dependancies on quaddouble, but leaves it in to be deprecated for a while. 

Some issues that need to be dealt with are (1) the speed regression in partitions and (2) whether the fix for real_roots would better be extracting fpu_fix from the qd autoconf script. Perhaps if qd is present, we could detect it and compile the above with the qd routines.



---

archive/issue_events_008629.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-01-24T02:50:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3762#event-8629"
}
```



---

archive/issue_comments_026695.json:
```json
{
    "body": "1. I applied this to sage-3.3.alpha1 on sage.math and got:\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/rings/complex_field.py # 1 doctests failed\n        sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 164.0 seconds\nwstein@sage:/scratch/wstein/sage-3.3.alpha1$  \n```\n\n\nWe have:\n\n```\nsage -t  devel/sage/sage/structure/sage_object.pyx**********************************************************************\nFile \"/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/structure/sage_object.pyx\", line 682:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data i\nn a more recent format.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data \nin a more recent format.\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled 448 objects.\n    Failed to unpickle 0 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_16\n***Test Failed*** 1 failures.\n\nsage -t  devel/sage/sage/rings/complex_field.py\n**********************************************************************\nFile \"/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/rings/complex_field.py\", line 105:\n    sage: C(RR.log2(), RR.e())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[7]>\", line 1, in <module>\n        C(RR.log2(), RR.e())###line 105:\n    sage: C(RR.log2(), RR.e())\n    AttributeError: 'sage.rings.real_mpfr.RealField' object has no attribute 'e'\n**********************************************************************\n1 items had failures:\n\n```\n\n\n\n\n2. Performance on sage.math:\n\n```\nBEFORE:\nsage: time k = number_of_partitions(10^8)\nCPU times: user 2.48 s, sys: 0.00 s, total: 2.48 s\nWall time: 2.49 s\nsage: time k = number_of_partitions(10^9)\nCPU times: user 22.85 s, sys: 0.00 s, total: 22.85 s\nWall time: 22.85 s\n\n\nAFTER:\nsage: time k = number_of_partitions(10^8)\nCPU times: user 3.29 s, sys: 0.00 s, total: 3.29 s\nWall time: 3.29 s\nsage: time k = number_of_partitions(10^9)\nCPU times: user 35.68 s, sys: 0.00 s, total: 35.68 s\nWall time: 35.71 s\n```\n\n\n3. I read all the code in the patches, and am fine with it. \n\nPositive review if the two doctest issues above are fixed. \n\nNOTE: you should not delete the quaddouble package, since this code still links it in.  That will have to happen in a few months after Deprecation.",
    "created_at": "2009-01-24T02:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26695",
    "user": "https://github.com/williamstein"
}
```

1. I applied this to sage-3.3.alpha1 on sage.math and got:

```
The following tests failed:

        sage -t  devel/sage/sage/rings/complex_field.py # 1 doctests failed
        sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 164.0 seconds
wstein@sage:/scratch/wstein/sage-3.3.alpha1$  
```


We have:

```
sage -t  devel/sage/sage/structure/sage_object.pyx**********************************************************************
File "/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data i
n a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data 
in a more recent format.
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 448 objects.
    Failed to unpickle 0 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_16
***Test Failed*** 1 failures.

sage -t  devel/sage/sage/rings/complex_field.py
**********************************************************************
File "/scratch/wstein/sage-3.3.alpha1/devel/sage-main/sage/rings/complex_field.py", line 105:
    sage: C(RR.log2(), RR.e())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[7]>", line 1, in <module>
        C(RR.log2(), RR.e())###line 105:
    sage: C(RR.log2(), RR.e())
    AttributeError: 'sage.rings.real_mpfr.RealField' object has no attribute 'e'
**********************************************************************
1 items had failures:

```




2. Performance on sage.math:

```
BEFORE:
sage: time k = number_of_partitions(10^8)
CPU times: user 2.48 s, sys: 0.00 s, total: 2.48 s
Wall time: 2.49 s
sage: time k = number_of_partitions(10^9)
CPU times: user 22.85 s, sys: 0.00 s, total: 22.85 s
Wall time: 22.85 s


AFTER:
sage: time k = number_of_partitions(10^8)
CPU times: user 3.29 s, sys: 0.00 s, total: 3.29 s
Wall time: 3.29 s
sage: time k = number_of_partitions(10^9)
CPU times: user 35.68 s, sys: 0.00 s, total: 35.68 s
Wall time: 35.71 s
```


3. I read all the code in the patches, and am fine with it. 

Positive review if the two doctest issues above are fixed. 

NOTE: you should not delete the quaddouble package, since this code still links it in.  That will have to happen in a few months after Deprecation.



---

archive/issue_comments_026696.json:
```json
{
    "body": "Attachment [3762-qd-fixes.patch](tarball://root/attachments/some-uuid/ticket3762/3762-qd-fixes.patch) by @robertwb created at 2009-01-24 03:06:54",
    "created_at": "2009-01-24T03:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26696",
    "user": "https://github.com/robertwb"
}
```

Attachment [3762-qd-fixes.patch](tarball://root/attachments/some-uuid/ticket3762/3762-qd-fixes.patch) by @robertwb created at 2009-01-24 03:06:54



---

archive/issue_comments_026697.json:
```json
{
    "body": "Attach all 5 patches in order. \n\nFollowup for speed regression at #5084 and fpu_fix at #5085.",
    "created_at": "2009-01-24T03:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26697",
    "user": "https://github.com/robertwb"
}
```

Attach all 5 patches in order. 

Followup for speed regression at #5084 and fpu_fix at #5085.



---

archive/issue_events_008630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T13:48:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3762#event-8630"
}
```



---

archive/issue_comments_026698.json:
```json
{
    "body": "Merged all five patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all five patches in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_026699.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3762#issuecomment-26699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
