# Issue 9370: customize printing of elements in CombinatorialFreeModules

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-29 04:09:11

Assignee: sage-combinat

CC:  sage-combinat

The attached patch allows customization of printing of elements in the class `CombinatorialFreeModuleElement`.  It also adds documentation to `CombinatorialFreeModule` spelling out these options (and all of the other options, I think).


---

Comment by saliola created at 2010-06-30 14:04:45

Hello John,

I like your ideas. I have a few quick comments for you now.

Comments on the docstring for `CombinatorialFreeModule`:

{{{                                                                             
    - ``basis_keys`` - list, tuple, family, set, etc. defining the 
      basis of this module
}}}
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

Comment by saliola created at 2010-06-30 14:04:45

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-06-30 16:57:52

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

Comment by jhpalmieri created at 2010-06-30 16:57:52

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-06-30 17:08:08

Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right.  It wouldn't be hard to implement, but is it worth doing?  Would the documentation start to get too complicated?


---

Comment by jhpalmieri created at 2010-06-30 18:12:59

> Another idea would be to allow repr_bracket to be a pair (list or tuple) of strings, one for the left side and one for the right. It wouldn't be hard to implement, but is it worth doing? Would the documentation start to get too complicated?

Here's a patch which implements this idea.  I think it's probably worth doing: consider

```
sage: F = CombinatorialFreeModule(QQ, [1,2,3], prefix='x', repr_bracket=["_{", "}"])
sage: e = F.basis()
sage: e[2] + 5*e[3]
x_{2} + 5*x_{3}
```



---

Comment by jhpalmieri created at 2010-07-01 04:34:26

Note: these print option interact with unique representation in ways which might be surprising, but this was also true with `F._prefix`.  I've added an example to the documentation illustrating this, starting at line 849.


---

Comment by jason created at 2010-09-28 02:41:32

ping to saliola: what do you think about the changes in response to your comments?


---

Comment by saliola created at 2010-09-28 05:33:26

I forgot about this ticket. Thanks for the ping, Jason.

I like the changes. As long as all the tests pass, it gets a positive review from me. (I don't really have the time this week to upgrade my Sage installation to test this; if someone else can do it beforehand, that would be great!)


---

Comment by nthiery created at 2010-09-30 10:03:40

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

Comment by nthiery created at 2010-09-30 10:17:05

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

Comment by nthiery created at 2010-09-30 10:17:05

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-09-30 20:19:05

Hi Nicolas,

Thanks for the feedback.  I've changed the code in print_options the way you suggested, and I shortened the docstring there.  I wasn't comfortable having the constructor call print_options, so I didn't change that.

I agree that "repr_asterisk" is a bad name, so I rethought the names.  We already had "prefix" to which I added "latex_prefix".  In parallel with this, I changed "repr_bracket" to "bracket" (to go with my addition, "latex_bracket").  That means that there is no reason for "repr_asterisk" to have "repr" in its name anymore.  I changed that to "scalar_mult".  I think this is better:

```
    - ``scalar_mult`` - string to use for scalar multiplication in
      the print representation (optional, default "*")
```

What do you think?


---

Comment by jhpalmieri created at 2010-09-30 20:19:05

Changing status from needs_work to needs_review.


---

Attachment

Hi,

I will fold #10852 in here, if that's okay.

I like the multiple options! I gonna have a more detailed look for a review; here are two first comments:

1. Why do you handle the old prefix option extra? Wouldn't it be enough to keep the prefix method and return to print_options()[\'prefix\'], rather thank keeping _prefix. A complete doctest provided by the buildbot can then check if _prefix is used anywhere.

2. in lines 155p, multiplication is set to ast. Isn't there a way to give this argument to the repr_lincomb method? Otherwise, we get the following:

```
sage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='`@``@`')
sage: A.an_element()
2`@``@`B['`@``@`'] + 2`@``@`B['+']
```


Best, Christian


---

Comment by jhpalmieri created at 2011-02-26 02:20:24

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
sage: A = CombinatorialFreeModule(QQ,['+','*'],scalar_mult='`@``@`')
sage: A.an_element()
2`@``@`B['`@``@`'] + 2`@``@`B['+']
```


Putting it in repr_lincomb would be better, I agree.


---

Comment by stumpc5 created at 2011-03-01 21:00:10

I added an additional patch containing my two suggested additional features above.

In there I made quite some changes in sage.misc.repr_lincomb which effects many files. So I want to see what the buildbot returns (as I have a segfault in sage.categories.semigroups._test_associativity, but also without having the patches applied, so I cannot do a complete test).

I also removed _prefix, thus I had to make changes as well in combinat.schubert_polynomial, in combinat.symmetric_group_algebra, and in combiat.combiatorial_algebra. Is that okay, or should I undo those changes and leave _prefix?


---

Comment by stumpc5 created at 2011-03-02 09:49:40

Maybe this makes the buildbot testing the ticket again.

For the buildbot:

Apply trac_9370-module-elt-repr.patch, trac_9370-module-elt-repr-suggestions-cs.patch


---

Attachment


---

Comment by jhpalmieri created at 2011-03-07 23:26:10

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

Attachment

apply on top of other two patches


---

Comment by nthiery created at 2011-03-10 09:57:59

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

Comment by jhpalmieri created at 2011-03-11 05:51:45

Here are two new patches.  The first is a replacement for "trac_9370-module-elt-repr-third.patch", and the second is an all-in-one patch incorporating all changes.

These restore the old behavior of setting prefix vs. latex_prefix.  In fact, now if you set prefix but not latex_prefix, then the latex_prefix option remains set to None, and whenever latex_prefix is used, if it's set to None, it just uses the prefix setting instead.  This makes some of the code cleaner.

These patches also document tensor_symbol and latex_scalar_mult.


---

Comment by jhpalmieri created at 2011-03-11 05:54:04

Just to be clear, the "v2" version of the third patch is for review purposes.

Apply only 

 - trac_9370-module-elt-repr-all-in-one.patch


---

Attachment

apply on top of other two patches instead of ...-third.patch


---

Comment by jhpalmieri created at 2011-03-11 22:34:29

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

Attachment

apply on top of first 3 patches, for review only


---

Attachment

apply only this patch


---

Comment by stumpc5 created at 2011-03-12 12:23:11

Changing status from needs_review to positive_review.


---

Comment by stumpc5 created at 2011-03-12 12:23:11

I haven't found any further issues; as all tests pass, so it gets a positive review.

Best, Christian


---

Comment by jdemeyer created at 2011-04-07 13:49:58

Resolution: fixed
