# Issue 4115: [with patch, not ready for review] Double coset problems

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-14 07:52:20

Assignee: rlm

Implements computations of properties which form double cosets. For example, if G is isomorphic to H, and m : G -> H is an isomorphism, then the set of all possible isomorphisms is the double coset Aut(H) m Aut(G).

This algorithm is pretty close to the canonical label algorithm, but it is a more efficient way to implement the isomorphism question. If the objects are not isomorphic, it will tend to discover this pretty quickly, via refinement invariants and examining the partition structure. If they are isomorphic, chances are this isomorphism will be discovered quickly and the algorithm will terminate at that moment.


---

Comment by wdj created at 2008-09-15 12:37:27

I know I'm missing something but could you tell me why this fails?


```
wdj`@`tinah:~/sagefiles/sage-3.1.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: dbl-coset
sage: hg_sage.apply("/home/wdj/sagefiles/trac_4115-double-cosets.patch")
cd "/home/wdj/sagefiles/sage-3.1.2.rc1/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc1/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc1/devel/sage" && hg import   "/home/wdj/sagefiles/trac_4115-double-cosets.patch"
applying /home/wdj/sagefiles/trac_4115-double-cosets.patch
patching file sage/groups/perm_gps/partn_ref/refinement_binary.pyx
Hunk #1 FAILED at 21
1 out of 19 hunks FAILED -- saving rejects to file sage/groups/perm_gps/partn_ref/refinement_binary.pyx.rej
unable to find 'sage/groups/perm_gps/partn_ref/refinement_matrices.pxd' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage/groups/perm_gps/partn_ref/refinement_matrices.pxd.rej
unable to find 'sage/groups/perm_gps/partn_ref/refinement_matrices.pyx' for patching
8 out of 8 hunks FAILED -- saving rejects to file sage/groups/perm_gps/partn_ref/refinement_matrices.pyx.rej
abort: patch failed to apply
```



---

Comment by mabshoff created at 2008-09-15 12:51:41

You need a more current release. rc4 will do fine, not sure about rc3 since some patches in that area went into rc4 IIRC:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc4/devel/sage$ patch -p1 --dry-run < ~/trac_4115-double-cosets.patch\?format\=raw 
patching file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pxd
patching file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx
patching file sage/groups/perm_gps/partn_ref/data_structures_pxd.pxi
patching file sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi
patching file sage/groups/perm_gps/partn_ref/double_coset.pxd
patching file sage/groups/perm_gps/partn_ref/double_coset.pyx
patching file sage/groups/perm_gps/partn_ref/refinement_binary.pxd
patching file sage/groups/perm_gps/partn_ref/refinement_binary.pyx
patching file sage/groups/perm_gps/partn_ref/refinement_graphs.pxd
patching file sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
patching file sage/groups/perm_gps/partn_ref/refinement_matrices.pxd
patching file sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
patching file setup.py
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-15 12:55:22

My guess is that once you apply #4097 to rc3 it will work with that release or even earlier ones.

Cheers,

Michael


---

Comment by wdj created at 2008-09-15 21:51:45

With this patch applied to 3.1.2.rc3, I got several failures including this one:


```
wdj`@`hera:~/sagefiles/sage-3.1.2.rc3$ ./sage -t  devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi
sage -t  devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc3/tmp/data_structures_pyx.py", line 7:
    sage: import sage.groups.perm_gps.partn_ref.data_structures
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        import sage.groups.perm_gps.partn_ref.data_structures###line 7:
    sage: import sage.groups.perm_gps.partn_ref.data_structures
    ImportError: No module named data_structures

```

This seems fairly serious so I'm guessing I should move one to rc4 instead. Sorry for the delay. I tried soing something witth this at work but my machine there is relatively slow.


---

Comment by rlm created at 2008-09-16 00:48:36

Sorry about that, `data_structures` was a module that I ended up not including, but since its ghost was still loitering around in build, tests passed for me...


---

Comment by wdj created at 2008-09-16 02:02:27

Okay. I applied #4131 (using hg_scripts.apply) and #4115 to 3.1.2.rc4 and am running tests now. This looks like an extremely interesting patch so far!


---

Comment by wdj created at 2008-09-16 09:51:01

I still get this data_structures error after applying #4131, #4115 and sage -b and sage -testall:


