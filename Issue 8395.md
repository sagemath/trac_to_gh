# Issue 8395: degree() reports the degree of a self-loop vertex as contributing 1 to total degree

archive/issues_008395.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout @nathanncohen\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/42110dbb598d11d2):\n\n```\n[mvngu@sage mvngu]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: G = Graph({1:[1]}); G\nLooped graph on 1 vertex\nsage: sum(G.degree())\n1\nsage: G.size()\n0\nsage: G = Graph({1:[1]}, loops=True); G\nLooped graph on 1 vertex\nsage: sum(G.degree())\n1\nsage: G.size()\n0\nsage: G = Graph({1:[1]}, loops=True, multiedges=True); G\nLooped multi-graph on 1 vertex\nsage: sum(G.degree())\n1\nsage: G.size()\n0\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nThe size of G is 1 because there is one edge, i.e. the single\nself-loop. As shown by the above session, Sage reports the size of G\nas 0. I believe this is a bug. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8395\n\n",
    "created_at": "2010-02-28T14:52:11Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "degree() reports the degree of a self-loop vertex as contributing 1 to total degree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8395",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @rlmill

CC:  @jasongrout @nathanncohen

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/42110dbb598d11d2):

```
[mvngu@sage mvngu]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: G = Graph({1:[1]}); G
Looped graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
sage: G = Graph({1:[1]}, loops=True); G
Looped graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
sage: G = Graph({1:[1]}, loops=True, multiedges=True); G
Looped multi-graph on 1 vertex
sage: sum(G.degree())
1
sage: G.size()
0
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
The size of G is 1 because there is one edge, i.e. the single
self-loop. As shown by the above session, Sage reports the size of G
as 0. I believe this is a bug. 
```


Issue created by migration from https://trac.sagemath.org/ticket/8395





---

archive/issue_comments_075093.json:
```json
{
    "body": "Attachment [trac-8395_degree.patch](tarball://root/attachments/some-uuid/ticket8395/trac-8395_degree.patch) by mvngu created at 2010-12-03 13:59:16",
    "created_at": "2010-12-03T13:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac-8395_degree.patch](tarball://root/attachments/some-uuid/ticket8395/trac-8395_degree.patch) by mvngu created at 2010-12-03 13:59:16



---

archive/issue_comments_075094.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-03T13:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075095.json:
```json
{
    "body": "Attachment [trac_8395-part2.patch](tarball://root/attachments/some-uuid/ticket8395/trac_8395-part2.patch) by @rlmill created at 2010-12-03 16:26:30\n\napply after previous patch",
    "created_at": "2010-12-03T16:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75095",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8395-part2.patch](tarball://root/attachments/some-uuid/ticket8395/trac_8395-part2.patch) by @rlmill created at 2010-12-03 16:26:30

apply after previous patch



---

archive/issue_comments_075096.json:
```json
{
    "body": "Minh,\n\nYour patch looks good to me. If you approve of mine, please set this to positive review.\n\nThanks!",
    "created_at": "2010-12-03T16:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75096",
    "user": "https://github.com/rlmill"
}
```

Minh,

Your patch looks good to me. If you approve of mine, please set this to positive review.

Thanks!



---

archive/issue_comments_075097.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-04T02:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75097",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008580.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-01-12T06:31:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8395#event-8580"
}
```



---

archive/issue_comments_075098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8395#issuecomment-75098",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
