# Issue 5816: [with patch; needs review] doctesting -- make it possible run doctests in order from file, in random order, and in random seeded order

Issue created by migration from https://trac.sagemath.org/ticket/5816

Original creator: was

Original creation time: 2009-04-18 21:41:48

Assignee: mabshoff




---

Attachment


---

Comment by was created at 2009-04-18 23:32:10

The following tests fail after applying this patch and running the test suite on rc3:

```
sage -t -long devel/sage/sage/quadratic_forms/quadratic_form.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/quadratic_forms/quadratic_form.py", line 1304:
    sage: Q1.level_ideal()
Expected:
    Principal ideal (1) of Rational Field
Got:
    doctest:1252: UserWarning: Warning -- The level of a quadratic form over a field is always 1.  Do you really want to do this?!?
    Principal ideal (1) of Rational Field
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_0351962372
***Test Failed*** 1 failures.




MOST EVERYTHING IN:
sage -t -long devel/sage/sage/misc/latex.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/misc/latex.py", line 62:
    sage: latex([1,2,3])
Expected:
 








sage -t -long devel/sage/sage/libs/pari/gen.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/pari/gen.pyx", line 8575:
    sage: pari._primelimit()
Expected:
    500519
Got:
    500000
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/pari/gen.pyx", line 7013:
    sage: pari('[a,b,c; d,e,f; g,h,i]').matadjoint()
Expected:
    [(i*e - h*f), (-i*b + h*c), (f*b - e*c); (-i*d + g*f), i*a - g*c, -f*a + d*c; (h*d - g*e), -h*a + g*b, e*a - d*b]
Got:
    [e*i - h*f, -b*i + h*c, (f*b - e*c); -d*i + g*f, a*i - g*c, (-f*a + d*c); (h*d - g*e), (-h*a + g*b), (e*a - d*b)]
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_0786952607
   1 of   4 in __main__.example_2085375216
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc3/tmp/.doctest_gen.py
         [3.4 s]








SEVERAL THINGS:
sage -t -long devel/sage/sage/libs/symmetrica/schur.pxi
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/symmetrica/schur.pxi", line 369:
    sage: symmetrica.compute_schur_with_alphabet_det(2,2)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0960543897[2]>", line 1, in <module>
        symmetrica.compute_schur_with_alphabet_det(Integer(2),Integer(2))###line 369:
    sage: symmetrica.compute_schur_with_alphabet_det(2,2)
      File "schur.pxi", line 382, in sage.libs.symmetrica.symmetrica.compute_schur_with_alphabet_det_symmetrica (sage/libs/symmetrica/symme
trica.c:17919)        if isinstance(part, (int, Integer)):
    TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types









sage -t -long devel/sage/sage/rings/real_rqdf.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/real_rqdf.pyx", line 531:
    sage: w= RQDF('1.34435343435344446376457677898097745635222')
Expected nothing
Got:
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/real_rqdf.pyx", line 4:
    : RQDF(1)
Expected:
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    1.000000000000000000000000000000000000000000000000000000000000000
Got:
    1.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_0123338167
   1 of  12 in __main__.example_0497399660
***Test Failed*** 2 failures.












sage -t -long devel/sage/sage/libs/fplll/fplll.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/fplll/fplll.pyx", line 761:
    sage: A = gen_ntrulike2(5,10,12); A
Expected:
    [ 12   0   0   0   0   0   0   0   0   0]
    [  0  12   0   0   0   0   0   0   0   0]
    [  0   0  12   0   0   0   0   0   0   0]
    [  0   0   0  12   0   0   0   0   0   0]
    [  0   0   0   0  12   0   0   0   0   0]

and a few more...









sage -t -long devel/sage/sage/rings/number_field/class_group.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/number_field/class_group.py", line 107:
    sage: C.gen(0)
Expected:
    Fractional ideal class (130, 1/2*a + 137/2)
Got:
    Fractional ideal class (41, a - 10)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/number_field/class_group.py", line 109:
    sage: C.gen(1)
Expected:
    Fractional ideal class (7, a)
Got:
    Fractional ideal class (17, a)
**********************************************************************













sage -t -long devel/sage/sage/structure/proof/proof.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/structure/proof/proof.py", line 109:
    sage: proof.number_field()
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_3571288829
***Test Failed*** 1 failures.








         [1.4 s]
sage -t -long devel/sage/sage/combinat/crystals/crystals.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/crystals/crystals.py", line 80:
    sage: Tab.plot()
Expected nothing
Got:
    Graphics object consisting of 52 graphics primitives
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_3764993440
***Test Failed*** 1 failures.











sage -t -long devel/sage/sage/combinat/words/word.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/words/word.py", line 119:
    sage: w
Expected:
    word: 2,1,3,12
Got:
    word: 2-1-3-12
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/words/word.py", line 837:
    sage: Words(range(1000))([0,1,10,101]).__str__()
Expected:
    'word: 0,1,10,101'
Got:
    'word: 0-1-10-101'
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_0401337461
   1 of   5 in __main__.example_2333993738
***Test Failed*** 2 failures.













sage -t -long devel/sage/sage/combinat/sf/sfa.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/sf/sfa.py", line 65:
    sage: m(a)
Expected:
    3*m[1, 1, 1, 1] + 2*m[2, 1, 1] + m[2, 2] + m[3, 1]
Got:
    3*m[1, 1, 1, 1] + m[2, 2] + 2*m[2, 1, 1] + m[3, 1]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/sf/sfa.py", line 94:
    sage: m.get_print_style()
Expected:
    'lex'
Got:
    'maximal_part'
**********************************************************************
1 items had failures:















sage -t -long devel/sage/sage/plot/plot3d/texture.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/plot/plot3d/texture.py", line 69:
    sage: t.mtl_str()
Expected:
    'newmtl texture2\nKa 0.2 0.2 0.5\nKd 0.4 0.4 1.0\nKs 0.0 0.0 0.0\nillum 1\nNs 1\nd 0.600000000000000'
Got:
    'newmtl texture13\nKa 0.2 0.2 0.5\nKd 0.4 0.4 1.0\nKs 0.0 0.0 0.0\nillum 1\nNs 1\nd 0.600000000000000'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/plot/plot3d/texture.py", line 71:
    sage: t.tachyon_str()
Expected:
    'Texdef texture2\n  Ambient 0.333333333333 Diffuse 0.666666666667 Specular 0.0 Opacity 0.600000000000000\n   Color 0.4 0.4 1.0\n   TexF
unc 0'
Got:
    'Texdef texture13\n  Ambient 0.333333333333 Diffuse 0.666666666667 Specular 0.0 Opacity 0.600000000000000\n   Color 0.4 0.4 1.0\n   Tex
Func 0'
**********************************************************************
1 items had failures:
   2 of  10 in __main__










sage -t -long devel/sage/sage/calculus/equations.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/equations.py", line 895:
    sage: bool( x^2 > x )
Expected:
    False
Got:
    True
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/equations.py", line 1391:
    sage: assumptions()
Expected:
    [x > 0, y > 0, z == 1]
Got:
    [x > 2, c != 0, x > 0, y > 0, z == 1]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/equations.py", line 1394:
    sage: assumptions()
Expected:
    [y > 0]
Got:
    [x > 2, c != 0, y > 0]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/equations.py", line 1397:
    sage: assumptions()
Expected:
    [y > 0, y is even]
Got:
    [x > 2, c != 0, y > 0, y is even]
**********************************************************************
2 items had failures:
   1 of  13 in __main__.example_0570214236
   3 of  13 in __main__.example_0930958418













age -t -long devel/sage/sage/interfaces/singular.py
Exception exceptions.RuntimeError: RuntimeError('Singular error:\n   ? `sage48` is not defined\n   ? error occurred in STDIN line 24: `sage48 == sage48;`',) in 'sage.structure.parent_old._unregister_pair' ignored
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/singular.py", line 1051:
    sage: singular.option()
Expected:
    //options: redefine loadLib usage prompt
Got:
    //options: intStrategy redefine loadLib usage prompt
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/singular.py", line 1053:
    sage: singular.option('get')
Expected:
    0,
    10321
Got:
    67108864,
    10321
[[tons more problems!]]













age -t -long devel/sage/sage/interfaces/maxima.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/maxima.py", line 275:
    sage: maxima("laplace(diff(x(t),t),t,s)")
Expected:
    s*?%laplace(x(t),t,s)-x(0)
Got:
    s*'laplace(x(t),t,s)-x(0)
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/maxima.py", line 280:
    sage: maxima("laplace(diff(x(t),t,2),t,s)")
Expected:
    -?%at('diff(x(t),t,1),t=0)+s^2*?%laplace(x(t),t,s)-x(0)*s
Got:
    -'at('diff(x(t),t,1),t=0)+s^2*'laplace(x(t),t,s)-x(0)*s
[[many other problems]]










sage -t -long devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/calculus.py", line 8081:
    sage: latex(gamma(x+1))
Expected:
    \Gamma \left( x + 1 \right)
Got:
    \Gamma \left( \mathrm{x} + 1 \right)
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_1540991106












sage -t -long devel/sage/sage/server/notebook/worksheet.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/worksheet.py", line 147:
    sage: sage.server.notebook.worksheet._a_sage
Expected nothing
Got:
    Sage
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_3589583854
***Test Failed*** 1 failures.









The following tests failed:

        sage -t -long devel/sage/sage/quadratic_forms/random_quadraticform.py # File not found
        sage -t -long devel/sage/sage/quadratic_forms/quadratic_form.py # 1 doctests failed
        sage -t -long devel/sage/sage/misc/random_testing.py # File not found
        sage -t -long devel/sage/sage/misc/randstate.pyx # File not found
        sage -t -long devel/sage/sage/misc/latex.py # 3 doctests failed
        sage -t -long devel/sage/sage/libs/pari/gen.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/libs/symmetrica/schur.pxi # 5 doctests failed
        sage -t -long devel/sage/sage/rings/real_rqdf.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/libs/fplll/fplll.pyx # 5 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/class_group.py # 2 doctests failed
        sage -t -long devel/sage/sage/structure/proof/proof.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/crystals/crystals.py # 1 doctests failed
        sage -t -long devel/sage/sage/combinat/words/word.py # 2 doctests failed
        sage -t -long devel/sage/sage/combinat/sf/sfa.py # 2 doctests failed
        sage -t -long devel/sage/sage/probability/random_variable.py # File not found
        sage -t -long devel/sage/sage/plot/plot3d/texture.py # 2 doctests failed
        sage -t -long devel/sage/sage/calculus/equations.py # 4 doctests failed
        sage -t -long devel/sage/sage/interfaces/singular.py # 5 doctests failed
        sage -t -long devel/sage/sage/interfaces/maxima.py # 5 doctests failed
        sage -t -long devel/sage/sage/calculus/calculus.py # 1 doctests failed
        sage -t -long devel/sage/sage/ext/random.pxi # File not found
        sage -t -long devel/sage/sage/server/notebook/worksheet.py # 1 doctests failed
----------------------------------------------------------------------

```



