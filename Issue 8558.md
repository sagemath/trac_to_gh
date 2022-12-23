# Issue 8558: Make gcd use pari for univariate polynomial rings over number fields

Issue created by migration from https://trac.sagemath.org/ticket/8558

Original creator: lftabera

Original creation time: 2010-03-18 17:14:43

Assignee: AlexGhitza

CC:  slelievre

Keywords: gcd, pari, number field

Question arised here,

http://groups.google.com/group/sage-devel/browse_thread/thread/0f5b029970e1a4e2/fcec7d0e35474fbd#fcec7d0e35474fbd

univariate gcd is performed using euclidean algorithm, which causes explosion of coefficients and is slow but for trivial examples. Instead we should use pari that performs better.

1.- Add a _pari_ function for absolute number fields taht work

2.- Add gcd using pari for absolute number fields

3.- For relative number fields, pass to an absolute representation. This may be slow. But for the cases where this is slow the current implementation may be unfeasible.


---

Comment by lftabera created at 2010-03-18 17:15:12

Changing status from new to needs_work.


---

Comment by lftabera created at 2010-03-27 19:15:04

Changing keywords from "gcd, pari, number field" to "gcd, pari, ntl, number field".


---

Attachment

The pari algorithm is not fast enough. I have implemented a modular algorithm using ntl.

The patch needs doctest and integration in sage (it is, right now, a separate function).

It adds a new function modular_gcd

To test it, apply the patch and

from sage.rings.polynomial.polynomial_absolute_number_field import modular_gcd

Some timmings: (800 Mhz i386 linux, 1Gb ram)


```
sage: N.<a>=NumberField(x^3 -123)         
sage: K.<t>=N[]                           
sage: f=K.random_element(degree=2)        
sage: g1=K.random_element(degree=15)      
sage: g2=K.random_element(degree=15)      
sage: h1=f*g1                             
sage: h2=f*g2                             
sage: %time modular_gcd(h1,h2,'pari')     
CPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s
Wall time: 0.31 s                                 
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
sage: %time modular_gcd(h1,h2)                                                                                
CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s                                                            
Wall time: 0.12 s                                                                                             
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
sage: %time modular_gcd(h1,h2,'euclidean')                                                                    
CPU times: user 11.28 s, sys: 0.05 s, total: 11.33 s                                                          
Wall time: 12.21 s                                                                                            
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
```



```
sage: N.<a>=NumberField(x^10 - 123)
sage: K.<t>=N[]
sage: f=K.random_element(degree=2)
sage: g1=K.random_element(degree=15)
sage: g2=K.random_element(degree=15)
sage: h1=f*g1
sage: h2=f*g2
sage: %time l=modular_gcd(h1,h2,'pari')
CPU times: user 30.06 s, sys: 0.02 s, total: 30.07 s
Wall time: 32.15 s
sage: %time l=modular_gcd(h1,h2,'modular')
CPU times: user 0.43 s, sys: 0.00 s, total: 0.43 s
Wall time: 0.47 s
```



---

Comment by lftabera created at 2010-06-22 15:17:46

Here there is a cleaner patch.

The patch adds a new class of univariate polynomials whose ground field is an absolute number field. There is a new _gcd method for this class. It actually implements several approaches to the modular gcd algorithm:

Langemyr-McCallum algorithm
Encarnacion
a mixture of the two previous (default)

moreover, a call to pari method and the old Euclidean method.

I think that there should be only one modular algorithm, but, as usual, there are cases in which any of them beats the others. So suggestions are welcome. It should probably be Encarnacion or the mixture of boths

some timmings for harder problems:



```
sage: N = NumberField(ZZ[x].random_element(15).monic(),'a')    
sage: K = N[x]
sage: f = K.random_element(100)
sage: g1 = K.random_element(100)
sage: g2 = K.random_element(100)
sage: g1 *= f
sage: g2 *= f
sage: %time _=gcd(g1,g2)
CPU times: user 7.32 s, sys: 0.02 s, total: 7.34 s
Wall time: 7.42 s
```


This example with the old implementation or even pari is unfeasible.


---

Comment by lftabera created at 2010-06-22 15:17:46

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2010-06-24 14:06:49

- Improved documentation
- Eliminated an improvement in a function that hos nothing to do with the ticket


---

Comment by lftabera created at 2010-06-26 10:05:33

Added the method also for number fields of degree 1 using Flint in this special case


