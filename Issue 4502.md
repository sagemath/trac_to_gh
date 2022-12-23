# Issue 4502: numerical noise in matrix_double_dense on intel mac os X 10.5: inverting a singular matrix

archive/issues_004502.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: numerical noise, matrix\n\n(This has only been reported on intel macs running 10.4 or 10.5.)\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/fae59a9a9a53b8c0):\n\n\n```\nsage: A = matrix(RDF,3,range(1,10));A\n\n[1.0 2.0 3.0]\n[4.0 5.0 6.0]\n[7.0 8.0 9.0]\nsage: A.determinant()\n0.0\nsage: -A\n\n[-1.0 -2.0 -3.0]\n[-4.0 -5.0 -6.0]\n[-7.0 -8.0 -9.0]\nsage: b = A.numpy(); b\n\narray([[ 1.,  2.,  3.],\n       [ 4.,  5.,  6.],\n       [ 7.,  8.,  9.]])\nsage: import scipy\nsage: import scipy.linalg\nsage: scipy.linalg.det(b)\n0.0\nsage: scipy.linalg.inv(b)\n\narray([[ -4.50359963e+15,   9.00719925e+15,  -4.50359963e+15],\n       [  9.00719925e+15,  -1.80143985e+16,   9.00719925e+15],\n       [ -4.50359963e+15,   9.00719925e+15,  -4.50359963e+15]])\n```\n\n\nThis leads to a doctest failure for `matrix_double_dense.py`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4502\n\n",
    "created_at": "2008-11-12T17:57:19Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "numerical noise in matrix_double_dense on intel mac os X 10.5: inverting a singular matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4502",
    "user": "jhpalmieri"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/4502





---

archive/issue_comments_033343.json:
```json
{
    "body": "I think the easiest way to avoid this (until we update to the latest scipy and test this again) is to check the scipy.linalg.det explicitly before attempting doing an inverse.  If that determinant is zero (or close enough to it), then return the same error as the doctest returns (i.e., some scipy error).",
    "created_at": "2008-11-14T05:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33343",
    "user": "jason"
}
```

I think the easiest way to avoid this (until we update to the latest scipy and test this again) is to check the scipy.linalg.det explicitly before attempting doing an inverse.  If that determinant is zero (or close enough to it), then return the same error as the doctest returns (i.e., some scipy error).



---

archive/issue_comments_033344.json:
```json
{
    "body": "patch against Sage 3.2.rc1",
    "created_at": "2008-11-16T09:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33344",
    "user": "GeorgSWeber"
}
```

patch against Sage 3.2.rc1



---

archive/issue_comments_033345.json:
```json
{
    "body": "Attachment\n\nWell, this makes the doctest failure go away on my Intel Mac. (I followed the proposal from Jason.)\n\nBut please someone have a look if it is worth the price paid.",
    "created_at": "2008-11-16T09:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33345",
    "user": "GeorgSWeber"
}
```

Attachment

Well, this makes the doctest failure go away on my Intel Mac. (I followed the proposal from Jason.)

But please someone have a look if it is worth the price paid.



---

archive/issue_comments_033346.json:
```json
{
    "body": "It fixes the doctest failure for me, too.  One or two questions:\n\nCould the error message \n\n```\nraise ValueError, \"self must be square\" \n```\n\nbe changed to something like \"matrix must be square\"?  Actually, why is this here?  I get an error message about non-square matrices (I think produced by scipy) before applying the patch.",
    "created_at": "2008-11-16T16:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33346",
    "user": "jhpalmieri"
}
```

It fixes the doctest failure for me, too.  One or two questions:

Could the error message 

```
raise ValueError, "self must be square" 
```

be changed to something like "matrix must be square"?  Actually, why is this here?  I get an error message about non-square matrices (I think produced by scipy) before applying the patch.



---

archive/issue_comments_033347.json:
```json
{
    "body": "I don't think this fix is worth the performance penalty, which for me looks like about a 25% hit.  The determinant is not a great measure of singularity.  I think it would be better to just change the doctest.",
    "created_at": "2008-11-18T16:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33347",
    "user": "mhampton"
}
```

I don't think this fix is worth the performance penalty, which for me looks like about a 25% hit.  The determinant is not a great measure of singularity.  I think it would be better to just change the doctest.



---

archive/issue_comments_033348.json:
```json
{
    "body": "Attachment\n\ndoctest changed in trac_4502.patch.  Apply instead of previous patch.",
    "created_at": "2008-11-18T16:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33348",
    "user": "jason"
}
```

Attachment

doctest changed in trac_4502.patch.  Apply instead of previous patch.



---

archive/issue_comments_033349.json:
```json
{
    "body": "Positive review on trac_4502.patch\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T17:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33349",
    "user": "mabshoff"
}
```

Positive review on trac_4502.patch

Cheers,

Michael



---

archive/issue_comments_033350.json:
```json
{
    "body": "Sorry, I spoke too soon. This needs work since it does not apply as is.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T17:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33350",
    "user": "mabshoff"
}
```

Sorry, I spoke too soon. This needs work since it does not apply as is.

Cheers,

Michael



---

archive/issue_comments_033351.json:
```json
{
    "body": "Attachment\n\npatch against Sage 3.2.rc1; apply only this one",
    "created_at": "2008-11-18T21:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33351",
    "user": "GeorgSWeber"
}
```

Attachment

patch against Sage 3.2.rc1; apply only this one



---

archive/issue_comments_033352.json:
```json
{
    "body": "Just changes the failing doctest (and only that single one) to be #random, and should apply cleanly against Sage 3.2.rc1. Now on my box, the doctest for this file passes.",
    "created_at": "2008-11-18T21:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33352",
    "user": "GeorgSWeber"
}
```

Just changes the failing doctest (and only that single one) to be #random, and should apply cleanly against Sage 3.2.rc1. Now on my box, the doctest for this file passes.



---

archive/issue_comments_033353.json:
```json
{
    "body": "`#random` does not fix it since the exception still gets thrown. I tried it, so that is how I found out. In IRC we concluded to nuke the doctests for now and deal with that once SciPy 0.7 is out.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T21:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33353",
    "user": "mabshoff"
}
```

`#random` does not fix it since the exception still gets thrown. I tried it, so that is how I found out. In IRC we concluded to nuke the doctests for now and deal with that once SciPy 0.7 is out.

