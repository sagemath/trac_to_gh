# Issue 5576: [with patch, needs review] MPolynomialSystem cleanup

Issue created by migration from https://trac.sagemath.org/ticket/5576

Original creator: malb

Original creation time: 2009-03-20 13:39:50

Assignee: malb

CC:  mhansen

Keywords: crypto

** clean up of ReST in `mq.MPolynomialSystem`
 * improved documentation of `mq.MPolynomialSystem`
 * deprecated `mq.MPolynomialSystem_gf2e.change_ring()`
 * added `mq.MPolynomialSystem_gf2e.weil_restriction()`
 * added `mq.MPolynomialSystem.connected_components()`
 * added `mq.MPolynomialSystem.connection_graph()`
 * added `mq.MPolynomialSystem_gf2.eliminate_linear_variables()`


---

Comment by malb created at 2009-03-20 13:41:17

The attached patch depends on #5569


---

Comment by mvngu created at 2009-03-27 06:13:47

First I applied the patch at #5569 against Sage 3.4, then I applied the patch on this ticket. Doctesting gave me timed out errors:

```
[mvngu@sage sage-3.4]$ sage -t -long devel/sage-5576/sage/crypto/mq/
sage -t -long "devel/sage-5576/sage/crypto/mq/sbox.py"      
         [11.3 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/mpolynomialsystemgenerator.py"
         [7.6 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.5 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/mpolynomialsystem.py"
         [24.4 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5576/sage/crypto/mq/sr.py"
Total time for all tests: 1843.9 seconds
```



---

Comment by malb created at 2009-03-27 11:04:05

I can reproduce your problem and I'll look into it. Thanks.


---

Comment by malb created at 2009-03-27 11:11:04

I fixed the underlying issue and will raise a question on [sage-devel] how to deal with the API change that caused it.


---

Comment by mvngu created at 2009-05-08 01:16:55

With the latest stable version sage-3.4.2, i.e. the "post-final" 3.4.2 version, I get the following hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 5576
sage: hg_sage.apply("/home/mvngu/patch/5576/mpolynomialsystem_rest.patch")
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/patch/5576/mpolynomialsystem_rest.patch"
applying /home/mvngu/patch/5576/mpolynomialsystem_rest.patch
patching file sage/crypto/mq/mpolynomialsystem.py
Hunk #7 FAILED at 262
Hunk #8 FAILED at 277
Hunk #9 FAILED at 314
Hunk #22 FAILED at 652
4 out of 51 hunks FAILED -- saving rejects to file sage/crypto/mq/mpolynomialsystem.py.rej
abort: patch failed to apply
```



---

Comment by malb created at 2009-05-12 00:07:18

I rebased the patch.


---

Attachment


---

Comment by malb created at 2009-05-12 00:35:09


```
[01:15] <mhansen> malb: You need to fix the REFERENCES section in eliminate_linear_variables([01:16] <malb> what about it?
[01:18] <mhansen> The text after the .. should all be aligned.
[01:18] <mhansen> (on the left.
```


fixed in updated patch.


---

Comment by burcin created at 2009-05-12 14:33:09

Patch looks good, doctests pass.


---

Comment by mabshoff created at 2009-05-12 17:15:31

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 17:15:31

Resolution: fixed
