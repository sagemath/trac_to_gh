# Issue 8553: Minor bugs in solve() if dictionary result requested

archive/issues_008553.json:
```json
{
    "body": "Assignee: leif\n\nCC:  schilly mhansen burcin jason kcrisman\n\nKeywords: solve, solution_dict\n\nsolve() raises an index error on empty solutions if solution dictionary was requested; returns empty list instead of empty dictionary in other cases.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8553\n\n",
    "created_at": "2010-03-17T15:39:40Z",
    "labels": [
        "symbolics",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Minor bugs in solve() if dictionary result requested",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8553",
    "user": "leif"
}
```
Assignee: leif

CC:  schilly mhansen burcin jason kcrisman

Keywords: solve, solution_dict

solve() raises an index error on empty solutions if solution dictionary was requested; returns empty list instead of empty dictionary in other cases.

Issue created by migration from https://trac.sagemath.org/ticket/8553





---

archive/issue_comments_077355.json:
```json
{
    "body": "\n```\nsage: x=var('x')\nsage: x\nx\nsage: solve([0==1], x, solution_dict = True)\n[]\nsage: solve([x==0, 0==1], x, solution_dict = True)\n[]\nsage: solve([(x == 0), (x == 1)], x, solution_dict = True)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n...\nIndexError: list index out of range\n```\n",
    "created_at": "2010-03-17T15:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77355",
    "user": "leif"
}
```


```
sage: x=var('x')
sage: x
x
sage: solve([0==1], x, solution_dict = True)
[]
sage: solve([x==0, 0==1], x, solution_dict = True)
[]
sage: solve([(x == 0), (x == 1)], x, solution_dict = True)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
...
IndexError: list index out of range
```




---

archive/issue_comments_077356.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-17T16:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77356",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077357.json:
```json
{
    "body": "Attachment [trac_8553_solve_dictionary_result_fix.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_dictionary_result_fix.patch) by leif created at 2010-03-17 16:39:28",
    "created_at": "2010-03-17T16:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77357",
    "user": "leif"
}
```

Attachment [trac_8553_solve_dictionary_result_fix.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_dictionary_result_fix.patch) by leif created at 2010-03-17 16:39:28



---

archive/issue_comments_077358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-17T17:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77358",
    "user": "schilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077359.json:
```json
{
    "body": "patch works for 4.3.4.rc0 and looks fine. i would just like to see a \"TESTS::\" header for the additional doctests and a line referring to this ticket, smth. like \"this fixes the problem reported in ticket #8553\".",
    "created_at": "2010-03-17T17:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77359",
    "user": "schilly"
}
```

patch works for 4.3.4.rc0 and looks fine. i would just like to see a "TESTS::" header for the additional doctests and a line referring to this ticket, smth. like "this fixes the problem reported in ticket #8553".



---

archive/issue_comments_077360.json:
```json
{
    "body": "Style-wise, this\n\n\n```\n{} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n```\n\n\nshould be\n\n\n```\n{} if kwds.get('solution_dict', False) is True else []\n```\n",
    "created_at": "2010-03-17T19:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77360",
    "user": "mhansen"
}
```

Style-wise, this


```
{} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
```


should be


```
{} if kwds.get('solution_dict', False) is True else []
```




---

archive/issue_comments_077361.json:
```json
{
    "body": "Or even \n\n\n```\n{} if kwds.get('solution_dict', False) else []\n```\n\n\nif you want to be a bit more lax with inputs.",
    "created_at": "2010-03-17T19:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77361",
    "user": "mhansen"
}
```

Or even 


```
{} if kwds.get('solution_dict', False) else []
```


if you want to be a bit more lax with inputs.



---

