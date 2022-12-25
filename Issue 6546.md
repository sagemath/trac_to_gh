# Issue 6546: Fully implement edge thickness in plots of graphs

archive/issues_006546.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @slel\n\nKeywords: plot graph edge width thickness\n\nThere is an option for specifying the thickness/width of an edge in a graph (\"thickness\").  For a graph `G`\n\n`G.plot(thickness=10)`\n\nworks as expected, but\n\n`show(G, thickness=10)`\n\nraises an error about the option name being unrecognized.\n\nAlso, I couldn't find any mention of this parameter in the documentation anywhere.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6546\n\n",
    "created_at": "2009-07-17T04:59:38Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.3",
    "title": "Fully implement edge thickness in plots of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6546",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @rlmill

CC:  @slel

Keywords: plot graph edge width thickness

There is an option for specifying the thickness/width of an edge in a graph ("thickness").  For a graph `G`

`G.plot(thickness=10)`

works as expected, but

`show(G, thickness=10)`

raises an error about the option name being unrecognized.

Also, I couldn't find any mention of this parameter in the documentation anywhere.

Issue created by migration from https://trac.sagemath.org/ticket/6546





---

archive/issue_comments_053280.json:
```json
{
    "body": "It would seem this has gone backwards.  Now `.plot()` complains about not understanding `thickness`.  Drawing a (graphics primitive) `line` understands `thickness`.  So it should be a matter of making `thickness` a valid option of a graph plot and passing it to `matplotlib` in `graphs/graph_plot.py` when drawing (straight) edges.  Maybe curved edges would be just as easy?",
    "created_at": "2013-11-01T04:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6546#issuecomment-53280",
    "user": "https://github.com/rbeezer"
}
```

It would seem this has gone backwards.  Now `.plot()` complains about not understanding `thickness`.  Drawing a (graphics primitive) `line` understands `thickness`.  So it should be a matter of making `thickness` a valid option of a graph plot and passing it to `matplotlib` in `graphs/graph_plot.py` when drawing (straight) edges.  Maybe curved edges would be just as easy?



---

archive/issue_comments_053281.json:
```json
{
    "body": "A preliminary patch is attached. Just wanted to get an implementation out there, so that others can look at it or enhance it.\n----\nNew commits:",
    "created_at": "2014-06-22T14:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6546#issuecomment-53281",
    "user": "https://github.com/ppurka"
}
```

A preliminary patch is attached. Just wanted to get an implementation out there, so that others can look at it or enhance it.
----
New commits:



---

archive/issue_comments_053282.json:
```json
{
    "body": "See also #20035, #21540.",
    "created_at": "2018-04-20T15:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6546#issuecomment-53282",
    "user": "https://github.com/slel"
}
```

See also #20035, #21540.