---

Attachment

Now that #4000 has possitive review, I raise the priority of this one.

Updated patch to work in 4.5.3

Now, it works also for relative number fields, passing to an absolute representation and performing there the computations. This is not optimal but it is usable.

If the extension of the field is one, then the gcd of QQ[x] is used wich is faster.


---

Comment by lftabera created at 2010-09-14 13:20:27

Changing priority from minor to major.


---

Attachment

I can confirm that the patch applies fine to 4.6.rc0 and all tests (including long) pass.

There are some minor problems with the documentation (just punctuation) -- now I am studying the code, since this looks like very useful functionality!


---

Comment by lftabera created at 2010-12-04 12:37:11

Some clean in the documentation, reorder of the methods (methods after the classes of the file) and a couple of small bugs (honor the method option for relative fields and duplicated code for degree 1 extensions). Rename correctly the patch.

Apply: trac-8558.patch

Try new buildbot  :)


---

Comment by davidloeffler created at 2011-01-19 16:13:13

Apply trac-8558.patch

(I think such messages have to come *after* the patch is uploaded)


---

Comment by lftabera created at 2011-03-28 10:45:29

avoid next_prime, better exceptions


---

Attachment


---

Comment by malb created at 2011-04-29 13:33:18

Changing status from needs_review to needs_info.


---

Comment by malb created at 2011-04-29 13:33:18

Hi, I don't know much about fast computation in polynomial rings over number fields. However, I'm wondering why you have this bias towards functions as opposed to methods? For example, `lift_pm` looks like it should be a method on `p` instead of a function? Perhaps the same applies to the gcd functions? Or am I missing something?


---

Comment by lftabera created at 2011-05-12 11:15:30

No bias intended. lift_pm can be a method and probably in more classes than polynomials in NTL.

I am reading again the code and it looks awful now. I think there are too many gcd alternatives with little gainamong them.

I will update the code.


---

Comment by lftabera created at 2011-06-10 11:24:05

Changing status from needs_info to needs_review.


---

Comment by lftabera created at 2011-06-10 11:24:05

Now the functions are methods.

lift_to_poly_ZZ and lift_to_poly_QQ are methods of ntl_ZZ_pEX

lift_pm is a method of ntl_ZZ_p

Still, I have left a lift_pm function in sage.rings.arith I think it is good for educational purposes in modular algorithms.

I have eliminated pure Encarnacion and pure Langemyr_McCallum methods. There is no real benefit compared to the extra code they add.


---

Comment by lftabera created at 2011-06-10 11:26:04

Apply: trac-8558.2.patch


---

Comment by lftabera created at 2011-08-24 17:00:49

rebase against 4.7.1


---

Comment by lftabera created at 2011-08-25 09:35:31

Apply: trac-8558.2.patch


---

Comment by jdemeyer created at 2011-10-15 12:25:56

Several comments:
 1. Why the name `lift_pm()`?  In PARI, this function is called `centerlift()` which is more understandable in my opinion.  On the other hand, having the name _begin_ with `lift` is more friendly for TAB-completion, so why not `lift_centered` or something?
 2. A special class for polynomials over number fields looks like a good idea, but please put it in a separate file `polynomial_number_field.pyx` instead of adding to `polynomial_element_generic.pyx`.
 3. I have a hard time understand the text below. What is `c`? What is `n`? Probably "reduction" is a better word than "project". And I also think the name `K` for a polynomial ring is badly chosen:

```
    def lift_to_poly_QQ(self,K):
        """
        Compute a lift of poly to K.
            
        INPUT:
    
        - K: an univariate polynomial ring over an absolute number field QQ[a].
        In order to make sense of this algorithm, the minimum polynomial of 'a'
        should project onto `c` modulo `m`.
      
        OUTPUT:
    
        -A polynomial in QQ[a] such that its projection coefficientwise is poly.
        This algorithm uses rational reconstruction, so it may fail.
```

 4. Why `_gcd()` instead of `gcd()`?
 5. Add some tests using the global `gcd()` function instead of always calling your `_gcd()` method.
 6. Thanks to #11904, the line
 {{{
 h1 = pari([coeff._pari_('y') for coeff in self.list()]).Polrev() 
 }}}
 can be changed to
 {{{
 h1 = pari(self)
 }}}
 7. This looks very fishy:
 {{{
 #Experimental bound IMPROVE
 }}}
 8. With
 {{{
 p = p.next_prime(False)
 }}}
 do you mean
 {{{
 p = p.next_prime(proof=False)
 }}}
 which is much clearer?
 9. I believe the keyword argument `algoritm=` is usually used instead of `method =` (note also the spacing!).


