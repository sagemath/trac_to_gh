# Issue 3111: sage's new baby-step giant step evidently needs additional polish

Issue created by migration from https://trac.sagemath.org/ticket/3111

Original creator: was

Original creation time: 2008-05-06 16:07:05

Assignee: cremona

Paste this code into a Sage session:

```
E = EllipticCurve('389a')
for p in prime_range(10000):
    if p != 389:
       try:
           G = E.change_ring(GF(p)).abelian_group()
       except Exception, msg:
           print "p = %s fails"%p
           print msg
```


The output varies on run and computer.  Typical output looks like this:

```
p = 7 fails
No solution in bsgs()
p = 1901 fails

p = 4273 fails

p = 5101 fails

p = 7177 fails

p = 7433 fails

p = 9013 fails

p = 9049 fails

p = 9749 fails
```


The actual failures are assertion failures in the baby-step giant-step implementation.

 -- William


---

Comment by was created at 2008-05-06 16:10:14

Under OS X (10.5.1 intel core2 duo with 2GB RAM)
I also get a repeatable massive memory overflow that completely crashes Sage:

```
sage: E = EllipticCurve('389a')
sage: for p in prime_range(10000):
....:         if p != 389:
....:            try:
....:                G = E.change_ring(GF(p)).abelian_group()
....:        except Exception, msg:
....:                print "p = %s fails"%p
....:            print msg
....: 
p = 7 fails
No solution in bsgs()
p = 523 fails

p = 2477 fails

p = 3001 fails

p = 3449 fails


error: no more memory
System 5120k:5120k Appl 4637k/482k Malloc 4094k/1k Valloc 1024k/480k Pages 152/104 Regions 2:2

halt 14
teragon-2:sage-3.0.1 was$ 

```



Running this under gdb yields nothing useful:


```

error: no more memory
System 5116k:5116k Appl 4629k/486k Malloc 4086k/5k Valloc 1024k/481k Pages 152/104 Regions 2:2

halt 14

Program exited with code 016.
(gdb) bt
No stack.
```



---

Comment by was created at 2008-05-06 16:10:14

Changing priority from major to critical.


---

Comment by was created at 2008-05-06 16:11:19

NOte -- the above is not a leak between calls of abelian_group.  It's that one single calculation is somehow using up all memory and crashing sage.


---

Comment by mabshoff created at 2008-05-06 17:14:09

