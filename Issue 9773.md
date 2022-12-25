# Issue 9773: Upgrade the notebook to use MathJax instead of jsMath

archive/issues_009773.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer @robert-marik @jhpalmieri rkirov @kcrisman @kini\n\n[MathJax](http://www.mathjax.org/) is the successor to [jsMath](http://www.math.union.edu/~dpvc/jsMath/).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9774\n\n",
    "created_at": "2010-08-21T09:36:05Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Upgrade the notebook to use MathJax instead of jsMath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9773",
    "user": "https://github.com/qed777"
}
```
Assignee: jason, was

CC:  @rbeezer @robert-marik @jhpalmieri rkirov @kcrisman @kini

[MathJax](http://www.mathjax.org/) is the successor to [jsMath](http://www.math.union.edu/~dpvc/jsMath/).

Issue created by migration from https://trac.sagemath.org/ticket/9774





---

archive/issue_comments_095633.json:
```json
{
    "body": "I've been experimenting a bit with `MathJax`, outside of the notebook.  Mostly thinking about how it will handle tex4ht output in jsMath mode, but here are some some observations that might be useful:\n\n1.  Easier in most ways to structure a page to use `MathJax`.  Just insert something like\n\n\n```\n<script type=\"text/javascript\" src=\"path-to-MathJax/MathJax.js\"></script>\n```\n\n\nNo need for a \"process()\" call at the end, etc.\n\n\n2.  Default is to not recognize single dollar-signs as delimiters.  Alternative is  `\\(..\\)`.  This would be a good thing, since if a user adds text (via TinyMCE) right now jsMath tries to parse the following as math.  `$$..$$` and  `\\[..\\]` both work for display math.  We would break lots of old worksheets if we stopped recognizing `$..$`.\n\n3.  There is a jsMath compatibility mode.  I believe I've found one bug in this already (reported upstream).  I'd imagine this is not a development priority, but who knows?\n\n4.  Modes and configuration is controlled globally by  `config/MathJax.js`  which is just one huge well-commented Javascript object.  It can be overridden in a web page by adding a new version into the script block mentioned above.  Maybe we want to make this easy for users to access, or maybe it is easy already, or maybe we don't want to bother.\n\n5.  This looks to me like the best introduction to the types of decisions we will want to make about what to cut over to:\nhttp://www.mathjax.org/resources/docs/?configuration.html\n\n6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.\n\n7.  I just noticed this morning that `html.table()` uses  `class=\"math\"` which is a jsMath way to tag span's or div's for processing.  I haven't found how to do something similiar in `MathJax`, though this will work in jsMath compatibility mode.  A very small test would indicate that the two modes can be used at the same time.\n\n8.  Consonant with (2) and (7), I'd love to see the notebook formatting move to something closer to rigorous XML (ie XHTML, I guess).  Certain types of processing would be easier if we did, but that is not really what this ticket is all about.",
    "created_at": "2010-08-24T18:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95633",
    "user": "https://github.com/rbeezer"
}
```

I've been experimenting a bit with `MathJax`, outside of the notebook.  Mostly thinking about how it will handle tex4ht output in jsMath mode, but here are some some observations that might be useful:

1.  Easier in most ways to structure a page to use `MathJax`.  Just insert something like


```
<script type="text/javascript" src="path-to-MathJax/MathJax.js"></script>
```


No need for a "process()" call at the end, etc.


2.  Default is to not recognize single dollar-signs as delimiters.  Alternative is  `\(..\)`.  This would be a good thing, since if a user adds text (via TinyMCE) right now jsMath tries to parse the following as math.  `$$..$$` and  `\[..\]` both work for display math.  We would break lots of old worksheets if we stopped recognizing `$..$`.

3.  There is a jsMath compatibility mode.  I believe I've found one bug in this already (reported upstream).  I'd imagine this is not a development priority, but who knows?

4.  Modes and configuration is controlled globally by  `config/MathJax.js`  which is just one huge well-commented Javascript object.  It can be overridden in a web page by adding a new version into the script block mentioned above.  Maybe we want to make this easy for users to access, or maybe it is easy already, or maybe we don't want to bother.

5.  This looks to me like the best introduction to the types of decisions we will want to make about what to cut over to:
http://www.mathjax.org/resources/docs/?configuration.html

6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.

7.  I just noticed this morning that `html.table()` uses  `class="math"` which is a jsMath way to tag span's or div's for processing.  I haven't found how to do something similiar in `MathJax`, though this will work in jsMath compatibility mode.  A very small test would indicate that the two modes can be used at the same time.

8.  Consonant with (2) and (7), I'd love to see the notebook formatting move to something closer to rigorous XML (ie XHTML, I guess).  Certain types of processing would be easier if we did, but that is not really what this ticket is all about.



---

archive/issue_comments_095634.json:
```json
{
    "body": "Thanks for comment, I feel that MathJax is much slower on cheap/older computer. This could be an important issue for using Sage in highschools and universities. Is it possible to keep both MathJax and jsMath and let the notebook admin to choose, which one will be used?",
    "created_at": "2010-08-24T19:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95634",
    "user": "https://github.com/robert-marik"
}
```

Thanks for comment, I feel that MathJax is much slower on cheap/older computer. This could be an important issue for using Sage in highschools and universities. Is it possible to keep both MathJax and jsMath and let the notebook admin to choose, which one will be used?



---

archive/issue_comments_095635.json:
```json
{
    "body": "Replying to [comment:2 rbeezer]:\n\n> 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.\n\n\nI think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.",
    "created_at": "2010-08-25T22:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95635",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 rbeezer]:

> 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.


I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.



---

archive/issue_comments_095636.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-10-15T01:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95636",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095637.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Replying to [comment:2 rbeezer]:\n> \n> > 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.\n> \n> \n> I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.\n\nJust in case you haven't thought of this, what Gollum (the [GitHub](GitHub) forum) folks did was host the MathJax fonts on Amazon S3, and then not include them in their distribution.  I don't know if that would work for you, but I wanted to point it out.",
    "created_at": "2010-10-21T20:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95637",
    "user": "https://trac.sagemath.org/admin/accounts/users/rminer"
}
```

Replying to [comment:4 jason]:
> Replying to [comment:2 rbeezer]:
> 
> > 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.
> 
> 
> I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.

Just in case you haven't thought of this, what Gollum (the [GitHub](GitHub) forum) folks did was host the MathJax fonts on Amazon S3, and then not include them in their distribution.  I don't know if that would work for you, but I wanted to point it out.



---

archive/issue_comments_095638.json:
```json
{
    "body": "Replying to [comment:10 rminer]:\n> Replying to [comment:4 jason]:\n> > Replying to [comment:2 rbeezer]:\n> > \n> > > 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.\n> > \n> > \n> > I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.\n> \n> Just in case you haven't thought of this, what Gollum (the [GitHub](GitHub) forum) folks did was host the MathJax fonts on Amazon S3, and then not include them in their distribution.  I don't know if that would work for you, but I wanted to point it out.\n\nThat's a very interesting solution.  I suppose we could host them on the main sage webserver, for example.  Or maybe Google Code or something like that so we had redundant sources.",
    "created_at": "2010-10-21T20:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95638",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 rminer]:
> Replying to [comment:4 jason]:
> > Replying to [comment:2 rbeezer]:
> > 
> > > 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.
> > 
> > 
> > I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.
> 
> Just in case you haven't thought of this, what Gollum (the [GitHub](GitHub) forum) folks did was host the MathJax fonts on Amazon S3, and then not include them in their distribution.  I don't know if that would work for you, but I wanted to point it out.

That's a very interesting solution.  I suppose we could host them on the main sage webserver, for example.  Or maybe Google Code or something like that so we had redundant sources.



---

archive/issue_comments_095639.json:
```json
{
    "body": "I just found the web page [http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home](http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home), which allows the use of Sphinx with MathJax.  Assuming it works, we could upgrade all of Sage (not just the notebook but also the docs), to use MathJax instead of jsMath.",
    "created_at": "2010-11-10T22:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95639",
    "user": "https://github.com/jhpalmieri"
}
```

I just found the web page [http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home](http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home), which allows the use of Sphinx with MathJax.  Assuming it works, we could upgrade all of Sage (not just the notebook but also the docs), to use MathJax instead of jsMath.



---

