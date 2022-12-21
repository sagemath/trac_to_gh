# Issue 8872: neighbor-finding for attractor of IFS from a multidimensional radix representation

Issue created by migration from Trac.

Original creator: ecurry

Original creation time: 2010-05-04 19:11:57

Assignee: Eva Curry

Add to sage a function that takes as input a dilation matrix A and a standard digit set D for A, and outputs the list of neighbors of the set T(A,D) = { sum_{j=1}^{infty} A^{-j}d_j : d_j \in D }.

This function will implement Scheicher and Thuswaldner's neighbor-finding algorithm.
