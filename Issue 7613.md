# Issue 7613: twin prime class

Issue created by migration from Trac.

Original creator: kevin.stueve

Original creation time: 2009-12-06 12:11:06

Assignee: was

CC:  was robertwb georgsweber kevin.stueve ohanar victor leif

Keywords: twin primes counting, sieving

Twin primes are pairs of primes that differ by 2.  Currently the twin prime counting function, which counts the number of twin primes less than a given x, is not implemented in Sage, Mathematica, or other computer algebra systems.  Where it is calculated, the method used is mere sieving.

Use the approach of #7013 and #7539 to make a competitive (if not the only available as general purpose software) implementation of the twin prime counting function.  It should be at least 1000-10000 times faster than mere sieving.

(possible names are twin_prime_pi and prime_pi2).

Implement next_twin_prime, is_twin_prime, is_chen_prime, is_semi_prime functions

Other types of primes such as cousin primes, prime triplets, and sexy primes could also be considered.

Maybe could also try to compute partial sums of Brun's constant or prime harmonics sums.


---

Comment by kevin.stueve created at 2009-12-06 12:17:07

Computing the Twin Prime Counting Function

If anyone is looking for a project to do over winter break (or knows anyone who would enjoy this project), they should read this.  This is a great opportunity to make a significant contribution to Sage and the mathematics community in general.  I would do it myself, but I already have a project (graphical physics simulation) for this month.  Just make sure that multiple people don't independently make distinct implementations.

Twin primes are primes that differ by 2.  Primes are difficult enough to understand, but twin primes are to an even greater extent.  Many techniques used in studying primes do not carry over to twin primes.  For example, Euclid's proof of the infinitude of primes does not carry over to twin primes.  Infinitude of twin primes is the twin prime conjecture, one of Landau's problems.  It was reading about this problem in Calvin C. Clawson's Mathematical Mysteries, the Beauty and Magic of Numbers when I was in junior high-school that made me fall in love with number theory.

"""At the 1912 International Congress of Mathematicians, Edmund Landau listed four basic problems about primes. These problems were characterised in his speech as "unattackable at the present state of science" and are now known as Landau's problems. They are as follows:

   1. Goldbach's conjecture: Can every even integer greater than 2 be written as the sum of two primes?
   2. Twin prime conjecture: Are there infinitely many primes p such that p + 2 is prime?
   3. Legendre's conjecture: Does there always exist at least one prime between consecutive perfect squares?
   4. Are there infinitely many primes p such that p − 1 is a perfect square? In other words: Are there infinitely many primes of the form n2 + 1?

As of 2009, all four problems are unresolved."""
http://en.wikipedia.org/wiki/Landau%27s_problems

Modeling the distribution of twin primes probabilistically (as done by the prime number theorem), produces convincing evidence (but not proof) of the twin prime conjecture.  There is even a twin prime analogue to the logarithmic integral.
"# Li_2(x) = integral(2*c_2/(ln t)^2, t, 2, x), the Hardy-Littlewood integral approximation for pi_2(x). Although this is the traditional formula, note that a slightly more accurate (for small x) approximation is produced by the asymptotically equivalent formula Li_2*(x) = integral(2*c_2/((ln(t+6))^2), t, 2, x) .
# c_2 = Hardy-Littlewood constant for twins = 0.66016 18158 46869 57392 78121 10014 55577 84326 23.... The kth Hardy-Littlewood constant (k > 1) is defined as c_k = prod((p<sup>(k-1))*(p-k)/(p-1)</sup>k, p; p prime, p > k) . The value c_2 is also referred to as the twin-primes constant; however, some authors use 2*c_2 as the twin-primes constant."
Thomas R. Nicely
http://www.trnicely.net/twins/t2_0000.htm

According to Jeffrey Lagarias, Victor Miller, and Andrew Odlyzko's 1985 paper "Computing pi(x): The Meissel-Lehmer Method" (where a record breaking value of the prime counting function was published that used a new essentially O(x^(2/3)) algorithm)
"Legendre [born 1752] was the first to suggest a method of calculating pi(x) without locating all the primes less than x."
http://www.dtc.umn.edu/~odlyzko/doc/arch/meissel.lehmer.pdf

