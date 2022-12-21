# Issue 1359: implement cyclotomic norm residues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-02 02:52:02

Assignee: was

Here's the code, basically:

bug day 6 -- #1342
system:sage


```
K.<zeta> = CyclotomicField(7)
```



```
def norm_symbol_prime(a, P):
     K = P.number_field()
     zeta = K.gen()
     n = K.zeta_order()
     exponent = (1/n) * ( P.norm() - 1)
     exponent = ZZ(exponent)
     FF = K.residue_field(P)
     aa = FF(a)
     b = FF(a)^exponent
     zeta_mod = FF(zeta)
     # Find power m of zeta_mod that is equal to b, then
     # return zeta^m
     m = 0
     w = FF(1)
     while w != b:
         w = w * zeta_mod
         m += 1
         assert m <= n, "bug in norm_symbol_prime"
     return zeta^m

def norm_symbol(a, b):
     F = K.fractional_ideal([b]).factor()
     return prod([norm_symbol_prime(a, P)^e for P, e in F],
               K(1))
```



```
norm_symbol(zeta^3, 13*zeta)
///
-zeta^5 - zeta^4 - zeta^3 - zeta^2 - zeta - 1
```



```
norm_symbol(zeta^7, K(11))
///
1
```



```
norm_symbol((1+zeta)^2, 23*zeta)
///
zeta^4
```




---

Comment by davidloeffler created at 2009-07-20 20:00:53

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 20:00:53

Changing assignee from was to davidloeffler.


---

Comment by jdemeyer created at 2011-10-09 11:08:22

Please explain what are "cyclotomic norm residues".


---

Comment by jdemeyer created at 2011-10-09 11:08:22

Changing status from new to needs_info.


---

Comment by chapoton created at 2014-04-14 20:22:40

Changing keywords from "" to "cyclotomic field".


---

Comment by chapoton created at 2014-04-14 20:22:40

Here is a git branch. But some of the original tests do not work..
----
New commits:


---

Comment by git created at 2014-04-18 19:43:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-04-18 21:16:50

Don't get caught out:

```
sage: K.<z> = CyclotomicField(7)
sage: z^7
1
sage: z^6
-z^5 - z^4 - z^3 - z^2 - z - 1
```



---

Comment by chapoton created at 2014-04-19 06:41:11

Yes, sure. So indeed the original answers are powers of zeta. But are they correct ?


---

Comment by git created at 2014-05-10 16:58:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-05-10 16:59:06

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2014-05-10 16:59:06

This should be good. It takes some expert to check the mathematical correctness.


---

Comment by pbruin created at 2014-05-11 23:40:16

This does not merge with 6.3.beta0, probably because of #11670.  Apart from that, the new code is definitely in need of documentation and references (see comment:2).


---

Comment by pbruin created at 2014-05-11 23:40:16

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-05-16 12:58:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-25 19:27:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-01 11:08:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-06-10 18:20:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-08 19:39:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-13 18:52:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-08-11 19:44:11

Branch pushed to git repo; I updated commit sha1. New commits:
