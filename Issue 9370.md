# Issue 9370: customize printing of elements in CombinatorialFreeModules

archive/issues_009370.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nThe attached patch allows customization of printing of elements in the class `CombinatorialFreeModuleElement`.  It also adds documentation to `CombinatorialFreeModule` spelling out these options (and all of the other options, I think).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9370\n\n",
    "created_at": "2010-06-29T04:09:11Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "customize printing of elements in CombinatorialFreeModules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9370",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: sage-combinat

CC:  sage-combinat

The attached patch allows customization of printing of elements in the class `CombinatorialFreeModuleElement`.  It also adds documentation to `CombinatorialFreeModule` spelling out these options (and all of the other options, I think).

Issue created by migration from https://trac.sagemath.org/ticket/9370





---

archive/issue_comments_088872.json:
```json
{
    "body": "Hello John,\n\nI like your ideas. I have a few quick comments for you now.\n\nComments on the docstring for `CombinatorialFreeModule`:\n\n\n```                                                                             \n    - ``basis_keys`` - list, tuple, family, set, etc. defining the \n      basis of this module\n```\n\nbasis_keys provides the indexing set for the basis, not the basis itself.\n \n\n```\n    - ``element_class`` - the class of which elements of this module\n      should be instances (optional, default None)\n```\n\nI understand that the default argument is None, but it would be nice to\nhave a description of the class used in that case since elements are not \ninstances of None.\n \n\n```\n    - ``prefix`` - prefix used for printing elements of this module\n      (optional, default 'B').  With the default, a monomial indexed\n      by 'a' would be printed as ``B['a']``.\n \n    - ``latex_prefix`` - prefix used in the LaTeX representation of\n      elements (optional, default same as 'prefix').  With the \n      default, a monomial indexed by 'a' would be printed as\n      ``B_{a}``.  If this is the empty string, then don't print\n      monomials as subscripts: the monomial indexed by 'a' would be\n      printed as ``a``, or as ``[a]`` if ``latex_bracket`` is True.\n```\n\nIt doesn't say here, but it seems that prefix and latex_prefix are supposed\nto be strings. Or anything that concatenates with a string (for example, I\nthink any instance of LatexExpr will work).\n \n\n```\n    - ``repr_bracket`` - whether to print a bracket when printing\n      elements (optional, default True).  If it is one of \"[\", \"(\", or\n      \"{\", use it and its partner as brackets.  If this is any other\n      string, use it as both brackets.\n```\n\nPlease describe what bracket gets used with the default option. Also, the \ncode sets the default to None, not True.\n\nAnd perhaps a method called print_options might be useful (instead of pointing the user to an \"internal\" attribute). With no arguments, it will return _print_options and otherwise it will set the appropriate option. For example,\n\n```\nsage: A.print_options(repr_bracket=\"|\") # to change repr_bracket\n```\n\nWhat do you think?",
    "created_at": "2010-06-30T14:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88872",
    "user": "https://github.com/saliola"
}
```

Hello John,

I like your ideas. I have a few quick comments for you now.

Comments on the docstring for `CombinatorialFreeModule`:


```                                                                             
    - ``basis_keys`` - list, tuple, family, set, etc. defining the 
      basis of this module
```

basis_keys provides the indexing set for the basis, not the basis itself.
 

```
    - ``element_class`` - the class of which elements of this module
      should be instances (optional, default None)
```

I understand that the default argument is None, but it would be nice to
have a description of the class used in that case since elements are not 
instances of None.
 

```
    - ``prefix`` - prefix used for printing elements of this module
      (optional, default 'B').  With the default, a monomial indexed
      by 'a' would be printed as ``B['a']``.
 
    - ``latex_prefix`` - prefix used in the LaTeX representation of
      elements (optional, default same as 'prefix').  With the 
      default, a monomial indexed by 'a' would be printed as
      ``B_{a}``.  If this is the empty string, then don't print
      monomials as subscripts: the monomial indexed by 'a' would be
      printed as ``a``, or as ``[a]`` if ``latex_bracket`` is True.
```

It doesn't say here, but it seems that prefix and latex_prefix are supposed
to be strings. Or anything that concatenates with a string (for example, I
think any instance of LatexExpr will work).
 

```
    - ``repr_bracket`` - whether to print a bracket when printing
      elements (optional, default True).  If it is one of "[", "(", or
      "{", use it and its partner as brackets.  If this is any other
      string, use it as both brackets.
