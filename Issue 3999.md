# Issue 3999: [with patch, needs review] Wrapper class to treat additive groups as multiplicative goups

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-08-30 11:27:57

Assignee: somebody

This will greatly facilitate writing generic code. 


```
        sage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper

        sage: R.<x,y> = ZZ[]
        sage: G = MultiplicativeWrapper(R)
        sage: a, b = G(x), G(y)
        sage: a^2 * b^5 * a
        (3*x + 5*y)
        sage: a/b
        (x - y)

        sage: E = EllipticCurve('37a')
        sage: P = E([0,0])
        sage: G = MultiplicativeWrapper(P.parent(), repr_format=None); G

        sage: a = G(P); a
        (0 : 0 : 1)
        sage: b = G(5*P); b
        (1/4 : -5/8 : 1)
        sage: a^2 * b
        (-5/9 : 8/27 : 1)
        sage: 7*P
        (-5/9 : 8/27 : 1)
        sage: 10*P == a^10
        True

```



---

Comment by robertwb created at 2008-08-30 11:30:53

Virtually no overhead: 

```
sage: from sage.groups.multiplicative_wrapper import MultiplicativeWrapper
sage: R.<x,y> = ZZ[]
sage: G = MultiplicativeWrapper(R)
sage: f = R.random_element()
sage: g = R.random_element()
sage: timeit("2*f + 5*g")
625 loops, best of 3: 48.4 µs per loop
sage: a = G(f)
sage: b = G(g)
sage: timeit("a^2 * b^5")
625 loops, best of 3: 49 µs per loop
```



---

Comment by cremona created at 2008-09-02 19:32:27

I am trying hard to see how this might actually be useful in practice.

If we had a whole implementation of additive abelian groups (as Z-modules, within the modules package) then this could be useful to allow for multiplicative abelian groups.

But in fact the whole abelian groups machinery is already multiplicative.  What I tried, and nearly succeeded doing, was to all additive notation for those.  Perhaps it would be possible to have a version of this patch which goes the other way.  But I have other things to do than learn how to do that.

This is not a negative review, just a non-review.


---

Comment by robertwb created at 2008-09-02 23:15:16

> I am trying hard to see how this might actually be useful in practice.

The first thing that comes to mind is the generic discrete log code that you wrote a while back. One then wouldn't have to use the cumbersome (and slower) op(x,y) notation for the group operations to be able to handle both additive (via the wrapper) and multiplicative groups. 

I had assumed the implementation of abelian groups was, at its core, additive using Z-modules and all (this seems more natural to me, as well as much more efficient). I'm not sure if this is part of the "great abelian groups rewrite" or not, but IMHO I think it should be. I also wrote the patch this direction because (in Sage) additive groups are all abelien (they inherit from modules), and there is a functor from them to generic non-abelien groups but not the other way around. It could also be handy in trying to (formally) implement Z[G] where G is initially presented as an additive group. 

Trying to add additive notation to these would be difficult, as they do not inherit from ModuleElement. Were you trying to make it so if I took elements of a multiplicative group (say, a permutation group) and did `a+b` it would instead do `a*b`. I would probably rather have it throw an error in this case. 

I could pretty easily write a patch going the other way if you would find it useful (though strange stuff might happen if one tries to use it on non-abelien groups, depending on the assumptions people make throughout the rest of the Sage library).


---

Comment by was created at 2008-11-28 21:48:19

REFEREE REPORT:

This bitrotted.  I couldn't apply cleanly because of setup.py being refactored.  I fixed that by hand, but then this wouldn't compile:

