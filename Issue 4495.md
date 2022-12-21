# Issue 4495: [with algorithm, needs implementation] weight distribution for binary codes

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-11-11 21:14:53

Assignee: tbd

Using Robert Bradshaw's bitsets, which include hamming weight functions, it should be trivial to implement a weight distribution algorithm for binary codes in pure Cython.

Essential ingredients:
 1. A list of bitsets representing the basis.
 2. A zeroed array to store the weight distribution.
 3. A gray code traversal of the span of the list.
 4. Hamming weight functions.

This should be nearly trivial to implement, and would remove the dependence (unmerged) ticket #4320 has on Guava, which will make the Windows port even harder...


---

Comment by wdj created at 2008-11-11 21:56:27

> This ...
> would remove the dependence (unmerged) ticket #4320 
> has on Guava, which will make the Windows port 
> even harder... 

Just to clarify a few points. 

First, the patch #4320 to the spectrum method in 
http://www.sagemath.org/hg/sage-main/file/3859ace86968/sage/coding/linear_code.py
does the following: 
(a) if no option is called and q>3 then 
spectrum calls the function wtdist (approximately line 180),
which does not use GUAVA (or leon or tjhal) code at all, but rather a GAP kernel function,
(b) if q=2 or q=3 and no option is called then spectrum calls the C code written by CJ Tjhal (which does not have the same problems as the leon code), so adding the binary case in Cython would be nice but still there is the issue of q=3,
(c) there is a new optional method which I added for the user's convenience, to call Leon's C code, which works for q=2,3,5,7. I don't understand why an optional method is bad. If there is a faster way added later, why would anyone use that option?

Second, GUAVA is cross-platform, as is GAP, though both have parts which are written in C. Does all the C code have to be rewritten for the windows port? 

Right now, leon and tjhal are only used for minimum distance and spectrum computations, q<=7. It would be nice to have the luxury of replacing them by Cython code but they are used for cases other than q=2.

Are these comments worthwhile?


---

Comment by mabshoff created at 2008-11-12 14:35:03

Replying to [comment:1 wdj]:

Hi David,

> Second, GUAVA is cross-platform, as is GAP, though both have parts which are written in C. Does all the C code have to be rewritten for the windows port? 

Nope, care to point me to a working MSVC port of GAP? Even the Cygwin one sucks :)

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-12-21 05:42:29

Changing assignee from tbd to rlm.


---

Comment by AlexGhitza created at 2008-12-21 05:42:29

Changing component from algebra to coding theory.


---

Comment by rlm created at 2008-12-24 21:12:37

For an 1100 times speedup (which is the real point of not using Guava):

OLD:
sage: time C.spectrum()
CPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s
Wall time: 3.36 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 2.20 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 3.26 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 2.74 s
[1, 0, 0, 7, 7, 0, 0, 1]

NEW:
sage: timeit('C.spectrum()')
625 loops, best of 3: 1.86 ms per loop


---

Comment by rlm created at 2008-12-24 21:13:51

Oops, bad formatting...


```
OLD:
sage: time C.spectrum()
CPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s
Wall time: 3.36 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 2.20 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 3.26 s
[1, 0, 0, 7, 7, 0, 0, 1]
sage: time C.spectrum()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 2.74 s
[1, 0, 0, 7, 7, 0, 0, 1]

NEW:
sage: timeit('C.spectrum()')
625 loops, best of 3: 1.86 ms per loop
```



---

Attachment

This is a great patch. It applies cleanly and I've done lots of testing, which it passes. 

I have a question though and this is what the Wall time on the following test means?


for i in range(20):
    C = RandomLinearCode(100, 25, GF(2))
    time s1 = C.spectrum()             
    time s2 = C.spectrum(method="gap") 
    s1 == s2       

          	

Time: CPU 0.84 s, Wall: 0.84 s
Time: CPU 0.94 s, Wall: 5.05 s
True
Time: CPU 0.87 s, Wall: 0.90 s
Time: CPU 1.05 s, Wall: 4.99 s
True
Time: CPU 0.87 s, Wall: 0.90 s
Time: CPU 0.95 s, Wall: 4.94 s
True
Time: CPU 0.84 s, Wall: 0.86 s
Time: CPU 0.96 s, Wall: 4.96 s
True
Time: CPU 0.88 s, Wall: 0.88 s
Time: CPU 0.98 s, Wall: 4.98 s
True
Time: CPU 0.85 s, Wall: 0.85 s
Time: CPU 0.92 s, Wall: 4.69 s
True
Time: CPU 0.85 s, Wall: 0.86 s
Time: CPU 0.84 s, Wall: 4.76 s
True
Time: CPU 0.84 s, Wall: 0.84 s
Time: CPU 0.98 s, Wall: 5.01 s
True
Time: CPU 0.85 s, Wall: 0.85 s
Time: CPU 0.94 s, Wall: 4.97 s
True
Time: CPU 0.88 s, Wall: 0.89 s
Time: CPU 0.94 s, Wall: 4.95 s
True
Time: CPU 0.85 s, Wall: 0.86 s
Time: CPU 0.93 s, Wall: 4.99 s
True
Time: CPU 0.85 s, Wall: 0.85 s
Time: CPU 1.00 s, Wall: 4.93 s
True
Time: CPU 0.93 s, Wall: 0.95 s
Time: CPU 1.03 s, Wall: 4.97 s
True
Time: CPU 0.85 s, Wall: 0.85 s
Time: CPU 1.04 s, Wall: 4.92 s
True
Time: CPU 0.84 s, Wall: 0.85 s
Time: CPU 1.02 s, Wall: 5.00 s
True
Time: CPU 0.86 s, Wall: 0.87 s
Time: CPU 0.85 s, Wall: 4.66 s
True
Time: CPU 0.85 s, Wall: 0.86 s
Time: CPU 0.83 s, Wall: 4.59 s
True
Time: CPU 0.85 s, Wall: 0.85 s
Time: CPU 0.86 s, Wall: 4.75 s
True
Time: CPU 0.91 s, Wall: 0.91 s
Time: CPU 0.90 s, Wall: 4.73 s
True
Time: CPU 0.91 s, Wall: 0.92 s
Time: CPU 0.88 s, Wall: 4.71 s
True


