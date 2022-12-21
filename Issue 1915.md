# Issue 1915: infinity doesn't behave well

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-01-24 17:35:48

Assignee: cwitty

The default model for handling infinity in Sage is not very user friendly.

Here is an example from Mathematica:


```
mathematica: Gamma[0]
ComplexInfinity

mathematica: 1/Gamma[0]
0

mathematica: 1 + 1/Gamma[0]
1
```


And an example from sage:


```
sage: 1/Infinity
Zero

sage: 1 + 1/Infinity
A positive finite number
```


In Sage `1/Infinity` should be `0` in some numeric domain. Returning `Zero` in `The Infinity Ring`  results in everything coercing to `The Infinity Ring`. 


---

Comment by AlexGhitza created at 2008-09-07 02:59:24

See the attached patch.  I am making 1/Infinity return the integer 0, since that should coerce without problems into any place one wants to do arithmetic.


---

Comment by jhpalmieri created at 2008-09-11 22:05:25

Overall, I like this. However, and this is not entirely the fault of your patch, I have an issue here. First, in the docs at the top of the file infinity.py, oo is defined to be `UnsignedInfinityRing.0`, and then later it is defined to be `InfinityRing.0`; however, oo is already defined (in sage.all). It seems bad to define it (since it's already defined), and it also makes the documentation really hard to read, since as it currently stands, sometimes oo means (unsigned) infinity, and sometimes it means +Infinity. If you're doing a quick skim (as I just was), you can get really confused.

Furthermore, in a fresh copy of sage:

```
sage: InfinityRing.0 == oo
True
sage: UnsignedInfinityRing.0 == oo
True
sage: 1 / (UnsignedInfinityRing.0)     
A number less than infinity
sage: 1 / oo                      
0
```

I don't like the fact that although these various infinities are ==, they don't behave the same when they are denominators.

Perhaps this could be fixed by:

1. having your patch return 0 for quotients like `1 / (UnsignedInfinityRing.0)` (or did you have a reason for not making `1 / (UnsignedInfinityRing.0)` return 0?), and

2. not defining oo in the documentation, but instead verify in the examples that `oo == UnsignedInfinityRing.0` and `oo == InfinityRing.0` both return True. (Or if the generator `UnsignedInfinityRing.0` really needs a name in the docs, give it a different one. Same for `InfinityRing.0`, so the two elements can be easily distinguished when reading the docs.)


---

Attachment

Thanks for catching the bug involving unsigned infinity.  I have replaced the patch with one that hopefully addresses the (very justified!) objections.  I chose to explain how oo relates to InfinityRing.0 and to UnsignedInfinity.0, and to replace oo by unsigned_oo in the docstrings related to the unsigned infinity ring.


---

Comment by jhpalmieri created at 2008-09-12 16:26:24

Looks good to me. I like the new comparisons using == and `is` at the top, too.


---

Comment by mabshoff created at 2008-09-15 03:54:36

Resolution: fixed


---

Comment by mabshoff created at 2008-09-15 03:54:36

Merged in Sage 3.1.2.rc4
