# Issue 4906: convert sage.combinat.* docstrings to Sphinx

archive/issues_004906.json:
```json
{
    "body": "Assignee: tba\n\nCC:  ddrake@member.ams.org\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4906\n\n",
    "created_at": "2009-01-01T22:47:01Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "convert sage.combinat.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4906",
    "user": "mhansen"
}
```
Assignee: tba

CC:  ddrake@member.ams.org



Issue created by migration from https://trac.sagemath.org/ticket/4906





---

archive/issue_comments_037224.json:
```json
{
    "body": "Patch at http://sage.math.washington.edu/home/mhansen/trac_4906.patch",
    "created_at": "2009-01-02T03:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37224",
    "user": "mhansen"
}
```

Patch at http://sage.math.washington.edu/home/mhansen/trac_4906.patch



---

archive/issue_comments_037225.json:
```json
{
    "body": "I looked at the html of the designs_incidence structures, latin squares and root systems code stuff and didn't see any problems. The patch is seaparate and not in the trac system though, so it is harder to read.",
    "created_at": "2009-01-02T11:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37225",
    "user": "wdj"
}
```

I looked at the html of the designs_incidence structures, latin squares and root systems code stuff and didn't see any problems. The patch is seaparate and not in the trac system though, so it is harder to read.



---

archive/issue_comments_037226.json:
```json
{
    "body": "Thanks for looking at those.  The patch is 2mb so it's a little more than Trac wants to handle :-)",
    "created_at": "2009-01-02T11:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37226",
    "user": "mhansen"
}
```

Thanks for looking at those.  The patch is 2mb so it's a little more than Trac wants to handle :-)



---

archive/issue_comments_037227.json:
```json
{
    "body": "in the function overlap_partition of the file word.py, the paragraph\n\n-            These three couples correspond to the pairs of letters one above \n-            the other in the following overlap :\n-                    cheval\n-                       abcdef\n-            The symmetric, reflexive and transitive closure of $R_{u,v,d}$\n\nbecame\n\n+        These three couples correspond to the pairs of letters one above\n+        the other in the following overlap : cheval abcdef The symmetric,\n+        reflexive and transitive closure of `R_{u,v,d}` defines\n+        the following partition of the alphabet `A`:\n+        `\\{\\{a, b, v\\}, \\{c, l\\}, \\{d\\}, \\{e\\}, \\{f\\}, \\{h\\}\\}`.\n\nbut I would prefer\n\n+        These three couples correspond to the pairs of letters one above\n+        the other in the following overlap : \n+              cheval \n+                 abcdef \n+        The symmetric, reflexive and transitive closure of `R_{u,v,d}` defines\n+        the following partition of the alphabet `A`:\n+        `\\{\\{a, b, v\\}, \\{c, l\\}, \\{d\\}, \\{e\\}, \\{f\\}, \\{h\\}\\}`.\n\nmaybe there is a better solution using the new functionalities of REST?",
    "created_at": "2009-01-04T02:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37227",
    "user": "slabbe"
}
```

in the function overlap_partition of the file word.py, the paragraph

-            These three couples correspond to the pairs of letters one above 
-            the other in the following overlap :
-                    cheval
-                       abcdef
-            The symmetric, reflexive and transitive closure of $R_{u,v,d}$

became

+        These three couples correspond to the pairs of letters one above
+        the other in the following overlap : cheval abcdef The symmetric,
+        reflexive and transitive closure of `R_{u,v,d}` defines
+        the following partition of the alphabet `A`:
+        `\{\{a, b, v\}, \{c, l\}, \{d\}, \{e\}, \{f\}, \{h\}\}`.

but I would prefer

+        These three couples correspond to the pairs of letters one above
+        the other in the following overlap : 
+              cheval 
+                 abcdef 
+        The symmetric, reflexive and transitive closure of `R_{u,v,d}` defines
+        the following partition of the alphabet `A`:
+        `\{\{a, b, v\}, \{c, l\}, \{d\}, \{e\}, \{f\}, \{h\}\}`.

maybe there is a better solution using the new functionalities of REST?



---

