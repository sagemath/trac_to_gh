# Issue 5: Change use of weak references in actions

CC:  simonking nbruin

Currently, the coercion model uses strong references to actions and actions use weak references to their domain. It seems more efficient and simpler to turn this around: actions should internally use ordinary strong references but the coercion model should use weak references.

Issue created by migration from https://trac.sagemath.org/ticket/26802


