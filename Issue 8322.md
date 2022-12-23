# Issue 8322: on sage.combinat.tableau.insert_word() , parameter left= is broken   (fix provided)

Issue created by migration from https://trac.sagemath.org/ticket/8322

Original creator: drini

Original creation time: 2010-02-22 00:41:13

Assignee: somebody

on
/usr/local/sage2/local/lib/python2.6/site-packages/sage/combinat/tableau.py

at the

```
def insert_word():

 if left:
        w = [i for i in reversed(w)]
    res = self
    for i in w:
        res = res.schensted_insert(i,left=left)
    return res
```


the left= parameter on insert word has no effect as the following code shows:


```
T=Tableau([])
w = [2,1,1,3,2,4]
print T.insert_word(w)
T=Tableau([])
print T.insert_word(w,left=True)
T=Tableau([])
print T.insert_word(w,left=False)
```

printing

```
[[1, 1, 2, 4], [2, 3]]
[[1, 1, 2, 4], [2, 3]]
[[1, 1, 2, 4], [2, 3]]
```

which is the correct result of right row-insertion for Schensted's algorithm but left-insertion is broken.

The problem lies on the left=left on the inner call, which should be 

*res = res.schensted_insert(i,left=False)  *

The background is this (ref: William, Fulton. Young Tableaux. Cambridge University Press)

A "left" insertion  a -> b -> c  (starting with c)
is equivalent to right insertion  a <- b <- c  (starting with a)

therefore the lines

```
 if left:
        w = [i for i in reversed(w)]
```

are *correctly transforming* the left insertion into a right one by reversing the insertion order .

However, left=left  is an error, shoud be left=False since it's already converted into a right insertion, and so:

setting left=True will exchange the meanings of left-right insertions, since the reversal already turned the column-insertion into row-insertion  (kind of like "negative-negative" cancelling)
and the result is that calling left=False on insert_word will give the left result and    left=True  will give the right one!!

The correct code, therefore is


```
def insert_word():

 if left:
        w = [i for i in reversed(w)]
    res = self
    for i in w:
        res = res.schensted_insert(i,left=False)
    return res
```


which would give the correct results:

```
w = [2,1,1,3,2,4]
T=Tableau([]); print insertar(T, w)
T=Tableau([]); print insertar(T, w,left=False)
T=Tableau([]); print insertar(T, w,left=True)
```


(insertar is an alias I made for testing) and would then print:

```
[[1, 1, 2, 4], [2, 3]]
[[1, 1, 2, 4], [2, 3]]
[[1, 1, 2], [2, 3], [4]]
```

default call : CORRECT (right insertion) 

explicit right insertion : CORRECT 

explicit left insertion : CORRECT 

whereas setting  res = res.schensted_insert(i,left=True)
would give

```
[[1, 1, 2], [2, 3], [4]]
[[1, 1, 2], [2, 3], [4]]
[[1, 1, 2, 4], [2, 3]]
```

default call : left-insertion WRONG! 

explicit right insertion : WRONG! (it gave the left one) 

explicit left insertion : WRONG! (it gave the right  one)

Notice also that setting left=True affects the default case.

*Conclusion*

```
res = res.schensted_insert(i,left=left) 
```


should be changed to

```
res = res.schensted_insert(i,left=False) 
```


This is first bug I send, so I apologize if I don't fill correctly the values below


---

Comment by jbandlow created at 2011-03-28 17:24:36

The left=True parameter does have an effect. One can compare:


```
    sage: t = Tableau([[2, 3], [3]])
    sage: w = [1, 1, 3, 3]
    sage: t.insert_word(w)
    [[1, 1, 3, 3], [2, 3], [3]]
    sage: t.insert_word(w, left=True)
    [[1, 1, 2, 3, 3, 3], [3]]
```


The latter is returning the result of Schensted inserting the concatenation of the words w and the reading word of t (in that order). This operation is used in the code for katabolism (and possibly elsewhere), and reflects multiplication in the plactic monoid.


---

Comment by jpswanson created at 2015-03-20 00:03:04

Changing status from new to needs_review.


---

Comment by jpswanson created at 2015-03-20 00:03:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-03-21 09:30:26

Resolution: invalid