---

Comment by was created at 2009-04-18 23:33:31

With -rand=1 we get the following failures, that are slightly different than the above


```


It's very interesting to run on the full rc3 tree with a fixed random seed.   I think this
reveals *numerous* errors and subtle problems:

./sage -tp 20 -long -rand=1 devel/sage/sage/ > testlong-rand1.log&

This already turns up the following *interesting* problems:

sage -t -long -rand=1 devel/sage/sage/modular/modform/space.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/modular/modform/space.py", line 763:
    sage: M.q_expansion_basis()
Expected:
    [
    q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
    1 + 12/5*q + 36/5*q^2 + 48/5*q^3 + 84/5*q^4 + 72/5*q^5 + O(q^6)
    ]
Got:
    [
    q - 2*q^2 - q^3 + 2*q^4 + q^5 + 2*q^6 - 2*q^7 - 2*q^9 - 2*q^10 + q^11 - 2*q^12 + 4*q^13 + O(q^14),
    1 + 12/5*q + 36/5*q^2 + 48/5*q^3 + 84/5*q^4 + 72/5*q^5 + 144/5*q^6 + 96/5*q^7 + 36*q^8 + 156/5*q^9 + 216/5*q^10 + 12/5*q^11 + 336/5*q^12 + 168/5*q^13 + O(q^14)
    ]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_3297184748




sage -t -long -rand=1 devel/sage/sage/misc/latex.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/misc/latex.py", line 62:
    sage: latex([1,2,3])
Expected:
    \left[1,
[[everything breaks as you know]]





sage -t -long -rand=1 devel/sage/sage/libs/pari/gen.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/pari/gen.pyx", line 8280:
    sage: a = pari('1.2'); a, a.type(), a.precision()
Expected:
    (1.20000000000000, 't_REAL', 3)
Got:
    (1.20000000000000, 't_REAL', 4)
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_0036674092






sage -t -long -rand=1 devel/sage/sage/misc/randstate.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/misc/randstate.pyx", line 59:
    : rtest()
Expected:
    (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), [ 0, 0, 1, 0, 1 ], 2137873234, 27695, 0.19982565117278328)
Got:
    (207, 0.505364206568040, 4*x^2 + 1/2, (2,3)(4,5), [ 0, 0, 1, 0, 1 ], 2137873234, 27695, 0.19982565117278328)
**********************************************************************
1 items had failures:
   1 of  62 in __main__.example_0299976341
***Test Failed*** 1 failures.






The following might be related to http://trac.sagemath.org/sage_trac/ticket/5789

sage -t -long -rand=1 devel/sage/sage/rings/real_rqdf.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/real_rqdf.pyx", line 1116:
    sage: RQDF(-1)._complex_double_(CDF)
Expected:
    -1.0
Got:
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    -1.0
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/real_rqdf.pyx", line 4:
    : RQDF(1)
Expected:
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    1.000000000000000000000000000000000000000000000000000000000000000
Got:
    1.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_0007003101
   1 of  12 in __main__.example_0299976341







sage -t -long -rand=1 devel/sage/sage/libs/fplll/fplll.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/fplll/fplll.pyx", line 715:
    sage: A = gen_ntrulike(5,10,12); A
Expected:
    [  1   0   0   0   0 320 351 920 714  66]
    [  0   1   0   0   0 351 920 714  66 320]
    [  0   0   1   0   0 920 714  66 320 351]
    [  0   0   0   1   0 714  66 320 351 920]
    [  0   0   0   0   1  66 320 351 920 714]
    [  0   0   0   0   0  12   0   0   0   0]
    [  0   0   0   0   0   0  12   0   0   0]
    [  0   0   0   0   0   0   0  12   0   0]
    [  0   0   0   0   0   0   0   0  12   0]
    [  0   0   0   0   0   0   0   0   0  12]
Got:
    [  1   0   0   0   0 116 331 303 963 456]
    [  0   1   0   0   0 331 303 963 456 116]
    [  0   0   1   0   0 303 963 456 116 331]
    [  0   0   0   1   0 963 456 116 331 303]
    [  0   0   0   0   1 456 116 331 303 963]
    [  0   0   0   0   0  12   0   0   0   0]
    [  0   0   0   0   0   0  12   0   0   0]
    [  0   0   0   0   0   0   0  12   0   0]
    [  0   0   0   0   0   0   0   0  12   0]
    [  0   0   0   0   0   0   0   0   0  12]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/libs/fplll/fplll.pyx", line 656:
    sage: A = gen_uniform(10,10,12); A

[[tons more problems]]








age -t -long -rand=1 devel/sage/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx", line 379:
    sage: f.small_roots()
Expected:
    [4]
Got:
    verbose 2 (<module>) epsilon = 0
    verbose 2 (<module>) m = 3
    verbose 2 (<module>) t = 0
    verbose 2 (<module>) X = 4
    verbose 1 (<module>) LLL of 9x12 matrix (algorithm fpLLL:wrapper)
    verbose 1 (<module>) LLL finished (time = 0.0)
    [4]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0208607704










sage -t -long -rand=1 devel/sage/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 3991:
    sage: p.roots(ring=RR, algorithm='numpy')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: array must not contain infs or NaNs
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0061063177[118]>", line 1, in <module>
        p.roots(ring=RR, algorithm='numpy')###line 3991:
    sage: p.roots(ring=RR, algorithm='numpy')
      File "polynomial_element.pyx", line 4235, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:34787)
        return self.change_ring(L).roots(multiplicities=multiplicities, algorithm=algorithm)
      File "polynomial_element.pyx", line 4156, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:33064)
        raise
      File "polynomial_element.pyx", line 4146, in sage.rings.polynomial.polynomial_element.roots (sage/rings/polynomial/polynomial_element.c:32862)
        ext_rts1 = numpy.roots(numpy_array)
      File "/home/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/numpy/lib/polynomial.py", line 180, in roots
        roots = _eigvals(A)
      File "/home/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/numpy/lib/polynomial.py", line 35, in _eigvals
        return eigvals(arg)
      File "/home/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/numpy/linalg/linalg.py", line 597, in eigvals
        _assertFinite(a)
      File "/home/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/numpy/linalg/linalg.py", line 125, in _assertFinite
        raise LinAlgError, "Array must not contain infs or NaNs"
    LinAlgError: Array must not contain infs or NaNs
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 4002:
    sage: p.roots(ring=RR)
Expected:
    [(0.000000000000000, 1)]
Got:
    [(-0.000000000000000, 1)]











sage -t -long -rand=1 devel/sage/sage/combinat/sloane_functions.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/sloane_functions.py", line 7203:
    sage: initial = len(sloane.A001358._b)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0246131326[2]>", line 1, in <module>
        initial = len(sloane.A001358._b)###line 7203:
    sage: initial = len(sloane.A001358._b)
    AttributeError: 'A001358' object has no attribute '_b'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/sloane_functions.py", line 7205:
    sage: len(sloane.A001358._b) - initial > 0
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0246131326[4]>", line 1, in <module>
        len(sloane.A001358._b) - initial > Integer(0)###line 7205:
    sage: len(sloane.A001358._b) - initial > 0
    NameError: name 'initial' is not defined
**********************************************************************
1 items had failures:






sage -t -long -rand=1 devel/sage/sage/combinat/words/word.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/words/word.py", line 119:
    sage: w
Expected:
    word: 2,1,3,12
Got:
    word: 2-1-3-12
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/words/word.py", line 837:
    sage: Words(range(1000))([0,1,10,101]).__str__()
Expected:
    'word: 0,1,10,101'
Got:
    'word: 0-1-10-101'
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_1192818567
   1 of   5 in __main__.example_1949818771
***Test Failed*** 2 failures.







sage -t -long -rand=1 devel/sage/sage/calculus/equations.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/equations.py", line 895:
    sage: bool( x^2 > x )
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_3038663466
***Test Failed*** 1 failures.








sage -t -long -rand=1 devel/sage/sage/interfaces/r.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/r.py", line 1071:
    sage: t = a.trait_names()
Expected nothing
Got:
    <BLANKLINE>
    Building R command completion list (this takes
    a few seconds only the first time you do it).
    To force rebuild later, delete /scratch/wstein/sage//r_commandlist.sobj.
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_1346836858







sage -t -long -rand=1 devel/sage/sage/interfaces/singular.py**********************************************************************File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/singular.py", line 988:    sage: singular.trait_names()Expected:    ['headStand',     ...     'stdfglm']Got:    ['pause', 'writelist', 'tab', 'split', 'showrecursive', 'show', 'rMacaulay', 'pmat', 'lprint', 'allprint', 'newtonDiag', 'subrInterred', 'id2mod', 'mod2id', 'denominator', 'numerator', 'content', 'lcm', 'rad_con', 'normalize', 'mindeg1', 'mindeg', 'maxdeg1', 'maxdeg', 'maxcoef', 'is_zero', 'freerank', 'kat_var', 'katsura', 'cyclic', 'substitute', 'hilbPoly', 'select1', 'select', 'sat', 'nselect', 'elim1', 'elim', 'blowup0', 'triangMH', 'triangM', 'triangLfak', 'triangL', 'absFactorize', 'newZero_decom

[[tons of other issues due to bad doctests]]







sage -t -long -rand=1 devel/sage/sage/interfaces/maxima.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/maxima.py", line 1872:
    sage: f.diff('x')
Expected:
    34*y*'diff(y,x,1)+2*x
Got:
    2*x
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/interfaces/maxima.py", line 1602:
    sage: f = maxima('1/(x-1)^3'); f
Expected:
    1/(x-1)^3
Got:
    1
And *NUMEROUS* other issues!!










sage -t -long -rand=1 devel/sage/sage/combinat/partition.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/combinat/partition.py", line 2372:
    sage: RestrictedPartitions(5,[3,2,1]).__repr__()
Expected:
    doctest:...: DeprecationWarning: RestrictedPartitions is deprecated; use Partitions with the parts_in keyword instead.
    'Partitions of 5 restricted to the values [1, 2, 3] '
Got:
    doctest:1: DeprecationWarning: RestrictedPartitions is deprecated; use Partitions with the parts_in keyword instead.
    doctest:2324: DeprecationWarning: RestrictedPartitions_nsk is deprecated; use Partitions with the parts_in keyword instead.
    'Partitions of 5 restricted to the values [1, 2, 3] '

[[and more]]





sage -t -long -rand=1 devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/calculus/calculus.py", line 8211:
    sage: latex(factorial(x))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2333006911[2]>", line 1, in <module>
        latex(factorial(x))###line 8211:
    sage: latex(factorial(x))
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8249, in __call__
        return factorial(n, **kwds)
      File "/scratch/wstein/build/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/rings/arith.py", line 328, in factorial
        raise ValueError, "factorial -- must be nonnegative"
    ValueError: factorial -- must be nonnegative

(not much more)







sage -t -long -rand=1 devel/sage/sage/server/notebook/worksheet.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/server/notebook/worksheet.py", line 147:
    sage: sage.server.notebook.worksheet._a_sage
Expected nothing
Got:
    Sage
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_3577862625






The following tests failed:

        sage -t -long -rand=1 devel/sage/sage/modular/modform/space.py # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/misc/session.pyx # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/misc/latex.py # 17 doctests failed
        sage -t -long -rand=1 devel/sage/sage/libs/pari/gen.pyx # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/misc/randstate.pyx # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/rings/real_rqdf.pyx # 2 doctests failed
        sage -t -long -rand=1 devel/sage/sage/libs/fplll/fplll.pyx # 5 doctests failed
        sage -t -long -rand=1 devel/sage/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed
        sage -t -long -rand=1 devel/sage/sage/combinat/sloane_functions.py # 2 doctests failed
        sage -t -long -rand=1 devel/sage/sage/combinat/words/word.py # 2 doctests failed
        sage -t -long -rand=1 devel/sage/sage/calculus/equations.py # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/interfaces/r.py # 1 doctests failed
        sage -t -long -rand=1 devel/sage/sage/interfaces/singular.py # 6 doctests failed
        sage -t -long -rand=1 devel/sage/sage/interfaces/maxima.py # 14 doctests failed
        sage -t -long -rand=1 devel/sage/sage/combinat/partition.py # 2 doctests failed
        sage -t -long -rand=1 devel/sage/sage/calculus/calculus.py # 5 doctests failed
        sage -t -long -rand=1 devel/sage/sage/server/notebook/worksheet.py # 1 doctests failed
----------------------------------------------------------------------




```



