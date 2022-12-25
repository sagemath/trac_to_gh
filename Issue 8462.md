# Issue 8462: Numerical noise in /sage/sage/plot/colors.py on Solairs SPARC

archive/issues_008462.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman @robertwb wcauchois\n\nRunning Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. \n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py\", line 660:\n    sage: gold / pi + yellow * e\nExpected:\n    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)\nGot:\n    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)\n**********************************************************************\n```\n\n\nThe test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. \n\nDave \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8462\n\n",
    "created_at": "2010-03-06T22:29:21Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Numerical noise in /sage/sage/plot/colors.py on Solairs SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8462",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @williamstein

CC:  @kcrisman @robertwb wcauchois

Running Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py", line 660:
    sage: gold / pi + yellow * e
Expected:
    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)
Got:
    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)
**********************************************************************
```


The test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. 

Dave 



Issue created by migration from https://trac.sagemath.org/ticket/8462





---

archive/issue_comments_076045.json:
```json
{
    "body": "The Mercurial patch I am about to attach fixes this. Tested on a Sun Blade 1000 with a pair of 900 MYHz UltraSPARC III+ processors. \n\n\n```\ndrkirkby@redstart:~/32/sage-4.3.4.alpha0$ ./sage -t  \"devel/sage/sage/plot/colors.py\"\nsage -t  \"devel/sage/sage/plot/colors.py\"                   \n         [13.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 13.2 seconds\n```\n",
    "created_at": "2010-03-06T22:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76045",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The Mercurial patch I am about to attach fixes this. Tested on a Sun Blade 1000 with a pair of 900 MYHz UltraSPARC III+ processors. 


```
drkirkby@redstart:~/32/sage-4.3.4.alpha0$ ./sage -t  "devel/sage/sage/plot/colors.py"
sage -t  "devel/sage/sage/plot/colors.py"                   
         [13.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 13.2 seconds
```




---

archive/issue_comments_076046.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-06T22:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76046",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076047.json:
```json
{
    "body": "Attachment [numerical-noise-colors.py.patch](tarball://root/attachments/some-uuid/ticket8462/numerical-noise-colors.py.patch) by drkirkby created at 2010-03-06 22:35:36\n\nMercurial patch to fix numerical noise on SPARC processor",
    "created_at": "2010-03-06T22:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76047",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [numerical-noise-colors.py.patch](tarball://root/attachments/some-uuid/ticket8462/numerical-noise-colors.py.patch) by drkirkby created at 2010-03-06 22:35:36

Mercurial patch to fix numerical noise on SPARC processor



---

archive/issue_comments_076048.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-03-06T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76048",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_076049.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76049",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076050.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8462#issuecomment-76050",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008646.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-03-06T23:47:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8462",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8462#event-8646"
}
```
