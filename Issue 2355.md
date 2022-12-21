# Issue 2355: Write a clearer submatrix implementation

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-02-29 20:30:57

Assignee: dfdeshom

*The current implementation of the submatrix command could be easier to use given that matrix_from_rows_and_columns is nicely suited for this task; ie, this should just work

```
A.submatrix([1..2],[0..1])
```


if A is (at least) a 3x2 matrix
 


---

Comment by was created at 2008-02-29 20:46:56

I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...


---

Comment by dfdeshom created at 2008-03-01 08:11:35

Replying to [comment:1 was]:
> I vote for at least seriously considering using the same notation as numpy for submatrices, whatever that is, by extending __getitem__...

Agreed. Looking at the relevant section of the code, it looks like it should not be too hard


---

Comment by dfdeshom created at 2008-03-02 17:42:32

Here's a patch that makes the following possible:

```
            sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
            sage: M
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]
            [-1  2 -2 -1  4]

            Get The 2 x 2 submatrix of M, starting at row index and column
            index 1
            sage: M[1:3,1:3]
            [ 8  6]
            [ 1 -1]

            Get the 2 x 3 submatrix of M starting at row index and column
            index 1:
            sage: M[1:3,[1..3]]
            [ 8  6  2]
            [ 1 -1  1]

            Get the second column of M:
            sage: M[1:,0]
            [ 1]
            [ 1]
            [-1]

            sage: M[range(2),:]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            sage: M[range(2),4]
            [9]
            [2]
            sage: M[range(3),range(5)]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]

            sage: M[3,range(5)]
            [-1  2 -2 -1  4]
            sage: M[3,:]
            [-1  2 -2 -1  4]
            sage: M[3,4]
            4

```



---

Comment by was created at 2008-03-02 17:49:55

I have to register the obvious concern.  You've replaced what I wrote:

```
554	 	            if PyTuple_Size(key) != 2: 
555	 	                raise IndexError, "index must be an integer or pair of integers" 
556	 	            i = <object> PyTuple_GET_ITEM(key, 0) 
557	 	            j = <object> PyTuple_GET_ITEM(key, 1) 
```



by 


```
 	587	            s1 = key[0] 
 	588	            s2 = key[1] 
 	589	 
 	590	            if isinstance(s1,sage.rings.integer.Integer) and \ 
 	591	                   isinstance(s2,sage.rings.integer.Integer): 
 	592	                self.check_bounds(s1, s2) 
 	593	                return self.get_unsafe(s1, s2) 
```


If A is a matrix doing A[i,j] is a sort of "critical speed operation",
so I'm concerned about speed.    Thoughts? Benchmarks?


---

Comment by dfdeshom created at 2008-03-02 18:16:10

Replying to [comment:4 was]:

The new method is slower, but not by much (surprisingly for me):

```
# sage-main
sage: %timeit M[3,4]
10000 loops, best of 3: 69.5 µs per loop

#sage-getitem
sage: %timeit M[3,4]
10000 loops, best of 3: 71.2 µs per loop

#sage-main
sage: %timeit M[3:]
10000 loops, best of 3: 68.3 µs per loop

#sage-getitem
sage: %timeit M[3:]
10000 loops, best of 3: 69.5 µs per loop
```



```
#sage-getitem only
sage: %timeit M[:4,range(4)]
10000 loops, best of 3: 87.8 µs per loop

sage: %timeit M[3:,:4]
10000 loops, best of 3: 78.8 µs per loop

sage: %timeit M[3:,0]
10000 loops, best of 3: 74.1 µs per loop

```


matrix_from_rows_and_columns could also be made a little faster. I plan to post another ticket/patch for it.


---

Comment by dfdeshom created at 2008-03-02 18:16:32

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-03-11 16:36:47

Changing type from defect to enhancement.


---

Comment by jsp created at 2008-03-13 18:40:43

Can't give this patch a positive review. After I applied it to a brand new sage-2.10.3
a lot of code seems to be broken.

I do not quite understand what is going on.

Jaap


---

Comment by dfdeshom created at 2008-03-13 19:20:48

My changes seem to have broken `matrix.__reduce___`. I'll look into it.


---

Comment by dfdeshom created at 2008-03-13 20:18:39

Found the bug. All doctests for matrix0,1,2 pass now.


---

Comment by jsp created at 2008-03-13 21:06:16

Applyin this bundle I still got an error:


```
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx
Total time for all tests: 113.4 seconds

```




