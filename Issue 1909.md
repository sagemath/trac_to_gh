# Issue 1909: Create a "partition" function like Mathematica has

Issue created by migration from https://trac.sagemath.org/ticket/1909

Original creator: jason

Original creation time: 2008-01-24 13:33:36

Assignee: cwitty

CC:  sage-combinat


```
Thanks.  I would actually strongly encourage you or somebody to
sit down and actually write a function that has the _same_ functionality
as http://reference.wolfram.com/mathematica/ref/Partition.html
since that looks like a very useful function, and I think having it
trivially available in Sage will be very useful to people used to
Mathematica or people porting Mathematica code to Sage.
I hope people will implement something with the same interface and
submit a patch.

 -- William
```


and 


```
Let me be the first of many  ;-)  to say that's maybe more efficient to
use a temporary variable for the padding:

def partition(v,n,pad=0):
    t=(v+[pad]*(n-len(v)%n))
    return [t[i:i+n] for i in range(0,len(v),n)]


-vgermrk-
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/64de09db029abe43




---

Comment by mabshoff created at 2008-03-16 08:10:57

Changing assignee from cwitty to mhansen.


---

Comment by mabshoff created at 2008-03-16 08:10:57

Changing component from misc to combinatorics.


---

Comment by AlexGhitza created at 2009-01-22 18:23:18

Changing type from defect to enhancement.
