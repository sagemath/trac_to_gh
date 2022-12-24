# Issue 4027: Sage 3.1.2.alpha3: matrix_mod2_dense.pyx doctest failure on 32 bits

archive/issues_004027.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nbash-3.2$ ./sage -t devel/sage/sage/matrix/matrix_mod2_dense.pyx\nsage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx       sh: line 1: 19961 Abort trap              /Users/mabshoff/sage-3.1.2.alpha3/local/bin/python /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doct\nest_matrix_mod2_dense.py > /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpqHbQOr 2> /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpBMZa3v\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py\", line 1496:\n    sage: print A.str()\nExpected:\n    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]\n    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\nGot:\n    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]\n    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py\", line 1501:\n    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,2,0,64))\nExpected:\n    13835058055282163713\nGot:\n    1\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py\", line 1505:\n    sage: print A.str()\nExpected:\n    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]\n    [0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]\nGot:\n    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]\n    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]\n    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py\", line 1510:\n    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,3,1,64))\nExpected:\n    13835058055282163713\nGot:\n    1\nFor whitespace errors, see the file /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doctest_matrix_mod2_dense.pym4ri_mm_calloc: calloc returned NULL\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n  [10.2 s]\nexit code: 768\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4027\n\n",
    "created_at": "2008-09-01T00:59:27Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sage 3.1.2.alpha3: matrix_mod2_dense.pyx doctest failure on 32 bits",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4027",
    "user": "mabshoff"
}
```
Assignee: malb


```
bash-3.2$ ./sage -t devel/sage/sage/matrix/matrix_mod2_dense.pyx
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx       sh: line 1: 19961 Abort trap              /Users/mabshoff/sage-3.1.2.alpha3/local/bin/python /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doct
est_matrix_mod2_dense.py > /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpqHbQOr 2> /var/folders/uO/uOBV9ZyXHvWiSlU9K+3AE++++UE/-Tmp-/tmpBMZa3v
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1496:
    sage: print A.str()
Expected:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Got:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1501:
    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,2,0,64))
Expected:
    13835058055282163713
Got:
    1
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1505:
    sage: print A.str()
Expected:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
Got:
    [1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 1510:
    sage: ZZ(sage.matrix.matrix_mod2_dense._read_bits(A,3,1,64))
Expected:
    13835058055282163713
Got:
    1
For whitespace errors, see the file /Users/mabshoff/sage-3.1.2.alpha3/tmp/.doctest_matrix_mod2_dense.pym4ri_mm_calloc: calloc returned NULL

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
  [10.2 s]
exit code: 768
```


Issue created by migration from https://trac.sagemath.org/ticket/4027





---

archive/issue_comments_029039.json:
```json
{
    "body": "Attachment [m4ri_3_1_2_failures.patch](tarball://root/attachments/some-uuid/ticket4027/m4ri_3_1_2_failures.patch) by malb created at 2008-09-01 10:16:45",
    "created_at": "2008-09-01T10:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29039",
    "user": "malb"
}
```

Attachment [m4ri_3_1_2_failures.patch](tarball://root/attachments/some-uuid/ticket4027/m4ri_3_1_2_failures.patch) by malb created at 2008-09-01 10:16:45



---

archive/issue_comments_029040.json:
```json
{
    "body": "The doctest failures can easily be fixed by disabling the respective code (it is just there for testing purposes and that code isn't used by anything in production use yet)\n\nI'll have to come up with a second patch for the CALLOC issue.",
    "created_at": "2008-09-01T10:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29040",
    "user": "malb"
}
```

The doctest failures can easily be fixed by disabling the respective code (it is just there for testing purposes and that code isn't used by anything in production use yet)

I'll have to come up with a second patch for the CALLOC issue.



---

archive/issue_comments_029041.json:
```json
{
    "body": "Patch looks good to me. The calloc issue might or might not be solved by the new upstream spkg. If it is still a problem I will open a new ticket for it.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T10:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29041",
    "user": "mabshoff"
}
```

Patch looks good to me. The calloc issue might or might not be solved by the new upstream spkg. If it is still a problem I will open a new ticket for it.

Cheers,

Michael



---

archive/issue_comments_029042.json:
```json
{
    "body": "A new SPKG is up at:\n\n  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg\n\nWith that SPKG and a touch on `matrix_mod2_dense.pxd` + `sage -b` all tests pass on BSD:\n\n\n```\nSage subshell$ sage -t ~/sage-3.1.2.alpha3/devel/sage/sage/matrix/matrix_mod2_dense.pyx\nsage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx\n         [4.4 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.4 seconds\n```\n",
    "created_at": "2008-09-01T11:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29042",
    "user": "malb"
}
```

A new SPKG is up at:

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080901.spkg

With that SPKG and a touch on `matrix_mod2_dense.pxd` + `sage -b` all tests pass on BSD:


```
Sage subshell$ sage -t ~/sage-3.1.2.alpha3/devel/sage/sage/matrix/matrix_mod2_dense.pyx
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx
         [4.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.4 seconds
```




---

archive/issue_comments_029043.json:
```json
{
    "body": "The spkg has been reviewed at #4024, so I am giving the patch a positive review since it makes the doctest work on OSX 32 bit again.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T12:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29043",
    "user": "mabshoff"
}
```

The spkg has been reviewed at #4024, so I am giving the patch a positive review since it makes the doctest work on OSX 32 bit again.

Cheers,

Michael



---

archive/issue_comments_029044.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T12:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29044",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029045.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T12:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4027#issuecomment-29045",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
