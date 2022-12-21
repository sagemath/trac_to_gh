# Issue 2400: maxima automatically simplifies floats to rationals

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-06 00:44:39

Assignee: was


```
I tried doing some integrals today and the output doesn't make much  
sense to me:

sage: f = e^(-x2)
sage: f.integrate(x, 0, 0.1)
2066*sqrt(pi)/36741
sage: f.integrate(x, 0, 1/10)
sqrt(pi)*erf(1/10)/2

Hmmmm. Does this mean erf(1/10) is a rational number? That's a little  
surprising to me. In fact:

sage: RR(f.integrate(x, 0, 0.1))
0.0996676643523801
sage: RR(f.integrate(x, 0, 1/10))
0.0996676642903363

What's going on here?

david
```




---

Comment by jason created at 2008-03-06 00:45:29

Following a lead from the mailing list, I added "keepfloat: true" to the init_code for the maxima interfaces.  The patch is attached.


---

Comment by dmharvey created at 2008-03-06 01:26:32

Jason, please improve the comment "# no ascii art output" to indicate what the new flag does.


---

Attachment

I replaced the patch with an updated one addressing dmharvey's concerns.  The patch is ready to be reviewed again.


---

Comment by dmharvey created at 2008-03-06 02:52:58

This patch fails doctests on

`sage -t  devel/sage-2400/sage/matrix/matrix_symbolic_dense.pyx`

(There might be more; I don't know, I killed it.)


---

Comment by gfurnish created at 2008-03-10 14:31:58

The code itself is fine but symbolic matrices with keepfloat appear to be broken in Maxima.  When/if symbolic matrices do not use maxima this will be a good patch.  


```
    TypeError: Error executing code in Maxima
    CODE:
    	sage173 : matrixexp(sage172)$
    Maxima ERROR:
    	
    `rat' replaced 1.0 by 1/1 = 1.0
    
    `rat' replaced -5.2 by -26/5 = -5.2
    
    `rat' replaced -12.0 by -12/1 = -12.0
    
    `rat' replaced 2.0 by 2/1 = 2.0
    
    `rat' replaced -5.2 by -26/5 = -5.2
    
    `rat' replaced 5.0 by 5/1 = 5.0
    
    `rat' replaced -26.0 by -26/1 = -26.0
    
    `rat' replaced -60.0 by -60/1 = -60.0
    
    `rat' replaced 10.0 by 10/1 = 10.0
    
    `rat' replaced -26.0 by -26/1 = -26.0
    
    `rat' replaced -12.0 by -12/1 = -12.0
    
    `rat' replaced -5.2 by -26/5 = -5.2
    
    `rat' replaced 1.0 by 1/1 = 1.0
    Unable to find the spectral representation
     
```



---

Comment by jason created at 2008-03-10 17:23:23

The matrixexp command seems to work fine in maxima (see below).  How do you reproduce your error?  (can you give a short sage session that gives the error above?)


```
sage: maxima.interact()

  --> Switching to Maxima <--

maxima: keepfloat: true
true
maxima: matrixexp(matrix([x,1],[1,x]));
matrix([(%e^2+1)*%e^(x-1)/2,(%e^2-1)*%e^(x-1)/2],[(%e^2-1)*%e^(x-1)/2,(%e^2+1)*%e^(x-1)/2])
maxima: keepfloat: false
false
maxima: matrixexp(matrix([x,1],[1,x]));
matrix([(%e^2+1)*%e^(x-1)/2,(%e^2-1)*%e^(x-1)/2],[(%e^2-1)*%e^(x-1)/2,(%e^2+1)*%e^(x-1)/2])
maxima: keepfloat: false
false
maxima: matrixexp(matrix([3,1],[1,2]));
matrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])
maxima: keepfloat: true
true
maxima: matrixexp(matrix([3,1],[1,2]));
matrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])
```



---

Comment by jason created at 2008-03-10 17:27:27

Here is a way to reproduce the above error:


```
maxima: keepfloat: true
true
maxima: matrixexp(matrix([3.0,1.0],[1.0,2.0]));
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)
    406         for i in range(len(B)):
    407             L = B[i]
--> 408             M = do_prefilter_paste(L, continuation or (not first))
    409             first = False
    410             # The L[:len(L)-len(L.lstrip())]  business here preserves

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py in do_prefilter_paste(line, continuation)
    347
    348     if len(line) > 0:
