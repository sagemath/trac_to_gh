# Issue 8591: Support for Gurobi

Issue created by migration from https://trac.sagemath.org/ticket/8591

Original creator: ncohen

Original creation time: 2010-03-23 18:26:56

Assignee: jkantor

CC:  malb schilly

Yet another solver, which has been reported to be interesting several times...

It shouldn't be hard to implement as it can be done through Coin's interface, as Cplex and Cbc, so it should mainly consist in a copy of a 15-lines file and a basic update of Cbc's package

http://www.gurobi.com/

Nathann


---

Comment by jason created at 2010-03-24 01:28:14

Looking at the Gurobi team, it certainly looks interesting!

!http://www.gurobi.com/html/management.html

It looks like a bunch of the CPLEX people split off and started Gurobi.


---

Comment by ncohen created at 2010-09-06 11:13:02

Changing component from numerical to linear programming.


---

Comment by ncohen created at 2011-11-01 13:48:04

OOps, I did it again.... Could this ticket be closed ? I created this ticket a loooong time ago, and finally implemented it in a new ticket (#11949) `:-)`

Nathann


---

Comment by ohanar created at 2012-06-07 08:48:28

Changing status from new to needs_review.


---

Comment by ohanar created at 2012-06-07 08:48:35

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-19 13:31:13

Resolution: duplicate
