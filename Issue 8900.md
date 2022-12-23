# Issue 8900: Implement multiparameter overloaded functions, with explicit registration

Issue created by migration from https://trac.sagemath.org/ticket/8900

Original creator: nthiery

Original creation time: 2010-05-05 23:41:28

Assignee: robertwb

CC:  sage-combinat

Keywords: overloading




---

Comment by kdilks created at 2015-06-12 16:34:02

I noticed that this ticket was mentioned in `hopf_algebras.py` in a commented out TODO note for `antipode_by_coercion`, and it seemed like it would be used to do what ticket: 15573 is attempting to achieve (have product/coproduct/antipode for Hopf algebras automatically choose a realization where the corresponding method is defined). Did this ever make it into Sage, and if not, are there still any plans to put it in?
