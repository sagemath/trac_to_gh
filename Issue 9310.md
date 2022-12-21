# Issue 9310: sage-4.4.4.alpha1 blocker -- random doctest failure on menas (skynet)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-22 15:00:46

Assignee: mvngu

CC:  vbraun


```

wstein`@`menas:~/screen/menas/sage-4.4.4.alpha1> ./sage -t  -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
sage -t -long "devel/sage/sage/groups/matrix_gps/matrix_group.py"
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 647:
    sage: G.random_element()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [0 1 1 0]
    [1 2 2 2]
    [1 1 1 0]
    [2 0 1 2]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 658:
    sage: G.random_element()
Expected:
    [1 3]
    [0 3]
Got:
    [4 2]
    [1 0]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 661:
    sage: G.random_element()
Expected:
    [2 2]
    [1 0]
Got:
    [4 1]
    [0 2]
**********************************************************************
File "/home/wstein/screen/menas/sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py", line 664:
    sage: G.random_element()
Expected:
    [4 0]
    [1 4]

Got:
    [2 4]
    [2 3]
**********************************************************************
1 items had failures:
   4 of  10 in __main__.example_22
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_matrix_group.py
         [88.9 s]
```



---

Comment by was created at 2010-06-22 15:01:08


```

wstein`@`menas:~/screen/menas/sage-4.4.4.alpha1> uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
wstein`@`menas:~/screen/menas/sage-4.4.4.alpha1> cat /etc/issue
Welcome to openSUSE 11.1 - Kernel \r (\l).
```



---

Comment by was created at 2010-06-22 15:29:25

Note -- In sage-4.4.1 on the same computer, the file doctests fine.  The only diff between the files is:

```
wstein`@`menas:~/screen/menas/sage-4.4.1> diff devel/sage/sage/groups/matrix_gps/matrix_group.py ../sage-4.4.4.alpha1/devel/sage/sage/groups/matrix_gps/matrix_group.py|more
330a331,351
>     def is_abelian(self):
>         r"""
>         Return True if this group is an abelian group.
>         
>         Note: The result is cached, since it tends to get called
>         rather often (e.g. by word_problem) and it's very slow to
>         use the Gap interface every time. 
> 
>         EXAMPLES::
>         
>             sage: SL(1, 17).is_abelian()
>             True
>             sage: SL(2, 17).is_abelian()
>             False
>         """
>         try:
>             return self.__is_abelian
>         except AttributeError:
>             self.__is_abelian = self._gap_().IsAbelian().bool()
>             return self.__is_abelian
> 
624c645,646
<   
```


Thus a change somewhere *else* in Sage is causing this problem.


---

Comment by mhansen created at 2010-06-22 17:11:10

I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984


---

Comment by drkirkby created at 2010-06-22 23:22:20

FWIW, I run this 6 times on my Solaris 10 box (SPARC) with no problems using sage-4.4.4.alpha1.tar 

Dave


---

Comment by nthiery created at 2010-06-23 05:49:28

Replying to [comment:3 mhansen]:
> I had noticed this on sage.math when merging http://trac.sagemath.org/sage_trac/ticket/8984

Ah, interesting. So hopefully #8984 is not the cause, and could be merged in!


---

Comment by was created at 2010-06-27 01:11:40

Changing priority from blocker to critical.


---

Comment by drkirkby created at 2010-07-08 11:59:54

There seems to be a *lot* of doctests which are failing in a non-reproducible way. 

 * elliptic_curves/BSD.py #9273 (Whilst #9316 is supposed to fix the spurious "# File not found" error at end of doctests, BSD.py has still failed for me in non-reproducible way. See #9449 which shows the output of `make ptestlong` First BSD.py fails without printing the  "# File not found" message, then it passes. 
 * devel/sage/sage/misc/trace.py - see #9446
 * devel/sage/doc/fr/tutorial/programming.rst - see #9449, where this failed first time, but subsequently passed on the same computer, with the same build of Sage. (Though a couple of patches were applied the second time). 
 * devel/sage/sage/schemes/plane_curves/constructor.py - again see #9449 which failed once, then passed on a second run. 
 * devel/sage/sage/parallel/decorate.py
