# Issue 2662: simplify_full function

Issue created by migration from https://trac.sagemath.org/ticket/2662

Original creator: jason

Original creation time: 2008-03-24 21:18:35

Assignee: was

Create a simplify_full function that (somewhat intelligently?) applies a battery simplifications to try to get a function to be simpler.  

It would be nice to support some of the options that FullSimplify in Mma has (see http://reference.wolfram.com/mathematica/ref/FullSimplify.html?q=fullsimplify&lang=en ):

 * user can pass in a "complexity function" which determines how simple an expression is
 * user can pass in a time limit for the simplification
 * user can pass in a list of things that won't be simplified
 * etc.



---

Comment by jason created at 2008-03-24 21:27:50

mhansen created a simplify_full function in #2661.  So how about this ticket is the enhancement ticket for putting the Mma options that we can into full_simplify.


---

Comment by gfurnish created at 2008-03-25 00:39:11

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-25 00:39:11

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-25 00:39:38

This definately *has* to be handled better in new symbolics then it is currently.


---

Comment by kcrisman created at 2009-12-30 04:01:47

Note also there are several other open tickets about the various simplify functions, with no resolution yet on what our "real" options should be.


---

Comment by jason created at 2012-12-04 16:57:46

#13099 is related.