---

Comment by rbeezer created at 2009-04-18 23:52:37

Great work!  I like the ability to do this optionally, and of course with a reproducible seed.  Motivating discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/320845a4c9b9c75f


---

Comment by mabshoff created at 2009-04-18 23:59:56

Replying to [comment:3 rbeezer]:
> Great work!  I like the ability to do this optionally, and of course with a reproducible seed.  

Hi Rob, this sounds like a positive review. Is it one? In that case you should change the summary.

Cheers,

Michael


---

Comment by cwitty created at 2009-04-19 00:02:14

I like the patch, except for one major and one minor issue:

Major: I can't positively review a patch where doctests fail after the patch is applied. I'm not sure what's the right thing to do here; I'm going to post on sage-devel.

Minor: I don't like the name of the command-line argument (I would guess that "-rand" would set the random seed for each doctest, or something). How about -randorder instead?


---

Comment by mabshoff created at 2009-04-19 00:08:49

Well, given the above I am bumping it to 3.4.2. There are bugs in doctests being exposed here, but short of a patch that fixes all those issues I don't think delaying 3.4.1 for this patch will be worth it.

Cheers,

Michael


---

Comment by rbeezer created at 2009-04-19 00:11:54

Replying to [comment:4 mabshoff]:
> Hi Rob, this sounds like a positive review. Is it one? In that case you should change the summary.

