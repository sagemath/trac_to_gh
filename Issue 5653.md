# Issue 5653: [with patch, needs work] display docstrings in the notebook using html and jsMath

archive/issues_005653.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mhansen\n\nThe attached patch shouldn't affect docstrings from the command line (well, except that it should replace 'a \\times b' with 'a x b'). In the notebook, though:\n\n```\nidentity_matrix(TAB\n```\n\nshould pop open the usual docstring, but it's not in html <pre> format: see [this picture](http://sage.math.washington.edu/home/palmieri/misc/docstring.png). It's in a variable width font, with math typeset correctly -- see the $n \\times n$ in the first line of the docstring -- and with example blocks in <pre> format.\n\nThis is marked \"needs work\" for two reasons, one of which is a mystery to me:\n\n1. (the mystery) start a fresh worksheet and type\n\n```\nidentity_matrix? [SHIFT-RETURN]\n```\n\nThis will be typeset in <pre> format. Then type\n\n```\nidentity_matrix? [TAB]\n```\n\nThis is typeset nicely. I don't know what the difference is.\n\n2. Math is not handled properly.  I have a hack in place to typeset inline math (\"`... `blah` ...`\") in the docstring, but not displayed math (directive \"`.. math::`\"). This is because I'm using docutils to convert the docstring to html, and docutils doesn't know about math. I would like to use Sphinx to do the conversion (in which case more math should be handled, and there would also be some syntax highlighting), but I don't know how to use Sphinx well enough to do that.  I've posted a question to the sphinx-dev group, and if I hear anything, I'll post it here or update the ticket.\n\nPlease test out the patch, improve it, rewrite it, whatever.\n\n(By the way, Tom Boothby deserves credit for getting jsMath to process the docstring.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5653\n\n",
    "created_at": "2009-03-31T21:23:24Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs work] display docstrings in the notebook using html and jsMath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5653",
    "user": "jhpalmieri"
}
```
Assignee: boothby

CC:  mhansen

The attached patch shouldn't affect docstrings from the command line (well, except that it should replace 'a \times b' with 'a x b'). In the notebook, though:

```
identity_matrix(TAB
```

should pop open the usual docstring, but it's not in html <pre> format: see [this picture](http://sage.math.washington.edu/home/palmieri/misc/docstring.png). It's in a variable width font, with math typeset correctly -- see the $n \times n$ in the first line of the docstring -- and with example blocks in <pre> format.

This is marked "needs work" for two reasons, one of which is a mystery to me:

1. (the mystery) start a fresh worksheet and type

```
identity_matrix? [SHIFT-RETURN]
```

This will be typeset in <pre> format. Then type

```
identity_matrix? [TAB]
```

This is typeset nicely. I don't know what the difference is.

2. Math is not handled properly.  I have a hack in place to typeset inline math ("`... `blah` ...`") in the docstring, but not displayed math (directive "`.. math::`"). This is because I'm using docutils to convert the docstring to html, and docutils doesn't know about math. I would like to use Sphinx to do the conversion (in which case more math should be handled, and there would also be some syntax highlighting), but I don't know how to use Sphinx well enough to do that.  I've posted a question to the sphinx-dev group, and if I hear anything, I'll post it here or update the ticket.

Please test out the patch, improve it, rewrite it, whatever.

(By the way, Tom Boothby deserves credit for getting jsMath to process the docstring.)

Issue created by migration from https://trac.sagemath.org/ticket/5653





---

archive/issue_comments_044143.json:
```json
{
    "body": "Okay, here's a new version with [a new picture](http://sage.math.washington.edu/home/palmieri/misc/sphinx.png).  This uses Pat LeSmithe's version of set_introspect_html (see [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/dc89425699137415)), with some modifications. \n\nActually, this patch has three versions of set_introspect_html:\n* SPHINX_set_introspect_html   (modification of Pat LeSmithe's version using Sphinx)\n* PYGMENTS_set_introspect_html  (Pat LeSmithe's version using pygments -- doesn't do much for me)\n* DOCUTILS_set_introspect_html  (the version from the first patch)\nYou can edit server/notebook/cell.py, changing the line\n\n```\nset_introspect_html = SPHINX_set_introspect_html\n```\n\nto test out each one.",
    "created_at": "2009-04-01T23:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44143",
    "user": "jhpalmieri"
}
```

Okay, here's a new version with [a new picture](http://sage.math.washington.edu/home/palmieri/misc/sphinx.png).  This uses Pat LeSmithe's version of set_introspect_html (see [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/dc89425699137415)), with some modifications. 

Actually, this patch has three versions of set_introspect_html:
* SPHINX_set_introspect_html   (modification of Pat LeSmithe's version using Sphinx)
* PYGMENTS_set_introspect_html  (Pat LeSmithe's version using pygments -- doesn't do much for me)
* DOCUTILS_set_introspect_html  (the version from the first patch)
You can edit server/notebook/cell.py, changing the line

```
set_introspect_html = SPHINX_set_introspect_html
```

to test out each one.



---

archive/issue_comments_044144.json:
```json
{
    "body": "Here's a new patch incorporating Pat LeSmithe's latest ideas, plus a few new things.  This handles everything pretty well, although it might be a bit slow since Sphinx creates various files. I think it's slower than the standard docstring display in the notebook, but on the other hand, I also think it's fast enough to be usable. If we ever figure out how to run Sphinx without reading and writing files, we can do that instead.\n\nThis latest version handles math well (via Sphinx), uses pygments to do syntax highlighting (via Sphinx), handles all of `identity_matrix( TAB`, `identity_matrix? TAB`, `identity_matrix? SHIFT-RETURN`, and `identity_matrix??`.  There is now only one version of `set_introspect_html`: the Sphinx version.\n\nOne of Pat's recent posts said:\n\n```\n* If anyone's interested, here's a way to render an input cell as\nsyntax-highlighted HTML output:\n\nfrom pygments import highlight\nfrom pygments.lexers import PythonLexer\nfrom pygments.formatters import HtmlFormatter\nfrom pygments.styles import STYLE_MAP\nfrom pygments.styles import get_style_by_name\nfrom sphinx.highlighting import SphinxStyle\n\nclass colorize:\n    def __init__(self, style=SphinxStyle):\n        self.lexer = PythonLexer(encoding='chardet')\n        self.formatter = HtmlFormatter(noclasses=True, style=style)\n    def eval(self, s, globals, locals):\n        return html(highlight(s, self.lexer, self.formatter))\n\nThen put %colorize('colorful'), say, at the beginning of a cell and\nevaluate it, e.g.,\n\n%colorize('colorful')\ndef f(x):\n  return x * x\nf(3.0)\n\nSTYLE_MAP.keys() gives a list of styles.  This is adapted from\nhttp://groups.google.com/group/sage-devel/msg/e53caae140cef7df . \n```\n\nThere is already a file and a function called \"colorize\", but I added code like this, so that you can do\n\n```\n%pygments('colorful')\ndef f(x):\n  return x * x\nf(3.0)\n```\n\n(I was thinking of a name like \"html\" or \"jsmath\": pygments is what processes the rest of the cell, so that's the name of the decorator.) With the patch, this is automatically available in the notebook.\n\nI'm sure all of this could still use work, but I'll mark it as \"needs review\".",
    "created_at": "2009-04-03T22:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44144",
    "user": "jhpalmieri"
}
```

Here's a new patch incorporating Pat LeSmithe's latest ideas, plus a few new things.  This handles everything pretty well, although it might be a bit slow since Sphinx creates various files. I think it's slower than the standard docstring display in the notebook, but on the other hand, I also think it's fast enough to be usable. If we ever figure out how to run Sphinx without reading and writing files, we can do that instead.

This latest version handles math well (via Sphinx), uses pygments to do syntax highlighting (via Sphinx), handles all of `identity_matrix( TAB`, `identity_matrix? TAB`, `identity_matrix? SHIFT-RETURN`, and `identity_matrix??`.  There is now only one version of `set_introspect_html`: the Sphinx version.

One of Pat's recent posts said:

```
* If anyone's interested, here's a way to render an input cell as
syntax-highlighted HTML output:

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import STYLE_MAP
from pygments.styles import get_style_by_name
from sphinx.highlighting import SphinxStyle

class colorize:
    def __init__(self, style=SphinxStyle):
        self.lexer = PythonLexer(encoding='chardet')
        self.formatter = HtmlFormatter(noclasses=True, style=style)
    def eval(self, s, globals, locals):
        return html(highlight(s, self.lexer, self.formatter))

Then put %colorize('colorful'), say, at the beginning of a cell and
evaluate it, e.g.,

%colorize('colorful')
def f(x):
  return x * x
f(3.0)

STYLE_MAP.keys() gives a list of styles.  This is adapted from
http://groups.google.com/group/sage-devel/msg/e53caae140cef7df . 
```

There is already a file and a function called "colorize", but I added code like this, so that you can do

```
%pygments('colorful')
def f(x):
  return x * x
f(3.0)
```

(I was thinking of a name like "html" or "jsmath": pygments is what processes the rest of the cell, so that's the name of the decorator.) With the patch, this is automatically available in the notebook.

I'm sure all of this could still use work, but I'll mark it as "needs review".



---

archive/issue_comments_044145.json:
```json
{
    "body": "A new patch to go on top of docstring-new.2.patch: this incorporates a contribution from Pat LeSmithe which caches docstrings which have been processed by Sphinx and also cleans up the Sphinx processing (better conf.py and layout.html, so simpler set_instrospect_html).  I added code to process docstrings which are not in ReST format (e.g. matrix_plot or preparse): these are displayed with headers like \"File:\" in boldface, just as for other docstrings, and with the body of the docstring in a <pre> block.",
    "created_at": "2009-04-05T15:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44145",
    "user": "jhpalmieri"
}
```

A new patch to go on top of docstring-new.2.patch: this incorporates a contribution from Pat LeSmithe which caches docstrings which have been processed by Sphinx and also cleans up the Sphinx processing (better conf.py and layout.html, so simpler set_instrospect_html).  I added code to process docstrings which are not in ReST format (e.g. matrix_plot or preparse): these are displayed with headers like "File:" in boldface, just as for other docstrings, and with the body of the docstring in a <pre> block.



---

archive/issue_comments_044146.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-05T15:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44146",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044147.json:
```json
{
    "body": "Changing assignee from boothby to jhpalmieri.",
    "created_at": "2009-04-05T15:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44147",
    "user": "jhpalmieri"
}
```

Changing assignee from boothby to jhpalmieri.



---

archive/issue_comments_044148.json:
```json
{
    "body": "A new standalone patch, docstring.3.patch, tweaks the Sphinx processing code.  The code now\n\n* Sets the cache directory once per session.\n\n* Deletes doctrees and environment pickles.\n\n* Tries to avoid crossed signals from [near] simultaneous calls to Sphinx.\n\nIt'd be great to learn how this performs under heavy server loads, especially when many people access the same (or different) docstrings at once.\n\nThe new patch also removes pygmentize.py.  Eventually, it'll return in a separate ticket, along with nascent support for highlighting tracebacks and published input cells of various systems (e.g., python, latex, html, sh).",
    "created_at": "2009-04-14T07:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44148",
    "user": "mpatel"
}
```

A new standalone patch, docstring.3.patch, tweaks the Sphinx processing code.  The code now

* Sets the cache directory once per session.

* Deletes doctrees and environment pickles.

* Tries to avoid crossed signals from [near] simultaneous calls to Sphinx.

It'd be great to learn how this performs under heavy server loads, especially when many people access the same (or different) docstrings at once.

The new patch also removes pygmentize.py.  Eventually, it'll return in a separate ticket, along with nascent support for highlighting tracebacks and published input cells of various systems (e.g., python, latex, html, sh).



---

archive/issue_comments_044149.json:
```json
{
    "body": "Three comments: docstring.3.patch failed to apply cleanly against Sage 3.4.1.rc2 (someone else fixed a typo in support.py), so I've attached a rebased version.  Also, you should post Mercurial patches, not just diff files, so there is an official record of who produced the patch.\n\nThe third comment is that it looks good to me.  (I helped to write it, though, so I can't review it.)",
    "created_at": "2009-04-14T21:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44149",
    "user": "jhpalmieri"
}
```

Three comments: docstring.3.patch failed to apply cleanly against Sage 3.4.1.rc2 (someone else fixed a typo in support.py), so I've attached a rebased version.  Also, you should post Mercurial patches, not just diff files, so there is an official record of who produced the patch.

The third comment is that it looks good to me.  (I helped to write it, though, so I can't review it.)



---

archive/issue_comments_044150.json:
```json
{
    "body": "The patch's file locking algorithm is adapted from Evan Fosmark's Pythonic cross-platform file lock:\n\nhttp://www.evanfosmark.com/2009/01/cross-platform-file-locking-support-in-python/\n\nIn an email, Evan has stated that this code falls under the BSD license.  I think Evan should definitely get some credit.",
    "created_at": "2009-04-16T06:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44150",
    "user": "mpatel"
}
```

The patch's file locking algorithm is adapted from Evan Fosmark's Pythonic cross-platform file lock:

http://www.evanfosmark.com/2009/01/cross-platform-file-locking-support-in-python/

In an email, Evan has stated that this code falls under the BSD license.  I think Evan should definitely get some credit.



---

archive/issue_comments_044151.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n\n> In an email, Evan has stated that this code falls under the BSD license.  I think Evan should definitely get some credit.\n\nCould you post that email here for the record?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T06:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44151",
    "user": "mabshoff"
}
```

Replying to [comment:6 mpatel]:

> In an email, Evan has stated that this code falls under the BSD license.  I think Evan should definitely get some credit.

Could you post that email here for the record?

Cheers,

Michael



---

archive/issue_comments_044152.json:
```json
{
    "body": "By the way: I saw this in action today at UW's Sage status report and I was **really** impressed.\n\nFor credit: We have John, Mitel and Tom? \n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44152",
    "user": "mabshoff"
}
```

By the way: I saw this in action today at UW's Sage status report and I was **really** impressed.

For credit: We have John, Mitel and Tom? 

Cheers,

Michael



---

archive/issue_comments_044153.json:
```json
{
    "body": "Email exchange with Evan Fosmark",
    "created_at": "2009-04-16T07:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44153",
    "user": "mpatel"
}
```

Email exchange with Evan Fosmark



---

archive/issue_comments_044154.json:
```json
{
    "body": "Attachment [bsd.txt](tarball://root/attachments/some-uuid/ticket5653/bsd.txt) by mpatel created at 2009-04-16 07:25:05\n\nAttachment to Evan Fosmark's email.",
    "created_at": "2009-04-16T07:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44154",
    "user": "mpatel"
}
```

Attachment [bsd.txt](tarball://root/attachments/some-uuid/ticket5653/bsd.txt) by mpatel created at 2009-04-16 07:25:05

Attachment to Evan Fosmark's email.



---

archive/issue_comments_044155.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n> Could you post that email here for the record?\n\nI've also repeated the license question in a comment on Evan Fosmark's original blog entry.  I mentioned this in my email reply to Evan, so he may soon name the license explicitly on that page.",
    "created_at": "2009-04-16T07:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44155",
    "user": "mpatel"
}
```

Replying to [comment:7 mabshoff]:
> Could you post that email here for the record?

I've also repeated the license question in a comment on Evan Fosmark's original blog entry.  I mentioned this in my email reply to Evan, so he may soon name the license explicitly on that page.



---

archive/issue_comments_044156.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n \n> I've also repeated the license question in a comment on Evan Fosmark's original blog entry.  I mentioned this in my email reply to Evan, so he may soon name the license explicitly on that page.\n\nThanks. I do agree with you that Evan should be credited for his code, so we do need to add him to the list of people getting credit for this patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44156",
    "user": "mabshoff"
}
```

Replying to [comment:9 mpatel]:
 
> I've also repeated the license question in a comment on Evan Fosmark's original blog entry.  I mentioned this in my email reply to Evan, so he may soon name the license explicitly on that page.

Thanks. I do agree with you that Evan should be credited for his code, so we do need to add him to the list of people getting credit for this patch.

Cheers,

Michael



---

archive/issue_comments_044157.json:
```json
{
    "body": "So, this is a Beautiful Thing.  ;-)  Very nicely formatted docstrings *and* in some cases, formatted source code as well.  This is a great addition to the notebook for both users and developers.\n\nI'm not qualified to do a review, but here are some comments based on a bit of testing.\n\n1. `sudoku??` yields nicely formatted source code, but `matrix??` does not.  Maybe there's something about the source, not the patch?\n\n2.  I'd documented sudoku.py a week ago, which is why I was experimenting with it.\n\n(a) A URL in the references, unadorned, is a live link in the docstring view in the notebook.  Very nice.  Even nicer would be if a click on the link opened in a new tab/window.\n\n(b) An error in the docstring (still) gets reported in the console where I invoked the notebook.  So a person writing docstrings can debug this way.\n\n3.  Would it be possible to build on this code to create a command to test doscstring formatting on a single file from the sage command line?  E.g., `sage -doc misc/sagedoc.py` would build all the docstrings as HTML and view it in the developers's default web browser?\n\n4.  Against 3.4.1.rc3 I had to fix a couple of rejects from the patch by hand.\n\nGreat work - I hope this sees a proper review soon.\n\nRob",
    "created_at": "2009-04-20T04:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44157",
    "user": "rbeezer"
}
```

So, this is a Beautiful Thing.  ;-)  Very nicely formatted docstrings *and* in some cases, formatted source code as well.  This is a great addition to the notebook for both users and developers.

I'm not qualified to do a review, but here are some comments based on a bit of testing.

1. `sudoku??` yields nicely formatted source code, but `matrix??` does not.  Maybe there's something about the source, not the patch?

2.  I'd documented sudoku.py a week ago, which is why I was experimenting with it.

(a) A URL in the references, unadorned, is a live link in the docstring view in the notebook.  Very nice.  Even nicer would be if a click on the link opened in a new tab/window.

(b) An error in the docstring (still) gets reported in the console where I invoked the notebook.  So a person writing docstrings can debug this way.

3.  Would it be possible to build on this code to create a command to test doscstring formatting on a single file from the sage command line?  E.g., `sage -doc misc/sagedoc.py` would build all the docstrings as HTML and view it in the developers's default web browser?

4.  Against 3.4.1.rc3 I had to fix a couple of rejects from the patch by hand.

Great work - I hope this sees a proper review soon.

Rob



---

archive/issue_comments_044158.json:
```json
{
    "body": "I don't know why matrix?? doesn't produce nice source code. \n\nI'm attaching a rebased version of the patch, also.\n\nThe other questions are good ones, and I don't have answers for them, but I think they should be dealt with in a later ticket, once this is in.",
    "created_at": "2009-04-21T18:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44158",
    "user": "jhpalmieri"
}
```

I don't know why matrix?? doesn't produce nice source code. 

I'm attaching a rebased version of the patch, also.

The other questions are good ones, and I don't have answers for them, but I think they should be dealt with in a later ticket, once this is in.



---

archive/issue_comments_044159.json:
```json
{
    "body": "Attachment [docstring.4.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.4.patch) by jhpalmieri created at 2009-04-21 18:54:02\n\nApply only this patch, as it's cumulative. Rebased against 3.4.1.rc4",
    "created_at": "2009-04-21T18:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44159",
    "user": "jhpalmieri"
}
```

Attachment [docstring.4.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.4.patch) by jhpalmieri created at 2009-04-21 18:54:02

Apply only this patch, as it's cumulative. Rebased against 3.4.1.rc4



---

archive/issue_comments_044160.json:
```json
{
    "body": "Replying to [comment:11 rbeezer]:\n> 1. `sudoku??` yields nicely formatted source code, but `matrix??` does not.  Maybe there's something about the source, not the patch?\n\nIt seems so.  Doing a search for just a space in emacs, or turning on whitespace-mode [1], reveals several stray TABs (I think) starting around the line \n\n```\n# Ensure we have a list of lists, each inner list\n```\n\nReplacing them with spaces or running whitespace-cleanup fixes the formatting.  I apologize again for not providing a patch.\n\n[1] http://www.emacswiki.org/emacs/WhiteSpace",
    "created_at": "2009-04-21T21:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44160",
    "user": "mpatel"
}
```

Replying to [comment:11 rbeezer]:
> 1. `sudoku??` yields nicely formatted source code, but `matrix??` does not.  Maybe there's something about the source, not the patch?

It seems so.  Doing a search for just a space in emacs, or turning on whitespace-mode [1], reveals several stray TABs (I think) starting around the line 

```
# Ensure we have a list of lists, each inner list
```

Replacing them with spaces or running whitespace-cleanup fixes the formatting.  I apologize again for not providing a patch.

[1] http://www.emacswiki.org/emacs/WhiteSpace



---

archive/issue_comments_044161.json:
```json
{
    "body": "This is a little silly, but untabify.patch removes all of the TABs I could find in the code.  If it's too silly, ignore the patch; it should be independent of everything else (although according to mpatel, it should make some source code look better).",
    "created_at": "2009-04-21T22:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44161",
    "user": "jhpalmieri"
}
```

This is a little silly, but untabify.patch removes all of the TABs I could find in the code.  If it's too silly, ignore the patch; it should be independent of everything else (although according to mpatel, it should make some source code look better).



---

archive/issue_comments_044162.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> This is a little silly, but untabify.patch removes all of the TABs I could find in the code.  If it's too silly, ignore the patch; it should be independent of everything else (although according to mpatel, it should make some source code look better).\n\nYeah, we don't want any tabs in the Sage library, so I am happy to apply it. But I would suggest to move it to its own ticket since it can be reviewed independently of this patch. It might cause some merge problems with other patches, so I am not sure when the best time to apply it would be. I still have not pushed 3.4.1.final out the door and am thinking to get it in now since then 3.4.1 would not have any tabs :)\n\nAlso: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T23:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44162",
    "user": "mabshoff"
}
```

