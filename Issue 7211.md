# Issue 7211: Improve implicit plotting

archive/issues_007211.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot, implicit, contour\n\nSee [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/603348c82c817a21) for some recent details, and [this thread](https://groups.google.com/group/sage-devel/browse_thread/thread/6b1d3d0f06db9c6a) for older discussion; both threads have links to explanations of algorithms.\n\nThe problem is that we only use contour plotting, and no adaptive changes, for implicit plotting, which means that a nice plot takes a huge number of plot points, but a realistic one doesn't look so nice, especially if there are weird turnarounds. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7211\n\n",
    "created_at": "2009-10-14T18:56:28Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Improve implicit plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7211",
    "user": "kcrisman"
}
```
Assignee: was

Keywords: plot, implicit, contour

See [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/603348c82c817a21) for some recent details, and [this thread](https://groups.google.com/group/sage-devel/browse_thread/thread/6b1d3d0f06db9c6a) for older discussion; both threads have links to explanations of algorithms.

The problem is that we only use contour plotting, and no adaptive changes, for implicit plotting, which means that a nice plot takes a huge number of plot points, but a realistic one doesn't look so nice, especially if there are weird turnarounds. 

Issue created by migration from https://trac.sagemath.org/ticket/7211