Hi Michael,

I wanted to wait for someone like Carl to weigh in, so I didn't mean my comments to be a positive review (just enthusiasm!).  I meant to restrict my comments to functionality, and not the code itself.  ;-)  I'm glad William did this so quickly, but I think I agree with your decision not to hold up releases for it.

Rob


---

Comment by was created at 2009-04-19 00:16:19

Replying to [comment:5 cwitty]:
> I like the patch, except for one major and one minor issue:
> 
> Major: I can't positively review a patch where doctests fail after the patch is applied. I'm not sure what's the right thing to do here; I'm going to post on sage-devel.
> 

Yep, that's a bit of an issue.  I will make it run with no changes ("traditional mode") if one doesn't pass the -randorder option. 

> Minor: I don't like the name of the command-line argument (I would guess that "-rand" would set the random seed for each doctest, or something). How about -randorder instead?

I like randorder better too.  I'll make a patch to change it to that.


---

Attachment

this fixes a bug (before it always ran in random order), changes to -randorder, and makes it so not giving the option uses the "traditional" order.


---

Comment by was created at 2009-04-19 00:21:25

With this patch applied we have

```
./sage -tp 30 devel/sage/sage/ 
...
----------------------------------------------------------------------
All tests passed!
Timings have been updated.
Total time for all tests: 181.0 seconds
```


on sage.math with sage-3.4.1.rc3.


---

Comment by rbeezer created at 2009-04-19 00:24:06

Replying to [comment:8 was]:
> I will make it run with no changes ("traditional mode") if one doesn't pass the -randorder option. 

I think that is a great approach (which I just advocated for on sage-devel).


---

Comment by cwitty created at 2009-04-19 01:59:39

Code looks good, doctests pass without randorder, doctests fail unpredictably with randorder, doctests fail repeatably with randorder=N... it's all good :)

Positive review.  Apply both patches (to the scripts repository).


---

Comment by mabshoff created at 2009-04-19 02:08:31

Merged both patches in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 02:08:31

Resolution: fixed