Since then, many improved methods of calculating the prime counting function have been developed that require less time, including the analytic method and a variant of the hybrid table look-up sieving method of Andrew Booker (http://primes.utm.edu/nthprime/) implemented by myself and Andrew Ohana under William Stein's direction in #7013 (together with many others, the most recent being Leif Leonhardy providing bug fixes, optimizations, and valuable insight see #7539).  The table/sieving and analytic methods produce quadratic speedup over locating each individual prime (under asymptotic analysis they run in essentially O(sqrt(x)) time, where we are counting primes less than x).

But there is no Legendre's formula, no LMO combinatorial method, no analytic method for calculating the twin prime counting function (the number of twin primes less than a given magnitude)-the methods simply do no carry over.  According to Tomás Oliveira e Silva (Universidade de Aveiro, Portugal) (who calculated the current record largest value of the prime counting function, prime_pi(10**23) and wrote the Sieve of Eratosthenes used in #7013 / #7539), 
"the only know[n] way to count the number of twin prime pairs with p<=x, denoted by pi2(x), is to enumerate them all."
http://www.ieeta.pt/~tos/primes.html

That is why applying the hybrid table look-up sieving algorithm to calculating the twin prime counting function would be so valuable.  It would convert the time complexity status of computing the twin prime counting function from that of the prime counting function in ancient Greece, counting each prime individually (before Legendre came along in the 18th century) to its status today after the discovery of the LMO combinatorial method, the analytic method, and the table/sieving method.

Look at the absolutely beautiful graphs of the twin prime counting function at http://curvebank.calstatela.edu/prime/prime.htm.

Results concerning how small the gaps between primes can be (representing progress toward the twin prime conjecture) have been made as recently as 2005.
"Small Gaps between Primes Exist"
http://arxiv.org/abs/math.NT/0505300

This prompted a Nova science now segment on twin primes (and a song).
http://www.pbs.org/wgbh/nova/sciencenow/3302/02.html

Some additional resources you (whoever takes on this project) will most likely find valuable for this project are:

Some Results of Computational Research in Prime Numbers (Computational Number Theory)
Thomas R. Nicely 
http://www.trnicely.net/index.html
(Provides extensive tables of various prime counting functions (including twin primes, prime triplets, and prime quadruplets), various logarithmic integral approximations, and errors between the approximations and the true values)

Tables of values of pi(x) and of pi2(x)
Tomás Oliveira e Silva
http://www.ieeta.pt/~tos/primes.html
(Provides extensive tables of the the twin prime counting function)

You may like to modify the modified [by myself, Andrew Ohana, and Leif Leonhardy] fast segmented sieve of Eratosthenes written by Tomás Oliveira e Silva at #7539 to sieve out not just non-primes but also non twin primes (for example, it might be that instead of sieving out just multiples of p, you also sieve out numbers two less than each multiple of p).  You may wish to find another sieve and modify it to count twin primes.  You may wish to find a sieve that is designed to find twin primes and optimize it for the purposes of this project.  You may wish to write the sieve from scratch.  What is important is that it is fast and robust.

Some may worry that what I am proposing will add too much to the Sage tarball.  Not to worry, the storage requirements for the tables of offsets between prime_pi2(x) and prime_pi2_approx(x) will be significantly smaller than that for prime_pi(x).  First of all, the twin prime counting function, prime_pi2 (or should it be called twin_prime_pi?) is little-oh of prime_pi.  For example, prime_pi(10**15) = 29,844,570,422,669 and twin_prime_pi(10**15) =1,177,209,242,304 (a small but noteworthy difference in storage).  Secondly the logarithmic integral approximations seem to be essentially square root accurate (the difference for this example is -750443.3188), halving the storage space (if you are able to find or come up with some code to calculate/approximate these integrals) as is the case with storing the offset between Li and pi in #7013.  Third, and most important, because the twin prime counting function is harder to calculate than the prime counting function (tables can only be generated by sieving, there is no known analogue of the combinatorial method), the tables of twin_prime_pi have significantly fewer values than those of prime_pi.

For a comparison of the number of entries in an available table of values of prime_pi and twin_prime_pi, consider that the spacing between table entries in the prime_pi tables (from http://www.primefan.ru/stuff/primes/table.html, the ones used in #7013) between 10^14 and 10^15 is 10^10 and that the spacing between entries in the twin_prime_pi tables (from http://www.ieeta.pt/~tos/primes.html) in the same interval is 10^11, a factor of 10 difference.

So the speed of twin_prime_pi won't be quite as spectacular as that of prime_pi, however, considering that (to the best of my knowledge) neither Sage nor Mathematica nor any other CAS currently implements a twin_prime_pi function (not to mention one that doesn't just enumerate twin primes), twin_prime_pi being 10 times slower than prime_pi (and up to an additional factor of 2 slower from having to sieve for p and p+2) is not really that bad.  What is 2.5-5 minutes spent sieving an interval of length 10^11 instead of 15 seconds sieving an interval of size 10^10 when the conventional wisdom would be to sieve all the way from 1 to 10^14 or 10^15.  There is a potential speed-up of 10^5 or more here over mere sieving.

There is currently ground-breaking research being performed regarding the twin primes, and the possibility exists that a proof of the twin prime conjecture is close.  I think that implementing a fast twin_prime class would be a step in the right direction, especially when such a class could aid those attempting to prove the twin prime conjecture.  One example of what could be done is making a histogram of the error between twin_prime_pi and twin_prime_pi_approx in an arbitrary interval that is currently beyond the reach of those using mere sieving unless they have weeks to wait or a distributed computing center.  Imagine how you would feel if it was your code that helped make it easier for someone attempting to prove the twin prime conjecture to have a breakthrough.

If you are feeling really ambitious you could also implement a counting function for other prime counting functions, such as cousin primes or prime triplets.

If you complete this project soon enough, I would love to collaborate for a combined research paper with that for #7013.

Best of Luck
Kevin Stueve


---

Comment by was created at 2009-12-07 06:51:05

You could make some of these functions methods of the Primes() object:

```
sage: P = Primes(); P
Set of all prime numbers: 2, 3, 5, 7, ...
```


So

```
sage: P.twin_prime_pi(1000)
...
sage: P.prime_pi2(1000)
...
```


This would help gather these functions together so it is easy to find, etc.


---

Comment by kevin.stueve created at 2009-12-10 22:36:31

After thinking about this some more, this problem seems easier than I had first realized.  You do not need to sieve out all non twin primes to calculate the twin prime counting function.

As sieving is likely much more computationally demanding than iterating over a bit array, it would be a better to sieve out primes, then iterate through your bit array, noting each twin prime, prime triplet, etc as the case may be.

Kevin Stueve


---

Comment by bascorp2 created at 2010-05-26 08:41:09

[rihanna pictures](http://top20search.biz/)