archive/issue_comments_095640.json:
```json
{
    "body": "[MathJax](http://www.mathjax.org/) is very impressive looking. I like the idea the user does not have to have any fonts installed on his computer, which is a major advantage over [jsMath](http://www.math.union.edu/~dpvc/jsMath/)\n\nDave",
    "created_at": "2011-03-02T20:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95640",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

[MathJax](http://www.mathjax.org/) is very impressive looking. I like the idea the user does not have to have any fonts installed on his computer, which is a major advantage over [jsMath](http://www.math.union.edu/~dpvc/jsMath/)

Dave



---

archive/issue_comments_095641.json:
```json
{
    "body": "Screenshot of double integral",
    "created_at": "2011-03-22T22:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95641",
    "user": "https://github.com/rbeezer"
}
```

Screenshot of double integral



---

archive/issue_comments_095642.json:
```json
{
    "body": "Attachment [mathjax-matrix-20110322.png](tarball://root/attachments/some-uuid/ticket9774/mathjax-matrix-20110322.png) by @rbeezer created at 2011-03-22 22:49:31\n\nScreenshot of matrix",
    "created_at": "2011-03-22T22:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95642",
    "user": "https://github.com/rbeezer"
}
```

Attachment [mathjax-matrix-20110322.png](tarball://root/attachments/some-uuid/ticket9774/mathjax-matrix-20110322.png) by @rbeezer created at 2011-03-22 22:49:31

Screenshot of matrix



---

archive/issue_comments_095643.json:
```json
{
    "body": "Steps that will install `MathJax` with the new Flask notebook.  \n\n1. Install the Flask version of the notebook.\n   {{{\n   http://code.google.com/r/rkirov-flask/\n   }}}\n\n2. Download v1.1 of `MathJax` as zip file (from bottom of page).\n   {{{\n   http://www.mathjax.org/download/\n   }}}\n\n3.  Unzip the MathJax distribution into\n\n   $SAGE_ROOT/devel/sagenb/sagenb/data\n\n   and\n\n   rename the new directory: `mathjax-MathJax-5a7e4d7` (or whatever)\n\n   to be just the directory:  `MathJax`\n\n4.  jsmath compatibility.  Edit\n   {{{\n   $SAGE_ROOT/devel/sagenb/sagenb/data/MathJax/config/default.js\n   }}}\n   by adding \"`jsMath2jax.js`\" as the first entry of the \"extensions\" list, so it becomes\n   {{{\n   extensions: [\"jsMath2jax.js\", \"tex2jax.js\"]\n   }}}\n\n5. Edit\n   {{{\n   $SAGE_ROOT/devel/sagenb/sagenb/data/sage/html/notebook/base.html\n   }}}\n   and change\n   {{{\n   <script type=\"text/javascript\" src=\"/javascript/sage/jsmath.js\"></script>\n   }}}\n   to\n   {{{\n   <script type=\"text/javascript\" src=\"/static/MathJax/MathJax.js?config=default\"></script>\n   }}}\n\n\nThis will install `MathJax` and the notebook will use it.  But the setup is buggy, so needs work.  I'm sure there is some configuration on the Sage side and/or the `MathJax` side that will need changes.\n\n* A mix of black and green symbols.\n\n* Only renders on a reload - adding new TeX via TinyMCE returns with an error about not finding fonts.\n\n* Some stray tags are being rendered, or something.\n\nScreenshots attached:\n\nDouble Integral:\n\nhttp://wiki.math.toronto.edu/TorontoMathWiki/index.php/JsMath/MathJax_%28TeX_for_Web%29\n\n```\n$$ (2\\pi h)^{-d}\\iint_{\\{H(x,\\xi) <\\tau\\}} dx d\\xi $$\n```\n\n\nMatrix:\n\n```\n$\\begin{bmatrix}\nx^2 & y^2\\\\\nx^3 & \\cos(z)\n\\end{bmatrix}$\n```\n",
    "created_at": "2011-03-22T22:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95643",
    "user": "https://github.com/rbeezer"
}
```

Steps that will install `MathJax` with the new Flask notebook.  

1. Install the Flask version of the notebook.
   {{{
   http://code.google.com/r/rkirov-flask/
   }}}

2. Download v1.1 of `MathJax` as zip file (from bottom of page).
   {{{
   http://www.mathjax.org/download/
   }}}

3.  Unzip the MathJax distribution into

   $SAGE_ROOT/devel/sagenb/sagenb/data

   and

   rename the new directory: `mathjax-MathJax-5a7e4d7` (or whatever)

   to be just the directory:  `MathJax`

4.  jsmath compatibility.  Edit
   {{{
   $SAGE_ROOT/devel/sagenb/sagenb/data/MathJax/config/default.js
   }}}
   by adding "`jsMath2jax.js`" as the first entry of the "extensions" list, so it becomes
   {{{
   extensions: ["jsMath2jax.js", "tex2jax.js"]
   }}}

5. Edit
   {{{
   $SAGE_ROOT/devel/sagenb/sagenb/data/sage/html/notebook/base.html
   }}}
   and change
   {{{
   <script type="text/javascript" src="/javascript/sage/jsmath.js"></script>
   }}}
   to
   {{{
   <script type="text/javascript" src="/static/MathJax/MathJax.js?config=default"></script>
   }}}


This will install `MathJax` and the notebook will use it.  But the setup is buggy, so needs work.  I'm sure there is some configuration on the Sage side and/or the `MathJax` side that will need changes.

* A mix of black and green symbols.

* Only renders on a reload - adding new TeX via TinyMCE returns with an error about not finding fonts.

* Some stray tags are being rendered, or something.

Screenshots attached:

Double Integral:

http://wiki.math.toronto.edu/TorontoMathWiki/index.php/JsMath/MathJax_%28TeX_for_Web%29

```
$$ (2\pi h)^{-d}\iint_{\{H(x,\xi) <\tau\}} dx d\xi $$
```


Matrix:

```
$\begin{bmatrix}
x^2 & y^2\\
x^3 & \cos(z)
\end{bmatrix}$
```




---

archive/issue_comments_095644.json:
```json
{
    "body": "I'm attaching a draft of a patch for the Sage library.  The integration with Sphinx is completely untested, and is probably broken.  See the top of the patch file for a list of things to do.",
    "created_at": "2011-06-14T22:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95644",
    "user": "https://github.com/jhpalmieri"
}
```

I'm attaching a draft of a patch for the Sage library.  The integration with Sphinx is completely untested, and is probably broken.  See the top of the patch file for a list of things to do.



---

archive/issue_comments_095645.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-flask-notebook.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook.patch) by @rbeezer created at 2011-06-16 03:25:09",
    "created_at": "2011-06-16T03:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95645",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9774-mathjax-flask-notebook.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook.patch) by @rbeezer created at 2011-06-16 03:25:09



---

archive/issue_comments_095646.json:
```json
{
    "body": "Added patch to Flask notebook code to support `MathJax`, built with Davide Cervone's help.\n\n1.  This is a hand-edited patch to recover from an hg mess-up.  I think it is OK, but be wary.\n2.  Fonts are coming from `MathJax` CDN.  Comment in code indicates change for local `MathJax` installation.\n3.  `<script>` tags added by Palmieri's Sage library patch need to be handled with care on notebook side, so notebook does not evaluate them.  Right now when \"Typeset\" box is checked, evaluated cells raise a Javascript error in `evaluate_script_tags` (or a function with a similar name).",
    "created_at": "2011-06-16T03:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95646",
    "user": "https://github.com/rbeezer"
}
```

Added patch to Flask notebook code to support `MathJax`, built with Davide Cervone's help.

1.  This is a hand-edited patch to recover from an hg mess-up.  I think it is OK, but be wary.
2.  Fonts are coming from `MathJax` CDN.  Comment in code indicates change for local `MathJax` installation.
3.  `<script>` tags added by Palmieri's Sage library patch need to be handled with care on notebook side, so notebook does not evaluate them.  Right now when "Typeset" box is checked, evaluated cells raise a Javascript error in `evaluate_script_tags` (or a function with a similar name).



---

archive/issue_comments_095647.json:
```json
{
    "body": "John's patch doesn't apply cleanly to stock 4.7; does it apply to the most recent alpha of 4.7.1?\n\n\n```\napplying mathjax.patch\npatching file sage/misc/latex.py\nHunk #15 succeeded at 1750 with fuzz 2 (offset 2 lines).\nHunk #23 FAILED at 2382\n1 out of 25 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh mathjax.patch\n\n\n```\n",
    "created_at": "2011-06-16T04:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95647",
    "user": "https://github.com/jasongrout"
}
```

John's patch doesn't apply cleanly to stock 4.7; does it apply to the most recent alpha of 4.7.1?


```
applying mathjax.patch
patching file sage/misc/latex.py
Hunk #15 succeeded at 1750 with fuzz 2 (offset 2 lines).
Hunk #23 FAILED at 2382
1 out of 25 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh mathjax.patch


```




---

archive/issue_comments_095648.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n> John's patch doesn't apply cleanly to stock 4.7; does it apply to the most recent alpha of 4.7.1?\n\nYes.\n\n\n```\nrob@tiger:/sage/dev/devel/sage$ ../../sage -version\n* Warning: this is a prerelease version, and it may be unstable.     *\nrob@tiger:/sage/dev/devel/sage$ hg qimport -P http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/mathjax.patch\nadding mathjax.patch to series file\napplying mathjax.patch\nnow at: mathjax.patch\n```\n",
    "created_at": "2011-06-16T05:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95648",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:18 jason]:
> John's patch doesn't apply cleanly to stock 4.7; does it apply to the most recent alpha of 4.7.1?

Yes.


```
rob@tiger:/sage/dev/devel/sage$ ../../sage -version
* Warning: this is a prerelease version, and it may be unstable.     *
rob@tiger:/sage/dev/devel/sage$ hg qimport -P http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/mathjax.patch
adding mathjax.patch to series file
applying mathjax.patch
now at: mathjax.patch
```




---

archive/issue_comments_095649.json:
```json
{
    "body": "Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?",
    "created_at": "2011-06-16T05:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95649",
    "user": "https://github.com/jasongrout"
}
```

Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?



---

archive/issue_comments_095650.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-flask-notebook-file-add.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook-file-add.patch) by @rbeezer created at 2011-06-16 05:30:09",
    "created_at": "2011-06-16T05:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95650",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9774-mathjax-flask-notebook-file-add.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook-file-add.patch) by @rbeezer created at 2011-06-16 05:30:09



---

archive/issue_comments_095651.json:
```json
{
    "body": "Attached a patch to add `sagenb/notebook/mathjax.py`\n\nNew file is similar to, but not identical to, `sagenb/notebook/jsmath.py`\n\nWe did not delete the latter, but I think it can safely go away.",
    "created_at": "2011-06-16T05:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95651",
    "user": "https://github.com/rbeezer"
}
```

Attached a patch to add `sagenb/notebook/mathjax.py`

New file is similar to, but not identical to, `sagenb/notebook/jsmath.py`

We did not delete the latter, but I think it can safely go away.



---

archive/issue_comments_095652.json:
```json
{
    "body": "Replying to [comment:20 jason]:\n> Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?\n\nWe need an spkg to be Internet-independent.  \n\nWe did not experiment with your old one.  I think it would be best to make a new one.  This requires a small edit (once you are sure all works with CDN version).\n\nFont suggestions coming up.",
    "created_at": "2011-06-16T05:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95652",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:20 jason]:
> Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?

We need an spkg to be Internet-independent.  

We did not experiment with your old one.  I think it would be best to make a new one.  This requires a small edit (once you are sure all works with CDN version).

Font suggestions coming up.



---

archive/issue_comments_095653.json:
```json
{
    "body": "Davide Cervone says for an spkg we need only keep font subdirectories called\n\n\n```\notf,  eot,  svg\n```\n\n\nIn particular `png` subdirectories are huge-est and can go away.\n\nRob",
    "created_at": "2011-06-16T05:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95653",
    "user": "https://github.com/rbeezer"
}
```

Davide Cervone says for an spkg we need only keep font subdirectories called


```
otf,  eot,  svg
```


In particular `png` subdirectories are huge-est and can go away.

Rob



---

archive/issue_comments_095654.json:
```json
{
    "body": "ah; I bet it's because the svg fonts replace the png fonts for all browsers we care about, or something.  Okay, Davide is the final authority on what browsers support what...",
    "created_at": "2011-06-16T05:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95654",
    "user": "https://github.com/jasongrout"
}
```

ah; I bet it's because the svg fonts replace the png fonts for all browsers we care about, or something.  Okay, Davide is the final authority on what browsers support what...



---

archive/issue_comments_095655.json:
```json
{
    "body": "I get an error from the line: `response = make_response(render_template('js/mathjax.js', theme_mathjax_macros=mathjax_macros))` in flask_version/base.py.  I see a jsmath.js template in `sagenb/data/sage/js/jsmath.js` template.  Is this another file that didn't get added to the patch?",
    "created_at": "2011-06-16T06:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95655",
    "user": "https://github.com/jasongrout"
}
```

I get an error from the line: `response = make_response(render_template('js/mathjax.js', theme_mathjax_macros=mathjax_macros))` in flask_version/base.py.  I see a jsmath.js template in `sagenb/data/sage/js/jsmath.js` template.  Is this another file that didn't get added to the patch?



---

archive/issue_comments_095656.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-flask-notebook-file-add-two.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook-file-add-two.patch) by @rbeezer created at 2011-06-16 06:33:03",
    "created_at": "2011-06-16T06:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95656",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9774-mathjax-flask-notebook-file-add-two.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-notebook-file-add-two.patch) by @rbeezer created at 2011-06-16 06:33:03



---

archive/issue_comments_095657.json:
```json
{
    "body": "Replying to [comment:25 jason]:\n> Is this another file that didn't get added to the patch?\n\nYes, same situation - \"old\" file could be removed.\n\n\"file-add-two\" should create the missing file.  Sorry about all the problems - my `hg status` is useless with the hg mess-up.\n\nThis file will require an edit when we move from CDN to spkg.\n\nThank-you!!!!!!!!!!!!!!",
    "created_at": "2011-06-16T06:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95657",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:25 jason]:
> Is this another file that didn't get added to the patch?

Yes, same situation - "old" file could be removed.

"file-add-two" should create the missing file.  Sorry about all the problems - my `hg status` is useless with the hg mess-up.

This file will require an edit when we move from CDN to spkg.

Thank-you!!!!!!!!!!!!!!



---

archive/issue_comments_095658.json:
```json
{
    "body": "I have a working version, but there still seems to be something slightly different about Typeset mode compared to before. I'm posting my patch, but there is still *lots* of debugging stuff in the patch that should be taken out before a final version is posted.",
    "created_at": "2011-06-16T09:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95658",
    "user": "https://github.com/jasongrout"
}
```

I have a working version, but there still seems to be something slightly different about Typeset mode compared to before. I'm posting my patch, but there is still *lots* of debugging stuff in the patch that should be taken out before a final version is posted.



---

archive/issue_comments_095659.json:
```json
{
    "body": "apply to sagenb repository; apply on top of previous patches",
    "created_at": "2011-06-16T09:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95659",
    "user": "https://github.com/jasongrout"
}
```

apply to sagenb repository; apply on top of previous patches



---

archive/issue_comments_095660.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-flask-eval-script.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-eval-script.patch) by @rbeezer created at 2011-06-17 17:37:44\n\nThe problem with the Sage notebook code intercepting (and evaluating) the contents of `<script>,</script>` tags can probably be rectified in one, or both, of the functions of the Flask notebook:\n\n\n```\nIn sagenb/data/sage/js/notebook_lib.js:\n\neval_script_tags\nseparate_script_tags\n```\n",
    "created_at": "2011-06-17T17:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95660",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9774-mathjax-flask-eval-script.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-flask-eval-script.patch) by @rbeezer created at 2011-06-17 17:37:44

The problem with the Sage notebook code intercepting (and evaluating) the contents of `<script>,</script>` tags can probably be rectified in one, or both, of the functions of the Flask notebook:


```
In sagenb/data/sage/js/notebook_lib.js:

