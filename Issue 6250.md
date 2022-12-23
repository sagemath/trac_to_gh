# Issue 6250: [with patch, needs review] Standardize MatrixGroup_gap: by adding .cardinality, and deprecating __len__

archive/issues_006250.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat wdjoyner@gmail.com\n\nKeywords: cardinality, __len__, order, groups\n\nFollowup on #5308:\n- cardinality now returns the size of the group (was order)\n- order is a backward compatibility alias for cardinality\n- __len__ raises a deprecation error\n\nIssue created by migration from https://trac.sagemath.org/ticket/6250\n\n",
    "created_at": "2009-06-08T23:23:10Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Standardize MatrixGroup_gap: by adding .cardinality, and deprecating __len__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6250",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat wdjoyner@gmail.com

Keywords: cardinality, __len__, order, groups

Followup on #5308:
- cardinality now returns the size of the group (was order)
- order is a backward compatibility alias for cardinality
- __len__ raises a deprecation error

Issue created by migration from https://trac.sagemath.org/ticket/6250





---

archive/issue_comments_049911.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-08T23:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49911",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_049912.json:
```json
{
    "body": "matrix_group_gap-cardinality_len-6250-nt.2.patch superceedes the previous one (should have replaced it)\n\n#4326 depends on it",
    "created_at": "2009-06-08T23:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49912",
    "user": "nthiery"
}
```

matrix_group_gap-cardinality_len-6250-nt.2.patch superceedes the previous one (should have replaced it)

#4326 depends on it



---

archive/issue_comments_049913.json:
```json
{
    "body": "I have not applied or tested this patch but upon reading the code a few lines struck me as odd. Can you please explain how, if F is a finite field, F.order() -> F.cardinality() is correct? Has the order method for finite fields been rewritten? Did I miss the discussion on sage-delev that order should be deprecated and replaced by cardinality?",
    "created_at": "2009-06-08T23:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49913",
    "user": "wdj"
}
```

I have not applied or tested this patch but upon reading the code a few lines struck me as odd. Can you please explain how, if F is a finite field, F.order() -> F.cardinality() is correct? Has the order method for finite fields been rewritten? Did I miss the discussion on sage-delev that order should be deprecated and replaced by cardinality?



---

archive/issue_comments_049914.json:
```json
{
    "body": "As far as I remember, what was discussed on the list was about the order of an *element* of a field/group/...\n\nHere this is about the order of the group itself, which is its cardinality.",
    "created_at": "2009-06-08T23:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49914",
    "user": "nthiery"
}
```

As far as I remember, what was discussed on the list was about the order of an *element* of a field/group/...

Here this is about the order of the group itself, which is its cardinality.



---

archive/issue_comments_049915.json:
```json
{
    "body": "I don't agree with the suggestion in one of the docstrings that order might be deprecated. But that is just my (American) opinion, which might not be shared by the rest of the world:-) In any case, the patches do not apply cleanly to 4.0.rc0.",
    "created_at": "2009-06-10T11:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49915",
    "user": "wdj"
}
```

I don't agree with the suggestion in one of the docstrings that order might be deprecated. But that is just my (American) opinion, which might not be shared by the rest of the world:-) In any case, the patches do not apply cleanly to 4.0.rc0.



---

archive/issue_comments_049916.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-10T16:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49916",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049917.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> I don't agree with the suggestion in one of the docstrings that order might be deprecated.\n> But that is just my (American) opinion, which might not be shared by the rest of the world:-)\n\nI am fine with both options. From discussions on sage-devel, it seems that in general aliases are somewhat frowned upon.\nWe definitely want .cardinality(). But yes, even in Europe, some users would certainly be trying G.order() to get the size\nof the group. That's why I raised the issue.\n\nI am happy to remove the comment if you think its better.\n\n\n> In any case, the patches do not apply cleanly to 4.0.rc0. \n\n? I just retried, and it applies smoothly on sage 4.0.1. Did you only apply the second patch? (the first one should be deleted)",
    "created_at": "2009-06-10T16:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49917",
    "user": "nthiery"
}
```

Replying to [comment:4 wdj]:
> I don't agree with the suggestion in one of the docstrings that order might be deprecated.
> But that is just my (American) opinion, which might not be shared by the rest of the world:-)

I am fine with both options. From discussions on sage-devel, it seems that in general aliases are somewhat frowned upon.
We definitely want .cardinality(). But yes, even in Europe, some users would certainly be trying G.order() to get the size
of the group. That's why I raised the issue.

I am happy to remove the comment if you think its better.


> In any case, the patches do not apply cleanly to 4.0.rc0. 

? I just retried, and it applies smoothly on sage 4.0.1. Did you only apply the second patch? (the first one should be deleted)



---

archive/issue_comments_049918.json:
```json
{
    "body": "The second patch applied cleanly to 4.0.rc0 but failed sage -testall. I think it was unrelated but I'll retry on another version of Sage.",
    "created_at": "2009-06-11T10:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49918",
    "user": "wdj"
}
```

The second patch applied cleanly to 4.0.rc0 but failed sage -testall. I think it was unrelated but I'll retry on another version of Sage.



---

archive/issue_comments_049919.json:
```json
{
    "body": "The second patch applied cleanly to 4.0.1.a0 but failed sage -testall. However, that failure (in \"devel/sage/sage/misc/html.py\") is a known unrelated failure. The patch reads fine and does as it claims.",
    "created_at": "2009-06-11T13:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49919",
    "user": "wdj"
}
```

The second patch applied cleanly to 4.0.1.a0 but failed sage -testall. However, that failure (in "devel/sage/sage/misc/html.py") is a known unrelated failure. The patch reads fine and does as it claims.



---

archive/issue_comments_049920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6250#issuecomment-49920",
    "user": "ncalexan"
}
```

Resolution: fixed
