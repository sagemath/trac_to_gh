# Issue 4457: tutorial: add find_root()  to "2.4.1 Solving Equations"

Issue created by migration from https://trac.sagemath.org/ticket/4457

Original creator: dhbradshaw

Original creation time: 2008-11-06 23:54:51

Assignee: tba

Currently, the section in the tutorial on solving equations refers only to analytical solutions, which are found using "solve()."  When solve fails, it may be worth using a numerical solution.  

For equations with a single variable, this can be done using find_root().  It will save new users time to find "find_root()" mentioned with "solve()" in the section on solving equations.

Examples:

```
id=1|
var('theta')
///

<html><span class="math">\theta</span></html>
```



```
id=2|
solve(theta^2 + 1==4)
///

<html><span class="math">\left[\theta  =  -\sqrt{ 3 }, 
 \theta  =  \sqrt{ 3 }\right]</span></html>
```



```
id=3|
solve(cos(theta)==sin(theta))
///

<html><span class="math">\left[\sin \left( \theta \right)  =  \cos \left( \theta \right)\right]</span></html>
```



```
id=4|
find_root(cos(theta)==sin(theta),0,pi/2)
///

<html><span class="math">0.785398163397</span></html>
```



```
id=5|
pi.n()/4
///

<html><span class="math">0.785398163397448</span></html>
```



```
id=6|

///
```



---

Comment by mhansen created at 2009-01-24 10:18:30

I've made a patch for this against the Sphinx version of the reference manual.

The output can be found at http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/tutorial/tour_algebra.html


---

Comment by mhansen created at 2009-01-24 10:18:30

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-01-24 10:18:30

Changing status from new to assigned.


---

Attachment


---

Comment by wdj created at 2009-01-24 13:31:09

The output looks great and the patch appears fine (modulo my understanding of Sphinx). I did not try to apply it though.


---

Comment by mhansen created at 2009-01-24 13:32:57

I think that's fine.  We can just move it to the Sphinx milestone and close it then.


---

Comment by mabshoff created at 2009-02-24 17:55:46

Fixed in Sage 3.4.alpha0 by merging #3479.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 17:55:46

Resolution: fixed
