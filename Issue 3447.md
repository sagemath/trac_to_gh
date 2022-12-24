# Issue 3447: sage -t foo gives wrong path to the file foo in the output

archive/issues_003447.json:
```json
{
    "body": "Assignee: failure\n\nCC:  gfurnish mjo\n\n\n```\nD-69-91-136-212:modular was$ sage -t dims.py \nsage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************\nFile \"/Users/was/s/tmp/dims.py\", line 1564:\n    sage: sturm_bound(Gamma1(13),5)\n```\n\n\nNotice the *tmp* above.  \n\nThis is not trivial to fix.  We need to change this:\n\n```\nD-69-91-136-212:modular was$ sage -t dims.py \nsage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************\nFile \".../devel/sage-main/sage/modular/dims.py\", line 1564:\n    sage: sturm_bound(Gamma1(13),5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3447\n\n",
    "created_at": "2008-06-17T04:46:36Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -t foo gives wrong path to the file foo in the output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3447",
    "user": "was"
}
```
Assignee: failure

CC:  gfurnish mjo


```
D-69-91-136-212:modular was$ sage -t dims.py 
sage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************
File "/Users/was/s/tmp/dims.py", line 1564:
    sage: sturm_bound(Gamma1(13),5)
```


Notice the *tmp* above.  

This is not trivial to fix.  We need to change this:

```
D-69-91-136-212:modular was$ sage -t dims.py 
sage -t  devel/sage-main/sage/modular/dims.py               **********************************************************************
File ".../devel/sage-main/sage/modular/dims.py", line 1564:
    sage: sturm_bound(Gamma1(13),5)
```


Issue created by migration from https://trac.sagemath.org/ticket/3447





---

archive/issue_comments_024315.json:
```json
{
    "body": "Gary, \n\nany idea about this one?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T05:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24315",
    "user": "mabshoff"
}
```

Gary, 

any idea about this one?

Cheers,

Michael



---

archive/issue_comments_024316.json:
```json
{
    "body": "seems to be fixed a long time ago\nright now it works:\n\n\n```\nmd:modular maarten$ sage -t dims.py\n/Users/maarten/Downloads/sage-4.7.2.alpha2\nsage -t  \"devel/sage-main/sage/modular/dims.py\"             \n\t [4.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.9 seconds\n```\n",
    "created_at": "2011-08-24T15:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24316",
    "user": "mderickx"
}
```

seems to be fixed a long time ago
right now it works:


```
md:modular maarten$ sage -t dims.py
/Users/maarten/Downloads/sage-4.7.2.alpha2
sage -t  "devel/sage-main/sage/modular/dims.py"             
	 [4.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.9 seconds
```




---

archive/issue_comments_024317.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-24T15:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24317",
    "user": "mderickx"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024318.json:
```json
{
    "body": "It is fixed. The temp file is still mentioned for failures, but is done so separately \"For whitespace errors...\"\n\n\n```\n$ sage -t dims.py \nsage -t  \"devel/sage-new_maxima/sage/modular/dims.py\"       \n**********************************************************************\nFile \"/home/mjo/src/sage-4.8.alpha2/devel/sage-new_maxima/sage/modular/dims.py\", line 110:\n    sage: sage.modular.dims.CO_delta(1,5,7,eps^3)\nExpected:\n    4\nGot:\n    2\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mjo/.sage//tmp/dims_12113.py\n\t [2.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-new_maxima/sage/modular/dims.py\"\nTotal time for all tests: 2.9 seconds\n```\n",
    "created_at": "2011-11-30T23:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24318",
    "user": "mjo"
}
```

It is fixed. The temp file is still mentioned for failures, but is done so separately "For whitespace errors..."


```
$ sage -t dims.py 
sage -t  "devel/sage-new_maxima/sage/modular/dims.py"       
**********************************************************************
File "/home/mjo/src/sage-4.8.alpha2/devel/sage-new_maxima/sage/modular/dims.py", line 110:
    sage: sage.modular.dims.CO_delta(1,5,7,eps^3)
Expected:
    4
Got:
    2
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mjo/.sage//tmp/dims_12113.py
	 [2.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-new_maxima/sage/modular/dims.py"
Total time for all tests: 2.9 seconds
```




---

archive/issue_comments_024319.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-01T00:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24319",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024320.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-12-09T10:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3447#issuecomment-24320",
    "user": "jdemeyer"
}
```

Resolution: worksforme