Replying to [comment:14 jhpalmieri]:
> This is a little silly, but untabify.patch removes all of the TABs I could find in the code.  If it's too silly, ignore the patch; it should be independent of everything else (although according to mpatel, it should make some source code look better).

Yeah, we don't want any tabs in the Sage library, so I am happy to apply it. But I would suggest to move it to its own ticket since it can be reviewed independently of this patch. It might cause some merge problems with other patches, so I am not sure when the best time to apply it would be. I still have not pushed 3.4.1.final out the door and am thinking to get it in now since then 3.4.1 would not have any tabs :)

Also: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.

Cheers,

Michael



---

archive/issue_comments_044163.json:
```json
{
    "body": "Replying to [comment:15 mabshoff]:\n\n> Yeah, we don't want any tabs in the Sage library, so I am happy to apply it. But I would suggest to move it to its own ticket since it can be reviewed independently of this patch. It might cause some merge problems with other patches, so I am not sure when the best time to apply it would be. I still have not pushed 3.4.1.final out the door and am thinking to get it in now since then 3.4.1 would not have any tabs :)\n\nOkay, see #5848.  I'll try to rebase it as needed...\n\n> Also: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.\n\nGreat, thanks.  Feel free to delete untabify.patch, too, since it's now in its own ticket.\n\n  John",
    "created_at": "2009-04-21T23:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44163",
    "user": "jhpalmieri"
}
```