```

Please describe what bracket gets used with the default option. Also, the 
code sets the default to None, not True.

And perhaps a method called print_options might be useful (instead of pointing the user to an "internal" attribute). With no arguments, it will return _print_options and otherwise it will set the appropriate option. For example,

```
sage: A.print_options(repr_bracket="|") # to change repr_bracket
```

What do you think?



---

archive/issue_comments_088873.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-30T14:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88873",
    "user": "https://github.com/saliola"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_088874.json:
```json
{
    "body": "Replying to [comment:1 saliola]:\n> Hello John,\n\nThanks for your comments.\n\n> basis_keys provides the indexing set for the basis, not the basis itself.\n\nFixed.\n\n> ``element_class``: I understand that the default argument is None, but it would be nice to\n> have a description of the class used in that case since elements are not \n> instances of None.\n\nFixed, I think.\n\n> It doesn't say here, but it seems that prefix and latex_prefix are supposed\n> to be strings. Or anything that concatenates with a string (for example, I\n> think any instance of LatexExpr will work).\n\nI've documented that they should be strings.  It's true that a `LatexExpr` will work, but I don't think we need to spell that out.\n\n> ``repr_bracket``: Please describe what bracket gets used with the default option. Also, the \n> code sets the default to None, not True.\n\nI've expanded on the explanation here.\n \n> And perhaps a method called print_options might be useful (instead of pointing the user to an \"internal\" attribute). With no arguments, it will return _print_options and otherwise it will set the appropriate option. \n\nGood idea, I've implemented this.",
    "created_at": "2010-06-30T16:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88874",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:1 saliola]:
> Hello John,

Thanks for your comments.

> basis_keys provides the indexing set for the basis, not the basis itself.

Fixed.

> ``element_class``: I understand that the default argument is None, but it would be nice to
> have a description of the class used in that case since elements are not 
> instances of None.

Fixed, I think.

> It doesn't say here, but it seems that prefix and latex_prefix are supposed
> to be strings. Or anything that concatenates with a string (for example, I
> think any instance of LatexExpr will work).

I've documented that they should be strings.  It's true that a `LatexExpr` will work, but I don't think we need to spell that out.

> ``repr_bracket``: Please describe what bracket gets used with the default option. Also, the 
> code sets the default to None, not True.

I've expanded on the explanation here.
 
> And perhaps a method called print_options might be useful (instead of pointing the user to an "internal" attribute). With no arguments, it will return _print_options and otherwise it will set the appropriate option. 

Good idea, I've implemented this.



---

archive/issue_comments_088875.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T16:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88875",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088876.json:
```json
{
    "body": "Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right.  It wouldn't be hard to implement, but is it worth doing?  Would the documentation start to get too complicated?",
    "created_at": "2010-06-30T17:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88876",
    "user": "https://github.com/jhpalmieri"
}
```

Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right.  It wouldn't be hard to implement, but is it worth doing?  Would the documentation start to get too complicated?



---

