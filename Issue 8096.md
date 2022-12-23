# Issue 8096: Coersion of square matrices is slow

Issue created by migration from https://trac.sagemath.org/ticket/8096

Original creator: boothby

Original creation time: 2010-01-27 20:32:00

Assignee: was

CC:  robertwb malb

Multiplication of small square matrices is ridiculously slow:

```
sage: for d in range(1, 100):
...    print d
...    A = random_matrix(GF(3), d)
...    B = random_matrix(GF(3), d)
...    timeit("C = A*B")
    

1
625 loops, best of 3: 93.8 µs per loop
2
625 loops, best of 3: 93.9 µs per loop
3
625 loops, best of 3: 94.2 µs per loop
4
625 loops, best of 3: 94.1 µs per loop
5
625 loops, best of 3: 94.7 µs per loop
6
625 loops, best of 3: 94.9 µs per loop
7
625 loops, best of 3: 95.2 µs per loop
8
625 loops, best of 3: 95.8 µs per loop
9
625 loops, best of 3: 96.8 µs per loop
10
625 loops, best of 3: 97.6 µs per loop
11
625 loops, best of 3: 98.1 µs per loop
12
625 loops, best of 3: 101 µs per loop
13
625 loops, best of 3: 101 µs per loop
14
625 loops, best of 3: 104 µs per loop
15
625 loops, best of 3: 104 µs per loop
16
625 loops, best of 3: 108 µs per loop
17
625 loops, best of 3: 108 µs per loop
18
625 loops, best of 3: 113 µs per loop
19
625 loops, best of 3: 112 µs per loop
20
625 loops, best of 3: 118 µs per loop
21
625 loops, best of 3: 117 µs per loop
22
625 loops, best of 3: 125 µs per loop
23
625 loops, best of 3: 123 µs per loop
24
625 loops, best of 3: 133 µs per loop
25
625 loops, best of 3: 129 µs per loop
26
625 loops, best of 3: 143 µs per loop
27
625 loops, best of 3: 137 µs per loop
28
625 loops, best of 3: 155 µs per loop
29
625 loops, best of 3: 147 µs per loop
30
625 loops, best of 3: 166 µs per loop
31
625 loops, best of 3: 157 µs per loop
32
625 loops, best of 3: 179 µs per loop
33
625 loops, best of 3: 168 µs per loop
34
625 loops, best of 3: 196 µs per loop
35
625 loops, best of 3: 182 µs per loop
36
625 loops, best of 3: 214 µs per loop
37
625 loops, best of 3: 198 µs per loop
38
625 loops, best of 3: 234 µs per loop
39
625 loops, best of 3: 213 µs per loop
40
625 loops, best of 3: 255 µs per loop
41
625 loops, best of 3: 231 µs per loop
42
625 loops, best of 3: 279 µs per loop
43
625 loops, best of 3: 251 µs per loop
44
625 loops, best of 3: 307 µs per loop
45
625 loops, best of 3: 271 µs per loop
46
625 loops, best of 3: 335 µs per loop
47
625 loops, best of 3: 298 µs per loop
48
625 loops, best of 3: 363 µs per loop
49
625 loops, best of 3: 319 µs per loop
50
625 loops, best of 3: 401 µs per loop
51
625 loops, best of 3: 346 µs per loop
```


Here's a profile of the 1x1 case:


```
625 loops, best of 3: 91.7 µs per loop
         810004 function calls in 5.980 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    40000    0.100    0.000    0.100    0.000 :0(IntegerMod)
    30000    0.080    0.000    0.080    0.000 :0(append)
    10000    0.030    0.000    0.030    0.000 :0(base_ring)
    10000    0.150    0.000    0.900    0.000 :0(category)
    40000    0.250    0.000    0.290    0.000 :0(has_key)
    10000    0.070    0.000    0.070    0.000 :0(hasattr)
    10000    0.030    0.000    0.030    0.000 :0(is_Matrix)
    80000    0.250    0.000    0.250    0.000 :0(isinstance)
    30000    0.070    0.000    0.070    0.000 :0(keys)
    30000    0.040    0.000    0.040    0.000 :0(len)
    30001    0.080    0.000    0.080    0.000 :0(range)
    10000    0.030    0.000    0.030    0.000 :0(setdefault)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
    30000    0.140    0.000    0.140    0.000 :0(sorted)
        1    0.380    0.380    5.980    5.980 <string>:1(<module>)
    30000    0.250    0.000    1.750    0.000 cachefunc.py:155(get_key)
    10000    0.060    0.000    0.850    0.000 cachefunc.py:220(__call__)
    10000    0.060    0.000    0.090    0.000 cachefunc.py:254(get_cache)
    10000    0.050    0.000    0.050    0.000 cachefunc.py:275(__get__)
    20000    0.270    0.000    1.550    0.000 cachefunc.py:76(__call__)
    20000    0.060    0.000    0.060    0.000 cachefunc.py:95(get_cache)
    10000    0.070    0.000    2.520    0.000 category.py:459(__contains__)
    10000    0.360    0.000    1.550    0.000 category.py:651(is_subcategory)
    20000    0.120    0.000    1.670    0.000 classcall_metaclass.py:64(__call__)
    20000    0.040    0.000    0.040    0.000 finite_field_prime_modn.py:121(characteristic)
    20000    0.110    0.000    0.110    0.000 finite_field_prime_modn.py:187(order)
    30000    1.010    0.000    1.500    0.000 function_mangling.py:205(fix_to_pos)
    30000    0.080    0.000    0.080    0.000 function_mangling.py:261(<genexpr>)
    40000    0.290    0.000    0.390    0.000 integer_mod_ring.py:733(__call__)
    10000    0.050    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)
    10000    0.450    0.000    0.710    0.000 matrix_space.py:1035(matrix)
    10000    0.140    0.000    4.000    0.000 matrix_space.py:1089(matrix_space)
    10000    0.200    0.000    3.830    0.000 matrix_space.py:110(MatrixSpace)
    10000    0.000    0.000    0.000    0.000 matrix_space.py:1112(ncols)
    10000    0.030    0.000    0.030    0.000 matrix_space.py:1124(nrows)
    10000    0.310    0.000    1.270    0.000 matrix_space.py:271(__call__)
    10000    0.000    0.000    0.000    0.000 misc.py:514(get_verbose)
        1    0.000    0.000    5.980    5.980 profile:0(for i in range(10000): C = A*B)
        0    0.000             0.000          profile:0(profiler)
    90000    0.270    0.000    0.270    0.000 unique_representation.py:454(__eq__)
```