Replying to [comment:15 mabshoff]:

> Yeah, we don't want any tabs in the Sage library, so I am happy to apply it. But I would suggest to move it to its own ticket since it can be reviewed independently of this patch. It might cause some merge problems with other patches, so I am not sure when the best time to apply it would be. I still have not pushed 3.4.1.final out the door and am thinking to get it in now since then 3.4.1 would not have any tabs :)

Okay, see #5848.  I'll try to rebase it as needed...

> Also: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.

Great, thanks.  Feel free to delete untabify.patch, too, since it's now in its own ticket.

  John



---

archive/issue_comments_044164.json:
```json
{
    "body": "Replying to [comment:16 jhpalmieri]:\n\n> Okay, see #5848.  I'll try to rebase it as needed...\n\nThanks, I am tempted to merge that ticket right now into 3.4.1.final since I see no point in delaying this :). \n \n> > Also: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.\n> \n> Great, thanks.  Feel free to delete untabify.patch, too, since it's now in its own ticket.\n\nDone.\n \n>   John\n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T23:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44164",
    "user": "mabshoff"
}
```

Replying to [comment:16 jhpalmieri]:

> Okay, see #5848.  I'll try to rebase it as needed...

Thanks, I am tempted to merge that ticket right now into 3.4.1.final since I see no point in delaying this :). 
 
> > Also: This ticket is somewhat messy due to many attachments, so I am deleting some old version of the patch that have been replaced by the unfied patch.
> 
> Great, thanks.  Feel free to delete untabify.patch, too, since it's now in its own ticket.

Done.
 
>   John

Cheers,

Michael



---

archive/issue_comments_044165.json:
```json
{
    "body": "Whoa, this is cool. I really like it!\n\nI do have a tiny suggestion: can the basic text color be changed to black? I like reading black text better than blue.\n\nOther than that, when doing `identity_matrix? TAB` and `identity_matrix? SHIFT-RETURN` both are typeset nicely, but with shift-return, I get a slightly thinner box with bigger text in the code blocks; with tab, the box is the full width of the worksheet. This is a little inconsistent, but both look very nice. (This is with the untabify patch applied.)\n\nIf I do `matrix? TAB`, it looks fine, but if I do `matrix? SHIFT-RETURN`, the box is wider, and is shifted a bit off to the right. I can read all the text, though.",
    "created_at": "2009-04-22T08:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44165",
    "user": "ddrake"
}
```

Whoa, this is cool. I really like it!

I do have a tiny suggestion: can the basic text color be changed to black? I like reading black text better than blue.

Other than that, when doing `identity_matrix? TAB` and `identity_matrix? SHIFT-RETURN` both are typeset nicely, but with shift-return, I get a slightly thinner box with bigger text in the code blocks; with tab, the box is the full width of the worksheet. This is a little inconsistent, but both look very nice. (This is with the untabify patch applied.)

If I do `matrix? TAB`, it looks fine, but if I do `matrix? SHIFT-RETURN`, the box is wider, and is shifted a bit off to the right. I can read all the text, though.



---

archive/issue_comments_044166.json:
```json
{
    "body": "Please see the comment",
    "created_at": "2009-04-22T09:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44166",
    "user": "mpatel"
}
```

Please see the comment



---

archive/issue_comments_044167.json:
```json
{
    "body": "Attachment [layout.html.pop](tarball://root/attachments/some-uuid/ticket5653/layout.html.pop) by mpatel created at 2009-04-22 09:46:26\n\nI've attached a sample `doc/introspect/templates/layout.html` with \"pop out\" and \"close\" links.  When testing it, be sure clear the doc cache, since the MD5 hash is applied only to the source.\n\nNote:  The JavaScript code may well be atrocious.",
    "created_at": "2009-04-22T09:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44167",
    "user": "mpatel"
}
```

