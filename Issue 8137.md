# Issue 8137: Thomas R. Nicely's Hardy-Littlewood logarithmic integral approximations to counts of prime constellations

Issue created by migration from https://trac.sagemath.org/ticket/8137

Original creator: kevin.stueve

Original creation time: 2010-01-31 07:42:26

Assignee: Kevin Stueve

CC:  leif

Get Thomas R. Nicely's code for approximating the counts of twin primes and other primes into Sage.

The code can be found at http://www.trnicely.net/.

Sage already has a Li implementation, so all that needs to be added to Sage is code for the twin primes, prime triplets, and prime quadruplets.  However, Sage's default Li implementation uses direct numerical integration.  Maybe this should be switched out for an equivalent (and faster) series implementation.


---

Comment by kevin.stueve created at 2010-01-31 18:07:46

Take note of Remark 4 in Introduction to twin primes and Brun’s constant computation, by Pascal Sebah and Xavier Gourdon at numbers.computation.free.fr/Constants/constants.html (July 30, 2002)

"Remark 4 The function Li2 (n) occuring in (1) may be related to the logarithmic integral Li(n) by the trivial relation

                      Li2(n) = Li(n) +   2 / log(2) - n / log(n)."

Kevin Stueve


---

Comment by leif created at 2010-02-01 21:22:53

Replying to [comment:1 kevin.stueve]:
> Take note of Remark 4 in Introduction to twin primes and Brun’s constant computation, by Pascal Sebah and Xavier Gourdon at http://numbers.computation.free.fr/Constants/constants.html (July 30, 2002)

The specific web page http://numbers.computation.free.fr/Constants/Primes/twin.html is also available in PDF: http://numbers.computation.free.fr/Constants/Primes/twin.pdf, the mentioned remark is on page 5.