---

Comment by boothby created at 2010-01-27 22:11:20

Changing assignee from was to boothby.


---

Attachment


---

Comment by boothby created at 2010-01-28 01:11:34

I'm not sure that I did this in the right place, but it cuts the time to multiply two 1x1 matrices down to 1/3 of the previous time -- which is still dog slow, but significantly better.  As a reference,


```
sage: A = GF(3).random_element()
sage: B = GF(3).random_element()
sage: timeit("C = A*B")
625 loops, best of 3: 142 ns per loop
```


and with this patch, I'm getting:


```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 32.5 µs per loop

sage: import profile
sage: profile.run("for i in range(10000): C = A*B")
         250004 function calls in 1.840 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    40000    0.120    0.000    0.120    0.000 :0(IntegerMod)
    10000    0.070    0.000    0.070    0.000 :0(hasattr)
    10000    0.060    0.000    0.060    0.000 :0(is_Matrix)
    70000    0.190    0.000    0.190    0.000 :0(isinstance)
        1    0.000    0.000    0.000    0.000 :0(range)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.400    0.400    1.840    1.840 <string>:1(<module>)
    20000    0.060    0.000    0.060    0.000 finite_field_prime_modn.py:121(characteristic)
    40000    0.230    0.000    0.350    0.000 integer_mod_ring.py:733(__call__)
    10000    0.060    0.000    0.070    0.000 matrix_group_element.py:68(is_MatrixGroupElement)
    10000    0.390    0.000    0.720    0.000 matrix_space.py:1035(matrix)
    10000    0.030    0.000    0.030    0.000 matrix_space.py:1112(ncols)
    10000    0.020    0.000    0.020    0.000 matrix_space.py:1124(nrows)
    10000    0.160    0.000    1.100    0.000 matrix_space.py:271(__call__)
    10000    0.050    0.000    0.050    0.000 misc.py:514(get_verbose)
        1    0.000    0.000    1.840    1.840 profile:0(for i in range(10000): C = A*B)
        0    0.000             0.000          profile:0(profiler)
```



---

Comment by boothby created at 2010-01-28 01:11:34

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-01-30 23:44:39

Replying to [comment:2 boothby]:

> ... As a reference, ` sage: A = GF(3).random_element() sage: B = GF(3).random_element() sage: timeit("C = A*B") 625 loops, best of 3: ``142 ns`` per loop ` and with this patch, I'm getting: {{{ sage: d = 1 sage: A = random_matrix(GF(3), d) sage: B = random_matrix(GF(3), d) sage: timeit("C = A*B") 625 loops, best of 3: 32.5 µs per loop

But 32.5 µs (with the patch) is much _slower _than `142 ns (without the patch)!`


---

Comment by boothby created at 2010-01-31 06:36:24

You'll note that the 32.5µs is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101µs.

I'd like the 32.5µs to go away, but I don't know how much of that would be possible, at the moment.


---

Comment by SimonKing created at 2010-01-31 09:41:31

Replying to [comment:4 boothby]:

> You'll note that the 32.5µs is matrix-by-matrix, whereas the 142ns is element-by-element.  Before my patch, the matrix-by-matrix time was 101µs. I'd like the 32.5µs to go away, but I don't know how much of that would be possible, at the moment.

OK, then it is an improvement. I hope to be able to do some refereeing later today or tomorrow.

Anyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By "slow", I mean "compared with MeatAxe matrices as provided by my cohomology spkg":


```
sage: from pGroupCohomology.mtx import MTX
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
625 loops, best of 3: 99.6 Âµs per loop
sage: timeit("c=a*b")
625 loops, best of 3: 1.01 Âµs per loop
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
sage: A = random_matrix(F,100)
sage: B = random_matrix(F,100)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
125 loops, best of 3: 2.43 ms per loop
sage: timeit("c=a*b")
625 loops, best of 3: 376 Âµs per loop
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
```



---

Comment by robertwb created at 2010-01-31 10:18:46

Replying to [comment:5 SimonKing]:

> Anyway, I still wonder why basic matrix operations in Sage tend to be so slow. I mean, do any complicated operations with parents happen behind the scenes? By "slow", I mean "compared with MeatAxe matrices as provided by my cohomology spkg":

This is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.


---

Comment by SimonKing created at 2010-01-31 11:52:35

Replying to [comment:6 robertwb]:

> This is because they have only been optimized for large dimension and word-sized p. I bet MeatAxe is slower for 1000 x 1000 matrices.

