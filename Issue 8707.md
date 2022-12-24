# Issue 8707: view(x) calls x._latex_() 5 times!

archive/issues_008707.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nKeywords: latex\n\nlatex(x) calls x._latex_() twice, and view(x) 5 times!!!\n\nFor small objects, that's fine, but when x is a graph, and latex'ing it requires calling graphviz, dot2tex, ... it is not reasonable!\n\n\n```\nsage: class blah():\n....:     def _latex_(x):\n....:         print \"coucou\"\n....:         return \"x\"\n....: \nsage: latex(blah())\ncoucou\ncoucou\nx\nsage: view(blah())\ncoucou\ncoucou\ncoucou\ncoucou\ncoucou\n```\n\n\nAnalysis:\n- latex makes use of has_latex_expr which makes a call to _latex_ but discards the result\n\n- latex_file does not reuse its calls to latex(x)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8707\n\n",
    "created_at": "2010-04-17T21:52:29Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "view(x) calls x._latex_() 5 times!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8707",
    "user": "nthiery"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

Keywords: latex

latex(x) calls x._latex_() twice, and view(x) 5 times!!!

For small objects, that's fine, but when x is a graph, and latex'ing it requires calling graphviz, dot2tex, ... it is not reasonable!


```
sage: class blah():
....:     def _latex_(x):
....:         print "coucou"
....:         return "x"
....: 
sage: latex(blah())
coucou
coucou
x
sage: view(blah())
coucou
coucou
coucou
coucou
coucou
```


Analysis:
- latex makes use of has_latex_expr which makes a call to _latex_ but discards the result

- latex_file does not reuse its calls to latex(x)

Issue created by migration from https://trac.sagemath.org/ticket/8707





---

archive/issue_comments_079418.json:
```json
{
    "body": "Attachment [trac_8707-5x_faster_latex-nt.patch](tarball://root/attachments/some-uuid/ticket8707/trac_8707-5x_faster_latex-nt.patch) by nthiery created at 2010-04-17 22:10:27",
    "created_at": "2010-04-17T22:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79418",
    "user": "nthiery"
}
```

Attachment [trac_8707-5x_faster_latex-nt.patch](tarball://root/attachments/some-uuid/ticket8707/trac_8707-5x_faster_latex-nt.patch) by nthiery created at 2010-04-17 22:10:27



---

archive/issue_comments_079419.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-04-17T22:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79419",
    "user": "nthiery"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_079420.json:
```json
{
    "body": "Now, e.g.\n\n```\nsage: g = sage.categories.category.category_graph()\nsage: g.set_latex_options(format = \"dot2tex\")\nsage: view(g, viewer=\"pdf\", tightpage = True)\n```\n\ntakes 6 seconds instead of .5 minutes, which makes it finally usable!",
    "created_at": "2010-04-17T22:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79420",
    "user": "nthiery"
}
```

Now, e.g.

```
sage: g = sage.categories.category.category_graph()
sage: g.set_latex_options(format = "dot2tex")
sage: view(g, viewer="pdf", tightpage = True)
```

takes 6 seconds instead of .5 minutes, which makes it finally usable!



---

archive/issue_comments_079421.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-17T22:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79421",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079422.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T23:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79422",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079423.json:
```json
{
    "body": "Looks good, passes all doctests!",
    "created_at": "2010-04-17T23:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79423",
    "user": "novoselt"
}
```

Looks good, passes all doctests!



---

archive/issue_comments_079424.json:
```json
{
    "body": "Do we know for sure that types are the only sorts of objects which have this problem (that is, which seem to inherit a `_latex_` method according to hasattr, but which actually don't when you try to call it)?",
    "created_at": "2010-04-18T02:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79424",
    "user": "jhpalmieri"
}
```

Do we know for sure that types are the only sorts of objects which have this problem (that is, which seem to inherit a `_latex_` method according to hasattr, but which actually don't when you try to call it)?



---

archive/issue_comments_079425.json:
```json
{
    "body": "I thought about it, but it seems to me that such objects should be \"special\" rather than \"usual\". Then it makes sense to check if x is in one of the special classes and hope that everything is good otherwise, i.e. return True. If it will turn out that there are other special cases, we can add tests for them and document them!",
    "created_at": "2010-04-18T03:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79425",
    "user": "novoselt"
}
```

I thought about it, but it seems to me that such objects should be "special" rather than "usual". Then it makes sense to check if x is in one of the special classes and hope that everything is good otherwise, i.e. return True. If it will turn out that there are other special cases, we can add tests for them and document them!



---

archive/issue_comments_079426.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79426",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079427.json:
```json
{
    "body": "Merged into 4.4.alpha1.",
    "created_at": "2010-04-19T05:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8707#issuecomment-79427",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha1.