eval_script_tags
separate_script_tags
```




---

archive/issue_comments_095661.json:
```json
{
    "body": "rbeezer: yes, that's what my patch does.  The current remaining problem is something different.",
    "created_at": "2011-06-17T19:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95661",
    "user": "https://github.com/jasongrout"
}
```

rbeezer: yes, that's what my patch does.  The current remaining problem is something different.



---

archive/issue_comments_095662.json:
```json
{
    "body": "In the current version of [attachment:mathjax.patch], look at the top of the file for some unfinished business.  For example, the pathname at the end of doc/common/themes/sage/static/mathjax_sage.js_t might be wrong, which might break MathJax in the Sphinx documentation.",
    "created_at": "2011-06-20T18:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95662",
    "user": "https://github.com/jhpalmieri"
}
```

In the current version of [attachment:mathjax.patch], look at the top of the file for some unfinished business.  For example, the pathname at the end of doc/common/themes/sage/static/mathjax_sage.js_t might be wrong, which might break MathJax in the Sphinx documentation.



---

archive/issue_comments_095663.json:
```json
{
    "body": "In the current state, the --mathjax  switch seems to work with a build of the html version of the reference manual.\n\nMathematics in the documentation is being wrapped with `\\(, \\)` pairs, which are the default MathJax delimiters for inline mathematics.  However these snippets are not being rendered when viewed in a browser.\n\nIn the page source of a page of the html documentation, I see a script in a file named `mathjax_sage.js` which we are not generating.  We do have `jsmath_sage.js` lying about in the doc directories, which have the full jsmath configuration information.  So this likely needs repair before an HTML documentation page with MathJax support is built properly.",
    "created_at": "2011-06-20T19:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95663",
    "user": "https://github.com/rbeezer"
}
```

In the current state, the --mathjax  switch seems to work with a build of the html version of the reference manual.

Mathematics in the documentation is being wrapped with `\(, \)` pairs, which are the default MathJax delimiters for inline mathematics.  However these snippets are not being rendered when viewed in a browser.

In the page source of a page of the html documentation, I see a script in a file named `mathjax_sage.js` which we are not generating.  We do have `jsmath_sage.js` lying about in the doc directories, which have the full jsmath configuration information.  So this likely needs repair before an HTML documentation page with MathJax support is built properly.



---

archive/issue_comments_095664.json:
```json
{
    "body": "OK, I can force `mathjax_sage.js` to be created by totally trashing some of the documentation output with\n\n\n```\ndevel/sage/doc/output/html$ rm -rf en\n```\n\n\nbefore rebuilding the HTML reference documentation. It comes from a template file `mathjax_sage.js_t` that one of the patches creates properly.\n\nMathematics still does not render, but I think the MathJax configuration is looking locally.  Time for a local MathJax install, I think.",
    "created_at": "2011-06-20T21:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95664",
    "user": "https://github.com/rbeezer"
}
```

OK, I can force `mathjax_sage.js` to be created by totally trashing some of the documentation output with


```
devel/sage/doc/output/html$ rm -rf en
```


before rebuilding the HTML reference documentation. It comes from a template file `mathjax_sage.js_t` that one of the patches creates properly.

Mathematics still does not render, but I think the MathJax configuration is looking locally.  Time for a local MathJax install, I think.



---

archive/issue_comments_095665.json:
```json
{
    "body": "In a page of the documentation, I inserted manually\n\n\n```\n<script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full\">\n```\n\n\nand the mathematics rendered properly with MathJax.\n\nThen I installed the mathjax 1.1a distribution alongside jsmath in the Flask notebook tree and used\n\n\n```\n<script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full\">\n```\n\n\nwhich also caused the math to render properly.  (/sage/notebook is my `SAGE_ROOT`)\n\nIn both cases the fonts did not look too great to my eye.\n\nQuestions:\n\n(a) How do we get these scripts commands to be placed properly in each page of the docs, with a proper relative path?\n\n(b) Is there really a clean separation between Sage and the notebook if  --mathjax  mode for documentation requires the MathJax code from the notebook?",
    "created_at": "2011-06-20T23:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95665",
    "user": "https://github.com/rbeezer"
}
```

In a page of the documentation, I inserted manually


```
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full">
```


and the mathematics rendered properly with MathJax.

Then I installed the mathjax 1.1a distribution alongside jsmath in the Flask notebook tree and used


```
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full">
```


which also caused the math to render properly.  (/sage/notebook is my `SAGE_ROOT`)

In both cases the fonts did not look too great to my eye.

Questions:

(a) How do we get these scripts commands to be placed properly in each page of the docs, with a proper relative path?

(b) Is there really a clean separation between Sage and the notebook if  --mathjax  mode for documentation requires the MathJax code from the notebook?



---

archive/issue_comments_095666.json:
```json
{
    "body": "Replying to [comment:33 rbeezer]:\n> Then I installed the mathjax 1.1a distribution alongside jsmath in the Flask notebook tree and \n\n> which also caused the math to render properly.  (/sage/notebook is my `SAGE_ROOT`)\n\nOops, the incantation for a local install of MathJax should have been\n\n\n```\n<script type=\"text/javascript\" src=\"/sage/notebook/devel/rkirov-flask/sagenb/data/mathjax/MathJax.js?config=TeX-AMS_HTML-full\"></script>\n```\n",
    "created_at": "2011-06-21T00:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95666",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:33 rbeezer]:
> Then I installed the mathjax 1.1a distribution alongside jsmath in the Flask notebook tree and 

> which also caused the math to render properly.  (/sage/notebook is my `SAGE_ROOT`)

Oops, the incantation for a local install of MathJax should have been


```
<script type="text/javascript" src="/sage/notebook/devel/rkirov-flask/sagenb/data/mathjax/MathJax.js?config=TeX-AMS_HTML-full"></script>
```




---

