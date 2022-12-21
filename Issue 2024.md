# Issue 2024: [with patch, needs review] univariate gcd over Z_N (N composite)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-01 11:51:40

Assignee: was

The attached patch implements GCDs for univariate polynomials over Z_N where N is composite by calling PARI.

*EXAMPLE*

A standard attack on textbook RSA due to Franklin and
Reiter: Consider that we are given two ciphertexts c<sub>1</sub>
and c<sub>2</sub> and the knowledge that the matching plaintexts
are related by m<sub>2</sub> = m<sub>1</sub> + 2<sup>10</sup>. We also know the public
key (N,e) and that e is rather small. Then we can
recover the plaintext using a GCD computation for two
univariate polynomials.

```
sage: N = 2157212598407
sage: e = 3
sage: c1 = 1429779991932
sage: c2 =  655688908482
sage: P.<x> = PolynomialRing(Zmod(N))
sage: f1 = x^e - c1
sage: f2 = (x+2^10)^e - c2
sage: g = gcd(f1,f2); g
x + 2155978030517
sage: m = -g[0]; m
1234567890
            
sage: m^e
1429779991932
```


Surprisingly, MAGMA cannot perform this operation:


```
sage: f1._magma_().GCD(f2._magma_())
Exception (click to the left for traceback):
...
Runtime error in 'GCD': Algorithm is not available for this kind of coefficient ring
```


The example is from http://www.isg.rhul.ac.uk/~sdg/mt466/lecture12.pdf which also claims that Mathematica cannot perform this operation.


---

Attachment

huh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.


---

Comment by ncalexan created at 2008-02-02 00:15:08

Replying to [comment:1 dmharvey]:
> huh? does gcd even make sense over this ring? `Z_N[x]` doesn't even have unique factorisation if N is composite.

I agree.  What is the gcd of `2 x` and `4 x` over `Z_8[x]`?  Should this return all divisors of largest degree?

As it stands, I think this patch should not be applied.


---

Comment by was created at 2008-02-02 05:55:18

I wrote `gcd(a,b)` for elements a,b in Z/NZ without further comment in an early version of my elementary number theory book, and when Brian Conrad saw that he went ballistic.  So I'm with you guys on now having this function unless its name is changed and the precise meaning of what is being computed is clarified.


---

Comment by malb created at 2008-02-02 14:31:47

replacement patch gcd -> common_divisor


---

Attachment

The attached patch renames `gcd` to `common_divisor` and adds some documentation. Also, some `_sig_on`/{{{_sig_off}}s were added to avoid zero divisions.


---

Comment by dmharvey created at 2008-02-02 22:52:15

Sorry, this still doesn't make much sense to me.

From the docstring:

```
Perform Euclid's algorithm and return a common divisor of 
\code{self} and \code{other} as a monic polynomial. This is 
similar to a GCD computation over a GCD domain.
```


Problems:

First, what is Euclid's algorithm here? For Euclid's algorithm you need a division algorithm, but I don't know what the division algorithm would be for `Z_N[x]` (at least when the divisor is not monic).

Second, sometimes there is *no* monic polynomial dividing both inputs. For example if N = 4, then 2x+1 is not divisible by *any* monic polynomial.

Third, what does the PARI documentation claim will happen when you call the gcd code over such a base ring? I'm too lazy to check. From memory, the NTL documentation specifically says that the modulus needs to be prime for any polynomial gcd routine. (I've had situations with a prime power modulus, where the gcd almost makes sense, but I still couldn't use the vanilla gcd routine, it would sometimes crash; I needed to write a p-adic gcd instead.)

You either need to specify precisely something that makes sense, or just bite the bullet and write in the docstring "this will call PARI's gcd routine and if the modulus is not prime then we don't promise anything and good luck to you". It seems that the reason you want to include this function at all is for the cryptographic application. That's fine (it's a nice application), but if we want this function in SAGE then it has to be something that mathematically make sense.


---

Comment by malb created at 2008-02-03 00:46:06

Resolution: invalid


---

Comment by malb created at 2008-02-03 00:46:06

> if we want this function in SAGE then it has to be something that mathematically
> make sense.

I agree. Because I cannot provide anything sensible due to time constraints and lack of background I withdraw the patch.


---

Comment by was created at 2008-02-03 00:50:23

What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?


---

