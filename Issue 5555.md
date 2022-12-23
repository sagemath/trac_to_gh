# Issue 5555: [with patch, not ready for review] make some TeX macros available to docstrings

archive/issues_005555.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nWith the attached patch, you should be able to use \\ZZ, \\CC, \\RR, and \\QQ in docstrings and have them typeset correctly in the html, live html, latex, and pdf versions of the documentation.  To add new macros, edit the file '$SAGE_ROOT/devel/sage/doc/common/sage-macros.tex'.  (I considered just using the existing file 'macros.tex' in the same directory, but decided it was too bloated.)\n\nThe point here is to be able to write docstrings which are readable from interactive help in Sage and which also get typeset correctly in the reference manual; this was discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/74e6bcf5ef716d1c), and people seemed to agree that a docstring like \n\n```\nThis computes the integral homology `H_d(X, \\ZZ)` of `X` in dimension `d`. \n```\n\nwas better than\n\n```\nThis computes the integral homology `H_d(X, \\mathbb{Z})` of `X` in dimension `d`. \n```\n\nespecially since the \\ZZ gets turned into ZZ when pre-parsed for interactive help.  \n\nThis point should be kept in mind if anyone wants to add new macros: the name should be short and unambiguous, and there should be a good reason for using it instead of plain LaTeX.  (This was maybe what I meant when I said that macros.tex was too bloated.)\n\nHaving said all of that, I would be happy to add some more macros now.  What else should be added?  Once we seem to have made some sort of decision about that, I'll update the patch and mark this ticket as \"needs review\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/5555\n\n",
    "created_at": "2009-03-17T23:38:59Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, not ready for review] make some TeX macros available to docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5555",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

With the attached patch, you should be able to use \ZZ, \CC, \RR, and \QQ in docstrings and have them typeset correctly in the html, live html, latex, and pdf versions of the documentation.  To add new macros, edit the file '$SAGE_ROOT/devel/sage/doc/common/sage-macros.tex'.  (I considered just using the existing file 'macros.tex' in the same directory, but decided it was too bloated.)

The point here is to be able to write docstrings which are readable from interactive help in Sage and which also get typeset correctly in the reference manual; this was discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/74e6bcf5ef716d1c), and people seemed to agree that a docstring like 

```
This computes the integral homology `H_d(X, \ZZ)` of `X` in dimension `d`. 
```

was better than

```
This computes the integral homology `H_d(X, \mathbb{Z})` of `X` in dimension `d`. 
```

especially since the \ZZ gets turned into ZZ when pre-parsed for interactive help.  

This point should be kept in mind if anyone wants to add new macros: the name should be short and unambiguous, and there should be a good reason for using it instead of plain LaTeX.  (This was maybe what I meant when I said that macros.tex was too bloated.)

Having said all of that, I would be happy to add some more macros now.  What else should be added?  Once we seem to have made some sort of decision about that, I'll update the patch and mark this ticket as "needs review".

Issue created by migration from https://trac.sagemath.org/ticket/5555





---

archive/issue_comments_043204.json:
```json
{
    "body": "Now I need help.  'new-macros.patch' doesn't work, and I don't know why.  When I run it, I get the error message\n\n```\n% sage -docbuild reference html\nsphinx-build -b html -d /Applications/sage/devel/sage/doc/output/doctrees/en/reference   .  /Applications/sage/devel/sage/doc/output/html/en/reference\nException occurred:\n  File \"<string>\", line 1, in <module>\nNameError: name 'sage' is not defined\nThe full traceback has been saved in /var/folders/JV/JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-l-jOy1.log, if you want to report the issue to the author.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\n```\n\nThis is coming from the line\n\n```\ndefn += eval('str(latex(' + module + \".\" + name + args + '))') + '}'\n```\n\nwhich, for example, doesn't seem to like doing this:\n\n```\neval('str(latex(sage.rings.all.ZZ))')\n```\n\n(A few lines earlier, `from sage.misc.latex import latex` seems to be perfectly acceptable.)\n\nWhen I run sage and \"attach conf.py\", then the function `produce_latex_macro` works just fine.  I'm probably making some stupid Python mistake.  Can anyone help?",
    "created_at": "2009-03-19T19:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43204",
    "user": "jhpalmieri"
}
```

Now I need help.  'new-macros.patch' doesn't work, and I don't know why.  When I run it, I get the error message

```
% sage -docbuild reference html
sphinx-build -b html -d /Applications/sage/devel/sage/doc/output/doctrees/en/reference   .  /Applications/sage/devel/sage/doc/output/html/en/reference
Exception occurred:
  File "<string>", line 1, in <module>