Cheers,

Michael



---

archive/issue_comments_033354.json:
```json
{
    "body": "Hi John,\n>Could the error message\n\n```\nraise ValueError, \"self must be square\" \n```\n\n>be changed to something like \"matrix must be square\"? Actually, why is this here? I get an error message about non-square matrices (I think produced by scipy) before applying the patch.\n\nThis test and error message were copied verbatim from lines 759/760 of that same file (function \"def determinant(self)\"). In my first patch, I introduced the additional calculation of the determinant in the function for inverting the matrix, and I wanted to make sure that all necessary sanity checks were in place.\n\nWould it be possible for you to provide not only a concrete wording, but a new trac ticket with patch, if you like some other wording better for that error message? I'll review it then. (Maybe just removing this test from the .pyx file and relying on scipy producing the error message for us also for determinants on non-square matrices is an option here.)\n\nCheers,\n\ngsw",
    "created_at": "2008-11-18T21:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33354",
    "user": "GeorgSWeber"
}
```

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

archive/issue_comments_033355.json:
```json
{
    "body": ">#random does not fix it since the exception still gets thrown. I tried it, so that is how I found out. \nStrange. So does this mean the doctest passing as follows:\n\n```\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc1/devel/sage georgweber$ sage -t sage/matrix/matrix_double_dense.pyx\nsage -t  devel/sage-test2/sage/matrix/matrix_double_dense.pyx\n         [4.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.2 seconds\n```\n\nis not enough here? I'm a bit puzzled, which exception exactly gets \"thrown nevertheless\" and when? I'm fine with nuking the doctest and postponing the issue till scipy 0.7 is there and included, I ask just out of curiosity.",
    "created_at": "2008-11-18T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33355",
    "user": "GeorgSWeber"
}
```

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

archive/issue_comments_033356.json:
```json
{
    "body": "With\n\n```\ndiff -r 50c6651a1286 sage/matrix/matrix_double_dense.pyx\n--- a/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 08:58:27 2008 -0800\n+++ b/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 13:49:26 2008 -0800\n@@ -441,7 +441,7 @@\n             \n             sage: A.determinant() < 10e-12\n             True\n-            sage: ~A\n+            sage: ~A # random\n             Traceback (most recent call last):\n             ...\n             LinAlgError: singular matrix\n```\n\nI get\n\n```\nsage -t  devel/sage/sage/matrix/matrix_double_dense.pyx     \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc2/devel/sage/sage/matrix/matrix_double_dense.pyx\", line 444:\n    sage: print \"ignore this\";  ~A # random\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_15[10]>\", line 1, in <module>\n        print \"ignore this\";  ~A # random###line 444:\n    sage: print \"ignore this\";  ~A # random\n      File \"matrix_double_dense.pyx\", line 460, in sage.matrix.matrix_double_dense.Matrix_double_dense.__invert__ (sage/matrix/matrix_double_dense.c:3878)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc2/local/lib/python2.5/site-packages/scipy/linalg/basic.py\", line 306, in inv\n        if info>0: raise LinAlgError, \"singular matrix\"\n    LinAlgError: singular matrix\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_15\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc2/tmp/.doctest_matrix_double_dense.py\n         [2.4 s]\nexit code: 1024\n```\n",
    "created_at": "2008-11-18T21:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33356",
    "user": "mabshoff"
}
```

With

```
diff -r 50c6651a1286 sage/matrix/matrix_double_dense.pyx
--- a/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 08:58:27 2008 -0800
+++ b/sage/matrix/matrix_double_dense.pyx       Tue Nov 18 13:49:26 2008 -0800
@@ -441,7 +441,7 @@
             
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

