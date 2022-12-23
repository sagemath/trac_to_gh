# Issue 1283: Update coercion model API

Issue created by migration from https://trac.sagemath.org/ticket/1283

Original creator: robertwb

Original creation time: 2007-11-26 20:48:01

Assignee: somebody

Currently, coercions (and conversions) are defined in many different places in the SAGE codebase. We are going through each parent and consolidating/cleaning up the codebase to conform to the new coercion API, as described in the new programming guide. 

This includes removing all Parent __call__ methods to use a generic __call__.


---

Attachment


---

Comment by robertwb created at 2007-11-26 23:44:33

See relevant section of http://wiki.sagemath.org/days6/sprint/prog_guide/prog_guide/outline


---

Comment by robertwb created at 2008-02-21 23:03:07

See also http://wiki.sagemath.org/days7/coercion/todo


---

Comment by robertwb created at 2008-03-04 22:24:05

Resolution: duplicate


---

Comment by robertwb created at 2008-03-04 22:24:05

Dupe of #2314
