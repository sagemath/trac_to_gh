# Issue 3436: random_matrix() with prescribed density buggy

Issue created by migration from https://trac.sagemath.org/ticket/3436

Original creator: rpw

Original creation time: 2008-06-16 04:56:11

Assignee: was

CC:  craigcitro

Matrices with prescribed density are not generated correctly:


```
sage: M = random_matrix(GF(65537), 100, 100, sparse=True, density=0.1)
sage: len(M.nonzero_positions())
940
sage: M = random_matrix(GF(2), 100, 100, sparse=True, density=0.1)
sage: len(M.nonzero_positions())
465
```


To wit: the actual density of the matrix over GF(2) is only approximately half of what we expect. This happens because the randomize() function populating the entries does not check whether the random element picked actually is non-zero. Apparently, all of the matrix classes are affected by this bug.


---

Comment by jhpalmieri created at 2009-02-07 00:11:39

I'll also point out that the documentation for random_matrix says that density should be an integer, not a float -- see also randomize in matrix2.pyx and random_element in matrix_space.py -- while in matrix_integer_dense.pyx, randomize says that density should be a float.


---

Comment by jason created at 2009-07-20 14:15:22

Some more examples with sage 4.1.  The last few examples show that the density is about an order of magnitude smaller than what we asked for.


```
sage: A=random_matrix(ZZ,1000,density=1e-3,sparse=True)  
sage: RR(len(A.nonzero_positions()))/(A.nrows()*A.ncols())
0.000814000000000000
sage: A=random_matrix(ZZ,10000,density=1e-4,sparse=True)  
sage: RR(len(A.nonzero_positions()))/(A.nrows()*A.ncols())
0.0000796700000000000
sage: A=random_matrix(ZZ,100000,density=1e-5,sparse=True) 
sage: RR(len(A.nonzero_positions()))/(A.nrows()*A.ncols())
1.13230000000000e-6
sage: A=random_matrix(ZZ,100000,density=1e-6,sparse=True) 
sage: RR(len(A.nonzero_positions()))/(A.nrows()*A.ncols())
1.12600000000000e-7
sage: A=random_matrix(ZZ,100000,density=1e-7,sparse=True) 
sage: RR(len(A.nonzero_positions()))/(A.nrows()*A.ncols())
1.08000000000000e-8
```



---

Comment by jhpalmieri created at 2009-09-30 03:40:28

Replying to [comment:3 jason]:
> Some more examples with sage 4.1.  The last few examples show that the density is about an order of magnitude smaller than what we asked for.

When I tried this, I got answers like the first two: the ratio of (fraction of nonzero entries) / (density) was about 4/5.  This is consistent with the observation in the ticket description that the randomize function doesn't check whether the random element is zero: for integers, the documentation for `random_element` says that the default distribution gives `Pr(X = 0) = 1/5`. 

I would try to write a patch for this but pretty much all of the matrix code is written in Cython, which I don't know, so anything I write would likely be buggy and slow things down by a factor of 100.


---

Comment by spancratz created at 2010-01-17 10:18:53

Attached a patch.  It introduces a new method in ``ring.pyx``, ``_random_nonzero_element``, which by default calls ``random_element`` until a non-zero element has been obtained.

On the matrix end, I've introduced a new parameter ``nonzero`` to the ``randomize`` methods in the various matrix implementations.  If this is set to ``True``, the modified entries are guaranteed to be non-zero, whereas if it is set to ``False`` they are not.  The method ``random_element`` on a matrix space now calls ``randomize`` on a zero matrix with ``nonzero=True``.

Finally, this is now also used to ensure that generating a fraction field element does not cause a division by zero error.

Sebastian


---

Comment by spancratz created at 2010-01-17 10:18:53

Changing status from new to needs_review.


---

Attachment

First patch


---

Comment by spancratz created at 2010-01-17 10:54:51

I've attached the patch now.  I've called it "First patch" since I've only doctested ``sage/matrix/`` and adjusted some docstrings as needed, but I expect that a few more such little changes might come up during a full test.

Sebastian


---

Attachment

Additional patch (more doctests)


---

Comment by spancratz created at 2010-01-17 19:48:07

The additional patch takes care of the remaining three doctest failures.  This should now pass all doctests done with ``./sage -t devel/sage/sage``.

Sebastian


---

Comment by boothby created at 2010-01-18 08:18:05

This looks good with one notable exception.  Due to implementation details, Matrix_cyclo_dense.randomize() makes overly dense matrices.  This should be pretty easy to fix.


---

Comment by boothby created at 2010-01-18 08:18:05

Changing status from needs_review to needs_work.


---

Comment by craigcitro created at 2010-01-18 08:23:36