---

Comment by jdemeyer created at 2011-10-15 12:26:12

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2011-11-10 17:11:51

rebase 4.7.2 still needs work


---

Comment by lftabera created at 2013-02-24 13:19:00

Back to business.

I have updated the patch with Jeroen's suggestions. Still I have to do something with 


```
#Experimental bound IMPROVE
p = ZZ(3+min(2**255, (max(map(abs,Bound.list())).n()**(0.4)).floor())).next_prime(proof=False)
```


p is the first prime to perform a modular gcd. If p=2, we will have to use a lot of primes and will be inefficient. On the other hand, if p is too big, we lose the advantages of modular gcd. So we have to give a sane, intermediate default.

The prime above is based on some experiments I made two years ago, the idea is to use a prime such that we will have to use few modular gcd, but limiting our stating prime to the interval `[3, 2^255]`.

Ideas welcomed.


---

Comment by lftabera created at 2013-02-24 18:16:20

Apply trac-8558.2.patch


---

Comment by lftabera created at 2013-03-02 15:59:17

Still, we have to look for a sensible default starting prime p, but the rest of the ticket can be reviewed.

Further improvements for other tickets and for big degree polynomials (different tickets) could be

 * add a half-gcd algorithm for ntl_ZZ_p_EX class, ntl libraries do not provide one.
 * Improve a lot the test of having a gcd, remainder algorithm is slow.

Apply: trac-8558.2.patch


---

Comment by lftabera created at 2013-03-02 15:59:17

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2013-03-02 17:32:42

The patchbot wants to apply too many patches

Apply: trac-8558.2.patch


---

Comment by lftabera created at 2013-03-03 19:53:23

rebase to 5.8.beta2


---

Attachment

Apply: trac-8558.2.patch


---

Comment by lftabera created at 2013-03-08 20:38:49

Apply: trac-8558.2.2.patch


---

Comment by jdemeyer created at 2013-03-13 14:57:12

