# Issue 4161: [with spkg, needs review] GAP doesn't compile with CXX='ccache g++'

Issue created by migration from https://trac.sagemath.org/ticket/4161

Original creator: mabshoff

Original creation time: 2008-09-20 23:01:41

Assignee: mabshoff

This is a follow up to #2575 where accidentally we only fixed on problem and not the other. The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/gap-4.4.10.p10.spkg

Cheers,

Michael 


---

Comment by mabshoff created at 2008-09-20 23:01:48

Changing status from new to assigned.


---

Comment by schilly created at 2008-09-20 23:23:07

the spkg works for me with set CC and CXX env vars.


---

Comment by mabshoff created at 2008-09-20 23:24:10

Resolution: fixed


---

Comment by mabshoff created at 2008-09-20 23:24:10

Merged in Sage 3.1.3.alpha1


---

Comment by leif created at 2012-03-22 18:23:52

See #7041 for a follow-up.
