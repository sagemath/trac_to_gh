# Issue 7313: Very bad thing in the behaviour of search_doc

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-26 13:44:46

Assignee: tba

CC:  ddrake

Hello !!!

Out of curiosity, I tried to look for a function I knew in Sage :

```
sage: search_doc("Floyd-Warshall")
html/en/reference/sage/graphs/graph.html:5797:<dd><p>Uses the Floyd-Warshall algorithm to find a shortest weighted path
sage: search_doc("Floyd-Warshall","pair")
sage: Graph.shortest_path_all_pairs?
```


I understand the current way to look for things in the doc is to grep it, and that for some reason we may need to keep our lines short ( less than 80 characters or so ).. I also understand that finding another way to search the doc ( if there is none available already ) may be some big amount of work. Even though, this really isn't the expected behaviour of the function, and I think we should do something about it.

Nathann


---

Comment by mhansen created at 2009-10-26 17:13:09

Changing type from defect to enhancement.


---

Comment by mhansen created at 2009-10-26 17:13:09

Please use summaries that actually describe the problem.


---

Comment by mhansen created at 2009-10-26 17:13:09

Changing priority from critical to minor.


---

Comment by ncohen created at 2009-10-26 18:40:11

Got it !! I mixed Sage-devel and TRAC :-)
Sorry !


---

Comment by jhpalmieri created at 2010-01-20 04:31:34

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-20 04:31:34

Here's a patch implementing a "multiline" keyword for searches, so you can do

```
sage: print search_src('dhsw', 'betti', interact=False)

sage: print search_src('dhsw', 'betti', interact=False, multiline=True)
homology/chain_complex.py
homology/simplicial_complex.py

```

(With multiline searches, it doesn't return line numbers, just the file names.)


---

Attachment

depends on #7018


---

Comment by rossk created at 2010-01-30 13:13:58

Tested this on sage-4.3.2.alpha0 with trac_7313-multiline.patch 
(tried the patch in ticket #7018 but that had errors)

Look for occurrences of "Pseudo". We find two occurrences.

```
sage: search_src("Pseudo-")
combinat/words/word.py:2655:        -   [2] V. Anne, L.Q. Zamboni, I. Zorca, Palindromes and Pseudo-
combinat/words/word.py:2656:            Palindromes in Episturmian and Pseudo-Palindromic Infinite Words,
rings/all.py:122:# Pseudo-ring of PARI objects.
databases/compressed_storage.py:113:        Pseudo-acquisition for base's stuff that we don't
```


Next, search for a multiline ocurrence of "Pseudo-Palindromes" which should occur over lines 2655-2656 in word.py according to the last search. (Note: the 2nd line is prefixed with whitespace)


```
sage: search_src("Pseudo-Palindromes", multiline=True) # finds nothing

```


Not sure if the problem is due to the patch mentioned in #7018 needs including and updating for alpha0, or this ticket needs more work or theres something Ive missed.


---

Comment by jhpalmieri created at 2010-01-30 16:38:42

> Tested this on sage-4.3.2.alpha0 with trac_7313-multiline.patch (tried the patch in ticket #7018 but that had errors)

(The patch from #7018 is already part of 4.3.2.alpha0, which is probably why applying it gave you errors.)

Since the string "Pseudo-Palindromes" doesn't appear, I think it is correct that searching for it returns nothing.  Try this instead:

```
sage: search_src("Pseudo-", "Palindromes", multiline=True)
```

Actually, though, Pseudo- and Palindromes appear on the same line, so this isn't the best test case.  How about

```
sage: search_src("Zamboni", "Infinite")

sage: search_src("Zamboni", "Infinite", multiline=True)
combinat/words/word.py
```



---

Comment by mpatel created at 2010-01-31 02:15:01

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-31 02:15:01

Quick note: `multiline = kwds.get('multiline', False)`, etc., should also work.


---

Comment by rossk created at 2010-01-31 03:04:43

(Confirming positive review). 
Tried a number of tests, verified using egrep and all worked (including using options such as path_re and ignore_case). Representative test below. 


```
sage: search_src("Labbe",path_re=".*py") # returned a few occurences including in word.py (not shown)

sage: search_src("Pirillo",path_re=".*py") 
combinat/words/word_generators.py:753:        -   [1] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some
combinat/words/word_generators.py:756:        -   [2] J. Justin, G. Pirillo, Episturmian words and episturmian
combinat/words/word.py:2875:        -   [3] X. Droubay, J. Justin, G. Pirillo, Episturmian words and

sage: search_src("Pirillo","Labbe",path_re=".*py") # not found (on same line)

sage: search_src("Pirillo","Labbe",multiline=True,path_re=".*py") # Expect one occurence and found one.
combinat/words/word_generators.py
```



---

Comment by mpatel created at 2010-02-11 14:40:56

Resolution: fixed
