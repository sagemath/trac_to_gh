# Issue 2424: [with patch, needs review] small roots method for polynomials mod N (N composite)

Issue created by migration from https://trac.sagemath.org/ticket/2424

Original creator: malb

Original creation time: 2008-03-07 22:43:01

Assignee: was

CC:  dmharvey

The attached patch implements ... well, lets just look at the docstring:

```
Let $N$ be the characteristic of the base ring this polynomial
is defined over: \code{N = self.base_ring().characteristic()}.
This method returns small roots of this polynomial modulo some
factor $b$ of $N$ with the constraint that $b >= N^\beta$.
Small in this context means that if $x$ is a root of $f$ modulo
$b$ then $|x| < X$.  This $X$ is either provided by the user or
the maximum $X$ is chosen such that this algorithm terminates in
polynomial time. If $X$ is chosen automatically it is $X =
N^{\beta^2/\delta - \epsilon}$.`This algorithm` in this context
means Coppersmith's algorithm for finding small roots using the
LLL algorithm. The implementation of this algorithm follows
Alexander May's PhD thesis referenced below.

INPUT:
    X -- an absolute bound for the root (default: see above)
    beta -- compute a root mod $b$ where $b$ is a factor of $N$
             and $b >= N^\beta$.  (default: 1.0 => $b = N$)
    **kwds -- passed through to LLL method of
              \code{Matrix_integer_dense}.

EXAMPLES:

First consider a small example:

    sage: N = 10001
    sage: K = Zmod(10001)
    sage: P.<x> = PolynomialRing(K)
    sage: f = x^3 + 10*x^2 + 5000*x - 222

This polynomial is irreducible of $K$

    sage: f.is_irreducible()
    True

and has no roots without modular reduction (i.e. over $\mathbb{ZZ}$):

    sage: f.change_ring(ZZ).roots()
    []

To compute its roots we need to factor the modulus $N$ and use
the chinese remainder theorem:

    sage: p,q = map(lambda (r,m): r, N.factor())
    sage: f.change_ring(GF(p)).roots()
    [(4, 1)]
    sage: f.change_ring(GF(q)).roots()
    [(4, 1)]

    sage: crt(4, 4, p, q) 
    4

This root is quite small compared to $N$ so we can attempt to
recover it without factoring $N$ using Coppersmith's small root
method:

   sage: f.small_roots()
   [4]

An application of this method is to consider RSA. We are using
512-bit RSA with public exponent $e=3$ to encrypt a 56-bit DES
key. Because it would be easy to attack this setting if no
padding was used we pad the key $K$ with 1s to get a large
number.

    sage: Nbits, Kbits = 512, 56
    sage: e = 3

We choose two primes of size 256-bit each.

    sage: p = 2^256 + 2^8 + 2^5 + 2^3 + 1
    sage: q = 2^256 + 2^8 + 2^5 + 2^3 + 2^2 + 1
    sage: N = p*q
    sage: ZmodN = Zmod( N )

We choose a random key

    sage: K = ZZ.random_element(0, 2^Kbits)

and pad it with 512-56=456 1s

    sage: Kdigits = K.digits()
    sage: M = [0]*Kbits + [1]*(Nbits-Kbits)
    sage: for i in range(len(Kdigits)): M[i] = Kdigits[i]

    sage: M = ZZ(M, 2)

Now we encrypt the resulting message:

    sage: C = ZmodN(M)^e

To recover $K$ we consider the following polynomial modulo $N$:

    sage: P.<x> = PolynomialRing(ZmodN)
    sage: f = (2^Nbits - 2^Kbits + x)^e - C

and recover its small roots:

    sage: Kbar = f.small_roots()[0]
    sage: K == Kbar
    True

The same algorithm can be used to factor $N = pq$ if partial
knowledge about $q$ is available. This example is from the MAGMA
handbook:

First, we set up $p$,$q$ and $N$.

    sage: length = 512
    sage: hidden = 110
    sage: p = next_prime(2^int(round(length/2)))
    sage: q = next_prime( round(pi.n()*p) )
    sage: N = p*q

Now we disturb the low 110 bits of $q$

     sage: qbar = q + ZZ.random_element(0,2^hidden-1)

And try to recover $q$ from it:

     sage: F.<x> = PolynomialRing(Zmod(N))
     sage: f = x - qbar

We know that the error is $<= 2^{hidden}-1$ and that the modulus
we are looking for is $>= sqrt(N)$.

     sage: set_verbose(2)
     sage: d = f.small_roots(X=2^hidden-1, beta=0.5)[0]
     verbose 2 (<module>) m = 4
     verbose 2 (<module>) t = 4
     verbose 2 (<module>) X = 1298074214633706907132624082305023
     verbose 1 (<module>) LLL of 8x8 matrix (algorithm fpLLL:wrapper)
     verbose 1 (<module>) LLL finished (time = 0.0...)
     sage: q == qbar - d
     True

REFERENCES:
    Don Coppersmith. Finding a small root of a univariate
        modular equation.  In Advances in Cryptology, EuroCrypt
        1996, volume 1070 of Lecture Notes in Computer Science,
        p. 155--165. Springer, 1996.
        http://cr.yp.to/bib/2001/coppersmith.pdf

  Alexander May. New RSA Vulnerabilities Using Lattice Reduction
        Methods.  PhD thesis, University of Paderborn, 2003
        http://www.informatik.tu-darmstadt.de/KP/publications/03/bp.ps
```