archive/issue_comments_095667.json:
```json
{
    "body": "Here's a new version of my patch.  With a locally installed version of MathJax, the documentation seems to render properly.  I don't know if this is the best solution, but at least it seems to work.\n\n(I installed MathJax by downloading a zip file: [https://github.com/mathjax/MathJax/zipball/v1.1a](https://github.com/mathjax/MathJax/zipball/v1.1a).  I unzipped it and renamed the resulting directory to `mathjax`, and moved it to `SAGE_ROOT/local/lib/python/site-packages/sagenb-0.9.0-py2.6.egg/sagenb/data/`, alongside of the old `jsmath` directory.  I also put a copy of the `mathjax` directory in `SAGE_ROOT/devel/sagenb/sagenb/data/`.  I haven't tried to install local fonts.)",
    "created_at": "2011-07-01T02:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95667",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new version of my patch.  With a locally installed version of MathJax, the documentation seems to render properly.  I don't know if this is the best solution, but at least it seems to work.

(I installed MathJax by downloading a zip file: [https://github.com/mathjax/MathJax/zipball/v1.1a](https://github.com/mathjax/MathJax/zipball/v1.1a).  I unzipped it and renamed the resulting directory to `mathjax`, and moved it to `SAGE_ROOT/local/lib/python/site-packages/sagenb-0.9.0-py2.6.egg/sagenb/data/`, alongside of the old `jsmath` directory.  I also put a copy of the `mathjax` directory in `SAGE_ROOT/devel/sagenb/sagenb/data/`.  I haven't tried to install local fonts.)



---

archive/issue_comments_095668.json:
```json
{
    "body": "Attachment [mathjax.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax.patch) by @jhpalmieri created at 2011-07-01 02:22:35\n\n(experimental) patch for Sage library",
    "created_at": "2011-07-01T02:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95668",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [mathjax.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax.patch) by @jhpalmieri created at 2011-07-01 02:22:35

(experimental) patch for Sage library



---

archive/issue_comments_095669.json:
```json
{
    "body": "By the way, one comment about the latest version of my patch: it fixes the problem Rob mentioned about getting the appropriate invocation to MathJax in each piece of documentation.  It does this by setting the variable `mathjax_path` to\n\n```\nfile://[path to MathJax.js]?config=TeX-AMS_HTML-full,file://[path to mathjax_sage.js]\n```\n\nThe paths here are absolute ones, in `SAGE_ROOT/devel/sage/doc/output/html/en/_static/`.  This directory is created by `sage -docbuild website html`, so now if you build the docs with the `-j` flag (to enable MathJax), it first builds the website target, then builds whatever you requested.  There might be a better way to do this, using relative paths, but I couldn't get it to work.    For example, using \n\n```\n    <script type=\"text/javascript\" src=\"_static/MathJax.js?config=TeX-AMS_HTML-full\"></script>\n```\n\nsuccessfully turns on MathJax, but without the local configuration turning on the custom macros.  Using\n\n```\n    <script type=\"text/javascript\" src=\"_static/MathJax.js?config=TeX-AMS_HTML-full,mathjax_sage.js\"></script>\n```\n\ndoesn't work, nor does any variation of it that I tried.  (Note that when you change the path specifying the local configuration file, you also need to change the last line of that configuration file to match it, according to [http://www.mathjax.org/docs/1.1/configuration.html](http://www.mathjax.org/docs/1.1/configuration.html).)  If we could copy the file `mathjax_sage.js` to `_static/config/local/`, then we could use \n\n```\n    <script type=\"text/javascript\" src=\"_static/MathJax.js?config=TeX-AMS_HTML-full,local/mathjax_sage.js\"></script>\n```\n\nfor the invocation, and \n\n```\nMathJax.Ajax.loadComplete(\"[MathJax]/config/local/mathjax_sage.js\")\n```\n\nfor the last line in mathjax_sage.js.  But I don't know how to put this file in the right place: it's autogenerated, so we can't put it in the MathJax local directory ahead of time, and I can't figure out how to get Sphinx to do it when it's building the documentation.\n\nAnother option would be to try to get Sphinx to write this into each html file:\n\n```\n<script type=\"text/x-mathjax-config\">\n[contents of mathjax_sage.js]\n</script>\n<script type=\"text/javascript\" src=\"_static/MathJax.js?config=TeX-AMS_HTML-full\"></script>\n```\n\nWe can get the last line by specifing mathjax_path in conf.py, but I don't know how to get the first part.\n\nI'll keep working on it...",
    "created_at": "2011-07-01T03:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95669",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, one comment about the latest version of my patch: it fixes the problem Rob mentioned about getting the appropriate invocation to MathJax in each piece of documentation.  It does this by setting the variable `mathjax_path` to

```
file://[path to MathJax.js]?config=TeX-AMS_HTML-full,file://[path to mathjax_sage.js]
```

The paths here are absolute ones, in `SAGE_ROOT/devel/sage/doc/output/html/en/_static/`.  This directory is created by `sage -docbuild website html`, so now if you build the docs with the `-j` flag (to enable MathJax), it first builds the website target, then builds whatever you requested.  There might be a better way to do this, using relative paths, but I couldn't get it to work.    For example, using 

```
    <script type="text/javascript" src="_static/MathJax.js?config=TeX-AMS_HTML-full"></script>
```

successfully turns on MathJax, but without the local configuration turning on the custom macros.  Using

```
    <script type="text/javascript" src="_static/MathJax.js?config=TeX-AMS_HTML-full,mathjax_sage.js"></script>
```

doesn't work, nor does any variation of it that I tried.  (Note that when you change the path specifying the local configuration file, you also need to change the last line of that configuration file to match it, according to [http://www.mathjax.org/docs/1.1/configuration.html](http://www.mathjax.org/docs/1.1/configuration.html).)  If we could copy the file `mathjax_sage.js` to `_static/config/local/`, then we could use 

```
    <script type="text/javascript" src="_static/MathJax.js?config=TeX-AMS_HTML-full,local/mathjax_sage.js"></script>
```

for the invocation, and 

```
MathJax.Ajax.loadComplete("[MathJax]/config/local/mathjax_sage.js")
```

for the last line in mathjax_sage.js.  But I don't know how to put this file in the right place: it's autogenerated, so we can't put it in the MathJax local directory ahead of time, and I can't figure out how to get Sphinx to do it when it's building the documentation.

Another option would be to try to get Sphinx to write this into each html file:

```
<script type="text/x-mathjax-config">
[contents of mathjax_sage.js]
</script>
<script type="text/javascript" src="_static/MathJax.js?config=TeX-AMS_HTML-full"></script>
```

We can get the last line by specifing mathjax_path in conf.py, but I don't know how to get the first part.

I'll keep working on it...



---

archive/issue_comments_095670.json:
```json
{
    "body": "Hi John,\n\nAre you testing with the Flask notebook?  If not, it might be easier to build what look like absolute paths to the MathJax files in the data directory of the notebook, because of the way Flask sets up paths with the \"route()\" command?  I can't tell if this will solve the problem you are wrestling with or not.\n\nThe `<script>` tags were being messed with by the notebook on the server side just before being dispatched.  But then the client sees two versions - wrapped and unwrapped, and totally trashes one of them to prevent running a script twice.  I thought Jason had a patch for this too, but I haven't seen it.  The symptom would be when you cycle through wrap, no-wrap, and hide for some output, then one of them is missing.  I guess we can press on and fix this eventually.\n\nAbout to go off-line shortly for the long weekend, but will come back to this when I can stick with it.\n\nRob",
    "created_at": "2011-07-01T04:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95670",
    "user": "https://github.com/rbeezer"
}
```

Hi John,

Are you testing with the Flask notebook?  If not, it might be easier to build what look like absolute paths to the MathJax files in the data directory of the notebook, because of the way Flask sets up paths with the "route()" command?  I can't tell if this will solve the problem you are wrestling with or not.

The `<script>` tags were being messed with by the notebook on the server side just before being dispatched.  But then the client sees two versions - wrapped and unwrapped, and totally trashes one of them to prevent running a script twice.  I thought Jason had a patch for this too, but I haven't seen it.  The symptom would be when you cycle through wrap, no-wrap, and hide for some output, then one of them is missing.  I guess we can press on and fix this eventually.

About to go off-line shortly for the long weekend, but will come back to this when I can stick with it.

Rob



---

archive/issue_comments_095671.json:
```json
{
    "body": "For building the documentation, the notebook isn't relevant: they get built from the command line.  I think that when trying to make MathJax work with the notebook, we'll want to construct the URLs differently than I'm doing for the docs, but I don't know enough about the paths, etc., in the notebook to say exactly how to do it.  For what it's worth, though, I have been using the flask notebook.",
    "created_at": "2011-07-01T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95671",
    "user": "https://github.com/jhpalmieri"
}
```

For building the documentation, the notebook isn't relevant: they get built from the command line.  I think that when trying to make MathJax work with the notebook, we'll want to construct the URLs differently than I'm doing for the docs, but I don't know enough about the paths, etc., in the notebook to say exactly how to do it.  For what it's worth, though, I have been using the flask notebook.



---

archive/issue_comments_095672.json:
```json
{
    "body": "I've uploaded my current flask patch queue here: http://sage.math.washington.edu/home/jason/mathjax-flask-patches.tar.gz  My current (probably non-working) patch queue for my sage library, including two mathjax patches, is here: \nhttp://sage.math.washington.edu/home/jason/mathjax-sage-patches.tar.gz\n\nThese are both works-in-progress, but currently stalled for at least a week or two.",
    "created_at": "2011-07-01T06:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95672",
    "user": "https://github.com/jasongrout"
}
```

I've uploaded my current flask patch queue here: http://sage.math.washington.edu/home/jason/mathjax-flask-patches.tar.gz  My current (probably non-working) patch queue for my sage library, including two mathjax patches, is here: 
http://sage.math.washington.edu/home/jason/mathjax-sage-patches.tar.gz

These are both works-in-progress, but currently stalled for at least a week or two.



---

archive/issue_comments_095673.json:
```json
{
    "body": "I stalled working on it because of other time pressures with the single-cell, but also because I realized that the *next* version of Sphinx supports Mathjax out of the box, while I thought the current version would require patches.",
    "created_at": "2011-07-01T06:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95673",
    "user": "https://github.com/jasongrout"
}
```

I stalled working on it because of other time pressures with the single-cell, but also because I realized that the *next* version of Sphinx supports Mathjax out of the box, while I thought the current version would require patches.



---

archive/issue_comments_095674.json:
```json
{
    "body": "I think that the implementation of MathJax in Sphinx comes from the file mathjax.py, which is available for download separately.  So my patch just adds it.\n\nI'm attaching another version (\"v2\") of my patch; this one writes the MathJax local configuration file to a file in `SAGE_ROOT/local/lib/python/site-libraries/sagenb.../`, which may not be a good idea.  But it allows for a simpler invocation of MathJax.  I'm really not sure which approach is better.",
    "created_at": "2011-07-01T06:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95674",
    "user": "https://github.com/jhpalmieri"
}
```

I think that the implementation of MathJax in Sphinx comes from the file mathjax.py, which is available for download separately.  So my patch just adds it.

I'm attaching another version ("v2") of my patch; this one writes the MathJax local configuration file to a file in `SAGE_ROOT/local/lib/python/site-libraries/sagenb.../`, which may not be a good idea.  But it allows for a simpler invocation of MathJax.  I'm really not sure which approach is better.



---

archive/issue_comments_095675.json:
```json
{
    "body": "Attachment [mathjax.v2.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax.v2.patch) by @jhpalmieri created at 2011-07-01 06:12:32\n\n(experimental) patch for Sage library, alternate version",
    "created_at": "2011-07-01T06:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95675",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [mathjax.v2.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax.v2.patch) by @jhpalmieri created at 2011-07-01 06:12:32

(experimental) patch for Sage library, alternate version



---

archive/issue_comments_095676.json:
```json
{
    "body": "What is the current status on this now?  Where should we start working on it again?",
    "created_at": "2012-01-09T20:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95676",
    "user": "https://github.com/jasongrout"
}
```

What is the current status on this now?  Where should we start working on it again?



---

archive/issue_comments_095677.json:
```json
{
    "body": "The last patch involving MathJax, that I rebased from the ones here is on google code:\n\nhttp://code.google.com/p/sagenb/issues/detail?id=46\n\nUnless Jonathan Gutow did something else on top of it, this is latest work.",
    "created_at": "2012-01-10T03:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95677",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

The last patch involving MathJax, that I rebased from the ones here is on google code:

http://code.google.com/p/sagenb/issues/detail?id=46

Unless Jonathan Gutow did something else on top of it, this is latest work.



---

archive/issue_comments_095678.json:
```json
{
    "body": "Rebased version of comprehensive mathjax patch to 4.8.alpha4",
    "created_at": "2012-01-11T06:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95678",
    "user": "https://github.com/jasongrout"
}
```

Rebased version of comprehensive mathjax patch to 4.8.alpha4



---

archive/issue_comments_095679.json:
```json
{
    "body": "Attachment [mathjax-try2.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax-try2.patch) by @jasongrout created at 2012-01-12 23:16:31\n\nApply only this patch",
    "created_at": "2012-01-12T23:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95679",
    "user": "https://github.com/jasongrout"
}
```

Attachment [mathjax-try2.patch](tarball://root/attachments/some-uuid/ticket9774/mathjax-try2.patch) by @jasongrout created at 2012-01-12 23:16:31

Apply only this patch



---

archive/issue_events_024502.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2012-01-12T23:18:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24502"
}
```



---

archive/issue_comments_095680.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-13T21:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95680",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095681.json:
```json
{
    "body": "apply to **scripts** repository",
    "created_at": "2012-01-13T22:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95681",
    "user": "https://github.com/jasongrout"
}
```

apply to **scripts** repository



---

archive/issue_comments_095682.json:
```json
{
    "body": "Attachment [trac_9774-scripts-mathjax.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-scripts-mathjax.patch) by @jasongrout created at 2012-01-13 22:30:18\n\napply to **sage** repository",
    "created_at": "2012-01-13T22:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95682",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9774-scripts-mathjax.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-scripts-mathjax.patch) by @jasongrout created at 2012-01-13 22:30:18

apply to **sage** repository



---

archive/issue_comments_095683.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-try3.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try3.patch) by @jasongrout created at 2012-01-13 22:42:12",
    "created_at": "2012-01-13T22:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95683",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9774-mathjax-try3.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try3.patch) by @jasongrout created at 2012-01-13 22:42:12



---

archive/issue_comments_095684.json:
```json
{
    "body": "I assume the description was incorrect, but even with the correction I made, [attachment:trac_9774-mathjax-try3.patch] does not apply cleanly on top of 4.8.alpha6. On 4.8.alpha4 (at least by `hg up 4.8.alpha4 && sage -b`) it fails a couple of doctests. Rebasing and fixing doctests now.",
    "created_at": "2012-01-14T11:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95684",
    "user": "https://github.com/kini"
}
```

I assume the description was incorrect, but even with the correction I made, [attachment:trac_9774-mathjax-try3.patch] does not apply cleanly on top of 4.8.alpha6. On 4.8.alpha4 (at least by `hg up 4.8.alpha4 && sage -b`) it fails a couple of doctests. Rebasing and fixing doctests now.



---

archive/issue_comments_095685.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-14T11:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95685",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095686.json:
```json
{
    "body": "Whoops, looks like \"a couple of doctests\" was an understatement. I guess it should be done in a separate patch. Here's the new patch, rebased only.",
    "created_at": "2012-01-14T11:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95686",
    "user": "https://github.com/kini"
}
```

Whoops, looks like "a couple of doctests" was an understatement. I guess it should be done in a separate patch. Here's the new patch, rebased only.



---

archive/issue_comments_095687.json:
```json
{
    "body": "apply to $SAGE_ROOT/devel/sage",
    "created_at": "2012-01-14T11:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95687",
    "user": "https://github.com/kini"
}
```

apply to $SAGE_ROOT/devel/sage



---

archive/issue_comments_095688.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-try4.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try4.patch) by @jasongrout created at 2012-01-14 14:42:49\n\nThe try3 patches were against alpha4.  Late last night I patched 5.0.beta1, and realized there were some patch failures, which I fixed.  I'll compare your rebase with mine.\n\nI also realized last night during dinner that I hadn't run doctests, so those should be run on sage and sagenb.  Thanks for checking this.",
    "created_at": "2012-01-14T14:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95688",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9774-mathjax-try4.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try4.patch) by @jasongrout created at 2012-01-14 14:42:49

The try3 patches were against alpha4.  Late last night I patched 5.0.beta1, and realized there were some patch failures, which I fixed.  I'll compare your rebase with mine.

I also realized last night during dinner that I hadn't run doctests, so those should be run on sage and sagenb.  Thanks for checking this.



---

