# Issue 2918: make scipy use umfpack

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-04-14 17:01:52

Assignee: mabshoff

Scipy can optionally use umfpack for sparse solvers. We currently build umfpack as part of cvxopt. 
We don't make scipy use umfpack because the wrappers use swig. We need to autogenerate the swig wrappers so scipy can build against them without swig. 


---

Comment by jkantor created at 2008-04-14 17:02:19

Changing component from Cygwin to numerical.


---

Comment by jkantor created at 2008-04-14 17:02:19

Changing assignee from mabshoff to jkantor.


---

Comment by mabshoff created at 2008-12-02 02:03:53

SciPy 0.7 is deprecating Umfpack support and moving it to a SciKit. It might be better to have an umfpack.spkg that also contains that new SciKit.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 08:58:48

Since scipy 0.7 is now out I am not sure what to do about this? Make it invalid? Change the ticket so that we install an optional umfpack-scikit.spkg? 

Note that cvxopt already compiles umfpack for intenal use, so we might be able to reuse it.

Cheers,

Michael


---

Comment by jason created at 2010-03-17 05:09:43

Changing type from defect to enhancement.
