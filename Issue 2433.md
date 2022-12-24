# Issue 2433: [patches coming soon] Refactor graph code; prepare for backend migration; miscellaneous small things from Waterloo

archive/issues_002433.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nThere are quite a few patches for this ticket, so I'll put them all on the ticket for easier review, but I'll also include a flattened patch, for easy merging.\n\n1. I have moved all functions that are specific to `Graph` or `DiGraph` to that class, and I have moved duplicate code into `GenericGraph`.\n\n2. In preparation for switching out the default backend for the much faster CGraphs, I have reduced the dependence on NetworkX as much as possible for the moment. For most of the rest of the functions, I have switched `G._nxg` to use `G.networkx_graph()` so that for functions where we still need to use NX, the switch won't be difficult, and we won't lose any functionality.\n\n3. In refactoring the code, and reducing duplicate code, I have combined the two plot3d options into one function, and made jmol the default, finally.\n\n4. Since I have been doing this during my visit with Godsil and Royle at Waterloo, there have been several very easy suggestions they have made which have gotten incorporated into this work as well. For example, providing much clearer aliases `num_verts` and `num_edges` for the somewhat cryptic `order` and `size` functions.\n\n5. I have fixed several documentation typos, and added several new doctests. The coverage score for `graph.py` has increased 87% -> 91%.\n\n6. The patches here are based on sage-2.10.3.rc2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2433\n\n",
    "created_at": "2008-03-09T04:50:04Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[patches coming soon] Refactor graph code; prepare for backend migration; miscellaneous small things from Waterloo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2433",
    "user": "@rlmill"
}
```
Assignee: @rlmill

CC:  @jasongrout

There are quite a few patches for this ticket, so I'll put them all on the ticket for easier review, but I'll also include a flattened patch, for easy merging.

1. I have moved all functions that are specific to `Graph` or `DiGraph` to that class, and I have moved duplicate code into `GenericGraph`.

2. In preparation for switching out the default backend for the much faster CGraphs, I have reduced the dependence on NetworkX as much as possible for the moment. For most of the rest of the functions, I have switched `G._nxg` to use `G.networkx_graph()` so that for functions where we still need to use NX, the switch won't be difficult, and we won't lose any functionality.

3. In refactoring the code, and reducing duplicate code, I have combined the two plot3d options into one function, and made jmol the default, finally.

4. Since I have been doing this during my visit with Godsil and Royle at Waterloo, there have been several very easy suggestions they have made which have gotten incorporated into this work as well. For example, providing much clearer aliases `num_verts` and `num_edges` for the somewhat cryptic `order` and `size` functions.

5. I have fixed several documentation typos, and added several new doctests. The coverage score for `graph.py` has increased 87% -> 91%.

6. The patches here are based on sage-2.10.3.rc2.

Issue created by migration from https://trac.sagemath.org/ticket/2433





---

archive/issue_comments_016464.json:
```json
{
    "body": "I can't actually post the patches as attachments to the trac ticket, so here are the links instead:\n\nThe patches one by one, to make reviewing them easier:\n\nhttp://sage.math.washington.edu/home/rlmill/2433-individual_patches.tar\n\nThe patches rolled into one big one, to make merging easier:\n\nhttp://sage.math.washington.edu/home/rlmill/2433-flat.patch",
    "created_at": "2008-03-09T05:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2433#issuecomment-16464",
    "user": "@rlmill"
}
```

I can't actually post the patches as attachments to the trac ticket, so here are the links instead:

The patches one by one, to make reviewing them easier:

http://sage.math.washington.edu/home/rlmill/2433-individual_patches.tar

The patches rolled into one big one, to make merging easier:

http://sage.math.washington.edu/home/rlmill/2433-flat.patch



---

archive/issue_comments_016465.json:
```json
{
    "body": "I've gone through all of the individual patches, and they definitely look good to me.  The big patch  applied cleanly to 2.10.3.rc2 for me and all tests pass.",
    "created_at": "2008-03-10T00:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2433#issuecomment-16465",
    "user": "@mwhansen"
}
```

I've gone through all of the individual patches, and they definitely look good to me.  The big patch  applied cleanly to 2.10.3.rc2 for me and all tests pass.



---

archive/issue_comments_016466.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2433#issuecomment-16466",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016467.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2433#issuecomment-16467",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4
