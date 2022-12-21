# Issue 4906: convert sage.combinat.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:47:01

Assignee: tba

CC:  ddrake@member.ams.org




---

Comment by mhansen created at 2009-01-02 03:04:16

Patch at http://sage.math.washington.edu/home/mhansen/trac_4906.patch


---

Comment by wdj created at 2009-01-02 11:34:28

I looked at the html of the designs_incidence structures, latin squares and root systems code stuff and didn't see any problems. The patch is seaparate and not in the trac system though, so it is harder to read.


---

Comment by mhansen created at 2009-01-02 11:41:14

Thanks for looking at those.  The patch is 2mb so it's a little more than Trac wants to handle :-)


---

Comment by slabbe created at 2009-01-04 02:48:17

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

Comment by slabbe created at 2009-01-04 02:51:51

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

Comment by slabbe created at 2009-01-04 02:58:44

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
`@``@` -63,38 +72,50 `@``@`
             Traceback (most recent call last):
             ...
             ValueError: The second and third characters must be '->' (not '-]')
```



---

Comment by slabbe created at 2009-01-04 03:06:41

I quickly look at some of the changes in some of the words library files. I saw two possible problems that I wrote above.

Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?

Clearly, this is a very good improvement to the documentation.

slabbe


---

Comment by mhansen created at 2009-01-04 03:12:50

Replying to [comment:7 slabbe]:
> Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?

Yes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.


---

Comment by slabbe created at 2009-01-04 03:20:34

Replying to [comment:8 mhansen]:
> Replying to [comment:7 slabbe]:
> > Sometimes, there are numbered enumeration that were not changed by the above patche (see for example the constructor of WordMorphism ). But maybe there is a good way to do an enumeration without writting the numbers using REST? Do we want to convert those right now also?
> 
> Yes, you can do this in ReST using #. to mark the number.  I'll post a patch which fixes some of these things later tonight.

Ok, so if you want to do some of those tonigh, by memory, I would tell you to look at the constructor of WordMorphism, __pow__ of word.py and __call__ of WordMorphism.


---

Attachment


---

Attachment


---

Comment by cwitty created at 2009-02-22 03:39:30

I've posted a tiny fix to make doctests pass in sage.combinat.* after sphinxification.  (Oops, typed in the wrong box before.)


---

Comment by hivert created at 2009-02-23 22:18:14

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

Comment by vdelecroix created at 2009-02-23 23:25:45

My corrections for files between integer_list.py and permutations_nk.py (included) are in :
   http://iml.univ-mrs.fr/~delecroi/rest_corrections


---

Comment by ddrake created at 2009-02-24 00:30:24

In `dyck_word.py`:

> The bouncing ball will strike the diagonal at places $(0, 0), (j_1, j_1), (j_2, j_2), ... ,(j_r-1, j_r-1), (j_r, j_r) = (n, n)$.

The dollar signs are showing.

In `dlx.py`, the docstring for DLXMatrix needs some work; the matrices aren't displayed correctly. The file is `dlx.py` in Sage, but seems to be [dlxcpp.py](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/matrices/dlxcpp.html) in the conversion?

This is something we may want to fix later, but the lowercase L looks like a slash; see [here](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/combinat/finite_class.html) at the top: `sage.combinat.finite_class.FiniteCombinatorialClass(l)` looks like there's a slash between the parentheses. Perhaps a different letter could be used?


---

Comment by nthiery created at 2009-02-24 00:33:20

Comments on the patch by Nicolas


---

Attachment

New corrections concerning set_partition.py and set_partition_ordered.py:

## File set_partition.py

 * function less: missing <

```
-    Returns True if s < t otherwise it returns False.
+    Returns True if s t otherwise it returns False.
}}} 

 == File ordered_set_partition.py ==

 * main doc: missing brackets (twice):
{{{
-EXAMPLES:
-  There are 13 ordered set partitions of {1,2,3}.
+EXAMPLES: There are 13 ordered set partitions of 1,2,3.
 
-  There are 12 ordered set partitions of {1,2,3,4} whose underlying
+There are 12 ordered set partitions of 1,2,3,4 whose underlying
}}}


---

Comment by hivert created at 2009-02-24 10:12:37

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

Comment by hivert created at 2009-02-24 10:31:52

## Note for Mike

The fast re-reading seems to be done right now... Please give credit to
 Vincent Delecroix, Dan Drake, Mike Hansen, Florent Hivert, David Joyner, Sebastien Labbe, Nicolas Thiery, Carl Witty


---

Comment by mabshoff created at 2009-02-24 13:37:37

I am changing this to needs work since the comments have not been addressed AFAIK. 

Mike: once the patch has been updated/supplemented please change this ticket to a positive review.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-02-24 18:37:59

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:37:59

Merged in Sage 3.4.alpha0.

Cheers,

Michael
