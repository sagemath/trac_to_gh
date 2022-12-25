# Issue 1348: Incorporate Jan Groenewald's documentation fixes

archive/issues_001348.json:
```json
{
    "body": "Assignee: tba\n\n```\nOn to the good stuff:\n\nGeneral comments and questions regarding this document should be sent by\nemail to wst...@gmail.com. If you are able to provide suggested text,\neither to replace existing incorrect or unclear material, or additional\ntext to supplement what's already available, we'd appreciate the\ncontribution.\n</snip>\n^^ Fix that notice to point to sage-support\n\nIn the tutorial, all main page titles at the top seem to\nbe lower case only. e.g.\n\n2.10.2 systems of des using laplace transforms\nShould read Systems of DEs...\n(Firefox on Feisty)\n\n2.10.2, few lines on: equatoins should read equations\n\n3.9 saving and loading complete sessions\nSome of the yellow blocks of unix shell code around section 3,\nwhich should be <pre> is displaying with italics and font errors.\nIn secion 3.9 for instance, the first yellow code block, only\n~/tmp is in verbatim font, then follows italic, larger, sagesage: ...\nWhen I view page source I get (should that not all be class=\"verbatim\"?):\n<div class=\"verbatim\"><pre>~/tmp<span class=\"math\"> sage sage: E =\nEllipticCurve('11a') sage: M = ModularSymbols(37) sage: a = 389 sage: t\n# M.T(2003).matrix(); t.charpoly().factor()  _4\n12)^2 * (x + 54)^2 </pre>...\n\n3.10 the notebook interface:\n\"displaces the SAGE notebook webpage.\"\nshould read\n\"displays the SAGE notebook webpage.\"\n\n4.2 GAP\nSAGE comes with GAP 4.4.7 for computational discrete mathematics,\nespecially group theory.\nShould read \"4.4.10\" by now.\n\n4.2 GAP (occurs elswhere too) The last line, <code><span\nclass=\"math\">SAGE_ROOT/local/lib/gap-4.4.7/pkg</code>.\nthe _R is rendered as a subscript. The text is large and italic.\nShould be verbatim.\n\n4.4 maxima\nThe yellow code blocks show \"sage.:\" as the sage prompt,\nnot \"sage:\".\n\n5.1 loading and attaching sage files\nIn particular, attach has the side effect of (auto-reload), very handy\nwhen debugging code, while load does not.\n^^ What are the parentheses for?\n\n6.1.2 how some python annoyances are resolved in sage\nInteger division: The expression 2/3 has much different behavior in\nPython than in any standard math system. In Python, if m  and n  are\nints then m/n  is also an int, namely the quotient of m  divided by n .\nTherefore 2/3=0 . This illustrates how Python is similar to C in many\nways (arrays are also indexed starting at 0). There has been talk in the\nPython community about changing Python so 2/3 returns the floating point\nnumber 0.6666..., and making 2//3 return 0 .\n^^^^^^^^^ my comment:\n\"from __future__ import\" division will import the future behaviour,\napparantly as of python3.0, which is / real division and // integer\ndivision.\n\n6.3 how do i reference sage?\nIf you write a paper using SAGE, please reference computations done with\nSAGE by including\n[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org\n^^^\nHow about a function bibtex() similar to latex() which gives a bibtex\nentry? Coudl default to bibtex(sage) but could also provide\nbibtex(pari), bibtex(gp), bibtex(Singular), etc.\n\nIf you happen to have just read straight through this tutorial, and have\nsome sense of how long it took you, please let me know (email\nwst...@gmail.com).\n^^^ Uhm, I did an hour or two yesterday and an hour or two today.\nNot sure. It's much more of a showcase() than a tutorial(). It has a\nheavy algebraic slant, and most students start learning more numerical\nwork. ODE and Statistics examples would be great (I know, I know, submit\nthem, I'm trying to learn SAGE!). We teach almost exclusively scipy\nat www.aims.ac.za now, but some lecturers still teach Maxima, Octave,\nand R, even Singular and GAP, and I would like to see them unified via SAGE,\nprobably. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1348\n\n",
    "created_at": "2007-12-01T10:08:57Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Incorporate Jan Groenewald's documentation fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tba

```
On to the good stuff:

General comments and questions regarding this document should be sent by
email to wst...@gmail.com. If you are able to provide suggested text,
either to replace existing incorrect or unclear material, or additional
text to supplement what's already available, we'd appreciate the
contribution.
</snip>
^^ Fix that notice to point to sage-support

In the tutorial, all main page titles at the top seem to
be lower case only. e.g.

2.10.2 systems of des using laplace transforms
Should read Systems of DEs...
(Firefox on Feisty)

2.10.2, few lines on: equatoins should read equations

3.9 saving and loading complete sessions
Some of the yellow blocks of unix shell code around section 3,
which should be <pre> is displaying with italics and font errors.
In secion 3.9 for instance, the first yellow code block, only
~/tmp is in verbatim font, then follows italic, larger, sagesage: ...
When I view page source I get (should that not all be class="verbatim"?):
<div class="verbatim"><pre>~/tmp<span class="math"> sage sage: E =
EllipticCurve('11a') sage: M = ModularSymbols(37) sage: a = 389 sage: t
# M.T(2003).matrix(); t.charpoly().factor()  _4
12)^2 * (x + 54)^2 </pre>...

3.10 the notebook interface:
"displaces the SAGE notebook webpage."
should read
"displays the SAGE notebook webpage."

4.2 GAP
SAGE comes with GAP 4.4.7 for computational discrete mathematics,
especially group theory.
Should read "4.4.10" by now.

4.2 GAP (occurs elswhere too) The last line, <code><span
class="math">SAGE_ROOT/local/lib/gap-4.4.7/pkg</code>.
the _R is rendered as a subscript. The text is large and italic.
Should be verbatim.

4.4 maxima
The yellow code blocks show "sage.:" as the sage prompt,
not "sage:".

5.1 loading and attaching sage files
In particular, attach has the side effect of (auto-reload), very handy
when debugging code, while load does not.
^^ What are the parentheses for?

6.1.2 how some python annoyances are resolved in sage
Integer division: The expression 2/3 has much different behavior in
Python than in any standard math system. In Python, if m  and n  are
ints then m/n  is also an int, namely the quotient of m  divided by n .
Therefore 2/3=0 . This illustrates how Python is similar to C in many
ways (arrays are also indexed starting at 0). There has been talk in the
Python community about changing Python so 2/3 returns the floating point
number 0.6666..., and making 2//3 return 0 .
^^^^^^^^^ my comment:
"from __future__ import" division will import the future behaviour,
apparantly as of python3.0, which is / real division and // integer
division.

6.3 how do i reference sage?
If you write a paper using SAGE, please reference computations done with
SAGE by including
[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org
^^^
How about a function bibtex() similar to latex() which gives a bibtex
entry? Coudl default to bibtex(sage) but could also provide
bibtex(pari), bibtex(gp), bibtex(Singular), etc.

If you happen to have just read straight through this tutorial, and have
some sense of how long it took you, please let me know (email
wst...@gmail.com).
^^^ Uhm, I did an hour or two yesterday and an hour or two today.
Not sure. It's much more of a showcase() than a tutorial(). It has a
heavy algebraic slant, and most students start learning more numerical
work. ODE and Statistics examples would be great (I know, I know, submit
them, I'm trying to learn SAGE!). We teach almost exclusively scipy
at www.aims.ac.za now, but some lecturers still teach Maxima, Octave,
and R, even Singular and GAP, and I would like to see them unified via SAGE,
probably. 
```

Issue created by migration from https://trac.sagemath.org/ticket/1348





---

archive/issue_events_003494.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T14:13:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1348#event-3494"
}
```



---

archive/issue_comments_008617.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2007-12-06T09:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8617",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_008618.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T09:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8618",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008619.json:
```json
{
    "body": "I'm going to split off the last suggestion into a separate ticket.",
    "created_at": "2007-12-07T21:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8619",
    "user": "https://github.com/mwhansen"
}
```

I'm going to split off the last suggestion into a separate ticket.



---

archive/issue_comments_008620.json:
```json
{
    "body": "Attachment [1348-doc.patch](tarball://root/attachments/some-uuid/ticket1348/1348-doc.patch) by @mwhansen created at 2007-12-07 21:50:31",
    "created_at": "2007-12-07T21:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8620",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1348-doc.patch](tarball://root/attachments/some-uuid/ticket1348/1348-doc.patch) by @mwhansen created at 2007-12-07 21:50:31



---

archive/issue_comments_008621.json:
```json
{
    "body": "Attachment [1348-sage.patch](tarball://root/attachments/some-uuid/ticket1348/1348-sage.patch) by mabshoff created at 2007-12-09 10:29:55\n\nLooks good to me.",
    "created_at": "2007-12-09T10:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [1348-sage.patch](tarball://root/attachments/some-uuid/ticket1348/1348-sage.patch) by mabshoff created at 2007-12-09 10:29:55

Looks good to me.



---

archive/issue_events_003495.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-09T10:31:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1348#event-3495"
}
```



---

archive/issue_comments_008622.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T10:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008623.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T10:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8623",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha2.



---

archive/issue_comments_008624.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> I'm going to split off the last suggestion into a separate ticket.\n\n\nSee #1422 for a ticket to implement such a BibTeX function.",
    "created_at": "2010-03-04T23:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1348#issuecomment-8624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 mhansen]:
> I'm going to split off the last suggestion into a separate ticket.


See #1422 for a ticket to implement such a BibTeX function.
