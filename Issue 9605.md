# Issue 9605: Caching latex preamble setup for graphs

archive/issues_009605.json:
```json
{
    "body": "Assignee: jason\n\nOn #9027 it was noted that using the cached_function decorator on `sage.graphs.graph_latex.setup_latex_preamble` excludes it from the reference manual.  While trying to resolve this (see suggestion on #9027), it seems the doctests, when run in random order, yield errors.  This situation has been split off that ticket and moved here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9605\n\n",
    "created_at": "2010-07-26T18:26:21Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Caching latex preamble setup for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9605",
    "user": "rbeezer"
}
```
Assignee: jason

On #9027 it was noted that using the cached_function decorator on `sage.graphs.graph_latex.setup_latex_preamble` excludes it from the reference manual.  While trying to resolve this (see suggestion on #9027), it seems the doctests, when run in random order, yield errors.  This situation has been split off that ticket and moved here.

Issue created by migration from https://trac.sagemath.org/ticket/9605


