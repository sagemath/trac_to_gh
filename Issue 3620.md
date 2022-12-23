# Issue 3620: minpoly slow for finte fields

Issue created by migration from https://trac.sagemath.org/ticket/3620

Original creator: robertwb

Original creation time: 2008-07-09 00:03:58

Assignee: tbd

It goes via pari calls, rather than invoking ntl directly.


---

Comment by was created at 2008-07-09 00:49:12

But note, we may want to use our own implementation since minpoly and charpoly of *matrices* over finite fields in sage is so fast.


---

Comment by was created at 2008-07-09 18:46:04

Changing priority from major to blocker.


---

Comment by was created at 2008-07-09 19:26:35

Here is an example that illustrates the difference:

```
sage: k.<a> = GF(2^100)
sage: time g = k.random_element().charpoly()
CPU times: user 1.17 s, sys: 0.02 s, total: 1.18 s
Wall time: 1.36 s
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^100)));')
'Time: 0.000'
```


Here's the sage code that does the charpoly computation:

```
sage: a.charpoly??
        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
        R = PolynomialRing(self.parent().prime_subfield(), var)
        return R(self._pari_().charpoly('x').lift())
```


It turns out that pari is just totally abysmal at computing charpolys of Mod's.

```
sage: f = k.random_element()._pari_()
sage: time g = f.charpoly('x')
CPU times: user 1.13 s, sys: 0.01 s, total: 1.14 s
Wall time: 1.26 s
sage: f.type()
't_POLMOD'
```


Fortunately Sage matrices aren't quite as bad, though of course this is still vastly
slower than Magma:

```
sage: time g = k.random_element().matrix().charpoly()
CPU times: user 0.36 s, sys: 0.00 s, total: 0.36 s
Wall time: 0.37 s

```


Asymptotically though this is still vastly better than the current situation:

```
age: k.<a> = GF(2^200)
sage: time g = k.random_element().matrix().charpoly()
CPU times: user 2.21 s, sys: 0.03 s, total: 2.24 s
Wall time: 2.24 s
sage: time g = k.random_element().charpoly()
CPU times: user 14.14 s, sys: 0.08 s, total: 14.22 s
Wall time: 14.27 s
```


But still this sucks compared to magma

```
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^300)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^400)));')
'Time: 0.010'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^600)));')
'Time: 0.010'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^1000)));')
'Time: 0.030'
```


I looked at NTL seems to have no functions at all for charpoly or minpoly
of elements of GF(2^n).  :-(

http://www.shoup.net/ntl/doc/GF2E.txt


---

Comment by dmharvey created at 2008-07-09 19:44:44

also note:


```
sage: k.<a> = GF(2^500)
sage: time g = k.random_element()
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
sage: time m = g.matrix()
CPU times: user 11.59 s, sys: 0.82 s, total: 12.41 s
Wall time: 12.41 s
sage: time f = m.charpoly()
CPU times: user 20.51 s, sys: 0.01 s, total: 20.52 s
Wall time: 20.51 s
```



---

Attachment


---

Comment by was created at 2008-07-09 19:59:27

1. dmharvey -- i have no clue what the point of your remark is above.

2. the point of my patch, by the way, is just to be a first tiny step.


---

Comment by mhansen created at 2008-07-09 20:12:11

Looks good to me.  Should there be another ticket for improving this further.


---

Comment by dmharvey created at 2008-07-09 20:36:21

My point is just that computing the matrix and computing its charpoly both take non-negligble time.


---

Comment by mabshoff created at 2008-07-10 02:01:33

Resolution: fixed


---

Comment by mabshoff created at 2008-07-10 02:01:33

Merged in Sage 3.0.4.rc3


---

Comment by robertwb created at 2008-07-10 06:47:42

Resolution changed from fixed to 


---

Comment by robertwb created at 2008-07-10 06:47:42

Changing status from closed to reopened.


---

Comment by robertwb created at 2008-07-10 06:47:42

It looks like NTL does have minimal polynomial computations, though provided in http://www.shoup.net/ntl/doc/GF2X.txt rather than http://www.shoup.net/ntl/doc/GF2E.txt . We should probably use the proof flag to decide the algorithm. Trace could be wrapped as well. 

Also, the computation of matrix() is using the completely generic code, which has got to be sub-optimal for manipulating elements of GF(2).


---

Comment by mabshoff created at 2008-07-10 10:04:08

Robert,

I see no reason to reason to reopen this ticket since what you describe seems to be an improvement/additional change. Please open another ticket since the attached patch has been merged in Sage 3.0.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-10 10:04:37

Resolution: fixed