archive/issue_comments_095689.json:
```json
{
    "body": "You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.\n\nIf you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.",
    "created_at": "2012-01-14T14:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95689",
    "user": "https://github.com/jasongrout"
}
```

You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.

If you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.



---

archive/issue_comments_095690.json:
```json
{
    "body": "I wonder if the reported problems with \"<\" and \">\" are due to line 1685 in latex.py:\n\n```\nx = x.replace('<', '&lt;').replace('>', '&gt;')\n```\n\nThis was put in for use with jsMath, but maybe MathJax doesn't have the same issues.",
    "created_at": "2012-01-14T18:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95690",
    "user": "https://github.com/jhpalmieri"
}
```

I wonder if the reported problems with "<" and ">" are due to line 1685 in latex.py:

```
x = x.replace('<', '&lt;').replace('>', '&gt;')
```

This was put in for use with jsMath, but maybe MathJax doesn't have the same issues.



---

archive/issue_comments_095691.json:
```json
{
    "body": "It was more complicated than that, but I've fixed it by getting rid of the math_parse function and conditional typesetting we were doing.  We've configured MathJax to make the math_parse function obsolete, and it's inconsistent to typeset only conditionally.  See https://github.com/jasongrout/sagenb/commit/6a4eed4d6baf78cd19fe634144c727843d1af08d and https://github.com/jasongrout/sagenb/commit/8d6b0a071c13850cea983faaa6b910be498cd0ae\n\n\n\nI've updated test.sagenb.org with the newest mathjax changes.",
    "created_at": "2012-01-14T18:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95691",
    "user": "https://github.com/jasongrout"
}
```

It was more complicated than that, but I've fixed it by getting rid of the math_parse function and conditional typesetting we were doing.  We've configured MathJax to make the math_parse function obsolete, and it's inconsistent to typeset only conditionally.  See https://github.com/jasongrout/sagenb/commit/6a4eed4d6baf78cd19fe634144c727843d1af08d and https://github.com/jasongrout/sagenb/commit/8d6b0a071c13850cea983faaa6b910be498cd0ae



I've updated test.sagenb.org with the newest mathjax changes.



---

archive/issue_comments_095692.json:
```json
{
    "body": "Replying to [comment:55 jason]:\n> You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.\n> \n> If you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.\n\nEr, no, I don't, unfortunately. You can get such a diff by doing `hg qfinish` on my patch on top of 4.8.alpha6, then `hg up 4.8.alpha4`, then `hg qimport -P [your patch]`, then `hg diff -r tip -r [revid of my patch]` (you would probably want to `hg strip [revid of my patch]` later).\n\nBut I don't see how that's very useful to you since it will be some gigantic patch subsuming everything that was merged in alpha5 and alpha6. In your position I would just diff the two patches, but maybe I don't understand what you're asking for. If you just want diffs for the files touched by the patch, that would also be possible, but maybe a bit messier. Do as above, except also qfinish your patch, and then merge the two qfinished patches' commits into a new commit, with your patch as the primary parent. Then do `hg log -r [the merge commit] -p [the file names]`. (I think that should work.) Or I guess you could just make the gigantic patch and ignore the parts that are on irrelevant files.",
    "created_at": "2012-01-15T07:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95692",
    "user": "https://github.com/kini"
}
```

Replying to [comment:55 jason]:
> You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.
> 
> If you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.

Er, no, I don't, unfortunately. You can get such a diff by doing `hg qfinish` on my patch on top of 4.8.alpha6, then `hg up 4.8.alpha4`, then `hg qimport -P [your patch]`, then `hg diff -r tip -r [revid of my patch]` (you would probably want to `hg strip [revid of my patch]` later).

But I don't see how that's very useful to you since it will be some gigantic patch subsuming everything that was merged in alpha5 and alpha6. In your position I would just diff the two patches, but maybe I don't understand what you're asking for. If you just want diffs for the files touched by the patch, that would also be possible, but maybe a bit messier. Do as above, except also qfinish your patch, and then merge the two qfinished patches' commits into a new commit, with your patch as the primary parent. Then do `hg log -r [the merge commit] -p [the file names]`. (I think that should work.) Or I guess you could just make the gigantic patch and ignore the parts that are on irrelevant files.



---

archive/issue_comments_095693.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-16T22:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95693",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095694.json:
```json
{
    "body": "kini: your try4 patch looks fine to me.  It applies cleanly on 5.0.some_version_of_prealpha1_or_beta1",
    "created_at": "2012-01-16T22:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95694",
    "user": "https://github.com/jasongrout"
}
```

kini: your try4 patch looks fine to me.  It applies cleanly on 5.0.some_version_of_prealpha1_or_beta1



---

archive/issue_comments_095695.json:
```json
{
    "body": "I seem to have a broken install here (2nd try). I followed this sequence of steps to install mathjax + jmol (output of `history` in zsh).\n\n```\n  663  local/bin\n  664  ../../sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/trac_9774-scripts-mathjax.patch\n  ***  ../../sage -hg qpush  # This line is missing because of my zsh setup\n  666  ../../\n  667  l\n  668  cd devel/sage\n  669  ../../sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/trac_9774-mathjax-try4.patch\n  670  ../../sage -hg qpush\n  671  ../../sage -b\n  672  ../..\n  674  ./sage -f http://sage.math.washington.edu/home/jason/mathjax/sagenb-0.9.0.spkg\n  675  ./sage -f http://sage.math.washington.edu/home/jason/jmol/jmol-12.0.45.p4.spkg\n  676  ./sage -b\n  678  ./sage -n\n  679  BROWSER=\"firefox\" ./sage -n\n```\n\nMathjax is broken and so is jmol. Do I need to install something extra for mathjax + jmol to work? These steps were followed on a freshly compiled sage-4.8. Screenshot: http://i.imgur.com/A6wrQ.png",
    "created_at": "2012-02-06T13:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95695",
    "user": "https://github.com/ppurka"
}
```

I seem to have a broken install here (2nd try). I followed this sequence of steps to install mathjax + jmol (output of `history` in zsh).

```
  663  local/bin
  664  ../../sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/trac_9774-scripts-mathjax.patch
  ***  ../../sage -hg qpush  # This line is missing because of my zsh setup
  666  ../../
  667  l
  668  cd devel/sage
  669  ../../sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9774/trac_9774-mathjax-try4.patch
  670  ../../sage -hg qpush
  671  ../../sage -b
  672  ../..
  674  ./sage -f http://sage.math.washington.edu/home/jason/mathjax/sagenb-0.9.0.spkg
  675  ./sage -f http://sage.math.washington.edu/home/jason/jmol/jmol-12.0.45.p4.spkg
  676  ./sage -b
  678  ./sage -n
  679  BROWSER="firefox" ./sage -n
```

Mathjax is broken and so is jmol. Do I need to install something extra for mathjax + jmol to work? These steps were followed on a freshly compiled sage-4.8. Screenshot: http://i.imgur.com/A6wrQ.png



---

archive/issue_comments_095696.json:
```json
{
    "body": "I only tested it on a 5.0 beta.  I see that #11080 isn't explicitly listed as a dependency (though it is mentioned in the description).\n\nSo please follow the directions on #11080 first (which involves a lot more patches).  My guess is that things won't apply cleanly to 4.8, and you'll need a 5.0 beta.",
    "created_at": "2012-02-06T13:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95696",
    "user": "https://github.com/jasongrout"
}
```

I only tested it on a 5.0 beta.  I see that #11080 isn't explicitly listed as a dependency (though it is mentioned in the description).

So please follow the directions on #11080 first (which involves a lot more patches).  My guess is that things won't apply cleanly to 4.8, and you'll need a 5.0 beta.



---

archive/issue_comments_095697.json:
```json
{
    "body": "And thanks for looking at this!  This ticket is also live at test.sagenb.org.",
    "created_at": "2012-02-06T13:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95697",
    "user": "https://github.com/jasongrout"
}
```

And thanks for looking at this!  This ticket is also live at test.sagenb.org.



---

archive/issue_comments_095698.json:
```json
{
    "body": "There seems to be some problem with mathjax rendering with `LatexExpr`. Compare the jsmath rendering here: http://sagenb.org/home/pub/4337/ to the mathjax here: http://test.sagenb.org/home/pub/19/",
    "created_at": "2012-02-19T15:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95698",
    "user": "https://github.com/ppurka"
}
```

There seems to be some problem with mathjax rendering with `LatexExpr`. Compare the jsmath rendering here: http://sagenb.org/home/pub/4337/ to the mathjax here: http://test.sagenb.org/home/pub/19/



---

archive/issue_comments_095699.json:
```json
{
    "body": "Some doctest failures with this patch:\n\n```\n...sage-5.0.beta2/devel/sage> ../../sage -t sage/misc/latex.py \nsage -t  \"devel/sage-main-backup/sage/misc/latex.py\"        \n**********************************************************************\nFile \"/home/punarbasu/Installations/sage-5.0.beta2/devel/sage-main-backup/sage/misc/latex.py\", line 1765:\n    sage: MathJax().eval(type(3), mode='inline')\nExpected:\n    <html><script type=\"math/tex\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\hbox{ < type 'sage.rings.integer.Integer' > }</script></html>\nGot:\n    <html><script type=\"math/tex\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\verb|&lt;type|\\phantom{\\verb!x!}\\verb|'sage.rings.integer.Integer'&gt;|</script></html>\n**********************************************************************\nFile \"/home/punarbasu/Installations/sage-5.0.beta2/devel/sage-main-backup/sage/misc/latex.py\", line 2199:\n    sage: sys.displayhook\nExpected:\n    <html>...\\verb|&lt;function|\\phantom{x}\\verb|pretty_print|...</html>\nGot:\n    <html><script type=\"math/tex\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\verb|&lt;function|\\phantom{\\verb!x!}\\verb|pretty_print|\\phantom{\\verb!x!}\\verb|at|\\phantom{\\verb!x!}\\verb|0x150b050&gt;|</script></html>\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_52\n   1 of   7 in __main__.example_59\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/punarbasu/.sage//tmp/latex_7938.py\n\t [3.1 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-main-backup/sage/misc/latex.py\"\nTotal time for all tests: 3.1 seconds\n```\n",
    "created_at": "2012-02-25T16:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95699",
    "user": "https://github.com/ppurka"
}
```

Some doctest failures with this patch:

```
...sage-5.0.beta2/devel/sage> ../../sage -t sage/misc/latex.py 
sage -t  "devel/sage-main-backup/sage/misc/latex.py"        
**********************************************************************
File "/home/punarbasu/Installations/sage-5.0.beta2/devel/sage-main-backup/sage/misc/latex.py", line 1765:
    sage: MathJax().eval(type(3), mode='inline')
Expected:
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}\hbox{ < type 'sage.rings.integer.Integer' > }</script></html>
Got:
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}\verb|&lt;type|\phantom{\verb!x!}\verb|'sage.rings.integer.Integer'&gt;|</script></html>
**********************************************************************
File "/home/punarbasu/Installations/sage-5.0.beta2/devel/sage-main-backup/sage/misc/latex.py", line 2199:
    sage: sys.displayhook
Expected:
    <html>...\verb|&lt;function|\phantom{x}\verb|pretty_print|...</html>
