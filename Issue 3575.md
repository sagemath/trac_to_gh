# Issue 3575: [with patch; needs review] delete random crap from the bottom of complex_double.pyx

archive/issues_003575.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3575\n\n",
    "created_at": "2008-07-06T22:04:22Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] delete random crap from the bottom of complex_double.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3575",
    "user": "was"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/3575





---

archive/issue_comments_025252.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-06T22:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3575#issuecomment-25252",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_025253.json:
```json
{
    "body": "In my merge tree somebody else already beat you to it and deleted the random crap:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/devel/sage$ tail -n 10 sage/rings/complex_double.pyx\n        True    \n    \"\"\"\n    return _CDF   \n\nfrom sage.misc.parser import Parser\ncdef cdf_parser = Parser(float, float,  {\"I\" : _CDF.gen(), \"i\" : _CDF.gen()})\n\n\n\n#####\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T01:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3575#issuecomment-25253",
    "user": "mabshoff"
}
```

In my merge tree somebody else already beat you to it and deleted the random crap:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/devel/sage$ tail -n 10 sage/rings/complex_double.pyx
        True    
    """
    return _CDF   

from sage.misc.parser import Parser
cdef cdf_parser = Parser(float, float,  {"I" : _CDF.gen(), "i" : _CDF.gen()})



#####
```


Cheers,

Michael



---

archive/issue_comments_025254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T01:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3575#issuecomment-25254",
    "user": "mabshoff"
}
```

Resolution: fixed
