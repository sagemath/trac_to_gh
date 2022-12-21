# Issue 5445: [with patch, needs review] coercion is very slow when new coercions are discovered

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-06 02:01:09

Assignee: robertwb

Consider the following timings:

```
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
625 loops, best of 3: 888 µs per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
625 loops, best of 3: 1.45 ms per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0", number=5000)
5000 loops, best of 3: 2.18 ms per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
125 loops, best of 3: 5.36 ms per loop
```


The operation of adding the Integer 0 to the polynomial keeps getting slower and slower.  This is because each time, it adds to the cache of known coercions, and there's a performance bug in the cache data structure.

In particular, in coerce_dict.pyx, this code:

```
        if self.threshold and len(self) > len(self.buckets) * self.threshold:
            self.resize()
```

calls len(self), where len(self) has a slow, O(n) implementation.  So adding n items to a `TripleDict` takes O(n<sup>2</sup>) time.

The attached patch fixes this by storing the size in the `TripleDict`, instead of always recomputing it.

After applying the patch, the timings above become:

```
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
625 loops, best of 3: 690 µs per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
625 loops, best of 3: 690 µs per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0", number=5000)
5000 loops, best of 3: 691 µs per loop
sage: timeit("polygen(QQ, name='x'+str(ZZ.random_element(2^100)))+0")
625 loops, best of 3: 690 µs per loop
```


So the operation is essentially constant time.


---

Attachment

Nice catch.


---

Comment by mabshoff created at 2009-03-08 05:40:06

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 05:40:06

Resolution: fixed
