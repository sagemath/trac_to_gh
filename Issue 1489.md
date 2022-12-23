# Issue 1489: serious bug in calculus maxima parsing

Issue created by migration from https://trac.sagemath.org/ticket/1489

Original creator: was

Original creation time: 2007-12-13 18:27:09

Assignee: was


```


On Dec 13, 2007 9:53 AM, Matthias Hillenbrand <mailanhilli@googlemail.com> wrote:
> 
> Hello,
> 
> doing my first steps with SAGE I have a problem dealing with small
> numbers like 2e-6. Here is a small example:
> 
> k=var('k')
> a0=2e-6
> a1=12
> b=sqrt(a1+a0*k)
> show(b)
> 
> With this parameters I don't get a result but have to interrupt the
> computation. If I change a0 to a0=2e-2, the computation only needs one
> second.
> 
> Am I doing something wrong?
> 

No, this is a bug in this part of Sage itself in calculus.py.  Many many thanks
for finding this (it will be fixed in the next Sage release, which is planned
for Saturday). 

Starting at Line 6146:
    #replace all instances of scientific notation
    #with regular notation
    search = sci_not.search(s)
    while not search is None:
        (start, end) = search.span()
        s = s.replace(s[start:end], str(RR(s[start:end])))
        search = sci_not.search(s)

I think this bug was caused by some recent changes in how
real number printing works in Sage.  In any case,
I'm glad you found the bug, which I'm sure we will easily be
able to fix.   
```



---

Attachment


---

Comment by mabshoff created at 2007-12-13 21:55:28

Hi,

2.9.alph6 + this patch passes -testall on OSX 10.5.1. It also looks cleaner and reuses hopefully better tested existing code. So my vote is on merging.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 05:11:50

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 05:11:50

Merged in 2.9.alpha7.