archive/issue_comments_037228.json:
```json
{
    "body": "in the function overlap_partition of the file word.py, the paragraph \n\n\n```\n-            These three couples correspond to the pairs of letters one above \n-            the other in the following overlap :\n-                    cheval\n-                       abcdef\n-            The symmetric, reflexive and transitive closure of $R_{u,v,d}$\n-            defines the following partition of the alphabet $A$:\n-            $\\{\\{a, b, v\\}, \\{c, l\\}, \\{d\\}, \\{e\\}, \\{f\\}, \\{h\\}\\}$.\n```\n\n\nbecame \n\n\n```\n+        These three couples correspond to the pairs of letters one above\n+        the other in the following overlap : cheval abcdef The symmetric,\n+        reflexive and transitive closure of `R_{u,v,d}` defines\n+        the following partition of the alphabet `A`:\n+        `\\{\\{a, b, v\\}, \\{c, l\\}, \\{d\\}, \\{e\\}, \\{f\\}, \\{h\\}\\}`.\n```\n\n\nbut I would prefer \n\n\n```\n+        These three couples correspond to the pairs of letters one above\n+        the other in the following overlap : \n+             cheval \n+                abcdef \n+        The symmetric, reflexive and transitive closure of `R_{u,v,d}` defines\n+        the following partition of the alphabet `A`:\n+        `\\{\\{a, b, v\\}, \\{c, l\\}, \\{d\\}, \\{e\\}, \\{f\\}, \\{h\\}\\}`.\n```\n\n\nmaybe there is a better solution using the new functionalities of REST?",
    "created_at": "2009-01-04T02:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37228",
    "user": "slabbe"
}
```

in the function overlap_partition of the file word.py, the paragraph 


```
-            These three couples correspond to the pairs of letters one above 
-            the other in the following overlap :
-                    cheval
-                       abcdef
-            The symmetric, reflexive and transitive closure of $R_{u,v,d}$
-            defines the following partition of the alphabet $A$:
-            $\{\{a, b, v\}, \{c, l\}, \{d\}, \{e\}, \{f\}, \{h\}\}$.
```


became 


```
+        These three couples correspond to the pairs of letters one above
+        the other in the following overlap : cheval abcdef The symmetric,
+        reflexive and transitive closure of `R_{u,v,d}` defines
+        the following partition of the alphabet `A`:
+        `\{\{a, b, v\}, \{c, l\}, \{d\}, \{e\}, \{f\}, \{h\}\}`.
```


but I would prefer 


```
+        These three couples correspond to the pairs of letters one above
+        the other in the following overlap : 
+             cheval 
+                abcdef 
+        The symmetric, reflexive and transitive closure of `R_{u,v,d}` defines
+        the following partition of the alphabet `A`:
+        `\{\{a, b, v\}, \{c, l\}, \{d\}, \{e\}, \{f\}, \{h\}\}`.
```


maybe there is a better solution using the new functionalities of REST?



---

archive/issue_comments_037229.json:
```json
{
    "body": "In the wordmorphism file, was the following change wanted?\n\n\n```\n-            \n-        Use the arrows ('->') correctly:\n+        \n+        Use the arrows ('-') correctly::\n+        \n             sage: WordMorphism('a->ab,b-')\n             Traceback (most recent call last):\n             ...\n@@ -63,38 +72,50 @@\n             Traceback (most recent call last):\n             ...\n             ValueError: The second and third characters must be '->' (not '-]')\n```\n",
    "created_at": "2009-01-04T02:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37229",
    "user": "slabbe"
}
```

In the wordmorphism file, was the following change wanted?


```
-            
-        Use the arrows ('->') correctly:
+        
+        Use the arrows ('-') correctly::
+        
             sage: WordMorphism('a->ab,b-')
             Traceback (most recent call last):
             ...
@@ -63,38 +72,50 @@
             Traceback (most recent call last):
             ...
             ValueError: The second and third characters must be '->' (not '-]')
```




---

archive/issue_comments_037230.json:
```json
{
    "body": "I quickly look at some of the changes in some of the words library files. I saw two possible problems that I wrote above.\n\nSometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?\n\nClearly, this is a very good improvement to the documentation.\n\nslabbe",
    "created_at": "2009-01-04T03:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37230",
    "user": "slabbe"
}
```

I quickly look at some of the changes in some of the words library files. I saw two possible problems that I wrote above.

Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?

Clearly, this is a very good improvement to the documentation.

slabbe



---

archive/issue_comments_037231.json:
```json
{
    "body": "Replying to [comment:7 slabbe]:\n> Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?\n\nYes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.",
    "created_at": "2009-01-04T03:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37231",
    "user": "mhansen"
}
```

Replying to [comment:7 slabbe]:
> Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?

Yes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.



---

