# Issue 4918: convert sage.matrix.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4918

Original creator: mhansen

Original creation time: 2009-01-01 22:53:12

Assignee: tba




---

Comment by mhansen created at 2009-01-02 03:01:47

Patch at http://sage.math.washington.edu/home/mhansen/trac_4918.patch


---

Attachment

## Files `matrix1.pyx`, `matrix_integer_dense.pyx` and `matrix_mod2_dense.pyx`

 * the doc of the stack method must keep the two line presentation, otherwise it's not understandable:

```
-        Return the augmented matrix self on top of other:
-           [ self  ]
-           [ other ]
-
```

Should not be replaced by

```
+        Return the augmented matrix self on top of other: [ self ] [ other
+        ]
```

Please use some kind of verbatim environment.

## File: matrix1.pyx
* in the augment method, the "|" should be kept

```
-        Return the augmented matrix of the form [self | other].
+        Return the augmented matrix of the form [self other].
```

 
* in block_sum it's crucial to keep the presentation:

```
-        [self |    0  ]
-        [  0  | other ]
```

is now

```
+        [self 0 ] [ 0 other ]
```


 * function _det_by_minors: missing > 

```
-        Does not handle degenerate cases, level MUST be >= 2
+        of self. Does not handle degenerate cases, level MUST be = 2
```




## File: matrix_modn_sparse.pyx

* Creation of a matrix: missing < :

```
-            parent -- a matrix space
-            entries -- * a Python list of triples (i,j,x), where 0 <= i < nrows,
-                         0 <= j < ncols, and x is coercible to an int.  The i,j
+           - a Python list of triples (i,j,x), where 0 = i nrows, 0 =
+             j ncols, and x is coercible to an int. The i,j entry of
```


## File: matrix_rational_dense.pyx

* function invert: missing <

```
-         * The n x n cases for n <= 2 are handcoded for speed. 
+           - The n x n cases for n = 2 are handcoded for speed.
```


* function _lift_crt_rr_with_lcm : missing <

```
-            Optimizations: When doing the rational_recon lift of a (mod m) 
-            first see if |a| < sqrt(m/2) in which case it lifts to 
-            an integer (often a=0 or 1). 
+        Optimizations: When doing the rational_recon lift of a (mod m)
+        first see if a sqrt(m/2) in which case it lifts to an integer
+        (often a=0 or 1).
```

and

```
-            If that fails, keep track of the lcm d of denominators found so far, 
-            and check to see if z = a*d lifts to an integer with |z| <= sqrt(m/2).
-            If so, no need to do rational recon.  This should be the case
-            for most a after a while, and should saves substantial time!
+        If that fails, keep track of the lcm d of denominators found so
+        far, and check to see if z = a\*d lifts to an integer with z =
+        sqrt(m/2). If so, no need to do rational recon. This should be the
+        case for most a after a while, and should saves substantial time!
```


## File: matrix_real_double_dense.pyx

* main doc : presentation must be kept

```
-    To solve a linear system Ax = b
-    where A = [[1,2]  and b = [5,6]
-             [3,4]] 
+    To solve a linear system Ax = b where A = [[1,2] and b = [5,6]
+    [3,4]]
```



---

Comment by mhansen created at 2009-02-24 19:01:23

These changes are in fixes.patch at #5330.


---

Comment by mhansen created at 2009-02-24 19:01:23

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-24 19:01:23

Changing assignee from tba to mhansen.


---

Comment by mabshoff created at 2009-02-24 19:04:15

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:04:15

Merged in Sage 3.4.alpha0.

Cheers,

Michael
