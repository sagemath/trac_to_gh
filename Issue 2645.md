# Issue 2645: arrow3d is sometimes too long

archive/issues_002645.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe patch below cuts off the shaft and part of the head if an arrow3d is too long for the given vector.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2645\n\n",
    "created_at": "2008-03-22T15:41:23Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "arrow3d is sometimes too long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2645",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

The patch below cuts off the shaft and part of the head if an arrow3d is too long for the given vector.

Issue created by migration from https://trac.sagemath.org/ticket/2645





---

archive/issue_comments_018183.json:
```json
{
    "body": "Attachment [arrow3d-short.patch](tarball://root/attachments/some-uuid/ticket2645/arrow3d-short.patch) by @jasongrout created at 2008-03-22 15:41:45",
    "created_at": "2008-03-22T15:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18183",
    "user": "@jasongrout"
}
```

Attachment [arrow3d-short.patch](tarball://root/attachments/some-uuid/ticket2645/arrow3d-short.patch) by @jasongrout created at 2008-03-22 15:41:45



---

archive/issue_comments_018184.json:
```json
{
    "body": "In https://groups.google.com/group/sage-devel/browse_thread/thread/d88bc7503638af0c Robert Bradshaw commented:\n\n```\nThe line3d command will produce much faster arrows:\n\nline3d([(0,0,0), (1,2,3)], thickness=2, arrow_head=True)\n\nThe ds parameter is supposed to relate the size of the overall scene  \nto the number of pixels in the final render. I agree there needs to  \nbe a better way to set it. \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T21:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18184",
    "user": "mabshoff"
}
```

In https://groups.google.com/group/sage-devel/browse_thread/thread/d88bc7503638af0c Robert Bradshaw commented:

```
The line3d command will produce much faster arrows:

line3d([(0,0,0), (1,2,3)], thickness=2, arrow_head=True)

The ds parameter is supposed to relate the size of the overall scene  
to the number of pixels in the final render. I agree there needs to  
be a better way to set it. 
```


Cheers,

Michael



---

archive/issue_comments_018185.json:
```json
{
    "body": "The comment about line3d does not change the bug and does not change the patch.  The comment about line3d was to address a problem with plot_vector_field3d (#2646)",
    "created_at": "2008-03-22T22:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18185",
    "user": "@jasongrout"
}
```

The comment about line3d does not change the bug and does not change the patch.  The comment about line3d was to address a problem with plot_vector_field3d (#2646)



---

archive/issue_comments_018186.json:
```json
{
    "body": "Works great for me. A good example of this is\n\n\n```\nsage: sum([arrow3d((cos(t),sin(t),0),(cos(t),sin(t),t/10)) for t in [0,0.3,..,2*pi]])\n```\n",
    "created_at": "2008-03-27T06:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18186",
    "user": "@robertwb"
}
```

Works great for me. A good example of this is


```
sage: sum([arrow3d((cos(t),sin(t),0),(cos(t),sin(t),t/10)) for t in [0,0.3,..,2*pi]])
```




---

archive/issue_comments_018187.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-27T07:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18187",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-27T07:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2645#issuecomment-18188",
    "user": "mabshoff"
}
```

Resolution: fixed
