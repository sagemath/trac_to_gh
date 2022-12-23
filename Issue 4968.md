# Issue 4968: switch Matrix_modn_dense from ints to CPU longs

Issue created by migration from https://trac.sagemath.org/ticket/4968

Original creator: malb

Original creation time: 2009-01-12 16:54:43

Assignee: was

CC:  simonking mraum

The switch would allow to cover larger primes with the specialised code (and I currently work with primes ~ 2<sup>32</sup>).

The switch requires changing all mentions of `int` to `long` and probably implementing `arith_long`.


---

Comment by mabshoff created at 2009-01-12 17:33:34

Replying to [ticket:4968 malb]:

> The switch requires changing all mentions of `int` to `long` and probably implementing `arith_long`.

I am not sure using long here is a good idea since on various platforms we want to support sizeof(long) == sizeof (int). You might want to replace it by some typedef so we can make it long long on those platforms.

Cheers,

Michael


---

Comment by malb created at 2009-01-12 21:58:03

> I am not sure using long here is a good idea since on various platforms we want to
> support sizeof(long) == sizeof (int). You might want to replace it by some typedef
> so we can make it long long on those platforms.

Is your point that the maximum prime for which we use `Matrix_modn_dense` shouldn't vary across platforms? I didn't think of it before, I can see why this would be desirable. How about "long long" across the board?


---

Comment by was created at 2009-01-13 14:49:34

> How about "long long" across the board? 

Won't that have negative implications. For example, on a 32-bit machine all matrices will take twice as much memory to store, and all arithmetic will be an order of magnitude slower.  That certainly wouldn't make me happy!



```
%cython
def foo(n):
    cdef long long i = 10, j = 10093, k
    cdef int z
    for z in range(n):
        k += i*j
    return k
///
```



```
%cython
def bar(n):
    cdef int i = 10, j = 10093, k
    cdef int z
    for z in range(n):
        k += i*j
    return k
///
```



```
time foo(10^8)
///

587410688573299048L
CPU time: 0.29 s,  Wall time: 0.29 s
```



```
time bar(10^8)
///

-171048080
CPU time: 0.04 s,  Wall time: 0.04 s
```



```
0.29/0.04
///

7.25000000000000
```



---

Comment by mabshoff created at 2009-01-13 15:00:43

Replying to [comment:3 was]:
> > How about "long long" across the board? 
> 
> Won't that have negative implications. For example, on a 32-bit machine all matrices will take twice as much memory to store, and all arithmetic will be an order of magnitude slower.  That certainly wouldn't make me happy!