Why should this function be in Sage?
 * Magma has it ;-)
 * It is of some importance in cryptography


---

Attachment

this patch addresses a concern raised by David via private communication


---

Comment by dmharvey created at 2008-03-12 17:37:34

I can't comment on the mathematical correctness, but the patch looks good otherwise, and the examples are nice. Martin: if you can find someone else who knows about this stuff and is willing to look over the code, that would be good. Otherwise, if we don't have anyone else on the team with this expertise, let's just merge it in.


---

Comment by wdj created at 2008-03-13 02:53:41

Doesn't this seem like there is an error in the code?


```
sage: R.<x> = PolynomialRing(IntegerModRing(6),"x")
sage: f = x*(x-5)*(x-1)
sage: [f(i) for i in range(6)]
[0, 0, 0, 0, 0, 0]
sage: f.small_roots()
[]
```

Seems obviously wrong, compared to

```
sage: f = (x-1)*(x-2)
sage: [f(i) for i in range(6)]
[2, 0, 0, 2, 0, 0]
sage: f.small_roots()
[2, 1, -1, -2]
```

which seems right, but with a non-standard way of representing elements
in ZZ/6ZZ:

```
sage: IntegerModRing(6).list()
[0, 1, 2, 3, 4, 5]
```

It's also possible I'm completely overlooking something obvious.


---

Comment by malb created at 2008-03-13 09:55:13

Coppersmith's method certainly isn't designed for such very small $N=6$. Note, that Magma gives similar answers:


```
sage: R.<x> = PolynomialRing(IntegerModRing(6),"x")
sage: f = x*(x-5)*(x-1)
sage: f.small_roots()
[]
sage: fM = f.change_ring(ZZ)._magma_()
sage: fM.SmallRoots(6,1)
<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[52] := SmallRoots(_sage_[49],_sage_[50],_sage_[51]);
OUT:
>> _sage_[52] := SmallRoots(_sage_[49],_sage_[50],_sage_[51]);
                           ^
Runtime error in 'SmallRoots': X is too large
```


and 


```
sage: R.<x> = PolynomialRing(IntegerModRing(6),"x")
sage: f = (x-1)*(x-2)
sage: f.small_roots()
[2, 1, -1, -2]
sage: fM = f.change_ring(ZZ)._magma_()
sage: fM.SmallRoots(6,1)
[ -1 ]
```


But there is at least one bug in my code, the return type is `Integer`.


---

Comment by malb created at 2008-03-13 09:59:32

apply on top of coppersmith.patch (fixes issue discovered by wdj)


---

Attachment

this patch adapts the bound X such that the examples of David Joyner work


---

Comment by malb created at 2008-03-14 11:53:56

I've attached a new patch which fixes the issue reported by David Joyner above:


```
sage: R.<x> = PolynomialRing(IntegerModRing(6),"x")
sage: f = x*(x-5)*(x-1)
sage: f.small_roots()
[0, 1, 5]
```



---

Comment by malb created at 2008-03-18 15:53:22

Review by Bill Hart via private communication:

I think the algorithm will fail if the content of f is not coprime to
N. Since f is reduced mod N, this implies that a non-trivial factor of
N has been found, but should be checked for by taking the GCD of the
content and N.

The polynomial should be made monic by multiplying by an inverse of
its leading coefficient if it isn't monic. If the user tries to run
this algorithm on a non-monic f, I believe that the results are
undefined.

