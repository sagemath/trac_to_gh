# Issue 9605: Caching latex preamble setup for graphs

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-07-26 18:26:21

Assignee: jason

On #9027 it was noted that using the cached_function decorator on `sage.graphs.graph_latex.setup_latex_preamble` excludes it from the reference manual.  While trying to resolve this (see suggestion on #9027), it seems the doctests, when run in random order, yield errors.  This situation has been split off that ticket and moved here.