```
The following tests failed:


        sage -t  devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi
        sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_binary.pyx
Total time for all tests: 5376.0 seconds
Please see /home/wdj/sagefiles/sage-3.1.2.rc4/tmp/test.log for the complete log from this test.
```


```
wdj`@`hera:~/sagefiles/sage-3.1.2.rc4$ ./sage -t devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi
sage -t  devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc4/tmp/data_structures_pyx.py", line 7:
    sage: import sage.groups.perm_gps.partn_ref.data_structures
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc4/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        import sage.groups.perm_gps.partn_ref.data_structures###line 7:
    sage: import sage.groups.perm_gps.partn_ref.data_structures
    ImportError: No module named data_structures
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.1.2.rc4/tmp/.doctest_data_structures_pyx.py
         [2.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/groups/perm_gps/partn_ref/data_structures_pyx.pxi
Total time for all tests: 2.4 seconds
```

I guess one could argue that somehow the patch includes an "add" which was not
needed and so this error is more-or-less spurious. However, this is more serious:


```
sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import NonlinearBinaryCodeStruct
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/wdj/sagefiles/sage-3.1.2.rc4/<ipython console> in <module>()

ImportError: cannot import name NonlinearBinaryCodeStruct
```


This suggests that a new patch is needed? Or am I doing something stupid again?


---

Comment by rlm created at 2008-09-17 02:00:38

Replying to [comment:8 wdj]:
> sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import NonlinearBinaryCodeStruct

This line does not show up at all in the patch, as-is right now. You should get the latest version of the patch and try again.


---

Attachment


---

Comment by wdj created at 2008-09-17 23:13:11

A couple of cool examples:-)


```
sage: P.<x> = PolynomialRing(GF(2),"x")
sage: g = x^3+x+1
sage: C1 = CyclicCodeFromGeneratingPolynomial(7,g); C1
Linear code of length 7, dimension 4 over Finite Field of size 2
sage: CW1 = matrix(GF(2),C1.list())
sage: C2 = HammingCode(3,GF(2)); C2
Linear code of length 7, dimension 4 over Finite Field of size 2
sage: CW2 = matrix(GF(2),C2.list())
sage: B = NonlinearBinaryCodeStruct(CW1)
sage: C = NonlinearBinaryCodeStruct(CW2)
sage: B.is_isomorphic(C)
[0, 1, 2, 6, 5, 3, 4]
```



```
sage: C1 = ExtendedQuadraticResidueCode(23,GF(2)); C1
Linear code of length 24, dimension 12 over Finite Field of size 2
sage: C2 = ExtendedBinaryGolayCode(); C2
Linear code of length 24, dimension 12 over Finite Field of size 2
sage: C1 == C2
False
sage: time CW1 = matrix(GF(2),C1.list())
CPU times: user 32.98 s, sys: 0.03 s, total: 33.01 s
Wall time: 33.12 s
sage: time CW2 = matrix(GF(2),C2.list())
CPU times: user 31.93 s, sys: 0.03 s, total: 31.95 s
Wall time: 32.05 s
sage: time B = NonlinearBinaryCodeStruct(CW1)
CPU times: user 0.19 s, sys: 0.00 s, total: 0.19 s
Wall time: 0.19 s
sage: time C = NonlinearBinaryCodeStruct(CW2)
CPU times: user 0.21 s, sys: 0.00 s, total: 0.21 s
Wall time: 0.21 s
sage: time B.is_isomorphic(C)
CPU times: user 0.22 s, sys: 0.00 s, total: 0.22 s
Wall time: 0.22 s

[0,
 1,
 2,
 3,
 4,
 5,
 14,
 19,
 23,
 21,
 16,
 15,
 18,
 17,
 22,
 7,
 11,
 12,
 8,
 6,
 10,
 13,
 9,
 20]
sage:                   
```

This is a 24x4096 matrix!

So far so good. I'm going to try to find some more complicated examples:-)


---

Comment by wdj created at 2008-09-18 12:32:42

I'm confused by this output:

Put

```
def test():
 G = SymmetricGroup(20)
 g = G("(11,12,13,14,15,16,17)")
 for i in range(10):
   C1 = RandomLinearCode(20,10,GF(2))
   C2 = C1.permuted_code(g)
   CW1 = matrix(GF(2),C1.list())
   CW2 = matrix(GF(2),C2.list())
   B = NonlinearBinaryCodeStruct(CW1)
   C = NonlinearBinaryCodeStruct(CW2)
   ans = B.is_isomorphic(C)
   L = [j+1 for j in ans]
   h = G(L)
   G1 = C1.automorphism_group_binary_code()
   print i, g, h, h*g^(-1) in G1
```