Got:
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}\verb|&lt;function|\phantom{\verb!x!}\verb|pretty_print|\phantom{\verb!x!}\verb|at|\phantom{\verb!x!}\verb|0x150b050&gt;|</script></html>
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_52
   1 of   7 in __main__.example_59
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/punarbasu/.sage//tmp/latex_7938.py
	 [3.1 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main-backup/sage/misc/latex.py"
Total time for all tests: 3.1 seconds
```




---

archive/issue_comments_095700.json:
```json
{
    "body": "Apply to devel/sage",
    "created_at": "2012-06-09T09:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95700",
    "user": "https://github.com/ppurka"
}
```

Apply to devel/sage



---

archive/issue_comments_095701.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-09T10:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95701",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095702.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-try5.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try5.patch) by @ppurka created at 2012-06-09 10:05:13\n\nrebased patch to sage-5.1beta2.\n\nThere is however a very weird problem with mathjax, both 1.0 and 2.0 branches. The math is not rendered as long as the sagenb directory is under `DOT_SAGE`. To reproduce, try the steps below. Use any branch (mathjax-1 or mathjax-2) for instance jasongrout/mathjax (mathjax-1) in github.\n1. `mkdir /tmp/a`\n2. `DOT_SAGE=/tmp/a sage -n`.\n3. First, note that the above command launches the nb in port 8000 instead of 8080. But if we use some other command such as the one below, then it does open in port 8080.\n\n```\nsage -n directory=/tmp/a.sagenb\n```\n\n4. Open a new worksheet, and try to print latex, for instance run the command `view('?')`. You will get a js error popup saying (in Opera 12.00RC, and Opera-11.64)\n\n```\nSyntaxError: at index 0 in \"\\newcommand{\\Bold}[1]{\\mathbf{#1}}?\": invalid character escape sequence\n```\n\n\nIn firefox-10.0.4 I simply get the error: `SyntaxError: illegal character`. This error is not present if I run sage instead as `sage -n directory=/tmp/a.sagenb`, and the mathjax output is all good.",
    "created_at": "2012-06-09T10:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95702",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_9774-mathjax-try5.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try5.patch) by @ppurka created at 2012-06-09 10:05:13

rebased patch to sage-5.1beta2.

There is however a very weird problem with mathjax, both 1.0 and 2.0 branches. The math is not rendered as long as the sagenb directory is under `DOT_SAGE`. To reproduce, try the steps below. Use any branch (mathjax-1 or mathjax-2) for instance jasongrout/mathjax (mathjax-1) in github.
1. `mkdir /tmp/a`
2. `DOT_SAGE=/tmp/a sage -n`.
3. First, note that the above command launches the nb in port 8000 instead of 8080. But if we use some other command such as the one below, then it does open in port 8080.

```
sage -n directory=/tmp/a.sagenb
```

4. Open a new worksheet, and try to print latex, for instance run the command `view('?')`. You will get a js error popup saying (in Opera 12.00RC, and Opera-11.64)

```
SyntaxError: at index 0 in "\newcommand{\Bold}[1]{\mathbf{#1}}?": invalid character escape sequence
```


In firefox-10.0.4 I simply get the error: `SyntaxError: illegal character`. This error is not present if I run sage instead as `sage -n directory=/tmp/a.sagenb`, and the mathjax output is all good.



---

archive/issue_comments_095703.json:
```json
{
    "body": "It looks like Samuel Ainsworth has independently got MathJax working in his \"newui\" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.",
    "created_at": "2012-06-09T17:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95703",
    "user": "https://github.com/kini"
}
```

It looks like Samuel Ainsworth has independently got MathJax working in his "newui" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.



---

archive/issue_comments_095704.json:
```json
{
    "body": "Replying to [comment:67 kini]:\n> It looks like Samuel Ainsworth has independently got MathJax working in his \"newui\" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.\n\nHas he applied the mathjax patches to the sage repo? Without those patches it won't work. And these patches were not applying for quite sometime. I just updated one today.\n\nThere are more changes to make actually. `SAGE_ROOT/devel/sage/doc` has lots of jsmath references, which all need to be converted to mathjax.\n\nIf you can independently confirm the behavior in comment:65 then it will be good.",
    "created_at": "2012-06-09T19:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95704",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:67 kini]:
> It looks like Samuel Ainsworth has independently got MathJax working in his "newui" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.

Has he applied the mathjax patches to the sage repo? Without those patches it won't work. And these patches were not applying for quite sometime. I just updated one today.

There are more changes to make actually. `SAGE_ROOT/devel/sage/doc` has lots of jsmath references, which all need to be converted to mathjax.

If you can independently confirm the behavior in comment:65 then it will be good.



---

archive/issue_comments_095705.json:
```json
{
    "body": "Regarding [comment:65 your comment]: the spkg in the ticket description is quite old, and that was probably the problem. The notebook has now been upgraded to use MathJax, and it does not have the problem you described.",
    "created_at": "2012-06-12T19:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95705",
    "user": "https://github.com/jhpalmieri"
}
```

Regarding [comment:65 your comment]: the spkg in the ticket description is quite old, and that was probably the problem. The notebook has now been upgraded to use MathJax, and it does not have the problem you described.



---

archive/issue_comments_095706.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-12T19:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95706",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_095707.json:
```json
{
    "body": "Fantastic news!\n\nThis was merged in the notebook at [this github pull request](https://github.com/sagemath/sagenb/pull/30), just for completeness.\n\nSince #11080 is for Sage 5.2, this should be too.",
    "created_at": "2012-06-12T20:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95707",
    "user": "https://github.com/kcrisman"
}
```

Fantastic news!

This was merged in the notebook at [this github pull request](https://github.com/sagemath/sagenb/pull/30), just for completeness.

Since #11080 is for Sage 5.2, this should be too.



---

archive/issue_events_024503.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-12T20:28:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24503"
}
```



---

archive/issue_events_024504.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-12T20:28:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24504"
}
```



---

archive/issue_comments_095708.json:
```json
{
    "body": "Just checking on this - Jason, will this indeed fix #1608?  That is, will we be shipping (the relevant) MathJax fonts?  From what I'm reading above, that seems to be the case.  Anyone who confirms this, please give positive review to #1608 and add your name as a reviewer.",
    "created_at": "2012-06-12T20:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95708",
    "user": "https://github.com/kcrisman"
}
```

Just checking on this - Jason, will this indeed fix #1608?  That is, will we be shipping (the relevant) MathJax fonts?  From what I'm reading above, that seems to be the case.  Anyone who confirms this, please give positive review to #1608 and add your name as a reviewer.



---

archive/issue_comments_095709.json:
```json
{
    "body": "We have doctest failures:\n\n```\n        sage -t  --long -force_lib devel/sagenb-main/sagenb/notebook/jsmath.py # 5 doctests failed\n        sage -t  --long -force_lib devel/sagenb-main/sagenb/misc/sphinxify.py # 1 doctests failed\n        sage -t  --long -force_lib devel/sage/doc/de/tutorial/latex.rst # 27 doctests failed\n        sage -t  --long -force_lib devel/sage/doc/en/tutorial/latex.rst # 27 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/matrix/matrix0.pyx # 1 doctests failed\n```\n\nThe problem with sphinxify is easy to fix. Should we delete jsmath.py, or is it still needed for something?\n\nThe problems with the tutorial are a bit more involved, since (a) it explicitly discusses using JSMath and (b) I don't speak German.\n\nI don't understand the matrix0.pyx problem at all, at least not yet.",
    "created_at": "2012-06-12T23:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95709",
    "user": "https://github.com/jhpalmieri"
}
```

We have doctest failures:

```
        sage -t  --long -force_lib devel/sagenb-main/sagenb/notebook/jsmath.py # 5 doctests failed
        sage -t  --long -force_lib devel/sagenb-main/sagenb/misc/sphinxify.py # 1 doctests failed
        sage -t  --long -force_lib devel/sage/doc/de/tutorial/latex.rst # 27 doctests failed
        sage -t  --long -force_lib devel/sage/doc/en/tutorial/latex.rst # 27 doctests failed
        sage -t  --long -force_lib devel/sage/sage/matrix/matrix0.pyx # 1 doctests failed
```

The problem with sphinxify is easy to fix. Should we delete jsmath.py, or is it still needed for something?

The problems with the tutorial are a bit more involved, since (a) it explicitly discusses using JSMath and (b) I don't speak German.

I don't understand the matrix0.pyx problem at all, at least not yet.



---

archive/issue_comments_095710.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-12T23:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95710",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095711.json:
```json
{
    "body": "> The problems with the tutorial are a bit more involved, since (a) it explicitly discusses using JSMath and (b) I don't speak German.\nThere are a number of Sage folks who do, though, so hopefully the second one won't be a problem.  Once you fix the English one let us know. \n\nI wonder why the other tutorial versions don't cause problems?  In particular, there is a tutorial in Russian and one in French in 5.1.beta3 that you don't mention as having caused problems - maybe they're based on different versions of the English tutorial.",
    "created_at": "2012-06-12T23:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95711",
    "user": "https://github.com/kcrisman"
}
```

> The problems with the tutorial are a bit more involved, since (a) it explicitly discusses using JSMath and (b) I don't speak German.
There are a number of Sage folks who do, though, so hopefully the second one won't be a problem.  Once you fix the English one let us know. 

I wonder why the other tutorial versions don't cause problems?  In particular, there is a tutorial in Russian and one in French in 5.1.beta3 that you don't mention as having caused problems - maybe they're based on different versions of the English tutorial.



---

archive/issue_comments_095712.json:
```json
{
    "body": "Attachment [trac_9774-doctests.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-doctests.patch) by @jhpalmieri created at 2012-06-13 05:50:25",
    "created_at": "2012-06-13T05:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95712",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9774-doctests.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-doctests.patch) by @jhpalmieri created at 2012-06-13 05:50:25



---

archive/issue_comments_095713.json:
```json
{
    "body": "Here is a patch fixing the doctests in the Sage library. For the English tutorial, I did a little bit more than a search-and-replace, changing \"JSMath\" to \"MathJax\". For the German tutorial, that's essentially all I did. \n\nsagenb also needs fixing, and I don't have the energy to do this right now. If someone else wants to, that would be great. Here's what I think should be done: delete notebook/jsmath.py, and patch misc/sphinxify.py:\n\n```diff\ndiff --git a/sagenb/misc/sphinxify.py b/sagenb/misc/sphinxify.py\nindex 837b40a..85c9f4d 100644\n--- a/sagenb/misc/sphinxify.py\n+++ b/sagenb/misc/sphinxify.py\n@@ -71,7 +71,7 @@ def sphinxify(docstring, format='html'):\n         sage: sphinxify('**Testing**\\n`monospace`')\n         '\\n<div class=\"docstring\"...<strong>Testing</strong>\\n<span class=\"math\"...</p>\\n\\n\\n</div\n         sage: sphinxify('`x=y`')\n-        '\\n<div class=\"docstring\">\\n    \\n  <p><span class=\"math\">x=y</span></p>\\n\\n\\n</div>'\n+        '\\n<div class=\"docstring\">\\n    \\n  <p><span class=\"math\">\\\\(x=y\\\\)</span></p>\\n\\n\\n</div>\n         sage: sphinxify('`x=y`', format='text')\n         'x=y\\n'\n         sage: sphinxify(':math:`x=y`', format='text')\n```\n",
    "created_at": "2012-06-13T05:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95713",
    "user": "https://github.com/jhpalmieri"
}
```

Here is a patch fixing the doctests in the Sage library. For the English tutorial, I did a little bit more than a search-and-replace, changing "JSMath" to "MathJax". For the German tutorial, that's essentially all I did. 

sagenb also needs fixing, and I don't have the energy to do this right now. If someone else wants to, that would be great. Here's what I think should be done: delete notebook/jsmath.py, and patch misc/sphinxify.py:

```diff
diff --git a/sagenb/misc/sphinxify.py b/sagenb/misc/sphinxify.py
index 837b40a..85c9f4d 100644
--- a/sagenb/misc/sphinxify.py
+++ b/sagenb/misc/sphinxify.py
@@ -71,7 +71,7 @@ def sphinxify(docstring, format='html'):
         sage: sphinxify('**Testing**\n`monospace`')
         '\n<div class="docstring"...<strong>Testing</strong>\n<span class="math"...</p>\n\n\n</div
         sage: sphinxify('`x=y`')