NameError: name 'sage' is not defined
The full traceback has been saved in /var/folders/JV/JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-l-jOy1.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
```

This is coming from the line

```
defn += eval('str(latex(' + module + "." + name + args + '))') + '}'
```

which, for example, doesn't seem to like doing this:

```
eval('str(latex(sage.rings.all.ZZ))')
```

(A few lines earlier, `from sage.misc.latex import latex` seems to be perfectly acceptable.)

When I run sage and "attach conf.py", then the function `produce_latex_macro` works just fine.  I'm probably making some stupid Python mistake.  Can anyone help?



---

archive/issue_comments_043205.json:
```json
{
    "body": "Ignore my previous remark.  This is now ready for review.\n\nTo add new macros, edit these lines in conf.py:\n\n```\nsage_macros = [(\"ZZ\", \"sage.rings.all\"),\n               (\"RR\", \"sage.rings.all\"),\n               (\"CC\", \"sage.rings.all\"),\n               (\"QQ\", \"sage.rings.all\"),\n               (\"QQbar\", \"sage.rings.all\"),\n               (\"GF\", \"sage.rings.all\", 17),\n               ]\n```\n\nThe file has comments explaining what to do...",
    "created_at": "2009-03-19T19:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43205",
    "user": "jhpalmieri"
}
```

Ignore my previous remark.  This is now ready for review.

To add new macros, edit these lines in conf.py:

```
sage_macros = [("ZZ", "sage.rings.all"),
               ("RR", "sage.rings.all"),
               ("CC", "sage.rings.all"),
               ("QQ", "sage.rings.all"),
               ("QQbar", "sage.rings.all"),
               ("GF", "sage.rings.all", 17),
               ]
```

The file has comments explaining what to do...



---

archive/issue_comments_043206.json:
```json
{
    "body": "We really should/need to make it so all of this plays well with jsMath: http://www.math.union.edu/~dpvc/jsMath/authors/macros.html",
    "created_at": "2009-03-19T21:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43206",
    "user": "mhansen"
}
```

We really should/need to make it so all of this plays well with jsMath: http://www.math.union.edu/~dpvc/jsMath/authors/macros.html



---

archive/issue_comments_043207.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> We really should/need to make it so all of this plays well with jsMath: \n> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html\n\nOkay, how about this patch?",
    "created_at": "2009-03-20T01:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43207",
    "user": "jhpalmieri"
}
```

Replying to [comment:3 mhansen]:
> We really should/need to make it so all of this plays well with jsMath: 
> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html

Okay, how about this patch?



---

archive/issue_comments_043208.json:
```json
{
    "body": "(I clicked 'submit' too early.  Here's a longer reply.)\n\nReplying to [comment:3 mhansen]:\n> We really should/need to make it so all of this plays well with jsMath: \n> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html\n\nOkay, how about this patch?  This seems to allow use of the imported macros in the notebook (e.g. by shift-clicking between cells and adding \"test: $\\ZZ$\") and in the live versions of the reference manual and the tutorial. Does that definitely mean that it's working well with jsMath?  I'm not sure how to test this...",
    "created_at": "2009-03-20T02:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43208",
    "user": "jhpalmieri"
}
```