```
sage -t  devel/sage-main/sage/matrix/matrix_integer_dense.pyx**********************************************************************
File "matrix_integer_dense.pyx", line 2961:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[1]>", line 1, in <module>
        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1),Integer(2)])###line 2961:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1,2])
      File "matrix_integer_dense.pyx", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form
        if b % a == 0:
      File "matrix0.pyx", line 1927, in sage.matrix.matrix0.Matrix.__mod__
        v[i] = v[i] % p
      File "integer.pyx", line 1335, in sage.rings.integer.Integer.__mod__
      File "integer.pyx", line 3747, in sage.rings.integer.integer
      File "integer.pyx", line 356, in sage.rings.integer.Integer.__init__
    TypeError: unable to coerce element to an integer
**********************************************************************
File "matrix_integer_dense.pyx", line 2970:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[4]>", line 1, in <module>
        a._add_row_and_maintain_echelon_form(vector(ZZ,[Integer(1),Integer(2),Integer(3)]),[Integer(0),Integer(1)])###line 2970:
    sage: a._add_row_and_maintain_echelon_form(vector(ZZ,[1,2,3]),[0,1])
      File "matrix_integer_dense.pyx", line 3013, in sage.matrix.matrix_integer_dense.Matrix_integer_dense._add_row_and_maintain_echelon_form
        if b % a == 0:
      File "matrix0.pyx", line 1927, in sage.matrix.matrix0.Matrix.__mod__
        v[i] = v[i] % p
      File "integer.pyx", line 1335, in sage.rings.integer.Integer.__mod__
      File "integer.pyx", line 3747, in sage.rings.integer.integer
      File "integer.pyx", line 356, in sage.rings.integer.Integer.__init__
    TypeError: unable to coerce element to an integer
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_52
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_matrix_integer_dense.pyx
         [3.2 s]

```



---

Comment by dfdeshom created at 2008-03-13 21:41:21

Thanks I've updated the bundle to take care of these doctest failures. Give it one more try if you can.


---

Comment by jason created at 2008-03-13 22:12:54

What should I apply to review this?  The patch, the bundle, or both?


---

Comment by dfdeshom created at 2008-03-13 22:13:39

Just the bundle


---

Comment by jsp created at 2008-03-14 12:12:27

Here we are again:


```
sage -t  devel/sage-main/sage/matrix/matrix0.pyx            **********************************************************************
File "matrix0.pyx", line 553:
    sage: M[1:,0]
Expected:
    [ 1]
    [ 1]
    [-1]
Got:
    1
**********************************************************************
File "matrix0.pyx", line 566:
    sage: M[range(2),4]
Expected:
    [9]
    [2]
Got:
    9
**********************************************************************
1 items had failures:
   2 of  23 in __main__.example_21
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_matrix0.pyx
         [2.3 s]
sage -t  devel/sage-main/sage/matrix/matrix1.pyx            
         [3.9 s]
sage -t  devel/sage-main/sage/matrix/action.pyx             
         [1.8 s]
sage -t  devel/sage-main/sage/matrix/matrix_generic_sparse.pyx
         [1.6 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/matrix/matrix0.pyx
Total time for all tests: 121.8 seconds

```



---

Attachment


---

Comment by dfdeshom created at 2008-03-14 13:25:02

A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix


---

Comment by jsp created at 2008-03-16 17:26:17

Replying to [comment:18 dfdeshom]:
> A little embarrassing, isn't it? The bundle 2355.hg has been updated and should pass all doctests in sage/matrix 

This patch once again broke a lot of code!

I tried it on a brand new sage-2.10.4.rc0

Just a snapshot:

```
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra.py", line 229, in _repr_
        self.__ngens, self.gens(), self.base_ring())
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/algebras/free_algebra_element.py", line 74, in _repr_
        x = repr_lincomb(mons, cffs).replace("*1 "," ")
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/misc/misc.py", line 508, in repr_lincomb
        b = str(symbols[i])
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__
      File "/home/jaap/work/sage-2.10.3/local/lib/python2.5/site-packages/sage/monoids/free_monoid_element.py", line 103, in _repr_
        x = self.parent().variable_names()
      File "parent_gens.pyx", line 375, in sage.structure.parent_gens.ParentWithGens.variable_names
    RuntimeError: maximum recursion depth exceeded in cmp
**********************************************************************

```


Testing seems to hang on


```
sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx
[1]+  Stopped                 ./sage -t devel/sage-main/sage/matrix/
[jaap`@`paix sage-2.10.4.rc0]$ 

```



---

Comment by mabshoff created at 2008-03-16 17:55:10

