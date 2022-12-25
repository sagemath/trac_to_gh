# Issue 7406: bug in conversion powers in to LaTeX

archive/issues_007406.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: latex, power, jsmath\n\nThe LaTeX representation of (x<sup>pi)</sup>e is not valid TeX string and is not rendered by jsmath\n\n```\nsage: latex((x^pi)^e)\n{(x)}^{\\pi}^{e}\n```\n\nBurcin [suggested](http://groups.google.cz/group/sage-devel/browse_thread/thread/c49c684f1c89d0c4) how to fix this and get output like \n\n```\n{{(x)}^{\\pi}}^{e}\n```\n\n```\nThe code for printing\nsymbolic expressions is in pynac (C++). The fix can be as simple as\nprinting an extra set of braces around power objects.\n\nIf anybody wants to try fixing this, the relevant function is\npower::do_print_latex() in power.cpp. To get to the file (using the\ninstructions I wrote in another message just now), go to your SAGE_ROOT\nand do:\n\n./sage -f -s spkg/standard/pynac-0.1.9.p0.spkg\n\ncd spkg/build/pynac-0.1.9/src/ginac\n\nEdit power.cpp. To compile and make your changes effective, go to your\nSAGE_ROOT again, and do\n\n./sage -sh\ncd spkg/build/pynac-0.1.9/src\nmake install \n```\n\nHowever a better fix would be to get \n\n```\n{x}^{a}\n```\nif the base is an atom (or not power) and\n\n```\n\\left({x^a}\\right}^{b}\n```\nif the base is a power. This allows to distinguish easily between\n\n```\nx^(a^b) \n```\nand \n\n```\n(x^a)^b\n```\n\nA workaround is to remove powers of powers by simplification. For example radcan function from Maxima perfoms such simplifications\n\n```\nsage: latex(maxima((x^pi)^e).radcan().sage())\nx^{\\pi e}\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7406\n\n",
    "created_at": "2009-11-06T20:37:51Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "bug in conversion powers in to LaTeX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7406",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

Keywords: latex, power, jsmath

The LaTeX representation of (x<sup>pi)</sup>e is not valid TeX string and is not rendered by jsmath

```
sage: latex((x^pi)^e)
{(x)}^{\pi}^{e}
```

Burcin [suggested](http://groups.google.cz/group/sage-devel/browse_thread/thread/c49c684f1c89d0c4) how to fix this and get output like 

```
{{(x)}^{\pi}}^{e}
```

```
The code for printing
symbolic expressions is in pynac (C++). The fix can be as simple as
printing an extra set of braces around power objects.

If anybody wants to try fixing this, the relevant function is
power::do_print_latex() in power.cpp. To get to the file (using the
instructions I wrote in another message just now), go to your SAGE_ROOT
and do:

./sage -f -s spkg/standard/pynac-0.1.9.p0.spkg

cd spkg/build/pynac-0.1.9/src/ginac

Edit power.cpp. To compile and make your changes effective, go to your
SAGE_ROOT again, and do

./sage -sh
cd spkg/build/pynac-0.1.9/src
make install 
```

However a better fix would be to get 

```
{x}^{a}
```
if the base is an atom (or not power) and

```
\left({x^a}\right}^{b}
```
if the base is a power. This allows to distinguish easily between

```
x^(a^b) 
```
and 

```
(x^a)^b
```

A workaround is to remove powers of powers by simplification. For example radcan function from Maxima perfoms such simplifications

```
sage: latex(maxima((x^pi)^e).radcan().sage())
x^{\pi e}
```

Issue created by migration from https://trac.sagemath.org/ticket/7406





---

archive/issue_comments_062204.json:
```json
{
    "body": "Changing keywords from \"latex, power, jsmath\" to \"latex, power, jsmath, pynac\".",
    "created_at": "2009-11-21T23:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62204",
    "user": "https://github.com/robert-marik"
}
```

Changing keywords from "latex, power, jsmath" to "latex, power, jsmath, pynac".



---

archive/issue_comments_062205.json:
```json
{
    "body": "Perhaps close problem is\n\n```\nsage: latex(x*(1/(x^2)+sqrt(x^7)))\n{(\\sqrt{x^{7}} + \\frac{1}{x^{2}})} x\n```\n\nNote missing \\left and \\right at outside parentheses which makes the rendering of the expression far from perfect. Should look like\n\n```\nsage: latex(x*(1/(x^2)+sqrt(x^7)))\n{\\left(\\sqrt{x^{7}} + \\frac{1}{x^{2}}\\right)} x\n```",
    "created_at": "2009-11-21T23:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62205",
    "user": "https://github.com/robert-marik"
}
```

Perhaps close problem is

```
sage: latex(x*(1/(x^2)+sqrt(x^7)))
{(\sqrt{x^{7}} + \frac{1}{x^{2}})} x
```

Note missing \left and \right at outside parentheses which makes the rendering of the expression far from perfect. Should look like

```
sage: latex(x*(1/(x^2)+sqrt(x^7)))
{\left(\sqrt{x^{7}} + \frac{1}{x^{2}}\right)} x
```



---

archive/issue_comments_062206.json:
```json
{
    "body": "add doctests",
    "created_at": "2009-11-22T17:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62206",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_062207.json:
```json
{
    "body": "Attachment [trac_7406-power_latex.patch](tarball://root/attachments/some-uuid/ticket7406/trac_7406-power_latex.patch) by @burcin created at 2009-11-22 18:11:40\n\nThe new pynac package here\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg\n\ncontains fixes for both the problem in the description and the one in comment:3.\n\nattachment:trac_7406-power_latex.patch contains doctests for the fix.\n\nNote that the new pynac version also contains fixes for #7508 and #7264. Tests should be run with the patches from those tickets also applied in this order:\n\n* #7508\n* #7264 \n* #7406 (this ticket)\n\nThis ticket now depends on #7490, #7508 and #7264.",
    "created_at": "2009-11-22T18:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62207",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7406-power_latex.patch](tarball://root/attachments/some-uuid/ticket7406/trac_7406-power_latex.patch) by @burcin created at 2009-11-22 18:11:40

The new pynac package here

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

contains fixes for both the problem in the description and the one in comment:3.

attachment:trac_7406-power_latex.patch contains doctests for the fix.

Note that the new pynac version also contains fixes for #7508 and #7264. Tests should be run with the patches from those tickets also applied in this order:

* #7508
* #7264 
* #7406 (this ticket)

This ticket now depends on #7490, #7508 and #7264.



---

archive/issue_comments_062208.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T18:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62208",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062209.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-05T13:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62209",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062210.json:
```json
{
    "body": "Positive review - they look great in show()!  Obviously pending #7264 or a rebase.",
    "created_at": "2009-12-05T13:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62210",
    "user": "https://github.com/kcrisman"
}
```

Positive review - they look great in show()!  Obviously pending #7264 or a rebase.



---

archive/issue_comments_062211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-10T14:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7406#issuecomment-62211",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017527.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-10T14:22:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7406",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7406#event-17527"
}
```