You just lost the bet.


```
sage: from pGroupCohomology.mtx import MTX
sage: F = GF(3)
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: a = MTX(3,[list(r) for r in A.rows()])
sage: b = MTX(3,[list(r) for r in B.rows()])
sage: timeit("C=A*B")
5 loops, best of 3: 12.6 s per loop
sage: timeit("c=a*b")
5 loops, best of 3: 2.01 s per loop
sage: C = A*B
sage: a*b == MTX(3,[list(r) for r in C.rows()])
True
```

When I did some benchmarks two years ago, I was often astonished how MeatAxe outperformed the usual matrices in Sage in basic operations such as computing hash, copying, getting the list of coefficients, changing a coefficient, etc: Hash and copying took _seconds_ for size 10000x10000!

I complained, and things did improve: hash and copy is alright. But with the above matrix, loads(dumps(A)) did not terminate after a minute, and ate 90% of my computer's memory.


---

Attachment

apply on top of previous


---

Comment by robertwb created at 2010-01-31 13:18:04

SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic? At least one can do


```
sage: A = random_matrix(GF(3), 2000)
sage: B = random_matrix(GF(3), 2000)
sage: %timeit A._multiply_linbox(B)
5 loops, best of 3: 1.9 s per loop
```


but I agree the current state of matrices are in quite a bit of a mess. Granted, most of this code was written *way* back before Sage had the quality control it has now, just to get something up and running, and hasn't been touched since. (They're pretty good over Z and Q, which is what I use...)

Tom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.


---

Comment by SimonKing created at 2010-01-31 16:05:22

Replying to [comment:8 robertwb]:

> SimonKing: I'm impressed and depressed. Is MeatAxe's runtime a function of the characteristic?

Yes. Over a non-prime field:


```
sage: F = GF(8,'t')
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: from pGroupCohomology.mtx import MTX
sage: a = MTX(8,[list(r) for r in A.rows()])
sage: b = MTX(8,[list(r) for r in B.rows()])
sage: %time c = a*b
CPU times: user 5.19 s, sys: 0.00 s, total: 5.19 s
Wall time: 5.19 s
sage: %time C = A*B
```

The last line took several minutes, and it was not possible to interrupt with Ctrl-c. So, I had to kill the Python process.

And with a bigger prime, comparing against linbox:


```
sage: F = GF(37)
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: a = MTX(37,[list(r) for r in A.rows()])
sage: b = MTX(37,[list(r) for r in B.rows()])
sage: %time c = a*b
CPU times: user 11.83 s, sys: 0.00 s, total: 11.84 s
Wall time: 11.87 s
sage: %time C = A._multiply_linbox(B)
CPU times: user 1.82 s, sys: 0.00 s, total: 1.82 s
Wall time: 1.82 s
sage: %time C = A*B
CPU times: user 12.65 s, sys: 0.00 s, total: 12.65 s
Wall time: 12.70 s
```

In other words, for bigger fields, linbox is clearly better than MeatAxe, but the overhead kills it.

> At least one can do ` sage: A = random_matrix(GF(3), 2000) sage: B = random_matrix(GF(3), 2000) sage: %timeit A._multiply_linbox(B) 5 loops, best of 3: 1.9 s per loop`

Again, there is a huge overhead. But at what point? I mean, the parents of A and B are the same, so, it can't be in the coercion model. And if two matrices have the same parent, then I'd expect that `A*B` would simply call A._multiply_linbox(B).

> Tom: Your patch looks good, positive review to that. I've posted another patch which provides another 2x speedup. There's still a lot of cruft it goes through, and matrix_space could really stand to be cythonized (there are 3 mandatory Python calls on it every time a matrix is created), but I don't have time to dig through it now.

Which means, a third person (e.g.) should review both Tom's and your patch, right?


---

Comment by SimonKing created at 2010-01-31 16:31:01

With the patch, I get:


```
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: %timeit C = A*B
625 loops, best of 3: 14.9 µs per loop # was: 99.6 Âµs
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: %timeit C = A*B
5 loops, best of 3: 12.4 s per loop # was: 12.6 s
```

So, there is only a small improvement. But it _is_ an improvement.

I currently do sage -testall. If it passes, I'll give it a positive review, and suggest to open two new tickets, one concerning the overhead in multiplying matrices, the other concerning the problem that loads(dumps()) fails on big matrices.


---

Comment by SimonKing created at 2010-01-31 17:47:00

There are doctest failures after installing the patches. See http://sage.math.washington.edu/home/SimonKing/logs/8096test.log

Some of these failures seem pretty severe. There are unexpected numerical values and recursion depth problems.

Do you have an idea how such innocent-looking change can have such a big effect?


---

Comment by SimonKing created at 2010-01-31 17:47:00

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2010-02-01 00:17:26

Looks to me like the second patch isn't compatible matrix_double_dense -- that's an easy fix.  I'm unsure of matrix_2x2, though.  I'll check these out after I get some homework done.


---

Comment by SimonKing created at 2010-02-01 08:24:02

Hi Tom!

Hopefully your fix will work. This message is mainly to test whether it works with Firefox 3.0.6 on my desktop computer to commit a message starting in wysiwyg mode.


---

Comment by jason created at 2010-03-17 06:01:59

Changing type from defect to enhancement.


---

Comment by SimonKing created at 2011-07-12 14:03:01

I think it is worth while to revive that ticket!

There has been some work done in the past, e.g., on #10763 (already merged) and #11589. I therefore suggest to start with determining the status quo (performance wise). 

