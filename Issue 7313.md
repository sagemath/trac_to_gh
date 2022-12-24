# Issue 7313: Very bad thing in the behaviour of search_doc

archive/issues_007313.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @dandrake\n\nHello !!!\n\nOut of curiosity, I tried to look for a function I knew in Sage :\n\n```\nsage: search_doc(\"Floyd-Warshall\")\nhtml/en/reference/sage/graphs/graph.html:5797:<dd><p>Uses the Floyd-Warshall algorithm to find a shortest weighted path\nsage: search_doc(\"Floyd-Warshall\",\"pair\")\nsage: Graph.shortest_path_all_pairs?\n```\n\n\nI understand the current way to look for things in the doc is to grep it, and that for some reason we may need to keep our lines short ( less than 80 characters or so ).. I also understand that finding another way to search the doc ( if there is none available already ) may be some big amount of work. Even though, this really isn't the expected behaviour of the function, and I think we should do something about it.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7313\n\n",
    "created_at": "2009-10-26T13:44:46Z",
    "labels": [
        "documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Very bad thing in the behaviour of search_doc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7313",
    "user": "@nathanncohen"
}
```
Assignee: tba

CC:  @dandrake

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

Issue created by migration from https://trac.sagemath.org/ticket/7313





---

archive/issue_comments_061106.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-26T17:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61106",
    "user": "@mwhansen"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_061107.json:
```json
{
    "body": "Please use summaries that actually describe the problem.",
    "created_at": "2009-10-26T17:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61107",
    "user": "@mwhansen"
}
```

Please use summaries that actually describe the problem.



---

archive/issue_comments_061108.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2009-10-26T17:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61108",
    "user": "@mwhansen"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_061109.json:
```json
{
    "body": "Got it !! I mixed Sage-devel and TRAC :-)\nSorry !",
    "created_at": "2009-10-26T18:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61109",
    "user": "@nathanncohen"
}
```

Got it !! I mixed Sage-devel and TRAC :-)
Sorry !



---

archive/issue_comments_061110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T04:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61110",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061111.json:
```json
{
    "body": "Here's a patch implementing a \"multiline\" keyword for searches, so you can do\n\n```\nsage: print search_src('dhsw', 'betti', interact=False)\n\nsage: print search_src('dhsw', 'betti', interact=False, multiline=True)\nhomology/chain_complex.py\nhomology/simplicial_complex.py\n\n```\n\n(With multiline searches, it doesn't return line numbers, just the file names.)",
    "created_at": "2010-01-20T04:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61111",
    "user": "@jhpalmieri"
}
```

Here's a patch implementing a "multiline" keyword for searches, so you can do

```
sage: print search_src('dhsw', 'betti', interact=False)

sage: print search_src('dhsw', 'betti', interact=False, multiline=True)
homology/chain_complex.py
homology/simplicial_complex.py

```

(With multiline searches, it doesn't return line numbers, just the file names.)



---

archive/issue_comments_061112.json:
```json
{
    "body": "Attachment [trac_7313-multiline.patch](tarball://root/attachments/some-uuid/ticket7313/trac_7313-multiline.patch) by @jhpalmieri created at 2010-01-20 04:35:14\n\ndepends on #7018",
    "created_at": "2010-01-20T04:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61112",
    "user": "@jhpalmieri"
}
```

Attachment [trac_7313-multiline.patch](tarball://root/attachments/some-uuid/ticket7313/trac_7313-multiline.patch) by @jhpalmieri created at 2010-01-20 04:35:14

depends on #7018



---

archive/issue_comments_061113.json:
```json
{
    "body": "Tested this on sage-4.3.2.alpha0 with trac_7313-multiline.patch \n(tried the patch in ticket #7018 but that had errors)\n\nLook for occurrences of \"Pseudo\". We find two occurrences.\n\n```\nsage: search_src(\"Pseudo-\")\ncombinat/words/word.py:2655:        -   [2] V. Anne, L.Q. Zamboni, I. Zorca, Palindromes and Pseudo-\ncombinat/words/word.py:2656:            Palindromes in Episturmian and Pseudo-Palindromic Infinite Words,\nrings/all.py:122:# Pseudo-ring of PARI objects.\ndatabases/compressed_storage.py:113:        Pseudo-acquisition for base's stuff that we don't\n```\n\n\nNext, search for a multiline ocurrence of \"Pseudo-Palindromes\" which should occur over lines 2655-2656 in word.py according to the last search. (Note: the 2nd line is prefixed with whitespace)\n\n\n```\nsage: search_src(\"Pseudo-Palindromes\", multiline=True) # finds nothing\n\n```\n\n\nNot sure if the problem is due to the patch mentioned in #7018 needs including and updating for alpha0, or this ticket needs more work or theres something Ive missed.",
    "created_at": "2010-01-30T13:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61113",
    "user": "rossk"
}
```

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

archive/issue_comments_061114.json:
```json
{
    "body": "> Tested this on sage-4.3.2.alpha0 with trac_7313-multiline.patch (tried the patch in ticket #7018 but that had errors)\n\n(The patch from #7018 is already part of 4.3.2.alpha0, which is probably why applying it gave you errors.)\n\nSince the string \"Pseudo-Palindromes\" doesn't appear, I think it is correct that searching for it returns nothing.  Try this instead:\n\n```\nsage: search_src(\"Pseudo-\", \"Palindromes\", multiline=True)\n```\n\nActually, though, Pseudo- and Palindromes appear on the same line, so this isn't the best test case.  How about\n\n```\nsage: search_src(\"Zamboni\", \"Infinite\")\n\nsage: search_src(\"Zamboni\", \"Infinite\", multiline=True)\ncombinat/words/word.py\n```\n",
    "created_at": "2010-01-30T16:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61114",
    "user": "@jhpalmieri"
}
```

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

archive/issue_comments_061115.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61115",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061116.json:
```json
{
    "body": "Quick note: `multiline = kwds.get('multiline', False)`, etc., should also work.",
    "created_at": "2010-01-31T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61116",
    "user": "@qed777"
}
```

Quick note: `multiline = kwds.get('multiline', False)`, etc., should also work.



---

archive/issue_comments_061117.json:
```json
{
    "body": "(Confirming positive review). \nTried a number of tests, verified using egrep and all worked (including using options such as path_re and ignore_case). Representative test below. \n\n\n```\nsage: search_src(\"Labbe\",path_re=\".*py\") # returned a few occurences including in word.py (not shown)\n\nsage: search_src(\"Pirillo\",path_re=\".*py\") \ncombinat/words/word_generators.py:753:        -   [1] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some\ncombinat/words/word_generators.py:756:        -   [2] J. Justin, G. Pirillo, Episturmian words and episturmian\ncombinat/words/word.py:2875:        -   [3] X. Droubay, J. Justin, G. Pirillo, Episturmian words and\n\nsage: search_src(\"Pirillo\",\"Labbe\",path_re=\".*py\") # not found (on same line)\n\nsage: search_src(\"Pirillo\",\"Labbe\",multiline=True,path_re=\".*py\") # Expect one occurence and found one.\ncombinat/words/word_generators.py\n```\n",
    "created_at": "2010-01-31T03:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61117",
    "user": "rossk"
}
```

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

archive/issue_comments_061118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7313#issuecomment-61118",
    "user": "@qed777"
}
```

Resolution: fixed
