# Issue 8227: Improving iterated palindromic closure computation

archive/issues_008227.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @seblabbe\n\nKeywords: iterated palindromic closure\n\nThere is a faster way to compute the iterated paindromic closure of a word than using the definition. The problem with the latter is that it needs to compute the longest f-palindromic suffix of the current word at each step, while it is possible to easily deduce this length only by looking at the directive word.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8227\n\n",
    "created_at": "2010-02-10T11:20:10Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Improving iterated palindromic closure computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8227",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```
Assignee: @aghitza

CC:  @seblabbe

Keywords: iterated palindromic closure

There is a faster way to compute the iterated paindromic closure of a word than using the definition. The problem with the latter is that it needs to compute the longest f-palindromic suffix of the current word at each step, while it is possible to easily deduce this length only by looking at the directive word.

Issue created by migration from https://trac.sagemath.org/ticket/8227





---

archive/issue_comments_072519.json:
```json
{
    "body": "I had to implement two other functions: find() and rfind() that were only available for Word_str words. It is not the more efficient implementation yet, but that was not the goal of this ticket...",
    "created_at": "2010-02-10T12:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72519",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I had to implement two other functions: find() and rfind() that were only available for Word_str words. It is not the more efficient implementation yet, but that was not the goal of this ticket...



---

archive/issue_comments_072520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T12:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72520",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072521.json:
```json
{
    "body": "Changing assignee from @aghitza to abmasse.",
    "created_at": "2010-02-10T13:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72521",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing assignee from @aghitza to abmasse.



---

archive/issue_comments_072522.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-02-10T13:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72522",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_072523.json:
```json
{
    "body": "1. I think the patch should follow the python behavior (i.e. return -1)\n\n```\nsage: '0123456789'.find('4566')\n-1\nsage: '0123456789'.rfind('4566')\n-1\n```\n\nfor those functions :\n\n```\nsage: Word(range(10)).rfind(Word([4,5,6,6]))\nsage: Word(range(10)).find(Word([4,5,6,6]))\n```\n\n2. The following comment found in the doc of `find` and `rfind` \n\n```\nThis function is different for Word_str objects:\n```\n\nillustrates a problem : the behavior for `Word_str` should be the same (`Word_str` is wrong). Can you fix it? You may consult #8127 for an idea of how to handle it. Make sure to ask the parent using super if type of other is not an str or a `Word_str`.\n\n\n3. An enumeration in the doc of the iterator function is broken as seen in the result of :\n\n```\nsage: w = Word(range(10))\nsage: browse_sage_doc(w._iterated_right_palindromic_closure_recursive_iterator)\n```\n\nAdding a blank line before the itemize should repair the problem. I also suggest to put `WordMorphism`,  `'recursive'` and `_iterative_righ...iterator()` inside double backquotes (like input arguments).\n\n4. Looking the function below but also how naive is the code of `find`, maybe the function `find` could use the function `first_pos_in` instead? This makes me realize that the function `first_pos_in` was probably a bad choice of name.... Using the new deprecation warning introduced recently by Florent Hivert this (name modif) can be done more easily now (but not in this ticket).\n\n```\nsage: %timeit Word([990,991,992,993]).first_pos_in(Word(range(1000)))\n125 loops, best of 3: 1.65 ms per loop\nsage: %timeit Word(range(1000)).find(Word([990,991,992,993]))\n5 loops, best of 3: 48 ms per loop\n```\n\n5. Could `rfind` could be improved easily using `_pos_in` and other good suffix table already implemented? If so, it can be good to do it now. But if you don't care now, it is fine. The function could be improved later if it is valuable. Anyway, the next step for all those search stuff is to be cythoned...\n\nThat's all for my comments.",
    "created_at": "2010-02-11T00:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72523",
    "user": "https://github.com/seblabbe"
}
```

1. I think the patch should follow the python behavior (i.e. return -1)

```
sage: '0123456789'.find('4566')
-1
sage: '0123456789'.rfind('4566')
-1
```

for those functions :

```
sage: Word(range(10)).rfind(Word([4,5,6,6]))
sage: Word(range(10)).find(Word([4,5,6,6]))
```

2. The following comment found in the doc of `find` and `rfind` 

```
This function is different for Word_str objects:
```

illustrates a problem : the behavior for `Word_str` should be the same (`Word_str` is wrong). Can you fix it? You may consult #8127 for an idea of how to handle it. Make sure to ask the parent using super if type of other is not an str or a `Word_str`.


3. An enumeration in the doc of the iterator function is broken as seen in the result of :

```
sage: w = Word(range(10))
sage: browse_sage_doc(w._iterated_right_palindromic_closure_recursive_iterator)
```

Adding a blank line before the itemize should repair the problem. I also suggest to put `WordMorphism`,  `'recursive'` and `_iterative_righ...iterator()` inside double backquotes (like input arguments).

4. Looking the function below but also how naive is the code of `find`, maybe the function `find` could use the function `first_pos_in` instead? This makes me realize that the function `first_pos_in` was probably a bad choice of name.... Using the new deprecation warning introduced recently by Florent Hivert this (name modif) can be done more easily now (but not in this ticket).

```
sage: %timeit Word([990,991,992,993]).first_pos_in(Word(range(1000)))
125 loops, best of 3: 1.65 ms per loop
sage: %timeit Word(range(1000)).find(Word([990,991,992,993]))
5 loops, best of 3: 48 ms per loop
```

5. Could `rfind` could be improved easily using `_pos_in` and other good suffix table already implemented? If so, it can be good to do it now. But if you don't care now, it is fine. The function could be improved later if it is valuable. Anyway, the next step for all those search stuff is to be cythoned...

That's all for my comments.



---

archive/issue_comments_072524.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T00:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72524",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072525.json:
```json
{
    "body": "Thank you S\u00e9bastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. I intend to do it in a close future, but this is in some way independent of the iterated palindromic closures functions. As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.",
    "created_at": "2010-02-11T17:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72525",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Thank you Sébastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. I intend to do it in a close future, but this is in some way independent of the iterated palindromic closures functions. As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.



---

archive/issue_comments_072526.json:
```json
{
    "body": "Replying to [comment:5 abmasse]:\n> Thank you S\u00e9bastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. \n\n\nWell, ok for 5 : `rfind` could be improved later. But for 4, I would like your new find function to make use of `first_pos_in` since it is already there and is faster. If you want to keep your implementation there, I suggest you use a parameter `algorithm` that defaults to `suffix_table` or a similar word and that make use of `first_pos_in`.\n\n> As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). \n\n\nI think both are possible (Je ne crois pas que l'un emp\u00eache l'autre) : one may selec the algorithm and the function can still behave like python. For example, \n\n```\nsage: w = Word(range(10))\nsage: u = Word(range(5, 8))\nsage: w.find(u)\n5\nsage: w.find(u, algorithm='KMP')\n5\nsage: w.find(u*u)\n-1\n```\n\n> If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.\n\n\nOk, so let's open a new ticket to clean up find and rfind.",
    "created_at": "2010-02-14T18:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72526",
    "user": "https://github.com/seblabbe"
}
```

Replying to [comment:5 abmasse]:
> Thank you Sébastien for all those comments ! I agree with you on items 4 and 5, but I think these issues should be addressed in another ticket. 


Well, ok for 5 : `rfind` could be improved later. But for 4, I would like your new find function to make use of `first_pos_in` since it is already there and is faster. If you want to keep your implementation there, I suggest you use a parameter `algorithm` that defaults to `suffix_table` or a similar word and that make use of `first_pos_in`.

> As for item 1, I agree with you as well, but I think it would be better if ``find()`` and ``rfind()`` functions could allow the user to choose between different string search algorithms (Boyer-Moore, KMP, etc.), so that it is maybe not necessary to make them look like the Python functions (what do you think?). 


I think both are possible (Je ne crois pas que l'un empêche l'autre) : one may selec the algorithm and the function can still behave like python. For example, 

```
sage: w = Word(range(10))
sage: u = Word(range(5, 8))
sage: w.find(u)
5
sage: w.find(u, algorithm='KMP')
5
sage: w.find(u*u)
-1
```

> If I understand you well in item 2, you would like me to change the ``find()`` and ``rfind()`` functions for Word_str objects or only to detect it in the algorithm computing the iterated palindromic closure? Finally, I will correct item 3 and the other problems as soon as you answer me.


Ok, so let's open a new ticket to clean up find and rfind.



---

archive/issue_comments_072527.json:
```json
{
    "body": "I have corrected items 1 to 4.\n\nAs discussed, item 5 will be done in another ticket or directly in Cython.\n\nI'll upload the new patch in a few minutes.",
    "created_at": "2010-02-21T01:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72527",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I have corrected items 1 to 4.

As discussed, item 5 will be done in another ticket or directly in Cython.

I'll upload the new patch in a few minutes.



---

archive/issue_comments_072528.json:
```json
{
    "body": "Attachment [trac_8227_iterated_palindromic_closure_improvement-abm.patch](tarball://root/attachments/some-uuid/ticket8227/trac_8227_iterated_palindromic_closure_improvement-abm.patch) by abmasse created at 2010-02-21 01:57:11\n\nUpdated patch with corrections",
    "created_at": "2010-02-21T01:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72528",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8227_iterated_palindromic_closure_improvement-abm.patch](tarball://root/attachments/some-uuid/ticket8227/trac_8227_iterated_palindromic_closure_improvement-abm.patch) by abmasse created at 2010-02-21 01:57:11

Updated patch with corrections



---

archive/issue_comments_072529.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-21T01:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72529",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072530.json:
```json
{
    "body": "Attachment [trac_8227_review-sl.patch](tarball://root/attachments/some-uuid/ticket8227/trac_8227_review-sl.patch) by @seblabbe created at 2010-02-23 02:43:07\n\nApplies over the precedent patch",
    "created_at": "2010-02-23T02:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72530",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8227_review-sl.patch](tarball://root/attachments/some-uuid/ticket8227/trac_8227_review-sl.patch) by @seblabbe created at 2010-02-23 02:43:07

Applies over the precedent patch



---

archive/issue_comments_072531.json:
```json
{
    "body": "I just tested the patch. All test passed in sage/combinat/words. The speed of the function is greatly improved. Doc builds fine. I am giving a positive review to this ticket.\n\nAlthought, I added a patch fixing some small sphinx editing and replace `l` for `L` because I was reading `1` at first glance. Alexandre, if you agree with my patch, I allow you to change the status of this ticket to positive review.",
    "created_at": "2010-02-23T02:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72531",
    "user": "https://github.com/seblabbe"
}
```

I just tested the patch. All test passed in sage/combinat/words. The speed of the function is greatly improved. Doc builds fine. I am giving a positive review to this ticket.

Althought, I added a patch fixing some small sphinx editing and replace `l` for `L` because I was reading `1` at first glance. Alexandre, if you agree with my patch, I allow you to change the status of this ticket to positive review.



---

archive/issue_comments_072532.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T08:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72532",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072533.json:
```json
{
    "body": "I agree with the changes. I tested the two patches and everything seems alright. All tests passed, no problem in the documentation. Positive review to S\u00e9bastien's changes.",
    "created_at": "2010-02-23T08:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72533",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I agree with the changes. I tested the two patches and everything seems alright. All tests passed, no problem in the documentation. Positive review to Sébastien's changes.



---

archive/issue_comments_072534.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8227_iterated_palindromic_closure_improvement-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_iterated_palindromic_closure_improvement-abm.patch)\n2. [trac_8227_review-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_review-sl.patch)",
    "created_at": "2010-03-02T21:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8227_iterated_palindromic_closure_improvement-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_iterated_palindromic_closure_improvement-abm.patch)
2. [trac_8227_review-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8227/trac_8227_review-sl.patch)



---

archive/issue_events_019687.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T21:22:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8227#event-19687"
}
```



---

archive/issue_comments_072535.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8227#issuecomment-72535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
