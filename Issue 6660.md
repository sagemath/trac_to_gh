# Issue 6660: Error in chromatic_number() and coloring() in the Graph class

archive/issues_006660.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe following code creates a Graph and computes its chromatic number :\n\nsage: h=Graph(\":I`ASWCaG`WaJC{afP\")\n\nsage: h.chromatic_number()\n\n4\n\nsage: h.coloring()\n\n[[6, 8], [9], [0, 4, 7, 3], [1, 2, 5]]\n\nMeanwhile, you can check that the coloring [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]] is valid with this code that checks that each class is actually an independent set.\n:\n\nfor c in [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]]:\n\n      print h.subgraph(c).connected_components_number()==len(c)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6660\n\n",
    "created_at": "2009-07-30T12:40:05Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Error in chromatic_number() and coloring() in the Graph class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6660",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

The following code creates a Graph and computes its chromatic number :

sage: h=Graph(":I`ASWCaG`WaJC{afP")

sage: h.chromatic_number()

4

sage: h.coloring()

[[6, 8], [9], [0, 4, 7, 3], [1, 2, 5]]

Meanwhile, you can check that the coloring [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]] is valid with this code that checks that each class is actually an independent set.
:

for c in [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]]:

      print h.subgraph(c).connected_components_number()==len(c)

Issue created by migration from https://trac.sagemath.org/ticket/6660





---

archive/issue_comments_054569.json:
```json
{
    "body": "Answer from Rob Beezer on Sage-devel :\n\n  It appears to me that this graph has chromatic number 4.  The three\n  classes given for a 3-coloring do not include every vertex and have\n  repeated vertices (namely 3 and 9).  Try the following:\n  \n* Color the 4-5-6 triangle with three colors.\n  \n* Color the 7-8-9 triangle with three colors where you will be forced to color vertex 8 the same color as vertex 5.\n  \n* Vertex 1 is adjacent to 4, 6, 8, which now all have different colors, forcing a fourth color for vertex 1.\n  \n* The coloring from  h.coloring()  seems to check as a legitimate 4-coloring.\n  \n  As an aside, maybe the graph6 format doesn't work so well in Trac? The back-ticks seem to have disappeared, leading to quite a different\ngraph.  ;-)\n  \n   Rob \n\n... which is perfectly right ! It came from a mistake I made in the LP relaxation... now fixed ! ;-)\n\nThis ticket can be deleted.\n\nNathann",
    "created_at": "2009-07-30T16:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6660#issuecomment-54569",
    "user": "https://github.com/nathanncohen"
}
```

Answer from Rob Beezer on Sage-devel :

  It appears to me that this graph has chromatic number 4.  The three
  classes given for a 3-coloring do not include every vertex and have
  repeated vertices (namely 3 and 9).  Try the following:
  
* Color the 4-5-6 triangle with three colors.
  
* Color the 7-8-9 triangle with three colors where you will be forced to color vertex 8 the same color as vertex 5.
  
* Vertex 1 is adjacent to 4, 6, 8, which now all have different colors, forcing a fourth color for vertex 1.
  
* The coloring from  h.coloring()  seems to check as a legitimate 4-coloring.
  
  As an aside, maybe the graph6 format doesn't work so well in Trac? The back-ticks seem to have disappeared, leading to quite a different
graph.  ;-)
  
   Rob 

... which is perfectly right ! It came from a mistake I made in the LP relaxation... now fixed ! ;-)

This ticket can be deleted.

Nathann



---

archive/issue_events_006896.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2009-07-30T16:55:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6660",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6660#event-6896"
}
```



---

archive/issue_comments_054570.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-30T16:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6660#issuecomment-54570",
    "user": "https://github.com/rlmill"
}
```

Resolution: invalid
