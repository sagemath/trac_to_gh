# Issue 6870: [with patch, needs review] Bug in binomial

Issue created by migration from Trac.

Original creator: hgranath

Original creation time: 2009-09-02 20:20:20

Assignee: somebody

Keywords: binomial

Here are two cases where binomial fails. I think it is not
properly converting its arguments to Integers in all cases where
it should.


```
sage: binomial(1/2,1/1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()

/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)
   2602             except AttributeError:
   2603                 pass
-> 2604             raise TypeError, 'Either m or x-m must be an integer'
   2605     if isinstance(x, (int, long, integer.Integer)):
   2606         if x >= 0 and (m < 0 or m > x):

TypeError: Either m or x-m must be an integer
```



```
sage: binomial(10^20+1/1,10^20) 
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()

/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)
   2625         from sage.functions.all import gamma
   2626         return gamma(x+1)/gamma(P(m+1))/gamma(x-m+1)
-> 2627     return misc.prod([x-i for i in xrange(m)]) / P(factorial(m))
   2628 
   2629 def multinomial(*ks):

OverflowError: long int too large to convert to int
```




---

Attachment


---

Comment by kcrisman created at 2009-09-14 20:51:34

This is a good idea, and somewhat surprisingly it speeds up very small binomials without slowing down biggish ones.  However, it does seem to slow down symbolic binomials:

Before:

```
sage: timeit('binomial(100,10)')
625 loops, best of 3: 21.9 µs per loop
sage: timeit('binomial(10^7,252525)')
5 loops, best of 3: 1.35 s per loop
sage: timeit('binomial(2*n,n)')
625 loops, best of 3: 60.3 µs per loop
sage: timeit('binomial(n+1,n)')
625 loops, best of 3: 78.4 µs per loop
```


After:

```
sage: timeit('binomial(100,10)')
625 loops, best of 3: 18.9 µs per loop
sage: sage: timeit('binomial(10^7,252525)')
5 loops, best of 3: 1.34 s per loop
sage: timeit('binomial(2*n,n)')
625 loops, best of 3: 76.2 µs per loop
sage: timeit('binomial(n+1,n)')
625 loops, best of 3: 137 µs per loop
```


I imagine that in some applications with a lot of symbolic stuff that could be a problem, but I'm not sure.  Is it possible to put a catch in for expressions that would keep things more or less as they were there, without making the numeric ones much slower?


---

Comment by hgranath created at 2009-09-16 03:48:47

I think to some extent this is a correctness vs speed issue. Before
the patch there is an asymmetry in the checking of whether m and x-m
is in ZZ. So e.g. binomial(3/2,1/2) works while binomial(3/2,1/1)
fails, although the documentation indicates they should be equivalent.
For me it was very confusing when something like that happened.
The benchmark case binomial(n+1,n) benefits from this asymmetry. I
have thought about it, but so far I have not found a satisfactory
solution which will not affect the speed of binomial(n+1,n) while
doing the right thing in other cases.

The other thing my patch is doing is to check more carefully if x is
an integer. As noted this will be an improvement when this succeeds.
Apart from the above benchmarks, try e.g. binomial(QQ(10**7),252525) or
binomial(SR(10**7),252525) with and without the patch applied. This
part of the patch however is not as important to me, a user could
always use binomial(ZZ(x),m) when beneficial. Hence an alternative
patch is to just do the first part. This will decrease the speed
regression in the symbolic case.


---

Attachment


---

Comment by kcrisman created at 2009-09-16 14:17:08

No, we should be able to compute the second type too, so don't jettison that.  But can't you combine the two?  Checking type is not so bad to do, and then you can still always try to coerce later.  After all, at the bottom there is a special case check for reals and floats.  So maybe you could do something like

```
if isinstance(m or x-m,whatever.rational):
   convert to integer if possible
```


I did check, and the slowdown for symbolic ones is because of that check.  Checking for an instance takes about 1/10 the time.