archive/issue_comments_088877.json:
```json
{
    "body": "> Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right. It wouldn't be hard to implement, but is it worth doing? Would the documentation start to get too complicated?\n\nHere's a patch which implements this idea.  I think it's probably worth doing: consider\n\n```\nsage: F = CombinatorialFreeModule(QQ, [1,2,3], prefix='x', repr_bracket=[\"_{\", \"}\"])\nsage: e = F.basis()\nsage: e[2] + 5*e[3]\nx_{2} + 5*x_{3}\n```\n",
    "created_at": "2010-06-30T18:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88877",
    "user": "https://github.com/jhpalmieri"
}
```

> Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right. It wouldn't be hard to implement, but is it worth doing? Would the documentation start to get too complicated?

Here's a patch which implements this idea.  I think it's probably worth doing: consider

```
sage: F = CombinatorialFreeModule(QQ, [1,2,3], prefix='x', repr_bracket=["_{", "}"])
sage: e = F.basis()
sage: e[2] + 5*e[3]
x_{2} + 5*x_{3}
```




---

archive/issue_comments_088878.json:
```json
{
    "body": "Note: these print option interact with unique representation in ways which might be surprising, but this was also true with `F._prefix`.  I've added an example to the documentation illustrating this, starting at line 849.",
    "created_at": "2010-07-01T04:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88878",
    "user": "https://github.com/jhpalmieri"
}
```

Note: these print option interact with unique representation in ways which might be surprising, but this was also true with `F._prefix`.  I've added an example to the documentation illustrating this, starting at line 849.



---

archive/issue_comments_088879.json:
```json
{
    "body": "ping to saliola: what do you think about the changes in response to your comments?",
    "created_at": "2010-09-28T02:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88879",
    "user": "https://github.com/jasongrout"
}
```

ping to saliola: what do you think about the changes in response to your comments?



---

archive/issue_comments_088880.json:
```json
{
    "body": "I forgot about this ticket. Thanks for the ping, Jason.\n\nI like the changes. As long as all the tests pass, it gets a positive review from me. (I don't really have the time this week to upgrade my Sage installation to test this; if someone else can do it beforehand, that would be great!)",
    "created_at": "2010-09-28T05:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88880",
    "user": "https://github.com/saliola"
}
```

I forgot about this ticket. Thanks for the ping, Jason.

I like the changes. As long as all the tests pass, it gets a positive review from me. (I don't really have the time this week to upgrade my Sage installation to test this; if someone else can do it beforehand, that would be great!)



---

archive/issue_comments_088881.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> > Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right. It wouldn't be hard to implement, but is it worth doing? Would the documentation start to get too complicated?\n> \n> Here's a patch which implements this idea.  I think it's probably worth doing: consider\n> {{{\n> sage: F = CombinatorialFreeModule(QQ, [1,2,3], prefix='x', repr_bracket=[\"_{\", \"}\"])\n> sage: e = F.basis()\n> sage: e[2] + 5*e[3]\n> x_{2} + 5*x_{3}\n> }}}\n\n+1",
    "created_at": "2010-09-30T10:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88881",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 jhpalmieri]:
> > Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right. It wouldn't be hard to implement, but is it worth doing? Would the documentation start to get too complicated?
> 
> Here's a patch which implements this idea.  I think it's probably worth doing: consider
> {{{
> sage: F = CombinatorialFreeModule(QQ, [1,2,3], prefix='x', repr_bracket=["_{", "}"])
> sage: e = F.basis()
> sage: e[2] + 5*e[3]
> x_{2} + 5*x_{3}
> }}}

+1



---

archive/issue_comments_088882.json:
```json
{
    "body": "Hi John,\n\nSorry for letting this patch rot ... I like it much though! Thanks! As you, I am bothered by the current interaction between unique representation and printing customization, but don't have a good solution at this point.\n\nI just went briefly through it. Three minor suggestions:\n- The logic in print_options could be factored out using something along:\n\n```\n    for option in ['latex_prefix',...]:\n        if option in kwds: \n            args = True \n \t    self._print_options[option] = kwds[option]\n```\n\n\n- The documentation of set_print_options duplicates that of the constructor. Could one of them just refer to the other? ``for the options ... see ...``. Actually, maybe the constructor should call set_print_options?\n\n- Could we find something better than _repr_asterix? That is that would refer more explicitly to scalar multiplication? In MuPAD it was timesDot, but it's not great either.",
    "created_at": "2010-09-30T10:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88882",
    "user": "https://github.com/nthiery"
}
```

Hi John,

Sorry for letting this patch rot ... I like it much though! Thanks! As you, I am bothered by the current interaction between unique representation and printing customization, but don't have a good solution at this point.

I just went briefly through it. Three minor suggestions:
- The logic in print_options could be factored out using something along:

```
    for option in ['latex_prefix',...]:
        if option in kwds: 
            args = True 
 	    self._print_options[option] = kwds[option]
```


- The documentation of set_print_options duplicates that of the constructor. Could one of them just refer to the other? ``for the options ... see ...``. Actually, maybe the constructor should call set_print_options?

- Could we find something better than _repr_asterix? That is that would refer more explicitly to scalar multiplication? In MuPAD it was timesDot, but it's not great either.



---

archive/issue_comments_088883.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-30T10:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88883",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088884.json:
```json
{
    "body": "Hi Nicolas,\n\nThanks for the feedback.  I've changed the code in print_options the way you suggested, and I shortened the docstring there.  I wasn't comfortable having the constructor call print_options, so I didn't change that.\n\nI agree that \"repr_asterisk\" is a bad name, so I rethought the names.  We already had \"prefix\" to which I added \"latex_prefix\".  In parallel with this, I changed \"repr_bracket\" to \"bracket\" (to go with my addition, \"latex_bracket\").  That means that there is no reason for \"repr_asterisk\" to have \"repr\" in its name anymore.  I changed that to \"scalar_mult\".  I think this is better:\n\n```\n    - ``scalar_mult`` - string to use for scalar multiplication in\n      the print representation (optional, default \"*\")\n```\n\nWhat do you think?",
    "created_at": "2010-09-30T20:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88884",
    "user": "https://github.com/jhpalmieri"
}
```

Hi Nicolas,

Thanks for the feedback.  I've changed the code in print_options the way you suggested, and I shortened the docstring there.  I wasn't comfortable having the constructor call print_options, so I didn't change that.

I agree that "repr_asterisk" is a bad name, so I rethought the names.  We already had "prefix" to which I added "latex_prefix".  In parallel with this, I changed "repr_bracket" to "bracket" (to go with my addition, "latex_bracket").  That means that there is no reason for "repr_asterisk" to have "repr" in its name anymore.  I changed that to "scalar_mult".  I think this is better:

```
    - ``scalar_mult`` - string to use for scalar multiplication in
      the print representation (optional, default "*")
```

What do you think?



---

archive/issue_comments_088885.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-30T20:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88885",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088886.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr.patch) by stumpc5 created at 2011-02-26 00:51:50\n\nHi,\n\nI will fold #10852 in here, if that's okay.\n\nI like the multiple options! I gonna have a more detailed look for a review; here are two first comments:\n\n1. Why do you handle the old prefix option extra? Wouldn't it be enough to keep the prefix method and return to print_options()[\\'prefix\\'], rather thank keeping _prefix. A complete doctest provided by the buildbot can then check if _prefix is used anywhere.\n\n2. in lines 155p, multiplication is set to ast. Isn't there a way to give this argument to the repr_lincomb method? Otherwise, we get the following:\n\n```\nsage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='@@')\nsage: A.an_element()\n2@@B['@@'] + 2@@B['+']\n```\n\n\nBest, Christian",
    "created_at": "2011-02-26T00:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88886",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Attachment [trac_9370-module-elt-repr.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr.patch) by stumpc5 created at 2011-02-26 00:51:50

Hi,

I will fold #10852 in here, if that's okay.

I like the multiple options! I gonna have a more detailed look for a review; here are two first comments:

1. Why do you handle the old prefix option extra? Wouldn't it be enough to keep the prefix method and return to print_options()[\'prefix\'], rather thank keeping _prefix. A complete doctest provided by the buildbot can then check if _prefix is used anywhere.

2. in lines 155p, multiplication is set to ast. Isn't there a way to give this argument to the repr_lincomb method? Otherwise, we get the following:

```
sage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='@@')
sage: A.an_element()
2@@B['@@'] + 2@@B['+']
```


Best, Christian



---

archive/issue_comments_088887.json:
```json
{
    "body": "Replying to [comment:11 stumpc5]:\n> Hi,\n> \n> I will fold #10852 in here, if that's okay.\n> \n> I like the multiple options! I gonna have a more detailed look for a review; here are two first comments:\n> \n> 1. Why do you handle the old prefix option extra? Wouldn't it be enough to keep the prefix method and return to print_options()[\\'prefix\\'], rather thank keeping _prefix. A complete doctest provided by the buildbot can then check if _prefix is used anywhere.\n\nI think it was just to preserve backward-compatibility, but if you think it's safe to remove it, please go ahead.\n\n> 2. in lines 155p, multiplication is set to ast. Isn't there a way to give this argument to the repr_lincomb method? Otherwise, we get the following:\n\n```\nsage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='@@')\nsage: A.an_element()\n2@@B['@@'] + 2@@B['+']\n```\n\n\nPutting it in repr_lincomb would be better, I agree.",
    "created_at": "2011-02-26T02:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88887",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:11 stumpc5]:
> Hi,
> 
> I will fold #10852 in here, if that's okay.
> 
> I like the multiple options! I gonna have a more detailed look for a review; here are two first comments:
> 
> 1. Why do you handle the old prefix option extra? Wouldn't it be enough to keep the prefix method and return to print_options()[\'prefix\'], rather thank keeping _prefix. A complete doctest provided by the buildbot can then check if _prefix is used anywhere.

I think it was just to preserve backward-compatibility, but if you think it's safe to remove it, please go ahead.

> 2. in lines 155p, multiplication is set to ast. Isn't there a way to give this argument to the repr_lincomb method? Otherwise, we get the following:

```
sage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='@@')
sage: A.an_element()
2@@B['@@'] + 2@@B['+']
```


Putting it in repr_lincomb would be better, I agree.



---

archive/issue_comments_088888.json:
```json
{
    "body": "I added an additional patch containing my two suggested additional features above.\n\nIn there I made quite some changes in sage.misc.repr_lincomb which effects many files. So I want to see what the buildbot returns (as I have a segfault in sage.categories.semigroups._test_associativity, but also without having the patches applied, so I cannot do a complete test).\n\nI also removed _prefix, thus I had to make changes as well in combinat.schubert_polynomial, in combinat.symmetric_group_algebra, and in combiat.combiatorial_algebra. Is that okay, or should I undo those changes and leave _prefix?",
    "created_at": "2011-03-01T21:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88888",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

I added an additional patch containing my two suggested additional features above.

In there I made quite some changes in sage.misc.repr_lincomb which effects many files. So I want to see what the buildbot returns (as I have a segfault in sage.categories.semigroups._test_associativity, but also without having the patches applied, so I cannot do a complete test).

I also removed _prefix, thus I had to make changes as well in combinat.schubert_polynomial, in combinat.symmetric_group_algebra, and in combiat.combiatorial_algebra. Is that okay, or should I undo those changes and leave _prefix?



---

archive/issue_comments_088889.json:
```json
{
    "body": "Maybe this makes the buildbot testing the ticket again.\n\nFor the buildbot:\n\nApply trac_9370-module-elt-repr.patch, trac_9370-module-elt-repr-suggestions-cs.patch",
    "created_at": "2011-03-02T09:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88889",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Maybe this makes the buildbot testing the ticket again.

For the buildbot:

Apply trac_9370-module-elt-repr.patch, trac_9370-module-elt-repr-suggestions-cs.patch



---

archive/issue_comments_088890.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr-suggestions-cs.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-suggestions-cs.patch) by stumpc5 created at 2011-03-03 14:17:41",
    "created_at": "2011-03-03T14:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88890",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Attachment [trac_9370-module-elt-repr-suggestions-cs.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-suggestions-cs.patch) by stumpc5 created at 2011-03-03 14:17:41