archive/issue_comments_077362.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> Or even \n> \n> {{{\n> {} if kwds.get('solution_dict', False) else []\n> }}}\n> \n> if you want to be a bit more lax with inputs.\n\nPlease correct me, but I do not see any difference to your former suggestion.\nIn what sense does this relax the inputs?",
    "created_at": "2010-03-17T20:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77362",
    "user": "leif"
}
```

Replying to [comment:6 mhansen]:
> Or even 
> 
> {{{
> {} if kwds.get('solution_dict', False) else []
> }}}
> 
> if you want to be a bit more lax with inputs.

Please correct me, but I do not see any difference to your former suggestion.
In what sense does this relax the inputs?



---

archive/issue_comments_077363.json:
```json
{
    "body": "In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.",
    "created_at": "2010-03-17T20:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77363",
    "user": "mhansen"
}
```

In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.



---

archive/issue_comments_077364.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.\n\n\nThat's perhaps what one would expect.\n\nBut `solution_dict=1` evaluates to `True` in all versions, while `solution_dict=42` surprisingly evaluates to `False`, even in your latter version.",
    "created_at": "2010-03-17T21:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77364",
    "user": "leif"
}
```

Replying to [comment:8 mhansen]:
> In the first cases, passing in solution_dict=1 would be the same as passing in solution_dict=False.  In the second case, solution_dict=1 would be the same as solution_dict=True.


That's perhaps what one would expect.

But `solution_dict=1` evaluates to `True` in all versions, while `solution_dict=42` surprisingly evaluates to `False`, even in your latter version.



---

archive/issue_comments_077365.json:
```json
{
    "body": "\n```\nsage: kwds = {'solution_dict': 42}\nsage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n{}\nsage: {} if kwds.get('solution_dict', False) is True else []\n[]\nsage: {} if kwds.get('solution_dict', False) else []\n{}\nsage: kwds = {'solution_dict': 42r}\nsage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n[]\nsage: {} if kwds.get('solution_dict', False) is True else []\n[]\nsage: {} if kwds.get('solution_dict', False) else []\n{}\n```\n",
    "created_at": "2010-03-17T21:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77365",
    "user": "mhansen"
}
```


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
{}
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
sage: kwds = {'solution_dict': 42r}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
```




---

archive/issue_comments_077366.json:
```json
{
    "body": "I have to corrct myself: `1` gives `True` only in the first (because of `==` comparison) and the last implementation.",
    "created_at": "2010-03-17T21:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77366",
    "user": "leif"
}
```

I have to corrct myself: `1` gives `True` only in the first (because of `==` comparison) and the last implementation.



---

archive/issue_comments_077367.json:
```json
{
    "body": "\n```\nsage: kwds = {'solution_dict': 42}\nsage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n[]\nsage: {} if kwds.get('solution_dict', False) is True else []\n[]\nsage: {} if kwds.get('solution_dict', False) else []\n{}\nsage: sage: kwds = {'solution_dict': 42r}\nsage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n[]\nsage: {} if kwds.get('solution_dict', False) is True else []\n[]\nsage: {} if kwds.get('solution_dict', False) else []\n{}\n\n```\n\n4.3.4.alpha1\n\nNotice the difference in the first case; 42 is not true for me ;-)",
    "created_at": "2010-03-17T21:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77367",
    "user": "leif"
}
```


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}
sage: sage: kwds = {'solution_dict': 42r}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
[]
sage: {} if kwds.get('solution_dict', False) is True else []
[]
sage: {} if kwds.get('solution_dict', False) else []
{}

```

4.3.4.alpha1

Notice the difference in the first case; 42 is not true for me ;-)



---

archive/issue_comments_077368.json:
```json
{
    "body": "\n```\nsage: kwds = {'solution_dict': 42}                                         \nsage: print kwds                  \n{'solution_dict': 42}\nsage: sage: kwds = {'solution_dict': 42r}                                  \nsage: print kwds                         \n{'solution_dict': 42}\n\n```\n\nPreparser issue?",
    "created_at": "2010-03-17T21:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77368",
    "user": "leif"
}
```


```
sage: kwds = {'solution_dict': 42}                                         
sage: print kwds                  
{'solution_dict': 42}
sage: sage: kwds = {'solution_dict': 42r}                                  
sage: print kwds                         
{'solution_dict': 42}

```

Preparser issue?



---