The following is with sage-4.7.rc2 (which contains #10763) and #11589. I provide the timings with sage-4.6.2 in square brackets:

```
sage: F = GF(3)
sage: A = random_matrix(F,3)
sage: B = random_matrix(F,3)
sage: %timeit C = A*B
625 loops, best of 3: 36.6 µs per loop
[625 loops, best of 3: 54.6 µs per loop]
sage: A = random_matrix(F,2000)
sage: B = random_matrix(F,2000)
sage: %timeit C = A*B
5 loops, best of 3: 8.36 s per loop
[5 loops, best of 3: 8.27 s per loop]
```


So, part of the issue with small matrices is resolved. The second patch [attachment:8096-new_matrix.patch] is actually obsoleted by #10763 and #11589, and the first patch needs to be rebased.

However, large matrices are still not nice. We have seen that linbox provides a much faster multiplication. Wouldn't it be a valid approach to use linbox more often? Perhaps make it the default over finite fields?


---

Comment by SimonKing created at 2011-07-12 15:11:19

For the record: Today I slightly improved MeatAxe matrix initialisation (my MeatAxe wrapper relies on a modified/improved version of MeatAxe-2.2.4, and today I added memset). 

Now, multiplication of two random 2000x2000 matrices over GF(3) takes 1.72 seconds with MeatAxe (it used to be 11 seconds, without memset), compared to 1.65 seconds with _multiply_linbox and 8.34 seconds with plain Sage matrices.

I really wonder why linbox isn't used by default.


---

Comment by SimonKing created at 2011-07-18 21:32:15

I guess that the generic Strassen-Winograd implementation in sage.matrix.strassen is related with, but not really in the focus of, this ticket. Therefore I opened a new ticket for Strassen: #11610.


---

Comment by SimonKing created at 2011-08-11 17:38:44

Here is another data point concerning slowness - ridiculous slowness, actually - of matrix multiplication in Sage. The following is with sage-4.7.1.rc1 plus the patches from #11589:

```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
# I think the following is already WAY too slow!
sage: %time A = MS.random_element()
CPU times: user 38.42 s, sys: 0.13 s, total: 38.55 s
Wall time: 38.67 s
sage: B = MS.random_element()
sage: %time C = A*B
^C^C^C^C^C^C^C^C^C^C^C^C^C^C
```


In other words:

 1. The computation can not be interrupted, which is a bug.
 2. The computation takes more than 45 minutes!!!
 3. The computation takes more than 880 MB.

As much as I see, GF(2) is the _only_ finite field such that multiplication of square matrices over that field is not blatantly slow in Sage.

It makes me wonder if we shouldn't use a different package for matrix multiplication over finite fields different from GF(2).

As much as I know, there already is an experimental version for matrices over `GF(2^n)`, isn't it, Martin? How fast is it?

Over finite prime fields, we could use Linbox. There are tickets to do so.

But What about finite non-prime fields? Would it be a reasonable idea to use something based on `MeatAxe`?

I will very likely be using a Sage wrapper for `MeatAxe` matrices in my current project. So, I'll do the work anyway. From my perspective, the only question is whether we can/should use it by default in Sage.

Here are some relevant data:

1. I work on top of `MeatAxe 2.2.4`. That version is identic with 2.2.3, with one important difference. While all other meataxe versions are `GPL 2`, version 2.2.4 is `GPL 2+`. In fact, that version was made after I wanted to use meataxe 2.2.3 in my group cohomology package and asked Michael Ringe whether he could provide it in `GPL 2+`. 

2. I am not just wrapping it, in fact I am branching meataxe. I improved the implementation of the "school book" multiplication in meataxe, and I implemented Strassen-Winograd multiplication, which had so far been missing in meataxe.

3. It would provide a vastly better performance. The above 5000x5000 multiplication over GF(4) with the school book method needs 173.68 CPU seconds and about 200 MB. With Strassen-Winograd, it is  only 85.04 CPU seconds, using less than 280 MB.

4. Concerning prime fields: A multiplication of two 5000x5000 matrices A, B over GF(5) using `A._multipliy_linbox(B)` needs 21.49 CPU seconds and 1.2 GB(!). Using school book multiplication in meataxe, it is 46.70 s and 140 MB, or 30.29 CPU seconds and 160 MB using Strassen-Winograd.

__Conclusion__

 * The licence of `MeatAxe 2.2.4` would be fine.

 * The default matrix multiplication over finite fields that is currently provided in Sage is not competitive at all.

 * Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.

 * As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).

 * My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.

 * Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. There is a "big" version of meataxe that can deal with field sizes of up to `2^16-1`, but I did not wrap it yet, and I don't know how difficult it would be.

As I said: I will work on that wrapper anyway, because it seems well suited for my current project. But would it make sense in Sage as a default implementation for matrices over small finite fields (or at least over the non-prime fields)?


---

Comment by SimonKing created at 2011-08-11 17:38:44

Changing status from needs_work to needs_info.


---

Comment by jason created at 2011-08-11 17:57:48

I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/


---

Comment by SimonKing created at 2011-08-11 18:09:22

Replying to [comment:19 jason]:
> I'm curious: have you compared with the matrix multiplication routines in flint 2? http://www.flintlib.org/

Perhaps I am confusing things; but the impression that I got from polynomials in Sage is that flint and ntl are over the rationals and the integers. Does flint also do finite fields? Is the relevant part of flint available in Sage, or do I need to install flint separately?


---

