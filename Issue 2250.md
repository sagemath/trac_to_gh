# Issue 2250: sage 2.10.2.rc0: elliptic_curves/monsky_washnitzer.py doctest failure with -long

archive/issues_002250.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py\n**********************************************************************\nFile \"monsky_washnitzer.py\", line 1380:\n    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_32[64]>\", line 1, in <module>\n        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1380:\n    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1439, in matrix_of_frobenius\n        F1_reduced = reduce_all(Q, p, F1_coeffs, offset)\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 913, in reduce_all\n        exact_form = reduce_positive(Q, p, coeffs, offset, exact_form)\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 790, in reduce_positive\n        a[0] = a[0] - Qa*a[2]/3   # subtract d(y^j + 3)\n      File \"element.pyx\", line 1482, in sage.structure.element.RingElement.__div__\n      File \"coerce.pyx\", line 247, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c\n      File \"coerce.pyx\", line 432, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c\n      File \"coerce.pyx\", line 550, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c\n      File \"action.pyx\", line 93, in sage.categories.action.Action.__invert__\n      File \"action.pyx\", line 156, in sage.categories.action.InverseAction.__init__\n    TypeError: No inverse defined for Right scalar multiplication by Integer Ring on Power Series Ring in t over Ring of integers modulo 14641.\n**********************************************************************\nFile \"monsky_washnitzer.py\", line 1382:\n    sage: B                                                     # long time\nExpected:\n    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]\n    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]\nGot:\n    [ 514  927]\n    [ 702 1036]\n**********************************************************************\nFile \"monsky_washnitzer.py\", line 1392:\n    sage: B.det()                                               # long time\nExpected:\n    11 + 484*t^2 + 451*t^3 + O(t^4)\nGot:\n    209\n**********************************************************************\n1 items had failures:\n   3 of  68 in __main__.example_32\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file .doctest_monsky_washnitzer.py\n         [14.3 s]\nexit code: 256\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2250\n\n",
    "created_at": "2008-02-21T19:30:23Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage 2.10.2.rc0: elliptic_curves/monsky_washnitzer.py doctest failure with -long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

```
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
**********************************************************************
File "monsky_washnitzer.py", line 1380:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[64]>", line 1, in <module>
        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1380:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1439, in matrix_of_frobenius
        F1_reduced = reduce_all(Q, p, F1_coeffs, offset)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 913, in reduce_all
        exact_form = reduce_positive(Q, p, coeffs, offset, exact_form)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 790, in reduce_positive
        a[0] = a[0] - Qa*a[2]/3   # subtract d(y^j + 3)
      File "element.pyx", line 1482, in sage.structure.element.RingElement.__div__
      File "coerce.pyx", line 247, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
      File "coerce.pyx", line 432, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c
      File "coerce.pyx", line 550, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c
      File "action.pyx", line 93, in sage.categories.action.Action.__invert__
      File "action.pyx", line 156, in sage.categories.action.InverseAction.__init__
    TypeError: No inverse defined for Right scalar multiplication by Integer Ring on Power Series Ring in t over Ring of integers modulo 14641.
**********************************************************************
File "monsky_washnitzer.py", line 1382:
    sage: B                                                     # long time
Expected:
    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]
    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]
Got:
    [ 514  927]
    [ 702 1036]
**********************************************************************
File "monsky_washnitzer.py", line 1392:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    209
**********************************************************************
1 items had failures:
   3 of  68 in __main__.example_32
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_monsky_washnitzer.py
         [14.3 s]
exit code: 256
```

Issue created by migration from https://trac.sagemath.org/ticket/2250





---

archive/issue_comments_014875.json:
```json
{
    "body": "On 2.10.2.alpha0 + #2079 fixes, it passes fine. \n\n```\nRobert-Bradshaws-Laptop:~/sage/current/devel/sage-bugs2 robert$ sage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py \nsage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py\nRaising timeout to 1800 seconds due to '-long' option\n\n         [28.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 28.5 seconds\n```",
    "created_at": "2008-02-21T20:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14875",
    "user": "https://github.com/robertwb"
}
```

On 2.10.2.alpha0 + #2079 fixes, it passes fine. 

```
Robert-Bradshaws-Laptop:~/sage/current/devel/sage-bugs2 robert$ sage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py 
sage -t -long sage/schemes/elliptic_curves/monsky_washnitzer.py
Raising timeout to 1800 seconds due to '-long' option

         [28.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 28.5 seconds
```



---

archive/issue_comments_014876.json:
```json
{
    "body": "I take that back, I was working in the wrong branch. I do get that error in 2.10.2.alpha0 + #2079 fixes.",
    "created_at": "2008-02-21T20:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14876",
    "user": "https://github.com/robertwb"
}
```

I take that back, I was working in the wrong branch. I do get that error in 2.10.2.alpha0 + #2079 fixes.



---

archive/issue_comments_014877.json:
```json
{
    "body": "Attachment [2250-inverse-action.patch](tarball://root/attachments/some-uuid/ticket2250/2250-inverse-action.patch) by @robertwb created at 2008-02-21 21:24:48\n\nThe above patch fixes this issue, returning None rather than raising an error in this corner case where there is no action (now that division by Z -> multiplication by Q).",
    "created_at": "2008-02-21T21:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14877",
    "user": "https://github.com/robertwb"
}
```

Attachment [2250-inverse-action.patch](tarball://root/attachments/some-uuid/ticket2250/2250-inverse-action.patch) by @robertwb created at 2008-02-21 21:24:48

The above patch fixes this issue, returning None rather than raising an error in this corner case where there is no action (now that division by Z -> multiplication by Q).



---

archive/issue_comments_014878.json:
```json
{
    "body": "This works fine:\n\n```\nwas@sage:~/build/sage-2.10.2.alpha2$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py\nsage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py\nRaising timeout to 1800 seconds due to '-long' option\n\n\t [14.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 14.4 seconds\n\n```",
    "created_at": "2008-02-21T22:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14878",
    "user": "https://github.com/williamstein"
}
```

This works fine:

```
was@sage:~/build/sage-2.10.2.alpha2$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py
Raising timeout to 1800 seconds due to '-long' option

	 [14.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 14.4 seconds

```



---

archive/issue_events_005338.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-21T22:56:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2250#event-5338"
}
```



---

archive/issue_comments_014879.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T22:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2250#issuecomment-14880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