archive/issue_comments_077369.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> Preparser issue?\n\nno, that's a feature and notice there is an \"r\" behind the 42! \n\n```\nsage: preparse('42r + 42')\n'42 + Integer(42)'\n```\n",
    "created_at": "2010-03-17T22:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77369",
    "user": "schilly"
}
```

Replying to [comment:13 leif]:
> Preparser issue?

no, that's a feature and notice there is an "r" behind the 42! 

```
sage: preparse('42r + 42')
'42 + Integer(42)'
```




---

archive/issue_comments_077370.json:
```json
{
    "body": "Replying to [comment:14 schilly]:\n\nOk, but I still don't understand the different behavior of Mike's and my machine:\n\n\n```\nsage: kwds = {'solution_dict': 42}\nsage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []\n```\n\n\nWhile Mike gets the empty set, I get the empty list, and if the doctests passed on your 4.3.4.rc0, your version behaves like my 4.3.4.alpha1 (on Ubuntu 9.04 x86_64), because I added the `solution_dict=42` case with an expected empty **list**.",
    "created_at": "2010-03-17T23:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77370",
    "user": "leif"
}
```

Replying to [comment:14 schilly]:

Ok, but I still don't understand the different behavior of Mike's and my machine:


```
sage: kwds = {'solution_dict': 42}
sage: {} if 'solution_dict' in kwds and kwds['solution_dict']==True else []
```


While Mike gets the empty set, I get the empty list, and if the doctests passed on your 4.3.4.rc0, your version behaves like my 4.3.4.alpha1 (on Ubuntu 9.04 x86_64), because I added the `solution_dict=42` case with an expected empty **list**.



---

archive/issue_comments_077371.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n\nI still get the empty **list** for the code above with 4.3.4.rc0 (just built on Ubuntu 9.04 x86_64), but I'll update the patch to the latter suggested version (with the 42-testcase changed, i.e. **inverted**!).",
    "created_at": "2010-03-18T00:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77371",
    "user": "leif"
}
```

Replying to [comment:15 leif]:

I still get the empty **list** for the code above with 4.3.4.rc0 (just built on Ubuntu 9.04 x86_64), but I'll update the patch to the latter suggested version (with the 42-testcase changed, i.e. **inverted**!).



---

archive/issue_comments_077372.json:
```json
{
    "body": "Attachment [trac_8553_solve_dictionary_result_fix-variant2.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_dictionary_result_fix-variant2.patch) by leif created at 2010-03-18 00:35:59\n\nApply **either** the first **or** the second patch, **not both**.",
    "created_at": "2010-03-18T00:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77372",
    "user": "leif"
}
```

Attachment [trac_8553_solve_dictionary_result_fix-variant2.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_dictionary_result_fix-variant2.patch) by leif created at 2010-03-18 00:35:59

Apply **either** the first **or** the second patch, **not both**.



---

archive/issue_comments_077373.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-18T16:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77373",
    "user": "burcin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077374.json:
```json
{
    "body": "AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.\n\nWith this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.\n\nIMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?",
    "created_at": "2010-03-18T16:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77374",
    "user": "burcin"
}
```

AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.

With this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.

IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?



---

archive/issue_comments_077375.json:
```json
{
    "body": "Replying to [comment:18 burcin]:\n> IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?\n\nYes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.",
    "created_at": "2010-03-18T17:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77375",
    "user": "schilly"
}
```

Replying to [comment:18 burcin]:
> IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?

Yes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.



---

archive/issue_comments_077376.json:
```json
{
    "body": "Replying to [comment:18 burcin]:\n> AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.\n> \n> With this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.\n\nThat's really a matter of design; one could equally well specify the function to return a list containing an empty dictionary in that case; i.e., the current specification is not precise (and that's not the only one).\n\nBut you're right, unless we change the *informal* \"prototype\" (its signature), it should in any case return a ***list** of something*.\n\n\nI'd change the patch to reflect whatever behavior you want... ;-)\n\n-Leif",
    "created_at": "2010-03-18T17:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77376",
    "user": "leif"
}
```

