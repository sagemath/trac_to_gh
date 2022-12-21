# Issue 9949: Change Brian package from experimental to optional

Issue created by migration from Trac.

Original creator: uri

Original creation time: 2010-09-19 17:51:10

Assignee: tbd

CC:  kcrisman

Keywords: brian brain simulator neuronal dynamics

Brian, a simulator for spiking neural networks, has been recently accepted as an experimental package (see ticket [#9675](http://trac.sagemath.org/sage_trac/ticket/9675) and [Brian's webage](http://www.briansimulator.org/)). In this ticket, it has been suggested the possibility to change it to an optional package. However, at least it should be tested in some different platforms.

Code can be downloaded by clicking [here](http://code.google.com/p/spkg-upload/downloads/detail?name=brian-1.2.1.p0.spkg&can=2&q=) or at Sage's experimental packages page: [http://www.sagemath.org/packages/experimental/](http://www.sagemath.org/packages/experimental/).


---

Comment by uri created at 2010-09-19 18:00:25

Brian has built-in tests, but they need nose to run. Ticket [#9921](http://trac.sagemath.org/sage_trac/ticket/9921) is precisely about adding nose as an optional/standard package; I installed the package provided there and runned Brian's tests by writing:

[[[
sage: import brian
sage: brian.test()
]]]

and all of them were passed. However, I didn't do an SPKG-TEST file because nose is not part of Sage yet.


---

Comment by kcrisman created at 2010-09-20 20:08:19

Works fine on OS X 10.4 PPC!  

116 tests, zero errors, zero failures.


---

Comment by kcrisman created at 2010-09-20 20:43:16

Same on OS X 10.6.


---

Comment by kcrisman created at 2012-05-26 20:14:29

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-05-26 20:14:29

This should be accepted.  It still works fine, installs fine.  Granted, perhaps one can do this without an spkg, but why not have it?

By the way, Brian is now in version 1.3.1, but that is a different issue.


---

Comment by kcrisman created at 2012-05-26 20:15:02

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-05-26 20:17:11

Also ok on sage.math.


---

Comment by kcrisman created at 2012-05-26 20:17:31

Changing keywords from "brian brain simulator neuronal dynamics" to "brian brain simulator neuronal dynamics sd40.5".


---

Comment by schilly created at 2012-06-11 20:34:50

spkg moved to optional


---

Comment by jdemeyer created at 2012-06-12 08:15:34

Resolution: fixed
