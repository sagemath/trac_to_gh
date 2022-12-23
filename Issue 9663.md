# Issue 9663: Fast computation of Stirling numbers of 2nd kind

Issue created by migration from https://trac.sagemath.org/ticket/9663

Original creator: fredrik.johansson

Original creation time: 2010-08-01 18:44:18

Assignee: sage-combinat

CC:  was

Currently, Stirling numbers are computed by calling GAP. The patch provides fast Cython code for Stirling numbers of the second kind, and allows using GAP or Maxima as an optional algorithm.

By having less overhead, the Cython code is about 10000 times faster than GAP or Maxima for tiny inputs, and it remains much faster than GAP for larger inputs as well. Apparently Maxima uses a fast algorithm unlike GAP, but my code is still about twice as fast as Maxima for huge n due to an algorithmic optimization.


```
sage: %timeit stirling_number2(10,5)
625 loops, best of 3: 2.33 µs per loop
sage: %timeit stirling_number2(10,5,algorithm='gap')
25 loops, best of 3: 20 ms per loop
sage: %timeit stirling_number2(10,5,algorithm='maxima')
5 loops, best of 3: 40 ms per loop

625 loops, best of 3: 16.2 µs per loop
sage: %timeit stirling_number2(100,50,algorithm='gap')
25 loops, best of 3: 20 ms per loop
sage: %timeit stirling_number2(100,50,algorithm='maxima')
5 loops, best of 3: 40 ms per loop

sage: %timeit stirling_number2(2000,1500)
25 loops, best of 3: 35.9 ms per loop
sage: %timeit stirling_number2(2000,1500,algorithm='gap')
5 loops, best of 3: 348 ms per loop
sage: %timeit stirling_number2(2000,1500,algorithm='maxima')
5 loops, best of 3: 210 ms per loop

sage: %timeit stirling_number2(4000,3000)
5 loops, best of 3: 249 ms per loop
sage: %timeit stirling_number2(4000,3000,algorithm='gap')
5 loops, best of 3: 2.96 s per loop
sage: %timeit stirling_number2(4000,3000,algorithm='maxima')
5 loops, best of 3: 948 ms per loop

sage: %time stirling_number2(20000,15000);
CPU times: user 20.30 s, sys: 0.23 s, total: 20.53 s
Wall time: 21.82 s
sage: %time stirling_number2(20000,15000,algorithm='maxima');
CPU times: user 0.00 s, sys: 0.01 s, total: 0.01 s
Wall time: 51.90 s
```


Mathematica seems to be about as slow as GAP (warning: timed on a different system):

```
In[1]:= Timing[StirlingS2[4000,3000];]
Out[1]= {27.1809, Null}
```



---

Comment by fredrik.johansson created at 2010-08-01 19:15:35

Changing status from new to needs_review.


---

Comment by was created at 2010-08-05 02:48:47

Please explain the *massive* number of changes to module_list.py of the form:

```
153	 	                [[blank looking line]]
 	153	                [[another blank looking line]]
```



---

Comment by fredrik.johansson created at 2010-08-05 10:05:16

Oops, my editor was set to "strip trailing whitespace when saving files".


---

Comment by fredrik.johansson created at 2010-08-05 22:39:31

fast implementation of stirling_number2 -- updated patch


---

Attachment

Please see the new version of the patch.


---

Comment by ncohen created at 2010-09-05 15:19:56

Nice one !!

I learned many things while reviewing this patch `:-)`

Would you mind adding this small doctest in the patch I attach ? If not, you can set this ticket to "positive_review" !

Thanksssssssssssss !!!

Nathann


---

Attachment


---

Comment by ncohen created at 2010-10-04 06:01:13

Are you around ? There's basically nothing to do on this patch `:-)`

Nathann


---

Comment by nborie created at 2010-10-24 10:44:09

Changing status from needs_review to positive_review.


---

Comment by nborie created at 2010-10-24 10:44:09

The two patch applied on 4.5.3 All tests pass, no warning in docbuild... Nice documentation, powerful implantation... Good job!

I give the two patch a positive review.

For the release manager, please apply :
 * stirling2.patch
 * trac_9663 - additional test.patch


---

Comment by jdemeyer created at 2010-10-26 08:52:31

I think you should add a patch with a test for "unknown algorithm".


---

Comment by jdemeyer created at 2010-10-26 08:53:19

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-10-26 08:54:28

Also, *please* do not put spaces in patch filenames.


---

Comment by ncohen created at 2010-10-26 09:15:49

Replying to [comment:8 jdemeyer]:
> I think you should add a patch with a test for "unknown algorithm".

What do you mean ?

Nathann


---

Comment by jdemeyer created at 2010-10-26 09:43:31

Replying to [comment:11 ncohen]:
> Replying to [comment:8 jdemeyer]:
> > I think you should add a patch with a test for "unknown algorithm".
> 
> What do you mean ?

A test which does something like

```
sage: n = stirling_number2(20,11,algorithm='foobar')
```

to check the "unknown algorithm" code.


---

Comment by ncohen created at 2010-10-26 10:20:33

Here is a new version of my patch with the requested doctest.

Nathann


---

Comment by ncohen created at 2010-10-26 10:20:33

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-10-26 11:50:22

Replying to [comment:13 ncohen]:
> Here is a new version of my patch with the requested doctest.
> 
> Nathann

On line 670, `TESTS::` should be `TESTS:` (the :: should precede a block of code, which is not the case here).


---

Comment by jdemeyer created at 2010-10-26 11:50:22

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-10-26 11:58:18

Done.

Nathann


---

Comment by ncohen created at 2010-10-26 11:58:18

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jdemeyer created at 2010-10-27 12:25:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:09:45

Resolution: fixed
