# Issue 5557: implement ridiculously fast 4x4 determinant

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-03-18 11:48:08

Assignee: was

#5520 calls M.det() for M a 4x4 matrix a huge number of times.  So, let's optimize the heck out of it!


---

Comment by cwitty created at 2009-03-18 17:16:01

This is a pretty stupid thing to do, but even so, I think an error message would be better than a wrong answer:

```
sage: foo = random_matrix(ZZ, 5)
sage: foo.determinant(algorithm='4x4')
-143
sage: copy(foo).determinant()
-159
```



---

Comment by boothby created at 2009-03-18 23:11:52

cwitty, this wasn't quite ready -- but thanks for your diligence!  The new patch makes this method default for dimension 4, and removes the algorithm='4x4' option.  Also, I put the code used to generate this code into the matrix_integer_dense.pyx file.  Finally, the _det_4x4 method has been changed to _det_4x4_unsafe.

Timings:

```
Sage 3.4:
    sage: S = MatrixSpace(ZZ,4)
    sage: M = S.random_element(1,10000^200)
    sage: timeit("M.determinant()")
    5 loops, best of 3: 1.75 s per loop
Updated...
    sage: S = MatrixSpace(ZZ,4)
    sage: M = S.random_element(1,10000^200)
    sage: timeit("M.determinant()")
    625 loops, best of 3: 175 µs per loop
Using Pari:
    sage: N = pari(M)
    sage: timeit("N.matdet();")
    625 loops, best of 3: 337 µs per loop
```


So in general, this is hugely faster than the previous version of Sage, and twice as fast as Pari.


---

Comment by mvngu created at 2009-03-19 04:35:54

Replying to [comment:2 boothby]:

```
> Timings:
> {{{
> Sage 3.4:
>     sage: S = MatrixSpace(ZZ,4)
>     sage: M = S.random_element(1,10000^200)
>     sage: timeit("M.determinant()")
>     5 loops, best of 3: 1.75 s per loop
> Updated...
>     sage: S = MatrixSpace(ZZ,4)
>     sage: M = S.random_element(1,10000^200)
>     sage: timeit("M.determinant()")
>     625 loops, best of 3: 175 µs per loop
> Using Pari:
>     sage: N = pari(M)
>     sage: timeit("N.matdet();")
>     625 loops, best of 3: 337 µs per loop
> }}}
```

> So in general, this is hugely faster than the previous version of Sage, and twice as fast as Pari.
Hi Tom. Is it possible for you to give some system/architecture info of the machine from which you got the above timing statistics? Such info plus timing statistics are good for a release tour.


---

Comment by was created at 2009-03-19 18:07:52

How fast is it on smaller input?  Using PARI more efficiently I was able to get the following timings (in my branch of Sage):


```
sage: M = S.random_element(1,10^8)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 14.9 µs per loop
sage: M = S.random_element(1,10^10)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 16.3 µs per loop
}}} 

Things slow down for bigger input though:
{{{
sage: M = S.random_element(1,10^200)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 104 µs per loop
sage: M = S.random_element(1,10^300)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 186 µs per loop
sage: M = S.random_element(1,10^1000)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 1.2 ms per loop
}}}

The above is on OS X 32-bit core2duo 2.6Ghz.

William


---

Comment by was created at 2009-03-19 20:24:50

Answering my question, on my computer with your code:

```
sage: M = S.random_element(1,10^8)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 8.82 µs per loop
sage: 
sage: M = S.random_element(1,10^10)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 9.86 µs per loop
sage: M = S.random_element(1,10^200)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 49.8 µs per loop
sage: M = S.random_element(1,10^300)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 92.2 µs per loop
sage: M = S.random_element(1,10^1000)
sage: timeit('M.det();M._clear_cache()')
625 loops, best of 3: 585 µs per loop
```



---

Comment by was created at 2009-03-20 09:13:06

For the record, despite me giving this a positive review, I'm nervous about putting this in Sage.  The issue is just that it's highly specialized and gives only a very small speedup over PARI, really.  Let the record speak...


---

Comment by boothby created at 2009-03-22 07:27:30

So, I'm obviously biased.  I think the code is rock-solid, though I admit it's a little silly to optimize to this level except in the case that it's being called hundreds of times.  Also, though the speedup is absolutely small (being on the order of microseconds), this appears to be asymptotically twice as fast as theirs; so relatively, it's a pretty big difference. 

So I guess the real question is; what percentage of the time in the Brandt matrix code is being spent computing determinants?  Will this cut a couple of seconds off, or only a few millis off of a 30-second computation?

Other opinions?


---

Comment by mabshoff created at 2009-03-25 09:38:54

Well, I am waiting until someone comes up with some opinion what to do. I am personally fine with this going in, so ....

Cheers,

Michael


---

Comment by was created at 2009-03-25 16:11:46

> So I guess the real question is; what percentage of the time 
> in the Brandt matrix code is being spent computing determinants? 
> Will this cut a couple of seconds off, or only a few millis off 
> of a 30-second computation? 

It will definitely only cut "a few millis".

But I guess I'm OK with this code going in.


---

Comment by mabshoff created at 2009-03-26 00:57:59

The two patches are causing a doctest failure:

```
sage -t -long "devel/sage/sage/matrix/matrix_integer_dense.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/matrix/matrix_integer_dense.pyx", line 3050:
    sage: A.determinant(algorithm='linbox')
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: you must pass the proof=False option to the determinant command to use Linbox's det algorithm
Got:
    -843
**********************************************************************
```


Cheers,

Michael


---

Comment by boothby created at 2009-03-28 06:25:22

The problem was that the doctest expected a failure where this succeeded.  I changed the doctest to use a 5x5 instead of 4x4 to avoid this.


---

Comment by was created at 2009-03-28 15:23:12

NO.  If you explicitly specify algorithm='linbox', then you *have* to get algorithm='linbox', even in the 4x4 case.  You need to change the code, not the doctest so the 4x4 algorithm doesn't get selected if the user explicitly requests to use linbox.


---

Comment by cwitty created at 2009-03-28 16:49:42

Note that this wasn't true before Tom's patch; for a 3x3 or smaller matrix, the algorithm='linbox' was ignored.


---

Comment by boothby created at 2009-03-28 17:34:47

cwitty's argument is precisely how I justified (to myself) that this behavior is OK.  If you disagree, then this is an orthogonal issue, and we should allow the user to override the algorithm for dimensions 1,2, and 3.  But, the point of the small special cases is that they're faster than the others methods, so we fast-track their execution to avoid a bunch of python string comparisons.


---

Comment by was created at 2009-03-29 18:20:39

> cwitty's argument is precisely how I justified (to myself) that this 
> behavior is OK. If you disagree, then this is an orthogonal issue, 
> and we should allow the user to override the

OK, I'm convinced.


---

Comment by was created at 2009-04-12 06:41:21

Please rebase this against 3.4.1.rc*


---

Attachment


---

Comment by boothby created at 2009-04-15 19:00:43

Ready to go.  How does one tag a rebase'd patch?  Does it need another review?


---

Comment by AlexGhitza created at 2009-04-30 11:56:13

In light of the above discussion, I'm giving this a positive review.  I've checked that it passes doctests.

There are no doctests for the new code, so I have added fairly trivial indirect doctests for them in the review patch.


---

Attachment

apply after the first patch


---

Comment by mabshoff created at 2009-05-11 13:35:09

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 13:35:09

Resolution: fixed