Furthermore, failure to compute such an inverse of the leading
coefficient would imply a factorisation of N, which again, should
technically be checked for. Obviously it is highly unlikely if N is
large, as it should be. But if this algorithm gets used in unintended
ways, it should still operate.

I see that you need the parameter epsilon to be less than beta/7, but
I am wondering why you choose it fixed at beta/8 rather than allow it
to be set by the user as a parameter and let epsilon have a default
value of beta/7?

What happens if the user enters a value of beta which is negative or
greater than 1 (t for example will then be negative)?

Currently if the user inputs a value of beta with beta <= deg(f)/8
then X gets set to 1.

Is LLL always guaranteed to return the vectors in order of length,
since the algorithm relies on using the shortest of the LLL reduced
basis vectors?

The algorithm, as currently implemented, may return values which are
not roots of the original polynomial f. You need to implement the rest
of step 4 on page 37 of the thesis.

The value of X should use the 1/2 factor as on page 34. The technique
of Coppersmith is proven to return the roots below the bound, however
the proof relies on the factor of 1/2 on page 36 (about 2/3 of the way
down). Unless it can be reproved without the factor of 1/2 it should
be used in the implementation.


---

Comment by malb created at 2008-03-19 11:32:34

patch addresses review remarks by Bill Hart


---

Attachment

Replying to [comment:7 malb]:
> I think the algorithm will fail if the content of f is not coprime to
> N. Since f is reduced mod N, this implies that a non-trivial factor of
> N has been found, but should be checked for by taking the GCD of the
> content and N.
> 
> The polynomial should be made monic by multiplying by an inverse of
> its leading coefficient if it isn't monic. If the user tries to run
> this algorithm on a non-monic f, I believe that the results are
> undefined.
> 
> Furthermore, failure to compute such an inverse of the leading
> coefficient would imply a factorisation of N, which again, should
> technically be checked for. Obviously it is highly unlikely if N is
> large, as it should be. But if this algorithm gets used in unintended
> ways, it should still operate.

All this should be addressed by raising an error if the polynomial is not monic (including the content remark). We don't make the polynomial monic because this way the user has full control and can use the fact of being lucky and just having split N.
 
> I see that you need the parameter epsilon to be less than beta/7, but
> I am wondering why you choose it fixed at beta/8 rather than allow it
> to be set by the user as a parameter and let epsilon have a default
> value of beta/7?

Updated accordingly.

> What happens if the user enters a value of beta which is negative or
> greater than 1 (t for example will then be negative)?
>
> Currently if the user inputs a value of beta with beta <= deg(f)/8
> then X gets set to 1.

The bounds are now enforced.
 
> Is LLL always guaranteed to return the vectors in order of length,
> since the algorithm relies on using the shortest of the LLL reduced
> basis vectors?

Yes.

> The algorithm, as currently implemented, may return values which are
> not roots of the original polynomial f. You need to implement the rest
> of step 4 on page 37 of the thesis.

Woops & updated accordingly.

> The value of X should use the 1/2 factor as on page 34. The technique
> of Coppersmith is proven to return the roots below the bound, however
> the proof relies on the factor of 1/2 on page 36 (about 2/3 of the way
> down). Unless it can be reproved without the factor of 1/2 it should
> be used in the implementation.

Fixed. However, I was under the impression that Magma does something different here. In any case, the user can supply his/her own X.


---

Comment by dmharvey created at 2008-03-19 21:18:59

Ummmm. The docstring says default value for epsilon is beta/8. But in the code it selects beta/7. Also, Bill seems to suggest above that epsilon needs to be less than beta/7 (or was it beta/8?) but this is not enforced anywhere in the code.


---

Comment by malb created at 2008-03-19 21:35:36

Replying to [comment:9 dmharvey]:
> Ummmm. The docstring says default value for epsilon is beta/8. But in the code it selects beta/7. 

Fixed in `small_roots_epsilon.patch`.

> Also, Bill seems to suggest above that epsilon needs to be less than beta/7 (or was it beta/8?) but this is not enforced anywhere in the code.

AFAIK, it doesn't need to be smaller than beta/7 but in my old code I assumed it was. The choice of epsilon is somewhat arbitrary ("choose an epsilon.").


---

Attachment


---

Comment by dmharvey created at 2008-03-19 21:47:19

Thumbs up from me.

(Thanks Bill Hart for doing the hard work in this review.)


---

Comment by mabshoff created at 2008-03-20 04:51:55

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 04:51:55

Merged all five patches in Sage 2.11.alpha0 - great work everybody.
