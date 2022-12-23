# Issue 4285: [with patch, needs review] update desolver interface

Issue created by migration from https://trac.sagemath.org/ticket/4285

Original creator: robertwb

Original creation time: 2008-10-14 17:39:28

Assignee: burcin

CC:  mhansen

The current interface takes and returns raw maxima strings, and doesn't do any error handling. This gives the desolver a much more sage-like interface. 


---

Comment by robertwb created at 2008-10-14 20:29:21

The last patch fixes some documentation.


---

Comment by wdj created at 2008-10-14 20:59:56

Using 3.1.3.alpha3, I got this:


```
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.2.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.2.patch"
applying /home/wdj/sagefiles/4285-desolver.2.patch
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.3.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.alpha3/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.3.patch"
applying /home/wdj/sagefiles/4285-desolver.3.patch
patching file sage/calculus/desolvers.py
Hunk #1 FAILED at 20
Hunk #2 FAILED at 33
Hunk #3 FAILED at 151
Hunk #4 FAILED at 161
Hunk #5 FAILED at 172
5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej
abort: patch failed to apply
```



---

Comment by robertwb created at 2008-10-14 21:01:19

Hm.... it's based on 3.1.3.rc0.


---

Comment by wdj created at 2008-10-14 21:07:26

Okay, I'll have to rebuild 3.1.3.rc0, which will take awhile.
But this:


```
sage: t = var('t')
sage: x = function('x', t)
sage: de = lambda y: diff(y,t) + y - 1
sage: desolve(de(x(t)),[x,t])
e^(-t)*(e^t + c)
sage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f
e^(-t)*(e^t + e^10)
sage: plot(f)
```


is absolutely fantastic. So far, this is great! Thanks very much Robert. 

I'll do more testing in a few hours...


---

Comment by wdj created at 2008-10-15 01:38:36

This is a newly built clone of 3.1.3.rc0:


```
wdj@hera:~/sagefiles/sage-3.1.3.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: desolve
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.2.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.2.patch"
applying /home/wdj/sagefiles/4285-desolver.2.patch
sage: hg_sage.apply("/home/wdj/sagefiles/4285-desolver.3.patch")
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.3.rc0/devel/sage" && hg import   "/home/wdj/sagefiles/4285-desolver.3.patch"
applying /home/wdj/sagefiles/4285-desolver.3.patch
patching file sage/calculus/desolvers.py
Hunk #1 FAILED at 20
Hunk #2 FAILED at 33
Hunk #3 FAILED at 151
Hunk #4 FAILED at 161
Hunk #5 FAILED at 172
5 out of 5 hunks FAILED -- saving rejects to file sage/calculus/desolvers.py.rej
abort: patch failed to apply
```

| SAGE Version 3.1.3.rc0, Release Date: 2008-10-12                   |
| Type notebook() for the GUI, and license() for information.        |
Just to be clear, I am to apply patch 2 then patch 3?


---

Comment by zimmerma created at 2008-10-15 07:16:35

> Just to be clear, I am to apply patch 2 then patch 3?

I guess no. The two patches are of the same size. Just apply one of them.


---

Comment by zimmerma created at 2008-10-15 07:29:03

I made a review of this patch (tested against 3.1.2) and it is positive, here are my remarks:

One issue is that in the 2nd desolve example, one would prefer y(10) to be
substituted by the initial condition y(10)=2 in the output, but this is still
better than previously, and as Robert told me there is no point in investing
too much in this if maxima is replaced by something else.

ics   -- (optional) the initial or boundary conditions (hereafter called x)
-> shouldn't "hereafter called x" be removed?

I see a few typos:
(in)dependant -> (in)dependent?
differeintial -> differential
if there more -> if there is more (twice)
variabe -> variable


---

Attachment

apply only this last patch


---

Comment by robertwb created at 2008-10-15 10:11:29

Typos fixed. 

I imagine we'll be using maxima for differential equations for a while yet, but this interface will almost certainly be affected by the move to PyNaC all the same. 

wdj: there is no need to use a lambda function, you can directly write 


```
sage: t = var('t')
sage: x = function('x', t)
sage: de = diff(x,t) + x - 1
sage: desolve(de,[x,t])
e^(-t)*(e^t + c)
sage: f = desolve(diff(x,t) + x - 1, x, ics=[10,2]); f
e^(-t)*(e^t + e^10)
sage: plot(f)
```



---

Comment by mabshoff created at 2008-10-18 11:30:25

There is one more trivial fix required for tut.tex:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/tut.py", line 830:
    : desolve(DE(x(t)), [x,t])
Expected:
    '%e^-t*(%e^t+%c)'
Got:
    e^(-t)*(e^t + c)
**********************************************************************
```


Cheers,

Michael


---

Comment by wdj created at 2008-10-18 11:49:56

based on 3.1.4


---

Attachment

I added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!


---

Comment by mabshoff created at 2008-10-18 12:05:34

Replying to [comment:10 wdj]:
> I added a patch which literally changes exactly this one line in tut.tex. Hope this is what you wanted!

Pretty much, thanks for the patch and a positive review for the last one.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 12:06:05

Merged both patches in Sage 3.2.alpha0.

Mike: Note that the patch by David touches tut.tex


---

Comment by mabshoff created at 2008-10-18 12:06:05

Resolution: fixed


---

Comment by zimmerma created at 2008-10-18 12:12:25

> Mike: Note that the patch by David touches tut.tex

as a consequence, it should be ported back to the translations of the tutorial
(in particular the french one, which is in progress, see the SD10 coding sprint page).


---

Comment by mabshoff created at 2008-10-18 12:16:19

Replying to [comment:13 zimmerma]:
> > Mike: Note that the patch by David touches tut.tex
> 
> as a consequence, it should be ported back to the translations of the tutorial
> (in particular the french one, which is in progress, see the SD10 coding sprint page).

I agree. The translation is already based on the ReST sources. One thing I just thought about was that all the documentation in the various languages ought to be doctested. This discussion should probably move to [sage-devel] so we can start designing a protocol how to deal with the new translation projects. Either way we will make the switch to the new ReST documentation for all bug the reference manual and depending on how things go we might even switch the reference manual for 3.2.

Cheers,

Michael


---

Comment by mhansen created at 2008-10-18 15:56:12

I made the change is the ReST documentation.
