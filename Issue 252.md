# Issue 252: Make number fields work when polynomial not integral or not monic.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-08 17:49:51

Assignee: was

CC:  katestange bouillaguet

Make number fields work when polynomial not integral or not monic.


```
sage: R.<x> = QQ[]
sage: L.<b> = NumberField(x^2-1/2)
sage: L.discriminant()
Traceback (most recent call last):
...
gen.PariError:  (8)
```



---

Comment by cwitty created at 2007-10-09 04:31:42

You may find sage.rings.algebraic_real.clear_denominators() useful here.  (If so, the function should probably be moved to a more sensible place, and perhaps renamed.)


---

Comment by was created at 2007-10-21 01:59:03

The example above works.  But other things don't:


```
sage: R.<x> = QQ[]
sage: sage: L.<b> = NumberField(x^2-1/2)
sage: sage: L.discriminant()
8
sage: L.ring_of_integers()
boom
```



---

Comment by mabshoff created at 2008-09-04 17:32:54

Notice that #4041 is a duplicate of this ticket.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-07-20 19:56:32

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 19:56:32

Changing assignee from was to davidloeffler.


---

Comment by lftabera created at 2010-07-06 10:59:30

Another example from #9408


```
sage: L.<a,b> = QQ[i].relativize(1) #Ok
sage: L.<a,b> = QQ[i].relativize(1/2) #PariError
```



---

Comment by katestange created at 2011-02-16 16:57:59

At least the pari errors could be changed to "not implemented" messages in the meantime?  This is an error a new user may encounter.  It would help them to know immediately that the problem is all non-integral coefficients, so they can program around it, and to know that it is known to the developers.


---

Comment by jdemeyer created at 2011-10-09 11:03:44

I agree that fixing this would be very nice, but also would require completely reworking the number field code.  I think it is feasible, but do we really want to put that much effort into this?


---

Comment by lftabera created at 2011-10-09 12:35:33

I, for myself would like to see this fixed. I would fix this myself if I had time...

In any case, current situation in Sage is not admissible. If we decide not to fix this then, should we allow to define number fields with nonintegral generators? This would also mean a lot of effort.


---

Comment by was created at 2011-10-09 16:00:54

Replying to [comment:9 jdemeyer]:
> I agree that fixing this would be very nice, but also would require 
> completely reworking the number field code.  I think it is feasible,
> but do we really want to put that much effort into this?

I don't know about "we", but it is a total no brainer that this has to get done eventually.   It is certainly easier than writing the number field code in the first place, which was hard, but not that hard.


---

Comment by Bouillaguet created at 2013-02-19 20:45:34

Changing priority from minor to major.


---

Comment by Bouillaguet created at 2013-02-19 20:45:34

I just ran into this issue


---

Comment by pbruin created at 2015-04-17 22:03:47

In SageMath 6.7.beta1:

```
sage: R.<x> = QQ[]
sage: L.<b> = NumberField(x^2-1/2)
sage: L.discriminant()
8
sage: L.ring_of_integers()
Maximal Order in Number Field in b with defining polynomial x^2 - 1/2
```

However, there are still problems; see e.g. #18243.  We should make use of the fact that when one feeds a non-monic or non-integral polynomial `f` to PARI's `nfinit()`, it returns a pair `[nf, c]` where `nf` is an number field isomorphic to *Q*[_x_]/(_f_) and defined by a monic integral polynomial, and `c` is a root of `f` in `nf`.


---

Comment by pbruin created at 2015-06-19 20:23:40

This branch is work in progress; it does not solve #18243 yet, and there are probably other places where it should be checked that non-integral and/or non-monic polynomials are supported.


---

Comment by git created at 2015-06-22 20:40:20

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by pbruin created at 2015-06-22 20:41:49

The examples in #14164 and #18243 now work.  This is mostly finished, but it needs more doctests to show that number fields defined by non-monic and non-integral polynomials are supported.


---

Comment by git created at 2015-06-24 10:03:58

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by pbruin created at 2015-06-24 10:12:09

Changing status from new to needs_review.


---

Comment by git created at 2015-07-03 09:47:56

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2015-07-22 11:44:39

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by pbruin created at 2015-07-22 11:47:17

The above version fixes `composite_fields()` to correctly solve #14164 and #18243.


---

Comment by git created at 2015-08-21 07:50:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kartikv created at 2015-08-22 22:02:40

Changing status from needs_review to needs_work.


---

Comment by kartikv created at 2015-08-22 22:02:40

Something weird seems to be going on with factoring. This is "normal" behavior for a number field.

```
sage: F.<a> = NumberField(x^3+x+1)
sage: F(2).factor()
2
sage: F(3).factor()
(a^2 + a + 2) * (-a + 1)
sage: (a^2 + a + 2).factor()
a^2 + a + 2
sage: F.factor(3)
(Fractional ideal (a^2 + a + 2)) * (Fractional ideal (-a + 1))
sage: (-a+1).factor()
-a + 1
```


This is not.


```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: F(2).factor()
(-47*a^2 + 21*a - 93/2) * (-1/2*a^2 + 1/2*a)^2 * (1/2*a^2 + 1/2*a)
sage: F.factor(2)
(Fractional ideal (-1/2*a^2 + 1/2*a))^2 * (Fractional ideal (1/2*a^2 + 1/2*a))
sage: (-47*a^2 + 21*a - 93/2).norm()
-8192
sage: (-47*a^2 + 21*a - 93/2).factor()
(3718815975/16384*a^2 - 1336872061/16384*a + 7884913157/32768) * (-1/2*a^2 + 1/2*a)^14 * (1/2*a^2 + 1/2*a)^-1
sage: (1/2*a^2 + 1/2*a).factor()
(13/512*a^2 - 11/512*a - 7/256) * (-1/2*a^2 + 1/2*a)^-4
```


Somehow, it's not controlling primes over the leading coefficient properly...


---

Comment by pbruin created at 2015-08-24 13:29:02

The underlying problem seems to be converting PARI ideals in Hilbert normal form to Sage ideals:

```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: Fp = F.pari_nf()
sage: I = F.ideal(2)
sage: Ip = I.pari_hnf()
sage: fact = Fp.idealfactor(Ip)
sage: Jp = fact[0, 0]
sage: Fp.idealnorm(Jp)
2
sage: J = F.ideal(Jp)
sage: J.norm()
1/2             # should be 2, like Fp.idealnorm(Jp)
```



---

Comment by pbruin created at 2015-08-24 16:41:03

Actually the bug is in the conversion from PARI elements expressed on the integral basis:

```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: b = F.random_element()
sage: F(F.pari_nf().nfalgtobasis(b)) == b
False  # should be True
```

I'm working on a patch.


---

Comment by git created at 2015-08-24 17:16:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-08-24 17:17:16

Changing status from needs_work to needs_review.


---

Comment by kartikv created at 2015-08-24 17:53:43

Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.


---

Comment by kartikv created at 2015-08-24 17:53:43

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-08-25 11:38:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-25 11:40:47

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by pbruin created at 2015-08-25 11:43:43

Replying to [comment:33 kartikv]:
> Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.
Thanks for your comments.  If you approve of the new examples you can set this to positive review (and remember to fill in your [real] name as reviewer).


---

Comment by pbruin created at 2015-08-25 11:43:43

Changing status from needs_work to needs_review.


---

Comment by kartikv created at 2015-08-25 13:49:35

Changing status from needs_review to positive_review.


---

Comment by kartikv created at 2015-08-25 13:49:35

Perfect.


---

Comment by vbraun created at 2015-08-26 03:00:18

Resolution: fixed