Replying to [comment:18 burcin]:
> AFAICT, `solve` returns a list of possible solutions to the given equality. When the `solution_dict` parameter is `True`, this list is populated by dictionaries instead of symbolic relations.
> 
> With this reasoning the current behavior of returning an empty list if we can't find any solutions even if the `solution_dict` parameter is `True` seems correct to me.

That's really a matter of design; one could equally well specify the function to return a list containing an empty dictionary in that case; i.e., the current specification is not precise (and that's not the only one).

But you're right, unless we change the *informal* "prototype" (its signature), it should in any case return a ***list** of something*.


I'd change the patch to reflect whatever behavior you want... ;-)

-Leif



---

archive/issue_comments_077377.json:
```json
{
    "body": "Replying to [comment:19 schilly]:\n> Replying to [comment:18 burcin]:\n> > IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?\n> \n> Yes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.\n\nSo we'd change the ticket description and the patch to only address and fix the index error?\n\nOk for me.",
    "created_at": "2010-03-18T17:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77377",
    "user": "leif"
}
```

Replying to [comment:19 schilly]:
> Replying to [comment:18 burcin]:
> > IMHO, the only thing that needs to be fixed is the `IndexError` when there is no solution. Comments?
> 
> Yes please, I don't get it why this is so complicated! All unrelated issues should be discussed off-ticket.

So we'd change the ticket description and the patch to only address and fix the index error?

Ok for me.



---

archive/issue_comments_077378.json:
```json
{
    "body": "Hi Leif,\n\nReplying to [comment:21 leif]:\n> So we'd change the ticket description and the patch to only address and fix the index error?\n> \n> Ok for me.\n\nCan you provide a patch that fixes the `IndexError` problem? If we get this reviewed in the next few days it might still make it to the next release.",
    "created_at": "2010-04-05T13:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77378",
    "user": "burcin"
}
```

Hi Leif,

Replying to [comment:21 leif]:
> So we'd change the ticket description and the patch to only address and fix the index error?
> 
> Ok for me.

Can you provide a patch that fixes the `IndexError` problem? If we get this reviewed in the next few days it might still make it to the next release.



---

archive/issue_comments_077379.json:
```json
{
    "body": "Attachment [trac_8553_solve_fix_IndexError.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.patch) by leif created at 2010-04-06 04:43:46",
    "created_at": "2010-04-06T04:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77379",
    "user": "leif"
}
```

Attachment [trac_8553_solve_fix_IndexError.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.patch) by leif created at 2010-04-06 04:43:46



---

archive/issue_comments_077380.json:
```json
{
    "body": "Sorry, unable to delete the previous patches; **apply only the last one**.\n\n* `IndexError` issue fixed.\n* Type of parameter `solution_dict` relaxed as suggested by Mike Hansen (now consistent; also in `expression.pyx`/`Expression.solve()`).\n* (More) Doctests added.\n* Description made more clear. Some typos fixed.",
    "created_at": "2010-04-06T05:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77380",
    "user": "leif"
}
```

Sorry, unable to delete the previous patches; **apply only the last one**.

* `IndexError` issue fixed.
* Type of parameter `solution_dict` relaxed as suggested by Mike Hansen (now consistent; also in `expression.pyx`/`Expression.solve()`).
* (More) Doctests added.
* Description made more clear. Some typos fixed.



---

archive/issue_comments_077381.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-06T05:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77381",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077382.json:
```json
{
    "body": "Attachment [trac_8553_solve_fix_IndexError.2.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.2.patch) by timdumol created at 2010-04-18 07:56:00\n\nRebase on sage-4.4.alpha0.",
    "created_at": "2010-04-18T07:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77382",
    "user": "timdumol"
}
```

Attachment [trac_8553_solve_fix_IndexError.2.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.2.patch) by timdumol created at 2010-04-18 07:56:00

Rebase on sage-4.4.alpha0.



---

archive/issue_comments_077383.json:
```json
{
    "body": "Works perfectly after this rebase. Positive review, but someone has to review this rebase first.",
    "created_at": "2010-04-18T07:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77383",
    "user": "timdumol"
}
```

Works perfectly after this rebase. Positive review, but someone has to review this rebase first.



---

