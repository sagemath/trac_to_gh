# Issue 7228: [with patch, need review] Generalized Petersen graph generator

archive/issues_007228.json:
```json
{
    "body": "Assignee: rlm\n\nThis patch introduces a generator for the generalized Petersen graphs.\n\nhttp://mathworld.wolfram.com/GeneralizedPetersenGraph.html\nhttp://en.wikipedia.org/wiki/Petersen_graph#Generalized_Petersen_graphs\n\nThe method used for plotting gives exactly the same result as the Petersen, Desargues, and the Moebius-Kantor graphs, so these functions have been simplified to just call GeneralizedPetersenGraph() with suitable parameter values and then change the graph's name to the named graph in question.\n\nPatch is made against sage 4.1.2\n\nIssue created by migration from https://trac.sagemath.org/ticket/7228\n\n",
    "created_at": "2009-10-15T15:29:31Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, need review] Generalized Petersen graph generator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7228",
    "user": "AJonsson"
}
```
Assignee: rlm

This patch introduces a generator for the generalized Petersen graphs.

http://mathworld.wolfram.com/GeneralizedPetersenGraph.html
http://en.wikipedia.org/wiki/Petersen_graph#Generalized_Petersen_graphs

The method used for plotting gives exactly the same result as the Petersen, Desargues, and the Moebius-Kantor graphs, so these functions have been simplified to just call GeneralizedPetersenGraph() with suitable parameter values and then change the graph's name to the named graph in question.

Patch is made against sage 4.1.2

Issue created by migration from https://trac.sagemath.org/ticket/7228





---

archive/issue_comments_059954.json:
```json
{
    "body": "generator for generalized Petersen graphs",
    "created_at": "2009-10-15T15:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59954",
    "user": "AJonsson"
}
```

generator for generalized Petersen graphs



---

archive/issue_comments_059955.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-15T15:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59955",
    "user": "AJonsson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059956.json:
```json
{
    "body": "Attachment [trac_7228.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228.patch) by AJonsson created at 2009-10-15 15:33:12",
    "created_at": "2009-10-15T15:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59956",
    "user": "AJonsson"
}
```

Attachment [trac_7228.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228.patch) by AJonsson created at 2009-10-15 15:33:12



---

archive/issue_comments_059957.json:
```json
{
    "body": "This patch seems perfect to me ! I just modified the name of this graph so that it includes the values of n and k, and added some ` somewhere.\n\nIf you agree with these, you can set this ticket to positive review !",
    "created_at": "2009-10-18T13:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59957",
    "user": "ncohen"
}
```

This patch seems perfect to me ! I just modified the name of this graph so that it includes the values of n and k, and added some ` somewhere.

If you agree with these, you can set this ticket to positive review !



---

archive/issue_comments_059958.json:
```json
{
    "body": "Attachment [trac_7228-reviewer.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228-reviewer.patch) by AJonsson created at 2009-10-20 07:15:23\n\nThanks for your review, I agree with all changes. I noticed however that my patch caused a test to fail in graph.py (a test that looks up the coordinates of all vertices of the Petersen Graph). The failure was trivial, the main reason was that I had placed the nodes at larger distance from (0,0) than before.\n\nI have fixed these position issues in this new patch, which should be applied on top of trac_7228-reviewer.patch",
    "created_at": "2009-10-20T07:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59958",
    "user": "AJonsson"
}
```

Attachment [trac_7228-reviewer.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228-reviewer.patch) by AJonsson created at 2009-10-20 07:15:23

Thanks for your review, I agree with all changes. I noticed however that my patch caused a test to fail in graph.py (a test that looks up the coordinates of all vertices of the Petersen Graph). The failure was trivial, the main reason was that I had placed the nodes at larger distance from (0,0) than before.

I have fixed these position issues in this new patch, which should be applied on top of trac_7228-reviewer.patch



---

archive/issue_comments_059959.json:
```json
{
    "body": "Attachment [trac_7228-fix_positions.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228-fix_positions.patch) by AJonsson created at 2009-10-20 07:16:34\n\nfixes failure of position test",
    "created_at": "2009-10-20T07:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59959",
    "user": "AJonsson"
}
```

Attachment [trac_7228-fix_positions.patch](tarball://root/attachments/some-uuid/ticket7228/trac_7228-fix_positions.patch) by AJonsson created at 2009-10-20 07:16:34

fixes failure of position test



---

archive/issue_comments_059960.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-20T14:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59960",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059961.json:
```json
{
    "body": "good point !\n\nPositive review !",
    "created_at": "2009-10-20T14:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59961",
    "user": "ncohen"
}
```

good point !

Positive review !



---

archive/issue_comments_059962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T04:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7228#issuecomment-59962",
    "user": "mhansen"
}
```

Resolution: fixed
