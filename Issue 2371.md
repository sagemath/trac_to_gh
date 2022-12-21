# Issue 2371: tut.tex failures for 2.10.3.rc0

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-03-02 22:31:29

Assignee: wdj

Extracted from a recent sage -testall:

Testing SAGE tutorial

sage -t  tut.tex                                            


```
**********************************************************************
File "tut.py", line 2377:
    : F.reduced_groebner_bases ()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_103[3]>", line 1, in <module>
        F.reduced_groebner_bases ()###line 2377:
    : F.reduced_groebner_bases ()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 272, in reduced_groebner_bases
        G0 = self._gfan_reduced_groebner_bases()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "<string>", line 1
         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field
                                                     ^
     SyntaxError: invalid syntax
**********************************************************************
File "tut.py", line 2386:
    : F.fvector()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_103[4]>", line 1, in <module>
        F.fvector()###line 2386:
    : F.fvector()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 358, in fvector
        f = self.gfan(cmd='fvector', I=self._gfan_reduced_groebner_bases().replace(' ',','))
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "<string>", line 1
         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field
                                                     ^
     SyntaxError: invalid syntax
**********************************************************************
File "tut.py", line 1453:
    : eigvecs = g.eigenspaces()[0][1], g.eigenspaces()[1][1]; eigvecs
Expected:
    ([
    (1, 5)
    ], [
    (1, 1)
    ])
Got:
    (Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 5], Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 1])
**********************************************************************
File "tut.py", line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_63[7]>", line 1, in <module>
        e.word_problem([b1,b2,b3,b4,b5],display=False)###line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
    TypeError: word_problem() got an unexpected keyword argument 'display'
**********************************************************************
3 items had failures:
   2 of   5 in __main__.example_103
   1 of   4 in __main__.example_57
   1 of  16 in __main__.example_63
***Test Failed*** 4 failures.
For whitespace errors, see the file .doctest_tut.tex
         [22.2 s]
exit code: 256

----------------------------------------------------------------------
```

The following tests failed:


        sage -t  tut.tex

Total time for all tests: 22.2 seconds



---

Comment by mabshoff created at 2008-03-02 22:36:10

Changing priority from minor to blocker.


---

Comment by mabshoff created at 2008-03-02 22:36:10

David, this is a *blocker* for the 2.10.3 release :)

Cheers,

Michael


---

Comment by wdj created at 2008-03-02 22:46:18

Okay, it is a blocker, but some of the failures possibly are from patches
new to 2.10.3.rc0. Should I wait for 2.10.3.rc1 or try to fix it now?

BTW, I would dearly love to include a new example based on the recent patches of
Simon King. Would that be okay?


---

Comment by wdj created at 2008-03-11 01:52:51

I assume that there errors have not changed from rc0 to rc3?


---

Comment by was created at 2008-03-11 02:33:34

Resolution: fixed


---

Attachment


---

Comment by mabshoff created at 2008-03-11 02:37:19

Merged in Sage 2.10.3.rc5
