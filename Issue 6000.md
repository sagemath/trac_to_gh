# Issue 6000: [with patch, positive review] Sets enumerated by exploring a search space with a (lazy) tree or graph structure

archive/issues_006000.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: enumerate sets, depth first search, ideal of a relation\n\nThis patches extend the sage.combinat.backtrack library with other\ngeneric tools for constructing large sets whose elements can be\nenumerated by exploring a search space with a (lazy) tree or graph\nstructure.\n\n- SearchForest:\n  Depth first search through a tree descrived by a `child` function\n- GenericBacktracker: (was readilly there)\n  Depth first search through a tree descrived by a `child` function, with branch pruning, ...\n- TransitiveIdeal:\n  Depth first search through a graph described by a `neighbours` relation\n- TransitiveIdealGraded:\n  Breath first search through a graph described by a `neighbours` relation\n\nTodo: the names are crappy and inconsistent, because they come from\ndifferent point of views. We need to find a good naming scheme!!! \n\nDo we want to emphasize the underlying graph/tree structure?  The\nbranch&bound aspect? The transitive closure of a relation point of\nview?\n\nTodo: which interface do we want:\n- TransitiveIdeal(relation, generators)\n- TransitiveIdeal(generators, relation)\nThe code needs to be standardized once the choice is done.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6000\n\n",
    "closed_at": "2009-06-01T00:02:26Z",
    "created_at": "2009-05-06T19:31:56Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] Sets enumerated by exploring a search space with a (lazy) tree or graph structure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6000",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: enumerate sets, depth first search, ideal of a relation

This patches extend the sage.combinat.backtrack library with other
generic tools for constructing large sets whose elements can be
enumerated by exploring a search space with a (lazy) tree or graph
structure.

- SearchForest:
  Depth first search through a tree descrived by a `child` function
- GenericBacktracker: (was readilly there)
  Depth first search through a tree descrived by a `child` function, with branch pruning, ...
- TransitiveIdeal:
  Depth first search through a graph described by a `neighbours` relation
- TransitiveIdealGraded:
  Breath first search through a graph described by a `neighbours` relation

Todo: the names are crappy and inconsistent, because they come from
different point of views. We need to find a good naming scheme!!! 

Do we want to emphasize the underlying graph/tree structure?  The
branch&bound aspect? The transitive closure of a relation point of
view?

Todo: which interface do we want:
- TransitiveIdeal(relation, generators)
- TransitiveIdeal(generators, relation)
The code needs to be standardized once the choice is done.


Issue created by migration from https://trac.sagemath.org/ticket/6000





---

archive/issue_comments_047636.json:
```json
{
    "body": "Attachment [transitive_ideal-6000-submitted.patch](tarball://root/attachments/some-uuid/ticket6000/transitive_ideal-6000-submitted.patch) by @nthiery created at 2009-05-06 22:48:06",
    "created_at": "2009-05-06T22:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47636",
    "user": "https://github.com/nthiery"
}
```

Attachment [transitive_ideal-6000-submitted.patch](tarball://root/attachments/some-uuid/ticket6000/transitive_ideal-6000-submitted.patch) by @nthiery created at 2009-05-06 22:48:06



---

archive/issue_comments_047637.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47637",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047638.json:
```json
{
    "body": "Apply on top of main patch",
    "created_at": "2009-05-21T05:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47638",
    "user": "https://github.com/rbeezer"
}
```

Apply on top of main patch



---

archive/issue_comments_047639.json:
```json
{
    "body": "Attachment [trac_6000_reviewer.patch](tarball://root/attachments/some-uuid/ticket6000/trac_6000_reviewer.patch) by @rbeezer created at 2009-05-21 05:11:41\n\nPasses tests:   ./sage -t devel/sage-backtrack/sage/combinat/\n\nReviewer patch adds two doctests, and some general cleanup, so apply on top of the main patch.\n\nIn the case of a search tree (not a graph), options for \"leaves only\" would be useful.  Then the generators could be checked for a first element when using a search tree for existence questions.\n\nBuilding a single function to call these routines as variants might ease the question of names and interfaces.\n\nPositive review.",
    "created_at": "2009-05-21T05:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47639",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6000_reviewer.patch](tarball://root/attachments/some-uuid/ticket6000/trac_6000_reviewer.patch) by @rbeezer created at 2009-05-21 05:11:41

Passes tests:   ./sage -t devel/sage-backtrack/sage/combinat/

Reviewer patch adds two doctests, and some general cleanup, so apply on top of the main patch.

In the case of a search tree (not a graph), options for "leaves only" would be useful.  Then the generators could be checked for a first element when using a search tree for existence questions.

Building a single function to call these routines as variants might ease the question of names and interfaces.

Positive review.



---

archive/issue_comments_047640.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47640",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_047641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6000#issuecomment-47641",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_014098.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-01T00:02:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6000",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6000#event-14098"
}
```