Attachment [layout.html.pop](tarball://root/attachments/some-uuid/ticket5653/layout.html.pop) by mpatel created at 2009-04-22 09:46:26

I've attached a sample `doc/introspect/templates/layout.html` with "pop out" and "close" links.  When testing it, be sure clear the doc cache, since the MD5 hash is applied only to the source.

Note:  The JavaScript code may well be atrocious.



---

archive/issue_comments_044168.json:
```json
{
    "body": "The layout.html.pop patch by mpatel works great for me, and the \"close\" link is almost as valuable as the \"pop out\" link.  ;-)  Limited testing prompts a few minor suggestions:\n\n1.  I think of the action being described as \"tear off\" as being more suggestive than \"pop out,\" but I'm not sure there is a real convention for naming this sort of thing.\n\n2.  In Firefox I get an address bar for the new window, which points back to the whole worksheet.  Can the Javascript create the window without an address bar?\n\n3.  Would it be possible to have a link for \"move to new tab\"?  I prefer to have all my browser \"stuff\" in one window with lots of tabs, rather than a proliferation of windows.  Maybe others would feel similarly.\n\nA great addition as-is, the above are just thoughts I had upon initial use.  I also just sent a demonstration screenshot off to sage-devel.",
    "created_at": "2009-04-23T04:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44168",
    "user": "rbeezer"
}
```

The layout.html.pop patch by mpatel works great for me, and the "close" link is almost as valuable as the "pop out" link.  ;-)  Limited testing prompts a few minor suggestions:

1.  I think of the action being described as "tear off" as being more suggestive than "pop out," but I'm not sure there is a real convention for naming this sort of thing.

2.  In Firefox I get an address bar for the new window, which points back to the whole worksheet.  Can the Javascript create the window without an address bar?

3.  Would it be possible to have a link for "move to new tab"?  I prefer to have all my browser "stuff" in one window with lots of tabs, rather than a proliferation of windows.  Maybe others would feel similarly.

A great addition as-is, the above are just thoughts I had upon initial use.  I also just sent a demonstration screenshot off to sage-devel.



---

archive/issue_comments_044169.json:
```json
{
    "body": "The pop-out thing is pretty neat, but the math is garbled in the popped-out window -- this is on Mac OS X, both Safari and Firefox.  The spacing is wrong; it's as if the math takes no space, so the plain text is written on top of it.  Check out `identity_matrix?` (in-line math) or `A.iterates?` (displayed math) for A a matrix.  I can provide a screen shot if you can't reproduce it.\n\nWould it be possible to have the new window have, as a title, the name of the object for which it is the docstring or source?  That would be cool.  Failing that, I would change \"Foo!\" to something else: \"Bar!\" maybe, or perhaps \"Sage documentation\"?\n\nBy the way, Rob, I see an address bar in Firefox but not in Safari.  I don't know what implications this has, as far as being able to control it...",
    "created_at": "2009-04-23T05:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44169",
    "user": "jhpalmieri"
}
```

The pop-out thing is pretty neat, but the math is garbled in the popped-out window -- this is on Mac OS X, both Safari and Firefox.  The spacing is wrong; it's as if the math takes no space, so the plain text is written on top of it.  Check out `identity_matrix?` (in-line math) or `A.iterates?` (displayed math) for A a matrix.  I can provide a screen shot if you can't reproduce it.

Would it be possible to have the new window have, as a title, the name of the object for which it is the docstring or source?  That would be cool.  Failing that, I would change "Foo!" to something else: "Bar!" maybe, or perhaps "Sage documentation"?

By the way, Rob, I see an address bar in Firefox but not in Safari.  I don't know what implications this has, as far as being able to control it...



---

archive/issue_comments_044170.json:
```json
{
    "body": "The pop-out help is all legible for me, but now that you mention it, the math portions degrade as they move to the pop-out.  This is Firefox on Ubuntu, reasonably up-to-date.  For the displayed math in `A.iterates()` the math is no longer centered, the font is not the heavier-weight italicized font, and the superscripts are positioned correctly but are not in a smaller font.  I notice in `layout.html.pop` the inclusion of the jsmath loading (`jsmath/easy/load.js`), but perhaps there is more information that needs to be available to this window for the math to typeset properly.  Viewing the page source for the tear-off window seems to indicate the markup is coming through OK, but only `main.css` and `jsmath/easy/load.js`  seem to be present for styling the text.\n\nAfter viewing the page source for the notebook, on a hunch I tried replacing `jsmath/easy/load.js` by `/jsmath/jsMath.js` but there was no noticeable change.  So perhaps the the pop-out needs more help, and the symptoms are just more severe on Mac OS X?  Lets hope so.\n\nI vote for \"Bar!\"  ;-)  It looks like \"Sage Documentation\" at minimum is an easy fix, but having something more specific would also be really useful.",
    "created_at": "2009-04-23T05:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44170",
    "user": "rbeezer"
}
```

The pop-out help is all legible for me, but now that you mention it, the math portions degrade as they move to the pop-out.  This is Firefox on Ubuntu, reasonably up-to-date.  For the displayed math in `A.iterates()` the math is no longer centered, the font is not the heavier-weight italicized font, and the superscripts are positioned correctly but are not in a smaller font.  I notice in `layout.html.pop` the inclusion of the jsmath loading (`jsmath/easy/load.js`), but perhaps there is more information that needs to be available to this window for the math to typeset properly.  Viewing the page source for the tear-off window seems to indicate the markup is coming through OK, but only `main.css` and `jsmath/easy/load.js`  seem to be present for styling the text.

After viewing the page source for the notebook, on a hunch I tried replacing `jsmath/easy/load.js` by `/jsmath/jsMath.js` but there was no noticeable change.  So perhaps the the pop-out needs more help, and the symptoms are just more severe on Mac OS X?  Lets hope so.

I vote for "Bar!"  ;-)  It looks like "Sage Documentation" at minimum is an easy fix, but having something more specific would also be really useful.



---

archive/issue_comments_044171.json:
```json
{
    "body": "I've written a few JavaScript functions for \"tear out\" introspection, but I'm not sure where to put them.  For now, I've put them in `javascript_local/introspect.js` and added \n\n```\nhead += '<script type=\"text/javascript\" src=\"/javascript_local/introspect.js\"></script>\\n'\n```\n\nto `notebook.py`, but the \"local\" repository seems to be gone.  Alternatively, I can put them in `javascript/introspect.js` and use the \"extcode\" repository, but I think the latter will soon change significantly (see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a08b413375558b46/d643be6b6bd04968#d643be6b6bd04968)).\n\n`js.py` is another possibility, but I'd rather not put them there, since it might be useful to load `introspect.js` into a \"torn out\" window.\n\nA related issue:  It would be nice to have just one `<script>` element load jsMath with all of Sage's customizations (extensions, plug-ins, macros, etc.) into regular, published, printed, and docbrowser worksheets, as well as \"torn out\" introspection windows and offline documentation.  Maybe `easy/load.js` is the right place (see #4714),\nbut I think notebook.py generates the macro list on-the-fly.",
    "created_at": "2009-05-03T09:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44171",
    "user": "mpatel"
}
```

I've written a few JavaScript functions for "tear out" introspection, but I'm not sure where to put them.  For now, I've put them in `javascript_local/introspect.js` and added 

```
head += '<script type="text/javascript" src="/javascript_local/introspect.js"></script>\n'
```