---

archive/issue_comments_088891.json:
```json
{
    "body": "I'm happy with the changes except for the following things: first, there are some typos and some ways I would reword things, and I've put up a patch to go on top of \"trac_9370-module-elt-repr-suggestions-cs.patch\" to make those changes.\n\nSecond, the change in the `print_options` method makes the code simpler, but it also modifies the behavior, and I'm not sure I like the change.  If we want to keep the change, then we need to modify the documentation.  The change is this: with my original patch, if you set `prefix` but not `latex_prefix`, then `latex_prefix` would become `prefix` rather than the default value of \"B\".  With your patch, we have this behavior:\n\n```\nsage: A = HeckeAlgebraSymmetricGroupT(QQ, 3)\nsage: A.an_element()\nT[1, 2, 3] + 2*T[1, 3, 2] + 3*T[2, 1, 3] \nsage: latex(A.an_element())\nB_{[1, 2, 3]} + 2B_{[1, 3, 2]} + 3B_{[2, 1, 3]}\n```\n\nIdeally, everyone would set latex_prefix when they set prefix, but if they don't, I think they should default to being the same.",
    "created_at": "2011-03-07T23:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88891",
    "user": "https://github.com/jhpalmieri"
}
```

I'm happy with the changes except for the following things: first, there are some typos and some ways I would reword things, and I've put up a patch to go on top of "trac_9370-module-elt-repr-suggestions-cs.patch" to make those changes.

