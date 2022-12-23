# Issue 5188: squaring some factorizations has a bug

Issue created by migration from https://trac.sagemath.org/ticket/5188

Original creator: was

Original creation time: 2009-02-05 21:39:31

Assignee: tbd

CC:  wjp

In particular this isn't good:

```
sage: factor(-1)
-1
sage: (factor(-1))^2
-1
sage: (factor(-1)^2).value() == -1 
True
```



---

Comment by was created at 2009-02-05 21:43:26

Some discussion in email:

```


On Thu, Feb 5, 2009 at 1:39 AM, Willem Jan Palenstijn <wjp@usecode.org> wrote:
>
>
> Hi all,
>
> We recently ran into two cases of confusing behaviour of Factorization
> objects.
>
> The first:
>
> sage: f = factor(-1); f
> -1
> sage: f^2
> -1
>

That's terrible!  This is now:
    http://trac.sagemath.org/sage_trac/ticket/5188

> I traced this to a special case in the powering code for taking powers
> of zero, which f is treated as:
>
> sage: bool(f)
> False
>
> This is because f.__len__() == 0, and f.__nonzero__ is not defined. What do
> you think the behaviour of __nonzero__() should be? Always return True?
> Return 'not self.value()' ? 

The safest is clearly

    return self.value().__nonzero__()

But this can be very expensive.     Always returning true would be excellent,
but if we do that we need to put a test in the Factorization constructor that
all the "primes" are nonzero.  That would be reasonable, especially if you put
a check=False option in, so one can skip checking nontriviality of the primes
for speed reasons. 

> Return 'len(self.__x) > 0 or bool(self.__unit)' ?
> It's not at all clear to me how this should behave.
>
> My main confusion stems from the fact that it's easy to manually create
> Factorization objects that have value 0, even though some methods in
> Factorization don't seem to work properly for such manually created (non-prime)
> factorizations.
>
> E.g.,
> Factorization([0,1]) and Factorization([(Integers(4)(2),2)]) have value 0, and:
> sage: Factorization([(6,1)]).gcd(factor(2))
> 1
> is unexpected, though understandable.
>
> One solution to this might be documenting the exact behaviour of the
> Factorization object and functions like gcd/lcm to make it clear what
> (not) to expect. In that case, making __nonzero__() always return True
> might be acceptable. (Although I'm not sure if that's acceptable for
> Factorizations of spaces.)
>
>
>
>
>
> The other is a non-commutative +:
>
> sage: f = factor(2)
> sage: f + 7
> 9
> sage: 7 + f
> ...
> TypeError: unsupported operand parent(s) for '+': 'Integer Ring' and '<class 'sage.structure.factorization.Factorization'>'
>
> Maybe add/sub should be removed entirely as John Cremona suggested in
> http://trac.sagemath.org/sage_trac/ticket/3927 ?
>
> Alternatively, could Factorization objects somehow be hooked into the coercion
> system through the natural map to their universe where appropriate? Or does
> them not having a parent make this impossible/hard/undesirable ?

Maybe they should have a parent...

William

>
>
> -Willem Jan
>
> P.S. See also http://groups.google.com/group/sage-devel/browse_thread/thread/425a8614d5765130 for a previous discussion on this topic.

```



---

Comment by cremona created at 2009-02-15 18:06:12

Wouldn't it be a good idea to fix the bug, whlie not dealing with the general issue, but completely changing the `__pow__()` function for factorizations?  Currently it calls a generic powering function, but that is rather silly.  We should take the power of the unit, but just multiply the exponents in the factorization!  (There would need to be a special check for raising to exponent zero, of course).


---

Comment by mhansen created at 2009-06-04 20:46:42

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 20:46:42

This is now invalid.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: factor(-1)
-1
sage: sage: (factor(-1))^2
1
sage: sage: (factor(-1)^2).value() == -1 
False
```

