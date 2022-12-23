# Issue 3684: linear algebra -- optimize computation of kernel for matrices over GF(2)

Issue created by migration from https://trac.sagemath.org/ticket/3684

Original creator: was

Original creation time: 2008-07-20 11:45:22

Assignee: was


```


On Sat, Jul 19, 2008 at 11:49 PM, Simon King <king@mathematik.uni-jena.de> wrote:
>
> Dear Sage team,
>
> I don't know whether this post should better go to sage-devel or sage-
> support.
>
> I understood that recently the implementation of matrices over GF(2)
> was considerably improved. Therefore i am very surprised that the
> computation of the (left) kernel is still very slow:
>
> sage: version()
> 'SAGE Version 3.0.5, Release Date: 2008-07-11'
> sage: M=MatrixSpace(GF(2),1000,500).random_element()
> sage: time K=M.kernel()
> CPU times: user 21.60 s, sys: 0.06 s, total: 21.66 s
> Wall time: 40.87 s
> sage: time K.matrix()
> CPU times: user 15.06 s, sys: 0.03 s, total: 15.09 s
> Wall time: 27.71 s
> 500 x 1000 dense matrix over Finite Field of size 2
>
>
> Version 2.2.3 of C-MeatAxe (for which i have a wrapper) does much
> better:
>
> sage: m=MTX(2,[M[i].list() for i in range(1000)]) # Now, m is "the
> same" as M
> sage: time k=m.nullspace()
> CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s
> Wall time: 0.18 s
> sage: time k
> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
> Wall time: 0.00 s
> (500 x 1000) MTX matrix over GF(2)
>
> Hence, we have an improvement from 21.60+15.06 CPU-seconds to 0.18
> seconds.
> And the result is right:
> sage: K.matrix()*M == 0
> True
> sage: k*m == MTX(2,500,500)   # this is a zero-matrix
> True
>
> Did i do something wrong? Is M.kernel() not what i should use here? Or
> is the kernel computation not optimised yet?

Computation of the kernel is done in two steps in Sage:

1. Compute the reduced row echelon form of the matrix.
2. Read off the kernel.
3. Create the kernel as a vector space.

In theory 1 takes most of the time and 2-3 are trivial.
In this particular case Sage is using 100% slow generic
code (over any base ring, etc.) to do 2-3, but superfast
code for 1:

sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: time E=M.echelon_form()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time K=M.kernel()
CPU times: user 13.02 s, sys: 0.82 s, total: 13.84 s
Wall time: 14.54 s

Writing a version of the generic code that is optimized
for gf2 mr4i matrices would make it so the second step
above would take 0.00 seconds.  Really it would 
probably take about 10 ms, since

sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: timeit('M[0,0]=0; M.echelon_form()')
125 loops, best of 3: 3.46 ms per loop

So with proper optimization Sage should be at least an order
of magnitude than your meataxe benchmarks above. 

 -- William
```



---

Comment by malb created at 2009-12-16 10:28:43

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-16 10:28:43

With attached patch things are a little bit better (I didn't touch the vectors yet):


```
sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: %time K=M.kernel()
CPU times: user 5.89 s, sys: 0.00 s, total: 5.90 s
Wall time: 5.99 s

sage: %time K.matrix()
CPU times: user 3.36 s, sys: 0.49 s, total: 3.86 s
Wall time: 3.95 s
500 x 1000 dense matrix over Finite Field of size 2
```



---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-12-19 21:32:46

Resolution: fixed
