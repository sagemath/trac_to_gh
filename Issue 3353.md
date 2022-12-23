# Issue 3353: bug in MatrixGroup iterator

Issue created by migration from https://trac.sagemath.org/ticket/3353

Original creator: wdj

Original creation time: 2008-06-03 01:49:52

Assignee: joyner


Here's a problem with the iterator for GL(2,p):


```
sage: p = 5
sage: G = GL(2,p)
sage: z = iter(G)
sage: z
<iterator object at 0x3c737d0>
sage: z.next()
[0 1]
[1 0]
sage: z.next()
[0 1]
[1 1]
```

It takes quite a bit of time to do each .next().

This is a serious issue for someone trying to compute orbits of matrix group actions.


---

Comment by mabshoff created at 2008-06-03 02:10:02

This because we are calling GAP via pexpect. Notice specifically

```
        1    0.009    0.009   35.754   35.754 matrix_group.py:390(list)
```

In total:

```

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   104450    5.372    0.000   17.593    0.000 pexpect.py:815(compile_pattern_list)
   104450    5.350    0.000   10.881    0.000 pexpect.py:914(expect_list)
  1029995    4.595    0.000    6.616    0.000 re.py:227(_compile)
  1029995    3.899    0.000   10.515    0.000 re.py:186(compile)
  1123001    2.472    0.000    2.472    0.000 {built-in method search}
  1029995    2.021    0.000    2.021    0.000 {method 'get' of 'dict' objects}
  1103065    1.829    0.000    1.829    0.000 {method 'append' of 'list' objects}
    28498    1.430    0.000    1.430    0.000 {posix.write}
   545128    0.942    0.000    0.942    0.000 {built-in method start}
    14249    0.819    0.000   32.053    0.002 gap.py:379(_execute_line)
   104450    0.662    0.000   29.136    0.000 pexpect.py:855(expect)
    27816    0.446    0.000    1.428    0.000 pexpect.py:498(read_nonblocking)
    14249    0.409    0.000   32.808    0.002 gap.py:468(_eval_line)
   208900    0.370    0.000    0.370    0.000 {built-in method end}
   143987    0.318    0.000    0.318    0.000 {method 'index' of 'list' objects}
     8006    0.261    0.000   18.662    0.002 expect.py:888(eval)
  960/480    0.250    0.000    5.572    0.012 {method '_gap_' of 'sage.structure.sage_object.SageObject' objects}
    27816    0.239    0.000    0.239    0.000 {select.select}
    27816    0.229    0.000    0.229    0.000 {posix.read}
    27816    0.218    0.000    0.409    0.000 pexpect.py:739(isalive)
125845/125808    0.207    0.000    0.216    0.000 {len}
    28498    0.206    0.000    1.745    0.000 pexpect.py:656(send)
    55632    0.191    0.000    0.191    0.000 {posix.waitpid}
     6243    0.176    0.000    0.303    0.000 expect.py:1300(__del__)
     8006    0.159    0.000   18.901    0.002 gap.py:294(eval)
    11040    0.158    0.000   11.676    0.001 {sage.rings.integer_mod.IntegerMod}
    14886    0.137    0.000    0.167    0.000 expect.py:1277(_check_valid)
    60190    0.123    0.000    0.123    0.000 {isinstance}
    28498    0.109    0.000    0.109    0.000 {time.sleep}
     6243    0.107    0.000   14.969    0.002 expect.py:1199(__init__)
    14249    0.100    0.000    1.845    0.000 pexpect.py:668(sendline)
     1920    0.099    0.000    8.714    0.005 gap.py:739(gfq_gap_to_sage)
     4802    0.096    0.000   10.702    0.002 expect.py:1326(__repr__)
7203/6243    0.094    0.000   19.651    0.003 expect.py:930(__call__)
11040/7520    0.089    0.000   20.444    0.003 integer_mod_ring.py:574(__call__)
     1600    0.080    0.000    0.083    0.000 {eval}
      480    0.077    0.000   29.161    0.061 gap.py:677(_matrix_)
    40827    0.074    0.000    0.074    0.000 {method 'join' of 'str' objects}
     1440    0.071    0.000    0.137    0.000 matrix_space.py:914(matrix)
    34218    0.067    0.000    0.067    0.000 {method 'find' of 'str' objects}
     3360    0.066    0.000    6.191    0.002 gap.py:613(__getitem__)
    23855    0.058    0.000    0.058    0.000 {method 'replace' of 'str' objects}
     8006    0.056    0.000    0.083    0.000 expect.py:123(__enter__)
     2403    0.055    0.000    8.096    0.003 expect.py:1101(function_call)
     6243    0.054    0.000   14.732    0.002 gap.py:341(set)
    31216    0.052    0.000    0.052    0.000 {method 'parent' of 'sage.structure.element.Element' objects}
    27816    0.051    0.000    0.051    0.000 {method 'lower' of 'str' objects}
     6243    0.049    0.000   14.840    0.002 expect.py:1089(_create)
     6243    0.049    0.000    0.059    0.000 gap.py:225(_next_var_name)
 1440/960    0.046    0.000    0.203    0.000 matrix_space.py:243(__call__)
     1920    0.043    0.000    4.339    0.002 expect.py:1396(_integer_)
     4802    0.043    0.000   10.755    0.002 gap.py:630(__repr__)
     8006    0.038    0.000    0.051    0.000 expect.py:127(__exit__)
    10407    0.034    0.000    0.034    0.000 gap.py:368(__getattr__)
     7205    0.032    0.000    0.040    0.000 gap.py:608(__getattr__)
     4802    0.031    0.000   10.535    0.002 gap.py:352(get)
     2403    0.029    0.000    8.129    0.003 expect.py:1181(__call__)
     5763    0.027    0.000   14.089    0.002 expect.py:1012(new)
    14249    0.025    0.000    0.025    0.000 gap.py:222(_quit_string)
    14088    0.023    0.000    0.023    0.000 {ord}
     8006    0.023    0.000    0.023    0.000 {method 'split' of 'str' objects}
     4323    0.019    0.000    0.027    0.000 expect.py:1075(clear)
      480    0.016    0.000    5.709    0.012 matrix_group_element.py:75(__init__)
     2882    0.015    0.000    6.466    0.002 {repr}
     7044    0.015    0.000    0.015    0.000 {chr}
     8006    0.015    0.000    0.015    0.000 {method 'rstrip' of 'str' objects}
     8006    0.014    0.000    0.014    0.000 {method 'strip' of 'str' objects}
     7203    0.014    0.000    0.014    0.000 gap.py:547(_object_class)
     8006    0.013    0.000    0.013    0.000 {gc.enable}
     8006    0.013    0.000    0.013    0.000 {gc.isenabled}
  960/480    0.013    0.000    5.580    0.012 expect.py:963(_coerce_from_special_method)
     8006    0.013    0.000    0.013    0.000 {gc.disable}
     4803    0.013    0.000    0.013    0.000 {hasattr}
     2401    0.012    0.000    0.017    0.000 expect.py:274(_repr_)
      480    0.011    0.000    0.027    0.000 matrix_space.py:105(MatrixSpace)
      480    0.010    0.000    0.013    0.000 {method 'has_key' of 'dict' objects}
     3840    0.010    0.000    0.010    0.000 expect.py:287(name)
     3360    0.010    0.000    0.010    0.000 finite_field_prime_modn.py:121(characteristic)
     3844    0.010    0.000    0.010    0.000 {range}
        1    0.009    0.009   35.754   35.754 matrix_group.py:390(list)
      480    0.008    0.000    0.011    0.000 {method 'copy' of 'sage.matrix.matrix0.Matrix' objects}
     1920    0.008    0.000    0.012    0.000 gap.py:736(is_GapElement)
     2887    0.008    0.000    0.008    0.000 expect.py:1404(name)
     2403    0.008    0.000    0.008    0.000 expect.py:1174(__init__)
     1600    0.006    0.000    0.006    0.000 finite_field_prime_modn.py:187(order)
     3200    0.006    0.000    0.006    0.000 {method 'index' of 'str' objects}
     1440    0.006    0.000    0.009    0.000 matrix_group_element.py:60(is_MatrixGroupElement)
      962    0.006    0.000    2.176    0.002 expect.py:1377(__int__)
     2401    0.005    0.000    0.005    0.000 {method 'capitalize' of 'str' objects}
     2560    0.005    0.000    0.005    0.000 finite_field_prime_modn.py:238(degree)
     1440    0.004    0.000    0.004    0.000 matrix_space.py:1001(nrows)
     1440    0.003    0.000    0.003    0.000 matrix_space.py:990(ncols)
     1440    0.003    0.000    0.003    0.000 {sage.matrix.matrix.is_Matrix}
      480    0.003    0.000    0.003    0.000 matrix_group.py:215(matrix_space)
      481    0.003    0.000    0.861    0.002 expect.py:1224(__iter__)
      480    0.002    0.000    0.002    0.000 {sum}
      480    0.002    0.000    0.002    0.000 {sage.modules.free_module_element.is_FreeModuleElement}
      480    0.001    0.000    0.001    0.000 {sage.rings.ring.is_Ring}
      480    0.001    0.000    0.001    0.000 {method 'is_immutable' of 'sage.matrix.matrix0.Matrix' objects}
        1    0.000    0.000    0.000    0.000 matrix_group.py:170(_gap_)
        2    0.000    0.000    0.020    0.010 gap.py:639(__len__)
        1    0.000    0.000    0.000    0.000 matrix_group.py:280(is_finite)
        1    0.000    0.000    0.000    0.000 matrix_group.py:263(base_ring)
        1    0.000    0.000    0.000    0.000 {method 'is_finite' of 'sage.rings.ring.FiniteField' objects}
        1    0.000    0.000    0.000    0.000 matrix_group.py:245(field_of_definition)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-06-03 02:33:12

Oh, while I am at it:

 * without prun z.next() costs 12 seconds
 * the resulting list created by matrix_group.py:390 is *not* even cached, i.e. each next() is equally expensive.

Cheers,

Michael


---

Comment by was created at 2008-06-03 02:46:54

First observation:  Every single time you call .next(), there are about a 1000 calls
via pexpect to gap.   Those calls create a list of the 474 elements of the group G.

The following works a little better:

```
sage: G = GL(2,p)
sage: time v = iter(G.list())
CPU times: user 7.95 s, sys: 2.95 s, total: 10.91 s
Wall time: 11.20 s
sage: time v.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
[0 1]
[1 0]
sage: time v.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
[0 1]
[1 1]
sage: time v.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
[0 1]
[1 2]
```



---

Comment by was created at 2008-06-03 04:15:23

I made some changes to the "programming model" to be much better about taking
advantage of how pexpect works, then fixed a bunch of major little efficiency
flaws in some code.  Now things are over 100 times faster:

```
sage: p = 5
sage: G = GL(2,p)
sage: z = iter(G)
sage: z
<iterator object at 0x8113910>
sage: time z.next()
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.37 s