Second, the change in the `print_options` method makes the code simpler, but it also modifies the behavior, and I'm not sure I like the change.  If we want to keep the change, then we need to modify the documentation.  The change is this: with my original patch, if you set `prefix` but not `latex_prefix`, then `latex_prefix` would become `prefix` rather than the default value of "B".  With your patch, we have this behavior:

```
sage: A = HeckeAlgebraSymmetricGroupT(QQ, 3)
sage: A.an_element()
T[1, 2, 3] + 2*T[1, 3, 2] + 3*T[2, 1, 3] 
sage: latex(A.an_element())
B_{[1, 2, 3]} + 2B_{[1, 3, 2]} + 3B_{[2, 1, 3]}
```

Ideally, everyone would set latex_prefix when they set prefix, but if they don't, I think they should default to being the same.



---

archive/issue_comments_088892.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr-third.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-third.patch) by @jhpalmieri created at 2011-03-07 23:26:38\n\napply on top of other two patches",
    "created_at": "2011-03-07T23:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88892",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9370-module-elt-repr-third.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-third.patch) by @jhpalmieri created at 2011-03-07 23:26:38

apply on top of other two patches



---

archive/issue_comments_088893.json:
```json
{
    "body": "Hi Christian, John,\n\nFirst, thanks so much for improving CombinatorialFreeModule's!\n\nReplying to [comment:15 jhpalmieri]:\n> The change is this: with my original patch, if you set `prefix` but not `latex_prefix`, then `latex_prefix` would become `prefix` rather than the default value of \"B\".  With your patch, we have this behavior:\n> {{{\n> sage: A = HeckeAlgebraSymmetricGroupT(QQ, 3)\n> sage: A.an_element()\n> T[1, 2, 3] + 2*T[1, 3, 2] + 3*T[2, 1, 3] \n> sage: latex(A.an_element())\n> B_{[1, 2, 3]} + 2B_{[1, 3, 2]} + 3B_{[2, 1, 3]}\n> }}}\n> Ideally, everyone would set latex_prefix when they set prefix,\n\nI would not even try to enforce setting latex_prefix. Whenever the\nprefix does not contains specific math code, it would be an\nunnecessary burden to have to set both latex_prefix and prefix.\n\n> but if they don't, I think they should default to being the same.\n\n+1",
    "created_at": "2011-03-10T09:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88893",
    "user": "https://github.com/nthiery"
}
```

Hi Christian, John,

First, thanks so much for improving CombinatorialFreeModule's!

Replying to [comment:15 jhpalmieri]:
> The change is this: with my original patch, if you set `prefix` but not `latex_prefix`, then `latex_prefix` would become `prefix` rather than the default value of "B".  With your patch, we have this behavior:
> {{{
> sage: A = HeckeAlgebraSymmetricGroupT(QQ, 3)
> sage: A.an_element()
> T[1, 2, 3] + 2*T[1, 3, 2] + 3*T[2, 1, 3] 
> sage: latex(A.an_element())
> B_{[1, 2, 3]} + 2B_{[1, 3, 2]} + 3B_{[2, 1, 3]}
> }}}
> Ideally, everyone would set latex_prefix when they set prefix,

I would not even try to enforce setting latex_prefix. Whenever the
prefix does not contains specific math code, it would be an
unnecessary burden to have to set both latex_prefix and prefix.

> but if they don't, I think they should default to being the same.

+1



---

archive/issue_comments_088894.json:
```json
{
    "body": "Here are two new patches.  The first is a replacement for \"trac_9370-module-elt-repr-third.patch\", and the second is an all-in-one patch incorporating all changes.\n\nThese restore the old behavior of setting prefix vs. latex_prefix.  In fact, now if you set prefix but not latex_prefix, then the latex_prefix option remains set to None, and whenever latex_prefix is used, if it's set to None, it just uses the prefix setting instead.  This makes some of the code cleaner.\n\nThese patches also document tensor_symbol and latex_scalar_mult.",
    "created_at": "2011-03-11T05:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88894",
    "user": "https://github.com/jhpalmieri"
}
```

Here are two new patches.  The first is a replacement for "trac_9370-module-elt-repr-third.patch", and the second is an all-in-one patch incorporating all changes.

These restore the old behavior of setting prefix vs. latex_prefix.  In fact, now if you set prefix but not latex_prefix, then the latex_prefix option remains set to None, and whenever latex_prefix is used, if it's set to None, it just uses the prefix setting instead.  This makes some of the code cleaner.