I wonder if this means that GAP's kernel computation (method="gap" is the slowest of the three) beats binary some percentage of the time but GAP's interface takes a long time to parse that information back to Sage (via pexpect and whatever fiddling GAP does), as indicated by the Wall time?


---

Comment by mabshoff created at 2008-12-26 18:46:55

Replying to [comment:6 wdj]:

Hi David,

> This is a great patch. It applies cleanly and I've done lots of testing, which it passes. 
> 
> I have a question though and this is what the Wall time on the following test means?

Fixing the formatting:


```
 for i in range(20):
     C = RandomLinearCode(100, 25, GF(2))
     time s1 = C.spectrum()             
     time s2 = C.spectrum(method="gap") 
     s1 == s2       
```

The timings:

```
 Time: CPU 0.84 s, Wall: 0.84 s
 Time: CPU 0.94 s, Wall: 5.05 s
 True
 Time: CPU 0.87 s, Wall: 0.90 s
 Time: CPU 1.05 s, Wall: 4.99 s
 True
 Time: CPU 0.87 s, Wall: 0.90 s
 Time: CPU 0.95 s, Wall: 4.94 s
 True
 Time: CPU 0.84 s, Wall: 0.86 s
 Time: CPU 0.96 s, Wall: 4.96 s
 True
 Time: CPU 0.88 s, Wall: 0.88 s
 Time: CPU 0.98 s, Wall: 4.98 s
 True
 Time: CPU 0.85 s, Wall: 0.85 s
 Time: CPU 0.92 s, Wall: 4.69 s
 True
 Time: CPU 0.85 s, Wall: 0.86 s
 Time: CPU 0.84 s, Wall: 4.76 s
 True
 Time: CPU 0.84 s, Wall: 0.84 s
 Time: CPU 0.98 s, Wall: 5.01 s
 True
 Time: CPU 0.85 s, Wall: 0.85 s
 Time: CPU 0.94 s, Wall: 4.97 s
 True
 Time: CPU 0.88 s, Wall: 0.89 s
 Time: CPU 0.94 s, Wall: 4.95 s
 True
 Time: CPU 0.85 s, Wall: 0.86 s
 Time: CPU 0.93 s, Wall: 4.99 s
 True
 Time: CPU 0.85 s, Wall: 0.85 s
 Time: CPU 1.00 s, Wall: 4.93 s
 True
 Time: CPU 0.93 s, Wall: 0.95 s
 Time: CPU 1.03 s, Wall: 4.97 s
 True
 Time: CPU 0.85 s, Wall: 0.85 s
 Time: CPU 1.04 s, Wall: 4.92 s
 True
 Time: CPU 0.84 s, Wall: 0.85 s
 Time: CPU 1.02 s, Wall: 5.00 s
 True
 Time: CPU 0.86 s, Wall: 0.87 s
 Time: CPU 0.85 s, Wall: 4.66 s
 True
 Time: CPU 0.85 s, Wall: 0.86 s
 Time: CPU 0.83 s, Wall: 4.59 s
 True
 Time: CPU 0.85 s, Wall: 0.85 s
 Time: CPU 0.86 s, Wall: 4.75 s
 True
 Time: CPU 0.91 s, Wall: 0.91 s
 Time: CPU 0.90 s, Wall: 4.73 s
 True
 Time: CPU 0.91 s, Wall: 0.92 s
 Time: CPU 0.88 s, Wall: 4.71 s
 True
}}]

> 
> I wonder if this means that GAP's kernel computation (method="gap" is the slowest of the three) 

What three? I see only two computations. 

> beats binary some percentage of the time but GAP's interface takes a long 
> time to parse that information back to Sage (via pexpect and whatever 
> fiddling GAP does), as indicated by the Wall time?  

That means the new code is beating the pants off GAP+Guava:
{{{
 Time: CPU 0.91 s, Wall: 0.92 s
 Time: CPU 0.88 s, Wall: 4.71 s
}}}

What counts it the total time, i.e. about 0.92s vs. 4.71s. The first line tells us that the new code spends all its time in Sage while the second line tells us that 4.71-0.88=3.83s were spend in GAP. I assume if we pick larger examples the favor will shift toward Robert's implementation, but that needs to be tested. One aspect here might be that the pexpect transfer to and from GAP is inefficient, but that can also easily be determined. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-12 01:12:41

Resolution: fixed


---

Comment by mabshoff created at 2009-01-12 01:12:41

Merged in Sage 3.3.alpha0