Replying to [comment:18 dfdeshom]:
> The bundle 2355.hg has been updated and should pass all doctests in sage/matrix 

Didier,

please post only Mercurial patches. `hg export tip > foo.patch` works perfectly well. Bundles for single commits are a serious annoyance.

Cheers,

Michael


---

Comment by dfdeshom created at 2008-03-17 03:17:13

Replying to [comment:19 jsp]:
> I tried it on a brand new sage-2.10.4.rc0

All tests pass on 2.10.3 here. 2.10.4rc0 obviously broke something so I'll wait until 2.10.4 is officially released to see what broke what.


---

Comment by dfdeshom created at 2008-03-18 05:35:27

Jaap, 2.4.10 with this patch passes all tests I care about (I ran sage -testall and only the matplotlib tests fail). This is on sage.math. I've reposted the patch file, it is named 2355.patch. Please try it out and if you still have failures, let me know which files/tests break what, your platform, etc.


---

Comment by jsp created at 2008-03-20 15:27:59

The patch works for me now!

Cheers,

Jaap


---

Comment by mabshoff created at 2008-03-20 23:57:43

Hi, 

while the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.

Cheers,

Michael


---

Attachment

Replying to [comment:24 mabshoff]:
> Hi, 
> 
> while the patch passes doctests for me with 2.10.4 [modulo some known problems] I am still reluctant to apply this until the performance concern that was raised has been addressed.
> 
> Cheers,
> 
> Michael

I've lost some speed while working on this. I've optimized the code a bit. Overall, my version is still slower because I'm doing more type-checking and handling more functionality (I think that's the reason):


```
# M is the same as above

# element-by-element: slower by about 0.1 micro-seconds ~ 1.2x slower

#2355
sage: %timeit M[2,3]
1000000 loops, best of 3: 395 ns per loop

#main
sage: %timeit M[2,3]
1000000 loops, best of 3: 304 ns per loop

# single slices: slower by < 1 micro-seconds ~ 1.01x slower

#2355
sage: %timeit M[:4]
10000 loops, best of 3: 48 Âµs per loop

#main
sage: %timeit M[:4]
10000 loops, best of 3: 48.5 Âµs per loop

# Getting a whole row: faster by < 1 micro-seconds 
#2355 
sage: %timeit M[3]
10000 loops, best of 3: 72.2 µs per loop

#main
sage: %timeit M[3]
10000 loops, best of 3: 72.9 µs per loop
}}} 

I'm not posting speed comparisons using the other cases (ie, `M[:3,2:]`) since sage doesn't handle them right now.

If people think this speed loss is unacceptable, I could try to fold the extra functionality into the `submatrix` method instead which would leave `__getitem__` idem. 


2355.patch is updated. Warning: I've added a new file: `ext/python_slice.pxi` to have fast access to slice objects so the patch is a bit heavy and rebuilds everything ( nearly everything depends on python.pxi). Passes all tests in `matrix/`.


---

Comment by gfurnish created at 2008-03-25 23:34:32


```
# M is the same as above

# element-by-element: 

#2355
sage: %timeit M[2,3]
1000000 loops, best of 3: 111 ns per loop

#main
sage: %timeit M[2,3]
1000000 loops, best of 3: 111 ns per loop

# single slices: 

#2355
sage: %timeit M[:4]
10000 loops, best of 3: 28.4 Âµs per loop

#main
sage: %timeit M[:4]
10000 loops, best of 3: 29.6 Âµs per loop

# Getting a whole row: 
#2355 
sage: %timeit M[3]
10000 loops, best of 3: 42.3 Âµs per loop

#main
sage: %timeit M[3]
10000 loops, best of 3: 43.7 Âµs per loop
```

I note these were the best times.  In my tests for (1) the new source averaged faster then main.


---

Attachment

Apply on top of 2355.patch


---

Comment by gfurnish created at 2008-03-26 09:08:42

I ran this on sage math, and while 1 was on average faster (although best time was slower), both 2 and 3 were slower.  I'm chalking this up to differences between the Core 2 and Opteron architecture.  __getitem__ is not a cdef function, so I don't see why we should be worrying over a 1Âµs slowdown on some older systems.  Also, 1 is the common case, so I don't see a good reason to worry about the slower cases of 2 and 3.  Note this test was done with "-O2" and the new build system.


---

Comment by mabshoff created at 2008-03-28 15:27:33

Looks good to me. My concerns regarding performance have been addressed. It merges cleanly against my 2.11.alpha2 tree. If this doctests ok I will merge.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 16:32:14

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 16:32:14

Resolution: fixed
