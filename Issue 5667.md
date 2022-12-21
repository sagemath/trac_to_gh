# Issue 5667: matrix modified when operation should be rolled back

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-04-02 19:42:42

Assignee: was

Check this out:


```
sage: b

[ 1  1  0 -1  1  0]
[ 0  2  0 -5  3  1]
[ 0  0  1  2 -1  0]
sage: b[1] = b[1]/2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/14543/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6325)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:6667)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/rational.so in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:16008)()

TypeError: no conversion of this rational to integer
sage: b

[ 1  1  0 -1  1  0]
[ 0  1  0 -5  3  1]
[ 0  0  1  2 -1  0]
sage: b.base_ring()
Integer Ring
```


The matrix `b` was modified, but should not have been modified since the operation had an error.
