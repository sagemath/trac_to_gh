# Issue 6719: Doctest failure with elliptic_eu (incomplete elliptic integral of the second kind) on Solaris.

archive/issues_006719.json:
```json
{
    "body": "Assignee: tbd\n\nThis is a report of a test failure of elliptic_eu (0.5, 0.1), seen on Sage sage-4.1.1.rc0 with updated Maxima (5.19.0) and ecl (9.8.1)\n\nI don't understand the maths of this, and don't even know how to independently verify this. But I'm just reporting it as a test failure. I don't even know if this should be 'algebra'. Please someone set the 'Component' to something else if this is inappropriate. \n\nFile \"/export/home/drkirkby/sage/sage-4.1.1.rc0/devel/sage/sage/functions/special.py\", line 1259:\n    sage: elliptic_eu (0.5, 0.1)\nExpected:\n    0.496054551287\nGot:\n    0.495848403419\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6719\n\n",
    "created_at": "2009-08-09T20:28:46Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Doctest failure with elliptic_eu (incomplete elliptic integral of the second kind) on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6719",
    "user": "drkirkby"
}
```
Assignee: tbd

This is a report of a test failure of elliptic_eu (0.5, 0.1), seen on Sage sage-4.1.1.rc0 with updated Maxima (5.19.0) and ecl (9.8.1)

I don't understand the maths of this, and don't even know how to independently verify this. But I'm just reporting it as a test failure. I don't even know if this should be 'algebra'. Please someone set the 'Component' to something else if this is inappropriate. 

File "/export/home/drkirkby/sage/sage-4.1.1.rc0/devel/sage/sage/functions/special.py", line 1259:
    sage: elliptic_eu (0.5, 0.1)
Expected:
    0.496054551287
Got:
    0.495848403419



Issue created by migration from https://trac.sagemath.org/ticket/6719





---

archive/issue_comments_055139.json:
```json
{
    "body": "Attachment\n\nPatch produced from a modified file in CVS, retrived on August 10th 2009",
    "created_at": "2009-08-11T06:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6719#issuecomment-55139",
    "user": "drkirkby"
}
```

Attachment

Patch produced from a modified file in CVS, retrived on August 10th 2009



---

archive/issue_comments_055140.json:
```json
{
    "body": "Juan Jose Garcia-Ripoll (Juanjo), the main developer of ECL has discovered a bug in ECL 9.8.1. On his advice, I took the CVS on August 10th 2009  and have updated just the one file. \n\n```\necl-9.8.1/src/cmp/sysfun.lsp\n```\n\n\nThis fixes the problem. \n\n\nAs far as I am concerned, this, and trac #6716 (which effected elliptic_e) can now be closed. Doctest\n\n\n```\nsage -t  \"devel/sage/sage/functions/special.py\"\n```\n\n\nnow passes. \n\nI will produce a revised ecl .spkg file, as per trac #6564",
    "created_at": "2009-08-11T07:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6719#issuecomment-55140",
    "user": "drkirkby"
}
```

Juan Jose Garcia-Ripoll (Juanjo), the main developer of ECL has discovered a bug in ECL 9.8.1. On his advice, I took the CVS on August 10th 2009  and have updated just the one file. 

```
ecl-9.8.1/src/cmp/sysfun.lsp
```


This fixes the problem. 


As far as I am concerned, this, and trac #6716 (which effected elliptic_e) can now be closed. Doctest


```
sage -t  "devel/sage/sage/functions/special.py"
```


now passes. 

I will produce a revised ecl .spkg file, as per trac #6564



---

archive/issue_comments_055141.json:
```json
{
    "body": "Closed as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4f409a99e668867) thread.",
    "created_at": "2009-08-11T08:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6719#issuecomment-55141",
    "user": "mvngu"
}
```

Closed as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4f409a99e668867) thread.



---

archive/issue_comments_055142.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-08-11T08:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6719#issuecomment-55142",
    "user": "mvngu"
}
```

Resolution: invalid
