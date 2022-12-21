# Issue 4502: numerical noise in matrix_double_dense on intel mac os X 10.5: inverting a singular matrix

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-11-12 17:57:19

Assignee: somebody

Keywords: numerical noise, matrix

(This has only been reported on intel macs running 10.4 or 10.5.)

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/fae59a9a9a53b8c0):


```
sage: A = matrix(RDF,3,range(1,10));A

[1.0 2.0 3.0]
[4.0 5.0 6.0]
[7.0 8.0 9.0]
sage: A.determinant()
0.0
sage: -A

[-1.0 -2.0 -3.0]
[-4.0 -5.0 -6.0]
[-7.0 -8.0 -9.0]
sage: b = A.numpy(); b

array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.],
       [ 7.,  8.,  9.]])
sage: import scipy
sage: import scipy.linalg
sage: scipy.linalg.det(b)
0.0
sage: scipy.linalg.inv(b)

array([[ -4.50359963e+15,   9.00719925e+15,  -4.50359963e+15],
       [  9.00719925e+15,  -1.80143985e+16,   9.00719925e+15],
       [ -4.50359963e+15,   9.00719925e+15,  -4.50359963e+15]])
```


This leads to a doctest failure for `matrix_double_dense.py`.


---

Comment by jason created at 2008-11-14 05:50:30

I think the easiest way to avoid this (until we update to the latest scipy and test this again) is to check the scipy.linalg.det explicitly before attempting doing an inverse.  If that determinant is zero (or close enough to it), then return the same error as the doctest returns (i.e., some scipy error).


---

Comment by GeorgSWeber created at 2008-11-16 09:49:51

patch against Sage 3.2.rc1


---

Attachment

Well, this makes the doctest failure go away on my Intel Mac. (I followed the proposal from Jason.)

But please someone have a look if it is worth the price paid.


---

Comment by jhpalmieri created at 2008-11-16 16:57:59

It fixes the doctest failure for me, too.  One or two questions:

Could the error message 

```
raise ValueError, "self must be square" 
```

be changed to something like "matrix must be square"?  Actually, why is this here?  I get an error message about non-square matrices (I think produced by scipy) before applying the patch.


---

Comment by mhampton created at 2008-11-18 16:46:58

I don't think this fix is worth the performance penalty, which for me looks like about a 25% hit.  The determinant is not a great measure of singularity.  I think it would be better to just change the doctest.


---

Attachment

doctest changed in trac_4502.patch.  Apply instead of previous patch.


---

Comment by mabshoff created at 2008-11-18 17:01:47

Positive review on trac_4502.patch

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-18 17:44:41

Sorry, I spoke too soon. This needs work since it does not apply as is.

Cheers,

Michael


---

Attachment

patch against Sage 3.2.rc1; apply only this one


---

Comment by GeorgSWeber created at 2008-11-18 21:26:40

Just changes the failing doctest (and only that single one) to be #random, and should apply cleanly against Sage 3.2.rc1. Now on my box, the doctest for this file passes.


---

Comment by mabshoff created at 2008-11-18 21:28:54

`#random` does not fix it since the exception still gets thrown. I tried it, so that is how I found out. In IRC we concluded to nuke the doctests for now and deal with that once SciPy 0.7 is out.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-18 21:43:00

Hi John,
>Could the error message

```
raise ValueError, "self must be square" 
```

>be changed to something like "matrix must be square"? Actually, why is this here? I get an error message about non-square matrices (I think produced by scipy) before applying the patch.

This test and error message were copied verbatim from lines 759/760 of that same file (function "def determinant(self)"). In my first patch, I introduced the additional calculation of the determinant in the function for inverting the matrix, and I wanted to make sure that all necessary sanity checks were in place.

Would it be possible for you to provide not only a concrete wording, but a new trac ticket with patch, if you like some other wording better for that error message? I'll review it then. (Maybe just removing this test from the .pyx file and relying on scipy producing the error message for us also for determinants on non-square matrices is an option here.)

Cheers,

gsw


---

Comment by GeorgSWeber created at 2008-11-18 21:48:49

>#random does not fix it since the exception still gets thrown. I tried it, so that is how I found out. 
Strange. So does this mean the doctest passing as follows:

```
susanne-webers-computer:~/Public/sage/sage-3.2.rc1/devel/sage georgweber$ sage -t sage/matrix/matrix_double_dense.pyx
sage -t  devel/sage-test2/sage/matrix/matrix_double_dense.pyx
         [4.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.2 seconds
```

is not enough here? I'm a bit puzzled, which exception exactly gets "thrown nevertheless" and when? I'm fine with nuking the doctest and postponing the issue till scipy 0.7 is there and included, I ask just out of curiosity.


---

Comment by mabshoff created at 2008-11-18 21:52:42

With

```
diff -r 50c6651a1286 sage/matrix/matrix_double_dense.pyx
--- a/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 08:58:27 2008 -0800
+++ b/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 13:49:26 2008 -0800
`@``@` -441,7 +441,7 `@``@`
             
             sage: A.determinant() < 10e-12
             True
-            sage: ~A
+            sage: ~A # random
             Traceback (most recent call last):
             ...
             LinAlgError: singular matrix
```

I get

```
sage -t  devel/sage/sage/matrix/matrix_double_dense.pyx     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc2/devel/sage/sage/matrix/matrix_double_dense.pyx", line 444:
    sage: print "ignore this";  ~A # random
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[10]>", line 1, in <module>
        print "ignore this";  ~A # random###line 444:
    sage: print "ignore this";  ~A # random
      File "matrix_double_dense.pyx", line 460, in sage.matrix.matrix_double_dense.Matrix_double_dense.__invert__ (sage/matrix/matrix_double_dense.c:3878)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/lib/python2.5/site-packages/scipy/linalg/basic.py", line 306, in inv
        if info>0: raise LinAlgError, "singular matrix"
    LinAlgError: singular matrix
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc2/tmp/.doctest_matrix_double_dense.py
         [2.4 s]
exit code: 1024
```



---

Comment by GeorgSWeber created at 2008-11-18 21:57:36

Ahhh, sorry for the noise --- the exception does not fly on my box because my box believes the matrix would be invertible and provides an inverse matrix --- but on other computers the matrix is not invertible and there, the exception comes up.

Would that not be an issue to enhance the "#random" pragma then?

More precisely: Allowing on certain boxes the calculation to finish (but throw away the result), and on other boxes having an exception (but again throwing the outcome)?

Just point out to me the respective parts of the IRC conversation if all that info is in there ... and if you find the time and have patience to do so ... ;-)


---

Comment by mabshoff created at 2008-11-18 22:00:55

The issue is the following:

```
[10:34am] wstein|afk: mabshoff -- all that #random does is the following.
[10:35am] wstein|afk: sage: foo # random
[10:35am] wstein|afk: gets replaced by
[10:35am] wstein|afk: sage: _ = foo
[10:35am] wstein|afk: That's it.
[10:35am] mabshoff: mhh
[10:35am] wstein|afk: So it won't work at all with exceptions.
[10:35am] wstein|afk: Better might be:
[10:35am] wstein|afk: sage: foo # random
[10:35am] wstein|afk: gets replaced by
[10:35am] wstein|afk: sage: foo
[10:35am] wstein|afk: ...
[10:35am] wstein|afk: If that worked.
[10:35am] wstein|afk: I didn't know about ... when I wrote # random.
```

The goal now is to get 3.2 out and the easiest way to do this is to nuke the affected doctests and then deal with `#random` properly in 3.2.1.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-18 22:17:05

Thanks a lot!!!


---

Attachment

apply only this one (doctest just nuked)


---

Comment by GeorgSWeber created at 2008-11-18 22:19:15

Is it that what you mean by "nuke"ing?


---

Comment by mabshoff created at 2008-11-18 22:26:01

Yes, but two things:

 * a comment would be nice that the issue needs to be fixed with a reference to the ticket
 * The other test right before, i.e. "sage: A.inverse().det()" also needs to be commented out

Once the above two happen with a new patch I will give this a positive review.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-19 07:33:24

OK, no problem. (Except for the time it will take --- another 12 hours or so till I am back home.)


---

Attachment

addressing the reviewers wishes (hopefully)


---

Comment by mabshoff created at 2008-11-19 19:43:55

Positive review for 4502-next_try.3.patch. Thanks.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-19 19:44:24

Resolution: fixed


---

Comment by mabshoff created at 2008-11-19 19:44:24

Merged in Sage 3.2.rc2