to `notebook.py`, but the "local" repository seems to be gone.  Alternatively, I can put them in `javascript/introspect.js` and use the "extcode" repository, but I think the latter will soon change significantly (see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a08b413375558b46/d643be6b6bd04968#d643be6b6bd04968)).

`js.py` is another possibility, but I'd rather not put them there, since it might be useful to load `introspect.js` into a "torn out" window.

A related issue:  It would be nice to have just one `<script>` element load jsMath with all of Sage's customizations (extensions, plug-ins, macros, etc.) into regular, published, printed, and docbrowser worksheets, as well as "torn out" introspection windows and offline documentation.  Maybe `easy/load.js` is the right place (see #4714),
but I think notebook.py generates the macro list on-the-fly.



---

archive/issue_comments_044172.json:
```json
{
    "body": "I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.",
    "created_at": "2009-05-03T16:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44172",
    "user": "jhpalmieri"
}
```

I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.



---

archive/issue_comments_044173.json:
```json
{
    "body": "Replying to [comment:25 jhpalmieri]:\n> I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.\n\n(Also, its presence here might slow down the refereeing process -- I think docstring.4.patch is ready to go and should get into Sage soon, while the tear-out stuff isn't there yet.)",
    "created_at": "2009-05-03T16:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44173",
    "user": "jhpalmieri"
}
```

Replying to [comment:25 jhpalmieri]:
> I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.

(Also, its presence here might slow down the refereeing process -- I think docstring.4.patch is ready to go and should get into Sage soon, while the tear-out stuff isn't there yet.)



---

archive/issue_comments_044174.json:
```json
{
    "body": "Replying to [comment:24 mpatel]:\n\n> A related issue:  It would be nice to have just one `<script>` element load jsMath with all of Sage's customizations (extensions, plug-ins, macros, etc.) into regular, published, printed, and docbrowser worksheets, as well as \"torn out\" introspection windows and offline documentation.  Maybe `easy/load.js` is the right place (see #4714),\n> but I think notebook.py generates the macro list on-the-fly.\n\nDavide (author of jsmath) sent these comments about the above paragraph:\n\nMpatel is right that jsMath/easy/load.js could be used for this.  Rather than putting calls to jsMath.Setup.Script() or jsMath.Extention.Require() in-line in the document itself, these can be be put in the loadFiles array in easy/load.js.  It is also possible to put the jsMath.Macro() calls into a file (say jsMath/local/sage.js), and add that file to the loadFiles array as well rather than put them in-line.  Any sage-specific customization could go in local/sage.js as well.  In the latest version of jsMath, there is even a macros array in easy/load.js for custom macros, so you would not even need an extra file for that.  These features are, in fact, one of the important reasons for easy/load.js, so I hope you are able to take advantage of them.",
    "created_at": "2009-05-04T14:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44174",
    "user": "jason"
}
```

Replying to [comment:24 mpatel]:

> A related issue:  It would be nice to have just one `<script>` element load jsMath with all of Sage's customizations (extensions, plug-ins, macros, etc.) into regular, published, printed, and docbrowser worksheets, as well as "torn out" introspection windows and offline documentation.  Maybe `easy/load.js` is the right place (see #4714),
> but I think notebook.py generates the macro list on-the-fly.

Davide (author of jsmath) sent these comments about the above paragraph:

Mpatel is right that jsMath/easy/load.js could be used for this.  Rather than putting calls to jsMath.Setup.Script() or jsMath.Extention.Require() in-line in the document itself, these can be be put in the loadFiles array in easy/load.js.  It is also possible to put the jsMath.Macro() calls into a file (say jsMath/local/sage.js), and add that file to the loadFiles array as well rather than put them in-line.  Any sage-specific customization could go in local/sage.js as well.  In the latest version of jsMath, there is even a macros array in easy/load.js for custom macros, so you would not even need an extra file for that.  These features are, in fact, one of the important reasons for easy/load.js, so I hope you are able to take advantage of them.



---

archive/issue_comments_044175.json:
```json
{
    "body": "Replying to [comment:26 jhpalmieri]:\n> Replying to [comment:25 jhpalmieri]:\n> > I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.\n> (Also, its presence here might slow down the refereeing process -- I think docstring.4.patch is ready to go and should get into Sage soon, while the tear-out stuff isn't there yet.)\n\nAgreed.  Please see #6001 for progress on the tear-out stuff.",
    "created_at": "2009-05-08T08:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44175",
    "user": "mpatel"
}
```

Replying to [comment:26 jhpalmieri]:
> Replying to [comment:25 jhpalmieri]:
> > I think the tear-out stuff should be part of a different ticket -- it enhances the other things here, but is a separate issue.
> (Also, its presence here might slow down the refereeing process -- I think docstring.4.patch is ready to go and should get into Sage soon, while the tear-out stuff isn't there yet.)

Agreed.  Please see #6001 for progress on the tear-out stuff.



---

archive/issue_comments_044176.json:
```json
{
    "body": "A comment from mhansen: we shouldn't reproduce the files builder.py and conf.py.  Instead, we should use the existing builder.py (in doc/common), and we should use doc/common/conf.py, putting modifications in introspect/conf.py (as with tutorial/conf.py, etc.).  I couldn't figure out how to run Sphinx and tell it to do all of this, so mpatel, can you fix it?",
    "created_at": "2009-05-18T22:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44176",
    "user": "jhpalmieri"
}
```

A comment from mhansen: we shouldn't reproduce the files builder.py and conf.py.  Instead, we should use the existing builder.py (in doc/common), and we should use doc/common/conf.py, putting modifications in introspect/conf.py (as with tutorial/conf.py, etc.).  I couldn't figure out how to run Sphinx and tell it to do all of this, so mpatel, can you fix it?



---

archive/issue_comments_044177.json:
```json
{
    "body": "Attachment [5653-cleanup.patch](tarball://root/attachments/some-uuid/ticket5653/5653-cleanup.patch) by mpatel created at 2009-05-19 10:05:47\n\nConform to docbuild setup.  This patch should be cumulative, against 3.4.2.",
    "created_at": "2009-05-19T10:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44177",
    "user": "mpatel"
}
```

Attachment [5653-cleanup.patch](tarball://root/attachments/some-uuid/ticket5653/5653-cleanup.patch) by mpatel created at 2009-05-19 10:05:47

Conform to docbuild setup.  This patch should be cumulative, against 3.4.2.



---

archive/issue_comments_044178.json:
```json
{
    "body": "Attachment [trac_5653_pretty_docstrings.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653_pretty_docstrings.patch) by mpatel created at 2009-05-19 10:22:08\n\nReplying to [comment:29 jhpalmieri]:\n> A comment from mhansen: we shouldn't reproduce the files builder.py and conf.py.  Instead, we should use the existing builder.py (in doc/common), and we should use doc/common/conf.py, putting modifications in introspect/conf.py (as with tutorial/conf.py, etc.).  I couldn't figure out how to run Sphinx and tell it to do all of this, so mpatel, can you fix it?\n\nI think so.  Please see [attachment:trac_5653_pretty_docstrings.patch this patch], which should be inclusive.  (I just exported changesets 12155-7 to the same file, in succession.  Let me know if this is wrong.)",
    "created_at": "2009-05-19T10:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44178",
    "user": "mpatel"
}
```

Attachment [trac_5653_pretty_docstrings.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653_pretty_docstrings.patch) by mpatel created at 2009-05-19 10:22:08

Replying to [comment:29 jhpalmieri]:
> A comment from mhansen: we shouldn't reproduce the files builder.py and conf.py.  Instead, we should use the existing builder.py (in doc/common), and we should use doc/common/conf.py, putting modifications in introspect/conf.py (as with tutorial/conf.py, etc.).  I couldn't figure out how to run Sphinx and tell it to do all of this, so mpatel, can you fix it?

I think so.  Please see [attachment:trac_5653_pretty_docstrings.patch this patch], which should be inclusive.  (I just exported changesets 12155-7 to the same file, in succession.  Let me know if this is wrong.)



---

archive/issue_comments_044179.json:
```json
{
    "body": "> (I just exported changesets 12155-7 to the same file, in succession. Let me know if this is wrong.)\n\nIt didn't work for me, but I prepared a new patch.  This incorporates all of the earlier changes, plus just a little more: boothby's patch turned off the sphinx messages, and mine turns off all of the other messages (about the location of the introspection cache, for example).  It provides a bad way to turn those messages back on, because I couldn't figure out a better way, despite trying for quite a while -- see the docstring for `set_instrospect_html`.\n\nTo produce the patch, here's what I did: \n\n1. imported the old patch \"docstring.4.patch\".  \n\n2. used \"hg rollback\" to uncommit the changes\n\n3. performed the changes in your patch file (by hand, basically)\n\n4. \"hg commit\"\n\nThis produced an all-in-one patch.",
    "created_at": "2009-05-19T21:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44179",
    "user": "jhpalmieri"
}
```

> (I just exported changesets 12155-7 to the same file, in succession. Let me know if this is wrong.)

It didn't work for me, but I prepared a new patch.  This incorporates all of the earlier changes, plus just a little more: boothby's patch turned off the sphinx messages, and mine turns off all of the other messages (about the location of the introspection cache, for example).  It provides a bad way to turn those messages back on, because I couldn't figure out a better way, despite trying for quite a while -- see the docstring for `set_instrospect_html`.

To produce the patch, here's what I did: 

1. imported the old patch "docstring.4.patch".  

2. used "hg rollback" to uncommit the changes

3. performed the changes in your patch file (by hand, basically)

4. "hg commit"

This produced an all-in-one patch.



---

archive/issue_comments_044180.json:
```json
{
    "body": "Attachment [docstring.5.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.5.patch) by jhpalmieri created at 2009-05-19 21:31:26\n\ncumulative against 4.0.alpha0.  Apply only this patch.",
    "created_at": "2009-05-19T21:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44180",
    "user": "jhpalmieri"
}
```

Attachment [docstring.5.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.5.patch) by jhpalmieri created at 2009-05-19 21:31:26

cumulative against 4.0.alpha0.  Apply only this patch.



---

archive/issue_comments_044181.json:
```json
{
    "body": "Thanks very much for making a proper all-in-one patch, though I can't test it just now, for lack of time.  How did tboothby combine two HG changesets into a single patch?\n\nPerhaps we can use Python's [logging](http://docs.python.org/library/logging.html) module.  I don't know how it affects performance, but with the right granularity and help from library authors, we may be able to provide \"histories\" for Sage computations, too.\n\nI also found [FirePython / FireLogger](http://firepython.binaryage.com/).  Apparently, it can work with the logging module to send live messages to a panel in Firefox's [Firebug extension](http://getfirebug.com/).  I don't know if the development version works with Firebug 1.4.  I'll try to take a closer look soon.  It might be useful to get feedback in the browser on \"What is my Sage process doing now?\"",
    "created_at": "2009-05-20T18:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44181",
    "user": "mpatel"
}
```

Thanks very much for making a proper all-in-one patch, though I can't test it just now, for lack of time.  How did tboothby combine two HG changesets into a single patch?

Perhaps we can use Python's [logging](http://docs.python.org/library/logging.html) module.  I don't know how it affects performance, but with the right granularity and help from library authors, we may be able to provide "histories" for Sage computations, too.

I also found [FirePython / FireLogger](http://firepython.binaryage.com/).  Apparently, it can work with the logging module to send live messages to a panel in Firefox's [Firebug extension](http://getfirebug.com/).  I don't know if the development version works with Firebug 1.4.  I'll try to take a closer look soon.  It might be useful to get feedback in the browser on "What is my Sage process doing now?"



---

archive/issue_comments_044182.json:
```json
{
    "body": "As far as the verbosity issue, I don't think it can be fixed cleanly now, so I propose that we leave it as is.  My understanding is that when you run a worksheet, there are two Sage processes going on -- one for the worksheet itself, and one associated to the notebook server.  The introspection stuff is handled by the notebook server, while any variables we might want to set are in the worksheet process; therefore we can't toggle verbosity from within a worksheet.",
    "created_at": "2009-05-21T03:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44182",
    "user": "jhpalmieri"
}
```

As far as the verbosity issue, I don't think it can be fixed cleanly now, so I propose that we leave it as is.  My understanding is that when you run a worksheet, there are two Sage processes going on -- one for the worksheet itself, and one associated to the notebook server.  The introspection stuff is handled by the notebook server, while any variables we might want to set are in the worksheet process; therefore we can't toggle verbosity from within a worksheet.



---

archive/issue_comments_044183.json:
```json
{
    "body": "Attachment [css.patch](tarball://root/attachments/some-uuid/ticket5653/css.patch) by whuss created at 2009-05-28 08:02:15\n\napply ontop of docstring.5.patch",
    "created_at": "2009-05-28T08:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44183",
    "user": "whuss"
}
```

Attachment [css.patch](tarball://root/attachments/some-uuid/ticket5653/css.patch) by whuss created at 2009-05-28 08:02:15

apply ontop of docstring.5.patch



---

archive/issue_comments_044184.json:
```json
{
    "body": "I think the documentation is currently much too colorful and therefore hard to read.\nI've attached a few tweaks to the css, which make the background lighter, change the\ntext color to black, and also tone down the colors of the examples.",
    "created_at": "2009-05-28T08:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44184",
    "user": "whuss"
}
```

I think the documentation is currently much too colorful and therefore hard to read.
I've attached a few tweaks to the css, which make the background lighter, change the
text color to black, and also tone down the colors of the examples.



---

archive/issue_comments_044185.json:
```json
{
    "body": "> I think the documentation is currently much too colorful and therefore hard to read. I've attached a few tweaks to the css, which make the background lighter, change the text color to black, and also tone down the colors of the examples. \n\nI don't have strong color preferences, so I'm mostly okay with this, but I like having the EXAMPLES blocks set off with a different background color.  So here's a slight variant on your css.patch; the only difference is that, while I'm keeping your light gray as the general background, the background for the examples is white.",
    "created_at": "2009-05-29T19:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44185",
    "user": "jhpalmieri"
}
```

> I think the documentation is currently much too colorful and therefore hard to read. I've attached a few tweaks to the css, which make the background lighter, change the text color to black, and also tone down the colors of the examples. 

I don't have strong color preferences, so I'm mostly okay with this, but I like having the EXAMPLES blocks set off with a different background color.  So here's a slight variant on your css.patch; the only difference is that, while I'm keeping your light gray as the general background, the background for the examples is white.



---

archive/issue_comments_044186.json:
```json
{
    "body": "apply on top of docstring.5.patch -- this replaces css.patch",
    "created_at": "2009-05-29T19:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44186",
    "user": "jhpalmieri"
}
```

apply on top of docstring.5.patch -- this replaces css.patch



---

archive/issue_comments_044187.json:
```json
{
    "body": "Attachment [css-new.patch](tarball://root/attachments/some-uuid/ticket5653/css-new.patch) by mpatel created at 2009-05-30 00:46:23\n\nThe [CSS overflow property](http://www.w3schools.com/Css/pr_pos_overflow.asp) can activate \"inline\" scrollbars:\n\n```\ndiv.docstring {\n  overflow: auto;\n}\n```\n",
    "created_at": "2009-05-30T00:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44187",
    "user": "mpatel"
}
```

Attachment [css-new.patch](tarball://root/attachments/some-uuid/ticket5653/css-new.patch) by mpatel created at 2009-05-30 00:46:23

The [CSS overflow property](http://www.w3schools.com/Css/pr_pos_overflow.asp) can activate "inline" scrollbars:

```
div.docstring {
  overflow: auto;
}
```




---

archive/issue_comments_044188.json:
```json
{
    "body": "This is awesome!\n\nWhen doing a double-question mark in Sage 4.0, I get:\n\n\n```\nTraceback (most recent call last):\n  File \"\", line 1, in \n  File \"/home/jason/.sage/sage_notebook/worksheets/admin/7/code/10.py\", line 6, in \n    print _support_.source_code(\"sudoku\", globals(), system=\"sage\")\n  File \"/home/jason/sage/local/lib/python2.5/site-packages/sage/server/support.py\", line 240, in source_code\n    lines, lineno = sageinspect.sage_getsourcelines(obj, is_binary=False)\n  File \"/home/jason/sage/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 568, in sage_getsourcelines\n    return inspect.getsourcelines(obj)\n  File \"/home/jason/sage/local/lib/python/inspect.py\", line 618, in getsourcelines\n    lines, lnum = findsource(object)\n  File \"/home/jason/download/sage-4.0.rc2/local/lib/python2.5/site-packages/IPython/ultraTB.py\", line 151, in findsource\nIOError: could not get source code\n```\n\n\nHowever, this may not be an issue with this patch. The directories above are the directories in which I built sage.  However, I moved Sage since then, so the directories above no longer exist.  Why are the directory paths not updated when I move the Sage directory (and start up Sage)?",
    "created_at": "2009-05-30T07:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44188",
    "user": "jason"
}
```

This is awesome!

When doing a double-question mark in Sage 4.0, I get:


```
Traceback (most recent call last):
  File "", line 1, in 
  File "/home/jason/.sage/sage_notebook/worksheets/admin/7/code/10.py", line 6, in 
    print _support_.source_code("sudoku", globals(), system="sage")
  File "/home/jason/sage/local/lib/python2.5/site-packages/sage/server/support.py", line 240, in source_code
    lines, lineno = sageinspect.sage_getsourcelines(obj, is_binary=False)
  File "/home/jason/sage/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 568, in sage_getsourcelines
    return inspect.getsourcelines(obj)
  File "/home/jason/sage/local/lib/python/inspect.py", line 618, in getsourcelines
    lines, lnum = findsource(object)
  File "/home/jason/download/sage-4.0.rc2/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 151, in findsource
IOError: could not get source code
```


However, this may not be an issue with this patch. The directories above are the directories in which I built sage.  However, I moved Sage since then, so the directories above no longer exist.  Why are the directory paths not updated when I move the Sage directory (and start up Sage)?



---

archive/issue_comments_044189.json:
```json
{
    "body": "Rebase of docstring.5.patch + css-new.patch against v4.0.2 + #6307's 6307bis.patch.  Apply only this patch.",
    "created_at": "2009-06-20T16:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44189",
    "user": "mpatel"
}
```

Rebase of docstring.5.patch + css-new.patch against v4.0.2 + #6307's 6307bis.patch.  Apply only this patch.



---

archive/issue_comments_044190.json:
```json
{
    "body": "Attachment [docstring.6.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.6.patch) by mpatel created at 2009-06-20 16:21:11\n\nReplying to [comment:38 jason]:\n> However, this may not be an issue with this patch. The directories above are the directories in which I built sage.  However, I moved Sage since then, so the directories above no longer exist.  Why are the directory paths not updated when I move the Sage directory (and start up Sage)?\n\nI've experienced something similar after upgrading and moving the installation to a new home.  I think this directory path issue is important but orthogonal to this ticket.",
    "created_at": "2009-06-20T16:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44190",
    "user": "mpatel"
}
```

Attachment [docstring.6.patch](tarball://root/attachments/some-uuid/ticket5653/docstring.6.patch) by mpatel created at 2009-06-20 16:21:11

Replying to [comment:38 jason]:
> However, this may not be an issue with this patch. The directories above are the directories in which I built sage.  However, I moved Sage since then, so the directories above no longer exist.  Why are the directory paths not updated when I move the Sage directory (and start up Sage)?

I've experienced something similar after upgrading and moving the installation to a new home.  I think this directory path issue is important but orthogonal to this ticket.



---

archive/issue_comments_044191.json:
```json
{
    "body": "I hate to say this, but I get conflicts on my 4.1 tree.  I applied the patches at #6307, then the patch here.  \nCan you rebase this?\n\n\n```\napplying docstring.6.patch\npatching file sage/misc/sagedoc.py\nHunk #1 FAILED at 19\nHunk #2 FAILED at 111\nHunk #4 FAILED at 143\n3 out of 6 hunks FAILED -- saving rejects to file sage/misc/sagedoc.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh docstring.6.patch\n```\n\n\nIt looks like this file was touched a lot in the last few weeks:\n\n\n```\ngrout@tiny:~/sage/devel/sage/sage/misc$ hg log -d -30 sagedoc.py\nchangeset:   12667:e40ab81e2c6d\ntag:         qtip\ntag:         docstring.6.patch\ntag:         tip\nuser:        Mitesh Patel <qed777@gmail.com>\ndate:        Sat Jun 20 09:07:16 2009 -0700\nsummary:     #5653, pretty docstrings\n\nchangeset:   12653:3534c8c4de50\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Tue Jul 07 07:52:02 2009 -0700\nsummary:     fix for ref manual\n\nchangeset:   12616:0df4e2e58e79\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Mon Jun 29 17:14:16 2009 -0700\nsummary:     add 1 to line numbers\n\nchangeset:   12615:50be675c81f1\nuser:        Dan Drake <drake@kaist.edu>\ndate:        Sun Jun 28 22:17:17 2009 -0700\nsummary:     [mq]: trac_6429_line_numbers.patch\n\nchangeset:   12614:6d776eac44c9\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Sun Jun 28 21:29:54 2009 -0700\nsummary:     try to make search_src etc. less OS dependent\n\nchangeset:   12603:96d0f059d528\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Thu Jun 25 17:13:23 2009 -0700\nsummary:     ref manual fixes\n```\n",
    "created_at": "2009-07-18T23:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44191",
    "user": "jason"
}
```

I hate to say this, but I get conflicts on my 4.1 tree.  I applied the patches at #6307, then the patch here.  
Can you rebase this?


```
applying docstring.6.patch
patching file sage/misc/sagedoc.py
Hunk #1 FAILED at 19
Hunk #2 FAILED at 111
Hunk #4 FAILED at 143
3 out of 6 hunks FAILED -- saving rejects to file sage/misc/sagedoc.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh docstring.6.patch
```


It looks like this file was touched a lot in the last few weeks:


```
grout@tiny:~/sage/devel/sage/sage/misc$ hg log -d -30 sagedoc.py
changeset:   12667:e40ab81e2c6d
tag:         qtip
tag:         docstring.6.patch
tag:         tip
user:        Mitesh Patel <qed777@gmail.com>
date:        Sat Jun 20 09:07:16 2009 -0700
summary:     #5653, pretty docstrings

changeset:   12653:3534c8c4de50
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Tue Jul 07 07:52:02 2009 -0700
summary:     fix for ref manual

changeset:   12616:0df4e2e58e79
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Mon Jun 29 17:14:16 2009 -0700
summary:     add 1 to line numbers

changeset:   12615:50be675c81f1
user:        Dan Drake <drake@kaist.edu>
date:        Sun Jun 28 22:17:17 2009 -0700
summary:     [mq]: trac_6429_line_numbers.patch

changeset:   12614:6d776eac44c9
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Sun Jun 28 21:29:54 2009 -0700
summary:     try to make search_src etc. less OS dependent

changeset:   12603:96d0f059d528
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Thu Jun 25 17:13:23 2009 -0700
summary:     ref manual fixes
```




---

archive/issue_comments_044192.json:
```json
{
    "body": "Attachment [trac_5653_pretty_docstrings_v7.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653_pretty_docstrings_v7.patch) by mpatel created at 2009-07-19 05:44:50\n\nRe-base against v4.1 + #6307's \"bis\" and \"reviewer\" patches. Apply only this patch.",
    "created_at": "2009-07-19T05:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44192",
    "user": "mpatel"
}
```

Attachment [trac_5653_pretty_docstrings_v7.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653_pretty_docstrings_v7.patch) by mpatel created at 2009-07-19 05:44:50

Re-base against v4.1 + #6307's "bis" and "reviewer" patches. Apply only this patch.



---

archive/issue_comments_044193.json:
```json
{
    "body": "I applied the rejected pieces by hand and exported anew.  See [attachment:trac_5653_pretty_docstrings_v7.patch].  A diff of the diffs does not reveal any surprises, but let me know...",
    "created_at": "2009-07-19T05:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44193",
    "user": "mpatel"
}
```

I applied the rejected pieces by hand and exported anew.  See [attachment:trac_5653_pretty_docstrings_v7.patch].  A diff of the diffs does not reveal any surprises, but let me know...



---

archive/issue_comments_044194.json:
```json
{
    "body": "Out of curiosity: Have any new TABs appeared in library .py and .pyx files?",
    "created_at": "2009-07-19T06:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44194",
    "user": "mpatel"
}
```

Out of curiosity: Have any new TABs appeared in library .py and .pyx files?



---

archive/issue_comments_044195.json:
```json
{
    "body": "Replying to [comment:42 mpatel]:\n> Out of curiosity: Have any new TABs appeared in library .py and .pyx files?\n\nQuite a few, according to \n\n```\ngrep \"`echo '\\t'`\" `find -name \\*.pyx -o -name \\*.py`\n```\n\n(from tcsh, on Linux).  Or am I mistaken?  If not, what is an efficient way to generate a patch like that at #5848?\n\nI suppose we should make a [firm] request on `sage-devel`, too.  Perhaps we can set up [Mercurial](http://hgbook.red-bean.com/read/handling-repository-events-with-hooks.html) to untabify or complain during commit or export events?",
    "created_at": "2009-07-19T06:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44195",
    "user": "mpatel"
}
```

Replying to [comment:42 mpatel]:
> Out of curiosity: Have any new TABs appeared in library .py and .pyx files?

Quite a few, according to 

```
grep "`echo '\t'`" `find -name \*.pyx -o -name \*.py`
```

(from tcsh, on Linux).  Or am I mistaken?  If not, what is an efficient way to generate a patch like that at #5848?

I suppose we should make a [firm] request on `sage-devel`, too.  Perhaps we can set up [Mercurial](http://hgbook.red-bean.com/read/handling-repository-events-with-hooks.html) to untabify or complain during commit or export events?



---

archive/issue_comments_044196.json:
```json
{
    "body": "I definitely think you should bring this up on sage-devel.",
    "created_at": "2009-07-19T07:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44196",
    "user": "jason"
}
```

I definitely think you should bring this up on sage-devel.



---

archive/issue_comments_044197.json:
```json
{
    "body": "This looks fantastic.\n\nThis sometimes messes up docstrings that are not yet in rest.  However, this also might spur action in getting the rest of the docs into rest format.\n\nI'll try to look through this next week.  I've also applied it to my tree so that I can test it normal usage.",
    "created_at": "2009-07-19T07:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44197",
    "user": "jason"
}
```

This looks fantastic.

This sometimes messes up docstrings that are not yet in rest.  However, this also might spur action in getting the rest of the docs into rest format.

I'll try to look through this next week.  I've also applied it to my tree so that I can test it normal usage.



---

archive/issue_comments_044198.json:
```json
{
    "body": "Replying to [comment:46 jason]:\n> This sometimes messes up docstrings that are not yet in rest.  However, this also might spur action in getting the rest of the docs into rest format.\n\n[Thanks!]  Please let us know about outliers.",
    "created_at": "2009-07-19T08:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44198",
    "user": "mpatel"
}
```

Replying to [comment:46 jason]:
> This sometimes messes up docstrings that are not yet in rest.  However, this also might spur action in getting the rest of the docs into rest format.

[Thanks!]  Please let us know about outliers.



---

archive/issue_comments_044199.json:
```json
{
    "body": "Ideas for possible future improvements:\n\n* Cross-references.  One approach: Post-process Sphinx's output in `cell.py`'s `set_introspect_html()`.  It may help to pass the module name as an argument.\n* Browse to the previous / next definition in the current module.\n* Live cells.\n* Tear-outs (cf. #6001).\n\nWhy don't we have figures in the reference manual?",
    "created_at": "2009-07-19T08:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44199",
    "user": "mpatel"
}
```

Ideas for possible future improvements:

* Cross-references.  One approach: Post-process Sphinx's output in `cell.py`'s `set_introspect_html()`.  It may help to pass the module name as an argument.
* Browse to the previous / next definition in the current module.
* Live cells.
* Tear-outs (cf. #6001).

Why don't we have figures in the reference manual?



---

archive/issue_comments_044200.json:
```json
{
    "body": "REFEREE REPORT:\n\nOh my god, this so totally rocks!!!\n\n\nRegarding the actual code:\n\n* It's pretty robust.  This is huge and worked no problem:\n\n```\nsage.combinat.sloane_functions??\n```\n\n\n\nThis just rocks.",
    "created_at": "2009-07-21T05:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44200",
    "user": "was"
}
```

REFEREE REPORT:

Oh my god, this so totally rocks!!!


Regarding the actual code:

* It's pretty robust.  This is huge and worked no problem:

```
sage.combinat.sloane_functions??
```



This just rocks.



---

archive/issue_comments_044201.json:
```json
{
    "body": "Fantastic!  I'm excited to see this in Sage!",
    "created_at": "2009-07-21T07:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44201",
    "user": "jason"
}
```

Fantastic!  I'm excited to see this in Sage!



---

archive/issue_comments_044202.json:
```json
{
    "body": "Replying to [comment:48 mpatel]:\n> Ideas for possible future improvements:\n* Cross-references.  One approach: Post-process Sphinx's output in `cell.py`'s `set_introspect_html()`.  It may help to pass the module name as an argument.\n* Browse to the previous / next definition in the current module.\n* Live cells.\n* Tear-outs (cf. #6001).\n* Faster hashing of long docstrings.  Perhaps we can first check the parent module's `mtime`, then hash if this test is inconclusive.  Or use `hg diff`.\n* A [tree-like](http://www.jstree.com/) browser.",
    "created_at": "2009-07-21T11:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44202",
    "user": "mpatel"
}
```

Replying to [comment:48 mpatel]:
> Ideas for possible future improvements:
* Cross-references.  One approach: Post-process Sphinx's output in `cell.py`'s `set_introspect_html()`.  It may help to pass the module name as an argument.
* Browse to the previous / next definition in the current module.
* Live cells.
* Tear-outs (cf. #6001).
* Faster hashing of long docstrings.  Perhaps we can first check the parent module's `mtime`, then hash if this test is inconclusive.  Or use `hg diff`.
* A [tree-like](http://www.jstree.com/) browser.



---

archive/issue_comments_044203.json:
```json
{
    "body": "With the patches at #6307, `trac_5653_pretty_docstrings_v7.patch` results in the following doctest failures:\n\n```\nsage -t -long devel/sage-main/sage/misc/sagedoc.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/misc/sagedoc.py\", line 156:\n    sage: detex(r'More math: `x \\mapsto y`.  {\\bf Bold face}.')\nExpected:\n    'More math: `x  |-->  y`.  { Bold face}.'\nGot:\n    'More math: `x  |-->  y`.  {bf Bold face}.'\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_sagedoc.py\n\t [21.5 s]\n\n<SNIP>\n\nsage -t -long devel/sage-main/sage/misc/sageinspect.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/misc/sageinspect.py\", line 446:\n    sage: sage_getdoc(identity_matrix)[5:43]\nExpected:\n    'Return the `n times n` identity matrix'\nGot:\n    'Return the `n x n` identity matrix ove'\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_sageinspect.py\n\t [2.2 s]\n```\n",
    "created_at": "2009-07-23T09:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44203",
    "user": "mvngu"
}
```

With the patches at #6307, `trac_5653_pretty_docstrings_v7.patch` results in the following doctest failures:

```
sage -t -long devel/sage-main/sage/misc/sagedoc.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/misc/sagedoc.py", line 156:
    sage: detex(r'More math: `x \mapsto y`.  {\bf Bold face}.')
Expected:
    'More math: `x  |-->  y`.  { Bold face}.'
Got:
    'More math: `x  |-->  y`.  {bf Bold face}.'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_sagedoc.py
	 [21.5 s]

<SNIP>

sage -t -long devel/sage-main/sage/misc/sageinspect.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-main/sage/misc/sageinspect.py", line 446:
    sage: sage_getdoc(identity_matrix)[5:43]
Expected:
    'Return the `n times n` identity matrix'
Got:
    'Return the `n x n` identity matrix ove'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_sageinspect.py
	 [2.2 s]
```




---

archive/issue_comments_044204.json:
```json
{
    "body": "Attachment [trac_5653-doc.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653-doc.patch) by jhpalmieri created at 2009-07-23 15:24:49\n\napply on top of the other patch",
    "created_at": "2009-07-23T15:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44204",
    "user": "jhpalmieri"
}
```

Attachment [trac_5653-doc.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653-doc.patch) by jhpalmieri created at 2009-07-23 15:24:49

apply on top of the other patch



---

archive/issue_comments_044205.json:
```json
{
    "body": "I think \"trac_5653-doc.patch\" should fix the doctest failures.",
    "created_at": "2009-07-23T15:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44205",
    "user": "jhpalmieri"
}
```

I think "trac_5653-doc.patch" should fix the doctest failures.



---

archive/issue_comments_044206.json:
```json
{
    "body": "(Since it got a positive review earlier, I think that only the doctest failures should be an issue now.)",
    "created_at": "2009-07-23T15:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44206",
    "user": "jhpalmieri"
}
```

(Since it got a positive review earlier, I think that only the doctest failures should be an issue now.)



---

archive/issue_comments_044207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T22:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44207",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_044208.json:
```json
{
    "body": "With the patches\n1. `trac_5653_pretty_docstrings_v7.patch` and\n2. `trac_5653-doc.patch`\nall doctests pass. Merged both patches.",
    "created_at": "2009-07-23T22:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44208",
    "user": "mvngu"
}
```

With the patches
1. `trac_5653_pretty_docstrings_v7.patch` and
2. `trac_5653-doc.patch`
all doctests pass. Merged both patches.



---

archive/issue_comments_044209.json:
```json
{
    "body": "Did [attachment:trac_5653_pretty_docstrings_v7.patch] merge without incident?  The patch includes, e.g., `doc/en/introspect/templates/layout.html`, but it appears to be missing in v4.1.1.alpha1.  Or am I mistaken?",
    "created_at": "2009-07-28T14:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44209",
    "user": "mpatel"
}
```

Did [attachment:trac_5653_pretty_docstrings_v7.patch] merge without incident?  The patch includes, e.g., `doc/en/introspect/templates/layout.html`, but it appears to be missing in v4.1.1.alpha1.  Or am I mistaken?



---

archive/issue_comments_044210.json:
```json
{
    "body": "I regenerated the missing files with `hg revert --all`.  I'm not sure what happened, since I have not touched them at all in v4.1.1.alpha1.  I'll assume it was an isolated oddity.  Or has `MANIFEST.in` struck again?",
    "created_at": "2009-07-28T15:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44210",
    "user": "mpatel"
}
```

I regenerated the missing files with `hg revert --all`.  I'm not sure what happened, since I have not touched them at all in v4.1.1.alpha1.  I'll assume it was an isolated oddity.  Or has `MANIFEST.in` struck again?



---

archive/issue_comments_044211.json:
```json
{
    "body": "Replying to [comment:60 mpatel]:\n> I regenerated the missing files with `hg revert --all`.  I'm not sure what happened, since I have not touched them at all in v4.1.1.alpha1.  I'll assume it was an isolated oddity.  Or has `MANIFEST.in` struck again?\nYes. For this ticket and also for #4460. I'm about to restore these missing files by posting a patch against `MANIFEST.in`.",
    "created_at": "2009-07-28T15:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44211",
    "user": "mvngu"
}
```

Replying to [comment:60 mpatel]:
> I regenerated the missing files with `hg revert --all`.  I'm not sure what happened, since I have not touched them at all in v4.1.1.alpha1.  I'll assume it was an isolated oddity.  Or has `MANIFEST.in` struck again?
Yes. For this ticket and also for #4460. I'm about to restore these missing files by posting a patch against `MANIFEST.in`.



---

archive/issue_comments_044212.json:
```json
{
    "body": "For the patch `trac_5653_pretty_docstrings_v7.patch`, I assume that `doc/en/introspect/static/empty` is an empty file, right?",
    "created_at": "2009-07-28T16:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44212",
    "user": "mvngu"
}
```

For the patch `trac_5653_pretty_docstrings_v7.patch`, I assume that `doc/en/introspect/static/empty` is an empty file, right?



---

archive/issue_comments_044213.json:
```json
{
    "body": "Replying to [comment:62 mvngu]:\n> For the patch `trac_5653_pretty_docstrings_v7.patch`, I assume that `doc/en/introspect/static/empty` is an empty file, right?\nI think it contains just a newline character.  Thanks very much for making a patch.  I should have known by now, especially given recent events.  I suppose it's manifest density.",
    "created_at": "2009-07-28T16:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44213",
    "user": "mpatel"
}
```

Replying to [comment:62 mvngu]:
> For the patch `trac_5653_pretty_docstrings_v7.patch`, I assume that `doc/en/introspect/static/empty` is an empty file, right?
I think it contains just a newline character.  Thanks very much for making a patch.  I should have known by now, especially given recent events.  I suppose it's manifest density.



---

archive/issue_comments_044214.json:
```json
{
    "body": "Attachment [trac_5653-manifest.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653-manifest.patch) by mvngu created at 2009-07-28 17:54:04\n\nfix MANIFEST.in",
    "created_at": "2009-07-28T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44214",
    "user": "mvngu"
}
```

Attachment [trac_5653-manifest.patch](tarball://root/attachments/some-uuid/ticket5653/trac_5653-manifest.patch) by mvngu created at 2009-07-28 17:54:04

fix MANIFEST.in



---

archive/issue_comments_044215.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-28T17:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44215",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_044216.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-28T17:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44216",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_044217.json:
```json
{
    "body": "I'm reopening this ticket since the patch `trac_5653_pretty_docstrings_v7.patch` resulted in a corrupted repository in Sage 4.1.1.alpha1. This now should be resolved with the patch `trac_5653-manifest.patch`, which depends on the corresponding manifest patch for #4460. So apply patches in this order:\n1. the patches at #4460\n2. `trac_5653_pretty_docstrings_v7.patch`\n3. `trac_5653-doc.patch`\n4. `trac_5653-manifest.patch`\nOf these, only `trac_5653-manifest.patch` needs to be reviewed.",
    "created_at": "2009-07-28T17:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44217",
    "user": "mvngu"
}
```

I'm reopening this ticket since the patch `trac_5653_pretty_docstrings_v7.patch` resulted in a corrupted repository in Sage 4.1.1.alpha1. This now should be resolved with the patch `trac_5653-manifest.patch`, which depends on the corresponding manifest patch for #4460. So apply patches in this order:
1. the patches at #4460
2. `trac_5653_pretty_docstrings_v7.patch`
3. `trac_5653-doc.patch`
4. `trac_5653-manifest.patch`
Of these, only `trac_5653-manifest.patch` needs to be reviewed.



---

archive/issue_comments_044218.json:
```json
{
    "body": "trac_5653-manifest.patch looks good to me.",
    "created_at": "2009-07-28T18:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44218",
    "user": "jhpalmieri"
}
```

trac_5653-manifest.patch looks good to me.



---

archive/issue_comments_044219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-30T02:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44219",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_044220.json:
```json
{
    "body": "Merged:\n1. `trac_5653_pretty_docstrings_v7.patch`\n2. `trac_5653-doc.patch`\n3. `trac_5653-manifest.patch`",
    "created_at": "2009-07-30T02:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5653#issuecomment-44220",
    "user": "mvngu"
}
```

Merged:
1. `trac_5653_pretty_docstrings_v7.patch`
2. `trac_5653-doc.patch`
3. `trac_5653-manifest.patch`