Comment by malb created at 2008-02-03 00:54:33

Replying to [comment:8 was]:
> What about the rest of the patch, i.e., the stuff that isn't part of common_divisor?

Mhh, I realised that checking for `is_nilpotent` is not sufficient, so I wonder what exactly to check for, maybe: `any(not x.is_unit() for x in f)`? In any case `_sig_on`/`_sig_off`s need to be added somehow.


---

Comment by was created at 2008-02-03 01:16:20

Changing status from closed to reopened.


---

Comment by was created at 2008-02-03 01:16:20

Resolution changed from invalid to 


---

Comment by cremona created at 2008-02-16 20:53:16

The pari documentation just says that gcd uses the subresultant algorithm in this case.  It certainly does not give a run-time error:


```
? f=x^20-1
%8 = x^20 - 1
? g=x^25-1
%9 = x^25 - 1
? gcd(f,g)
%10 = x^5 - 1
? gcd(f*Mod(1,15),g*Mod(1,15))
%11 = Mod(1, 15)*x^5 + Mod(14, 15)
? lift(%)
%12 = x^5 + 14
```

But I agree with earlier contributors that unless we can define what the output is then we should not include this function.


---

Comment by dmharvey created at 2008-04-05 18:35:04

Closing this ticket, per IRC discussion with malb (see also #2497):


```
[2:20pm] dmharvey: ok I'm looking at the 2nd patch file
[2:20pm] dmharvey: basically consists of:
[2:20pm] dmharvey: (1) removing commented-out crud
[2:20pm] dmharvey: (2) adding a _sig_on/_sig_off somewhere
[2:20pm] dmharvey: (3) adding common_divisor which I don't know if I believe in
[2:20pm] dmharvey: (4) some right.is_nilpotent() tests
[2:20pm] malb: (3) is out
[2:20pm] dmharvey: ok
[2:21pm] dmharvey: so that's basically the guts of the ticket
[2:21pm] malb: I think (4) is not sufficient
[2:21pm] dmharvey: ok just hang on a second
[2:21pm] dmharvey: so do we agree the ticket is essentially invalid?
[2:21pm] malb: yes
[2:21pm] dmharvey: ok
[2:21pm] malb: I closed it before
[2:21pm] dmharvey: for (4), I don't understand what you're trying to do there
[2:22pm] malb: don't crash
[2:22pm] malb: that's all
[2:22pm] dmharvey: ah
[2:22pm] dmharvey: so ZZ_pX_DivRem can crash/.
[2:22pm] dmharvey: hmmm
[2:22pm] dmharvey: perhaps that should be a separate ticket anyway.
[2:22pm] malb: yep
[2:22pm] dmharvey: do you know how to make it crash?
[2:23pm] malb: so this one is invalid but we open another one for the crashes
[2:23pm] dmharvey: given how expensive ZZ_pX_DivRem is compared to setting up the signal handler, I'd be inclined to just call sig_on universally
[2:24pm] malb: sage: N = 35
[2:24pm] malb: sage: P.<x> = PolynomialRing(Zmod(N))
[2:24pm] malb: sage: 7*x//(5*x)
[2:24pm] malb: InvMod: inverse undefined
[2:24pm] malb: /usr/local/sage-2.11/local/bin/sage-sage: line 214: 30395 Aborted                sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
[2:24pm] malb: okay, I have no idea how expensive it is
[2:24pm] dmharvey: well, how expensive is _sig_on?
[2:24pm] malb: it is a system call
[2:25pm] malb: the siglongjmp
[2:25pm] dmharvey: and 5*x is not nilpotent :-)
[2:26pm] dmharvey: the Right Way to deal with this is to make NTL return error codes more nicely
[2:26pm] dmharvey: instead of aborting
[2:27pm] malb: yep
[2:28pm] malb: but that requires changing NTL
[2:28pm] dmharvey: malb: okay, I think the rest of the patch is probably not worth resurrecting. I will report that crash as a separate ticket (I have a feeling I've seen it before already?), and close #2024, does that sound ok?
[2:28pm] malb: yes
[2:28pm] dmharvey: yeah I think it's already #2497
[2:28pm] malb: ack
[2:29pm] dmharvey: ok I will do that
```



---

Comment by dmharvey created at 2008-04-05 18:35:04

Resolution: invalid