-        '\n<div class="docstring">\n    \n  <p><span class="math">x=y</span></p>\n\n\n</div>'
+        '\n<div class="docstring">\n    \n  <p><span class="math">\\(x=y\\)</span></p>\n\n\n</div>
         sage: sphinxify('`x=y`', format='text')
         'x=y\n'
         sage: sphinxify(':math:`x=y`', format='text')
```




---

archive/issue_comments_095714.json:
```json
{
    "body": "Regarding the change in matrix0.py: the main patch already modified that file, and this doctest was missed. (jsMath can't handle the command `\\hline`, so matrices with subdivisions had to be handled specially in the notebook. MathJax handles this command just fine, so the special-casing went away, so the extra doctest for the notebook needed to go away, too.)",
    "created_at": "2012-06-13T05:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95714",
    "user": "https://github.com/jhpalmieri"
}
```

Regarding the change in matrix0.py: the main patch already modified that file, and this doctest was missed. (jsMath can't handle the command `\hline`, so matrices with subdivisions had to be handled specially in the notebook. MathJax handles this command just fine, so the special-casing went away, so the extra doctest for the notebook needed to go away, too.)



---

archive/issue_comments_095715.json:
```json
{
    "body": "test.sagenb.org and alpha.sagenb.org are running these patches up through try5 (but not the doctest patch just posted).",
    "created_at": "2012-06-13T06:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95715",
    "user": "https://github.com/jasongrout"
}
```

test.sagenb.org and alpha.sagenb.org are running these patches up through try5 (but not the doctest patch just posted).



---

archive/issue_comments_095716.json:
```json
{
    "body": "Regarding my comment about sagenb: apparently jsmath.py is already gone in the new sagenb; I don't know why I thought otherwise. sphinxify.py still needs to be patched.",
    "created_at": "2012-06-13T17:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95716",
    "user": "https://github.com/jhpalmieri"
}
```

Regarding my comment about sagenb: apparently jsmath.py is already gone in the new sagenb; I don't know why I thought otherwise. sphinxify.py still needs to be patched.



---

archive/issue_comments_095717.json:
```json
{
    "body": "> Here is a patch fixing the doctests in the Sage library. For the English tutorial, I did a little bit more than a search-and-replace, changing \"JSMath\" to \"MathJax\". For the German tutorial, that's essentially all I did. \n\nThat looks to have been enough.  I have no idea if all the stuff in English is actually *true* any more, of course.  As long as\n\n```\nIn the \ncase of Sage, the notebook is always connected to a server used to \nexecute the Sage commands, and this server also provides the necessary \njsMath fonts.  So there is nothing extra to set up to have typeset \nmathematics in your web browser when you use the Sage notebook.\n```\n\nis still true for MathJax you should be fine.",
    "created_at": "2012-06-13T18:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95717",
    "user": "https://github.com/kcrisman"
}
```

> Here is a patch fixing the doctests in the Sage library. For the English tutorial, I did a little bit more than a search-and-replace, changing "JSMath" to "MathJax". For the German tutorial, that's essentially all I did. 

That looks to have been enough.  I have no idea if all the stuff in English is actually *true* any more, of course.  As long as

```
In the 
case of Sage, the notebook is always connected to a server used to 
execute the Sage commands, and this server also provides the necessary 
jsMath fonts.  So there is nothing extra to set up to have typeset 
mathematics in your web browser when you use the Sage notebook.
```

is still true for MathJax you should be fine.



---

archive/issue_comments_095718.json:
```json
{
    "body": "I just [submitted a pull request](https://github.com/sagemath/sagenb/pull/60) for the sphinxify change in sagenb. So I think this is ready for review. The only thing that needs review is the doctest patch, which just fixes doctests. I'm running doctests now.",
    "created_at": "2012-06-13T18:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95718",
    "user": "https://github.com/jhpalmieri"
}
```

I just [submitted a pull request](https://github.com/sagemath/sagenb/pull/60) for the sphinxify change in sagenb. So I think this is ready for review. The only thing that needs review is the doctest patch, which just fixes doctests. I'm running doctests now.



---

archive/issue_comments_095719.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-13T18:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95719",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095720.json:
```json
{
    "body": "All tests pass with the new patches.",
    "created_at": "2012-06-13T20:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95720",
    "user": "https://github.com/jhpalmieri"
}
```

All tests pass with the new patches.



---

archive/issue_comments_095721.json:
```json
{
    "body": "Replying to [comment:80 kcrisman]:\n> As long as\n> {{{\n> In the \n> case of Sage, the notebook is always connected to a server used to \n> execute the Sage commands, and this server also provides the necessary \n> jsMath fonts.  So there is nothing extra to set up to have typeset \n> mathematics in your web browser when you use the Sage notebook.\n> }}}\n> is still true for MathJax you should be fine.\n\nAs far as I can tell, it still is. If it's not, it's close enough.",
    "created_at": "2012-06-13T22:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95721",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:80 kcrisman]:
> As long as
> {{{
> In the 
> case of Sage, the notebook is always connected to a server used to 
> execute the Sage commands, and this server also provides the necessary 
> jsMath fonts.  So there is nothing extra to set up to have typeset 
> mathematics in your web browser when you use the Sage notebook.
> }}}
> is still true for MathJax you should be fine.

As far as I can tell, it still is. If it's not, it's close enough.



---

archive/issue_comments_095722.json:
```json
{
    "body": "I see that after this mathjax-1.1 is merged into sagenb. Shouldn't we move to mathjax-2 directly?",
    "created_at": "2012-06-14T03:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95722",
    "user": "https://github.com/ppurka"
}
```

I see that after this mathjax-1.1 is merged into sagenb. Shouldn't we move to mathjax-2 directly?



---

archive/issue_comments_095723.json:
```json
{
    "body": "MathJax 2.0 should be a separate patch.  Let's not delay this year-in-the-making positively-reviewed patch any longer.",
    "created_at": "2012-06-14T04:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95723",
    "user": "https://github.com/jasongrout"
}
```

MathJax 2.0 should be a separate patch.  Let's not delay this year-in-the-making positively-reviewed patch any longer.



---

archive/issue_comments_095724.json:
```json
{
    "body": "Once my `make ptestlong` finishes, I'm just going to give this positive review. The pull request has already been merged into sagenb (and so everyone will need to apply these patches anyway if they want to test the latest revision of the notebook), the patch looks good to me (though I don't know much about the code it touches), and from some poking around it seems to work as advertised.",
    "created_at": "2012-06-14T22:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95724",
    "user": "https://github.com/kini"
}
```

Once my `make ptestlong` finishes, I'm just going to give this positive review. The pull request has already been merged into sagenb (and so everyone will need to apply these patches anyway if they want to test the latest revision of the notebook), the patch looks good to me (though I don't know much about the code it touches), and from some poking around it seems to work as advertised.



---

archive/issue_comments_095725.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-15T00:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95725",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095726.json:
```json
{
    "body": "All systems go!",
    "created_at": "2012-06-15T00:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95726",
    "user": "https://github.com/kini"
}
```

All systems go!



---

archive/issue_comments_095727.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd41\".",
    "created_at": "2012-06-15T00:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95727",
    "user": "https://github.com/kini"
}
```

Changing keywords from "" to "sd41".



---

archive/issue_comments_095728.json:
```json
{
    "body": "This obviously needs a proper sagenb spkg before it can be merged.",
    "created_at": "2012-06-15T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95728",
    "user": "https://github.com/jdemeyer"
}
```

This obviously needs a proper sagenb spkg before it can be merged.



---

archive/issue_comments_095729.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-15T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95729",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095730.json:
```json
{
    "body": "Important note: if the sagenb people can write me a script which *automatically* creates a new sagenb spkg from a git repository, I'll be happy to use it.",
    "created_at": "2012-06-15T21:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95730",
    "user": "https://github.com/jdemeyer"
}
```

Important note: if the sagenb people can write me a script which *automatically* creates a new sagenb spkg from a git repository, I'll be happy to use it.



---

archive/issue_comments_095731.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-15T21:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95731",
    "user": "https://github.com/kini"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_095732.json:
```json
{
    "body": "No, we'll (I'll) do it manually. SPKGs being autogenerated is at odds with having repositories for SPKGs.\n\nI have written scripts which at least simplify the process, though - they create a directory which can be used as the new SPKG's `src/` directory without modification of the `spkg-install` script. Those are at [this pull request](https://github.com/sagemath/sagenb/pull/63), which I'd appreciate it if someone reviewed :)\n\nI'm setting this ticket to positive review because there is nothing left to be done on the Sage end other than wait for #13121 to get in (i.e. Sage to upgrade to sagenb 0.9.1).",
    "created_at": "2012-06-15T21:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95732",
    "user": "https://github.com/kini"
}
```

No, we'll (I'll) do it manually. SPKGs being autogenerated is at odds with having repositories for SPKGs.

I have written scripts which at least simplify the process, though - they create a directory which can be used as the new SPKG's `src/` directory without modification of the `spkg-install` script. Those are at [this pull request](https://github.com/sagemath/sagenb/pull/63), which I'd appreciate it if someone reviewed :)

I'm setting this ticket to positive review because there is nothing left to be done on the Sage end other than wait for #13121 to get in (i.e. Sage to upgrade to sagenb 0.9.1).



---

archive/issue_events_024505.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-18T22:12:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24505"
}
```



---

