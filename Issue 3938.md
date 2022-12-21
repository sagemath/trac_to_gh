# Issue 3938: coercion framework converts built-in types to Sage types when it should not

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-08-23 21:02:17

Assignee: robertwb

CC:  cwitty

This came up while reviewing #2898, which adds a conversion from float to ZZ (for integral values).  After applying that patch, you get:


```
sage: 1.0r/8
1/8
```


That's because of this code in coerce.pyx, which does a conversion rather than a coercion:

```
        elif PY_IS_NUMERIC(x):
            try:
                x = yp(x)
                if PY_TYPE_CHECK(yp, type): return x,y
```


I tried to fix this, but every time I fixed something it broke something else.  I'm going to attach my latest non-working patch, which may or may not be a useful place to start.


---

Attachment

I've been playing around with this a bit, simplified your patch some, but one consequence is that 


```
sage: parent(RealField(100)(1.5) + float(1.5)) # good?
<type 'float'>
sage: RealField(100)(2^4000) == float('inf')   # bad?
True
```


Thoughts?


---

Comment by cwitty created at 2008-08-24 22:26:48

Both of these changes make float act more like RDF.  I've sometimes wished that comparison operators would coerce to more-precise types instead of less-precise, but that would be a huge change across big parts of Sage; unless such a policy change is made, I think that both consequences are actually good.


---

Attachment


---

Attachment

I feel your pain...what a nasty patch to try and write! Well, I finally feel like I've got a correct, working solution. Apply all three patches.


---

Comment by mabshoff created at 2008-08-30 23:05:07

Carl,

any chance you could review those three patches?

Cheers,

Michael


---

Comment by anakha created at 2008-09-06 23:13:12

I get


```
sage: parent(RealField(10)(1) * float(1))
Real Field with 10 bits of precision
```


with the patches applied against 3.1.2.alpha4.


---

Comment by robertwb created at 2008-09-08 16:27:11

Is this not the desired behavior?


---

Comment by anakha created at 2008-09-08 17:40:22

I thought the goal was to convert to the type with most precision.  It seems I was mistaken and this is trying to convert to the type with less precision.  

In that case it works and passes a good chunk of the test suite.  (I can't test the rest because of the interfaces/lisp.py failure)

It also passes its own tests and the code looks good.


---

Comment by mabshoff created at 2008-09-19 01:45:18

This patch causes a Heisenbug:

```

mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0$ ./sage -t -long devel/sage/sage/modular/modsym/ambient.py
sage -t -long devel/sage/sage/modular/modsym/ambient.py     

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [4.6 s]
exit code: 768
```

It does not happen without "-long" and when running "-long -verbose" it also seems to pass. I guess it is time to valgrind :)

Cheers,

Michael


---

Comment by roed created at 2009-01-23 02:46:56

I didn't find the Heisenbug that Michael mentioned.  I rebased the patches against 3.2.3.


---

Comment by robertwb created at 2009-01-23 22:05:39

Thanks for rebasing this. Since you're not the one who originally wrote it, do you want to give it a review?


---

Attachment

Merged the three patches, added a few fixes to precision.


---

Comment by craigcitro created at 2009-01-24 08:50:50

Patch looks good. Thankfully, David folded everything into one patch. 

I have two minor issues, and after these are fixed, I'm happy to give this a positive review. 

 * There are two long blocks (an `EXAMPLES` and a `TESTS`) that are not indented correctly. 

 * There are three functions that are moved and one that is new which need doctests. (The moved functions don't necessarily have to have them added, but since it's three functions, it seems worth just adding doctests.)

Once these are done, I'm happy to give this a positive review.


---

Comment by robertwb created at 2009-01-24 08:59:22

OK, I'll go ahead and add those doctests.


---

Attachment

apply only this patch


---

Comment by robertwb created at 2009-01-24 10:48:04

OK, I added the doctests and fixed the indentation.


---

Comment by craigcitro created at 2009-01-24 11:31:55

Looks good.


---

Comment by mabshoff created at 2009-01-28 15:15:59

One fix:

```
    TypeError: no cannonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision
```

needs to become

```
    TypeError: no canonical coercion from Real Field with 53 bits of precision to Real Field with 100 bits of precision
```


I am fixing that in the patch I am applying.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:22:03

Merged 3938-type-coercion-final.patch with spelling fix in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:22:03

Resolution: fixed