Well, assuming we will transparently switch over to another implementation (using gmpz's for example) we should use the "fast" integer type, i.e. 32 bit ints and a 64 bit int type on 64 bit boxen. But my original point remains: On 

 * 64 bit Solaris
 * 64 bit Windows

sizeof(long) == sizeof(int) == 4, so using either a C99 type or some platform dependent typedef is what we need here to get optimum performance on all 64 bit platforms. Since we are already requiring C99 due to FLINT we might as well go for that solution.

Cheers,

Michael


---

Comment by burcin created at 2009-01-15 12:59:23

I don't know what `arith_long` is, but the `long_extras` module of FLINT might help here.


---

Comment by malb created at 2011-08-30 15:57:17

I'd say this is now a duplicate? of #4260 and should be closed?


---

Comment by burcin created at 2011-09-22 00:48:57

#4260 doesn't cover your request of modulus > 2<sup>32</sup> from the ticket description. Maximum modulus there is 2<sup>23</sup>.

We could use the template class from #4260 to provide a matrix class using `long long`s.


---

Comment by was created at 2012-03-23 02:15:04

Changing status from new to needs_review.


---

Comment by was created at 2012-03-23 02:15:04

Replying to [comment:8 burcin]:
> #4260 doesn't cover your request of modulus > 2<sup>32</sup> from the ticket description. Maximum modulus there is 2<sup>23</sup>.
> 
> We could use the template class from #4260 to provide a matrix class using `long long`s.

I elected not to do this because:

   * the template class is very, very heavily tied to linbox, and disentangling that seemed insane.  We can't use linbox anyways for primes above 2^23.

   * much of the work in writing this patch was spent writing a lot of really good tests that truly exercise the new functionality, and in debugging and properly using the old Strassen code for matrix multiplication and echelon forms.    None of that would have been made better by using the template.


---

Comment by robertwb created at 2012-03-23 07:16:31

matrix_window_modn_dense_uint64.pyx looks an awfully lot like matrix_window_modn_dense.pyx (and the same could be said of the non-window files), is there any reason to keep both?


---

Comment by malb created at 2012-04-18 18:47:53

William, are you still working on this code? I was about to start reviewing but then saw that you didn't reply to Robert's comment, hence wondering how high priority it is for you at the moment.


---

Comment by was created at 2012-04-18 19:30:14

Replying to [comment:13 malb]:
> William, are you still working on this code? I was about to start reviewing but then saw that you didn't reply to Robert's comment, hence wondering how high priority it is for you at the moment.

Yes!  Please review!   Regarding robert's comment -- No, there is no reason to keep both.  But maybe I can put all the cleanup in another patch, just in case there is a reason.   Just to keep things simple.  

I care very much about this code.


---

Comment by robertwb created at 2012-04-19 08:34:10

apply only this patch


---

Attachment

I've squashed this into just changing matrix_modn_dense directly, which should make it both easier to see the changes and avoid adding a (modified) second copy of everything.


---

Comment by robertwb created at 2012-04-19 08:38:08

It's also rebased on top of sage-5.0.beta15.


---

Comment by malb created at 2012-04-19 20:23:58

Changing status from needs_review to needs_work.


---

Comment by malb created at 2012-04-19 20:23:58

*32-bit vs 64-bit*

 * I think there is a bit of confusion about 32-bit vs. 64-bit in the patch, or at least I am confused. If I understand correctly, then `ctypedef unsigned long uint_fast64_t` is used to define the data type of the matrix. However, `unsigned long` is not necessarily 64-bit, on 32-bit machines it may be 32-bit. Arithmetic uses `long long` which is at least 64-bit. So either the datatype should not mention 64 bits or should be moved over to e.g. `uint64_t` or `unsigned long long` (which doesn't exist in older C++ standards FWIW). Once this is fixed there seem to be a few places like: "Reduce the integer matrix modulo a positive machine size integer." and "stored as a 64-bit unsigned int" which might need adapting too.  

 * I am not sure about this code:

```python  
  if use_32bit_type(p): 
        raise RuntimeError, "BUG: p (=%s) is too small to use this matrix type"%p 
```

  Why raise an error? Of course, the LinBox matrices take care of that by default, I am just confused by this. Also, this seems to contradict with "If the prime is small enough to fit in a byte" later.

 * I assume this `long long` vs `unsigned long long` is the reason for restricting the modulus to 2<sup>31</sup>?

*mod_int vs. mod_int_uint64*

 * I think Robert's merge introduced a bug in pickling. We are at version 10 of pickling for `Matrix_modn_dense` but William started counting at zero again for his new type. Now that we're back to the old type, we shouldn't check for `version == 0`.

*Other stuff*

 * "TODO: should free up memory allocated so far -- this would leak otherwise, in exactly a situation where a *lot* leaks" Shouldn't this be fixed?

 * Of course, far from mandatory but couldn't we -- while we are at it -- not also fix those `raise OverflowError, string` to read `raise OverflowError(string)` which is Python3 style (?)

 * performance: it seems picking a bigger Strassen cutoff would be quite beneficial:


```
sage: A = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: %time A*A                               
CPU times: user 2.67 s, sys: 0.00 s, total: 2.68 s
Wall time: 2.69 s
1000 x 1000 dense matrix over Finite Field of size 16777213
sage: %time A._multiply_strassen(A,100)                    
CPU times: user 1.12 s, sys: 0.00 s, total: 1.12 s
Wall time: 1.13 s
1000 x 1000 dense matrix over Finite Field of size 16777213
```



---

Comment by mraum created at 2012-04-26 11:32:20

The unsigned long thing seems OK (int_fast64_t is a C type, defined in stdint.h). For consistency it would be good if MAX_MODULUS was INTEGER_MOD_INT64_LIMIT to be found in sage/rings/finite_rings/stdint.h this is less by one. In integer_mod.pyx the modulus is tested using <= and in the patch < is used.

Apart from this I more or less agree with all points made previously. If you don't see a good reason to change the Strassen cutoff, I would leave it at is. File a new ticket instead. We should optimize it, but changing it based on one observation is daring.

Honestly, I am against the if use_32bit_type(p) test. The matrix works perfectly for such p. Even thought it shouldn't be called, it may be called.

If anybody has time to make the changes, I will test it within the next two weeks and it will have a positive review.


---

Comment by malb created at 2012-04-26 11:43:48

Replying to [comment:18 mraum]:
> The unsigned long thing seems OK (int_fast64_t is a C type, defined in stdint.h). For consistency it would be good if MAX_MODULUS was INTEGER_MOD_INT64_LIMIT to be found in sage/rings/finite_rings/stdint.h this is less by one. In integer_mod.pyx the modulus is tested using <= and in the patch < is used.

You are right, I got confused about Cython ctypdefs. "unsigned long" does not appear in a meaningful way in the generated C files. Sorry for the noise. Still, the documentation is wrong in various places and should be fixed (machine sized ints).
 
> Apart from this I more or less agree with all points made previously. If you don't see a good reason to change the Strassen cutoff, I would leave it at is. File a new ticket instead. We should optimize it, but changing it based on one observation is daring.

Fair enough, so let's make more observations. This code is about performance. I am not saying: let's run a comprehensive optimisation suite but not at least trying to use cutoffs which make the code reasonable fast seems wrong.


---

Comment by mraum created at 2012-04-26 11:50:34

I don't think this code is about performance. The new code will only be used in cases that were not available previously (see the cases treated in matrix_int_dense). This is why I would like to separate this patch and the optimization.

Also, please keep in mind, that not only William is desperate for having Sage use larger moduli (me certainly, John and his student recently posted on sage-devel, and most likely many more).


---

Comment by malb created at 2012-04-26 12:07:40

Replying to [comment:20 mraum]:
> I don't think this code is about performance. The new code will only be used in cases that were not available previously (see the cases treated in matrix_int_dense). This is why I would like to separate this patch and the optimization.

Sage can compute with larger primes it's just terribly slow, this patch fixes that.

> Also, please keep in mind, that not only William is desperate for having Sage use larger moduli (me certainly, John and his student recently posted on sage-devel, and most likely many more).

Fair enough. I am not asking anyone to spend days and days improving the performance, but I am asking those who care about this patch to spend 10 minutes to test various cutoff parameters so that we have a reasonable default. If there are that many people who care about this, this should be easy.


---

Comment by mraum created at 2012-04-27 10:24:39

I acknowledge that we really see this ticket from different perspectives.

Would you be so kind and run some of the test that you think give a reasonable cutoff? If you post the commands, I can run them myself (on AMD and Intel). Based on this we can choose one.


---

Comment by malb created at 2012-04-27 10:38:53

I'd say just running


```
sage: A = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: B = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: %time A._multiply_strassen(B, 20)
sage: %time A._multiply_strassen(B, 50)
sage: %time A._multiply_strassen(B,100)
sage: %time A._multiply_strassen(B,150)
sage: %time A._multiply_strassen(B,200)
```


should probably do the trick. I posted timings on my machine above. I'll run some timings on other machines as well.

I'm really not suggesting to spend hours and hours on this, just that we should pick a decent default value, i.e., my impression is that 20 is bad on most machines. I might be wrong though.


---

Comment by was created at 2012-04-27 11:15:22

I'm completely with mraum here.  In fact I have run tests like you suggest to set the current parameters.  You'll find optimal parameters differ *dramatically* depending on the computer and the OS... e.g., Mac OS X could be totally different than one linux; Intel versus AMD, etc.   I can see almost no point in doing what you suggest above.  Either do things right (with a database for many machines), or leave it.


---

Comment by malb created at 2012-04-27 11:18:22

sage.math:

*24 bits*


```
sage: %time _ = A._multiply_strassen(B, 20)
CPU times: user 3.31 s, sys: 0.01 s, total: 3.32 s
Wall time: 3.32 s

sage: %time _ = A._multiply_strassen(B, 50)
CPU times: user 2.02 s, sys: 0.03 s, total: 2.05 s
Wall time: 2.04 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 1.90 s, sys: 0.01 s, total: 1.91 s
Wall time: 1.91 s
```


* 31 bits *


```
sage: %time _ = A._multiply_strassen(B,20)
CPU times: user 4.06 s, sys: 0.00 s, total: 4.06 s
Wall time: 4.05 s
sage: %time _ = A._multiply_strassen(B,50)
CPU times: user 2.95 s, sys: 0.00 s, total: 2.95 s
Wall time: 2.95 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 3.00 s, sys: 0.00 s, total: 3.00 s
Wall time: 3.00 s

sage: %time _ = A._multiply_strassen(B,200)
CPU times: user 3.20 s, sys: 0.00 s, total: 3.20 s
Wall time: 3.20 s
```



---

Comment by malb created at 2012-04-27 11:19:54

Replying to [comment:24 was]:
> I'm completely with mraum here.  In fact I have run tests like you suggest to set the current parameters.  You'll find optimal parameters differ *dramatically* depending on the computer and the OS... e.g., Mac OS X could be totally different than one linux; Intel versus AMD, etc.   I can see almost no point in doing what you suggest above.  Either do things right (with a database for many machines), or leave it.

I find it odd to claim this before even trying (perhaps you did and I missed that though).


---

Comment by was created at 2012-04-27 11:55:29

> I find it odd to claim this before even trying (perhaps you did and I missed that though).

I did a lot of timings like the above on my laptop when writing this patch...


---

Comment by malb created at 2012-04-27 11:59:24

So, was 20 a good on your laptop (I am asking because the 20 cutoff is older than your patch).

FWIW I'll try this on bsd.math and cicero.skynet. If those too suggest to increase the cutoff to > 20, I suggest we do that. If only bsd.math and sage.math agree, I'd still say it's worth increasing the limit, because these are more mainstream machines than cicero.skynet.


---

Comment by malb created at 2012-04-28 14:08:30

Btw. it seems something went wrong with the quashing, there are still mentions of `_uint64` in the patch.


---

Comment by malb created at 2012-04-28 14:14:44

*bsd.math*


```
sage: A = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: B = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: %time _ = A._multiply_strassen(B, 20)
CPU times: user 2.87 s, sys: 0.01 s, total: 2.88 s
Wall time: 2.88 s

sage: %time _ = A._multiply_strassen(B, 50)
CPU times: user 1.47 s, sys: 0.01 s, total: 1.47 s
Wall time: 1.47 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 1.24 s, sys: 0.01 s, total: 1.24 s
Wall time: 1.24 s

sage:  %time _ = A._multiply_strassen(B,150)
CPU times: user 1.16 s, sys: 0.01 s, total: 1.17 s
Wall time: 1.17 s

sage: %time _ = A._multiply_strassen(B,200)
CPU times: user 1.16 s, sys: 0.01 s, total: 1.17 s
Wall time: 1.17 s
```



```
sage: A = random_matrix(GF(previous_prime(2^31)),1000,1000)
sage: B = random_matrix(GF(previous_prime(2^31)),1000,1000)

sage: %time A._multiply_strassen(B, 20)
CPU times: user 3.72 s, sys: 0.00 s, total: 3.72 s
Wall time: 3.72 s
1000 x 1000 dense matrix over Finite Field of size 2147483647

sage: %time _ = A._multiply_strassen(B, 50)
CPU times: user 2.55 s, sys: 0.01 s, total: 2.55 s
Wall time: 2.55 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 2.53 s, sys: 0.01 s, total: 2.54 s
Wall time: 2.54 s

sage: %time _ = A._multiply_strassen(B,150)
CPU times: user 2.68 s, sys: 0.00 s, total: 2.69 s
Wall time: 2.69 s

sage: %time _ = A._multiply_strassen(B,200)
CPU times: user 2.68 s, sys: 0.00 s, total: 2.69 s
Wall time: 2.69 s
```


So 100 is much better than 20, but not necessarily optimal.


---

Comment by malb created at 2012-04-29 14:19:11

*Cicero* is less conclusive as it's too loaded for benchmarketing. Anyway, here are the numbers:

*2<sup>24</sup>*


```
sage: A = random_matrix(GF(previous_prime(2^24)),1000,1000)
sage: B = random_matrix(GF(previous_prime(2^24)),1000,1000)

sage: %time _ = A._multiply_strassen(B, 20)
CPU times: user 25.93 s, sys: 0.03 s, total: 25.95 s
Wall time: 85.44 s

sage: %time _ = A._multiply_strassen(B, 50)
CPU times: user 21.48 s, sys: 0.04 s, total: 21.52 s
Wall time: 68.51 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 21.99 s, sys: 0.11 s, total: 22.09 s
Wall time: 70.36 s

sage: %time _ = A._multiply_strassen(B,150)
CPU times: user 23.95 s, sys: 0.05 s, total: 24.01 s
Wall time: 76.56 s
```


*2^31*


```
sage: A = random_matrix(GF(previous_prime(2^31)),1000,1000)
sage: B = random_matrix(GF(previous_prime(2^31)),1000,1000)
sage: %time _ = A._multiply_strassen(B, 20)
CPU times: user 25.93 s, sys: 0.08 s, total: 26.00 s
Wall time: 83.17 s

sage: %time _ = A._multiply_strassen(B, 50)
CPU times: user 21.47 s, sys: 0.06 s, total: 21.53 s
Wall time: 68.69 s

sage: %time _ = A._multiply_strassen(B,100)
CPU times: user 22.02 s, sys: 0.06 s, total: 22.08 s
Wall time: 70.31 s

sage: %time _ = A._multiply_strassen(B,150)
CPU times: user 23.92 s, sys: 0.14 s, total: 24.06 s
Wall time: 76.67 s
```


_What I take away from these numbers:_ increasing the default cutoff from 20 to 100 makes Sage  twice as fast on some mainstream architectures (64-bit Linux, Xeon), about 1.7x faster on others (64-bit OSX) and probably slightly faster on less mainstream architectures (32-bit Linux on Pentium4). Am I missing something here?


---

Attachment


---

Comment by mraum created at 2012-05-01 09:38:36

I made this work; Only very few points had been overseen when squashing.

I changed the cutoff back to 100. Since William and I both think one should do it properly or not at all, I thought it would be best to keep the old cutoff. This had been 100. The biggest advantage from my perspective is that the release manager will have to deal with one change only (32 -> 64bit) and not with two, when investigating potential speed regressions. Not that I found any, but there are more exotic architectures than mine.


---

Comment by malb created at 2012-05-01 09:52:06

Replying to [comment:32 mraum]:
> I changed the cutoff back to 100. Since William and I both think one should do it properly or not at all, I thought it would be best to keep the old cutoff. This had been 100. 

Fair enough, 100 is what I was arguing for regardless. But I have to say being so blatantly ignored leaves a bitter aftertaste. Anyway, it seems to you have this patch covered, I won't intervene any more.


---

Comment by mraum created at 2012-05-01 18:45:24

Please, don't take it like that. I was happy to see that your suggestion and the old cutoff were the same. But consider us changing this and the underlying implementation in parallel. What would the release manager do if regressions showed up. I would unmerge the whole thing (and we would feel like stealing his time). This way you can open a new ticket and do the optimization independently.


---

Comment by mraum created at 2012-05-01 18:45:24

Changing status from needs_work to needs_review.


---

Comment by kini created at 2012-05-20 06:18:54

By the way, doctesting this patch left several (5-10) python processes running on a patchbot for more than 13 hours, which is probably abnormal...


---

Comment by vbraun created at 2012-06-18 16:00:30

I'm reviewing the linbox update (#12883), where malb removed linbox-stuff from `matrix_modn_dense.py`. This might conflict with this ticket's patch but, I think, only in a trivial way. If I got this wrong then please let me know.


---

Comment by Snark created at 2015-03-11 16:22:01

This ticket is in needs_review since three years... putting it into needs_info status, since obviously sagemath has move forward in the intervening time.


---

Comment by Snark created at 2015-03-11 16:22:01

Changing status from needs_review to needs_info.