archive/issue_events_024506.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-18T22:12:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24506"
}
```



---

archive/issue_comments_095733.json:
```json
{
    "body": "Rebased to Sage 5.1.beta5 (because of #11775).",
    "created_at": "2012-06-20T19:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95733",
    "user": "https://github.com/jhpalmieri"
}
```

Rebased to Sage 5.1.beta5 (because of #11775).



---

archive/issue_comments_095734.json:
```json
{
    "body": "Sage library",
    "created_at": "2012-06-25T16:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95734",
    "user": "https://github.com/jasongrout"
}
```

Sage library



---

archive/issue_comments_095735.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-try6.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try6.patch) by @jasongrout created at 2012-06-25 16:54:32\n\nI rebased [attachment:trac_9774-mathjax-try6.patch] to sage 5.1beta6",
    "created_at": "2012-06-25T16:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95735",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9774-mathjax-try6.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try6.patch) by @jasongrout created at 2012-06-25 16:54:32

I rebased [attachment:trac_9774-mathjax-try6.patch] to sage 5.1beta6



---

archive/issue_comments_095736.json:
```json
{
    "body": "Dumb question.  If the changes to the latex of some vectors is to work around a jsmath bug, maybe we shouldn't remove that comment; after all, maybe that workaround is no longer needed, but now no one will no that it was a workaround in the first place...  Maybe it works now completely, and we should change it or remove it!\n\nThis was apparently introduced in the try3 patch.",
    "created_at": "2012-07-05T16:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95736",
    "user": "https://github.com/kcrisman"
}
```

Dumb question.  If the changes to the latex of some vectors is to work around a jsmath bug, maybe we shouldn't remove that comment; after all, maybe that workaround is no longer needed, but now no one will no that it was a workaround in the first place...  Maybe it works now completely, and we should change it or remove it!

This was apparently introduced in the try3 patch.



---

archive/issue_comments_095737.json:
```json
{
    "body": "Can you tell which part is \"weird\"? Is it the braces around ``\\mapsto``? If I remove those braces, it works with both jsMath and MathJax.",
    "created_at": "2012-07-05T16:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95737",
    "user": "https://github.com/jhpalmieri"
}
```

Can you tell which part is "weird"? Is it the braces around ``\mapsto``? If I remove those braces, it works with both jsMath and MathJax.



---

archive/issue_comments_095738.json:
```json
{
    "body": "> Can you tell which part is \"weird\"? Is it the braces around ``\\mapsto``? If I remove those braces, it works with both jsMath and MathJax.\nI wish I could tell you!  I didn't write it.  I was just trying to point this out, in case it was clear to someone else.  If it's not clear what the problem is, maybe we leave the comment in?  Maybe Jason can explain.\n\nAlso, both representations have the braces, and braces are fine for demarcating things in TeX, so I don't think that's the issue.  hg blame says that this dates from before the symbolics switch to Pynac.\n\nAnyway, not a huge deal, but pointing it out.",
    "created_at": "2012-07-05T17:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95738",
    "user": "https://github.com/kcrisman"
}
```

> Can you tell which part is "weird"? Is it the braces around ``\mapsto``? If I remove those braces, it works with both jsMath and MathJax.
I wish I could tell you!  I didn't write it.  I was just trying to point this out, in case it was clear to someone else.  If it's not clear what the problem is, maybe we leave the comment in?  Maybe Jason can explain.

Also, both representations have the braces, and braces are fine for demarcating things in TeX, so I don't think that's the issue.  hg blame says that this dates from before the symbolics switch to Pynac.

Anyway, not a huge deal, but pointing it out.



---

archive/issue_comments_095739.json:
```json
{
    "body": "Updated patch to the changes introduced in #11775. Otherwise, typeset was broken.",
    "created_at": "2012-07-14T00:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95739",
    "user": "https://github.com/ppurka"
}
```

Updated patch to the changes introduced in #11775. Otherwise, typeset was broken.



---

archive/issue_comments_095740.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-07-26T09:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95740",
    "user": "https://github.com/kini"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095741.json:
```json
{
    "body": "Patch needs rebasing on #13109 - doing that now.",
    "created_at": "2012-07-26T09:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95741",
    "user": "https://github.com/kini"
}
```

Patch needs rebasing on #13109 - doing that now.



---

archive/issue_comments_095742.json:
```json
{
    "body": "Hmm. There is a failing doctest caused by #11775. Did you attempt to fix doctests when you made try7, ppurka? Or is this failing doctest somehow new or caused by my rebasing? Looking at a diff between the try7 patch and my new try8 patch, I don't see anything suspicious...",
    "created_at": "2012-07-26T10:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95742",
    "user": "https://github.com/kini"
}
```

Hmm. There is a failing doctest caused by #11775. Did you attempt to fix doctests when you made try7, ppurka? Or is this failing doctest somehow new or caused by my rebasing? Looking at a diff between the try7 patch and my new try8 patch, I don't see anything suspicious...



---

archive/issue_comments_095743.json:
```json
{
    "body": "In particular this doctest fails, on Sage 5.2.rc1: \n\n\n```\n[3] fs@boone /opt/sage/devel/sage $ sage -t --long --force_lib sage/misc/latex.py\nsage -t --long --force_lib \"devel/sage-main/sage/misc/latex.py\"\n**********************************************************************\nFile \"/opt/sage-5.2.rc1/devel/sage-main/sage/misc/latex.py\", line 1972:\n    sage: view((x,2), combine_all=True) # trac 11775\nExpected:\n    <html><script type=\"math/tex\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}\\left(x, 2\\right)</script></html>\nGot:\n    <html><script type=\"math/tex\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}x 2</script></html>\n**********************************************************************\n1 items had failures:\n   1 of  17 in __main__.example_54\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/fs/.sage//tmp/latex_17232.py\n         [1.3 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t --long --force_lib \"devel/sage-main/sage/misc/latex.py\"\nTotal time for all tests: 1.3 seconds\n```\n",
    "created_at": "2012-07-26T11:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95743",
    "user": "https://github.com/kini"
}
```

In particular this doctest fails, on Sage 5.2.rc1: 


```
[3] fs@boone /opt/sage/devel/sage $ sage -t --long --force_lib sage/misc/latex.py
sage -t --long --force_lib "devel/sage-main/sage/misc/latex.py"
**********************************************************************
File "/opt/sage-5.2.rc1/devel/sage-main/sage/misc/latex.py", line 1972:
    sage: view((x,2), combine_all=True) # trac 11775
Expected:
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}\left(x, 2\right)</script></html>
Got:
    <html><script type="math/tex">\newcommand{\Bold}[1]{\mathbf{#1}}x 2</script></html>
**********************************************************************
1 items had failures:
   1 of  17 in __main__.example_54
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/fs/.sage//tmp/latex_17232.py
         [1.3 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t --long --force_lib "devel/sage-main/sage/misc/latex.py"
Total time for all tests: 1.3 seconds
```




---

archive/issue_comments_095744.json:
```json
{
    "body": "Hmm.. I had updated to try7 exactly because it was failing the doctests and in the notebook. I thought I had fixed all the doctests. Updating try7 again  soon.",
    "created_at": "2012-07-26T15:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95744",
    "user": "https://github.com/ppurka"
}
```

Hmm.. I had updated to try7 exactly because it was failing the doctests and in the notebook. I thought I had fixed all the doctests. Updating try7 again  soon.



---

archive/issue_comments_095745.json:
```json
{
    "body": "Updated try7. Please test.",
    "created_at": "2012-07-26T16:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95745",
    "user": "https://github.com/ppurka"
}
```

Updated try7. Please test.



---

archive/issue_comments_095746.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-26T16:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95746",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095747.json:
```json
{
    "body": "updated the try7 patch again, to changes in #13109. To make the review easier, the diff between this and earlier patch [is here](https://github.com/ppurka/sage-patches/commit/f1253cc6d3f5d0051e5192d17678425b3029e879).",
    "created_at": "2012-08-03T10:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95747",
    "user": "https://github.com/ppurka"
}
```

updated the try7 patch again, to changes in #13109. To make the review easier, the diff between this and earlier patch [is here](https://github.com/ppurka/sage-patches/commit/f1253cc6d3f5d0051e5192d17678425b3029e879).



---

archive/issue_comments_095748.json:
```json
{
    "body": "The patch has fuzz against 5.3.beta2.",
    "created_at": "2012-08-22T06:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95748",
    "user": "https://github.com/kini"
}
```

The patch has fuzz against 5.3.beta2.



---

archive/issue_comments_095749.json:
```json
{
    "body": "The fuzz is caused by #13310 which was merged in 5.3.beta1 and is harmless.",
    "created_at": "2012-08-22T07:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95749",
    "user": "https://github.com/kini"
}
```

The fuzz is caused by #13310 which was merged in 5.3.beta1 and is harmless.



---

archive/issue_comments_095750.json:
```json
{
    "body": "Fixed.",
    "created_at": "2012-08-22T07:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95750",
    "user": "https://github.com/kini"
}
```

Fixed.



---

archive/issue_comments_095751.json:
```json
{
    "body": "Attachment [trac_9774-mathjax-try7.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try7.patch) by @kini created at 2012-08-22 07:02:28\n\napply to $SAGE_ROOT/devel/sage",
    "created_at": "2012-08-22T07:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95751",
    "user": "https://github.com/kini"
}
```

Attachment [trac_9774-mathjax-try7.patch](tarball://root/attachments/some-uuid/ticket9774/trac_9774-mathjax-try7.patch) by @kini created at 2012-08-22 07:02:28

apply to $SAGE_ROOT/devel/sage



---

archive/issue_comments_095752.json:
```json
{
    "body": "What thing needs \"review\" here?",
    "created_at": "2012-08-22T07:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95752",
    "user": "https://github.com/ppurka"
}
```

What thing needs "review" here?



---

archive/issue_comments_095753.json:
```json
{
    "body": "Uh... hmm. The rebasing, I guess? Whatever, looks fine to me ;)",
    "created_at": "2012-08-22T07:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95753",
    "user": "https://github.com/kini"
}
```

Uh... hmm. The rebasing, I guess? Whatever, looks fine to me ;)



---

archive/issue_comments_095754.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-22T07:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95754",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024507.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-02T21:43:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24507"
}
```



---

archive/issue_events_024508.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-02T21:43:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "milestone": "sage-5.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24508"
}
```



---

archive/issue_comments_095755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-05T18:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95755",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_024509.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-05T18:05:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9773#event-24509"
}
```



---

archive/issue_comments_095756.json:
```json
{
    "body": "This document does not compile anymore with SageTeX\n\n```\n\\documentclass[12pt,letterpaper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[english]{babel}\n\\usepackage{sagetex}\n\\begin{document}\n$\\sage{\"1 2\"}$\n\\end{document}\n```\n\nbecause someone has replaced a verbatim spacer with a version that does not work, as was explicitly explained in the surrounding comment, and then deleted the comment altogether:\n\n```diff\n--- a/sage/misc/latex.py\n+++ b/sage/misc/latex.py\n@@ -323,11 +323,7 @@\n     # 2) wrap each line into \\verb;\n     # 3) assemble lines into a left-justified array.\n     \n-    # There is a bug in verb-space treatment in jsMath...\n-    spacer = \"\\\\phantom{%s}\"\n-    # \\phantom{\\verb!%s!} is more accurate and it works, but it is not a valid\n-    # LaTeX and may cause problems, so let's live with the above variant until\n-    # spaces are properly treated in jsMath/MathJax and we don't need to worry.\n+    spacer = r\"\\phantom{\\verb!%s!}\"\n     lines = []\n     for line in x.split(\"\\n\"):\n         parts = []\n```\n\nWhat was the motivation for this???",
    "created_at": "2012-09-19T16:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95756",
    "user": "https://github.com/novoselt"
}
```

This document does not compile anymore with SageTeX

```
\documentclass[12pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{sagetex}
\begin{document}
$\sage{"1 2"}$
\end{document}
```

because someone has replaced a verbatim spacer with a version that does not work, as was explicitly explained in the surrounding comment, and then deleted the comment altogether:

```diff
--- a/sage/misc/latex.py
+++ b/sage/misc/latex.py
@@ -323,11 +323,7 @@
     # 2) wrap each line into \verb;
     # 3) assemble lines into a left-justified array.
     
-    # There is a bug in verb-space treatment in jsMath...
-    spacer = "\\phantom{%s}"
-    # \phantom{\verb!%s!} is more accurate and it works, but it is not a valid
-    # LaTeX and may cause problems, so let's live with the above variant until
-    # spaces are properly treated in jsMath/MathJax and we don't need to worry.
+    spacer = r"\phantom{\verb!%s!}"
     lines = []
     for line in x.split("\n"):
         parts = []
```

What was the motivation for this???



---

archive/issue_comments_095757.json:
```json
{
    "body": "Do you by chance see who changed it?  If it was me, I don't recall the motivation.  So +1 to making sure things work.",
    "created_at": "2012-09-19T16:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95757",
    "user": "https://github.com/jasongrout"
}
```

Do you by chance see who changed it?  If it was me, I don't recall the motivation.  So +1 to making sure things work.



---

archive/issue_comments_095758.json:
```json
{
    "body": "It is in the jumbo patch to Sage library uploaded by Keshav, I guess it is a flattening of others. Most of it was automatic, I imagine, but this part is definitely made by hand.",
    "created_at": "2012-09-19T16:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95758",
    "user": "https://github.com/novoselt"
}
```

It is in the jumbo patch to Sage library uploaded by Keshav, I guess it is a flattening of others. Most of it was automatic, I imagine, but this part is definitely made by hand.



---

archive/issue_comments_095759.json:
```json
{
    "body": "Another reason why we shouldn't flatten patches...",
    "created_at": "2012-09-20T13:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95759",
    "user": "https://github.com/kini"
}
```

Another reason why we shouldn't flatten patches...



---

archive/issue_comments_095760.json:
```json
{
    "body": "#14382 finally reverts the change, sorry for delay.",
    "created_at": "2013-03-29T17:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9773#issuecomment-95760",
    "user": "https://github.com/novoselt"
}
```

#14382 finally reverts the change, sorry for delay.
