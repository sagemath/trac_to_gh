# Issue 4627: CRT_list in HNF dominates computation

Issue created by migration from https://trac.sagemath.org/ticket/4627

Original creator: ncalexan

Original creation time: 2008-11-26 19:06:10

Assignee: was

Keywords: hermite normal form hnf gcd


```
On 4-Sep-08, at 3:57 PM, Clement Pernet wrote:

Hi,

No problem, the patch looks fine, and I will run some testings to check
it. Nick, are you going to open a ticket?

--
Clément

William Stein a écrit :
On Wed, Sep 3, 2008 at 4:39 PM, Nick Alexander <ncalexander@gmail.com> wrote:
Hi William,

The attached patch prevents recomputing a CRT a number of times when doing a
multi modular Hermite normal form.  I was finding that this CRT computation
was taking *much* longer than the rest of the calculation of a midsize HNF
(40 x 40).  Has this been addressed?

No.

 Should this be run by Clement and some
randomized testing?

Yes, definitely.   I've cc'd Clement and included the attachment.

-- William
```



---

Attachment

What is the credit situation here?

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-27 00:23:07

So this code looks fine to me, but I can't find any cases where it makes a significant change in runtime. For instance, taking a random 40x40 matrix over ZZ, the runtimes are the same before and after the patch. 

Nick, what is a good test case to see the performance improvement?


---

Attachment


---

Comment by craigcitro created at 2008-11-27 04:21:01

Looks good! Nick pointed out a nice example of a test case:

BEFORE:

```
sage: y = polygen(ZZ)
sage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)
sage: time M.ideal(prod(prime_range(6000,6200))).free_module()
CPU times: user 33.71 s, sys: 2.02 s, total: 35.73 s
Wall time: 36.06 s

Free module of degree 20 and rank 20 over Integer Ring
User basis matrix:
20 x 20 dense matrix over Rational Field
```


AFTER:

```
sage: y = polygen(ZZ)
sage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)
sage: time M.ideal(prod(prime_range(6000,6200))).free_module()
CPU times: user 0.65 s, sys: 0.05 s, total: 0.70 s
Wall time: 0.70 s

Free module of degree 20 and rank 20 over Integer Ring
User basis matrix:
20 x 20 dense matrix over Rational Field
```


Speedup of 50X -- not too shabby! In particular, it seems to apply when you have really large coefficients compared to the size of the matrix. (This seems reasonable, given that for small entries, the CRT simply doesn't get applied that many times, since one has a bound on the size of the output.)

I added another doctest (which really needs compared between versions with `%timeit`), and committed the patch in Nick's name.


---

Comment by mabshoff created at 2008-11-27 04:48:23

Merged trac-4627-v2.patch in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 04:48:23

Resolution: fixed