These patches also document tensor_symbol and latex_scalar_mult.



---

archive/issue_comments_088895.json:
```json
{
    "body": "Just to be clear, the \"v2\" version of the third patch is for review purposes.\n\nApply only \n\n- trac_9370-module-elt-repr-all-in-one.patch",
    "created_at": "2011-03-11T05:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88895",
    "user": "https://github.com/jhpalmieri"
}
```

Just to be clear, the "v2" version of the third patch is for review purposes.

Apply only 

- trac_9370-module-elt-repr-all-in-one.patch



---

archive/issue_comments_088896.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr-third.v2.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-third.v2.patch) by @jhpalmieri created at 2011-03-11 05:56:28\n\napply on top of other two patches instead of ...-third.patch",
    "created_at": "2011-03-11T05:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88896",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9370-module-elt-repr-third.v2.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-third.v2.patch) by @jhpalmieri created at 2011-03-11 05:56:28

apply on top of other two patches instead of ...-third.patch



---

archive/issue_comments_088897.json:
```json
{
    "body": "The Steenrod algebra code at #10052 revealed a small bug in the `_latex_` method: when replacing a trailing \"* 1\" in latex code via\n\n```\nif x[len(x)-l-1:] == ast_replace+\"1\": \n     return x[:len(x)-l-1] \n```\n\nif `ast_replace` is the empty string, this will just remove any trailing 1, for example from \"x \\otimes 1\" or from \"31\", etc.  So I'm changing the test to\n\n```\nif l > 0 and x[len(x)-l-1:] == ast_replace+\"1\": \n     return x[:len(x)-l-1] \n```\n\nso it only does the replacement if the length `l` of `ast_replace` is positive.  (I also find the letter \"l\" hard to distinguish from the number \"1\", so I'm changing it to \"ln\".  Then we can pretend it's the natural log and we're doing calculus instead of algebra.)",
    "created_at": "2011-03-11T22:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88897",
    "user": "https://github.com/jhpalmieri"
}
```

The Steenrod algebra code at #10052 revealed a small bug in the `_latex_` method: when replacing a trailing "* 1" in latex code via

```
if x[len(x)-l-1:] == ast_replace+"1": 
     return x[:len(x)-l-1] 
```

if `ast_replace` is the empty string, this will just remove any trailing 1, for example from "x \otimes 1" or from "31", etc.  So I'm changing the test to

```
if l > 0 and x[len(x)-l-1:] == ast_replace+"1": 
     return x[:len(x)-l-1] 
```

so it only does the replacement if the length `l` of `ast_replace` is positive.  (I also find the letter "l" hard to distinguish from the number "1", so I'm changing it to "ln".  Then we can pretend it's the natural log and we're doing calculus instead of algebra.)



---

archive/issue_comments_088898.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr-fourth.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-fourth.patch) by @jhpalmieri created at 2011-03-11 22:36:24\n\napply on top of first 3 patches, for review only",
    "created_at": "2011-03-11T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88898",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9370-module-elt-repr-fourth.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-fourth.patch) by @jhpalmieri created at 2011-03-11 22:36:24

apply on top of first 3 patches, for review only



---

archive/issue_comments_088899.json:
```json
{
    "body": "Attachment [trac_9370-module-elt-repr-all-in-one.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-all-in-one.patch) by @jhpalmieri created at 2011-03-11 22:37:08\n\napply only this patch",
    "created_at": "2011-03-11T22:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88899",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9370-module-elt-repr-all-in-one.patch](tarball://root/attachments/some-uuid/ticket9370/trac_9370-module-elt-repr-all-in-one.patch) by @jhpalmieri created at 2011-03-11 22:37:08

apply only this patch



---

archive/issue_comments_088900.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-12T12:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88900",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088901.json:
```json
{
    "body": "I haven't found any further issues; as all tests pass, so it gets a positive review.\n\nBest, Christian",
    "created_at": "2011-03-12T12:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88901",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

I haven't found any further issues; as all tests pass, so it gets a positive review.

Best, Christian



---

archive/issue_events_009525.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-04-07T13:49:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9370#event-9525"
}
```



---

archive/issue_comments_088902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T13:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9370#issuecomment-88902",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