With Sage 3.0.1 on sage.math this seems rather harmless:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
28670 mabshoff  20   0  455m 141m  21m S    0  0.2   0:35.02 sage-ipython
29958 mabshoff  15   0 97.7m  24m 2060 S    0  0.0   0:03.67 python
28715 mabshoff  16   0  634m  14m 2096 S    0  0.0   0:02.27 gp
```

If for some dumb reason pari doubles the stack once more on OSX you are SOL. I tried on OSX 10.5 and I hit the same error. Now it sounds like a 64 bit OSX version of Sage would fix that issue, but .....

Cheers,

Michael


---

Comment by cremona created at 2008-05-06 21:07:45

Changing status from new to assigned.


---

Comment by cremona created at 2008-05-06 21:07:45

I found the bug which causes this.  It is not in any of the generic code at all, but in some lines I added quite late on in ell_finite_field.py to make one step (in code which happens relatively infrequently) "more efficient".  I'll post a patch on Wednesday.


---

Comment by cremona created at 2008-05-07 10:12:22

Two bugs fixed:

* A stupid rounding error in `ell_generic.Hasse_bounds()`   [NB the floor of 2*sqrt(q) is not 2*floor(sqrt(q))!]

* A more subtle bug in the abelian_group() function for curves over finite fields, in a bit of code added late on for "efficiency".  We now still have the efficiency but without the bug (at least, not that one).  The code in the original post now runs fine;  I also ran it up to `10***5` and for `GF(p^k)` up to `10^3` for `k=2,3,4,5`.

For the future: I still have some more plans for ell_finite_field in cases where j is not in the prime field.  Then, at present the only way we have to compute the cardinality is via the group structure, but for the majority of cases it should be easier to compute the cardinality only using Mestre's trick.  However, Mestre's trick (as stated and proved by Schoof's second JNTB paper) is usually stated over prime fields, and over non-prime fields of square size there is one situation where Mestre's trick does not work (specifically when q is a square and the Frobenius is an integer and the group order (and structure) is either `(sqrt(q)-1)**2` or `(sqrt(q)+1)**2`.)  

When I have worked out how best to detect that case there will be a new patch.  Until then, curves whose j is not in the prime field and which do not have cyclic groups run into the efficiency problem (fixed above but only when the cardinality is already known) where some rather large elliptic curve discrete logs may need to be computed.


---

Comment by craigcitro created at 2008-05-08 21:23:04

Hmm ... there doesn't seem to be a patch attached, despite the title saying "with patch." :)


---

Attachment

Sorry about that, it is there now.

And as I looked at the patch after uploading it I saw that there are a couple of debugging print statements which need deleting, near the end (lines 1194/5) but I'll leave that until tomorrow.


---

Comment by broune created at 2008-05-12 10:37:05

Doctests pass in ell_generic.py and ell_finite_field. No more printed failues when running code in ticket description (they were there before I applied the paths), though I also run out of memory on mac 10.5 with 2 GB ram. If this is not expected behavior it should be reported as a separate ticket. Positive review pending removal of debugging print statements.


---

Comment by craigcitro created at 2008-05-12 16:35:25

I think that we should also add at least one doctest showing that this behavior is fixed.


---

Comment by cremona created at 2008-05-12 21:24:26

Additional tp sage-3111.patch


---

Attachment

sage-3111-extra.patch does the following:

   * deleted two debuggin print lines
   * added doctest to show that the original post is fixed
   * passes all doctests in sage/schemes/elliptic_curves

For the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.


---

Comment by broune created at 2008-05-12 21:38:59

I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?


---

Comment by mabshoff created at 2008-05-12 21:41:36

Replying to [comment:10 cremona]:
> sage-3111-extra.patch does the following:
> 
>    * deleted two debuggin print lines
>    * added doctest to show that the original post is fixed
>    * passes all doctests in sage/schemes/elliptic_curves
> 
> For the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.

Hi John,

you could do two tests: 
 * a quick one that is run per default 
 * a long one marked with `#long` - 18 seconds is not a problem with long.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-12 21:43:07

Replying to [comment:11 broune]:
> I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?

Sage now uses the same seed per default for randomness at the start of each doctest, so it is reproducible. Not all sources of randomness have that property yet, but for primes it should work. So no need to stick `#random` in the doctest string.

Cheers,

Michael


---

Attachment

Apply after previous two


---

Comment by cremona created at 2008-05-12 21:49:53

Michael,

I have added an extra patch anyway -- my comment on it was killed by trac as you were editing at the same time )I thought trac would be cleverer than that!)

John


---

Comment by cremona created at 2008-05-12 21:51:09

If you still want the long test (all primes to 10000) I can add it tomorrow -- my bedtime now.


---

Comment by broune created at 2008-05-12 21:51:36

Sorry about the misinformation on random - it is good that Sage handles this nicely.

Runnning the doctest code for the 10 primes with an unpatched Sage does not trigger the bug after I tried it a few times on my machine. Ten primes just does not seem to be enough to hit the bug with high probability. It would be better to find some primes that always trigger the bug. I get different numbers failing on each run, except that 7 seems to show up every time. So it would be nice to check p=7 every time in the doctest, in addition to the random tests.


---

Attachment

apply after all previous


---

Comment by cremona created at 2008-05-13 08:22:11

Yet another patch sage-3111-extra3.patch now tests the original full code for primes to 10000 but this longer test is marked #long as it takes around 20s.

Apologies for the succession of small cumulative patches, Michael:  I only trust myself to do `hg_sage.export("tip")`.


---

Comment by cremona created at 2008-05-14 21:45:49

The phrase "needs minimal further review" resulted in this one not being listed by trac as a "needs review" ticket so I have changed that and hope that someone can oblige.  The extra patches do what was wanted by the orginal reviewer.


---

Comment by craigcitro created at 2008-06-02 07:59:18

This looks good. (I don't know how this slipped under the radar as long as it did.)


---

Comment by mabshoff created at 2008-06-04 18:54:32

Resolution: fixed


---

Comment by mabshoff created at 2008-06-04 18:54:32

Finally! Merged all four patches in Sage 3.0.3.alpha1
