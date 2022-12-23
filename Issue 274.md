# Issue 274: memory leak --- Polynomial arithmetic over finite field

Issue created by migration from https://trac.sagemath.org/ticket/274

Original creator: ifti

Original creation time: 2007-02-21 08:50:03

Assignee: was

Leaks like a bad ...


```

sage: get_memory_usage()
'276M'
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: for i in range(1000):
    s = K.random_element(); t = K.random_element()
    poly = s + t*X
....:     
sage: get_memory_usage()
'281M'

```



---

Comment by was created at 2007-08-18 16:12:20

This much simpler example also leaks:

```
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: s = K.random_element(); t = K.random_element()
sage: for i in range(1000):
    _ = t*X
```



---

Comment by was created at 2007-08-18 16:13:31


```
09:10 < was_> the problem is also *only* over GF(10007^2)
09:10 < was_> not over GF(10007)
09:10 < was_> so it's givaro, probably.
```



---

Comment by was created at 2007-08-18 16:15:51

Not givaro, pari:

sage: K = GF(10007^2, 'a')
sage: type(K)
<class 'sage.rings.finite_field.FiniteField_ext_pari'>


---

Comment by was created at 2007-08-18 20:05:03

The problem is in polynomial creation.


```
K = GF(2^16, 'a')
print type(K)
R.<x> = K[]
print type(R)
s = K.random_element()

def leak(n):
    m = get_memory_usage()
    for i in range(n):
        _ = R([1])
    print get_memory_usage() - m

leak(10000)
```



---

Comment by dmharvey created at 2007-08-18 21:56:05

after much hunting, the bug appears to be in PARI gen __bool__ method, which currently is implemented as:


```
def __bool__(gen self):
   _sig_on
   t = bool(self.g != stoi(0))
   _sig_off
   return t
```


which doesn't make a whole lot of sense.


---

Comment by was created at 2007-08-19 01:42:26

Changing priority from major to critical.


---

Comment by was created at 2007-08-19 05:32:46

This is really a symptom of some sort of much more general memory leak problem in the PARI C library interface, as the following bizarre example illustrates:


```
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = pari(0)
...
sage: print get_memory_usage() - s
0.0
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = n == m
...
sage: print get_memory_usage() - s
0.0
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = n == pari(0)
...
sage: print get_memory_usage() - s
10.87109375
```



---

Comment by was created at 2007-08-19 08:28:30

Resolution: fixed