I mentioned this to Tom, but just in case no one gets to it: implementing this for cyclotomic matrices should be pretty easy once you find out about the `set_unsafe` method on dense cyclotomic matrices. You can use the same generic code that loops over any other matrix, but use `set_unsafe` and (as long as you're really not going outside the bounds of the matrix!) it'll take care of setting the entry in the matrix correctly and quickly.


---

Comment by spancratz created at 2010-01-18 18:59:17

Craig:  the approach you suggest does not seem to work out quite as nicely, since the ``randomize`` method accepts two parameters ``num_bound`` and ``den_bound``, which are accept by the rational field but *not* by the cyclotomic field.  A way around this problem is to generate the cyclotomic numbers ourselves in the matrix method, as a sequence of rationals of length the degree of the field extension.  I'll write that now.

Sebastian


---

Comment by craigcitro created at 2010-01-18 19:11:02

I'm a little confused -- why aren't we just using `K.random_element()` where `K` is whatever ring the entries lie in? The `num_bound` and `den_bound` definitely aren't uniform, though we could definitely easily add them for cyclotomic fields ...


---

Comment by spancratz created at 2010-01-18 20:27:42

I think that is the same reason why certain matrices have their ``randomize`` methods implemented themselves in the very first place:  speed.

Personally, I don't really care about this (the speed of generating random matrices), but since others do, I don't think this patch should make anything significantly slower.


---

Comment by was created at 2010-01-18 22:16:16

> Personally, I don't really care about this (the speed of generating random matrices),

I care because this gets used a *LOT* in benchmarking and automated testing of linear algebra algorithms.


---

Comment by boothby created at 2010-01-18 22:44:32

all that has to happen here is

1) write a for loop that fills in the entries with set_unsafe

2) update the polynomial quotient ring and numberfield random_element methods to pass *args and **kwargs down the line.


---

Comment by spancratz created at 2010-01-18 23:16:57

Tom, before you wrote your message, I already wrote the code for the randomize method, by including a _randomize_column method in matrix_rational_dense, and this is then used in the cyclotomic matrix code.  This way, the code doesn't have to modify any more classes than it does already.  I'll do some testing and upload it later.

Also, I talked to Robert Miller and he said this patch needs to be re-based to 4.3.1.rc0, so I'll do that, too.

Sebastian


---

Comment by boothby created at 2010-01-19 01:22:54

I view the fact that the random_element methods don't pass *args and **kwargs down the line as a bug -- and if you have to rebase, we might as well fix those up too.  Moreover, I'm not convinced that randomizing columns is the right way to go -- though I haven't seen your implementation, so I might be wrong.


---

Comment by spancratz created at 2010-01-19 01:56:47

I've now finished the implementation, but I still need to re-base it.  Here are some timings.  First, the old implementation:

```
sage: MS = MatrixSpace(CyclotomicField(10), 100, 100)
sage: timeit('A = MS.random_element()')
25 loops, best of 3: 17.5 ms per loop
sage: timeit('A = MS.random_element(density=0.1)')
25 loops, best of 3: 8.89 ms per loop
sage: A = MS.random_element(density=0.1)
sage: n(len(A.nonzero_positions())/10000)
0.231700000000000
```

Second, the new implementation:

```
sage: MS = MatrixSpace(CyclotomicField(10), 100, 100)
sage: timeit('A = MS.random_element()')
25 loops, best of 3: 22 ms per loop
sage: timeit('A = MS.random_element(density=0.1)')
25 loops, best of 3: 9.36 ms per loop
sage: timeit('A = MS.random_element(density=0.1, nonzero=True)')
25 loops, best of 3: 9.35 ms per loop
sage: timeit('A = MS.random_element(density=0.1, nonzero=False)')
25 loops, best of 3: 9.37 ms per loop
sage: A = MS.random_element(density=0.1, nonzero=True)
sage: n(len(A.nonzero_positions())/10000)
0.0963000000000000
```



---

Comment by spancratz created at 2010-01-19 01:59:50

Third patch, for matrices over cyclotomic fields


---

Attachment

Rebase of the first three patches to 4.3.1.rc0


---

Comment by spancratz created at 2010-01-19 02:24:54

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2010-01-19 02:24:54

I've now re-based the patch.  I still need to run tests, I'll write back later to confirm if everything passes.

Tom, which random element methods are you referring to?

Sebastian


---

Comment by spancratz created at 2010-01-19 02:56:59

The re-base makes *lots* of doctests fail, I'll update the patch and post another one when I am done.

Sebastian


---

Comment by spancratz created at 2010-01-19 03:52:08

Fixes the doctests for the rebase


---

Attachment

random_element method in polynomial quotient rings (and number fields) passes on args and kwds


---

Attachment

