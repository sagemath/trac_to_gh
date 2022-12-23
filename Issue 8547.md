# Issue 8547: implement hidden markov models in Cython from scratch (so can remove the GHMM standard package from Sage)

Issue created by migration from https://trac.sagemath.org/ticket/8547

Original creator: was

Original creation time: 2010-03-16 08:08:50

Assignee: amhou

CC:  jason mhampton




---

Comment by was created at 2010-03-20 12:49:05

apply this. Then look at devel/sage/sage/stats/intlist.pyx, devel/sage/sage/stats/hmm (which is entirely new code), and look at the few minor bug fixes to finance/time_series.pyx


---

Attachment


---

Comment by was created at 2010-03-20 12:49:50

Changing status from new to needs_review.


---

Comment by was created at 2010-03-20 12:53:10

This is now ready for review.  Some notes:

  1. Don't bother looking at the diff, except for time_series.pyx and module_list.py.  Just look at at the files in stats/hmm, which are all new, and stats/intlist.pyx.

  2. There are a number of very small API changes (for the better).   This technically violates our DeprecationPolicy.  However, frankly, the current code was -- upon inspection -- so bad, that there is no way anybody was actually using it for anything serious.  (As was evidenced by the response on sage-devel.)  And the API is only a tiny bit changed now. 

  3. I do have a long list of possible followup projects. However, I wanted to make a first solid release that at least has enough to replace the existing HMM functionality in Sage, before adding lots of new stuff.


---

Comment by mhampton created at 2010-03-21 17:04:23

Changing assignee from amhou to mhampton.


---

Comment by mhampton created at 2010-03-21 17:05:04

Changing assignee from mhampton to amhou.


---

Comment by boothby created at 2010-03-28 20:25:49

This patch touches matrix2.pyx which results in failures of a number of doctests.  Example:


```
sage -t  devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "/mnt/usb1/scratch/boothby/sage-4.3.4/devel/sage-main/sage/matrix/matrix2.pyx", line 3142:
    sage: A.restrict(W2, check=True)
Expected:
    Traceback (most recent call last):
    ...
    ArithmeticError: subspace is not invariant under matrix
Got:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_48[10]>", line 1, in <module>
        A.restrict(W2, check=True)###line 3142:
    sage: A.restrict(W2, check=True)
      File "matrix2.pyx", line 3167, in sage.matrix.matrix2.Matrix.restrict (sage/matrix/matrix2.c:19470)
        raise ArithmeticError, "subspace is not invariant under matrix (%s)"%msg
    ArithmeticError: subspace is not invariant under matrix (vector is not in free module)
**********************************************************************
```


That should be easy to fix.


---

Comment by was created at 2010-03-28 21:47:19

this completely replaces the previous patch


---

Attachment

Ok, doctests run clean now.  I've tested the code out and read it over, and it works for me.  I'm a little cautious giving this a positive review because I know very little about this area of math.  However, given that it's replacing something that barely worked and used memory like toilet paper, I'm willing to throw caution to the wind if mhampton or jason are willing to sign off on the idea.


---

Comment by mhampton created at 2010-03-31 03:06:55

I've been wanting to review this but I just haven't had the time.  I might this weekend, but its unclear.


---

Comment by jason created at 2010-03-31 03:52:17

Some notes from reading through the code looking at stylistic issues.  I really wish we had line-by-line commenting like rietveld for this sort of thing.

 1. Lots of cdef'd functions do not have doctests.  I thought the policy from discussions on sage-devel was that *every* function (including cdef functions) should have doctests (but, of course, these doctests would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).  Some functions (_baum_welch_gamma, for example) don't even have docstrings.
 1. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.  How much of a performance penalty is there?  Can this "python semantics" part be extracted out to be a more general cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement !__getitem!__?  Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also support slices.  At the very least, the doctests for normalize_index probably ought to be run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.
 1. IntList.sum() does not have a doctest for the overflow case


---

Comment by was created at 2010-04-03 08:49:53

Replying to [comment:10 jason]:
> Some notes from reading through the code looking at stylistic issues.  I really wish we had
>  line-by-line commenting like rietveld for this sort of thing.
> 
>  1. Lots of cdef'd functions do not have doctests.  I thought the policy from discussions on sage-devel 
> was that *every* function (including cdef functions) should have doctests (but, of course, these doctests
>  would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).  

We definitely do not require doctests for cdef'd methods.   The requirement is that "sage -coverage" returns a score of 100%.  This is clearly stated in the patch reviewers guide.    I did seriously consider them in this case, but literally every single one of these doctests would just be a literal *exact* copy of a doctest from elsewhere (!) but with # indirect doctest next to it.  There's just no value in that.   I could also make the methods cpdef, but that does incur a performance penalty -- in this case, it would be huge (which is totally unacceptable). 

