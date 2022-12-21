# Issue 6621: [with patch, needs review] Permutation.inverse too slow

Issue created by migration from Trac.

Original creator: aclaesson

Original creation time: 2009-07-25 17:31:34

Assignee: mhansen

The running time of the current implementation of Permutation.inverse is quadratic in the length of the permutation. The attached small patch is linear.



---

Comment by ddrake created at 2009-07-25 17:43:38

Uh oh, this doesn't pass doctests: I get

```
File "/var/tmp/sage-4.1/devel/sage/sage/combinat/symmetric_group_algebra.py", line 141:
    sage: QS3.cpi([1,1,1])
Exception raised:
    Traceback (most recent call last):
      File "/var/tmp/sage-4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/var/tmp/sage-4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/var/tmp/sage-4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[5]>", line 1, in <module>
        QS3.cpi([Integer(1),Integer(1),Integer(1)])###line 141:
    sage: QS3.cpi([1,1,1])
      File "/var/tmp/sage-4.1/local/lib/python/site-packages/sage/combinat/symmetric_group_algebra.py", line 158, in cpi
        cpi += big_coeff * character_table[p_index][np.index(g.inverse().cycle_type())] * self(g)
    AttributeError: 'list' object has no attribute 'cycle_type'
```


Instead of `return w`, you need `return Permutation(w)`


---

Attachment

Positive review! Here are some timings:

For the permutation [6,7,8,9,4,2,3,1,5], on my machine, the timing went from 70.9 µs per loop to 24.7 µs per loop. (This is all "%timeit p.inverse()".

For [19, 5, 13, 8, 7, 15, 9, 10, 16, 3, 12, 6, 2, 20, 18, 11, 14, 4, 17, 1], it went from 
263 µs per loop to 40 µs per loop.

For [14, 17, 1, 24, 16, 34, 19, 9, 20, 18, 36, 5, 22, 2, 27, 40, 37, 15, 3, 35, 10, 25, 21, 8, 13, 26, 12, 32, 23, 38, 11, 4, 6, 39, 31, 28, 29, 7, 30, 33], it went from 923 to 64.8. So it does look like this patch turns quadratic behavior into linear behavior.

This is Anders' first contribution to Sage, by the way.


---

Comment by mvngu created at 2009-07-25 22:01:52

Resolution: fixed
