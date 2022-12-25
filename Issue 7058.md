# Issue 7058: linbox reports "using frickin' slow GSL C-blas" if building with Sun Studio compiler

archive/issues_007058.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.ne\n\n\n```\nlinbox-1.1.6.p2/spkg-debian\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nCopying commentator patch\nWARNING WARNING\nWARNING WARNING\nWARNING WARNING\nWARNING WARNING\nusing frickin' slow GSL C-blas\nWARNING WARNING\nWARNING WARNING\nWARNING WARNING\nWARNING WARNING\nWARNING WARNING\n*************************************************\n Using LINBOX_BLAS=/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/libgslcblas.so\n*************************************************\n\n```\n\n\nIt should be noted, that linbox later fails to build with Sun Studio, see #7026, as it does not think GMP is installed. That is of course another, and more serious issue. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7058\n\n",
    "created_at": "2009-09-28T21:38:45Z",
    "labels": [
        "component: porting: solaris"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "linbox reports \"using frickin' slow GSL C-blas\" if building with Sun Studio compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7058",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.ne


```
linbox-1.1.6.p2/spkg-debian
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Copying commentator patch
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
using frickin' slow GSL C-blas
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
*************************************************
 Using LINBOX_BLAS=/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/libgslcblas.so
*************************************************

```


It should be noted, that linbox later fails to build with Sun Studio, see #7026, as it does not think GMP is installed. That is of course another, and more serious issue. 

Issue created by migration from https://trac.sagemath.org/ticket/7058





---

archive/issue_comments_058297.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-19T18:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7058#issuecomment-58297",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058298.json:
```json
{
    "body": "Is this still an issue?",
    "created_at": "2015-05-19T18:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7058#issuecomment-58298",
    "user": "https://github.com/a-andre"
}
```

Is this still an issue?



---

archive/issue_comments_058299.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-09-14T09:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7058#issuecomment-58299",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058300.json:
```json
{
    "body": "The recent changes to linbox have made this obsolete.",
    "created_at": "2016-09-14T09:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7058#issuecomment-58300",
    "user": "https://github.com/jdemeyer"
}
```

The recent changes to linbox have made this obsolete.



---

archive/issue_events_007278.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-01-21T18:03:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7058#event-7278"
}
```



---

archive/issue_comments_058301.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-01-21T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7058#issuecomment-58301",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