archive/issue_comments_033357.json:
```json
{
    "body": "Ahhh, sorry for the noise --- the exception does not fly on my box because my box believes the matrix would be invertible and provides an inverse matrix --- but on other computers the matrix is not invertible and there, the exception comes up.\n\nWould that not be an issue to enhance the \"#random\" pragma then?\n\nMore precisely: Allowing on certain boxes the calculation to finish (but throw away the result), and on other boxes having an exception (but again throwing the outcome)?\n\nJust point out to me the respective parts of the IRC conversation if all that info is in there ... and if you find the time and have patience to do so ... ;-)",
    "created_at": "2008-11-18T21:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33357",
    "user": "GeorgSWeber"
}
```

Ahhh, sorry for the noise --- the exception does not fly on my box because my box believes the matrix would be invertible and provides an inverse matrix --- but on other computers the matrix is not invertible and there, the exception comes up.

Would that not be an issue to enhance the "#random" pragma then?

More precisely: Allowing on certain boxes the calculation to finish (but throw away the result), and on other boxes having an exception (but again throwing the outcome)?

Just point out to me the respective parts of the IRC conversation if all that info is in there ... and if you find the time and have patience to do so ... ;-)



---

archive/issue_comments_033358.json:
```json
{
    "body": "The issue is the following:\n\n```\n[10:34am] wstein|afk: mabshoff -- all that #random does is the following.\n[10:35am] wstein|afk: sage: foo # random\n[10:35am] wstein|afk: gets replaced by\n[10:35am] wstein|afk: sage: _ = foo\n[10:35am] wstein|afk: That's it.\n[10:35am] mabshoff: mhh\n[10:35am] wstein|afk: So it won't work at all with exceptions.\n[10:35am] wstein|afk: Better might be:\n[10:35am] wstein|afk: sage: foo # random\n[10:35am] wstein|afk: gets replaced by\n[10:35am] wstein|afk: sage: foo\n[10:35am] wstein|afk: ...\n[10:35am] wstein|afk: If that worked.\n[10:35am] wstein|afk: I didn't know about ... when I wrote # random.\n```\n\nThe goal now is to get 3.2 out and the easiest way to do this is to nuke the affected doctests and then deal with `#random` properly in 3.2.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T22:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33358",
    "user": "mabshoff"
}
```

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

archive/issue_comments_033359.json:
```json
{
    "body": "Thanks a lot!!!",
    "created_at": "2008-11-18T22:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33359",
    "user": "GeorgSWeber"
}
```

Thanks a lot!!!



---

archive/issue_comments_033360.json:
```json
{
    "body": "Attachment\n\napply only this one (doctest just nuked)",
    "created_at": "2008-11-18T22:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33360",
    "user": "GeorgSWeber"
}
```

Attachment

apply only this one (doctest just nuked)



---

archive/issue_comments_033361.json:
```json
{
    "body": "Is it that what you mean by \"nuke\"ing?",
    "created_at": "2008-11-18T22:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33361",
    "user": "GeorgSWeber"
}
```

Is it that what you mean by "nuke"ing?



---

archive/issue_comments_033362.json:
```json
{
    "body": "Yes, but two things:\n\n* a comment would be nice that the issue needs to be fixed with a reference to the ticket\n* The other test right before, i.e. \"sage: A.inverse().det()\" also needs to be commented out\n\nOnce the above two happen with a new patch I will give this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T22:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33362",
    "user": "mabshoff"
}
```

Yes, but two things:

* a comment would be nice that the issue needs to be fixed with a reference to the ticket
* The other test right before, i.e. "sage: A.inverse().det()" also needs to be commented out

Once the above two happen with a new patch I will give this a positive review.

Cheers,

Michael



---

archive/issue_comments_033363.json:
```json
{
    "body": "OK, no problem. (Except for the time it will take --- another 12 hours or so till I am back home.)",
    "created_at": "2008-11-19T07:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33363",
    "user": "GeorgSWeber"
}
```

OK, no problem. (Except for the time it will take --- another 12 hours or so till I am back home.)



---

archive/issue_comments_033364.json:
```json
{
    "body": "Attachment\n\naddressing the reviewers wishes (hopefully)",
    "created_at": "2008-11-19T18:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33364",
    "user": "GeorgSWeber"
}
```

Attachment

addressing the reviewers wishes (hopefully)



---

archive/issue_comments_033365.json:
```json
{
    "body": "Positive review for 4502-next_try.3.patch. Thanks.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-19T19:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33365",
    "user": "mabshoff"
}
```

Positive review for 4502-next_try.3.patch. Thanks.

Cheers,

Michael



---

archive/issue_comments_033366.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-19T19:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33366",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033367.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-19T19:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4502#issuecomment-33367",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc2
