# Issue 2404: subs_expr claims to take a dictionary, but doesn't

archive/issues_002404.json:
```json
{
    "body": "Assignee: was\n\nKeywords: calculus, substitution, subs_expr\n\nThe docstring for subs_expr (in calculus.py) says:\n\n> Given a dictionary of key:value pairs, substitute all occurences of key for value in self.\n\n...but the function does not accept a dictionary:\n\n\n```\ndef subs_expr(self, *equations):\n```\n\n\nIt'll take an arbitrary number of regular parameters (which must be SymbolicEquations), but not a dictionary.\n\nI tried to modify the function to something like the following, but couldn't get it to work. Someone familiar with this code should have no problem implementing it correctly:\n\n\n```\ndef subs_expr(self, *equations, **equationsdict):\n  for x in equations:\n    if not isinstance(x, SymbolicEquation):\n      raise TypeError, \"each expression must be an equation\"\n\n  R = self.parent()\n  v = ','.join(['%s=%s'%(x.lhs()._maxima_init_(), x.rhs()._maxima_init_()) \\\n                    for x in equations])\n  v = v + ','.join(['%s=%s' % (key._maxima_init_(), \\\n    equationsdict[key]._maxima_init_()) for key in equationsdict.keys()]\n  return R(self._maxima_().subst(v))\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2404\n\n",
    "created_at": "2008-03-06T09:49:43Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "subs_expr claims to take a dictionary, but doesn't",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2404",
    "user": "ddrake"
}
```
Assignee: was

Keywords: calculus, substitution, subs_expr

The docstring for subs_expr (in calculus.py) says:

> Given a dictionary of key:value pairs, substitute all occurences of key for value in self.

...but the function does not accept a dictionary:


```
def subs_expr(self, *equations):
```


It'll take an arbitrary number of regular parameters (which must be SymbolicEquations), but not a dictionary.

I tried to modify the function to something like the following, but couldn't get it to work. Someone familiar with this code should have no problem implementing it correctly:


```
def subs_expr(self, *equations, **equationsdict):
  for x in equations:
    if not isinstance(x, SymbolicEquation):
      raise TypeError, "each expression must be an equation"

  R = self.parent()
  v = ','.join(['%s=%s'%(x.lhs()._maxima_init_(), x.rhs()._maxima_init_()) \
                    for x in equations])
  v = v + ','.join(['%s=%s' % (key._maxima_init_(), \
    equationsdict[key]._maxima_init_()) for key in equationsdict.keys()]
  return R(self._maxima_().subst(v))
```




Issue created by migration from https://trac.sagemath.org/ticket/2404





---

archive/issue_comments_016231.json:
```json
{
    "body": "Attachment [trac_2404.patch](tarball://root/attachments/some-uuid/ticket2404/trac_2404.patch) by AlexGhitza created at 2009-01-23 19:03:16\n\nThe attached patch fixes subs_expr to take a dictionary, adds an appropriate doctest, and clarifies the docstring a bit.",
    "created_at": "2009-01-23T19:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2404#issuecomment-16231",
    "user": "AlexGhitza"
}
```

Attachment [trac_2404.patch](tarball://root/attachments/some-uuid/ticket2404/trac_2404.patch) by AlexGhitza created at 2009-01-23 19:03:16

The attached patch fixes subs_expr to take a dictionary, adds an appropriate doctest, and clarifies the docstring a bit.



---

archive/issue_comments_016232.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-24T03:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2404#issuecomment-16232",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_016233.json:
```json
{
    "body": "Note that the following in the patch needs to be changed\n\n```\nThe following test shows that \\#4364 is indeed fixed.\n```\n\nI did so in the patch I applied.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2404#issuecomment-16233",
    "user": "mabshoff"
}
```

Note that the following in the patch needs to be changed

```
The following test shows that \#4364 is indeed fixed.
```

I did so in the patch I applied.

Cheers,

Michael



---

archive/issue_comments_016234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2404#issuecomment-16234",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016235.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2404#issuecomment-16235",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
