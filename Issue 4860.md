# Issue 4860: upgrade networkx to 0.99 upstream release

archive/issues_004860.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason\n\nSee http://networkx.lanl.gov/reference/news.html\n\nIt seems that this could still come in handy since we will need it for Python 2.6 support for example. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4860\n\n",
    "created_at": "2008-12-23T21:23:00Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "upgrade networkx to 0.99 upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4860",
    "user": "mabshoff"
}
```
Assignee: rlm

CC:  jason

See http://networkx.lanl.gov/reference/news.html

It seems that this could still come in handy since we will need it for Python 2.6 support for example. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4860





---

archive/issue_comments_036836.json:
```json
{
    "body": "Proposed upgrade package found here:\n\nhttp://8tb.us/home/rlmill/networkx-0.99.spkg\n\nPassed long tests in `sage.graphs`, haven't yet tested elsewhere. Someone should check this out, because the pkg doubled in size (although this is 0.36 --> 0.99)",
    "created_at": "2008-12-23T21:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36836",
    "user": "rlm"
}
```

Proposed upgrade package found here:

http://8tb.us/home/rlmill/networkx-0.99.spkg

Passed long tests in `sage.graphs`, haven't yet tested elsewhere. Someone should check this out, because the pkg doubled in size (although this is 0.36 --> 0.99)



---

archive/issue_comments_036837.json:
```json
{
    "body": "From http://groups.google.com/group/networkx-discuss/browse_thread/thread/28e898e144a5e282\n\nLooks like we need to wait for Scipy 0.7:\n\n```\n> > Thanks Cyril.  It looks like networkx-0.99 currently depends on \n> > python-scipy >= 0.7.0 (just out in beta).  I'll see if I can make it \n> > work correctly with 0.6.0. \n> Note that it's not really required on my end, I thought I would report \n> it in case that could be useful. I can live (and the package in \n> experimental too) with a failure in the test suite. Don't bother too \n> much. ;-) \n\n\nI took a look and it looks like the SciPy sparse matrix handling \nhas changed quite a bit between 0.6.0 and 0.7.0.  So I'll leave \nit as is and require 0.7.0 for that (small,optional) part of networkx. \nAric \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T22:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36837",
    "user": "mabshoff"
}
```

From http://groups.google.com/group/networkx-discuss/browse_thread/thread/28e898e144a5e282

Looks like we need to wait for Scipy 0.7:

```
> > Thanks Cyril.  It looks like networkx-0.99 currently depends on 
> > python-scipy >= 0.7.0 (just out in beta).  I'll see if I can make it 
> > work correctly with 0.6.0. 
> Note that it's not really required on my end, I thought I would report 
> it in case that could be useful. I can live (and the package in 
> experimental too) with a failure in the test suite. Don't bother too 
> much. ;-) 


I took a look and it looks like the SciPy sparse matrix handling 
has changed quite a bit between 0.6.0 and 0.7.0.  So I'll leave 
it as is and require 0.7.0 for that (small,optional) part of networkx. 
Aric 
```


Cheers,

Michael



---

archive/issue_comments_036838.json:
```json
{
    "body": "AFAIK nothing we do in Sage depends on that (small,optional) part of networkx that requires up-to-date scipy.",
    "created_at": "2008-12-23T23:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36838",
    "user": "rlm"
}
```

AFAIK nothing we do in Sage depends on that (small,optional) part of networkx that requires up-to-date scipy.



---

archive/issue_comments_036839.json:
```json
{
    "body": "Changing keywords from \"\" to \"networkx-0.99\".",
    "created_at": "2009-01-28T23:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36839",
    "user": "mvngu"
}
```

Changing keywords from "" to "networkx-0.99".



---

archive/issue_comments_036840.json:
```json
{
    "body": "On i686 Debian 5.0 Lenny (testing) with kernel 2.6.24-1-686, and Sage 3.2.3, I downloaded the package at \n\n\n\n[http://8tb.us/home/rlmill/networkx-0.99.spkg](http://8tb.us/home/rlmill/networkx-0.99.spkg)\n\n\n\nto my machine and installed it with\n\n```\nsage -i networkx-0.99.spkg\n```\n\nand ran tests with\n\n```\nsage -t -long /path/to/SAGE_ROOT/devel/sage-main/sage/graphs\n```\n\nAll tests passed.",
    "created_at": "2009-01-28T23:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36840",
    "user": "mvngu"
}
```

On i686 Debian 5.0 Lenny (testing) with kernel 2.6.24-1-686, and Sage 3.2.3, I downloaded the package at 



[http://8tb.us/home/rlmill/networkx-0.99.spkg](http://8tb.us/home/rlmill/networkx-0.99.spkg)



to my machine and installed it with

```
sage -i networkx-0.99.spkg
```

and ran tests with

```
sage -t -long /path/to/SAGE_ROOT/devel/sage-main/sage/graphs
```

All tests passed.



---

archive/issue_comments_036841.json:
```json
{
    "body": "I have fixed various issues in SPKG.txt and spkg-install and put the updates spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/networkx-0.99.p0.spkg\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T06:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36841",
    "user": "mabshoff"
}
```

I have fixed various issues in SPKG.txt and spkg-install and put the updates spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/networkx-0.99.p0.spkg

Positive review.

Cheers,

Michael



---

archive/issue_comments_036842.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T06:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36842",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_036843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T06:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4860#issuecomment-36843",
    "user": "mabshoff"
}
```

Resolution: fixed