Comment by jason created at 2011-08-11 18:18:42

Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.


---

Comment by SimonKing created at 2011-08-11 18:27:04

Replying to [comment:21 jason]:
> Flint 2.20 (which is not in Sage yet, IIRC) apparently handles Z mod n matrices.  See section 19 of the manual: http://www.flintlib.org/flint-2.2.pdf.

Yep, I was just reading the documentation.

They have matrices over Z/nZ, but I don't see finite fields mentioned. Except prime fields, of course. They go up to `n=2^64-1`, which Meataxe can't manage, even in the big implementation (the field size must be less than `2^16`).

Concerning comparison of matrix operations, one must not forget higher level operations. To compute the echelon form of a 5000x5000 matrix over GF(5), the default implementation in Sage needs 12.65 s and 1.2 GB on my machine. _echelonize_linbox needs the same.

Meataxe needs much less memory, but 45 seconds. Admittedly I did not care about echelonization in meataxe, since I don't need it for my application. Hm. That could be a show stopper.


---

Comment by SimonKing created at 2011-08-11 18:42:48

The original implementation of school book multiplication was far from optimal, and thus I guess that the school book echelonization in meataxe isn't optimal as well. And meataxe does not use Strassen's algorithm for echelon computation.

So, there probably is a similar room for improvement of echelonization than it was for matrix multiplication.

The problem is that, so far, the echelonization does not seem to be a bottle neck for my application. So, my motivation to implement it is not exactly big. But who knows: At some point of my project, I _will_ be needing echelonization - I just don't know, yet, how large the matrix sizes will eventually be.


---

Comment by jason created at 2011-08-11 19:28:38

Yes, I should have clarified that I meant that it would be potentially interesting to compare flint 2 speeds for Z/pZ (p prime) with the other code that you are comparing, given that flint has a reputation for being blazingly fast.  Of course, it's not a total solution or replacement for meataxe, since meataxe handles many more fields.


---

Comment by fredrik.johansson created at 2011-08-11 22:11:21

Just a heads-up: flint2 should hold up well for a 32-bit or 64-bit prime field, but it is not optimized for and probably slower than some other libraries (e.g. Linbox) over something like GF(5). And yes, only prime fields are supported.


---

Comment by malb created at 2011-08-15 15:27:42

> As much as I know, there already is an experimental version for matrices over 
> GF(2^n), isn't it, Martin? How fast is it?

Sorry, I completely missed this question. M4RIE, i.e. dense linear algebra over GF(2<sup>e</sup>) for 2 <= e <= 10, is either about as fast as Magma or much faster. Actually, it's not experimental but a fully working patch + library has been around for ages, it was agreed months ago it would go into Sage, there has just not been enough push to finish the review: #9562

Here's a summary of the current approach & performance:

http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf

To compare with your results:

*Karatsuba*


```python
sage: K.<a> = GF(4)
sage: A = random_matrix(K,5000,5000)
sage: B = random_matrix(K,5000,5000)
sage: %time C=A*B
CPU times: user 0.51 s, sys: 0.01 s, total: 0.52 s
Wall time: 0.52 s
```


*Travolta*


```python
sage: K.<a> = GF(4)
sage: A = random_matrix(K,5000,5000)
sage: B = random_matrix(K,5000,5000)
sage: %time C=A._multiply_travolta(B)
CPU times: user 1.19 s, sys: 0.00 s, total: 1.20 s
Wall time: 1.20 s
```


So both algorithms in M4RIE are much faster than ~80 seconds. I didn't precisely measure memory consumption though. 



> The default matrix multiplication over finite fields that is currently provided in Sage is  not competitive at all.

Very much agreed!

> Over prime fields, Linbox is still faster, but my implementation of Strassen multiplication needs only one tenth of the memory.

I hope to fix this next week at Sage Days, i.e. to wrap LinBox properly.

> As far as I know, Linbox does not officially support non-prime fields, in contrast to meataxe. And Meataxe is a lot faster than the current implementation in Sage, except for GF(2).

Clément told me that LinBox does support non-prime fields we just never wrapped them in Sage.

> My meataxe wrapper could still be improved - I have no idea of how to optimize the use of L1 and L2 cache, and would need help to do so.

Let's move that to e-mail.

> Big disadvantage of my current meataxe wrapper: It only supports field sizes less than 256. 

I don't think it's that big of an issue, a lot of applications need small fields!


---

Comment by malb created at 2011-08-15 15:40:19

One more data point.

Again, this is with #9562:


```python
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: %time A = MS.random_element()
CPU times: user 0.46 s, sys: 0.01 s, total: 0.46 s
Wall time: 0.47 s
sage: B = MS.random_element()
sage: %time C = A*B 
CPU times: user 22.69 s, sys: 0.06 s, total: 22.75 s
Wall time: 22.84 s
```


Note that we only implemented Travolta for GF(2<sup>6</sup>) so far. With Karatsuba we expect to get close to 4.5 seconds, because:


```python
sage: A = random_matrix(GF(2),5000,5000)
sage: B = random_matrix(GF(2),5000,5000)
sage: %timeit C=A*B
5 loops, best of 3: 249 ms per loop
```


and the best known formula for degree 5 polynomials needs 17 such multiplications: 

http://www.csd.uwo.ca/~eschost/Exam/Montgomery--Five_six_and_seven_terms_Karatsuba-like_formulae.pdf


---

Comment by malb created at 2011-08-15 15:48:21

... and Magma for comparison:

GF(2<sup>2</sup>):