This failed both times, but on the first time it failed, the test was reported to have a 0 failures! 

```
    sage -t     -long devel/sage/sage/parallel/decorate.py # 0 doctests failed
```

After adding patches #8641, #9243, #9316 which are related to the doctesting framework, this was at least reported as one doctest failing in `devel/sage/sage/parallel/decorate.py` 

```
       sage -t  -long devel/sage/sage/parallel/decorate.py # 1 doctests failed
```

I'm not however convinced that the addition of  #8641, #9243 and #9316 were the result of the improved behavior, as other tests still failed with 0 reported failures. 

*IT SEEMS TO ME, THE DOCTESTING FRAMEWORK IS BROKEN IN SAGE NOW*


---

Comment by saliola created at 2011-02-05 04:07:37

As noted in #10739, I have two independent builds of sage-4.6.2.alpha3 on my machine, one in which this test passes and the other in which it fails.

Replying to [vbraun](http://trac.sagemath.org/sage_trac/ticket/10739#comment:10) (from #10739)
> But if one build repeatedly passes "make ptest" and the other consistently fails, this would be an excellent opportunity to debug #9310. Presumably the only difference is that the first compilation was interrupted at one point, so the order in which spkgs were built is different.

Precisely, the first build was interrupted (see #10739 for details) and the second was not.

> This might have changed linked libraries in some components due to (undiscovered) soft dependencies, for example. Can you diff the two trees (excluding log files etc) and find out the difference? 

I ran `diff -rq` on the two directories and there are about 25000 files that differ (pyc files, pyo files, ...). I figured that this might have something to do with hardcoded paths, so I moved one out of the way, moved the other into its place, launched sage to reset the hardcoded paths, and then ran `diff -rq` on the two trees. It still shows about 25000 differing files.

Any suggestions on what to try next?


---

Comment by saliola created at 2011-02-05 04:39:51

I just noticed that after I tar up the offending build directory, untar it elsewhere, launch sage to reset the hardcoded paths, and doctest the `matrix_group.py` file, then all tests pass. So relocating the tree has some sort of an effect here.


---

Comment by vbraun created at 2011-02-20 12:33:10

I was able to reproduce the failure on Sage-4.6.2.rc0 with Fedora 14 x86_64 by running 

```
sage -t -randorder sage/groups/matrix_gps/matrix_group.py
```

repeatedly. The doctest usually passes but once in a while fails as in the ticket description.


---

Comment by vbraun created at 2011-02-21 11:51:53

I did run the test 1000x with -randorder, and found a couple of doctests that depend on the execution order. Since we always initialize GAP's random number generator it is very likely that the output of these operations depends on the order of memory locations. Presumably this causes the doctest failure on some architectures even without -randorder.

The problems are in 
  * `module_composition_factors`
  * `as_permutation_group`
  * `random_element`

The first two use `MeatAxe`. I think that `random_element` enumerates all group elements and then picks a random one. We do control the random numbers, but enumerating uses the coset enumerator and presumably depends on memory locations.


---

Attachment

Initial patch


---

Comment by vbraun created at 2011-02-21 19:07:28

Changing status from new to needs_review.


---

Comment by vbraun created at 2011-02-21 19:07:28

This patch 
  * sorts the output of `module_composition_factors`, and
  * changes the doctests for `as_permutation_group`, `random_element` to be insensitive to the random choices.


---

Comment by mariah created at 2011-06-15 14:16:07

Applied patch to sage-4.7.1.alpha2, did 'make testlong'.  All tests passed.  Positive review!


---

Comment by mariah created at 2011-06-15 14:16:07

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-18 08:35:30

Resolution: fixed


---

Comment by leif created at 2011-06-25 21:15:59

We should perhaps now change the ticket's title.


---

Comment by leif created at 2011-06-25 21:15:59

Changing keywords from "" to "matrix_group random_element doctest failure".