(I clicked 'submit' too early.  Here's a longer reply.)

Replying to [comment:3 mhansen]:
> We really should/need to make it so all of this plays well with jsMath: 
> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html

Okay, how about this patch?  This seems to allow use of the imported macros in the notebook (e.g. by shift-clicking between cells and adding "test: $\ZZ$") and in the live versions of the reference manual and the tutorial. Does that definitely mean that it's working well with jsMath?  I'm not sure how to test this...



---

archive/issue_comments_043209.json:
```json
{
    "body": "By the way, #5568 should be trivial to review and is somewhat related to this one.",
    "created_at": "2009-03-20T02:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43209",
    "user": "jhpalmieri"
}
```

By the way, #5568 should be trivial to review and is somewhat related to this one.



---

archive/issue_comments_043210.json:
```json
{
    "body": "Am I right that $\\GF(2^n)$ won't work, from the patch it looks like it?",
    "created_at": "2009-03-23T10:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43210",
    "user": "malb"
}
```

Am I right that $\GF(2^n)$ won't work, from the patch it looks like it?



---

archive/issue_comments_043211.json:
```json
{
    "body": "Replying to [comment:7 malb]:\n> Am I right that `$\\GF(2^n)$` won't work, from the patch it looks like it?\n\nIf you put ``\\GF{2^n}`` in a docstring (note the curly braces, not parentheses), then this will appear as `\"GF{2^n}\"` in a docstring, and it will be typeset as `\"\\mathbf{F}_{2^n}\"` in the reference manual.  In general, given ``\\GF{blah}``, then `blah` is not modified: it appears as is in both the docstring and the LaTeX which produces reference manual. It can be a complicated LaTeX expression, for example, and it should work fine.\n\nYou can test this by applying the patch and then putting `\\GF{2<sup>{3</sup>n}}` somewhere in the tutorial, for example, and then type \"sage -docbuild tutorial html\" (or \"pdf\" instead of \"html\") to check the output, or \"sage -docbuild tutorial latex\" to check the LaTeX source code.  \n\nIs that good enough, or were you hoping for something else?",
    "created_at": "2009-03-24T05:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43211",
    "user": "jhpalmieri"
}
```

Replying to [comment:7 malb]:
> Am I right that `$\GF(2^n)$` won't work, from the patch it looks like it?

If you put ``\GF{2^n}`` in a docstring (note the curly braces, not parentheses), then this will appear as `"GF{2^n}"` in a docstring, and it will be typeset as `"\mathbf{F}_{2^n}"` in the reference manual.  In general, given ``\GF{blah}``, then `blah` is not modified: it appears as is in both the docstring and the LaTeX which produces reference manual. It can be a complicated LaTeX expression, for example, and it should work fine.

You can test this by applying the patch and then putting `\GF{2<sup>{3</sup>n}}` somewhere in the tutorial, for example, and then type "sage -docbuild tutorial html" (or "pdf" instead of "html") to check the output, or "sage -docbuild tutorial latex" to check the LaTeX source code.  

Is that good enough, or were you hoping for something else?



---

archive/issue_comments_043212.json:
```json
{
    "body": "> If you put ``\\GF{2^n}`` in a docstring \n\nOf course, you need to be careful about single vs. double backslashes.  This should probably be ``\\\\GF{2^n}`` ...",
    "created_at": "2009-03-24T05:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43212",
    "user": "jhpalmieri"
}
```

> If you put ``\GF{2^n}`` in a docstring 

Of course, you need to be careful about single vs. double backslashes.  This should probably be ``\\GF{2^n}`` ...



---

archive/issue_comments_043213.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> Is that good enough, or were you hoping for something else?\n\nAll good, sorry I didn't understand the patch properly. Thanks for explaining!",
    "created_at": "2009-03-24T10:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43213",
    "user": "malb"
}
```

Replying to [comment:8 jhpalmieri]:
> Is that good enough, or were you hoping for something else?

All good, sorry I didn't understand the patch properly. Thanks for explaining!



---

archive/issue_comments_043214.json:
```json
{
    "body": "Here's an additional patch; apply on top of the other one.  This allows use of these macros interactively; for example, in the notebook you could do\n\n```\n%latex\n$\\ZZ$\n```\n\nand it will be typeset correctly.",
    "created_at": "2009-03-24T20:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43214",
    "user": "jhpalmieri"
}
```

