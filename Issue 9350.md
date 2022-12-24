# Issue 9350: Python max flow method

archive/issues_009350.json:
```json
{
    "body": "Assignee: jason, mvngu, ncohen, rlm\n\nImplementation of a max-flow algorithm which does not use Linear Programming.\n\nI will update it right after #8870 is merged\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9350\n\n",
    "created_at": "2010-06-27T10:19:03Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Python max flow method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9350",
    "user": "ncohen"
}
```
Assignee: jason, mvngu, ncohen, rlm

Implementation of a max-flow algorithm which does not use Linear Programming.

I will update it right after #8870 is merged

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9350





---

archive/issue_comments_088745.json:
```json
{
    "body": "Updated, and now needs review :-)",
    "created_at": "2010-07-08T12:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88745",
    "user": "ncohen"
}
```

Updated, and now needs review :-)



---

archive/issue_comments_088746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-08T12:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88746",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088747.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-07-29T13:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88747",
    "user": "wdj"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_088748.json:
```json
{
    "body": "This applies okay to 4.5.2.a1 and seems to pass all tests, except for some unrelated failures. However, there are no examples in edge_cut with vertices=True, eg\n\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.edge_cut(0, 3, method=\"FF\", vertices=True)\n[3, [(0, 1, None), (0, 4, None), (0, 5, None)], [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]\n```\n\nWhy is this?",
    "created_at": "2010-07-29T13:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88748",
    "user": "wdj"
}
```

This applies okay to 4.5.2.a1 and seems to pass all tests, except for some unrelated failures. However, there are no examples in edge_cut with vertices=True, eg


```
sage: g = graphs.PetersenGraph()
sage: g.edge_cut(0, 3, method="FF", vertices=True)
[3, [(0, 1, None), (0, 4, None), (0, 5, None)], [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
```

Why is this?



---

archive/issue_comments_088749.json:
```json
{
    "body": "> Why is this?\n \nWhat do you think of line 3652 of the generic_graph.py file ? `:-)`\n\n\n```\nsage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) \n```\n\n\nNathann",
    "created_at": "2010-07-29T14:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88749",
    "user": "ncohen"
}
```

> Why is this?
 
What do you think of line 3652 of the generic_graph.py file ? `:-)`


```
sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) 
```


Nathann



---

archive/issue_comments_088750.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> > Why is this?\n>  \n> What do you think of line 3652 of the generic_graph.py file ? `:-)`\n> \n> {{{\n> sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) \n> }}}\n> \n> Nathann\n\nThe value isn't returned, so the potential user cannot see examples of how the output changes for different choices of the input. I'm just wondering if there was a good reason for omitting the edges in the output. An example with value_only=False would be equally nice. Finally, to be extremely picky, the description\n\n\n```\n``vertices`` -- boolean (default: ``False``). When set to ``True``,\n          also returns the two sets of vertices that are disconnected by\n          the cut. Implies ``value_only=False``.\n```\n\nshould probably read\n\n```\n``vertices`` -- boolean (default: ``False``). When set to ``True``,\n          returns a list of edges in the edge cut and the two \n          sets of vertices that are disconnected by the cut. \n          Note: ``vertices=True`` implies ``value_only=False``.\n```\n\n\nDoes this seem reasonable?",
    "created_at": "2010-07-29T16:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88750",
    "user": "wdj"
}
```

Replying to [comment:4 ncohen]:
> > Why is this?
>  
> What do you think of line 3652 of the generic_graph.py file ? `:-)`
> 
> {{{
> sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) 
> }}}
> 
> Nathann

The value isn't returned, so the potential user cannot see examples of how the output changes for different choices of the input. I'm just wondering if there was a good reason for omitting the edges in the output. An example with value_only=False would be equally nice. Finally, to be extremely picky, the description


```
``vertices`` -- boolean (default: ``False``). When set to ``True``,
          also returns the two sets of vertices that are disconnected by
          the cut. Implies ``value_only=False``.
```

should probably read

