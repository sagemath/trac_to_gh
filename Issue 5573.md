# Issue 5573: genus2reduction interface has at least two problems

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-20 03:54:25

Assignee: was


```
On Thu, Mar 19, 2009 at 6:14 PM, ARMAND BRUMER wrote:
> Hi William,
>
> This is my first attempt to use sage. I have OSX 10.4.11 and just downloaded
> it.
>
> I wanted to use liu's program. After trying out your examples and getting
> the same result, I tried the example I was curious about and here is the
> output. Can you do better. Did I screw up?
>
> Thanks,
> armand
>
> sage: genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
> ---------------------------------------------------------------------------
> ValueError                                Traceback (most recent call last)
>


You have found a bug in Sage.    When I try the above by directly using Liu's program (note that i have to remove the spaces in the polynomials and use an explanation point to run the program), I get the following problem:

sage: !genus2reduction
   
enter Q(x) : x^3+x^2+x        
enter P(x) : -2*x^5+3*x^4-x^3-x^2-6*x-2
 
factorization CPU time = 5
a minimal equation over Z[1/2] is : 
y^2 = x^6+18*x^3+36*x^2-27
 
factorization of the minimal (away from 2) discriminant : 
[2,1;3,15;53,1]
 
p=2
(potential) stable reduction :  (II), j=1
reduction at p : [I{1-0-0}] page 170, (1), f=1
p=3
(potential) stable reduction :  (I)
reduction at p :   ***   expected character: ',' instead of: mod(y,y^2-3)
     
I don't know if this ever worked, but I bet it did, and PARI changed from 2004 or whatever, until now, and we just didn't pick up the change because we didn't test genus2reduction enough.  

2. A second problem is that if genus2reduction works once, then fails, then it fails to work again:

sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
sage: R.conductor
1416875
sage: R = genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
Traceback (most recent call last):
ValueError: error in input; possibly singular curve? (Q=x^3 + x^2 + x, P=-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)  # just worked above
Traceback (most recent call last):
...
ValueError: error in input; possibly singular curve? (Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)

---

When we fix this, we will of course have to write code to run through random curves and verify that genus2reduction works sensibly on millions of inputs.

Liu's program genus2reduction, included with Sage, is a C program that is written to use the Pari C library. 

```



---

Attachment

New spkg here:

http://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg


---

Comment by was created at 2009-04-05 22:33:01


```
 Basically you should just do (make sure lines don't break when the shouldn't):

$ sage -f http://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg 

$ sage
...
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5573/trac_5573.patch')
sage: quit

$ sage -br
...
```



---

Comment by mabshoff created at 2009-04-05 22:46:47

Patch looks good, I need to have the changes in the spkg explained to me to review this :). William hinted about a change in the pari library.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 05:47:07

Spkg and patch look good. Positive review. William did explain the mod/Mod change that fixed the issue in the spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 05:47:27

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 05:47:27

Reviewed in Sage 3.4.1.rc1.

Cheers,

Michael
