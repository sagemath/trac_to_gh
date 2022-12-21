# Issue 1678: docs -- tutorial: modification to the tutorial to address numerous gotcha's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-04 04:35:08

Assignee: tba

Somebody wrote those
comments to me about Sage.  I envision the tutorial mainly having a 
gotchas section that would address all of these confusions and issues below. 

```
Metacomment: Using SAGE Version 2.5.3, Release Date: 2007-05-22.
I did
*not* use the python documentation (I didn't have access to it, due to
some uninteresting technical problems that have now been fixed).

(9) This might be an unreasonable request, but: it might be nice to be
   able to get sage documentation w/out the python doc -- for example,
   my python documentation might be from somewhere on the Internet, and
   my Internet connection might be down (perhaps I'm flying on a
   plane) -- the specific case I ran across was trying to get the `if'
   syntax: it might be nice if somehow ?if, too, worked in sage.

(10) The Abstract on the Front Matter page of the tutorial says "[...]
    from the SAGE notebook click Documentation [...]" but doesn't
    tell you how to get to the sage notebook; perhaps a pointer (say
    to Section 3.10) at that point would help.

(11) I couldn't easily find the right way to get an integer/float (not
    symbolic) square root.  Should ?sqrt tell me how to do that?

(12) In general, it would be nice to know, for example, what types of
    sqrt are available, what types of arguments they take, etc.
    (Perhaps somewhat similar to what, e.g., Emacs-calc allows if you
    type M-x apropos, then sqrt to the prompt, then you can click on
    a sqrt of interest.)

(13) More generally, perhaps a way to see the names of all "available"
    functions would be nice.  (It may exist, but I couldn't see in
    two minutes how to get it.)  For example, I guessed `nextprime',
    but that didn't exist; it was only much later that I stumbled
    across the next_prime function, with an underscore.

(14) Back to sqrt?; it gave me --

    Type:              Function_sqrt
    Base Class:        <class 'sage.calculus.calculus.Function_sqrt'>
    String Form:                                            sqrt
    Namespace: Interactive
    Docstring:
       The square root function. This is a symbolic square root.
       EXAMPLES:
           sage: sqrt(-1)
           I
           sage: sqrt(2)
           sqrt(2)
           sage: sqrt(x^2)
           abs(x)

    -- but from this I couldn't figure out what type the argument had
    to be.  For example, I was surprised that

      sage: M = 3099044504245996706400
      sage: float(sqrt(M))
      55669062361.836098

    worked but then doing

      sage: M = int(M)
      sage: float(sqrt(M))

    gave an error.  Part of my surprise was that the next_prime
    function that I came across *did* work with both integer types
    (sage and python).

(15) Eventually someone showed me the timeit function, which I found
    really useful (with it, I easily found out that the X.is_square()
    form ran much faster than the is_square(X) form).  Perhaps some
    quick mention of timeit should be in the 3.4 Timing Commands
    section of the tutorial.

(16) I was a bit surprised when

      print "N = %d" %N

    didn't work if N got too large (more than about 63 bits); I guess
    I expected sage?python? to do the coercion.  (I wound up using

      print "N = %d" %(int(N))

    and that worked for smallish large N but I wasn't sure it would
    work for arbitrarily large N; I now know to use %s for this.)

(17) I was surprised that this code failed --

     for p in range(1,50) :
        if (p.is_prime()) :
           print p

    -- apparently because p somehow has become a python int, not a
    sage Integer.  Here was the error message:

<type 'exceptions.AttributeError'>: 'int' object has no attribute 'is_prime'
----------------------------------------------------------------------
----------------------------------------------------------------------
(18) I unexpectedly got this error:

 <type 'exceptions.OverflowError'>         Traceback (most recent call last)
 [ . . . ]
 ---> 22  for N in xrange(BASE, MAXBOUND, BASE) :
 [ . . . ]
 <type 'exceptions.OverflowError'>: long int too large to convert to int

 Also, it would have been nice if the error had told me which variable
 caused the overflow.  (I forget how I figured this out, but I wound up
 using xsrange instead.)

(19) I was surprised that with s defined as

   s = RealField(5000)(X).sqrt()

 that (where X is a very large nonsquare integer)

   print "%.4f [...]" %(s, [...])

 "stops" working if s gets too large.  Presumably this is a coercion
 problem.

(20) I was a little surprised that something of length 725760
 (apparently) would cause a problem:

 sage: len(quadratic_residues(232792560))
 /usr/local/sage-2.8.2/local/bin/sage-sage: line 182: 25097 Killed
     sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
----------------------------------------------------------------------
```