```
``vertices`` -- boolean (default: ``False``). When set to ``True``,
          returns a list of edges in the edge cut and the two 
          sets of vertices that are disconnected by the cut. 
          Note: ``vertices=True`` implies ``value_only=False``.
```


Does this seem reasonable?



---

archive/issue_comments_088751.json:
```json
{
    "body": "Attachment [trac_9350.patch](tarball://root/attachments/some-uuid/ticket9350/trac_9350.patch) by ncohen created at 2010-07-29 17:00:56",
    "created_at": "2010-07-29T17:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88751",
    "user": "ncohen"
}
```

Attachment [trac_9350.patch](tarball://root/attachments/some-uuid/ticket9350/trac_9350.patch) by ncohen created at 2010-07-29 17:00:56



---

archive/issue_comments_088752.json:
```json
{
    "body": "It does ! I just updated the patch with you example and the corrected docstring `:-)`\n\nThere was, indeed, a reason for never showing directly the output of all these methods : it formerly used Linear Programming, and the results of LP, eve though correct, can vary depending on the time of the day and the solver used. So showing it is asking for trouble, though one can perfectly check some relations... But this Python implementation being deterministic, it's fine now !\n\nNathann",
    "created_at": "2010-07-29T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88752",
    "user": "ncohen"
}
```

It does ! I just updated the patch with you example and the corrected docstring `:-)`

There was, indeed, a reason for never showing directly the output of all these methods : it formerly used Linear Programming, and the results of LP, eve though correct, can vary depending on the time of the day and the solver used. So showing it is asking for trouble, though one can perfectly check some relations... But this Python implementation being deterministic, it's fine now !

Nathann



---

archive/issue_comments_088753.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-29T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88753",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_088754.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> It does ! I just updated the patch with you example and the corrected docstring `:-)`\n> \n> There was, indeed, a reason for never showing directly the output of all these \n> methods : it formerly used Linear Programming, and the results of LP, even \n> though correct, can vary depending on the time of the day and the solver used. \n> So showing it is asking for trouble, though one can perfectly check some \n> relations... But this Python implementation being deterministic, it's fine now !\n> \n> Nathann\n\nExcellent. Passed tested for me (except for unrelated doctest failures on a mac 10.6.4).\n\nThanks Nathann!!",
    "created_at": "2010-07-29T22:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88754",
    "user": "wdj"
}
```

Replying to [comment:6 ncohen]:
> It does ! I just updated the patch with you example and the corrected docstring `:-)`
> 
> There was, indeed, a reason for never showing directly the output of all these 
> methods : it formerly used Linear Programming, and the results of LP, even 
> though correct, can vary depending on the time of the day and the solver used. 
> So showing it is asking for trouble, though one can perfectly check some 
> relations... But this Python implementation being deterministic, it's fine now !
> 
> Nathann

Excellent. Passed tested for me (except for unrelated doctest failures on a mac 10.6.4).

Thanks Nathann!!



---

archive/issue_comments_088755.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T05:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88755",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088756.json:
```json
{
    "body": "I also tested this, and it looks OK. \nWdj, have you forgotten to give it positive review?\n\nDima",
    "created_at": "2010-09-04T05:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88756",
    "user": "dimpase"
}
```

I also tested this, and it looks OK. 
Wdj, have you forgotten to give it positive review?

Dima



---

archive/issue_comments_088757.json:
```json
{
    "body": "Thanksssss ! :-)",
    "created_at": "2010-09-04T06:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88757",
    "user": "ncohen"
}
```

Thanksssss ! :-)



---

archive/issue_comments_088758.json:
```json
{
    "body": "Please remember to fill in the \"Author(s)\" and \"Reviewer(s)\" fields.",
    "created_at": "2010-09-15T22:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88758",
    "user": "mpatel"
}
```

Please remember to fill in the "Author(s)" and "Reviewer(s)" fields.



---

archive/issue_comments_088759.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9350#issuecomment-88759",
    "user": "mpatel"
}
```

Resolution: fixed
