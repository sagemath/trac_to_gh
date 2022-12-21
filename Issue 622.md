# Issue 622: SAGE's factor function is not provably correct

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-07 17:25:19

Assignee: somebody

In short, modify the factor function in SAGE to test primality with isprime of
all factors < 10**15.  The best place to put this is libs/pari/gen.pyx, by
modifying the isprime function there to have an extra proof flag that defaults
to True. 


```
On 9/7/07, Bill Hart <goodwillhart`@`googlemail.com> wrote:
>

>
> Are there other algorithms available in SAGE from Pari that rely on
> conjectures? This would include the stuff for totally real fields that
> relies on the Stark conjectures.

mwrank uses the pari library for factorization of integers, so the
correctness of mwrank funtions (and in particular, elliptic curve
ranks) relies on pari giving actual prime numbers when asked to
factor.

The pari manual says (about factor(x)):

If $x$ is of type integer or rational, the factors are \var{pseudoprimes}
(see \kbd{ispseudoprime}), and in general not rigorously proven primes. In
fact, any factor which is $\leq 10^{15}$ is a genuine prime number. Use
\kbd{isprime} to prove primality of other factors,

I would need to change the mwrank code to test "primes" > 10^15 for
primality as recommended.   A better solution would be to ask the pari
developers to add an optional "proof=true" flag to factor() which does
the isprime() calls automatically.  I will do that.
```



---

Comment by syazdani created at 2007-09-12 16:52:33

Changing assignee from somebody to was.


---

Attachment

this should fix the problem pretty well


---

Comment by was created at 2007-09-12 18:32:59

Resolution: fixed