---

Comment by mabshoff created at 2008-04-19 19:21:05

The above laundry list should be checked, broken down into individual problems, the ones that are still valid should become their own tickets and then this ticket should be closed.

Cheers,

Michael


---

Comment by kcrisman created at 2014-11-20 17:44:04

20 - doesn't crash, though very long hang, probably because it has an incredibly naive algorithm.  See #17372.

19 - ???  I think I know what is meant, though.

```
sage: X = 100000000000000000000000000000000000000000000000000^2+1
sage: s = RealField(5000)(X).sqrt()
sage: print "%.4f"%s
100000000000000007629769841091887003294964970946560.0000  # really not close to the square root
sage: RealField(5000)(X)
1.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e100
sage: _.sqrt()
1.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000049999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999998750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000062499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996093750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000273437499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999979492187500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001611328124999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999869079589843750000000000000000000000000000000000000000000000000000000000000000000000000000000000000010910034179687499999999999999999999999999999999999999999999999999999999999999999999999999999999999999072647094726562500000000000000000000000000000000000000000000000000000000000000000000000000000000000080089569091796874999999999999999999999999999999999999999999999999999999999999999999999999999999999992992162704467773437500000000000000000000000000000000000000000000000000000000000000000000000000000000619924068450927734374999999999999999999999999999999999999999999999999999999999999999999999999999999944649636745452880859375000000000000000000000000000000000000000000000000000000000000000000000000000005e50
sage: _^2
1.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e100
```

Well, that's what you get when you do float formatting, as it's not a float.  In fact,

```
print "%f"%100000000000000000000000000000000000000000000000000
```

so invalid, or at least not fixable by us, I think.

18 - this is a pure Python error which we could in principle try to catch, but there are SO many places you'd have to do it.  I think wontfix.

17 - valid and truly a problem in many interesting places.  I don't know how to fix that other than education, though; removing "range" from everywhere is not so good.  This has been discussed before, whether `srange` or `range` is better - well, each has its uses.

16 - I can't reproduce this, and with formatting it's buyer beware, I think, as that is not a "basic" thing in Sage, but rather for people who actually know something about programming.

```
sage:  print "N = %d" %1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111112222222222222
N = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111112222222222222
```


15 - absolutely,  http://sagemath.org/doc/tutorial/interactive_shell.html#timing-commands should have timeit mentioned.

10 - This is really no longer valid, the tutorial has changed so much.

9 - I don't know what this means, but it is true that there are external links to Python docs.  In principle, we could include them - see #10831 - but I don't think that is necessary here.

11 - I guess we could add an example for `sqrt(2.)` or `sqrt(4.)`.

12 - I don't get this question.

13 - this is tab-completion.  Perhaps that didn't exist yet then.

14 - no longer valid for `sqrt` and we are making progress updating doc in cases where it might be valid, way too big for any one ticket.

----

Summary of what could still be done here:
* Education on range versus srange
* Mention `timeit` in the tutorial
* Include example in `sqrt` for `sqrt(2.)` or `sqrt(4.)` or both


---

Comment by kcrisman created at 2014-11-20 17:59:23

> * Education on range versus srange
#17373
> * Mention `timeit` in the tutorial
In the branch needing review.  Naturally, one could do more, but this is a start.
> * Include example in `sqrt` for `sqrt(2.)` or `sqrt(4.)` or both
In the branch needing review.


---

Comment by kcrisman created at 2014-11-20 17:59:50

Changing priority from major to minor.


---

Comment by kcrisman created at 2014-11-20 17:59:50

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-11-20 17:59:50

New commits:


---

Comment by ncohen created at 2014-12-31 10:53:14

Good to go !

Nathann


---

Comment by ncohen created at 2014-12-31 10:53:14

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-02 22:12:32

Resolution: fixed