Some quick comments:
1. `_sig_on` and `_sig_off` are very deprecated and should be changed to `sig_on()` and `sig_off()` (#10115).
2. The change "somewhat" -> "somewha" clearly is a mistake.
3. [Documentation](http://sagemath.org/doc/developer/conventions.html#documentation-strings) and [library](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files) formatting must be fixed.
4. Could you replace `centerlift` by `lift_centered` in `sage/rings/finite_rings/integer_mod.pyx` for consistency?
5. As I already mentioned, replace `method =` by `algorithm=`
6. Since `QQ` is a unique parent, replace `base_ring != QQ` by `base_ring is not QQ`.
6. Remove `# There has to be a better way to do this, self.change_ring()` does not work.  I don't see any problem with that code.
6. It is better to use a `**kwds` argument for `sparse` and `implementation` in

```
def __init__(self, base_ring, name="x", sparse=False, element_class=None, implementation=None)
```



---

Comment by jdemeyer created at 2013-03-16 22:09:29

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2013-05-10 14:13:07

I have taken into acoount the suggestions. I have deprecated integer_mod.centerlift and have eliminated the PolynomialRing new classes, since they only differed from PolynomialRing_field in the element_class and ignored the sparse option.


---

Comment by lftabera created at 2013-05-10 14:13:07

Changing status from needs_work to needs_review.


---

Attachment

rebase to 5.13


---

Comment by lftabera created at 2013-12-20 12:28:32

Apply: trac-8558.2.2.patch​


---

Comment by jdemeyer created at 2014-01-06 16:57:31

Certainly looks in much better shape than it used to be, but I'm afraid I don't know enough NTL to completely review this. Why not split up this ticket in two? The first which adds the new classes and implements `gcd` via PARI and the second which implements the modular algorithm.


---

Comment by git created at 2014-02-10 15:27:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2014-02-10 16:07:19

I have split the ticket into three tickets for easier reviewer and to allow partial merging.


---

Comment by pbruin created at 2014-05-07 14:08:19

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-05-08 10:31:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-05-08 14:35:09

(I'm not sure if the merge conflict was caused by this ticket or one of its dependencies; I just reported what the patchbot told me.)

I don't really have time to review any of this at the moment, but I agree with earlier reviewers that this looks like a very nice addition.  I was just wondering whether it would make sense to do this via a `NumberField._gcd_univariate_polynomial()` method as introduced by #13442.  On the one hand, this would mean you didn't have to introduce new classes (potentially many of them: we have absolute and relative number fields, quadratic fields, cyclotomic fields, sparse and dense polynomials, who knows what other distinctions we'll have in the future).  On the other hand, the code of this ticket has already been written and #13442 is still at `needs_work`, so it probably isn't worth the effort for now.


---

Comment by lftabera created at 2014-05-09 07:31:38

Thanks anyway, this made me update my local branches :)

The code is ok, but the branch of patches is a little mess due to my poor "git-fu". As of now I think that it is more important to get the dependencies merged, they are much simpler and would allow to prepare cleaner patches for this ticket.

Concerning #13442, I had in mind an implementation of these rings as in ticket #10591, so it would be better to have different classes for polynomials over number fields. The long term goal would be to have nice multiple extensions without the need of computing a primitive element for basic arithmetic, IMO it would be faster than using singular (cf. #9541).


---

Comment by git created at 2014-11-16 16:45:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-21 12:30:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2015-05-22 10:00:07

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2015-12-03 17:25:30

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2015-12-03 17:25:30

After so much time, I want to check if the code needs refactoring.


---

Comment by git created at 2016-02-23 15:03:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2016-02-23 15:07:53

It works again with latest beta


---

Comment by lftabera created at 2016-02-23 15:07:53

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2016-03-16 13:30:42

- `.. NOTE:` -> `.. NOTE::`

- In the docstring of "lift_to_poly_QQ" it is written that "it may fail with a ``ValueError`` exception.". But there is only an example which gives an "ArithmeticError". So either fix the note or add a doctest.

- you should do more typing in Cython file (with `cdef`). For example, `cdef list lifted = []`. It will help cython to speed up loops including the loops. And if I am not mistaken, this syntax `for 0 <= i < r` is equivalent to `for i in range(r)` which is more Python friendly.

- the name `lift_to_poly_QQ` looks strange to me. What does the `QQ` stands for?

- Could you provide more examples why the situation is it better with this new algorithm?


---

Comment by git created at 2016-07-15 08:57:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2016-07-15 11:44:48

- I have added mor cdef, however, I cannot do that in polynomial_number_field since the class inherist from a python class. I was not able to cdef, rings or number field elements. The latter has at least two classes and I was not able to cdef the common parent.
- I have fixed types, more verbose method names, clean unusued variables.
- modular method can be further improved for high degree using half-gcd algorithms in ntl.

- Some more examples:

Pari seems to use either Euclid or some subresultant variation. I would expect pari to perform better when the gcd is big with respect to the degree of the inputs. Or, when the input has small degree.

The polynomials are generated with K.random_element() so small coefficients. This benefits pari.

Small extension, not impressing except for huge polynomials


```
sage: K=QQ[I]['x']
```



```
deg f, deg g, deg gcd, timeit pari, timeit modular
2, 2, 0, 111 µs, 176 µs
2, 2, 1, 173 µs, 360 µs
2, 2, 2, 185 µs, 466 µs

100, 100, 0, 30.6 ms, 7.06 ms
100, 100, 50, 22.5 ms, 34.7 ms
100, 100, 100, 4.82 ms, 6.58 ms

300, 300, 0, 1.8 s, 45.1 ms
300, 300, 150, 534 ms, 201 ms
300, 300, 300, 13.3 ms, 11.3 ms

1000, 1000, 100, 2min 52s, 2.07 s
```


A degree 3, easy extension


```
sage: R=NumberField(x^3-2,'a')['x']
```



```
deg f, deg g, deg gcd, timeit pari, timeit modular
2, 2, 0, 163 µs, 243 µs
2, 2, 1, 239 µs, 597 µs
2, 2, 2, 257 µs, 587 µs

100, 100, 0, 19 s, 11.2 ms (1000x faster)
100, 100, 50, 8.6 s, 47.3 ms (100x faster)
100, 100, 100, 6.57 ms, 11.9 ms (2x slower)

300, 300, 150, > 600 s, 403 ms
```


Tu support my claim that big coefficients benefits modular


```
sage: K=QQ[I]['x']
sage: f=K.random_element(2,10**10)
```



```
100, 100, 0, 282 ms, 6.92 ms
100, 100, 50, 117 ms, 15.4 ms
100, 100, 100, 4.69 ms, 5.01 ms
```



---

Comment by lftabera created at 2016-07-15 11:47:04

lift methods still need better documentation according to #18


---

Comment by lftabera created at 2016-07-15 11:47:04

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2016-07-15 12:23:52

If I were a pari developer reasing this, I would ask:  why not implement the algorithm in pari itself, rather than in Sage?


---

Comment by lftabera created at 2016-07-15 13:22:44

I am not a pari developer, it would certainly benefit more people than an implementation in Sage. I thought about an implementation in ntl, but I do not touch C++ since 15 years ago. Flint would also be a good place to put a similar code.

According to the documentation:

gcd uses:

* integers: use modified right-shift binary ("plus-minus" variant).

* univariate polynomials with coefficients in the same number field (in particular rational): use modular gcd algorithm.

* general polynomials: use the subresultant algorithm if coefficient explosion is likely (non modular coefficients).

So, it may be the case that we are not translating polynomials to the correct pari setting and so I get bad timings? It may be the case, in order not to compute the discriminant of the number field we are dealing with...


---

Comment by cremona created at 2016-07-15 13:43:38

One thing to watch when comparing timings with pari is that when Sage calls pari to compute class number s and units in a number field, unless Proof=False it assumes no hypothesis (like GRH) so is often a lot slower than the same thing done in pari, where the default is to assume everything (and you can ask for certification later).  This should be as issue if you only do basic number field arithmetic, but if you do anything which requires knowing the units or class group it can be quite significant.  You might want to try setting Proof=False in Sage and seeing if your timings change.


---

Comment by lftabera created at 2016-07-15 14:24:51

It it is not that, I only need basic arithmetic, at most, pari could be interested in the  discriminant, but I am working in QQ[I] in my examples. Which should be easy. 

I have tried to write polynomials in pure gp as

`f= Mod(3*y,y<sup>2-1)*x</sup>2+Mod(1,y<sup>2-1)*x+Mod(y,y</sup>2-1)`

or as 


```
w=quadgen(-4)
f= 3*w*x^2+1*x+w
```


in both cases I get bad timing. Reading the documentation now to see how to deal with polynomials with number field coefficients in pari...


---

Comment by git created at 2016-07-18 10:30:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2016-07-18 10:35:25

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2016-07-18 10:35:25

It looks that Pari is not really using a modular algorithm...

In any case, I have fixed the documentation, I have also fixed some heuristic assumptions about the primes. Do not use proof=False and be more conservative about the size of the primes. In principle, with proof=False we could try a composite number such that the gcd in the residue ring success but some prime factors are good and some are bad. Not sure if this is possible. Also, chinese remainder could potentially fail, in this case I think that can only happens if the gcd is already unfeasible by any method. But let's be conservative and use only failproof methods.


---

Comment by git created at 2018-03-09 16:44:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2018-06-28 09:19:05

Changing keywords from "gcd, pari, ntl, number field" to "gcd, pari, ntl, number field, days94".


---

Comment by git created at 2018-06-28 16:53:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2018-07-07 23:34:05

This code uses ntl ZZ_pEX while it should use the faster lzz_pEX for word-sized primes.


---

Comment by lftabera created at 2018-07-07 23:34:05

Changing status from needs_review to needs_work.


---

Comment by embray created at 2019-03-25 10:56:15

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)


---

Comment by embray created at 2019-06-14 14:50:27

Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).


---

Comment by git created at 2019-06-26 11:21:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by lftabera created at 2019-06-26 11:26:29

lzz_pEX is not interfaced in Sage, so that should be a different ticket.

Still, with latest ntl library the code should be even much faster since the modular gcds are subquadratic for these types.

develop merged.


---

Comment by lftabera created at 2019-06-26 11:26:29

Changing status from needs_work to needs_review.


---

Comment by slelievre created at 2019-06-30 12:22:11

Replying to [comment:69 lftabera]:
> lzz_pEX is not interfaced in Sage, so that should be a different ticket.

There is #8109 for that.


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by slabbe created at 2020-08-15 13:33:31

The branch has conflict with the sage develop branch since at least 9.1.beta7 according to the patchbot reports.


---

Comment by slabbe created at 2020-08-15 13:33:31

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.


---

Comment by git created at 2021-07-20 10:52:37

Branch pushed to git repo; I updated commit sha1. New commits:
