# Issue 5365: graphplot arrowheads are hidden in multi-edge digraphs

archive/issues_005365.json:
```json
{
    "body": "Assignee: ekirkman, rlm\n\nKristin Lauter pointed out that the following input:\n\nsage: S = SupersingularModule(389)\nsage: D = DiGraph(S.hecke_matrix(2))\nsage: D.plot(vertex_size=50).show(figsize=10)\n\nproduces a graph where the arrowheads of some edges are hidden by the vertex.  \n\nThis is going to be a one-ish line fix that I can post as soon as I'm done building 3.3.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5365\n\n",
    "created_at": "2009-02-24T23:44:54Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "graphplot arrowheads are hidden in multi-edge digraphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5365",
    "user": "ekirkman"
}
```
Assignee: ekirkman, rlm

Kristin Lauter pointed out that the following input:

sage: S = SupersingularModule(389)
sage: D = DiGraph(S.hecke_matrix(2))
sage: D.plot(vertex_size=50).show(figsize=10)

produces a graph where the arrowheads of some edges are hidden by the vertex.  

This is going to be a one-ish line fix that I can post as soon as I'm done building 3.3.


Issue created by migration from https://trac.sagemath.org/ticket/5365





---

archive/issue_comments_041329.json:
```json
{
    "body": "Attachment [t2.png](tarball://root/attachments/some-uuid/ticket5365/t2.png) by ekirkman created at 2009-02-24 23:48:52\n\nThe picture attachment (t2.png) is the current buggy output.  I will post another picture example with my patch this evening.",
    "created_at": "2009-02-24T23:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5365#issuecomment-41329",
    "user": "ekirkman"
}
```

Attachment [t2.png](tarball://root/attachments/some-uuid/ticket5365/t2.png) by ekirkman created at 2009-02-24 23:48:52

The picture attachment (t2.png) is the current buggy output.  I will post another picture example with my patch this evening.



---

archive/issue_comments_041330.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-02-24T23:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5365#issuecomment-41330",
    "user": "ekirkman"
}
```

Resolution: duplicate



---

archive/issue_comments_041331.json:
```json
{
    "body": "This is a duplicate now...  (See ticket #5366).  Apparently the back button isn't the best way to adjust your wiki formatting...  (Sorry mabs).",
    "created_at": "2009-02-24T23:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5365#issuecomment-41331",
    "user": "ekirkman"
}
```

This is a duplicate now...  (See ticket #5366).  Apparently the back button isn't the best way to adjust your wiki formatting...  (Sorry mabs).
