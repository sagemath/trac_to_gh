# Issue 785: standard smith normal form

Issue created by migration from https://trac.sagemath.org/ticket/785

Original creator: syazdani

Original creation time: 2007-10-02 13:38:16

Assignee: syazdani

Keywords: smith_form

The smith_form function for integer dense matrices are printed backward from the usual notation. This is because pari prints them backward.

The enclosed patch fixes this problem, by permuting the entries appropriately.


---

Comment by syazdani created at 2007-10-02 13:43:37

Resolution: duplicate