Tom suggested that we should change the code for random matrix generation over cyclotomic fields to rely on the random element generation code in the cyclotomic field, mostly in order to reduce code size.

The patch above now ensures that the polynomial quotient rings (and number fields) pass on additional arguments.

This patch should be applied in addition to all the other ones, in any case.

The next step is to compare the timings of the above code to Tom's suggestion.  If there is no noticeable speed difference, we should go with Tom's suggestion as it provides for cleaner code.  Otherwise, we should leave it done in the above patches.  We'll see.


---

Attachment


---

Comment by spancratz created at 2010-01-19 04:34:46

Addendum to the last patch on polynomial quotients


---

Attachment

Here are the timings for the code that Tom wrote, which gets rid of the "ugly" code I wrote for generating the random matrices over cyclotomic fields and instead uses the generic code of random elements in cyclotomic fields (implemented by two of the patches above):


```
sage: MS = MatrixSpace(CyclotomicField(10), 100, 100)
sage: time A = MS.random_element()
CPU times: user 27.11 s, sys: 0.35 s, total: 27.46 s
Wall time: 27.46 s
```


I suspect that the slowness of this code is largely due to the fact that for every random element of the cyclotomic field, two conversions take place.  One of a random list of rationals into the polynomial ring, and then another of that polynomial into the polynomial quotient ring.

I don't think there is much we can do about this at the moment.  Thus, I propose that we should apply all of the patches on this ticket apart from ``trac3436-tb.patch``.  I'll flatten them a little, (1) main patch (2) ``random_element`` in polynomial rings, polynomial quotient rings, and number fields.  Hopefully, this will then pass all doctests and we'll be done.

Any comments?

PS: Of course, I'll include the fixed doctests (64-bit difference) from Tom's patch.


---

Comment by boothby created at 2010-01-19 04:54:16

I'll eat crow here -- spancratz's implementation is so much faster, we'd be dumb not to use it.  I'll test a clean build once you post the new patches.


---

Comment by spancratz created at 2010-01-19 05:25:58

Main patch


---

Attachment

Polynomial part


---

Comment by spancratz created at 2010-01-19 05:32:41

I've now uploaded all the work we did in two patches, one for the matrix generation (and all the additional code all over the place necessary) as ``trac3436_main.patch`` and another one for the polynomial quotient ring (and number field) part as ``trac3436_poly.patch``.

I am running tests now.  I've got the feeling that it might fail doctests in two files on the remote machine at Oxford but that it'll pass those on my local machine.  But we'll see.  I'll report back once that's done.

Sebastian


---

Comment by craigcitro created at 2010-01-19 05:42:12

So I'm tempted to (re-)propose a fix in the other direction. As Tom noted, the problem with the "smaller" bit of code is that generating random elements in a cyclotomic field is insanely slow. Rather than program around that, why not fix it? I'm going to sit down and look at this now ...


---

Attachment

I attached a minor patch that fixes two whitespace problems in the doctests that caused failures.

Current patch list:

trac3436_main.patch
trac3436_poly.patch
trac3436_whitespace.patch


---

Comment by craigcitro created at 2010-01-19 09:16:56

Okay, so I'm finally convinced. I just spent some time optimizing generation of random number field elements, and got something like a ~150X speedup -- and the resulting randomization for cyclotomic matrices was *still* something like six times slower than the original version. So I'm going to make a new ticket with that code, but I think the code that Sebastian's been writing is definitely the winner. (Tom said he was going to review it in the morning, so I'll let him do that.)

The underlying reason for the speed difference is easy to understand -- we represent elements of number fields as NTL polynomials, so the process of randomly generating the matrix entries involves a huge number of copies of the data: once from sage Integers to NTL integers in generating a random element of the number field, and then *two* copies (due to the way things are getting moved around) in moving the values from the NTL polynomial into the matrix entries. There's just no way this is going to beat code that just generates entries down the line right in the matrix.

I'll add a note on this ticket once I clean up and post the faster number field random element code ...


---

Comment by boothby created at 2010-01-19 20:53:58

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2010-01-19 20:53:58

Looks good / all tests pass.


---

Comment by craigcitro created at 2010-01-20 04:54:37

For the sake of it, I thought I'd mention that I posted my random number field element code at #8007. If we one day move away from NTL for representing elements of polynomials, I think that the "generic" approach Tom and I were trying to push above would probably be a good thing.


---

Comment by mvngu created at 2010-01-24 00:28:15

Merged patches in this order:

 1. [trac3436_main.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/3436/trac3436_main.patch)
 1. [trac3436_poly.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/3436/trac3436_poly.patch)
 1. [trac3436_whitespace.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/3436/trac3436_whitespace.patch)


---

Comment by mvngu created at 2010-01-24 00:28:15

Resolution: fixed