archive/issue_comments_077384.json:
```json
{
    "body": "Attachment [trac_8553_solve_fix_IndexError.3.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.3.patch) by burcin created at 2010-05-05 01:23:35\n\nrevised version of Leif's patch",
    "created_at": "2010-05-05T01:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77384",
    "user": "burcin"
}
```

Attachment [trac_8553_solve_fix_IndexError.3.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553_solve_fix_IndexError.3.patch) by burcin created at 2010-05-05 01:23:35

revised version of Leif's patch



---

archive/issue_comments_077385.json:
```json
{
    "body": "reviewer's patch",
    "created_at": "2010-05-05T01:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77385",
    "user": "burcin"
}
```

reviewer's patch



---

archive/issue_comments_077386.json:
```json
{
    "body": "Attachment [trac_8553-review.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553-review.patch) by burcin created at 2010-05-05 01:44:30\n\nThe doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`. I uploaded a revised version of Leif's patch, attachment:trac_8553_solve_fix_IndexError.3.patch, which cuts down on these examples.\n\nattachment:trac_8553-review.patch adds a new test condition to check if the first argument is a list, after the statement that handles a single symbolic expression.\n\nCan someone review my patch?",
    "created_at": "2010-05-05T01:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77386",
    "user": "burcin"
}
```

Attachment [trac_8553-review.patch](tarball://root/attachments/some-uuid/ticket8553/trac_8553-review.patch) by burcin created at 2010-05-05 01:44:30

The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`. I uploaded a revised version of Leif's patch, attachment:trac_8553_solve_fix_IndexError.3.patch, which cuts down on these examples.

attachment:trac_8553-review.patch adds a new test condition to check if the first argument is a list, after the statement that handles a single symbolic expression.

Can someone review my patch?



---

archive/issue_comments_077387.json:
```json
{
    "body": "Replying to [comment:26 burcin]:\n> The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.\n\n:-) Adding `# optional` or `# long` would have been possible, too.\n\n(Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)",
    "created_at": "2010-05-05T12:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77387",
    "user": "leif"
}
```

Replying to [comment:26 burcin]:
> The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.

:-) Adding `# optional` or `# long` would have been possible, too.

(Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)



---