called test.sage or something and attach it.
It seems to me it should always return True.

```
sage: time test()
0 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
1 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
2 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
3 (11,12,13,14,15,16,17) (11,12,13,14,15,16) True
4 (11,12,13,14,15,16,17) (9,12,13,14,15,16,17) False
5 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
6 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
7 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
8 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
9 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
CPU times: user 88.99 s, sys: 0.10 s, total: 89.09 s
Wall time: 90.93 s
```

If you change the script to

```
def test():
 G = SymmetricGroup(20)
 g = G("(11,12,13,14,15,16,17)")
 for i in range(10):
   C1 = RandomLinearCode(20,10,GF(2))
   C2 = C1.permuted_code(g)
   CW1 = matrix(GF(2),C1.list())
   CW2 = matrix(GF(2),C2.list())
   B = NonlinearBinaryCodeStruct(CW1)
   C = NonlinearBinaryCodeStruct(CW2)
   ans = B.is_isomorphic(C)
   L = [j+1 for j in ans]
   h = G(L)
   G1 = C1.automorphism_group_binary_code()
   print i, g, h, h^(-1)*g in G1 
```

you get 

```
sage: time test()
0 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
1 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
2 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
3 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
4 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
5 (11,12,13,14,15,16,17) (8,15,16,17,11)(12,13,14) False
6 (11,12,13,14,15,16,17) (10,12,13,14,15,16,17) False
7 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
8 (11,12,13,14,15,16,17) (9,12,13,14,15,16,17) False
9 (11,12,13,14,15,16,17) (11,12,13,14,15,16,17) True
CPU times: user 92.33 s, sys: 0.11 s, total: 92.45 s
Wall time: 92.92 s
```

Again funny.

It should be g,h:C1->C2, so h^(-1)*g in G1 should be true
and h*g^(-1) in G1 should be false.

I'm probably misinterpreting something in the docstrings
(and probably and still too sleepy to think straight:-) 
but something seems confusing to me here.

Can someone see the error here?


---

Comment by rlm created at 2008-09-18 15:47:07

First of all, you should be using a `LinearBinaryCodeStruct` for this, since these are linear binary codes, and the code will run much faster. The `list` function of linear codes seemed pretty slow, so I posted something at #4145.

Second, after playing with this for a while, I realized that GAP permutations act on the right, which reverses the familiar multiplication:

```
sage: G = SymmetricGroup(20)
sage: g = G("(11,12,13,14,15,16,17)")
sage: h = G("(11,12)(13,14,15,16,17)")
sage: h^(-1)
(11,12)(13,17,16,15,14)
sage: (h^(-1))*g
(11,13)
sage: g*(h^(-1))
(12,17)
```


So I think the first version of your function was the correct one. With the patches here and at #4145 applied, and with `test` defined as below, I get nothing but `True`s for 100 trials. Without #4145, I frequently get `False`'s. So perhaps #4145 is actually a bug fix!

```
def test(n):
    G = SymmetricGroup(20)
    g = G("(11,12,13,14,15,16,17)")
    for i in range(n):
        C1 = RandomLinearCode(20,10,GF(2))
        C2 = C1.permuted_code(g)
        CW1 = matrix(GF(2),C1.list())
        CW2 = matrix(GF(2),C2.list())
        B = NonlinearBinaryCodeStruct(CW1)
        C = NonlinearBinaryCodeStruct(CW2)
        ans = B.is_isomorphic(C)
        L = [j+1 for j in ans]
        h = G(L)
        G1 = C1.automorphism_group_binary_code()
        print i, g, h, g*(h^(-1)), g*(h^(-1)) in G1
        print G1
```



---

Comment by wdj created at 2008-09-18 17:11:07

I agree and also just gave #4145 a positive review, so now I give this a positive review too.

Michael: If you apply this please also apply #4145 at the same time. They need to go together.

Wow, this is a cool patch! There are a *ton* of improvements to the linear codes modules which will result from this....


---

Comment by mabshoff created at 2008-09-19 00:48:18

Merged in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-19 00:48:18

Resolution: fixed