archive/issue_comments_037232.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> Replying to [comment:7 slabbe]:\n> > Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?\n> \n> Yes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.\n\nOk, so if you want to do some of those tonigh, by memory, I would tell you to look at the constructor of WordMorphism, __pow__ of word.py and __call__ of WordMorphism.",
    "created_at": "2009-01-04T03:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37232",
    "user": "slabbe"
}
```

Replying to [comment:8 mhansen]:
> Replying to [comment:7 slabbe]:
> > Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?
> 
> Yes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.

Ok, so if you want to do some of those tonigh, by memory, I would tell you to look at the constructor of WordMorphism, __pow__ of word.py and __call__ of WordMorphism.



---

archive/issue_comments_037233.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-21T19:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37233",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_037234.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-22T03:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37234",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_037235.json:
```json
{
    "body": "I've posted a tiny fix to make doctests pass in sage.combinat.* after sphinxification.  (Oops, typed in the wrong box before.)",
    "created_at": "2009-02-22T03:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37235",
    "user": "cwitty"
}
```

I've posted a tiny fix to make doctests pass in sage.combinat.* after sphinxification.  (Oops, typed in the wrong box before.)



---

archive/issue_comments_037236.json:
```json
{
    "body": "I've been through the file from `alternating_sign_matrix.py`\nto `sage/combinat/graph_path.py` in alphabetic order and from `species/characteristic_species.py` to `yamanouchi.py`. \n\nHere is my list of corrections:\n\n\n```\nFile alternating_sign_matrix.py\n===============================\n* Function_next_column_iterator: typo \nReturns a generator for all columbs of height height properly\n                            columns\n\t\t\t    \n\nFile choose_nk.py\n=================\n*  function _comb_largest(a,b,x): The < are missing. \n-    Returns the largest w < a such that binomial(w,b) <= x.\n+    Returns the largest w a such that binomial(w,b) = x.\n\n\nFile combinat.py\n=================\n\nIn the web page, the Integrated patch about Bell's polynomial still contains\nlatex command (Ticket #5109) in particular: \n$$ B_{n,k}(x_1, x_2, ldots, x_{n-k+1}) = sum_{sum{j_i}=k, sum{i j_i} =n}\nfrac{n!}{j_1!j_2!ldots} frac{x_1}{1!}^j_1 frac{x_2}{2!}^j_2 ldots $$\n\n* Function unordered_tuples: typo\n+    An unordered tuple of length k of set is a unordered selection with\n                                              an\n\nFile composition.py\n===================\n\nThe definition of Peak is wrong. This is the definition for permutations.\n         The peaks are the positions i in the compositions such that\n-        self[i-1] < self[i] > self[i+1].  Note that len(self)-1 is\n-        never a peak.\n\nThe peaks of a composition are the descents which does not imediately follows\nanother descent. The function seems to be also completely wrong: in mupad we\nhad: \n>> compositions::peaks([1, 1, 3, 1, 2, 1, 3])\n  [5, 8]\n\nFile crystals.py\n================\n* class FastCrystal: The < are missing. \n-    integral. It is assumed that l1 >= l2 >= 0.  If l1\n+    integral. It is assumed that l1 = l2 = 0. If l1 and l2 are\n\n* class CrystalOfTableaux: The < are missing.\n-    a partition of length <= type[1]. Produces a classical crystal with\n+    partition of length = type[1]. Produces a classical crystal with\n\nFile designs/incidence_structures.py\n====================================\n\n* function block_design_checker: Misspelled argnument name:\n-            lmbda - each t-tuple of points should be incident with lmda blocks\n+            lmbda - each t-tuple of points should be incident with lmbda blocks\n\n* The doc after __init__ do not appear in the compiled doc. Is it normal ?\n\nFile dlx.py\n===========\n\n* In the doc all the matrices have been smashed eg:\n-            [\n-             [1, [i_11,i_12,...,i_1r]]\n-             ...\n-             [m, [i_m1,i_m2,...,i_ms]]\n-            ]\n-        where M[j][i_jk] = 1. \nis now\n[ [1, [i_11,i_12,...,i_1r]] ... [m,\n+        [i_m1,i_m2,...,i_ms]] ] where M[j][i_jk] = 1.\n\nAnd later on:\n-            1110\n-            1010\n-            0100\n-            0001\n-\n+        \n+        1110 1010 0100 0001\n+        \nThis is no more readable.\n\n* same remark on the code of _covercolumn:\n* same remark on the code of _uncovercolumn:\n\n\nfile matrices/dlxcpp.p\n======================\nSame problem as dlx.py. (actually the doc is the same, there should be a link\nrather than a copy paste). \n\n\n\nFile free_module.py\n===================\n\n* function _apply_module_morphism: Strange quotes. \n         INPUT:\n-            -- x : a element of self\n-            -- f : a function that takes in a combinatorial object\n+        -   x : a element of self\n+        \n+        -```` - f : a function that takes in a combinatorial\n          ^^^^\n\nFile matrices/latin.py\n======================\n\n* The main doc seems to have been removed !!! :\n-Latin squares\n-\n-A {\\it latin square} of order $n$ is an $n \\times n$ array such that\n[... one page removed] \n-TESTS:\n-    sage: L = elementary_abelian_2group(3)\n-    sage: L == loads(dumps(L))\n-    True\n+Latin Squares\n\n* function __init__: missing comparison sign : < \n-        at row r, column c is empty if and only if L[r, c] < 0. In this \n+        if L[r, c] 0. In this way we allow partial latin squares and can\n\n\n* function actual_row_col_sym_sizes: Please keep the brackets. \n-        {0, 1, ..., m} (no holes in that list).\n+           0, 1, ..., m (no holes in that list).\n\n* function filled_cells_map: Please keep the braclets:\n-        Number the filled cells of self with integers from {1, 2, 3, ...}.\n+        Number the filled cells of self with integers from 1, 2, 3, ....\n\n\t  \nFile integer_list.py\n====================\n\n* function comp2floor: there is a missing arrow:\n-    Given a composition, returns the lowest regular function N->N above\n+    Given a composition, returns the lowest regular function N-N above\n\n* same in comp2ceil:\n-    Given a composition, returns the lowest regular function N->N below\n+    Given a composition, returns the lowest regular function N-N below\n\n\n\nFile integer_vector.py\n======================\n\n* class class IntegerVectors_nnondescents: the itemize should be kept:\n-    The combinatorial class of integer vectors v graded by two parameters:\n-     - n: the sum of the parts of v\n-     - comp: the non descents composition of v\n+    The combinatorial class of integer vectors v graded by two\n+    parameters: - n: the sum of the parts of v - comp: the non descents\n+    composition of v\n\n* missing arrow:\n-    maximal (for the natural left->right reading) in their orbit by the\n+    maximal (for the natural left-right reading) in their orbit by the\n\n\nFile species/series.py:\n=======================\n\ndef _power_gen(self): The exponent is missing\n-        Returns a generator for all the powers self^k starting with\n+        Returns a generator for all the powers selfk starting with k = 1.\n\n\nFile species/structure.py\n==========================\n* Main doc: In the equation the \"|\" should not be lost !\n-BB = o + o*BB + o*|*BB\n+BB = o + o\\*BB + o\\*\\*BB\n\n\nFile tableau.py\n===============\n\n* function descents: Missing comparison sign\n\n-        Returns a list of the boxes (i,j) such that\n-        self[i][j] > self[i-1][j].\n+        Returns a list of the boxes (i,j) such that self[i][j]\n+        self[i-1][j].\n\nwords/morphism.py\n=================\n\n* class WordMorphism: missing > \n-        Use the arrows ('->') correctly:\n+        Use the arrows ('-') correctly::\n\n\nwords/suffix_trees.py\n* function __init__: The presentation should be kept:\n-        function t is defined as\n-                t(-1,a) = 0 for all letters a; and\n-                t(x',a) = y' for all x',y' \\in Q such that y = xa,\n-        and the suffix link function is defined as\n-                suffix_link(0) = -1;\n-                suffix_link(x') = y', if x = ay for some letter a.\n+        purposes of the algorithm, there is also an auxiliary state -1. The\n+        transition function t is defined as t(-1,a) = 0 for all letters a;\n+        and t(x',a) = y' for all x',y' Q such that y = xa, and the suffix\n+        link function is defined as suffix_link(0) = -1; suffix_link(x')\n+        = y', if x = ay for some letter a.\n\n* function _find_transition: the bracket should be kept (python code):\n-            ._transition_function = {..., node: {(i,j): target_node, ...} }\n+        ._transition_function = ..., node: (i,j): target_node, ...\n\n\nwords/word.py\n=============\n\n* function swap_increase: missing comparison sign:\n-        Returns the word with positions i and i+1 exchanged\n-        if self[i] > self[i+1]. Otherwise, it returns self.\n+        Returns the word with positions i and i+1 exchanged if self[i]\n+        self[i+1]. Otherwise, it returns self.\n\n* same for function swap_decrease.\n```\n",
    "created_at": "2009-02-23T22:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37236",
    "user": "hivert"
}
```

I've been through the file from `alternating_sign_matrix.py`
to `sage/combinat/graph_path.py` in alphabetic order and from `species/characteristic_species.py` to `yamanouchi.py`. 

Here is my list of corrections:


```
File alternating_sign_matrix.py
===============================
* Function_next_column_iterator: typo 
Returns a generator for all columbs of height height properly
                            columns
			    

