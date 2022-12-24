# Issue 2400: maxima automatically simplifies floats to rationals

archive/issues_002400.json:
```json
{
    "body": "Assignee: was\n\n\n```\nI tried doing some integrals today and the output doesn't make much  \nsense to me:\n\nsage: f = e^(-x2)\nsage: f.integrate(x, 0, 0.1)\n2066*sqrt(pi)/36741\nsage: f.integrate(x, 0, 1/10)\nsqrt(pi)*erf(1/10)/2\n\nHmmmm. Does this mean erf(1/10) is a rational number? That's a little  \nsurprising to me. In fact:\n\nsage: RR(f.integrate(x, 0, 0.1))\n0.0996676643523801\nsage: RR(f.integrate(x, 0, 1/10))\n0.0996676642903363\n\nWhat's going on here?\n\ndavid\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2400\n\n",
    "created_at": "2008-03-06T00:44:39Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "maxima automatically simplifies floats to rationals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2400",
    "user": "jason"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/2400





---

archive/issue_comments_016200.json:
```json
{
    "body": "Following a lead from the mailing list, I added \"keepfloat: true\" to the init_code for the maxima interfaces.  The patch is attached.",
    "created_at": "2008-03-06T00:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16200",
    "user": "jason"
}
```

Following a lead from the mailing list, I added "keepfloat: true" to the init_code for the maxima interfaces.  The patch is attached.



---

archive/issue_comments_016201.json:
```json
{
    "body": "Jason, please improve the comment \"# no ascii art output\" to indicate what the new flag does.",
    "created_at": "2008-03-06T01:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16201",
    "user": "dmharvey"
}
```

Jason, please improve the comment "# no ascii art output" to indicate what the new flag does.



---

archive/issue_comments_016202.json:
```json
{
    "body": "Attachment [keepfloat.patch](tarball://root/attachments/some-uuid/ticket2400/keepfloat.patch) by jason created at 2008-03-06 01:38:50\n\nI replaced the patch with an updated one addressing dmharvey's concerns.  The patch is ready to be reviewed again.",
    "created_at": "2008-03-06T01:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16202",
    "user": "jason"
}
```