[0 1]
[1 0]
sage: time z.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s

[0 1]
[1 1]
sage: time z.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s

[0 1]
[1 2]
sage: time z.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s

[0 1]
[1 4]
sage: time z.next()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s

[0 1]
[1 3]
```


You will also find that arithmetic is vastly faster.

Before:


```
sage: a = z.next()
sage: timeit('a*a')
125 loops, best of 3: 3.09 ms per loop
```


After

```
sage: a = z.next()
sage: timeit('a*a')
625 loops, best of 3: 80.6 µs per loop
```


That's about 40 times faster!


---

Attachment


---

Comment by robertwb created at 2008-06-03 05:40:52

For the most part the patch looks good, and cleans up a lot of stuff as well as being way faster. Something needs to be handled more carefully with the string substitution though: 


```
sage: list(GL(3,3))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "parent_gens.pyx", line 218, in sage.structure.parent_gens.ParentWithGens.__len__ (sage/structure/parent_gens.c:1759)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 443, in list
    v = eval(s, {'a':a, 'b':b})
  File "<string>", line 757, in <module>
<type 'exceptions.NameError'>: name 'Z' is not defined
```



---

Comment by was created at 2008-06-03 05:49:53

this fixes the one bug spotted by the referee


---

Attachment


---

Comment by robertwb created at 2008-06-03 06:31:48

That fixes it for me, and all else works well.


---

Comment by mabshoff created at 2008-06-04 20:36:19

Resolution: fixed


---

Comment by mabshoff created at 2008-06-04 20:36:19

Merged both patches in Sage 3.0.3.alpha1


---

Comment by rlm created at 2008-06-11 16:20:53

I know the ticket is closed, but I'd like to add a very positive review to this ticket. A computation I was trying this morning to check a small conjecture was just not going to happen. After applying the patch, I know that my conjecture was right!