File choose_nk.py
=================
*  function _comb_largest(a,b,x): The < are missing. 
-    Returns the largest w < a such that binomial(w,b) <= x.
+    Returns the largest w a such that binomial(w,b) = x.


File combinat.py
=================

In the web page, the Integrated patch about Bell's polynomial still contains
latex command (Ticket #5109) in particular: 
$$ B_{n,k}(x_1, x_2, ldots, x_{n-k+1}) = sum_{sum{j_i}=k, sum{i j_i} =n}
frac{n!}{j_1!j_2!ldots} frac{x_1}{1!}^j_1 frac{x_2}{2!}^j_2 ldots $$

* Function unordered_tuples: typo
+    An unordered tuple of length k of set is a unordered selection with
                                              an

File composition.py
===================

The definition of Peak is wrong. This is the definition for permutations.
         The peaks are the positions i in the compositions such that
-        self[i-1] < self[i] > self[i+1].  Note that len(self)-1 is
-        never a peak.

The peaks of a composition are the descents which does not imediately follows
another descent. The function seems to be also completely wrong: in mupad we
had: 
>> compositions::peaks([1, 1, 3, 1, 2, 1, 3])
  [5, 8]

File crystals.py
================
* class FastCrystal: The < are missing. 
-    integral. It is assumed that l1 >= l2 >= 0.  If l1
+    integral. It is assumed that l1 = l2 = 0. If l1 and l2 are

* class CrystalOfTableaux: The < are missing.
-    a partition of length <= type[1]. Produces a classical crystal with
+    partition of length = type[1]. Produces a classical crystal with

File designs/incidence_structures.py
====================================

* function block_design_checker: Misspelled argnument name:
-            lmbda - each t-tuple of points should be incident with lmda blocks
+            lmbda - each t-tuple of points should be incident with lmbda blocks

* The doc after __init__ do not appear in the compiled doc. Is it normal ?

File dlx.py
===========

* In the doc all the matrices have been smashed eg:
-            [
-             [1, [i_11,i_12,...,i_1r]]
-             ...
-             [m, [i_m1,i_m2,...,i_ms]]
-            ]
-        where M[j][i_jk] = 1. 
is now
[ [1, [i_11,i_12,...,i_1r]] ... [m,
+        [i_m1,i_m2,...,i_ms]] ] where M[j][i_jk] = 1.

And later on:
-            1110
-            1010
-            0100
-            0001
-
+        
+        1110 1010 0100 0001
+        
This is no more readable.

* same remark on the code of _covercolumn:
* same remark on the code of _uncovercolumn:


file matrices/dlxcpp.p
======================
Same problem as dlx.py. (actually the doc is the same, there should be a link
rather than a copy paste). 



File free_module.py
===================

* function _apply_module_morphism: Strange quotes. 
         INPUT:
-            -- x : a element of self
-            -- f : a function that takes in a combinatorial object
+        -   x : a element of self
+        
+        -```` - f : a function that takes in a combinatorial
          ^^^^

File matrices/latin.py
======================

* The main doc seems to have been removed !!! :
-Latin squares
-
-A {\it latin square} of order $n$ is an $n \times n$ array such that
[... one page removed] 
-TESTS:
-    sage: L = elementary_abelian_2group(3)
-    sage: L == loads(dumps(L))
-    True
+Latin Squares

* function __init__: missing comparison sign : < 
-        at row r, column c is empty if and only if L[r, c] < 0. In this 
+        if L[r, c] 0. In this way we allow partial latin squares and can


* function actual_row_col_sym_sizes: Please keep the brackets. 
-        {0, 1, ..., m} (no holes in that list).
+           0, 1, ..., m (no holes in that list).

* function filled_cells_map: Please keep the braclets:
-        Number the filled cells of self with integers from {1, 2, 3, ...}.
+        Number the filled cells of self with integers from 1, 2, 3, ....

	  
File integer_list.py
====================

* function comp2floor: there is a missing arrow:
-    Given a composition, returns the lowest regular function N->N above
+    Given a composition, returns the lowest regular function N-N above

* same in comp2ceil:
-    Given a composition, returns the lowest regular function N->N below
+    Given a composition, returns the lowest regular function N-N below



File integer_vector.py
======================

* class class IntegerVectors_nnondescents: the itemize should be kept:
-    The combinatorial class of integer vectors v graded by two parameters:
-     - n: the sum of the parts of v
-     - comp: the non descents composition of v
+    The combinatorial class of integer vectors v graded by two
+    parameters: - n: the sum of the parts of v - comp: the non descents
+    composition of v

* missing arrow:
-    maximal (for the natural left->right reading) in their orbit by the
+    maximal (for the natural left-right reading) in their orbit by the


File species/series.py:
=======================

def _power_gen(self): The exponent is missing
-        Returns a generator for all the powers self^k starting with
+        Returns a generator for all the powers selfk starting with k = 1.


File species/structure.py
==========================
* Main doc: In the equation the "|" should not be lost !
-BB = o + o*BB + o*|*BB
+BB = o + o\*BB + o\*\*BB


File tableau.py
===============

* function descents: Missing comparison sign

-        Returns a list of the boxes (i,j) such that
-        self[i][j] > self[i-1][j].
+        Returns a list of the boxes (i,j) such that self[i][j]
+        self[i-1][j].

words/morphism.py
=================

* class WordMorphism: missing > 
-        Use the arrows ('->') correctly:
+        Use the arrows ('-') correctly::


words/suffix_trees.py
* function __init__: The presentation should be kept:
-        function t is defined as
-                t(-1,a) = 0 for all letters a; and
-                t(x',a) = y' for all x',y' \in Q such that y = xa,
-        and the suffix link function is defined as
-                suffix_link(0) = -1;
-                suffix_link(x') = y', if x = ay for some letter a.
+        purposes of the algorithm, there is also an auxiliary state -1. The
+        transition function t is defined as t(-1,a) = 0 for all letters a;
+        and t(x',a) = y' for all x',y' Q such that y = xa, and the suffix
+        link function is defined as suffix_link(0) = -1; suffix_link(x')
+        = y', if x = ay for some letter a.

* function _find_transition: the bracket should be kept (python code):
-            ._transition_function = {..., node: {(i,j): target_node, ...} }
+        ._transition_function = ..., node: (i,j): target_node, ...


words/word.py
=============

* function swap_increase: missing comparison sign:
-        Returns the word with positions i and i+1 exchanged
-        if self[i] > self[i+1]. Otherwise, it returns self.
+        Returns the word with positions i and i+1 exchanged if self[i]
+        self[i+1]. Otherwise, it returns self.

* same for function swap_decrease.
```




---

archive/issue_comments_037237.json:
```json
{
    "body": "My corrections for files between integer_list.py and permutations_nk.py (included) are in :\n   http://iml.univ-mrs.fr/~delecroi/rest_corrections",
    "created_at": "2009-02-23T23:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37237",
    "user": "vdelecroix"
}
```

My corrections for files between integer_list.py and permutations_nk.py (included) are in :
   http://iml.univ-mrs.fr/~delecroi/rest_corrections



---

archive/issue_comments_037238.json:
```json
{
    "body": "In `dyck_word.py`:\n\n> The bouncing ball will strike the diagonal at places $(0, 0), (j_1, j_1), (j_2, j_2), ... ,(j_r-1, j_r-1), (j_r, j_r) = (n, n)$.\n\nThe dollar signs are showing.\n\nIn `dlx.py`, the docstring for DLXMatrix needs some work; the matrices aren't displayed correctly. The file is `dlx.py` in Sage, but seems to be [dlxcpp.py](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/matrices/dlxcpp.html) in the conversion?\n\nThis is something we may want to fix later, but the lowercase L looks like a slash; see [here](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/finite_class.html) at the top: `sage.combinat.finite_class.FiniteCombinatorialClass(l)` looks like there's a slash between the parentheses. Perhaps a different letter could be used?",
    "created_at": "2009-02-24T00:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37238",
    "user": "ddrake"
}
```

In `dyck_word.py`:

> The bouncing ball will strike the diagonal at places $(0, 0), (j_1, j_1), (j_2, j_2), ... ,(j_r-1, j_r-1), (j_r, j_r) = (n, n)$.

The dollar signs are showing.

In `dlx.py`, the docstring for DLXMatrix needs some work; the matrices aren't displayed correctly. The file is `dlx.py` in Sage, but seems to be [dlxcpp.py](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/matrices/dlxcpp.html) in the conversion?

This is something we may want to fix later, but the lowercase L looks like a slash; see [here](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/finite_class.html) at the top: `sage.combinat.finite_class.FiniteCombinatorialClass(l)` looks like there's a slash between the parentheses. Perhaps a different letter could be used?



---

archive/issue_comments_037239.json:
```json
{
    "body": "Comments on the patch by Nicolas",
    "created_at": "2009-02-24T00:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37239",
    "user": "nthiery"
}
```

Comments on the patch by Nicolas



---

archive/issue_comments_037240.json:
```json
{
    "body": "Attachment\n\nNew corrections concerning set_partition.py and set_partition_ordered.py:\n\n## File set_partition.py\n\n* function less: missing <\n\n```\n-    Returns True if s < t otherwise it returns False.\n+    Returns True if s t otherwise it returns False.\n```\n \n\n == File ordered_set_partition.py ==\n\n* main doc: missing brackets (twice):\n\n```\n-EXAMPLES:\n-  There are 13 ordered set partitions of {1,2,3}.\n+EXAMPLES: There are 13 ordered set partitions of 1,2,3.\n \n-  There are 12 ordered set partitions of {1,2,3,4} whose underlying\n+There are 12 ordered set partitions of 1,2,3,4 whose underlying\n```\n",
    "created_at": "2009-02-24T09:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37240",
    "user": "hivert"
}
```

Attachment

New corrections concerning set_partition.py and set_partition_ordered.py:

## File set_partition.py

* function less: missing <

```
-    Returns True if s < t otherwise it returns False.
+    Returns True if s t otherwise it returns False.
```
 

 == File ordered_set_partition.py ==

* main doc: missing brackets (twice):

```
-EXAMPLES:
-  There are 13 ordered set partitions of {1,2,3}.
+EXAMPLES: There are 13 ordered set partitions of 1,2,3.
 
-  There are 12 ordered set partitions of {1,2,3,4} whose underlying
+There are 12 ordered set partitions of 1,2,3,4 whose underlying
```




---

archive/issue_comments_037241.json:
```json
{
    "body": "New corrections by Vincent Delecroix and myself on the files:\n\n```\n sage/combinat/q_analogues.py\n sage/combinat/ranker.py\n sage/combinat/restricted_growth.py\n sage/combinat/ribbon.py\n sage/combinat/ribbon_tableau.py\n```\n\n\n\n## File ranker.py\n\n* Function from_list(l): missing \":\" after output + quote\n\n```\n+ OUTPUT [rank, unrank] - functions\n```\n\nshould be probably\n\n```\nOUTPUT ::\n     ``[rank, unrank]`` - functions\n```\n\n\n## File ribbon_tableau.py\n\n* class RibonTableau_class :: method length(): missing 's' added 'x'\n\n```\n- Returns the length of the ribbons into a ribbon tableau.\n+ Return the length of the ribbons into a ribbon tableaux.\n```\n\n* function spin_polynomial_square: missing \">\" and \"^\"\n\n```\n-    length, with the substitution t -> t^2 made.\n+    length, with the substitution t - t2 made.\n```\n\n\n## File root_system/dynkin_diagram.py\n\n* function column: composed latex subscripts seems to have been lost:\n\n```\n-        of tuples (i, a_{i,j})\n+        (or iterator) of tuples (i, a_i,j)\n]}}\nshould be probably\n{{{\n+        (or iterator) of tuples `(i, a_{i,j})`.\n}}}\n```\n\n\n* same remark for the function row\n\n\n## File root_system/weyl_characters.py\n\n* function branch_weyl_character: lots of problems:\n  - input is garlbed:\n\n```\n-    INPUT:\n-       chi - a character of G\n-       R - the Weyl Character Ring of G\n-       S - the Weyl Character Ring of H\n-       rule - a set of r dominant weights in H where r is the rank of G.\n+    INPUT: chi - a character of G R - the Weyl Character Ring of G S -\n+    the Weyl Character Ring of H rule - a set of r dominant weights in\n+    H where r is the rank of G.\n```\n\n- lots of lost > in arrows:\n\n```\n-    connected. This excludes branching rules such as A3 -> A1 x A1, which are\n+    connected. This excludes branching rules such as A3 - A1 x A1,\n```\n\n- the rule for branching type are also garbled (three series):\n\n```\n-    ['A',r] -> ['A',r-1]\n-    ['B',r] -> ['A',r-1]\n   [...]\n-    ['G',2] -> ['A',1] (short root) (not implemented yet)\n+    ['A',r] - ['A',r-1] ['B',r] - ['A',r-1] ['B',r] - ['B',r-1] ['C',r]\n+    - ['A',r-1] ['C',r] - ['C',r-1] ['D',r] - ['A',r-1] ['D',r] -\n+    ['D',r-1] ['E',r] - ['A',r-1] r = 6,7,8 (not implemented yet)\n+    ['E',r] - ['D',r-1] r = 6,7,8 (not implemented yet) ['E',r] -\n+    ['E',r-1] r = 6,7 (not implemented yet) ['F',4] - ['B',3] (not\n```\n\n- In the example starting with  \"Here A3(x,y,z,w) can be understood as a representation of SL(4)\": missing \">\":\n\n```\n-    square representation SL(4) --> GL(6) admits an invariant symmetric\n-    bilinear form, so is a representation SL(4) --> SO(6) that lifts to\n-    an isomorphism SL(4) --> Spin(6).  Conversely, there are two\n-    isomorphisms SO(6) --> SL(4), of which we've selected one.\n+    square representation SL(4) - GL(6) admits an invariant symmetric\n+    bilinear form, so is a representation SL(4) - SO(6) that lifts to\n+    an isomorphism SL(4) - Spin(6). Conversely, there are two\n+    isomorphisms SO(6) - SL(4), of which we've selected one.\n```\n\n\n\n## file root_system/weyl_group.py\n\n* function WeylGroup:\n\n```\n+    INPUT: ct - a Cartan Type.\n```\n\nshould probably be\n\n```\n   INPUT::\n   \n       ``ct`` - a Cartan Type.\n```\n\n\n* function  simple_reflection: typo\n\n```\n+        Returns the `i^th` simple reflection.\n```\n\nshould be\n\n```\n+        Returns the `i`-th simple reflection.\n```\n",
    "created_at": "2009-02-24T10:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37241",
    "user": "hivert"
}
```

New corrections by Vincent Delecroix and myself on the files:

```
 sage/combinat/q_analogues.py
 sage/combinat/ranker.py
 sage/combinat/restricted_growth.py
 sage/combinat/ribbon.py
 sage/combinat/ribbon_tableau.py
```



## File ranker.py

* Function from_list(l): missing ":" after output + quote

```
+ OUTPUT [rank, unrank] - functions
```

should be probably

```
OUTPUT ::
     ``[rank, unrank]`` - functions
```


## File ribbon_tableau.py

* class RibonTableau_class :: method length(): missing 's' added 'x'

```
- Returns the length of the ribbons into a ribbon tableau.
+ Return the length of the ribbons into a ribbon tableaux.
```

* function spin_polynomial_square: missing ">" and "^"

```
-    length, with the substitution t -> t^2 made.
+    length, with the substitution t - t2 made.
```


## File root_system/dynkin_diagram.py

* function column: composed latex subscripts seems to have been lost:

```
-        of tuples (i, a_{i,j})
+        (or iterator) of tuples (i, a_i,j)
]}}
should be probably
{{{
+        (or iterator) of tuples `(i, a_{i,j})`.
}}}
```


* same remark for the function row


## File root_system/weyl_characters.py

* function branch_weyl_character: lots of problems:
  - input is garlbed:

```
-    INPUT:
-       chi - a character of G
-       R - the Weyl Character Ring of G
-       S - the Weyl Character Ring of H
-       rule - a set of r dominant weights in H where r is the rank of G.
+    INPUT: chi - a character of G R - the Weyl Character Ring of G S -
+    the Weyl Character Ring of H rule - a set of r dominant weights in
+    H where r is the rank of G.
```

- lots of lost > in arrows:

```
-    connected. This excludes branching rules such as A3 -> A1 x A1, which are
+    connected. This excludes branching rules such as A3 - A1 x A1,
```

- the rule for branching type are also garbled (three series):

```
-    ['A',r] -> ['A',r-1]
-    ['B',r] -> ['A',r-1]
   [...]
-    ['G',2] -> ['A',1] (short root) (not implemented yet)
+    ['A',r] - ['A',r-1] ['B',r] - ['A',r-1] ['B',r] - ['B',r-1] ['C',r]
+    - ['A',r-1] ['C',r] - ['C',r-1] ['D',r] - ['A',r-1] ['D',r] -
+    ['D',r-1] ['E',r] - ['A',r-1] r = 6,7,8 (not implemented yet)
+    ['E',r] - ['D',r-1] r = 6,7,8 (not implemented yet) ['E',r] -
+    ['E',r-1] r = 6,7 (not implemented yet) ['F',4] - ['B',3] (not
```

- In the example starting with  "Here A3(x,y,z,w) can be understood as a representation of SL(4)": missing ">":

```
-    square representation SL(4) --> GL(6) admits an invariant symmetric
-    bilinear form, so is a representation SL(4) --> SO(6) that lifts to
-    an isomorphism SL(4) --> Spin(6).  Conversely, there are two
-    isomorphisms SO(6) --> SL(4), of which we've selected one.
+    square representation SL(4) - GL(6) admits an invariant symmetric
+    bilinear form, so is a representation SL(4) - SO(6) that lifts to
+    an isomorphism SL(4) - Spin(6). Conversely, there are two
+    isomorphisms SO(6) - SL(4), of which we've selected one.
```



## file root_system/weyl_group.py

* function WeylGroup:

```
+    INPUT: ct - a Cartan Type.
```

should probably be

```
   INPUT::
   
       ``ct`` - a Cartan Type.
```


* function  simple_reflection: typo

```
+        Returns the `i^th` simple reflection.
```

should be

```
+        Returns the `i`-th simple reflection.
```




---

archive/issue_comments_037242.json:
```json
{
    "body": "## Note for Mike\n\nThe fast re-reading seems to be done right now... Please give credit to\n Vincent Delecroix, Dan Drake, Mike Hansen, Florent Hivert, David Joyner, Sebastien Labbe, Nicolas Thiery, Carl Witty",
    "created_at": "2009-02-24T10:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37242",
    "user": "hivert"
}
```

## Note for Mike

The fast re-reading seems to be done right now... Please give credit to
 Vincent Delecroix, Dan Drake, Mike Hansen, Florent Hivert, David Joyner, Sebastien Labbe, Nicolas Thiery, Carl Witty



---

archive/issue_comments_037243.json:
```json
{
    "body": "I am changing this to needs work since the comments have not been addressed AFAIK. \n\nMike: once the patch has been updated/supplemented please change this ticket to a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T13:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37243",
    "user": "mabshoff"
}
```

I am changing this to needs work since the comments have not been addressed AFAIK. 

Mike: once the patch has been updated/supplemented please change this ticket to a positive review.

Cheers,

Michael



---

archive/issue_comments_037244.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-24T16:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37244",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_037245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37245",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037246.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4906#issuecomment-37246",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
