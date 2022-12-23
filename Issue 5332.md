# Issue 5332: Convert MV polynomial constructors in multi_polynomial_ideal.py, category_object.py, etc

archive/issues_005332.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  malb\n\nFrom http://groups.google.com/group/sage-support/browse_thread/thread/21d861876918e668\n\n\n```\n> While I looked at ideal's docstring I noticed plenty of construct like \n>     sage: R, x = PolynomialRing(ZZ, 'x').objgen() \n> Shouldn't we get those cleaned up to read \n>    sage: R.<x>=ZZ[] \n> or am I missing the point? I have seen too many people use the above \n> old objgen() constuct and I find it rather hideous. \n\n\nYeah, its just old and noone got around cleaning that up. \n\nMartin \n```\n\n\nThere are some more places, to find them run\n\n```\ngrep \"PolynomialRing\" .doctest* | grep objgen\n```\n\nin $SAGE_ROOT/tmp\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5332\n\n",
    "created_at": "2009-02-21T22:50:25Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "title": "Convert MV polynomial constructors in multi_polynomial_ideal.py, category_object.py, etc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5332",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  malb

From http://groups.google.com/group/sage-support/browse_thread/thread/21d861876918e668


```
> While I looked at ideal's docstring I noticed plenty of construct like 
>     sage: R, x = PolynomialRing(ZZ, 'x').objgen() 
> Shouldn't we get those cleaned up to read 
>    sage: R.<x>=ZZ[] 
> or am I missing the point? I have seen too many people use the above 
> old objgen() constuct and I find it rather hideous. 


Yeah, its just old and noone got around cleaning that up. 

Martin 
```


There are some more places, to find them run

```
grep "PolynomialRing" .doctest* | grep objgen
```

in $SAGE_ROOT/tmp
Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5332





---