--> 349         line = preparser_ipython.preparse_ipython(line, not continuation)
    350     return line
    351

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/preparser_ipython.py in preparse_ipython(line, reset)
    104         # TODO: do sage substitutions here
    105         #t = interface._eval_line(line)
--> 106         t = interface.eval(line)
    107
    108     import sage.misc.interpreter

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    712             raise
    713         except TypeError, s:
--> 714             raise TypeError, 'error evaluating "%s":\n%s'%(code,s)
    715
    716     def execute(self, *args, **kwds):

<type 'exceptions.TypeError'>: error evaluating "matrixexp(matrix([3.0,1.0],[1.0,2.0]));":
Error executing code in Maxima
CODE:
        matrixexp(matrix([3.0,1.0],[1.0,2.0]));
Maxima ERROR:

`rat' replaced 1.0 by 1/1 = 1.0

`rat' replaced -5.0 by -5/1 = -5.0

`rat' replaced 5.0 by 5/1 = 5.0

`rat' replaced 2.0 by 2/1 = 2.0

`rat' replaced -5.0 by -5/1 = -5.0

`rat' replaced 1.0 by 1/1 = 1.0

`rat' replaced -5.0 by -5/1 = -5.0

`rat' replaced 5.0 by 5/1 = 5.0

`rat' replaced 2.0 by 2/1 = 2.0

`rat' replaced -5.0 by -5/1 = -5.0

`rat' replaced 5.0 by 5/1 = 5.0

`rat' replaced -5.0 by -5/1 = -5.0

`rat' replaced 1.0 by 1/1 = 1.0
Unable to find the spectral representation


maxima: keepfloat: false
false
maxima: matrixexp(matrix([3.0,1.0],[1.0,2.0]));
matrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])
maxima:
```



---

Comment by jason created at 2008-03-10 17:29:13

This post talks about the weakness of the maxima linear algebra functionality and explicitly includes the above error: http://www.ma.utexas.edu/pipermail/maxima/2006/003031.html


---

Comment by jason created at 2008-03-10 17:39:15

The last post at http://www.nabble.com/matrix-exponential--td6816907.html suggests using the "diag" package instead of the "linearalgebra" package for calculating the matrix exponential.  This works with keepfloat:


```
sage: maxima.interact()

  --> Switching to Maxima <--

maxima: keepfloat: true
true
maxima: load("diag")
?\/home\/grout\/sage\/local\/share\/maxima\/5\.13\.0\/share\/contrib\/diag\.mac
maxima: mat_function(exp,matrix([3.0,1.0],[1.0,2.0]));
matrix([(sqrt(5)+1)*%e^((sqrt(5)+5)/2)/(2*sqrt(5))+(sqrt(5)-1)*%e^-((sqrt(5)-5)/2)/(2*sqrt(5)),%e^((sqrt(5)+5)/2)/sqrt(5)-%e^-((sqrt(5)-5)/2)/sqrt(5)],[%e^((sqrt(5)+5)/2)/sqrt(5)-%e^-((sqrt(5)-5)/2)/sqrt(5),2*%e^((sqrt(5)+5)/2)/(sqrt(5)*(sqrt(5)+1))+2*%e^-((sqrt(5)-5)/2)/(sqrt(5)*(sqrt(5)-1))])
```



---

Comment by jason created at 2008-03-10 19:34:25

The maxima matrixexp function has problems with floating point entries.  I don't think that should keep us from fixing *wrong* output (or at least, unnecessarily rounded) from maxima due to their rounding floating points to rationals.

I've attached a patch which works around the problems in the matrixexp function by specifying keepfloat: false for that one command.  I've also added a note talking about maxima automatically rounding floating point numbers to the docstring for matrixexp.


---

Attachment

apply on top of  keepfloat.patch


---

Comment by mhansen created at 2008-03-15 21:45:50

These two patches apply against 2.10.4.alpha0, fix the problems, and pass tests for me.


---

Comment by mabshoff created at 2008-03-16 02:48:45

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 02:48:45

Merged both patches in Sage 2.10.4.rc0


---

Comment by kcrisman created at 2013-06-18 18:22:54

For some reason this hack doesn't work anymore in Maxima 5.30, see #13973.
