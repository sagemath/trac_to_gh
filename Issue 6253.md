# Issue 6253: [with patch, needs review] Constant functions

Issue created by migration from https://trac.sagemath.org/ticket/6253

Original creator: nthiery

Original creation time: 2009-06-09 22:08:39

Assignee: nthiery

CC:  sage-combinat mhansen jason

Keywords: constant functions

This trivial patch adds basic support for constant functions

Such a function could be written as lambda x: constant, but that's not picklable. Besides, this should eventually be cythoned for speed.


---

Comment by nthiery created at 2009-06-09 22:13:58

Oh, I forgot to mention: let me know if this readily exists somewhere and I missed it.


---

Comment by mhansen created at 2009-06-09 22:26:19

How is this intended to be used?  What are your typical constants? Are there instances where you'd want a non-constant function to be used in the same place?


---

Comment by nthiery created at 2009-06-10 07:10:10

Replying to [comment:2 mhansen]:
> How is this intended to be used?  

One of my use case looks like:

def my_objects(<some parameters>, predicate = ConstantFunction(True)):
    """
    Returns all the objects blah blah blah (as an EnumeratedSet)
    Optionally, a predicate can be specified to select only those objects satisfying the predicate

Another one looks like:

def generating_series(..., weight = ConstantFunction(1)):
    ...

> What are your typical constants? 

So far, True, 1, Integer(1)

Btw: with UniqueRepresentation, the two first yield the same constant function with the current implementation, thanks to this horror:

    sage: { 1: 'a', True: 'b' }
    {1: 'b'}

Fixed patch in a couple minutes.

> Are there instances where you'd want a non-constant function to be used in the same place? 

Yes. Actually, that's the case in all the situations I encountered so far


---

Comment by nthiery created at 2009-06-10 07:10:10

Changing status from new to assigned.


---

Attachment


---

Comment by nthiery created at 2009-07-26 23:09:04

The updated patch removes two unused imports spotted by Florent. Apply only this one.


---

Comment by hivert created at 2009-07-26 23:12:00

The patch looks good ! Positive review !

Florent


---

Comment by mvngu created at 2009-08-23 01:50:00

reviewer patch


---

Attachment

This is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:

 1. `trac_6253-constant_function-nt.patch`
 1. `trac_6253-reviewer.patch`


---

Comment by nthiery created at 2009-08-23 08:34:42

Replying to [comment:7 mvngu]:
> This is great stuff! So let's put it in the reference manual. The reviewer patch `trac_6253-reviewer.patch` adds the module `sage/misc/constant_function.py` to the reference manual. It also fixes some typos so that the reference manual builds without any warnings. If people are happy with my changes, then patches should be merged in this order:
> 
>  1. `trac_6253-constant_function-nt.patch`
>  1. `trac_6253-reviewer.patch`

Thanks Minh! (again)

Positive review on your reviewer patch.


---

Comment by mvngu created at 2009-08-23 09:52:52

Merged patches in this order:

 1. `trac_6253-constant_function-nt.patch`
 1. `trac_6253-reviewer.patch`


---

Comment by mvngu created at 2009-08-23 09:52:52

Resolution: fixed