```
Magma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]
Type ? for help.  Type <Ctrl>-D to quit.
> K<a> := GF(4);               
> A:=RandomMatrix(K,5000,5000);
> B:=RandomMatrix(K,5000,5000);
> time C:=A*B;                 
Time: 2.130
```


GF(2<sup>6</sup>):


```
Magma V2.15-10    Mon Aug 15 2011 16:41:46 on road     [Seed = 3840120025]
Type ? for help.  Type <Ctrl>-D to quit.
> K<a> := GF(64);
> A:=RandomMatrix(K,5000,5000);
> B:=RandomMatrix(K,5000,5000); 
> time C:=A*B;
Time: 273.310
```


It seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?


---

Comment by SimonKing created at 2011-08-15 15:51:02

Hi Martin!

Your data points are amazing! Good that you point us to #9562, it really seems that it should soon become part of Sage. The link http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy.pdf seems to be broken, though. 

Concerning my application, it probably was a very wise decision that my programs for the computation of Ext algebras of basic algebras are designed to use _any_ type of matrices. So, one can easily pick the fastest available implementation for each base ring. It could be that eventually I will use M4RI(E) for powers of two, Meataxe for non-prime fields and and a full-grown Linbox-wrapper for prime fields except GF(2).


---

Comment by SimonKing created at 2011-08-15 16:01:22

Replying to [comment:28 malb]:
> ... and Magma for comparison:
> 
> GF(2<sup>2</sup>):
> ...
> Time: 2.130