> Some functions (_baum_welch_gamma, for example) don't even have docstrings.

I do think that all cdef'd methods should have docstrings, and will add docstrings to any that don't have them (in a part 2 patch). 

>  1. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.  
> How much of a performance penalty is there? 

I'll switch to using normalize_index, since I'm not concerned with performance for list indexing, since everywhere that performance matters, I'm directly accessing the memory buffer (which is the only way to really compete with tightly coded C libraries).   So my updated patch will change to use normalize_index, unless there is a serious problem with doing so. 

>  Can this "python semantics" part be extracted out to be a more general 
> cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement 
> !__getitem!__?  

Perhaps.  I'm certainly not doing so for this patch. 

> Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also 
> support slices.  At the very least, the doctests for normalize_index probably ought to be 
> run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.

Fortunately this won't be necessary since I'm switching to it. 

>  1. IntList.sum() does not have a doctest for the overflow case

I can add that.   I like testing all corner cases.

Thanks for your helpful review of style...

 - William


---

Comment by mhampton created at 2010-04-03 14:37:05

I got one numerical noise doctest failure on OS X 10.5.8:

sage -t  devel/sage-t2/sage/stats/hmm/util.pyx
**********************************************************************
File "/Users/mh/sagestuff/sage-4.3.5/devel/sage-t2/sage/stats/hmm/util.pyx", line 55:
    sage: T.sum()
Expected:
    1.0                   
Got:
    0.99999999999999978

I used this code in class yesterday (see http://wiki.sagemath.org/interact/stats#HiddenMarkovModel.3ATheOccasionallyDishonestCasino) and for that limited purpose it seemed fine.

It would be nice to have the forward and backward algorithms more exposed, but I don't think that needs to go into this ticket unless you feel like it.

Apart from the noise issue  I think can give this a positive review.


---

Comment by was created at 2010-04-08 21:47:38

* I've attached a part 2 patch.   I made sure all cdef's methods have docstrings and also that doctests are properly sphinx formated (some weren't since they were copied from the old code). 

* Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 
 
* I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:

```
sage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5),10^5)')   # slow because constructions a big python list
125 loops, best of 3: 2.17 ms per loop
sage: a = stats.IntList([1..10^5])
sage: timeit('a[1:10^5]')                       # slice is just a memcpy
625 loops, best of 3: 48.4 µs per loop
sage: 2.17/0.0484
44.8347107438017
```

Here's an example with a step:

```
sage: a = stats.IntList([1..10^5])
sage: timeit('a[1:10^5:2]')
625 loops, best of 3: 92.2 µs per loop
sage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5,2),10^5)')
625 loops, best of 3: 772 µs per loop
```

and that 772 microseconds is *before* we do the actual iteration through the returned list of python ints, convert them to c ints, copy stuff around in memory, etc. 

This stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in "realtime" processing of large datastreams.    I don't want slow functions anywhere in there. 

 -- William


---

Comment by was created at 2010-04-08 21:55:51

part 2; apply this and the previous patch


---

Attachment

Replying to [comment:13 was]:



> * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 


I meant that the doctest looks like this:


```
Note that there can be overflow, since the entries are C ints:: 
    sage: a = stats.IntList([2^30,2^30]); a 
    [1073741824, 1073741824] 

```


That's it.  There's no test there; you're just creating a list, not summing anything.


>  
> * I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:

> This stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in "realtime" processing of large datastreams.    I don't want slow functions anywhere in there. 


I agree.


---

Comment by was created at 2010-04-10 19:18:23

Replying to [comment:14 jason]:
> Replying to [comment:13 was]:
> 
> 
> 
> > * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 
> 
> 
> I meant that the doctest looks like this:
> 
> {{{
> Note that there can be overflow, since the entries are C ints:: 
>     sage: a = stats.IntList([2<sup>30,2</sup>30]); a 
>     [1073741824, 1073741824] 
> 
> }}}
> 
> That's it.  There's no test there; you're just creating a list, not summing anything.
> 

Thanks for the clarification -- I was being dense; I've put up a part 3 that addresses this. 

So, can I get a positive review now?


---

Attachment


---

Comment by mhampton created at 2010-04-11 21:32:11

OK, positive review.  I think this and basic_stats should be added to the reference manual, but that can be another ticket I guess.


---

Comment by mhampton created at 2010-04-11 21:32:11

Changing assignee from amhou to mhampton.


---

Comment by mhampton created at 2010-04-11 21:32:22

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:43:45

Merged in 4.4.alpha0:
 - trac-8547-take2.patch
 - trac_8547-take2-part2.patch
 - trac_8547-take2-part3.patch


---

Comment by jhpalmieri created at 2010-04-16 18:43:45

Resolution: fixed
