# Issue 4971: make get_memory_usage() return a float on all platforms

Issue created by migration from https://trac.sagemath.org/ticket/4971

Original creator: mabshoff

Original creation time: 2009-01-14 02:01:27

Assignee: cwitty

From http://groups.google.com/group/sage-support/t/58b8f491e4906f71

```
If you know the limitations of get_memory_usage() you can work 
around them. Case in point from 3.2.3 right after startup: 

64 bit linux, i.e. sage.math: 
sage: get_memory_usage() 
668.32421875 
---- 
32 bit OSX 10.5: 
sage: get_memory_usage() 
'131M+' 
---- 
64 bit OSX 10.5: 
sage: get_memory_usage() 
'171M+' 
--- 
32 bit Solaris/Sparc: 
sage: get_memory_usage() 
'81M' 

While there should be a difference between 32 and 64 bit, i.e 64 bit 
code is larger and consumes more memory, the result from Linux is not 
even close to the truth, i.e. I don't think 32 bit Solaris is roughly 
a magnitude more efficient than 64 bit Linux. 
Either way, the result of get_memory_usage() should be consistent 
across platforms and not return a string in some cases and something 
else on Linux. It should be a float of the memory used in MB. 
```

William then replied:

```
+1  Create a trac ticket.  This will be an easy point for the 
"fix-the-most-trac-bugs-in-sage contest we're having next week. 
```



---

Attachment


---

Comment by mabshoff created at 2009-01-24 16:20:27

Nice. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 17:14:20

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 17:14:20

Resolution: fixed
