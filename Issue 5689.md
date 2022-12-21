# Issue 5689: hitting control c while computing pi results in wrong answers later

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-05 19:06:09

Assignee: somebody


```
D-69-91-159-159:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: RealField(10^6).pi()
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/.sage/temp/D_69_91_159_159.dhcp4.washington.edu/27480/_Users_wstein__sage_init_sage_0.py in <module>()

KeyboardInterrupt: 
sage: RealField(10^3).pi()
3.14159265358979323851280895940618620443274267017841339111328125000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```


Jeff Blakeslee reported this.

Cwitty followed up with:

```
Oh, interesting!  I've always worried about _sig_on/_sig_off, but this
is the first reproducible bug I've seen them cause.

When Sage is computing pi to many digits (and in many other cases), it
sets up a signal handler; if you press Control-C, then it will longjmp
out of the signal handler.  This lets you interrupt long-running
computations, but it's a really nasty thing to do... you can easily
get memory leaks, and I can imagine lots of (somewhat unlikely)
situations where you would crash Sage or get wrong answers.

I'm not sure what to do about the problem, though.  The "right" fix is
to go through all the C libraries that Sage calls, and add periodic
checks for Control-C; but that's pretty impractical.  Another
possibility would be to disable _sig_on, so that Control-C doesn't
work in long-running C computations.  This would fix the bug, but it
would also be vastly annoying.

One workaround that might fix this particular problem is to catch
KeyboardInterrupt exceptions in the .pi() method (and in
.euler_constant(), .catalan_constant(), and .log2()), and call
mpfr_free_cache() if one is seen.  Hopefully then MPFR would no longer
believe it has a higher precision value computed than it actually does
have.

Carl
```



---

Comment by was created at 2009-04-05 19:17:45

I wrote code to fix this problem in this case.  The following testing code, which I wrote, does not work.  I'm recording it here for posterity:


```
        TESTS::

        We check that trac 5689 is fixed:
            sage: alarm(1); RealField(10^6).pi()
            Traceback (most recent call last):
            ...
            KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
            sage: RealField(10^3).pi()
            3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127
```



---

Comment by was created at 2009-04-05 19:24:58

This patch resolves this problem completely, but has a performance penalty:

```
BEFORE:
sage: a = RealField(1000)
sage: timeit('a.pi()')
625 loops, best of 3: 3.4 µs per loop

AFTER:
sage: a = RealField(1000)
sage: timeit('a.pi()')
625 loops, best of 3: 64.4 µs per loop
```


Of course the difference in time is because the answer is being 100% cached in the first place. 

I tried catching the interrupt, as carl suggests, but that isn't easy in Cython without writing a whole new sig handler system like Gonzalo T. and I did for the pari gen.pyx file, and that is pretty painful. 

Note -- there is one way to defeat the attached patch: (1) hit control c during computation of a constant, then (2) call some other mpfr function that assumes that internally does compute one of these constants.   Thus this patch is not bullet proof.  I'm posting it since it seems better than nothing, resolves the immediate problem, and was totally trivial to write. 

 -- William


---

Attachment


---

Comment by mabshoff created at 2009-04-06 05:43:43

One small issue: The comments do not mention the mpfr_const_catalan constant and are also not consistently indented. This is nick picking, but what the heck :)

Cheers,

Michael


---

Comment by was created at 2009-04-06 16:43:35

> One small issue: The comments do not mention the mpfr_const_catalan constant 
> and are also not consistently indented. This is nick picking, but what the heck :) 

That's because I'm quoting from the MPFR documentation, which is *wrong* in that *it* doesn't mention mpfr_const_catalan. 

William


---

Attachment


---

Comment by mabshoff created at 2009-04-06 18:32:09

This is a 3.4.1 blocker.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 22:40:39

Positive review to both patches. I agree that correctness is way more importan than speed in this case.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 22:54:55

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 22:54:55

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
