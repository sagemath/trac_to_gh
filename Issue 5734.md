# Issue 5734: Bring doctests of modular/modsym/manin_symbols.py up to 100%

archive/issues_005734.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @loefflerd mtaranes\n\nKeywords: modular symbols\n\nAs of 3.4.1.rc1, we have\n\n```\nSCORE /home/jec/sage-3.4.1.rc1/devel/sage-main/sage/modular/modsym/manin_symbols.py: 2% (2 of 68)\n\nMissing documentation:\n\t * is_ManinSymbol(x):\n\t * __init__(self, weight, list):\n\t * __cmp__(self, right):\n\t * __getitem__(self, n):\n\t * __len__(self):\n\t * apply(self, j, X):\n\t * apply_S(self, j):\n\t * apply_I(self, j):\n\t * apply_T(self, j):\n\t * apply_TT(self, j):\n\t * manin_symbol_list(self):\n\t * manin_symbol(self, i):\n\t * normalize(self, x):\n\t * weight(self):\n\t * __init__(self, level, weight, syms):\n\t * apply_T(self, j):\n\t * apply_TT(self, j):\n\t * level(self):\n\t * normalize(self, x):\n\t * __init__(self, level, weight):\n\t * __repr__(self):\n\t * __init__(self, level, weight):\n\t * __repr__(self):\n\t * __init__(self, group, weight):\n\t * __repr__(self):\n\t * __init__(self, character, weight):\n\t * __repr__(self):\n\t * apply_T(self, j):\n\t * apply_TT(self, j):\n\t * character(self):\n\t * level(self):\n\t * normalize(self, x):\n\t * __init__(self, level, weight):\n\t * __repr__(self):\n\t * apply_T(self, j):\n\t * apply_TT(self, j):\n\t * level(self):\n\t * normalize(self, x):\n\t * tuple(self):\n\t * __get_i(self):\n\t * __get_u(self):\n\t * __get_v(self):\n\t * _repr_(self):\n\t * _latex_(self):\n\t * __cmp__(self, other):\n\t * __mul__(self, matrix):\n\t * copy(self):\n\t * parent(self):\n\t * weight(self):\n\t * _print_polypart(i, j):\n\n\nMissing doctests:\n\t * index(self, x):\n\t * apply_S(self, j):\n\t * apply_I(self, j):\n\t * apply(self, j, m):\n\t * apply_S(self, j):\n\t * apply_I(self, j):\n\t * index(self, x):\n\t * apply_S(self, j):\n\t * apply_I(self, j):\n\t * apply_J(self, j):\n\t * apply(self, j, m):\n\t * __init__(self, parent, t):\n\t * apply(self, a,b,c,d):\n\t * lift_to_sl2z(self, N):\n\t * endpoints(self, N=None):\n\t * modular_symbol_rep(self):\n```\n\nand I think I might have the right background to fix this!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5734\n\n",
    "created_at": "2009-04-10T16:09:32Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Bring doctests of modular/modsym/manin_symbols.py up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5734",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: mabshoff

CC:  @loefflerd mtaranes

Keywords: modular symbols

As of 3.4.1.rc1, we have

```
SCORE /home/jec/sage-3.4.1.rc1/devel/sage-main/sage/modular/modsym/manin_symbols.py: 2% (2 of 68)

Missing documentation:
	 * is_ManinSymbol(x):
	 * __init__(self, weight, list):
	 * __cmp__(self, right):
	 * __getitem__(self, n):
	 * __len__(self):
	 * apply(self, j, X):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * manin_symbol_list(self):
	 * manin_symbol(self, i):
	 * normalize(self, x):
	 * weight(self):
	 * __init__(self, level, weight, syms):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * level(self):
	 * normalize(self, x):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * __init__(self, group, weight):
	 * __repr__(self):
	 * __init__(self, character, weight):
	 * __repr__(self):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * character(self):
	 * level(self):
	 * normalize(self, x):
	 * __init__(self, level, weight):
	 * __repr__(self):
	 * apply_T(self, j):
	 * apply_TT(self, j):
	 * level(self):
	 * normalize(self, x):
	 * tuple(self):
	 * __get_i(self):
	 * __get_u(self):
	 * __get_v(self):
	 * _repr_(self):
	 * _latex_(self):
	 * __cmp__(self, other):
	 * __mul__(self, matrix):
	 * copy(self):
	 * parent(self):
	 * weight(self):
	 * _print_polypart(i, j):


Missing doctests:
	 * index(self, x):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply(self, j, m):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * index(self, x):
	 * apply_S(self, j):
	 * apply_I(self, j):
	 * apply_J(self, j):
	 * apply(self, j, m):
	 * __init__(self, parent, t):
	 * apply(self, a,b,c,d):
	 * lift_to_sl2z(self, N):
	 * endpoints(self, N=None):
	 * modular_symbol_rep(self):
```

