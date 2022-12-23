# Issue 6249: graph1.plot() + graph2.plot() doesn't zorder correctly

Issue created by migration from https://trac.sagemath.org/ticket/6249

Original creator: ncalexan

Original creation time: 2009-06-08 16:25:31

Assignee: rlm

CC:  ekirkman rlm kcrisman

Keywords: graph plot z order overlay

Let G1 and G2 be arbitrary graphs.  G1.plot() + G2.plot() and G2.plot() + G1.plot() (notice the ordering) look the same for me, ie I cannot make one graph appear above the other.  What seems to happen is that the vertices are brought forward in the zorder, but it appears that this is done globally, not locally for the individual plot.  I claim this is a bug.


---

Comment by mhampton created at 2009-06-11 19:28:57

I'd just like to add that this bothers me too.  I once tried to fix it and got confused and gave up.


---

Comment by vbraun created at 2009-10-08 19:10:30

I disagree. If you do not specify the z-order then there is no good way of automatically figuring out what to do. Amongst the multitude of possible behaviours you could even argue that G1.plot() + G2.plot() and G2.plot() + G1.plot() should be the same as addition is commutative. 

Just do G1.plot(zorder=0) + G2.plot(zorder=1) or vice versa if you care about the z-ordering. 

I recommend to close this bug.


---

Comment by kcrisman created at 2010-06-23 13:50:37

Changing component from graph theory to graphics.


---

Comment by kcrisman created at 2010-06-23 13:50:37

Changing priority from major to minor.


---

Comment by kcrisman created at 2011-06-02 03:36:42

#3251 seems to be related, though perhaps not a dup.