archive/issue_comments_041041.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-14T08:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41041",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041042.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2015-04-14T08:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41042",
    "user": "mmezzarobba"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_041043.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-04-14T08:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41043",
    "user": "mmezzarobba"
}
```

New commits:



---

archive/issue_comments_041044.json:
```json
{
    "body": "Changing component from doctest coverage to documentation.",
    "created_at": "2015-04-14T08:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41044",
    "user": "mmezzarobba"
}
```

Changing component from doctest coverage to documentation.



---

archive/issue_comments_041045.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-14T08:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41045",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041046.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-14T09:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41046",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_041047.json:
```json
{
    "body": "With the last version of the patch:\n\n```\n$ git grep \"sage: .*PolynomialRing.*objgen\" src/sage/\nsrc/sage/rings/fraction_field_element.pyx:        sage: K, x = FractionField(PolynomialRing(QQ, 'x')).objgen()\nsrc/sage/rings/polynomial/multi_polynomial_element.py:            sage: R, x = PolynomialRing(QQbar, 10, 'x').objgens()\nsrc/sage/rings/polynomial/multi_polynomial_ring.py:    sage: PolynomialRing(GF(5), 3, 'xyz').objgens()\nsrc/sage/rings/polynomial/polynomial_element.pyx:    sage: PolynomialRing(ZZ,'x').objgen()\nsrc/sage/structure/category_object.pyx:            sage: R, x = PolynomialRing(QQ,'x').objgen()\nsrc/sage/structure/category_object.pyx:         sage: R, x = PolynomialRing(QQ,'x',12).objgens()\n```\n",
    "created_at": "2015-04-14T09:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41047",
    "user": "mmezzarobba"
}
```

With the last version of the patch:

```
$ git grep "sage: .*PolynomialRing.*objgen" src/sage/
src/sage/rings/fraction_field_element.pyx:        sage: K, x = FractionField(PolynomialRing(QQ, 'x')).objgen()
src/sage/rings/polynomial/multi_polynomial_element.py:            sage: R, x = PolynomialRing(QQbar, 10, 'x').objgens()
src/sage/rings/polynomial/multi_polynomial_ring.py:    sage: PolynomialRing(GF(5), 3, 'xyz').objgens()
src/sage/rings/polynomial/polynomial_element.pyx:    sage: PolynomialRing(ZZ,'x').objgen()
src/sage/structure/category_object.pyx:            sage: R, x = PolynomialRing(QQ,'x').objgen()
src/sage/structure/category_object.pyx:         sage: R, x = PolynomialRing(QQ,'x',12).objgens()
```




---

archive/issue_comments_041048.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-14T09:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41048",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041049.json:
```json
{
    "body": "This is horrible\n\n```\nR.<x,y> = QQ[]\n```\n\n(but working, I know).\n\nPlease use either\n\n```\nsage: R = QQ['x,y']\nsage: x,y = R.gens()\n```\n\nor the shorter\n\n```\nsage: R.<x,y> = QQ['x,y']\n```\n\n\nHaving something implicit in the right hand side of this declaration is really bad. Don't you think?\n\nVincent",
    "created_at": "2015-04-14T09:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41049",
    "user": "vdelecroix"
}
```

This is horrible

```
R.<x,y> = QQ[]
```

(but working, I know).

Please use either

```
sage: R = QQ['x,y']
sage: x,y = R.gens()
```

or the shorter

```
sage: R.<x,y> = QQ['x,y']
```


Having something implicit in the right hand side of this declaration is really bad. Don't you think?

Vincent



---

archive/issue_comments_041050.json:
```json
{
    "body": "Replying to [comment:10 vdelecroix]:\n> Having something implicit in the right hand side of this declaration is really bad. Don't you think?\n\nNo `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.",
    "created_at": "2015-04-14T11:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41050",
    "user": "mmezzarobba"
}
```

Replying to [comment:10 vdelecroix]:
> Having something implicit in the right hand side of this declaration is really bad. Don't you think?

No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.



---

archive/issue_comments_041051.json:
```json
{
    "body": "Replying to [comment:11 mmezzarobba]:\n> Replying to [comment:10 vdelecroix]:\n> > Having something implicit in the right hand side of this declaration is really bad. Don't you think?\n> \n> No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.\n\nThis is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.",
    "created_at": "2015-04-14T11:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41051",
    "user": "vdelecroix"
}
```

Replying to [comment:11 mmezzarobba]:
> Replying to [comment:10 vdelecroix]:
> > Having something implicit in the right hand side of this declaration is really bad. Don't you think?
> 
> No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.

This is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.



---

archive/issue_comments_041052.json:
```json
{
    "body": "Replying to [comment:12 vdelecroix]:\n> Replying to [comment:11 mmezzarobba]:\n> > Replying to [comment:10 vdelecroix]:\n> > > Having something implicit in the right hand side of this declaration is really bad. Don't you think?\n> > \n> > No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.\n> \n> This is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.\n\nI agree with Marc, I clearly see `sage: R.<x,y> = QQ['x,y']` as a repetition. And I honestly do not see the problem with `sage: R.<x,y> = QQ[]`: one is simply saying \"*I define the polynomial ring over QQ with 2 variables, and I use the Python `x` and `y` to denote its generators. I let Sage choose the way it represents graphically these generators*\". And then, of course it is quite nice that the default choice is to use the string `\"x\"` for `x` and the string `\"y\"` for `y`. \n\nOtherwise stated, I like in the notation `sage: R.<x,y> = QQ[]` the fact that I simply define the object and not the way it is printed.",
    "created_at": "2015-04-14T11:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41052",
    "user": "bruno"
}
```

Replying to [comment:12 vdelecroix]:
> Replying to [comment:11 mmezzarobba]:
> > Replying to [comment:10 vdelecroix]:
> > > Having something implicit in the right hand side of this declaration is really bad. Don't you think?
> > 
> > No `:-)`. At least, less so that repeating the name when the intention is to have the variable name match the identifier. Also, that's both the style the ticket description suggests and a very common choice in existing sage documentation.
> 
> This is one more thing that induces confusion between Python variables and mathematical variables (not worse than `var(x)` though). It is not a repetition as the semantic are very different.

I agree with Marc, I clearly see `sage: R.<x,y> = QQ['x,y']` as a repetition. And I honestly do not see the problem with `sage: R.<x,y> = QQ[]`: one is simply saying "*I define the polynomial ring over QQ with 2 variables, and I use the Python `x` and `y` to denote its generators. I let Sage choose the way it represents graphically these generators*". And then, of course it is quite nice that the default choice is to use the string `"x"` for `x` and the string `"y"` for `y`. 

Otherwise stated, I like in the notation `sage: R.<x,y> = QQ[]` the fact that I simply define the object and not the way it is printed.



---

archive/issue_comments_041053.json:
```json
{
    "body": "Its Magma syntax so its going to stay either way.\n\nI also prefer `R.<x,y> = QQ[]`. Technically the variable labels also enter the right hand side, but thats just an implementation detail. We could dig the labels out of the globals dictionary without having the preparser put them into the right hand side of the declaration, so its not truly necessary. Of course the preparser implementation is superior.",
    "created_at": "2015-04-14T12:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41053",
    "user": "vbraun"
}
```

Its Magma syntax so its going to stay either way.

I also prefer `R.<x,y> = QQ[]`. Technically the variable labels also enter the right hand side, but thats just an implementation detail. We could dig the labels out of the globals dictionary without having the preparser put them into the right hand side of the declaration, so its not truly necessary. Of course the preparser implementation is superior.



---

archive/issue_comments_041054.json:
```json
{
    "body": "> Its Magma syntax so its going to stay either way.\nAs well as being old and so liable to break others' code if removed.\n\n+1",
    "created_at": "2015-04-14T13:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41054",
    "user": "kcrisman"
}
```

> Its Magma syntax so its going to stay either way.
As well as being old and so liable to break others' code if removed.

+1



---

archive/issue_comments_041055.json:
```json
{
    "body": "All right, let me start again.\n\n1. I agree with all of you on what **I** am doing every day to implement a polynomial ring in Sage. The syntax `R.<x,y> = QQ[]` is compact and useful.\n\n2. My comment was about newcomers for which the concept of a Python variable is not necessarily clear (and the confusion with mathematic variable is automatic). So if you answer, please either be a newcomer or try to be one. Claiming as Bruno in [comment:13 comment:13] that the syntax is very simple is a bit of a lie.\n\nVincent",
    "created_at": "2015-04-14T13:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41055",
    "user": "vdelecroix"
}
```

All right, let me start again.

1. I agree with all of you on what **I** am doing every day to implement a polynomial ring in Sage. The syntax `R.<x,y> = QQ[]` is compact and useful.

2. My comment was about newcomers for which the concept of a Python variable is not necessarily clear (and the confusion with mathematic variable is automatic). So if you answer, please either be a newcomer or try to be one. Claiming as Bruno in [comment:13 comment:13] that the syntax is very simple is a bit of a lie.

Vincent



---

archive/issue_comments_041056.json:
```json
{
    "body": "If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.",
    "created_at": "2015-04-14T13:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41056",
    "user": "mmezzarobba"
}
```

If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.



---

archive/issue_comments_041057.json:
```json
{
    "body": "Replying to [comment:17 mmezzarobba]:\n> If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.\n\nTrue. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.",
    "created_at": "2015-04-14T13:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41057",
    "user": "vdelecroix"
}
```

Replying to [comment:17 mmezzarobba]:
> If the compact syntax is confusing for newcomers (which I agree it may be), I think we should better explain it in tutorials and other documentation targetted at newcomers, not avoid using it in reference documentation. So I don't see what the problem has to do with this ticket.

True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.



---

archive/issue_comments_041058.json:
```json
{
    "body": "Replying to [comment:18 vdelecroix]:\n> True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.\n\nThen add a paragraph or two to explain the syntax in well-chosen docstrings...\n\nDo you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?",
    "created_at": "2015-04-14T13:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41058",
    "user": "mmezzarobba"
}
```

Replying to [comment:18 vdelecroix]:
> True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.

Then add a paragraph or two to explain the syntax in well-chosen docstrings...

Do you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?



---

archive/issue_comments_041059.json:
```json
{
    "body": "Replying to [comment:19 mmezzarobba]:\n> Replying to [comment:18 vdelecroix]:\n> > True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.\n> \n> Then add a paragraph or two to explain the syntax in well-chosen docstrings...\n\nWill do.\n\n> Do you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?\n\nI don't know. Some researcher in algebraic geometry might.",
    "created_at": "2015-04-14T13:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41059",
    "user": "vdelecroix"
}
```

Replying to [comment:19 mmezzarobba]:
> Replying to [comment:18 vdelecroix]:
> > True. But the point is that `sage: my_object?` is also an entry point for newcomers. I am fine to have the compact syntax in `ideal` or `elliptic_curves`. But I would avoid it without explanations in  `polynomial_element.pyx` for example.
> 
> Then add a paragraph or two to explain the syntax in well-chosen docstrings...

Will do.

> Do you really see `Polynomial.valuation?` as something people who don't know how to define basic objects are likely to read?

I don't know. Some researcher in algebraic geometry might.



---

archive/issue_comments_041060.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-04-15T17:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41060",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_041061.json:
```json
{
    "body": "I will update a commit in a minute. Few questions first:\n\n- what about other parts of the doc? (I have a commit ready for that)\n- what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)\n- what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?\n\nVincent",
    "created_at": "2015-04-15T17:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41061",
    "user": "vdelecroix"
}
```

I will update a commit in a minute. Few questions first:

- what about other parts of the doc? (I have a commit ready for that)
- what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
- what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?

Vincent



---

archive/issue_comments_041062.json:
```json
{
    "body": "Replying to [comment:21 vdelecroix]:\n> I will update a commit in a minute. Few questions first:\n> \n> - what about other parts of the doc? (I have a commit ready for that)\n\nWhich \u201cother parts\u201d are you talking about?\n\n> - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)\n> - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?\n\nIn library code, they are very useful!",
    "created_at": "2015-04-15T17:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41062",
    "user": "mmezzarobba"
}
```

Replying to [comment:21 vdelecroix]:
> I will update a commit in a minute. Few questions first:
> 
> - what about other parts of the doc? (I have a commit ready for that)

Which “other parts” are you talking about?

> - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
> - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?

In library code, they are very useful!



---

archive/issue_comments_041063.json:
```json
{
    "body": "Replying to [comment:22 mmezzarobba]:\n> Replying to [comment:21 vdelecroix]:\n> > I will update a commit in a minute. Few questions first:\n> > \n> > - what about other parts of the doc? (I have a commit ready for that)\n> \n> Which \u201cother parts\u201d are you talking about?\n\nNumber field\n\n```\nsage: K.<a> = NumberField(x^2 - 2)\n```\n\nFinite fields\n\n```\nsage: K.<a> = GF(3^5)\n```\n\nPower series\n\n```\nsage: R.<x> = QQ[[]]\n```\n\nDirichlet group\n\n```\nsage: G.<e> = DirichletGroup(20)\n```\n\nThere are more or less a dozen of files (including `sage/schemes` and `sage/modular`).\n\n> > - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)\n> > - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?\n> \n> In library code, they are very useful!\n\nI agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?\n\nVincent\n\nPS: Not speaking about the fact that\n\n```\nK = NumberField(x^2 - 2, 'a')\na = K.gen()\n```\n\nis faster, less cryptic and more economic in characters than\n\n```\nK,a = NumberField(x^2-2,'a').objgen()\n```\n",
    "created_at": "2015-04-15T17:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41063",
    "user": "vdelecroix"
}
```

Replying to [comment:22 mmezzarobba]:
> Replying to [comment:21 vdelecroix]:
> > I will update a commit in a minute. Few questions first:
> > 
> > - what about other parts of the doc? (I have a commit ready for that)
> 
> Which “other parts” are you talking about?

Number field

```
sage: K.<a> = NumberField(x^2 - 2)
```

Finite fields

```
sage: K.<a> = GF(3^5)
```

Power series

```
sage: R.<x> = QQ[[]]
```

Dirichlet group

```
sage: G.<e> = DirichletGroup(20)
```

There are more or less a dozen of files (including `sage/schemes` and `sage/modular`).

> > - what about the call to `objgen` or `objgens` in the code? (I have a commit to get rid of that)
> > - what about deprecating the global functions `objgen` and `objgens` as well as the methods on `CategoryObject`?
> 
> In library code, they are very useful!

I agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?

Vincent

PS: Not speaking about the fact that

```
K = NumberField(x^2 - 2, 'a')
a = K.gen()
```

is faster, less cryptic and more economic in characters than

```
K,a = NumberField(x^2-2,'a').objgen()
```




---

archive/issue_comments_041064.json:
```json
{
    "body": "Replying to [comment:23 vdelecroix]:\n> > Which \u201cother parts\u201d are you talking about?\n> \n> Number field\n[...]\n> There are more or less a dozen of files (including `sage/schemes` and `sage/modular`).\n\nYes, why not. To be honest I made the changes here because I stumbled upon this ticket and thought it would take five minutes and make one years-old open ticket less, but I don't really care about the problem.\n\n> I agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?\n\nOkay, I misunderstood, sorry. I don't know.\n\n> PS: Not speaking about the fact that\n> {{{\n> K = NumberField(x^2 - 2, 'a')\n> a = K.gen()\n> }}}\n> is faster, less cryptic and more economic in characters than\n> {{{\n> K,a = NumberField(x^2-2,'a').objgen()\n> }}}\n\nI actually tend to find the latter more readable, mostly because it only takes one line.",
    "created_at": "2015-04-15T17:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41064",
    "user": "mmezzarobba"
}
```

Replying to [comment:23 vdelecroix]:
> > Which “other parts” are you talking about?
> 
> Number field
[...]
> There are more or less a dozen of files (including `sage/schemes` and `sage/modular`).

Yes, why not. To be honest I made the changes here because I stumbled upon this ticket and thought it would take five minutes and make one years-old open ticket less, but I don't really care about the problem.

> I agree that the method is useful on number fields, polynomial rings, power series. But at the level of category objects or parent?

Okay, I misunderstood, sorry. I don't know.

> PS: Not speaking about the fact that
> {{{
> K = NumberField(x^2 - 2, 'a')
> a = K.gen()
> }}}
> is faster, less cryptic and more economic in characters than
> {{{
> K,a = NumberField(x^2-2,'a').objgen()
> }}}

I actually tend to find the latter more readable, mostly because it only takes one line.



---

archive/issue_comments_041065.json:
```json
{
    "body": "Rebased on sge-6.7.beta0 with a new commit.\n----\nNew commits:",
    "created_at": "2015-04-15T17:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41065",
    "user": "vdelecroix"
}
```

Rebased on sge-6.7.beta0 with a new commit.
----
New commits:



---

archive/issue_comments_041066.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-04-15T17:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41066",
    "user": "vdelecroix"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_041067.json:
```json
{
    "body": "* I'm wondering why you made this change:\n\n```\n--- a/src/sage/rings/polynomial/polynomial_element.pyx\n+++ b/src/sage/rings/polynomial/polynomial_element.pyx\n@@ -181,8 +181,12 @@ cdef class Polynomial(CommutativeAlgebraElement):\n \n     EXAMPLE::\n \n-        sage: R.<y> = QQ['y']\n-        sage: S.<x> = R['x']\n+        sage: R = QQ['x']['y']\n+        sage: R\n+        Univariate Polynomial Ring in y over Univariate Polynomial Ring in x\n+        over Rational Field\n+        sage: y = R.gen()\n+        sage: x = R.base_ring().gen()\n         sage: f = x*y; f\n         y*x\n         sage: type(f)\n```\n\n\n* Does this work? How?\n\n```\n--- a/src/sage/schemes/generic/algebraic_scheme.py\n+++ b/src/sage/schemes/generic/algebraic_scheme.py\n@@ -194,7 +194,7 @@ def is_AlgebraicScheme(x):\n \n     We create a more complicated closed subscheme::\n \n-        sage: A, x = AffineSpace(10, QQ).objgens()\n+        sage: A = AffineSpace(10, QQ)\n         sage: X = A.subscheme([sum(x)]); X\n         Closed subscheme of Affine Space of dimension 10 over Rational Field defined by:\n         x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9\n```\n\n\n* Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.\n\n```\n The third argument specifies the printing names of the generators\n-of the homogenous coordinate ring. Using objgens() you can obtain\n-both the space and the generators as ready to use variables.\n+of the homogenous coordinate ring. Using the special syntax with\n+``<`` and ``>>`` you can obtain both the space and the generators as ready to\n+use variables.\n```\n",
    "created_at": "2015-04-18T10:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41067",
    "user": "mmezzarobba"
}
```

* I'm wondering why you made this change:

```
--- a/src/sage/rings/polynomial/polynomial_element.pyx
+++ b/src/sage/rings/polynomial/polynomial_element.pyx
@@ -181,8 +181,12 @@ cdef class Polynomial(CommutativeAlgebraElement):
 
     EXAMPLE::
 
-        sage: R.<y> = QQ['y']
-        sage: S.<x> = R['x']
+        sage: R = QQ['x']['y']
+        sage: R
+        Univariate Polynomial Ring in y over Univariate Polynomial Ring in x
+        over Rational Field
+        sage: y = R.gen()
+        sage: x = R.base_ring().gen()
         sage: f = x*y; f
         y*x
         sage: type(f)
```


* Does this work? How?

```
--- a/src/sage/schemes/generic/algebraic_scheme.py
+++ b/src/sage/schemes/generic/algebraic_scheme.py
@@ -194,7 +194,7 @@ def is_AlgebraicScheme(x):
 
     We create a more complicated closed subscheme::
 
-        sage: A, x = AffineSpace(10, QQ).objgens()
+        sage: A = AffineSpace(10, QQ)
         sage: X = A.subscheme([sum(x)]); X
         Closed subscheme of Affine Space of dimension 10 over Rational Field defined by:
         x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
```


* Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.

```
 The third argument specifies the printing names of the generators
-of the homogenous coordinate ring. Using objgens() you can obtain
-both the space and the generators as ready to use variables.
+of the homogenous coordinate ring. Using the special syntax with
+``<`` and ``>>`` you can obtain both the space and the generators as ready to
+use variables.
```




---

archive/issue_comments_041068.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-18T10:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41068",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041069.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2015-04-18T10:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41069",
    "user": "mmezzarobba"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_041070.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-18T11:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41070",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_041071.json:
```json
{
    "body": "Replying to [comment:26 mmezzarobba]:\n> * I'm wondering why you made this change:\n\nRight, it is not really better. Reverted.\n\n> * Does this work? How?\n\nIt does not.\n\n> * Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.\n\ndone.",
    "created_at": "2015-04-18T11:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41071",
    "user": "vdelecroix"
}
```

Replying to [comment:26 mmezzarobba]:
> * I'm wondering why you made this change:

Right, it is not really better. Reverted.

> * Does this work? How?

It does not.

> * Shouldn't `>>` be `>` here? Also, I would add a mention of `.<>` without removing that of `objgens()`.

done.



---

archive/issue_comments_041072.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-18T17:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41072",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_041073.json:
```json
{
    "body": "I pushed a small fix to your fix (not tested, I'm having trouble with my development build at the moment).\n\nOne more comment: exemples like `A, z = R.poly_ring().objgen()` are typical cases where I would have kept the `objgens` version. But I have no problem with your version, do as you prefer.\n\nIf you are okay with my commits and assuming all tests pass, please feel free to set the ticket to positive review.",
    "created_at": "2015-04-18T18:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41073",
    "user": "mmezzarobba"
}
```

I pushed a small fix to your fix (not tested, I'm having trouble with my development build at the moment).

One more comment: exemples like `A, z = R.poly_ring().objgen()` are typical cases where I would have kept the `objgens` version. But I have no problem with your version, do as you prefer.

If you are okay with my commits and assuming all tests pass, please feel free to set the ticket to positive review.



---

archive/issue_comments_041074.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-19T06:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41074",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_041075.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-19T06:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41075",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041076.json:
```json
{
    "body": "Turns out the tests didn't pass, but now they should.",
    "created_at": "2015-04-19T06:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41076",
    "user": "mmezzarobba"
}
```

Turns out the tests didn't pass, but now they should.



---

archive/issue_comments_041077.json:
```json
{
    "body": "They do!",
    "created_at": "2015-04-20T11:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41077",
    "user": "vdelecroix"
}
```

They do!



---

archive/issue_comments_041078.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-20T11:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41078",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-21T00:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5332#issuecomment-41079",
    "user": "vbraun"
}
```

Resolution: fixed