That beats Meataxe by a factor of 12 :-(

> GF(2<sup>6</sup>):
> ...
> Time: 273.310
> It seems your MeatAxe fork is faster than Magma for GF(2<sup>6</sup>)?

Amazing! The Meataxe approach is very simple: Row-first storage of data, as many field elements stored in one Byte as possible (hence, over `GF(2^6)` we have two marks per byte), and multiplication tables that allow to multiply a field element with a whole byte in one go. 
The rest is school book or Strassen-Winograd multiplication.

Anyway. M4RIE seems to be a lot faster, and I am looking forward to use it!


---

Comment by malb created at 2011-08-15 16:04:34

correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf

What does "two marks per byte" mean? Do you store [xxxxxx00][xxxxxx00] or [xxxxxx|xx][xxxx0000] i.e. do you fit one element into one byte or do you really use every bit? In M4RIE (`mzed_t` data type) we do the former. The other representation `mzd_slice_t` stores matrices in "slices": GF(2) matrices.


---

Comment by malb created at 2011-08-15 16:09:45

Btw. the Travolta algorithm is also very simple and just avoids any multiplications in the inner loop. It's complexity is O(n<sup>2</sup>*2<sup>e</sup>) multiplications and O(n<sup>3</sup>) additions.

  cf. https://bitbucket.org/malb/m4rie-old/src/841a71d72e24/matrix.cc#cl-202

Btw. it takes 80 seconds for you to do 5,000 x 5,000 over GF(2<sup>2</sup>) and GF(2<sup>6</sup>)? Can time MeatAxe again and post the two timings here?


---

Comment by SimonKing created at 2011-08-15 16:23:25

Replying to [comment:31 malb]:
> correct link:  http://martinralbrecht.files.wordpress.com/2011/03/20110330_-_m4ri_-_nancy1.pdf

Thank you!

> What does "two marks per byte" mean? 

Sorry, where's my head? For field size 64, only one mark per byte is used, and it is [xxxxxx00][xxxxxx00].

Meataxe packs as many field elements into a single byte as possible. Hence, if you work over GF(5) then a triple of field elements will be packed into one byte. That is since 5<sup>3</sup> is smaller than 256, but 5<sup>4</sup> is bigger.

So, really quite simplistic. No bit slicing or anything fancy.


---

Comment by SimonKing created at 2011-08-15 17:39:10

Martin, I just found that M4RIE just needs 10.42 seconds resp. 8.78 seconds on my computer for multiplying two random 5000x5000 matrices over GF(64).


```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: A = MS.random_element()
sage: type(A)
<type 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense'>
sage: B = MS.random_element()
sage: %time C = A*B
CPU times: user 10.42 s, sys: 0.15 s, total: 10.56 s
Wall time: 10.60 s
sage: %time C = A._mult
A._multiply_classical  A._multiply_karatsuba  A._multiply_strassen   A._multiply_travolta
sage: %time C = A._multiply_travolta(B)
CPU times: user 8.73 s, sys: 0.02 s, total: 8.75 s
Wall time: 8.78 s
```


That's awesome! For these particular matrices, the Meataxe fork needs 85.26 seconds. Hopefully I'll be able to review #9562 tomorrow.


---

Comment by SimonKing created at 2011-11-28 09:01:57

This ticket is "needs info". What info is actually needed?


---

Comment by SimonKing created at 2012-03-02 10:06:23

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2012-03-02 10:06:23

Again, what information is needed? I'm changing it into "needs review", since I don't see a question that needed to be addressed.


---

Comment by robertwb created at 2012-03-02 10:49:43

Agreed. This ticket is about the overhead of multiplying small matrices, not the runtime of large non-prime-finite-field matrices.


---

Comment by davidloeffler created at 2012-03-10 17:01:16

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-10 17:01:16

These patches do not apply correctly on either the current release or the current beta (see patchbot logs).


---

Comment by SimonKing created at 2012-03-10 20:34:20

Replying to [comment:38 davidloeffler]:
> These patches do not apply correctly on either the current release or the current beta (see patchbot logs).

No surprise that two-year-old patches don't apply anymore. I am rebasing them now, producing a single patch replacing the two. I am not totally sure, but I think the ideas of the second patch are already in Sage - need to verify it, though.


---

Comment by SimonKing created at 2012-03-10 20:53:32

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-03-10 20:53:32

I have rebased the patches, combining them into one patch. In fact, a part (but not all) of the second patch is not needed anymore, since the creation of the zero matrix has been improved in another ticket.

Here is evidence that the patch still does improve the timings for the computation of small matrices - even after we have switched to linbox:

Without patch:

```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 40.5 µs per loop
```


With the patch:

```
sage: d = 1
sage: A = random_matrix(GF(3), d)
sage: B = random_matrix(GF(3), d)
sage: timeit("C = A*B")
625 loops, best of 3: 18.5 µs per loop
```


I need to run the doctests, though. But needs review.

Apply trac8096_speedup_matrix_parent.patch


---

Comment by SimonKing created at 2012-03-10 21:01:27

Here is the example from the ticket description.

Without the patch:

```
sage: for d in range(1, 70):
....:     print d,
....:     A = random_matrix(GF(3), d)
....:     B = random_matrix(GF(3), d)
....:     timeit("C = A*B")
....:     
1 625 loops, best of 3: 41 µs per loop
2 625 loops, best of 3: 41.1 µs per loop
3 625 loops, best of 3: 41 µs per loop
4 625 loops, best of 3: 41.4 µs per loop
5 625 loops, best of 3: 41.6 µs per loop
6 625 loops, best of 3: 42.4 µs per loop
7 625 loops, best of 3: 42.9 µs per loop
8 625 loops, best of 3: 43.3 µs per loop
9 625 loops, best of 3: 43.5 µs per loop
10 625 loops, best of 3: 44.1 µs per loop
11 625 loops, best of 3: 44.8 µs per loop
12 625 loops, best of 3: 45.5 µs per loop
13 625 loops, best of 3: 46.3 µs per loop
14 625 loops, best of 3: 47.6 µs per loop
15 625 loops, best of 3: 48.8 µs per loop
16 625 loops, best of 3: 50.4 µs per loop
17 625 loops, best of 3: 51.8 µs per loop
18 625 loops, best of 3: 53.4 µs per loop
19 625 loops, best of 3: 54.7 µs per loop
20 625 loops, best of 3: 56.5 µs per loop
21 625 loops, best of 3: 58.4 µs per loop
22 625 loops, best of 3: 60.8 µs per loop
23 625 loops, best of 3: 63.3 µs per loop
24 625 loops, best of 3: 61.7 µs per loop
25 625 loops, best of 3: 64.1 µs per loop
26 625 loops, best of 3: 66.3 µs per loop
27 625 loops, best of 3: 70.3 µs per loop
28 625 loops, best of 3: 72.7 µs per loop
29 625 loops, best of 3: 75.2 µs per loop
30 625 loops, best of 3: 79.4 µs per loop
31 625 loops, best of 3: 82 µs per loop
32 625 loops, best of 3: 86.5 µs per loop
33 625 loops, best of 3: 89.8 µs per loop
34 625 loops, best of 3: 94.3 µs per loop
35 625 loops, best of 3: 98.1 µs per loop
36 625 loops, best of 3: 92.1 µs per loop
37 625 loops, best of 3: 95.9 µs per loop
38 625 loops, best of 3: 100 µs per loop
39 625 loops, best of 3: 105 µs per loop
40 625 loops, best of 3: 109 µs per loop
41 625 loops, best of 3: 117 µs per loop
42 625 loops, best of 3: 123 µs per loop
43 625 loops, best of 3: 129 µs per loop
44 625 loops, best of 3: 136 µs per loop
45 625 loops, best of 3: 142 µs per loop
46 625 loops, best of 3: 149 µs per loop
47 625 loops, best of 3: 156 µs per loop
48 625 loops, best of 3: 146 µs per loop
49 625 loops, best of 3: 154 µs per loop
50 625 loops, best of 3: 161 µs per loop
51 625 loops, best of 3: 168 µs per loop
52 625 loops, best of 3: 177 µs per loop
53 625 loops, best of 3: 185 µs per loop
54 625 loops, best of 3: 194 µs per loop
55 625 loops, best of 3: 202 µs per loop
56 625 loops, best of 3: 213 µs per loop
57 625 loops, best of 3: 222 µs per loop
58 625 loops, best of 3: 234 µs per loop
59 625 loops, best of 3: 244 µs per loop
60 625 loops, best of 3: 225 µs per loop
61 625 loops, best of 3: 235 µs per loop
62 625 loops, best of 3: 248 µs per loop
63 625 loops, best of 3: 260 µs per loop
64 625 loops, best of 3: 271 µs per loop
65 625 loops, best of 3: 287 µs per loop
66 625 loops, best of 3: 297 µs per loop
67 625 loops, best of 3: 311 µs per loop
68 625 loops, best of 3: 324 µs per loop
69 625 loops, best of 3: 340 µs per loop
```


With the patch:

```
sage: for d in range(1, 70):
....:     print d,
....:     A = random_matrix(GF(3), d)
....:     B = random_matrix(GF(3), d)
....:     timeit("C = A*B")
....:     
1 625 loops, best of 3: 18.3 µs per loop
2 625 loops, best of 3: 18.4 µs per loop
3 625 loops, best of 3: 18.5 µs per loop
4 625 loops, best of 3: 18.8 µs per loop
5 625 loops, best of 3: 18.9 µs per loop
6 625 loops, best of 3: 19.5 µs per loop
7 625 loops, best of 3: 19.9 µs per loop
8 625 loops, best of 3: 20.3 µs per loop
9 625 loops, best of 3: 21 µs per loop
10 625 loops, best of 3: 21.4 µs per loop
11 625 loops, best of 3: 22 µs per loop
12 625 loops, best of 3: 22.4 µs per loop
13 625 loops, best of 3: 23.9 µs per loop
14 625 loops, best of 3: 24.9 µs per loop
15 625 loops, best of 3: 25.6 µs per loop
16 625 loops, best of 3: 27.2 µs per loop
17 625 loops, best of 3: 28.2 µs per loop
18 625 loops, best of 3: 29.8 µs per loop
19 625 loops, best of 3: 31.4 µs per loop
20 625 loops, best of 3: 33.1 µs per loop
21 625 loops, best of 3: 35 µs per loop
22 625 loops, best of 3: 37.2 µs per loop
23 625 loops, best of 3: 39.4 µs per loop
24 625 loops, best of 3: 38.3 µs per loop
25 625 loops, best of 3: 40.9 µs per loop
26 625 loops, best of 3: 43.2 µs per loop
27 625 loops, best of 3: 46 µs per loop
28 625 loops, best of 3: 49 µs per loop
29 625 loops, best of 3: 51.9 µs per loop
30 625 loops, best of 3: 55.2 µs per loop
31 625 loops, best of 3: 58.3 µs per loop
32 625 loops, best of 3: 62.8 µs per loop
33 625 loops, best of 3: 66.9 µs per loop
34 625 loops, best of 3: 71.1 µs per loop
35 625 loops, best of 3: 75.1 µs per loop
36 625 loops, best of 3: 68.1 µs per loop
37 625 loops, best of 3: 72.3 µs per loop
38 625 loops, best of 3: 76.9 µs per loop
39 625 loops, best of 3: 81.7 µs per loop
40 625 loops, best of 3: 85.8 µs per loop
41 625 loops, best of 3: 94.2 µs per loop
42 625 loops, best of 3: 99.8 µs per loop
43 625 loops, best of 3: 106 µs per loop
44 625 loops, best of 3: 112 µs per loop
45 625 loops, best of 3: 119 µs per loop
46 625 loops, best of 3: 126 µs per loop
47 625 loops, best of 3: 132 µs per loop
48 625 loops, best of 3: 123 µs per loop
49 625 loops, best of 3: 130 µs per loop
50 625 loops, best of 3: 137 µs per loop
51 625 loops, best of 3: 145 µs per loop
52 625 loops, best of 3: 153 µs per loop
53 625 loops, best of 3: 162 µs per loop
54 625 loops, best of 3: 170 µs per loop
55 625 loops, best of 3: 180 µs per loop
56 625 loops, best of 3: 190 µs per loop
57 625 loops, best of 3: 200 µs per loop
58 625 loops, best of 3: 210 µs per loop
59 625 loops, best of 3: 221 µs per loop
60 625 loops, best of 3: 202 µs per loop
61 625 loops, best of 3: 212 µs per loop
62 625 loops, best of 3: 224 µs per loop
63 625 loops, best of 3: 237 µs per loop
64 625 loops, best of 3: 248 µs per loop
65 625 loops, best of 3: 263 µs per loop
66 625 loops, best of 3: 276 µs per loop
67 625 loops, best of 3: 288 µs per loop
68 625 loops, best of 3: 305 µs per loop
69 625 loops, best of 3: 318 µs per loop
```


So, there is an improvement for bigger matrices as well.


---

Comment by SimonKing created at 2012-03-11 08:53:50

The patchbot found no doctest errors, but complains that the old patch has introduced white space.

Hence, I have updated the patch and hope that it will be fine now.

Apply trac8096_speedup_matrix_parent.patch


---

Comment by davidloeffler created at 2012-03-11 09:24:32

Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)


