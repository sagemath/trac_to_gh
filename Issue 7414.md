# Issue 7414: improve {from,to}_inversion_vector

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-11-08 20:31:45

Assignee: mhansen

CC:  sage-combinat

The method to_inversion_vector can be greatly improved by using a divide-and-conquer strategy.


---

Comment by ylchapuy created at 2009-11-08 20:34:54

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-11-08 20:34:54

for the record,

before:

```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
5 loops, best of 3: 2.08 s per loop
sage: iv = p.to_inversion_vector()
sage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')
25 loops, best of 3: 9.57 ms per loop
```


after:

```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
25 loops, best of 3: 14.7 ms per loop
sage: iv = p.to_inversion_vector()
sage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')
625 loops, best of 3: 1.47 ms per loop
```



---

Comment by hivert created at 2009-11-09 08:35:32

Changing keywords from "" to "permutations, inversion vector, lehmer code".


---

Comment by hivert created at 2009-11-09 08:35:32

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2009-11-09 08:35:32

Yes, this is very good for large permutaions ! but is is much slower on small permutations, where I will use it :-) Sorry for this...

Before:

```
625 loops, best of 3: 16.4 µs per loop
625 loops, best of 3: 19.2 µs per loop
625 loops, best of 3: 33.3 µs per loop
625 loops, best of 3: 87.4 µs per loop
625 loops, best of 3: 356 µs per loop
125 loops, best of 3: 2.04 ms per loop
25 loops, best of 3: 14.2 ms per loop
5 loops, best of 3: 117 ms per loop
```

after:

```
625 loops, best of 3: 18.1 µs per loop
625 loops, best of 3: 19.9 µs per loop
625 loops, best of 3: 51.2 µs per loop
625 loops, best of 3: 166 µs per loop
625 loops, best of 3: 794 µs per loop
125 loops, best of 3: 4.86 ms per loop
25 loops, best of 3: 33.2 ms per loop
5 loops, best of 3: 271 ms per loop
```


I suggest you to reinstate the former implementation and to change from one to the other depending on the size of the permutations. I wrote the same in MuPAD, the cut-of point where around 18. 

Moreover, since the Lehmer code is the inversion vector of the inverse, you can speed up it for large n. Also, if you would take the chance to write the definition of the lehmer code (c_i = the number of j > i s.t. s(j) < s(i)) and to put a link beetween those two methods, then I would be extremely happy to put a positive review. 

Sorry to give you more work. 

Cheers,

Florent


---

Comment by hivert created at 2009-11-09 14:54:20

And finally, it would be perfect if you add a note on the complexity of the algorithm. 

Cheers,

Florent


---

Attachment


---

Comment by ylchapuy created at 2009-11-09 23:26:07

I did my best to keep small permutations fast.
Here are the new timings.


```
sage: for k in [0,1,2,3,4,5,6,7]:
    L=Permutations(k).list()
    print k
    timeit('[len(p._to_inversion_vector_orig()) for p in L]')
    timeit('[len(p._to_inversion_vector_small()) for p in L]')
    timeit('[len(p.to_inversion_vector()) for p in L]')
....:     
0
625 loops, best of 3: 2.35 µs per loop
625 loops, best of 3: 3.86 µs per loop
625 loops, best of 3: 1.43 µs per loop
1
625 loops, best of 3: 3.23 µs per loop
625 loops, best of 3: 4.98 µs per loop
625 loops, best of 3: 1.54 µs per loop
2
625 loops, best of 3: 7.69 µs per loop
625 loops, best of 3: 12.2 µs per loop
625 loops, best of 3: 3.13 µs per loop
3
625 loops, best of 3: 29.6 µs per loop
625 loops, best of 3: 38 µs per loop
625 loops, best of 3: 11.2 µs per loop
4
625 loops, best of 3: 152 µs per loop
625 loops, best of 3: 171 µs per loop
625 loops, best of 3: 197 µs per loop
5
625 loops, best of 3: 957 µs per loop
625 loops, best of 3: 961 µs per loop
625 loops, best of 3: 1.09 ms per loop
6
125 loops, best of 3: 7.14 ms per loop
125 loops, best of 3: 6.39 ms per loop
125 loops, best of 3: 7.12 ms per loop
7
5 loops, best of 3: 64.4 ms per loop
5 loops, best of 3: 51.1 ms per loop
5 loops, best of 3: 55.5 ms per loop
```


Timings for big permutations are also quite improved thanks to an improved base case.


```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
125 loops, best of 3: 7.03 ms per loop
```


As you suggested, I also improved the to_lehmer_code method. Here is the comparison, first for small sizes,

before:

```
sage: for k in [0,1,2,3,4,5,6]:
....:         L=Permutations(k).list()
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
625 loops, best of 3: 4.06 µs per loop
625 loops, best of 3: 5.86 µs per loop
625 loops, best of 3: 13.8 µs per loop
625 loops, best of 3: 51.2 µs per loop
625 loops, best of 3: 248 µs per loop
625 loops, best of 3: 1.55 ms per loop
25 loops, best of 3: 11.4 ms per loop
```


after:

```
sage: for k in [0,1,2,3,4,5,6]:
....:         L=Permutations(k).list()
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
625 loops, best of 3: 2.5 µs per loop
625 loops, best of 3: 3.81 µs per loop
625 loops, best of 3: 9.44 µs per loop
625 loops, best of 3: 32 µs per loop
625 loops, best of 3: 150 µs per loop
625 loops, best of 3: 880 µs per loop
125 loops, best of 3: 5.89 ms per loop
```


and for big sizes,

before:

```
sage: for k in [100,300,600,1000]:
....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
25 loops, best of 3: 20.2 ms per loop
5 loops, best of 3: 174 ms per loop
5 loops, best of 3: 704 ms per loop
5 loops, best of 3: 1.94 s per loop
```


after

```
sage: for k in [100,300,600,1000]:
....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
125 loops, best of 3: 1.89 ms per loop
25 loops, best of 3: 11.2 ms per loop
25 loops, best of 3: 37.4 ms per loop
5 loops, best of 3: 69.1 ms per loop
```



---

Comment by ylchapuy created at 2009-11-09 23:26:07

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2009-11-09 23:36:29

NB: The tests are long, but they should be much faster of applying #7415 which improves `random_element`


---

Attachment

Sorry, I forgot the from_* methods in the first patch. Please apply both.

Cheers,
 Yann


---

Comment by hivert created at 2009-11-10 08:54:57

Good work ! Positive review. 

Some remarks: 
 - as you commented in the code the hardcoded handling of the n=0,1,2,3 case is a little bit overkill :-)
 - we should'nt spent too much time in optimizing very finely those function since at some point, we will probably change the datastructure for permutations to a fastest one (plain python list or tuple or Cython object or even C int[]).

Cheers,

Florent


---

Comment by hivert created at 2009-11-10 08:54:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:40:17

Resolution: fixed
