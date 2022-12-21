# Issue 9175: cygwin: pari's sea.gp program just segfaults on Cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:59:26

Assignee: tbd


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py"
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py", line 865:
    sage: EllipticCurve(GF(next_prime(10**20)),[1,2,3,4,5]).cardinality(algorithm='sea')
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[12]>", line 1, in <module>
        EllipticCurve(GF(next_prime(Integer(10)**Integer(20))),[Integer(1),Integer(2),Integer(3),Integer(4),Integer(5)]).cardinality(algorithm='sea')###line 865:
    sage: EllipticCurve(GF(next_prime(10**20)),[1,2,3,4,5]).cardinality(algorithm='sea')
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 921, in cardinality
        N = self.cardinality_sea()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 1155, in cardinality_sea
        return sea.ellsea(list(self.a_invariants()), p, early_abort=early_abort)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/sea.py", line 48, in ellsea
        raise RuntimeError, "Error: '%s'"%N
    RuntimeError: Error: '  *** CM_CardEFp: bug in GP (Segmentation Fault), please report'
**********************************************************************
1 items had failures:
```



---

Comment by was created at 2010-06-07 05:16:10

SEA.gp does not *always* fail.  often it works:

```

sage: E = EllipticCurve('389a').change_ring(GF(next_prime(10^15)))
sage: E.cardinality_sea()
999999960319827

```



---

Comment by jdemeyer created at 2010-08-01 15:55:27

By #9343, the script sea.gp will be removed, so this will trivially be fixed.


---

Comment by mpatel created at 2010-09-10 10:48:43

Resolution: duplicate