Attachment [keepfloat.patch](tarball://root/attachments/some-uuid/ticket2400/keepfloat.patch) by jason created at 2008-03-06 01:38:50

I replaced the patch with an updated one addressing dmharvey's concerns.  The patch is ready to be reviewed again.



---

archive/issue_comments_016203.json:
```json
{
    "body": "This patch fails doctests on\n\n`sage -t  devel/sage-2400/sage/matrix/matrix_symbolic_dense.pyx`\n\n(There might be more; I don't know, I killed it.)",
    "created_at": "2008-03-06T02:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16203",
    "user": "dmharvey"
}
```

This patch fails doctests on

`sage -t  devel/sage-2400/sage/matrix/matrix_symbolic_dense.pyx`

(There might be more; I don't know, I killed it.)



---

archive/issue_comments_016204.json:
```json
{
    "body": "The code itself is fine but symbolic matrices with keepfloat appear to be broken in Maxima.  When/if symbolic matrices do not use maxima this will be a good patch.  \n\n\n```\n    TypeError: Error executing code in Maxima\n    CODE:\n    \tsage173 : matrixexp(sage172)$\n    Maxima ERROR:\n    \t\n    `rat' replaced 1.0 by 1/1 = 1.0\n    \n    `rat' replaced -5.2 by -26/5 = -5.2\n    \n    `rat' replaced -12.0 by -12/1 = -12.0\n    \n    `rat' replaced 2.0 by 2/1 = 2.0\n    \n    `rat' replaced -5.2 by -26/5 = -5.2\n    \n    `rat' replaced 5.0 by 5/1 = 5.0\n    \n    `rat' replaced -26.0 by -26/1 = -26.0\n    \n    `rat' replaced -60.0 by -60/1 = -60.0\n    \n    `rat' replaced 10.0 by 10/1 = 10.0\n    \n    `rat' replaced -26.0 by -26/1 = -26.0\n    \n    `rat' replaced -12.0 by -12/1 = -12.0\n    \n    `rat' replaced -5.2 by -26/5 = -5.2\n    \n    `rat' replaced 1.0 by 1/1 = 1.0\n    Unable to find the spectral representation\n     \n```\n",
    "created_at": "2008-03-10T14:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16204",
    "user": "gfurnish"
}
```

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

archive/issue_comments_016205.json:
```json
{
    "body": "The matrixexp command seems to work fine in maxima (see below).  How do you reproduce your error?  (can you give a short sage session that gives the error above?)\n\n\n```\nsage: maxima.interact()\n\n  --> Switching to Maxima <--\n\nmaxima: keepfloat: true\ntrue\nmaxima: matrixexp(matrix([x,1],[1,x]));\nmatrix([(%e^2+1)*%e^(x-1)/2,(%e^2-1)*%e^(x-1)/2],[(%e^2-1)*%e^(x-1)/2,(%e^2+1)*%e^(x-1)/2])\nmaxima: keepfloat: false\nfalse\nmaxima: matrixexp(matrix([x,1],[1,x]));\nmatrix([(%e^2+1)*%e^(x-1)/2,(%e^2-1)*%e^(x-1)/2],[(%e^2-1)*%e^(x-1)/2,(%e^2+1)*%e^(x-1)/2])\nmaxima: keepfloat: false\nfalse\nmaxima: matrixexp(matrix([3,1],[1,2]));\nmatrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])\nmaxima: keepfloat: true\ntrue\nmaxima: matrixexp(matrix([3,1],[1,2]));\nmatrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])\n```\n",
    "created_at": "2008-03-10T17:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16205",
    "user": "jason"
}
```

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

archive/issue_comments_016206.json:
```json
{
    "body": "Here is a way to reproduce the above error:\n\n\n```\nmaxima: keepfloat: true\ntrue\nmaxima: matrixexp(matrix([3.0,1.0],[1.0,2.0]));\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py in sage_prefilter(self, block, continuation)\n    406         for i in range(len(B)):\n    407             L = B[i]\n--> 408             M = do_prefilter_paste(L, continuation or (not first))\n    409             first = False\n    410             # The L[:len(L)-len(L.lstrip())]  business here preserves\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py in do_prefilter_paste(line, continuation)\n    347\n    348     if len(line) > 0:\n--> 349         line = preparser_ipython.preparse_ipython(line, not continuation)\n    350     return line\n    351\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/preparser_ipython.py in preparse_ipython(line, reset)\n    104         # TODO: do sage substitutions here\n    105         #t = interface._eval_line(line)\n--> 106         t = interface.eval(line)\n    107\n    108     import sage.misc.interpreter\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)\n    712             raise\n    713         except TypeError, s:\n--> 714             raise TypeError, 'error evaluating \"%s\":\\n%s'%(code,s)\n    715\n    716     def execute(self, *args, **kwds):\n\n<type 'exceptions.TypeError'>: error evaluating \"matrixexp(matrix([3.0,1.0],[1.0,2.0]));\":\nError executing code in Maxima\nCODE:\n        matrixexp(matrix([3.0,1.0],[1.0,2.0]));\nMaxima ERROR:\n\n`rat' replaced 1.0 by 1/1 = 1.0\n\n`rat' replaced -5.0 by -5/1 = -5.0\n\n`rat' replaced 5.0 by 5/1 = 5.0\n\n`rat' replaced 2.0 by 2/1 = 2.0\n\n`rat' replaced -5.0 by -5/1 = -5.0\n\n`rat' replaced 1.0 by 1/1 = 1.0\n\n`rat' replaced -5.0 by -5/1 = -5.0\n\n`rat' replaced 5.0 by 5/1 = 5.0\n\n`rat' replaced 2.0 by 2/1 = 2.0\n\n`rat' replaced -5.0 by -5/1 = -5.0\n\n`rat' replaced 5.0 by 5/1 = 5.0\n\n`rat' replaced -5.0 by -5/1 = -5.0\n\n`rat' replaced 1.0 by 1/1 = 1.0\nUnable to find the spectral representation\n\n\nmaxima: keepfloat: false\nfalse\nmaxima: matrixexp(matrix([3.0,1.0],[1.0,2.0]));\nmatrix([%e^(5/2-sqrt(5)/2)*((sqrt(5)+5)*%e^sqrt(5)-sqrt(5)+5)/10,%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5],[%e^(5/2-sqrt(5)/2)*(sqrt(5)*%e^sqrt(5)-sqrt(5))/5,-%e^(5/2-sqrt(5)/2)*((sqrt(5)-5)*%e^sqrt(5)-sqrt(5)-5)/10])\nmaxima:\n```\n",
    "created_at": "2008-03-10T17:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16206",
    "user": "jason"
}
```

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

archive/issue_comments_016207.json:
```json
{
    "body": "This post talks about the weakness of the maxima linear algebra functionality and explicitly includes the above error: http://www.ma.utexas.edu/pipermail/maxima/2006/003031.html",
    "created_at": "2008-03-10T17:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16207",
    "user": "jason"
}
```

This post talks about the weakness of the maxima linear algebra functionality and explicitly includes the above error: http://www.ma.utexas.edu/pipermail/maxima/2006/003031.html



---

archive/issue_comments_016208.json:
```json
{
    "body": "The last post at http://www.nabble.com/matrix-exponential--td6816907.html suggests using the \"diag\" package instead of the \"linearalgebra\" package for calculating the matrix exponential.  This works with keepfloat:\n\n\n```\nsage: maxima.interact()\n\n  --> Switching to Maxima <--\n\nmaxima: keepfloat: true\ntrue\nmaxima: load(\"diag\")\n?\\/home\\/grout\\/sage\\/local\\/share\\/maxima\\/5\\.13\\.0\\/share\\/contrib\\/diag\\.mac\nmaxima: mat_function(exp,matrix([3.0,1.0],[1.0,2.0]));\nmatrix([(sqrt(5)+1)*%e^((sqrt(5)+5)/2)/(2*sqrt(5))+(sqrt(5)-1)*%e^-((sqrt(5)-5)/2)/(2*sqrt(5)),%e^((sqrt(5)+5)/2)/sqrt(5)-%e^-((sqrt(5)-5)/2)/sqrt(5)],[%e^((sqrt(5)+5)/2)/sqrt(5)-%e^-((sqrt(5)-5)/2)/sqrt(5),2*%e^((sqrt(5)+5)/2)/(sqrt(5)*(sqrt(5)+1))+2*%e^-((sqrt(5)-5)/2)/(sqrt(5)*(sqrt(5)-1))])\n```\n",
    "created_at": "2008-03-10T17:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16208",
    "user": "jason"
}
```

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

archive/issue_comments_016209.json:
```json
{
    "body": "The maxima matrixexp function has problems with floating point entries.  I don't think that should keep us from fixing *wrong* output (or at least, unnecessarily rounded) from maxima due to their rounding floating points to rationals.\n\nI've attached a patch which works around the problems in the matrixexp function by specifying keepfloat: false for that one command.  I've also added a note talking about maxima automatically rounding floating point numbers to the docstring for matrixexp.",
    "created_at": "2008-03-10T19:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16209",
    "user": "jason"
}
```

The maxima matrixexp function has problems with floating point entries.  I don't think that should keep us from fixing *wrong* output (or at least, unnecessarily rounded) from maxima due to their rounding floating points to rationals.

I've attached a patch which works around the problems in the matrixexp function by specifying keepfloat: false for that one command.  I've also added a note talking about maxima automatically rounding floating point numbers to the docstring for matrixexp.



---

archive/issue_comments_016210.json:
```json
{
    "body": "Attachment [matrixexp-keepfloat.patch](tarball://root/attachments/some-uuid/ticket2400/matrixexp-keepfloat.patch) by jason created at 2008-03-10 19:35:09\n\napply on top of  keepfloat.patch",
    "created_at": "2008-03-10T19:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16210",
    "user": "jason"
}
```

Attachment [matrixexp-keepfloat.patch](tarball://root/attachments/some-uuid/ticket2400/matrixexp-keepfloat.patch) by jason created at 2008-03-10 19:35:09

apply on top of  keepfloat.patch



---

archive/issue_comments_016211.json:
```json
{
    "body": "These two patches apply against 2.10.4.alpha0, fix the problems, and pass tests for me.",
    "created_at": "2008-03-15T21:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16211",
    "user": "mhansen"
}
```

These two patches apply against 2.10.4.alpha0, fix the problems, and pass tests for me.



---

archive/issue_comments_016212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T02:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16212",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016213.json:
```json
{
    "body": "Merged both patches in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T02:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16213",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.4.rc0



---

archive/issue_comments_016214.json:
```json
{
    "body": "For some reason this hack doesn't work anymore in Maxima 5.30, see #13973.",
    "created_at": "2013-06-18T18:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2400#issuecomment-16214",
    "user": "kcrisman"
}
```

For some reason this hack doesn't work anymore in Maxima 5.30, see #13973.
