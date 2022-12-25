# Issue 8322: on sage.combinat.tableau.insert_word() , parameter left= is broken   (fix provided)

archive/issues_008322.json:
```json
{
    "body": "Assignee: somebody\n\non\n/usr/local/sage2/local/lib/python2.6/site-packages/sage/combinat/tableau.py\n\nat the\n\n```\ndef insert_word():\n\n if left:\n        w = [i for i in reversed(w)]\n    res = self\n    for i in w:\n        res = res.schensted_insert(i,left=left)\n    return res\n```\n\n\nthe left= parameter on insert word has no effect as the following code shows:\n\n\n```\nT=Tableau([])\nw = [2,1,1,3,2,4]\nprint T.insert_word(w)\nT=Tableau([])\nprint T.insert_word(w,left=True)\nT=Tableau([])\nprint T.insert_word(w,left=False)\n```\n\nprinting\n\n```\n[[1, 1, 2, 4], [2, 3]]\n[[1, 1, 2, 4], [2, 3]]\n[[1, 1, 2, 4], [2, 3]]\n```\n\nwhich is the correct result of right row-insertion for Schensted's algorithm but left-insertion is broken.\n\nThe problem lies on the left=left on the inner call, which should be \n\n**res = res.schensted_insert(i,left=False)  **\n\nThe background is this (ref: William, Fulton. Young Tableaux. Cambridge University Press)\n\nA \"left\" insertion  a -> b -> c  (starting with c)\nis equivalent to right insertion  a <- b <- c  (starting with a)\n\ntherefore the lines\n\n```\n if left:\n        w = [i for i in reversed(w)]\n```\n\nare **correctly transforming** the left insertion into a right one by reversing the insertion order .\n\nHowever, left=left  is an error, shoud be left=False since it's already converted into a right insertion, and so:\n\nsetting left=True will exchange the meanings of left-right insertions, since the reversal already turned the column-insertion into row-insertion  (kind of like \"negative-negative\" cancelling)\nand the result is that calling left=False on insert_word will give the left result and    left=True  will give the right one!!\n\nThe correct code, therefore is\n\n\n```\ndef insert_word():\n\n if left:\n        w = [i for i in reversed(w)]\n    res = self\n    for i in w:\n        res = res.schensted_insert(i,left=False)\n    return res\n```\n\n\nwhich would give the correct results:\n\n```\nw = [2,1,1,3,2,4]\nT=Tableau([]); print insertar(T, w)\nT=Tableau([]); print insertar(T, w,left=False)\nT=Tableau([]); print insertar(T, w,left=True)\n```\n\n\n(insertar is an alias I made for testing) and would then print:\n\n```\n[[1, 1, 2, 4], [2, 3]]\n[[1, 1, 2, 4], [2, 3]]\n[[1, 1, 2], [2, 3], [4]]\n```\n\ndefault call : CORRECT (right insertion) \n\nexplicit right insertion : CORRECT \n\nexplicit left insertion : CORRECT \n\nwhereas setting  res = res.schensted_insert(i,left=True)\nwould give\n\n```\n[[1, 1, 2], [2, 3], [4]]\n[[1, 1, 2], [2, 3], [4]]\n[[1, 1, 2, 4], [2, 3]]\n```\n\ndefault call : left-insertion WRONG! \n\nexplicit right insertion : WRONG! (it gave the left one) \n\nexplicit left insertion : WRONG! (it gave the right  one)\n\nNotice also that setting left=True affects the default case.\n\n**Conclusion**\n\n```\nres = res.schensted_insert(i,left=left) \n```\n\n\nshould be changed to\n\n```\nres = res.schensted_insert(i,left=False) \n```\n\n\nThis is first bug I send, so I apologize if I don't fill correctly the values below\n\nIssue created by migration from https://trac.sagemath.org/ticket/8322\n\n",
    "created_at": "2010-02-22T00:41:13Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "on sage.combinat.tableau.insert_word() , parameter left= is broken   (fix provided)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8322",
    "user": "https://trac.sagemath.org/admin/accounts/users/drini"
}
```
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

**res = res.schensted_insert(i,left=False)  **

The background is this (ref: William, Fulton. Young Tableaux. Cambridge University Press)

A "left" insertion  a -> b -> c  (starting with c)
is equivalent to right insertion  a <- b <- c  (starting with a)

therefore the lines

```
 if left:
        w = [i for i in reversed(w)]
```

are **correctly transforming** the left insertion into a right one by reversing the insertion order .

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

**Conclusion**

```
res = res.schensted_insert(i,left=left) 
```


should be changed to

```
res = res.schensted_insert(i,left=False) 
```


This is first bug I send, so I apologize if I don't fill correctly the values below

Issue created by migration from https://trac.sagemath.org/ticket/8322





---

archive/issue_comments_073737.json:
```json
{
    "body": "The left=True parameter does have an effect. One can compare:\n\n\n```\n    sage: t = Tableau([[2, 3], [3]])\n    sage: w = [1, 1, 3, 3]\n    sage: t.insert_word(w)\n    [[1, 1, 3, 3], [2, 3], [3]]\n    sage: t.insert_word(w, left=True)\n    [[1, 1, 2, 3, 3, 3], [3]]\n```\n\n\nThe latter is returning the result of Schensted inserting the concatenation of the words w and the reading word of t (in that order). This operation is used in the code for katabolism (and possibly elsewhere), and reflects multiplication in the plactic monoid.",
    "created_at": "2011-03-28T17:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8322#issuecomment-73737",
    "user": "https://github.com/jbandlow"
}
```

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

archive/issue_comments_073738.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-20T00:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8322#issuecomment-73738",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpswanson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073739.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-20T00:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8322#issuecomment-73739",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpswanson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008515.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-03-21T09:30:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8322#event-8515"
}
```



---

archive/issue_comments_073740.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2015-03-21T09:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8322#issuecomment-73740",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