---

Comment by davidloeffler created at 2012-03-11 09:24:32

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-03-11 12:14:52

Replying to [comment:44 davidloeffler]:
> Curiously the latest version doesn't seem to build on 5.0.beta7: the patch applies, but the modified cython file `matrix_window.pyx` won't build. (See patchbot logs; I also reproduced this separately by hand.)

Oops. Apparently, while removing white space, I have also removed something else. Sorry, I'll update it in a minute.


---

Comment by SimonKing created at 2012-03-11 12:18:35

Sorry that I did not try to build Sage again after manually editing the patch.

I have updated the patch, and now it does build. I leave tests to the patchbot...

Apply trac8096_speedup_matrix_parent.patch


---

Comment by SimonKing created at 2012-03-11 12:18:35

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-03-11 14:27:54

Replaces the previous patches, rebased rel sage-5.0.beta7


---

Attachment

Arrgh! There was another trailing whitespace in the patch!

It should now be fixed.

By the way: Am I entitled to review the patch, even though rebasing the two original patches has not been totally mechanic? I still think that Tom and Robert are the authors, so that I could be reviewer. Agreed?


---

Comment by SimonKing created at 2012-03-11 14:30:49

Patchbot...

Apply trac8096_speedup_matrix_parent.patch


---

Comment by davidloeffler created at 2012-03-11 14:40:17

I think reviewing patches you have rebased is allowed, as long as there's no change in functionality.


---

Comment by davidloeffler created at 2012-03-13 01:48:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-21 22:04:46

Resolution: fixed
