# Issue 9980: Unify univariate and multivariate power series rings, as has been done for polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/9981

Original creator: niles

Original creation time: 2010-09-23 17:49:58

Assignee: malb

CC:  niles

Keywords: power series

Multivariate power series rings are implemented in #1956 as a subclass of (univariate) power series rings.  The two should be merged, following the implementation of polynomial rings.  As a first step, some behavior of `PowerSeriesRing` must be deprecated; a ticket for this is at #9980.