```
sage: def f():
....:     try:
....:         m=ZZ(a)
....:     except:
....:         pass
....:     
sage: timeit('f()')
625 loops, best of 3: 34.4 µs per loop
sage: def g():
....:     isinstance(a,(int,long,Integer))
....:     
sage: timeit('g()')
625 loops, best of 3: 2.57 µs per loop
```

where a = n+1

I guess the point is that we should definitely have as many correct answers as possible, but that the slowdown should be on these admittedly unusual cases with rationals, which are less likely to come up than the usual cases.


---

Comment by hgranath created at 2009-09-17 06:42:04

But I have a problem then. In the situation where x is of type SR and
m of type Integer, consider the cases x is n+1 (case A) and x is
SR(10**7) (case B).

To handle these cases correctly they have to be treated differently,
but how to distinguish between them using fast checks like
"isinstance" and similar if using "try: ZZ(x)" is not allowed because
it will slow down case A?


---

Comment by kcrisman created at 2009-09-17 13:42:50

Maybe this?

```
sage: var('n')
n
sage: a = n+1
sage: from sage.symbolic.expression import Expression
sage: isinstance(a,Expression)
True
sage: def g():
....:     isinstance(a,Expression)
....:     
sage: timeit('g()')
625 loops, best of 3: 573 ns per loop
sage: a=SR(10**7)
sage: timeit('g()')
625 loops, best of 3: 595 ns per loop
sage: timeit('f()')
625 loops, best of 3: 1.59 µs per loop
```

You can still use try: ZZ(x), it just makes sense to check type first, since it adds only nanoseconds, and then if someone is silly enough to use SR(10**7) instead of 10**7, they'll have to pay the microsecond penalty.  I jest a little, but I think you should try something like this to see if it would work.  If not, the first patch is probably better than allowing rational things to get through.  You could also add a check for rationals instead:

```
sage: from sage.rings.rational import Rational
sage: def g():
....:     isinstance(a,Rational)
....:     
sage: timeit('g()')
625 loops, best of 3: 1.23 µs per loop
sage: a = 10**7-1/1
sage: type(a)
<type 'sage.rings.rational.Rational'>
sage: timeit('g()')
625 loops, best of 3: 570 ns per loop
```

So even if a isn't rational, you lose very little time by checking that before you coerce.


---

Comment by hgranath created at 2009-09-21 16:34:47

If we want to fix only the rational case, that is of course easy to
do. I have two alternative new patches: one for doing just that, and
one which is basically my first patch but reworked to not affect the
case of floating point input (which was an undesired side effect).

With the QQ patch, it is unfortunately still easy to construct cases
that will fail: e.g. binomial(1/2,SR(1)),
binomial(SR(10**20+1),10**20) and binomial(SR(10**7+1),10**7) (the
last one takes a looong time).


---

Attachment


---

Attachment


---

Comment by kcrisman created at 2009-09-21 16:41:25

