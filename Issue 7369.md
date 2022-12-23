# Issue 7369: Split graph.py into several files

Issue created by migration from https://trac.sagemath.org/ticket/7369

Original creator: ncohen

Original creation time: 2009-11-01 15:34:19

Assignee: rlm

The file graph.py should be split into several files in next release. I am thinking about creating 3 files :
   * generic_graph.py
   * graph.py
   * digraph.py
But it is likely many of you will have better ideas. Regardless of what is chosen, this is getting urgent as the best moment to do it is just before releasing a new version, just after all the patches for graph.py have been merged.


---

Comment by was created at 2009-11-11 17:45:24

Why was this made a defect?  a blocker??  I'm changing it to not be a blocker or defect.


---

Comment by was created at 2009-11-11 17:45:24

Changing priority from blocker to major.


---

Comment by was created at 2009-11-11 17:45:24

Changing type from defect to enhancement.


---

Comment by ncohen created at 2009-11-11 19:16:28

I set it to "blocker" because it had to be done just before releasing. It is not easy to split a file in two if there are patches to be applied on this very file, so I thought the best way would be to take care of this just before releasing, thus setting it as a blocker to avoid it being forgotten, as it will most probably be done by the release manager ! :-)

What's your advice ???

Nathann


---

Comment by was created at 2009-11-12 00:04:21

To me, blocker = high priority ticket that we *have* to close before making the next release of Sage.     I don't think refactoring code ever satisfies that criterion. 

I think you should set this as an enhancement then work with the release manager (and post to sage-release) to do the refactoring once you're sure about what you want to do.  

 -- william


---

Comment by ncohen created at 2009-12-17 16:24:51

Copy of #7634


---

Comment by ncohen created at 2009-12-17 16:24:51

Resolution: duplicate
