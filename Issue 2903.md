# Issue 2903: [with spkg + patch, needs review] make NTL error messages propagate to RuntimeError messages

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-13 02:55:37

Assignee: cwitty

The spkg and patch achieve the following:

 * add a mechanism to NTL for setting a callback, so that when NTL calls its `Error()` function, the callback is called instead of printing an error message to stderr and abort()-ing

 * use this mechanism in Sage to propagate NTL's error messages back to a `RuntimeError` with a message. This means that instead of crashing to the command line, the user lands back at the sage prompt.

It would be nice if the NTL modifications were accepted upstream.

Obviously this solution is suboptimal, since it will very likely cause memory leaks. But memory leaks are better than crashing to the command line (well, that's debatable I suppose....). But the only way to fix this would be a major rewrite of lots of NTL to implement saner error propagation.



---

Comment by dmharvey created at 2008-04-13 02:58:59

spkg was too big, trac didn't like it.

Here it is instead:

http://sage.math.washington.edu/home/dmharvey/ntl-5.4.2.p1.spkg


---

Attachment


---

Comment by mabshoff created at 2008-04-17 19:49:23

The spkg as well as the patch looks good to me. I added patches of the changed files to the patches directory, so that external packages have an easier time updating the source.

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-17 20:06:50

Merged in Sage 3.0.alpha6


---

Comment by mabshoff created at 2008-04-17 20:06:50

Resolution: fixed
