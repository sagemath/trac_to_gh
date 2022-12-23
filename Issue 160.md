# Issue 160: partitions -- sage dies

Issue created by migration from https://trac.sagemath.org/ticket/160

Original creator: was

Original creation time: 2006-10-29 02:00:44

Assignee: was


```
 
 
On Oct 28, 2006, at 12:28 , David Joyner wrote:
 
>  
> Hi:
>  
> Here's an odd bug:
>  
> sage: n = 15
> sage: time  P = partitions_set(range(n),3)
> /home/wdj/sagefiles/sage-1.4.1/local/bin/sage-sage: line 163: 22761
> Killed                  sage-ipython -c "$SAGE_STARTUP_COMMAND;" $*
> wdj@wooster:~/sagefiles/sage-1.4.1>
 
Looks like a Gap or Python runaway problem.  On Mac OS X, SAGE  
doesn't die, but I get this:
=========================================
sage.bin(25351) malloc: *** vm_allocate(size=1069056) failed (error  
code=3)
sage.bin(25351) malloc: *** error: can't allocate region
sage.bin(25351) malloc: *** set a breakpoint in szone_error to debug
------------------------------------------------------------------------ 
---
<type 'exceptions.MemoryError'>           Traceback (most recent call  
last)
 
/SandBox/Justin/sb/Sage/<ipython console> in <module>()
 
/SandBox/Justin/sb/sage-1.4/local/lib/python2.5/site-packages/IPython/ 
iplib.py in ipmagic(self, arg_s)
     899         else:
     900             magic_args = self.var_expand(magic_args)
--> 901             return fn(magic_args)
     902
     903     def ipalias(self,arg_s):
 
/SandBox/Justin/sb/sage-1.4/local/lib/python2.5/site-packages/IPython/ 
Magic.py in magic_time(self, parameter_s)
    1761         else:
    1762             st = clk()
-> 1763             exec code in glob
    1764             end = clk()
    1765             out = None
 
/SandBox/Justin/sb/Sage/<timed exec> in <module>()
 
/SandBox/Justin/sb/sage-1.4/local/lib/python2.5/site-packages/sage/ 
combinat/combinat.py in partitions_set(S, k)
     908     else:
     909         ans=gap.eval("PartitionsSet(%s,%s)"%(S,k))
--> 910     return eval(ans)
     911
     912 def number_of_partitions_set(S,k):
 
<type 'exceptions.MemoryError'>:
=========================================
 
where the three malloc error messages are repeated an infinite number  
of times (i.e., it blew out the scroll-back buffer for this window  
(10,000 lines).  PID 25351 is 'python' (from sage.bin).
 
Justin
 
--
Justin C. Walker, Curmudgeon at Large

 
```



---

Comment by was created at 2007-01-13 00:53:26

Changing type from defect to enhancement.


---

Comment by was created at 2007-01-13 00:53:26

This is Python running out of memory trying to read out a *MASSIVE* string
from GAP.  A solution would involve using files to communicate such huge
data.  That's a NotImplemented issue.  I'm changing this to an enhacement, 
since it's not a bug, but a reflection of a general issue. 

ENHANCEMENT: Make it much easier to get huge data out of systems,
e.g., the eval method and str methods of interface objects should
easily be extractable via a file.


---

Comment by was created at 2007-08-19 09:31:39

Resolution: fixed


---

Comment by was created at 2007-08-19 09:31:39

Fixed by using files to move data.


---

Attachment