archive/issue_comments_077388.json:
```json
{
    "body": "Replying to [comment:27 leif]:\n> Replying to [comment:26 burcin]:\n> > The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.\n> \n> :-) Adding `# optional` or `# long` would have been possible, too.\n> \n> (Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)\n\nSince they weren't testing the functionality of `solve()`, but a convenience in Python, I think it's OK if they are not so extensive. I run doctests on these files very often, so it's rather important that even the long tests take a reasonable time.\n\nCan you review my changes BTW?",
    "created_at": "2010-05-06T16:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77388",
    "user": "burcin"
}
```

Replying to [comment:27 leif]:
> Replying to [comment:26 burcin]:
> > The doctests for using values that are taken to be True in Leif's patch added a few extra seconds to the time to test `sage/symbolic/relation.py`.
> 
> :-) Adding `# optional` or `# long` would have been possible, too.
> 
> (Now the tests of Python `int`s vs. Sage's `Integer`s are omitted.)

Since they weren't testing the functionality of `solve()`, but a convenience in Python, I think it's OK if they are not so extensive. I run doctests on these files very often, so it's rather important that even the long tests take a reasonable time.

Can you review my changes BTW?



---

archive/issue_comments_077389.json:
```json
{
    "body": "Changing keywords from \"solve, solution_dict\" to \"solve, solution_dict, beginner\".",
    "created_at": "2010-05-26T16:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77389",
    "user": "leif"
}
```

Changing keywords from "solve, solution_dict" to "solve, solution_dict, beginner".



---

archive/issue_comments_077390.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-07T17:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77390",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077391.json:
```json
{
    "body": "Replying to [comment:28 burcin]:\n> Can you review my changes BTW? \n\n`m.to_poly_solve(variables)` might be called twice.\n\nBtw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.",
    "created_at": "2010-06-07T17:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77391",
    "user": "leif"
}
```

Replying to [comment:28 burcin]:
> Can you review my changes BTW? 

`m.to_poly_solve(variables)` might be called twice.

Btw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.



---

archive/issue_comments_077392.json:
```json
{
    "body": "Just for reference, see [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/d54b283435a8ed4b/1eab51e2561da568) for another report of this.",
    "created_at": "2011-05-18T13:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77392",
    "user": "kcrisman"
}
```

Just for reference, see [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/d54b283435a8ed4b/1eab51e2561da568) for another report of this.



---

archive/issue_comments_077393.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-18T16:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77393",
    "user": "kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_077394.json:
```json
{
    "body": "Replying to [comment:30 leif]:\n> Replying to [comment:28 burcin]:\n> > Can you review my changes BTW? \n> \n> `m.to_poly_solve(variables)` might be called twice.\n\nIt is, but only in the unusual situation that Maxima's solve gave an error and `to_poly_solve` gave the empty list.  More to the point, this was there before, and should be a different ticket.\n\n> Btw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.\n>  \nNot at all - usually it is appropriate to review a reviewer patch.  This reviewer patch really is pretty minimally invasive, and in fact provides a much more useful error message.\n\nIt is true that \n\n```\nsage: solve(x==1,x,solution_dict=int(3))\n[{x: 1}]\nsage: solve([0==1],x,solution_dict=int(3))\n[]\nsage: solve(0==1,x,solution_dict=int(3))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/<ipython console> in <module>()\n\n/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)\n    652 \n    653     if not isinstance(f, (list, tuple)):\n--> 654         raise TypeError(\"The first argument must be a symbolic expression or a list of symbolic expressions.\")\n    655 \n    656     if len(f)==1 and is_Expression(f[0]):\n\nTypeError: The first argument must be a symbolic expression or a list of symbolic expressions.\n```\n\nwhich is not ideal.  However, this is still better behavior than the mysterious message about bools and len before, so that could be another ticket.  \n\nIn any case, this (somewhat surprisingly) still applies fine to 4.7.rc2!  And does what it says.  And passes tests. Positive review.",
    "created_at": "2011-05-18T16:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77394",
    "user": "kcrisman"
}
```

Replying to [comment:30 leif]:
> Replying to [comment:28 burcin]:
> > Can you review my changes BTW? 
> 
> `m.to_poly_solve(variables)` might be called twice.

It is, but only in the unusual situation that Maxima's solve gave an error and `to_poly_solve` gave the empty list.  More to the point, this was there before, and should be a different ticket.

> Btw, I think the patch should be finally reviewed by someone else, not me, as I'm one of the authors.
>  
Not at all - usually it is appropriate to review a reviewer patch.  This reviewer patch really is pretty minimally invasive, and in fact provides a much more useful error message.

It is true that 

```
sage: solve(x==1,x,solution_dict=int(3))
[{x: 1}]
sage: solve([0==1],x,solution_dict=int(3))
[]
sage: solve(0==1,x,solution_dict=int(3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/<ipython console> in <module>()

/Users/karl-dietercrisman/Downloads/sage-4.7.rc1/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    652 
    653     if not isinstance(f, (list, tuple)):
--> 654         raise TypeError("The first argument must be a symbolic expression or a list of symbolic expressions.")
    655 
    656     if len(f)==1 and is_Expression(f[0]):

TypeError: The first argument must be a symbolic expression or a list of symbolic expressions.
```

which is not ideal.  However, this is still better behavior than the mysterious message about bools and len before, so that could be another ticket.  

In any case, this (somewhat surprisingly) still applies fine to 4.7.rc2!  And does what it says.  And passes tests. Positive review.



---

archive/issue_comments_077395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-01T07:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77395",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_077396.json:
```json
{
    "body": "For the sagebot:\n\nApply [attachment:trac_8553_solve_fix_IndexError.3.patch] [attachment:trac_8553-review.patch]",
    "created_at": "2011-07-22T19:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8553#issuecomment-77396",
    "user": "leif"
}
```

For the sagebot:

Apply [attachment:trac_8553_solve_fix_IndexError.3.patch] [attachment:trac_8553-review.patch]