```
was`@`sage:~/build/sage-3.2.1.alpha1$ ./sage -br

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/groups/multiplicative_wrapper.pyx.
Execute 1 commands (using 1 cpus)
python2.5 `which cython` --embed-positions --incref-local-binop -I/home/was/build/sage-3.2.1.alpha1/devel/sage-main -o sage/groups/multiplicative_wrapper.c sage/groups/multiplicative_wrapper.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        except:
            if x == 1:
                return self.one
            raise
            
    cpdef bint _has_coerce_map_from_(self, S) except -2:
         ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:113:10: C method '_has_coerce_map_from_' not previously declared in definition part of extension type

Error converting Pyrex file to C:
------------------------------------------------------------
...
        cdef MultWrapperElement e = <MultWrapperElement>PY_NEW(MultWrapperElement)
        e._parent = self._parent
        e._elt = elt
        return e

    cdef MonoidElement _mul_c_impl(self, MonoidElement right):
        ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:191:9: C method '_mul_c_impl' not previously declared in definition part of extension type

Error converting Pyrex file to C:
------------------------------------------------------------
...
        return e

    cdef MonoidElement _mul_c_impl(self, MonoidElement right):
        return self._new(self._elt._add_c((<MultWrapperElement>right)._elt))

    cdef MultiplicativeGroupElement _div_c_impl(self, MultiplicativeGroupElement right):
        ^
------------------------------------------------------------

/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/groups/multiplicative_wrapper.pyx:194:9: C method '_div_c_impl' not previously declared in definition part of extension type
Parallel build failed with status 256.
sage: There was an error installing modified sage library code.
```



---

Comment by cremona created at 2008-12-03 20:49:15

I have made more progress in my adaptation of the existing Abelian Groups code (which uses additive representation internally, but multiplicative notation for input and output) work for additive group notation (for input and output).  I'll post a patch when I have finished doing doctests -- everything I wanted to be able to do now works, but for every single function I need to add additive examples as well as the existing multiplicative ones).

For my purposes, my patch will work fine, for example with elliptic curve groups which are naturally additive, and is preferable to what Robert has implemented here.  But it is a very different approach to the one here, which uses the coercion machinery which I am pretty sure I will never understand.


---

Comment by robertwb created at 2008-12-07 10:43:51

The bitrot was due to #4310 and #4175, the patch has been updated. 

Thre needs to be more doctests. 


```
sage/groups/multiplicative_wrapper.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)
...
```


I'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. 

Most of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.


---

Attachment


---

Comment by cremona created at 2008-12-07 13:14:38

Replying to [comment:6 robertwb]:
> The bitrot was due to #4310 and #4175, the patch has been updated. 
> 
> Thre needs to be more doctests. 
> 
> {{{
> sage/groups/multiplicative_wrapper.pyx
> ERROR: Please define a s == loads(dumps(s)) doctest.
> SCORE sage/groups/multiplicative_wrapper.pyx: 20% (5 of 24)
> ...
> }}}
> 
> I'll hold off until I see John Cremona's patch. Could you post it, even if it's not done yet? I'm not sure I like the idea of `a+b` just working for any multiplicative group though. 

OK, will do.  a+b will not work for multiplicative groups:  it will give a NotImplementedError, while a*b will work.  And vive versa if the group was created as multiplicative (which will be the old, default behaviour).

> 
> Most of my patch is not about coercion, but anyone doesn't understand how coercion is working I'm the one to blame until I at the very least put out some good documentation.


---

Attachment


---

Comment by boothby created at 2009-01-23 09:02:46

Coverage at 100%.  Currently, some of the examples use Steenrod algebras, and expose some bugs in that code -- those will get fixed soon.


---

Comment by cremona created at 2009-01-23 09:34:21

I have said enough on this ticket already.  None of the doctests give me a clue as to how I might ever find this useful (I don't know about Steenrod algebras), so the review should be done by someone who can appreciate that better.


---

Comment by robertwb created at 2009-01-23 10:14:54

Thanks for the doctests. I don't know about Steenrod algebras either. 

This would be useful, for example, if one wrote a blackbox group algorithm multiplicatively, then wanted to run it on an abelian group (such as points on an elliptic curve).


---

Attachment

Doctests fixed after #5064 is applied.


---

Comment by shumow created at 2009-01-24 11:53:26

Still doesn't work for me.


---

Comment by robertwb created at 2009-01-24 21:39:17

Could you clarify what doesn't work?