and I think I might have the right background to fix this!

Issue created by migration from https://trac.sagemath.org/ticket/5734





---

archive/issue_comments_044719.json:
```json
{
    "body": "David, I thought you might like this one too (when I have done it)  -J",
    "created_at": "2009-04-13T12:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44719",
    "user": "https://github.com/JohnCremona"
}
```

David, I thought you might like this one too (when I have done it)  -J



---

archive/issue_comments_044720.json:
```json
{
    "body": "Attachment [trac_5734.patch](tarball://root/attachments/some-uuid/ticket5734/trac_5734.patch) by @JohnCremona created at 2009-04-14 21:53:34\n\nThe patch touches only sage/modular/modsym/manin_symbols.py, based on 3.4.1.rc2.\n\n```\n----------------------------------------------------------------------\nsage/modular/modsym/manin_symbols.py\nSCORE sage/modular/modsym/manin_symbols.py: 100% (59 of 59)\n----------------------------------------------------------------------\n```\n\n\nI also fixed some small bugs in functions which did not seem to be used, removed (by commenting out) a class `x__ManinSymbolList_gamma1` which was not used, and implemented a slightly more sensible cmp() function for class ManinSymbol (which used to return 1 for any two distinct symbols).  All doctests in sage/modular pass, and I also checked quite thoroughly through the resulting reference manual page, which also looks good.\n\nReview please!",
    "created_at": "2009-04-14T21:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44720",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5734.patch](tarball://root/attachments/some-uuid/ticket5734/trac_5734.patch) by @JohnCremona created at 2009-04-14 21:53:34

The patch touches only sage/modular/modsym/manin_symbols.py, based on 3.4.1.rc2.

```
----------------------------------------------------------------------
sage/modular/modsym/manin_symbols.py
SCORE sage/modular/modsym/manin_symbols.py: 100% (59 of 59)
----------------------------------------------------------------------
```


I also fixed some small bugs in functions which did not seem to be used, removed (by commenting out) a class `x__ManinSymbolList_gamma1` which was not used, and implemented a slightly more sensible cmp() function for class ManinSymbol (which used to return 1 for any two distinct symbols).  All doctests in sage/modular pass, and I also checked quite thoroughly through the resulting reference manual page, which also looks good.

Review please!



---

archive/issue_comments_044721.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2009-04-15T13:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44721",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_044722.json:
```json
{
    "body": "Attachment [trac_5734-2.patch](tarball://root/attachments/some-uuid/ticket5734/trac_5734-2.patch) by @loefflerd created at 2009-04-15 13:35:46\n\nThis looks great: applies fine to 3.4.1.rc2, all doctests pass, and documentation builds happily.\n\nI've made a few slight adjustments to the formatting (mainly enforcing a consistent convention that INPUT: is always followed by a bulleted list and OUTPUT: never is, which was true for most but not all of the new doctests), and I've added an x == loads(dumps(x)) doctest for each of the classes that are actually intended for direct use. (There was a loads(dumps()) test in the file already, so sage -coverage didn't protest, but it was commented out, and it was for a different class anyway.)\n\nJohn: if you're happy with the changes I've made, feel free to change this to \"positive review\".",
    "created_at": "2009-04-15T13:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44722",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5734-2.patch](tarball://root/attachments/some-uuid/ticket5734/trac_5734-2.patch) by @loefflerd created at 2009-04-15 13:35:46

This looks great: applies fine to 3.4.1.rc2, all doctests pass, and documentation builds happily.

I've made a few slight adjustments to the formatting (mainly enforcing a consistent convention that INPUT: is always followed by a bulleted list and OUTPUT: never is, which was true for most but not all of the new doctests), and I've added an x == loads(dumps(x)) doctest for each of the classes that are actually intended for direct use. (There was a loads(dumps()) test in the file already, so sage -coverage didn't protest, but it was commented out, and it was for a different class anyway.)

John: if you're happy with the changes I've made, feel free to change this to "positive review".



---

archive/issue_comments_044723.json:
```json
{
    "body": "I am happy.  Thanks for going through this carefully.   I also think that the conventions to be followed in these new-style docstrings should be written down somewhere!",
    "created_at": "2009-04-15T14:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44723",
    "user": "https://github.com/JohnCremona"
}
```

I am happy.  Thanks for going through this carefully.   I also think that the conventions to be followed in these new-style docstrings should be written down somewhere!



---

archive/issue_events_013460.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-15T19:57:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5734#event-13460"
}
```



---

archive/issue_comments_044724.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T19:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_013461.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-15T19:57:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5734#event-13461"
}
```



---

archive/issue_comments_044725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T19:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5734#issuecomment-44725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