Here's an additional patch; apply on top of the other one.  This allows use of these macros interactively; for example, in the notebook you could do

```
%latex
$\ZZ$
```

and it will be typeset correctly.



---

archive/issue_comments_043215.json:
```json
{
    "body": "Attachment\n\n(don't use, obsolete)",
    "created_at": "2009-03-24T20:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43215",
    "user": "jhpalmieri"
}
```

Attachment

(don't use, obsolete)



---

archive/issue_comments_043216.json:
```json
{
    "body": "Attachment\n\n(don't use, obsolete)",
    "created_at": "2009-03-24T20:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43216",
    "user": "jhpalmieri"
}
```

Attachment

(don't use, obsolete)



---

archive/issue_comments_043217.json:
```json
{
    "body": "Attachment\n\n(don't use, obsolete)",
    "created_at": "2009-03-24T20:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43217",
    "user": "jhpalmieri"
}
```

Attachment

(don't use, obsolete)



---

archive/issue_comments_043218.json:
```json
{
    "body": "apply this one first",
    "created_at": "2009-03-24T20:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43218",
    "user": "jhpalmieri"
}
```

apply this one first



---

archive/issue_comments_043219.json:
```json
{
    "body": "Attachment\n\n(Is there a way to delete attachments?)",
    "created_at": "2009-03-24T20:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43219",
    "user": "jhpalmieri"
}
```

Attachment

(Is there a way to delete attachments?)



---

archive/issue_comments_043220.json:
```json
{
    "body": "Hmm, this patch was not on my radar at all. Given the patch at #5700 which patch here is the current one to apply and review?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T22:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43220",
    "user": "mabshoff"
}
```

Hmm, this patch was not on my radar at all. Given the patch at #5700 which patch here is the current one to apply and review?

Cheers,

Michael



---

archive/issue_comments_043221.json:
```json
{
    "body": "This one may have been posted during the Great Trac Email Blackout.\n\nAs I've tried to indicate at #5700, that patch is temporary.  This one is supposed to be permanent.  Applying this one will make #5700 unnecessary.  If you think this patch might get in some time soon, then maybe we should ignore #5700?",
    "created_at": "2009-04-06T22:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43221",
    "user": "jhpalmieri"
}
```

This one may have been posted during the Great Trac Email Blackout.

As I've tried to indicate at #5700, that patch is temporary.  This one is supposed to be permanent.  Applying this one will make #5700 unnecessary.  If you think this patch might get in some time soon, then maybe we should ignore #5700?



---

archive/issue_comments_043222.json:
```json
{
    "body": "Ok, looking at the patches again I think it is obvious that we need to review\n\n* new-macros-with-jsmath.patch\n* 5555-second.patch\n\nonly and can ignore the others as indicated. I am actually for merging and reviewing this one instead of merging #5700 now as a stopgap, so reassigned without any guarantee which one will go in.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T23:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43222",
    "user": "mabshoff"
}
```

Ok, looking at the patches again I think it is obvious that we need to review

* new-macros-with-jsmath.patch
* 5555-second.patch

only and can ignore the others as indicated. I am actually for merging and reviewing this one instead of merging #5700 now as a stopgap, so reassigned without any guarantee which one will go in.

Cheers,

Michael



---

archive/issue_comments_043223.json:
```json
{
    "body": "I'm looking over this, and the code seems good, but I can't find any examples of it doing anything in the html documentation. Am I missing something, or building the documentation wrong? I'm using --jsmath, which works in the notebook, but when I click the Help link at the top, it's not typesetting anything.",
    "created_at": "2009-04-10T04:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43223",
    "user": "ddrake"
}
```

I'm looking over this, and the code seems good, but I can't find any examples of it doing anything in the html documentation. Am I missing something, or building the documentation wrong? I'm using --jsmath, which works in the notebook, but when I click the Help link at the top, it's not typesetting anything.



---

archive/issue_comments_043224.json:
```json
{
    "body": "This patch doesn't actually add any examples in the documentation.  However, there are examples, recently added in Sage, which use these macros:\n\n* in sage/algebras/quatalg/quaternion_algebra.py, the functions `ideal`, `left_ideal` and `right_ideal` all use \\ZZ, \n\n* in sage/rings/polynomial/polynomial_element.pyx, `is_primitive` uses \\GF{-},\n\n* in sage/schemes/elliptic_curves/ell_rational_field.py, `modular_symbol` uses \\QQ.\n\nSo right now, those docstrings don't appear correctly in the html version of the reference manual, and they actually produce errors in the pdf version.  If you apply the patches here, those issues should be fixed.\n\nAlso as I said earlier:\n\n> You can test this by applying the patch and then putting `\"\\GF{q}\"` somewhere in the tutorial, for example, and then type  \"sage -docbuild tutorial html\" (or \"pdf\" instead of \"html\") to check the output, or \"sage -docbuild tutorial latex\" to check the LaTeX source code.\n\nDoes this answer your question?",
    "created_at": "2009-04-10T04:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43224",
    "user": "jhpalmieri"
}
```

This patch doesn't actually add any examples in the documentation.  However, there are examples, recently added in Sage, which use these macros:

* in sage/algebras/quatalg/quaternion_algebra.py, the functions `ideal`, `left_ideal` and `right_ideal` all use \ZZ, 

* in sage/rings/polynomial/polynomial_element.pyx, `is_primitive` uses \GF{-},

* in sage/schemes/elliptic_curves/ell_rational_field.py, `modular_symbol` uses \QQ.

So right now, those docstrings don't appear correctly in the html version of the reference manual, and they actually produce errors in the pdf version.  If you apply the patches here, those issues should be fixed.

Also as I said earlier:

> You can test this by applying the patch and then putting `"\GF{q}"` somewhere in the tutorial, for example, and then type  "sage -docbuild tutorial html" (or "pdf" instead of "html") to check the output, or "sage -docbuild tutorial latex" to check the LaTeX source code.

Does this answer your question?



---

archive/issue_comments_043225.json:
```json
{
    "body": "Replying to [comment:17 jhpalmieri]:\n> Does this answer your question?\n\nYes, pretty much. I think most of my problems involve my own lack of knowledge about building the documentation, and the problems we still have with building it. But I got the tutorial to correctly show the macros in html, pdf, and text form.\n\nI've reviewed the patches \"new-macros-with-jsmath.patch\" and \"5555-second.patch\" and they are very nice. Works as advertised, good code, all doctests pass: positive review.",
    "created_at": "2009-04-10T09:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43225",
    "user": "ddrake"
}
```

Replying to [comment:17 jhpalmieri]:
> Does this answer your question?

Yes, pretty much. I think most of my problems involve my own lack of knowledge about building the documentation, and the problems we still have with building it. But I got the tutorial to correctly show the macros in html, pdf, and text form.

I've reviewed the patches "new-macros-with-jsmath.patch" and "5555-second.patch" and they are very nice. Works as advertised, good code, all doctests pass: positive review.



---

archive/issue_comments_043226.json:
```json
{
    "body": "Did someone not run doctests? :)\n\n\n```\nsage -t -long \"devel/sage/sage/misc/latex.py\"               \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py\", line 371:\n    sage: _latex_file_(3, title=\"The number three\")\nExpected:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf The number three}\\\\end{center}\\n\\\\vspace{40mm}\\\\[3\\\\]\\n\\\\end{document}'\nGot:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\n\\\\newcommand{\\\\ZZ}{\\\\mathbf{Z}}\n\\n\\\\newcommand{\\\\RR}{\\\\mathbf{R}}\\n\\\\newcommand{\\\\CC}{\\\\mathbf{C}}\\n\\\\newcommand{\\\\QQ}\n{\\\\mathbf{Q}}\\n\\\\newcommand{\\\\QQbar}{\\\\overline{\\\\mathbf{Q}}}\\n\\\\newcommand{\\\\GF}\n[1]{\\\\mathbf{F}_{#1}}\\n\\\\newcommand{\\\\Zp}[1]{\\\\mathbf{Z}_{#1}}\\n\\\\newcommand{\\\\Qp}\n[1]{\\\\mathbf{Q}_{#1}}\\n\\\\newcommand{\\\\Zmod}[1]{\\\\mathbf{Z}/#1\\\\mathbf{Z}}\n\\n\\\\newcommand{\\\\CDF}{\\\\text{Complex Double Field}}\\n\\\\newcommand{\\\\CIF}{\\\\mathbf{C}}\n\\n\\\\newcommand{\\\\CLF}{\\\\mathbf{C}}\\n\\\\newcommand{\\\\RDF}{\\\\mathbf{R}}\n\\n\\\\newcommand{\\\\RIF}{\\\\I \\\\R}\\n\\\\newcommand{\\\\RLF}{\\\\mathbf{R}}\\n\\\\newcommand{\\\\RQDF}\n{\\\\mathbf{R}}\\n\\\\newcommand{\\\\CFF}{\\\\mathbf{CFF}}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf The number three}\\\\end{center}\\n\\\\vspace{40mm}\\\\[3\\\\]\\n\\\\end{document}'\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py\", line 373:\n    sage: _latex_file_([7, 8, 9], title=\"Why was six afraid of seven?\", sep='\\\\vfill\\\\hrule\\\\vfill')\nExpected:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf Why was six afraid of seven?}\\\\end{center}\\n\\\\vspace{40mm}\\\\[7\\\\]\n\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[8\\\\]\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[9\n\\\\]\\n\\\\end{document}'\nGot:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\n\\\\newcommand{\\\\ZZ}{\\\\mathbf{Z}}\n\\n\\\\newcommand{\\\\RR}{\\\\mathbf{R}}\\n\\\\newcommand{\\\\CC}{\\\\mathbf{C}}\\n\\\\newcommand{\\\\QQ}\n{\\\\mathbf{Q}}\\n\\\\newcommand{\\\\QQbar}{\\\\overline{\\\\mathbf{Q}}}\\n\\\\newcommand{\\\\GF}\n[1]{\\\\mathbf{F}_{#1}}\\n\\\\newcommand{\\\\Zp}[1]{\\\\mathbf{Z}_{#1}}\\n\\\\newcommand{\\\\Qp}\n[1]{\\\\mathbf{Q}_{#1}}\\n\\\\newcommand{\\\\Zmod}[1]{\\\\mathbf{Z}/#1\\\\mathbf{Z}}\n\\n\\\\newcommand{\\\\CDF}{\\\\text{Complex Double Field}}\\n\\\\newcommand{\\\\CIF}{\\\\mathbf{C}}\n\\n\\\\newcommand{\\\\CLF}{\\\\mathbf{C}}\\n\\\\newcommand{\\\\RDF}{\\\\mathbf{R}}\n\\n\\\\newcommand{\\\\RIF}{\\\\I \\\\R}\\n\\\\newcommand{\\\\RLF}{\\\\mathbf{R}}\\n\\\\newcommand{\\\\RQDF}\n{\\\\mathbf{R}}\\n\\\\newcommand{\\\\CFF}{\\\\mathbf{CFF}}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf Why was six afraid of seven?}\\\\end{center}\\n\\\\vspace{40mm}\\\\[7\\\\]\n\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[8\\\\]\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[9\n\\\\]\\n\\\\end{document}'\n**********************************************************************\n```\n\nOnce this obvious failure is fixed feel free to reinstate the positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T21:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43226",
    "user": "mabshoff"
}
```

Did someone not run doctests? :)


```
sage -t -long "devel/sage/sage/misc/latex.py"               
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py", line 371:
    sage: _latex_file_(3, title="The number three")
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\n\\newcommand{\\ZZ}{\\mathbf{Z}}
\n\\newcommand{\\RR}{\\mathbf{R}}\n\\newcommand{\\CC}{\\mathbf{C}}\n\\newcommand{\\QQ}
{\\mathbf{Q}}\n\\newcommand{\\QQbar}{\\overline{\\mathbf{Q}}}\n\\newcommand{\\GF}
[1]{\\mathbf{F}_{#1}}\n\\newcommand{\\Zp}[1]{\\mathbf{Z}_{#1}}\n\\newcommand{\\Qp}
[1]{\\mathbf{Q}_{#1}}\n\\newcommand{\\Zmod}[1]{\\mathbf{Z}/#1\\mathbf{Z}}
\n\\newcommand{\\CDF}{\\text{Complex Double Field}}\n\\newcommand{\\CIF}{\\mathbf{C}}
\n\\newcommand{\\CLF}{\\mathbf{C}}\n\\newcommand{\\RDF}{\\mathbf{R}}
\n\\newcommand{\\RIF}{\\I \\R}\n\\newcommand{\\RLF}{\\mathbf{R}}\n\\newcommand{\\RQDF}
{\\mathbf{R}}\n\\newcommand{\\CFF}{\\mathbf{CFF}}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]\n\\end{document}'
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py", line 373:
    sage: _latex_file_([7, 8, 9], title="Why was six afraid of seven?", sep='\\vfill\\hrule\\vfill')
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf Why was six afraid of seven?}\\end{center}\n\\vspace{40mm}\\[7\\]
\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill\n\n\\[9
\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\n\\newcommand{\\ZZ}{\\mathbf{Z}}
\n\\newcommand{\\RR}{\\mathbf{R}}\n\\newcommand{\\CC}{\\mathbf{C}}\n\\newcommand{\\QQ}
{\\mathbf{Q}}\n\\newcommand{\\QQbar}{\\overline{\\mathbf{Q}}}\n\\newcommand{\\GF}
[1]{\\mathbf{F}_{#1}}\n\\newcommand{\\Zp}[1]{\\mathbf{Z}_{#1}}\n\\newcommand{\\Qp}
[1]{\\mathbf{Q}_{#1}}\n\\newcommand{\\Zmod}[1]{\\mathbf{Z}/#1\\mathbf{Z}}
\n\\newcommand{\\CDF}{\\text{Complex Double Field}}\n\\newcommand{\\CIF}{\\mathbf{C}}
\n\\newcommand{\\CLF}{\\mathbf{C}}\n\\newcommand{\\RDF}{\\mathbf{R}}
\n\\newcommand{\\RIF}{\\I \\R}\n\\newcommand{\\RLF}{\\mathbf{R}}\n\\newcommand{\\RQDF}
{\\mathbf{R}}\n\\newcommand{\\CFF}{\\mathbf{CFF}}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf Why was six afraid of seven?}\\end{center}\n\\vspace{40mm}\\[7\\]
\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill\n\n\\[9
\\]\n\\end{document}'
**********************************************************************
```

Once this obvious failure is fixed feel free to reinstate the positive review.

Cheers,

Michael



---

archive/issue_comments_043227.json:
```json
{
    "body": "apply this one second",
    "created_at": "2009-04-10T22:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43227",
    "user": "jhpalmieri"
}
```

apply this one second



---

archive/issue_comments_043228.json:
```json
{
    "body": "Attachment\n\nOkay, here's a new patch with revised doctests.",
    "created_at": "2009-04-10T22:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43228",
    "user": "jhpalmieri"
}
```

Attachment

Okay, here's a new patch with revised doctests.



---

archive/issue_comments_043229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T00:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43229",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043230.json:
```json
{
    "body": "Merged  new-macros-with-jsmath.patch and 5555-second.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43230",
    "user": "mabshoff"
}
```

Merged  new-macros-with-jsmath.patch and 5555-second.patch in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_043231.json:
```json
{
    "body": "Replying to [comment:19 mabshoff]:\n> Did someone not run doctests? :)\n\nThat's weird...I doctested the whole tree and everything worked. I'm glad to see it was fixed and merged, though.",
    "created_at": "2009-04-11T02:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5555#issuecomment-43231",
    "user": "ddrake"
}
```

Replying to [comment:19 mabshoff]:
> Did someone not run doctests? :)

That's weird...I doctested the whole tree and everything worked. I'm glad to see it was fixed and merged, though.
