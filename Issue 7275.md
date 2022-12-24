# Issue 7275: [with patch, needs review] numerical noise in tutorial/tour_algebra.rst

archive/issues_007275.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/d2b922ad4ffba33c):\n\n```\nsage -t  \"devel/sage/doc/en/tutorial/tour_algebra.rst\" \n********************************************************************** \nFile \"/home/jaap/downloads/sage-4.2.alpha0/devel/sage/doc/en/tutorial/tour_algeb ra.rst\", line 87: \n     sage: find_root(cos(phi)==sin(phi),0,pi/2) \nExpected: \n     0.78539816339744839 \nGot: \n     0.78539816339744828 \n********************************************************************** \n1 items had failures: \nSame as in alpha0! No ticket yet? \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7275\n\n",
    "created_at": "2009-10-23T21:43:58Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] numerical noise in tutorial/tour_algebra.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7275",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/d2b922ad4ffba33c):

```
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst" 
********************************************************************** 
File "/home/jaap/downloads/sage-4.2.alpha0/devel/sage/doc/en/tutorial/tour_algeb ra.rst", line 87: 
     sage: find_root(cos(phi)==sin(phi),0,pi/2) 
Expected: 
     0.78539816339744839 
Got: 
     0.78539816339744828 
********************************************************************** 
1 items had failures: 
Same as in alpha0! No ticket yet? 
```


Issue created by migration from https://trac.sagemath.org/ticket/7275





---

archive/issue_comments_060541.json:
```json
{
    "body": "Attachment [trac_7275-tutorial-noise.patch](tarball://root/attachments/some-uuid/ticket7275/trac_7275-tutorial-noise.patch) by jhpalmieri created at 2009-10-23 21:44:30",
    "created_at": "2009-10-23T21:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60541",
    "user": "jhpalmieri"
}
```

Attachment [trac_7275-tutorial-noise.patch](tarball://root/attachments/some-uuid/ticket7275/trac_7275-tutorial-noise.patch) by jhpalmieri created at 2009-10-23 21:44:30



---

archive/issue_comments_060542.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60542",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060543.json:
```json
{
    "body": "I could not have done this better!\n\n\n\n```\nsage -t  \"devel/sage/doc/en/tutorial/tour_algebra.rst\"      \n\t [81.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n\n```\n\n\nSo positive review.\n\nJaap",
    "created_at": "2009-10-23T21:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60543",
    "user": "jsp"
}
```

I could not have done this better!



```
sage -t  "devel/sage/doc/en/tutorial/tour_algebra.rst"      
	 [81.2 s]
 
----------------------------------------------------------------------
All tests passed!

```


So positive review.

Jaap



---

archive/issue_comments_060544.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-24T03:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60544",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060545.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-24T03:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60545",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060546.json:
```json
{
    "body": "unique name please",
    "created_at": "2017-07-19T08:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7275#issuecomment-60546",
    "user": "chapoton"
}
```

unique name please
