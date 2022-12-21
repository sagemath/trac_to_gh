# Issue 7391: Warn the user of incorrect results when an approximate ill-conditioned matrix is used

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-04 21:36:06

Assignee: was

This should probably give a warning to the user that the matrix is ill-conditioned and you may get wrong results (like you do in this case).


```
sage: n = matrix([ [-0.3, 0.2, 0.1],
                    [0.2, -0.4, 0.4],
                    [0.1, 0.2, -0.5] ])

sage: n.echelon_form()

[ 1.00000000000000 0.000000000000000 0.000000000000000]
[0.000000000000000  1.00000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000  1.00000000000000]

```



---

Comment by jason created at 2009-11-04 21:36:38

FYI: 


```
sage: m.change_ring(RDF).SVD()[1]

[   0.772642968023               0.0               0.0]
[              0.0    0.450580563234               0.0]
[              0.0               0.0 3.13289758759e-17]
```



---

Comment by jason created at 2010-03-17 05:58:36

Changing type from defect to enhancement.