I think you misunderstood.  My point is that one can ALSO do a check for symbolic expressions, as outlined above (that's what I meant by "they'll have to pay the microsecond penalty".  We can't catch every case, of course, but we might as well try to get the ones we know about.  

I hope that these comments are not frustrating; this is overall a good fix to a non-critical but nonetheless important bug.


---

Comment by hgranath created at 2009-09-21 17:08:39

I really have no idea what to do. So assume we have something like


```
if isinstance(x,Expression):
```


then what to do? We have no idea at this point if x happens to be something
like SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If
that try should fail, it is already too late to avoid the time penalty
that is the point of this discussion.


---

Comment by kcrisman created at 2009-09-21 18:19:37

Replying to [comment:8 hgranath]:
> I really have no idea what to do. So assume we have something like
> 
> {{{
> if isinstance(x,Expression):
> }}}
> 
> then what to do? We have no idea at this point if x happens to be something
> like SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If
> that try should fail, it is already too late to avoid the time penalty
> that is the point of this discussion.

Understood; I think I didn't catch what the salient point was in your earlier comment, but now I do, and I agree that there is no easy way around it.  My apologies.  

Here is my last idea.  I think that the .pyobject() method of Expression can catch this - because it returns an error for anything which is not a bare coefficient:

```
sage: def h():
    try:
        a.pyobject()
        return ZZ(a)
    except:
            return a
sage: a = n+1
sage: h()
n + 1
sage: timeit('h()')
625 loops, best of 3: 5.98 µs per loop
sage: a = SR(10^7)
sage: timeit('h()')
625 loops, best of 3: 1.89 µs per loop
```

The docstring confirms this performs as advertised.  If that doesn't speed things up, then I guess it's not possible :(

So if that doesn't work, your original solution stands as a definite improvement, with the changes you noted - put the rational check inside the already existing not isinstance(m, int etc.) check, before trying m = ZZ(m), do the floating point fix where you have it.  Oh yeah, be sure to add doctests for the SR(10**7) etc. 

Because in the long run, we should have more correct cases, I think.  If someone notices a really bad slowdown, we will have to write a very fast symbolic binomial or something.  But all of these are an improvement on before.  Thanks for all of it!


---

Comment by hgranath created at 2009-09-22 15:01:39

Thanks for the tip, I did not know about the pyobject method. It
definitely improved performance in the symbolic case.

I hope I finally got everything right in version 5 of the patch!


---

Attachment

Unfortunately my Sage upgrade croaked, so I can't check it immediately.   I will try to do so as soon as possible.

However, what does this patch do with this?

```
sage: binomial(SR(3/2),SR(1/1))?
```

Trying x-m won't work on this.   Note that 

```
sage: type(SR(1/1).pyobject())
<type 'sage.rings.rational.Rational'>
```

which means you may still want a m=ZZ(m) or rational check once you have discovered you aren't in the n+1 case.   I may have that wrong, though, since I can't actually try the patch out.

As for a trivial point, there is a misspelling of "coerce" as well.


---

Comment by hgranath created at 2009-09-22 16:28:31

You are right, binomial(SR(3/2),SR(1/1)) actually worked (for other
reasons) but not e.g. binomial(3/2,SR(1/1)). Fixed in new version.


---

Attachment


---

Comment by kcrisman created at 2009-09-22 18:07:36

I get an odd doctest failure:


```
**********************************************************************
File "/Users/.../crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    222
Got:
    217
**********************************************************************
```

One might as well add a doctest for that last case you mentioned, too.  I'm rebasing your last patch to fix these, and putting positive review since I only changed the doctests so they pass.  I think we finally got it!


---

Attachment

Based on 4.1.2.alpha2; apply this patch only.


---

Comment by kcrisman created at 2009-09-22 18:09:24

Incidentally, in the future you may want to name your patches by Trac number and replace ones that are outdated.  Not a big deal, but I know if I don't say it then Minh will :)


---

Comment by mvngu created at 2009-09-24 11:07:18

set username to Hakan Granath


---

Attachment

The patch `trac_6870-final-v2.patch` is the same as `trac_6870-final.patch`. The only difference is that I have set the username to Hakan Granath. This is because `trac_6870-final.patch` is a rebase of Hakan's previous patches.


---

Comment by mvngu created at 2009-09-24 11:37:09

With `trac_6870-final-v2.patch`, I got the following doctest failure:

```
sage -t -long devel/sage/sage/crypto/boolean_function.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    217
Got:
    222
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py
	 [5.3 s]
```



---

Comment by hgranath created at 2009-09-24 11:48:23

I do not know what is happening with the file boolean_function.pyx, I can not find it in my version of sage (4.1.1).


---

Comment by kcrisman created at 2009-09-24 12:19:58

Yeah, I saw that, but couldn't figure out where it came from.  I don't think it's from this, because I got it in a branch without this patch.  Can you try that in a clean branch, Minh?

(Incidentally, this file is in 4.1.2.alpha2, at any rate.)


---

Comment by kcrisman created at 2009-09-24 12:20:51

And how do you DO that keeping the name the same thing?


---

Comment by kcrisman created at 2009-09-24 13:40:32

Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  

(Actually, I think it's a true one-liner, because that function depends on the current random state in Sage, and probably somewhere that got reset or changed, so that the "random" output isn't really that random. But I leave it the release manager to verify this and open a ticket.)


---

Attachment

fix 32- vs. 64-bit issue


---

Comment by mvngu created at 2009-09-26 05:48:39

Replying to [comment:20 kcrisman]:
> Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  
The doctest failure I got above is due to a 32- vs. 64-bit issue. On a 32-bit system, it would report 217. But on a 64-bit system, it would report 222. These results are consistent for all the machines I have tested on. See my doctest reports for Sage 4.1.2.alpha2:

 * 32- and 64-bit [Ubuntu](http://groups.google.com/group/sage-devel/browse_thread/thread/ec8e2958f394eb5b)
 * 32- and 64-bit [Mandriva](http://groups.google.com/group/sage-devel/browse_thread/thread/e61bb57a2637ba2e)
 * 32- and 64-bit [Debian](http://groups.google.com/group/sage-devel/browse_thread/thread/55d756fb80c94780)
 * 32- and 64-bit [Fedora](http://groups.google.com/group/sage-devel/browse_thread/thread/ff85e2965dc9e59b), [Red Hat, CentOS](http://groups.google.com/group/sage-devel/browse_thread/thread/4ddf1b90690d4cfa)
 * 32- and 64-bit [openSUSE](http://groups.google.com/group/sage-devel/browse_thread/thread/792bb7c3d1f662ef)
 * 32- and 64-bit [Mac OS X 10.5.8](http://groups.google.com/group/sage-devel/browse_thread/thread/954ecbadeb7676a8)
 
In all of the above reports, the doctest in question pass on 64-bit platforms, but fail on 32-bit platforms. I have attached the patch `trac_6870-bitness-issue.patch` which takes care of this bitness issue. It should be applied on top of `trac_6870-final-v2.patch`. If my patch is good, then everything is ready to be merged.


---

Comment by kcrisman created at 2009-09-27 00:32:26

I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  

In any case, I an unable to review that part of your patch.  I'm sorry :(


---

Comment by mvngu created at 2009-09-27 00:40:40

Replying to [comment:22 kcrisman]:
> I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  
> 
> In any case, I an unable to review that part of your patch.  I'm sorry :(
What you can do is get the patch `trac_6870-final-v2.patch` and remove the hunk:

```
1011	1011	        sage: B.nvariables() 
1012	1012	        9 
1013	1013	        sage: B.nonlinearity() 
1014	 	        222 
 	1014	        217 
1015	1015	    """ 
1016	1016	    from sage.misc.randstate import current_randstate 
1017	1017	    r = current_randstate().python_random() 
```

from that patch. The new patch would be the same as the original, only with changes to the file `sage/rings/arith.py`. As for my patch, you could open another ticket and put the patch there. That way, the patch won't be lost to history, and you could still review Hakan's changes to `sage/rings/arith.py`. As for the doctest failure in `sage/crypto/boolean_function.pyx`, you reference the new ticket from this ticket. How does that sound?


---

Attachment

The final patch.  No, really.


---

Comment by kcrisman created at 2009-09-27 00:54:45

That seems reasonable.

Okay, v2.2 should be it.  You can revert to positive review once you check it really does pass all tests - on my current machine, that would probably take 12 hours or so.

New ticket is #7020.


---

Comment by awebb created at 2009-09-30 07:43:22

The patch looks good to me too. Tested on 32 and 64 bit systems.  ~ Adam


---

Comment by mvngu created at 2009-09-30 08:26:28

Merged `trac_6870-final-v2.2.patch`.


---

Comment by mvngu created at 2009-09-30 08:26:28

Resolution: fixed
