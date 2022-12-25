# Issue 7314: Average distance, Wiener Index, Szeged index

archive/issues_007314.json:
```json
{
    "body": "Assignee: @rlmill\n\nHello !!\n\nThis patch defines :\n* The average distance between vertices : Graph.average_distance\n* The Szeged Index of a graph : Graph.szeged_index\n* The Wiener Index of a graph : Graph.wiener_index\n\nEverything this patch adds (except the average distance) is documented in :\nhttp://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TY9-3VVCHY8-9&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=6d22be39b064af51023439c3bb59c459\n\nThis reference is mentioned in the docstrings.\n\nNathann\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7314\n\n",
    "created_at": "2009-10-26T16:09:59Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Average distance, Wiener Index, Szeged index",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7314",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Hello !!

This patch defines :
* The average distance between vertices : Graph.average_distance
* The Szeged Index of a graph : Graph.szeged_index
* The Wiener Index of a graph : Graph.wiener_index

Everything this patch adds (except the average distance) is documented in :
http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TY9-3VVCHY8-9&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=6d22be39b064af51023439c3bb59c459

This reference is mentioned in the docstrings.

Nathann


Issue created by migration from https://trac.sagemath.org/ticket/7314





---

archive/issue_comments_061006.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T16:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61006",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061007.json:
```json
{
    "body": "In the docstrings, you should not put comments on the sage: line like in \n\n\n```\nEXAMPLE:: \n\n    sage: # From [2], cited in [1] \n    sage: g=graphs.PathGraph(10) \n    sage: w=lambda x: (x*(x*x -1)/6) \n    sage: g.wiener_index()==w(10) \n    True \n```\n\n\nInstead, it should be\n\n\n```\nEXAMPLE:\n\nFrom [2], cited in [1]::\n\n    sage: g=graphs.PathGraph(10) \n    sage: w=lambda x: (x*(x*x -1)/6) \n    sage: g.wiener_index()==w(10) \n    True \n```\n\n\nAlso, you should see the way that references are handled elsewhere in the Sage library.",
    "created_at": "2009-10-26T16:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61007",
    "user": "https://github.com/mwhansen"
}
```

In the docstrings, you should not put comments on the sage: line like in 


```
EXAMPLE:: 

    sage: # From [2], cited in [1] 
    sage: g=graphs.PathGraph(10) 
    sage: w=lambda x: (x*(x*x -1)/6) 
    sage: g.wiener_index()==w(10) 
    True 
```


Instead, it should be


```
EXAMPLE:

From [2], cited in [1]::

    sage: g=graphs.PathGraph(10) 
    sage: w=lambda x: (x*(x*x -1)/6) 
    sage: g.wiener_index()==w(10) 
    True 
```


Also, you should see the way that references are handled elsewhere in the Sage library.



---

archive/issue_comments_061008.json:
```json
{
    "body": "I hope you will prefer this one ! I had taken as examples other docstrings which you may find badly formatted... This time, I took as an example Minh's code from Cliques functiosn, knowing that never I witnessed Minh making the slightest error :-)\n\nNathann",
    "created_at": "2009-10-26T19:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61008",
    "user": "https://github.com/nathanncohen"
}
```

I hope you will prefer this one ! I had taken as examples other docstrings which you may find badly formatted... This time, I took as an example Minh's code from Cliques functiosn, knowing that never I witnessed Minh making the slightest error :-)

Nathann



---

archive/issue_comments_061009.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T17:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61009",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061010.json:
```json
{
    "body": "Attachment [trac_7314.patch](tarball://root/attachments/some-uuid/ticket7314/trac_7314.patch) by @rlmill created at 2009-12-15 17:17:02",
    "created_at": "2009-12-15T17:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61010",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7314.patch](tarball://root/attachments/some-uuid/ticket7314/trac_7314.patch) by @rlmill created at 2009-12-15 17:17:02



---

archive/issue_comments_061011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T17:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7314#issuecomment-61011",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007537.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-15T17:29:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7314",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7314#event-7537"
}
```
