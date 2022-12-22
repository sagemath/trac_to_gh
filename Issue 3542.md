# Issue 3542: [with patch, needs review] multimodular algorithm for Bernoulli numbers

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-07-02 19:22:20

Assignee: somebody

This patch implements the algorithm in my preprint "A multimodular algorithm for computing Bernoulli numbers".

http://math.harvard.edu/~dmharvey/bernmm/

It adds a few files into a new bernmm directory, a cython wrapper (bernmm.pyx), modifies setup.py to build those files, removes the old implementation of `bernoulli_mod_p_single`, and adds a new algorithm option and a `num_threads` option to the global `bernoulli()` function.

My main concern from a build point of view is whether pthreads is supported on all of our target platforms. If not, it will be necessary to modify setup.py to conditionally remove the -lpthreads option and also to #define `USE_THREADS` appropriately.



---

Attachment


---

Comment by dmharvey created at 2008-07-02 19:23:34

Changing type from defect to enhancement.


---

Comment by was created at 2008-07-02 20:53:29

OMFG! W00t!!


---

Comment by was created at 2008-08-01 02:13:39

REFEREE REPORT:

 * Patch applies and works fine. Doctests pass.

 * You need r""" instead of """ for some of the docstrings where you use backslashes.

```
 	75	def bernmm_bern_modp(long p, long k): 
 	76	    """ 
 	77	    Computes $B_k \mod p$, where $B_k$ is the k-th Bernoulli number. 
```


 * You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?

 * I would prefer if there were an algorithm="default" or algorithm="heuristic" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.

 * I found bugs in either PARI or your new code!  This happens also with num_threads=1.

```
sage: for k in range(1,10000):
....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k
....:     
2932
2957
3443
3962
3973
...
```

This is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). 

 * What does this do?  Just curious.  Maybe you could document it.

``` 
NTL_CLIENT; 
```


 * Wow, this patch has a really large amount of interesting C++ code, all well documented.  This must have been quite a lot of work -- it's of course the best in the world and multithreaded.  Amazing.


---

Comment by dmharvey created at 2008-08-01 03:22:19

Replying to [comment:3 was]:
>  * You may want to post a patch to add the docs to the reference manual.   Do you know how to do that?

No, I don't understand what you mean. I thought all the function documentation was automatically included in the reference manual?


>  * I would prefer if there were an algorithm="default" or algorithm="heuristic" option or something that say uses pari for small inputs (up to 20000 or so), then switches over to bernmm for larger inputs.

Okay.


>  * I found bugs in either PARI or your new code!  This happens also with num_threads=1.
> {{{
> sage: for k in range(1,10000):
> ....:     if bernoulli(2*k, algorithm='bernmm', num_threads=2) != bernoulli(2*k, algorithm='pari'): print k
> ....:     
> 2932
> 2957
> 3443
> 3962
> 3973
> ...
> }}}
> This is on a 32-bit build of Sage running Mac OS X 10.5 (i.e., my core 2 duo MBP laptop). 

Nasty. Thanks for picking that up. I've found the bug and I should have a fix tomorrow. That's quite annoying, because I actually do have a test suite which I ran on a 32-bit machine, and it was specifically designed to pick up that kind of crap, and I still missed it. (The first failure occurs when the largest prime modulus is just below `2^15`, which was a good clue :-))


>  * What does this do?  Just curious.  Maybe you could document it.
> {{{ 
> NTL_CLIENT; 
> }}}

This is a standard NTL macro that Shoup recommends putting at the top of any file that uses NTL. It does something to do with namespaces. See

http://www.shoup.net/ntl/doc/tour-ex1.html


---

Comment by was created at 2008-08-01 12:58:43

>     * You may want to post a patch to add the docs to the reference manual. Do you know how to do that?

> No, I don't understand what you mean. I thought all the function documentation was automatically
> included in the reference manual? 

The layout and choice contents of the reference manual are done by hand.  If you read the instructions in SAGE_ROOT/devel/doc/ref/README.txt hopefully that will explain what you need to do.


---

Attachment

I've addressed all issues raised by reviewer (see attached patch), except for the reference manual thing.

The bernoulli number function itself is already in the reference manual, in

http://www.sagemath.org/doc/ref/module-sage.rings.arith.html

Are you talking about adding the bernmm.pyx wrapper to the manual? It's not at all clear to me where in the manual it would belong. I already don't really understand why bernoulli() is in rings.arith, that seems pretty random.


---

Attachment

I think this looks good.  I added a few doctests that verify that your code agrees with the pari code, for a few of the cases that William found did not agree.

Apply only `3542-dharvey-bernoulli-numbers-multimodular.patch`.


---

Comment by mabshoff created at 2008-08-11 01:24:55

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 01:24:55

Resolution: fixed
