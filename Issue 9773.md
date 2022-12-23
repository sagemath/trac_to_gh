# Issue 9773: Upgrade the notebook to use MathJax instead of jsMath

Issue created by migration from https://trac.sagemath.org/ticket/9774

Original creator: mpatel

Original creation time: 2010-08-21 09:36:05

Assignee: jason, was

CC:  rbeezer robert.marik jhpalmieri rkirov kcrisman kini

[MathJax](http://www.mathjax.org/) is the successor to [jsMath](http://www.math.union.edu/~dpvc/jsMath/).


---

Comment by rbeezer created at 2010-08-24 18:52:40

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

Comment by robert.marik created at 2010-08-24 19:57:06

Thanks for comment, I feel that MathJax is much slower on cheap/older computer. This could be an important issue for using Sage in highschools and universities. Is it possible to keep both MathJax and jsMath and let the notebook admin to choose, which one will be used?


---

Comment by jason created at 2010-08-25 22:34:11

Replying to [comment:2 rbeezer]:

> 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.


I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.


---

Comment by jason created at 2010-10-15 01:50:18

Changing status from new to needs_work.


---

Comment by rminer created at 2010-10-21 20:21:34

Replying to [comment:4 jason]:
> Replying to [comment:2 rbeezer]:
> 
> > 6.  `MathJax` is HUGE.  Fonts for lots of Unicode points, I guess.  SVN checkout is 53 MB, after unzipping  fonts.zip  it all occupies  171 MB.
> 
> 
> I think MathJax includes the equivalent of our jsmath-image-fonts spkg.  If we added MathJax to Sage, it might be good to strip out the image fonts and distribute them separately as a mathjax-image-fonts spkg (mathjax faq tells how to do this, I believe).  Somewhere I have a half-finished prototype of this solution.

Just in case you haven't thought of this, what Gollum (the [GitHub](GitHub) forum) folks did was host the MathJax fonts on Amazon S3, and then not include them in their distribution.  I don't know if that would work for you, but I wanted to point it out.


---

Comment by jason created at 2010-10-21 20:44:55

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

Comment by jhpalmieri created at 2010-11-10 22:11:11

I just found the web page [http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home](http://bitbucket.org/kevindunn/sphinx-extension-mathjax/wiki/Home), which allows the use of Sphinx with MathJax.  Assuming it works, we could upgrade all of Sage (not just the notebook but also the docs), to use MathJax instead of jsMath.


---

Comment by drkirkby created at 2011-03-02 20:26:53

[MathJax](http://www.mathjax.org/) is very impressive looking. I like the idea the user does not have to have any fonts installed on his computer, which is a major advantage over [jsMath](http://www.math.union.edu/~dpvc/jsMath/)

Dave


---

Comment by rbeezer created at 2011-03-22 22:49:12

Screenshot of double integral


---

Attachment

Screenshot of matrix


---

Comment by rbeezer created at 2011-03-22 22:53:38

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

Comment by jhpalmieri created at 2011-06-14 22:04:56

I'm attaching a draft of a patch for the Sage library.  The integration with Sphinx is completely untested, and is probably broken.  See the top of the patch file for a list of things to do.


---

Attachment


---

Comment by rbeezer created at 2011-06-16 03:35:12

Added patch to Flask notebook code to support `MathJax`, built with Davide Cervone's help.

  1.  This is a hand-edited patch to recover from an hg mess-up.  I think it is OK, but be wary.
  1.  Fonts are coming from `MathJax` CDN.  Comment in code indicates change for local `MathJax` installation.
  1.  `<script>` tags added by Palmieri's Sage library patch need to be handled with care on notebook side, so notebook does not evaluate them.  Right now when "Typeset" box is checked, evaluated cells raise a Javascript error in `evaluate_script_tags` (or a function with a similar name).


---

Comment by jason created at 2011-06-16 04:15:42

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

Comment by rbeezer created at 2011-06-16 05:18:07

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

Comment by jason created at 2011-06-16 05:29:12

Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?


---

Attachment


---

Comment by rbeezer created at 2011-06-16 05:33:20

Attached a patch to add `sagenb/notebook/mathjax.py`

New file is similar to, but not identical to, `sagenb/notebook/jsmath.py`

We did not delete the latter, but I think it can safely go away.


---

Comment by rbeezer created at 2011-06-16 05:35:52

Replying to [comment:20 jason]:
> Don't we need the actual MathJax spkg or files somewhere?  Rob: do you have instructions for putting these in the directory, or do we use my half-finished patch mentioned in the description, or something else?

We need an spkg to be Internet-independent.  

We did not experiment with your old one.  I think it would be best to make a new one.  This requires a small edit (once you are sure all works with CDN version).

Font suggestions coming up.


---

Comment by rbeezer created at 2011-06-16 05:45:04

Davide Cervone says for an spkg we need only keep font subdirectories called


```
otf,  eot,  svg
```


In particular `png` subdirectories are huge-est and can go away.

Rob


---

Comment by jason created at 2011-06-16 05:50:21

ah; I bet it's because the svg fonts replace the png fonts for all browsers we care about, or something.  Okay, Davide is the final authority on what browsers support what...


---

Comment by jason created at 2011-06-16 06:01:09

I get an error from the line: `response = make_response(render_template('js/mathjax.js', theme_mathjax_macros=mathjax_macros))` in flask_version/base.py.  I see a jsmath.js template in `sagenb/data/sage/js/jsmath.js` template.  Is this another file that didn't get added to the patch?


---

Attachment


---

Comment by rbeezer created at 2011-06-16 06:35:33

Replying to [comment:25 jason]:
> Is this another file that didn't get added to the patch?

Yes, same situation - "old" file could be removed.

"file-add-two" should create the missing file.  Sorry about all the problems - my `hg status` is useless with the hg mess-up.

This file will require an edit when we move from CDN to spkg.

Thank-you!!!!!!!!!!!!!!


---

Comment by jason created at 2011-06-16 09:07:31

I have a working version, but there still seems to be something slightly different about Typeset mode compared to before. I'm posting my patch, but there is still *lots* of debugging stuff in the patch that should be taken out before a final version is posted.


---

Comment by jason created at 2011-06-16 09:08:09

apply to sagenb repository; apply on top of previous patches


---

Attachment

The problem with the Sage notebook code intercepting (and evaluating) the contents of `<script>,</script>` tags can probably be rectified in one, or both, of the functions of the Flask notebook:


```
In sagenb/data/sage/js/notebook_lib.js:

eval_script_tags
separate_script_tags
```



---

Comment by jason created at 2011-06-17 19:38:39

rbeezer: yes, that's what my patch does.  The current remaining problem is something different.


---

Comment by jhpalmieri created at 2011-06-20 18:55:07

In the current version of [attachment:mathjax.patch], look at the top of the file for some unfinished business.  For example, the pathname at the end of doc/common/themes/sage/static/mathjax_sage.js_t might be wrong, which might break MathJax in the Sphinx documentation.


---

Comment by rbeezer created at 2011-06-20 19:23:20

In the current state, the --mathjax  switch seems to work with a build of the html version of the reference manual.

Mathematics in the documentation is being wrapped with `\(, \)` pairs, which are the default MathJax delimiters for inline mathematics.  However these snippets are not being rendered when viewed in a browser.

In the page source of a page of the html documentation, I see a script in a file named `mathjax_sage.js` which we are not generating.  We do have `jsmath_sage.js` lying about in the doc directories, which have the full jsmath configuration information.  So this likely needs repair before an HTML documentation page with MathJax support is built properly.


---

Comment by rbeezer created at 2011-06-20 21:29:18

OK, I can force `mathjax_sage.js` to be created by totally trashing some of the documentation output with


```
devel/sage/doc/output/html$ rm -rf en
```


before rebuilding the HTML reference documentation. It comes from a template file `mathjax_sage.js_t` that one of the patches creates properly.

Mathematics still does not render, but I think the MathJax configuration is looking locally.  Time for a local MathJax install, I think.


---

Comment by rbeezer created at 2011-06-20 23:50:31

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

Comment by rbeezer created at 2011-06-21 00:04:09

Replying to [comment:33 rbeezer]:
> Then I installed the mathjax 1.1a distribution alongside jsmath in the Flask notebook tree and 

> which also caused the math to render properly.  (/sage/notebook is my `SAGE_ROOT`)

Oops, the incantation for a local install of MathJax should have been


```
<script type="text/javascript" src="/sage/notebook/devel/rkirov-flask/sagenb/data/mathjax/MathJax.js?config=TeX-AMS_HTML-full"></script>
```



---

Comment by jhpalmieri created at 2011-07-01 02:07:22

Here's a new version of my patch.  With a locally installed version of MathJax, the documentation seems to render properly.  I don't know if this is the best solution, but at least it seems to work.

(I installed MathJax by downloading a zip file: [https://github.com/mathjax/MathJax/zipball/v1.1a](https://github.com/mathjax/MathJax/zipball/v1.1a).  I unzipped it and renamed the resulting directory to `mathjax`, and moved it to `SAGE_ROOT/local/lib/python/site-packages/sagenb-0.9.0-py2.6.egg/sagenb/data/`, alongside of the old `jsmath` directory.  I also put a copy of the `mathjax` directory in `SAGE_ROOT/devel/sagenb/sagenb/data/`.  I haven't tried to install local fonts.)


---

Attachment

(experimental) patch for Sage library


---

Comment by jhpalmieri created at 2011-07-01 03:59:03

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

Comment by rbeezer created at 2011-07-01 04:50:48

Hi John,

Are you testing with the Flask notebook?  If not, it might be easier to build what look like absolute paths to the MathJax files in the data directory of the notebook, because of the way Flask sets up paths with the "route()" command?  I can't tell if this will solve the problem you are wrestling with or not.

The `<script>` tags were being messed with by the notebook on the server side just before being dispatched.  But then the client sees two versions - wrapped and unwrapped, and totally trashes one of them to prevent running a script twice.  I thought Jason had a patch for this too, but I haven't seen it.  The symptom would be when you cycle through wrap, no-wrap, and hide for some output, then one of them is missing.  I guess we can press on and fix this eventually.

About to go off-line shortly for the long weekend, but will come back to this when I can stick with it.

Rob


---

Comment by jhpalmieri created at 2011-07-01 05:17:39

For building the documentation, the notebook isn't relevant: they get built from the command line.  I think that when trying to make MathJax work with the notebook, we'll want to construct the URLs differently than I'm doing for the docs, but I don't know enough about the paths, etc., in the notebook to say exactly how to do it.  For what it's worth, though, I have been using the flask notebook.


---

Comment by jason created at 2011-07-01 06:07:01

I've uploaded my current flask patch queue here: http://sage.math.washington.edu/home/jason/mathjax-flask-patches.tar.gz  My current (probably non-working) patch queue for my sage library, including two mathjax patches, is here: 
http://sage.math.washington.edu/home/jason/mathjax-sage-patches.tar.gz

These are both works-in-progress, but currently stalled for at least a week or two.


---

Comment by jason created at 2011-07-01 06:08:33

I stalled working on it because of other time pressures with the single-cell, but also because I realized that the *next* version of Sphinx supports Mathjax out of the box, while I thought the current version would require patches.


---

Comment by jhpalmieri created at 2011-07-01 06:12:05

I think that the implementation of MathJax in Sphinx comes from the file mathjax.py, which is available for download separately.  So my patch just adds it.

I'm attaching another version ("v2") of my patch; this one writes the MathJax local configuration file to a file in `SAGE_ROOT/local/lib/python/site-libraries/sagenb.../`, which may not be a good idea.  But it allows for a simpler invocation of MathJax.  I'm really not sure which approach is better.


---

Attachment

(experimental) patch for Sage library, alternate version


---

Comment by jason created at 2012-01-09 20:13:14

What is the current status on this now?  Where should we start working on it again?


---

Comment by rkirov created at 2012-01-10 03:43:41

The last patch involving MathJax, that I rebased from the ones here is on google code:

http://code.google.com/p/sagenb/issues/detail?id=46

Unless Jonathan Gutow did something else on top of it, this is latest work.


---

Comment by jason created at 2012-01-11 06:50:56

Rebased version of comprehensive mathjax patch to 4.8.alpha4


---

Attachment

Apply only this patch


---

Comment by jason created at 2012-01-13 21:49:29

Changing status from needs_work to needs_review.


---

Comment by jason created at 2012-01-13 22:29:25

apply to *scripts* repository


---

Attachment

apply to *sage* repository


---

Attachment


---

Comment by kini created at 2012-01-14 11:28:18

I assume the description was incorrect, but even with the correction I made, [attachment:trac_9774-mathjax-try3.patch] does not apply cleanly on top of 4.8.alpha6. On 4.8.alpha4 (at least by `hg up 4.8.alpha4 && sage -b`) it fails a couple of doctests. Rebasing and fixing doctests now.


---

Comment by kini created at 2012-01-14 11:28:18

Changing status from needs_review to needs_work.


---

Comment by kini created at 2012-01-14 11:58:15

Whoops, looks like "a couple of doctests" was an understatement. I guess it should be done in a separate patch. Here's the new patch, rebased only.


---

Comment by kini created at 2012-01-14 11:59:15

apply to $SAGE_ROOT/devel/sage


---

Attachment

The try3 patches were against alpha4.  Late last night I patched 5.0.beta1, and realized there were some patch failures, which I fixed.  I'll compare your rebase with mine.

I also realized last night during dinner that I hadn't run doctests, so those should be run on sage and sagenb.  Thanks for checking this.


---

Comment by jason created at 2012-01-14 14:44:11

You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.

If you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.


---

Comment by jhpalmieri created at 2012-01-14 18:11:07

I wonder if the reported problems with "<" and ">" are due to line 1685 in latex.py:

```
x = x.replace('<', '&lt;').replace('>', '&gt;')
```

This was put in for use with jsMath, but maybe MathJax doesn't have the same issues.


---

Comment by jason created at 2012-01-14 18:15:51

It was more complicated than that, but I've fixed it by getting rid of the math_parse function and conditional typesetting we were doing.  We've configured MathJax to make the math_parse function obsolete, and it's inconsistent to typeset only conditionally.  See https://github.com/jasongrout/sagenb/commit/6a4eed4d6baf78cd19fe634144c727843d1af08d and https://github.com/jasongrout/sagenb/commit/8d6b0a071c13850cea983faaa6b910be498cd0ae



I've updated test.sagenb.org with the newest mathjax changes.


---

Comment by kini created at 2012-01-15 07:03:12

Replying to [comment:55 jason]:
> You don't happen to have your changes as a separate patch on top of mine, do you?  I'd love to review your changes, but it's a bit hard to see where your additions are.
> 
> If you don't have it, I'll just diff the two patches, but that's a little harder to read than a separate patch.

Er, no, I don't, unfortunately. You can get such a diff by doing `hg qfinish` on my patch on top of 4.8.alpha6, then `hg up 4.8.alpha4`, then `hg qimport -P [your patch]`, then `hg diff -r tip -r [revid of my patch]` (you would probably want to `hg strip [revid of my patch]` later).

But I don't see how that's very useful to you since it will be some gigantic patch subsuming everything that was merged in alpha5 and alpha6. In your position I would just diff the two patches, but maybe I don't understand what you're asking for. If you just want diffs for the files touched by the patch, that would also be possible, but maybe a bit messier. Do as above, except also qfinish your patch, and then merge the two qfinished patches' commits into a new commit, with your patch as the primary parent. Then do `hg log -r [the merge commit] -p [the file names]`. (I think that should work.) Or I guess you could just make the gigantic patch and ignore the parts that are on irrelevant files.


---

Comment by jason created at 2012-01-16 22:07:40

Changing status from needs_work to needs_review.


---

Comment by jason created at 2012-01-16 22:07:40

kini: your try4 patch looks fine to me.  It applies cleanly on 5.0.some_version_of_prealpha1_or_beta1


---

Comment by ppurka created at 2012-02-06 13:32:57

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

Comment by jason created at 2012-02-06 13:39:51

I only tested it on a 5.0 beta.  I see that #11080 isn't explicitly listed as a dependency (though it is mentioned in the description).

So please follow the directions on #11080 first (which involves a lot more patches).  My guess is that things won't apply cleanly to 4.8, and you'll need a 5.0 beta.


---

Comment by jason created at 2012-02-06 13:40:39

And thanks for looking at this!  This ticket is also live at test.sagenb.org.


---

Comment by ppurka created at 2012-02-19 15:38:23

There seems to be some problem with mathjax rendering with `LatexExpr`. Compare the jsmath rendering here: http://sagenb.org/home/pub/4337/ to the mathjax here: http://test.sagenb.org/home/pub/19/


---

Comment by ppurka created at 2012-02-25 16:56:50

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

Comment by ppurka created at 2012-06-09 09:49:11

Apply to devel/sage


---

Comment by ppurka created at 2012-06-09 10:05:13

Changing status from needs_review to needs_work.


---

Attachment

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

Comment by kini created at 2012-06-09 17:26:34

It looks like Samuel Ainsworth has independently got MathJax working in his "newui" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.


---

Comment by ppurka created at 2012-06-09 19:40:36

Replying to [comment:67 kini]:
> It looks like Samuel Ainsworth has independently got MathJax working in his "newui" branch (I haven't tested it). At a glance it seems he's using the MathJax CDN.

Has he applied the mathjax patches to the sage repo? Without those patches it won't work. And these patches were not applying for quite sometime. I just updated one today.

There are more changes to make actually. `SAGE_ROOT/devel/sage/doc` has lots of jsmath references, which all need to be converted to mathjax.

If you can independently confirm the behavior in comment:65 then it will be good.


---

Comment by jhpalmieri created at 2012-06-12 19:43:51

Regarding [comment:65 your comment]: the spkg in the ticket description is quite old, and that was probably the problem. The notebook has now been upgraded to use MathJax, and it does not have the problem you described.


---

Comment by jhpalmieri created at 2012-06-12 19:43:51

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2012-06-12 20:28:40

Fantastic news!

This was merged in the notebook at [this github pull request](https://github.com/sagemath/sagenb/pull/30), just for completeness.

Since #11080 is for Sage 5.2, this should be too.


---

Comment by kcrisman created at 2012-06-12 20:38:19

Just checking on this - Jason, will this indeed fix #1608?  That is, will we be shipping (the relevant) MathJax fonts?  From what I'm reading above, that seems to be the case.  Anyone who confirms this, please give positive review to #1608 and add your name as a reviewer.


---

Comment by jhpalmieri created at 2012-06-12 23:35:59

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

Comment by jhpalmieri created at 2012-06-12 23:35:59

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2012-06-12 23:55:13

> The problems with the tutorial are a bit more involved, since (a) it explicitly discusses using JSMath and (b) I don't speak German.
There are a number of Sage folks who do, though, so hopefully the second one won't be a problem.  Once you fix the English one let us know. 

I wonder why the other tutorial versions don't cause problems?  In particular, there is a tutorial in Russian and one in French in 5.1.beta3 that you don't mention as having caused problems - maybe they're based on different versions of the English tutorial.


---

Attachment


---

Comment by jhpalmieri created at 2012-06-13 05:54:47

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

Comment by jhpalmieri created at 2012-06-13 05:58:14

Regarding the change in matrix0.py: the main patch already modified that file, and this doctest was missed. (jsMath can't handle the command `\hline`, so matrices with subdivisions had to be handled specially in the notebook. MathJax handles this command just fine, so the special-casing went away, so the extra doctest for the notebook needed to go away, too.)


---

Comment by jason created at 2012-06-13 06:53:34

test.sagenb.org and alpha.sagenb.org are running these patches up through try5 (but not the doctest patch just posted).


---

Comment by jhpalmieri created at 2012-06-13 17:44:01

Regarding my comment about sagenb: apparently jsmath.py is already gone in the new sagenb; I don't know why I thought otherwise. sphinxify.py still needs to be patched.


---

Comment by kcrisman created at 2012-06-13 18:29:40

> Here is a patch fixing the doctests in the Sage library. For the English tutorial, I did a little bit more than a search-and-replace, changing "JSMath" to "MathJax". For the German tutorial, that's essentially all I did. 

That looks to have been enough.  I have no idea if all the stuff in English is actually _true_ any more, of course.  As long as

```
In the 
case of Sage, the notebook is always connected to a server used to 
execute the Sage commands, and this server also provides the necessary 
jsMath fonts.  So there is nothing extra to set up to have typeset 
mathematics in your web browser when you use the Sage notebook.
```

is still true for MathJax you should be fine.


---

Comment by jhpalmieri created at 2012-06-13 18:46:15

I just [submitted a pull request](https://github.com/sagemath/sagenb/pull/60) for the sphinxify change in sagenb. So I think this is ready for review. The only thing that needs review is the doctest patch, which just fixes doctests. I'm running doctests now.


---

Comment by jhpalmieri created at 2012-06-13 18:46:15

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-06-13 20:11:07

All tests pass with the new patches.


---

Comment by jhpalmieri created at 2012-06-13 22:14:04

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

Comment by ppurka created at 2012-06-14 03:59:10

I see that after this mathjax-1.1 is merged into sagenb. Shouldn't we move to mathjax-2 directly?


---

Comment by jason created at 2012-06-14 04:59:13

MathJax 2.0 should be a separate patch.  Let's not delay this year-in-the-making positively-reviewed patch any longer.


---

Comment by kini created at 2012-06-14 22:59:03

Once my `make ptestlong` finishes, I'm just going to give this positive review. The pull request has already been merged into sagenb (and so everyone will need to apply these patches anyway if they want to test the latest revision of the notebook), the patch looks good to me (though I don't know much about the code it touches), and from some poking around it seems to work as advertised.


---

Comment by kini created at 2012-06-15 00:22:53

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-06-15 00:22:53

All systems go!


---

Comment by kini created at 2012-06-15 00:29:59

Changing keywords from "" to "sd41".


---

Comment by jdemeyer created at 2012-06-15 21:03:29

This obviously needs a proper sagenb spkg before it can be merged.


---

Comment by jdemeyer created at 2012-06-15 21:03:29

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-06-15 21:05:28

Important note: if the sagenb people can write me a script which _automatically_ creates a new sagenb spkg from a git repository, I'll be happy to use it.


---

Comment by kini created at 2012-06-15 21:54:42

Changing status from needs_work to positive_review.


---

Comment by kini created at 2012-06-15 21:54:42

No, we'll (I'll) do it manually. SPKGs being autogenerated is at odds with having repositories for SPKGs.

I have written scripts which at least simplify the process, though - they create a directory which can be used as the new SPKG's `src/` directory without modification of the `spkg-install` script. Those are at [this pull request](https://github.com/sagemath/sagenb/pull/63), which I'd appreciate it if someone reviewed :)

I'm setting this ticket to positive review because there is nothing left to be done on the Sage end other than wait for #13121 to get in (i.e. Sage to upgrade to sagenb 0.9.1).


---

Comment by jhpalmieri created at 2012-06-20 19:07:54

Rebased to Sage 5.1.beta5 (because of #11775).


---

Comment by jason created at 2012-06-25 16:54:06

Sage library


---

Attachment

I rebased [attachment:trac_9774-mathjax-try6.patch] to sage 5.1beta6


---

Comment by kcrisman created at 2012-07-05 16:28:19

Dumb question.  If the changes to the latex of some vectors is to work around a jsmath bug, maybe we shouldn't remove that comment; after all, maybe that workaround is no longer needed, but now no one will no that it was a workaround in the first place...  Maybe it works now completely, and we should change it or remove it!

This was apparently introduced in the try3 patch.


---

Comment by jhpalmieri created at 2012-07-05 16:40:47

Can you tell which part is "weird"? Is it the braces around ``\mapsto``? If I remove those braces, it works with both jsMath and MathJax.


---

Comment by kcrisman created at 2012-07-05 17:45:39

> Can you tell which part is "weird"? Is it the braces around ``\mapsto``? If I remove those braces, it works with both jsMath and MathJax.
I wish I could tell you!  I didn't write it.  I was just trying to point this out, in case it was clear to someone else.  If it's not clear what the problem is, maybe we leave the comment in?  Maybe Jason can explain.

Also, both representations have the braces, and braces are fine for demarcating things in TeX, so I don't think that's the issue.  hg blame says that this dates from before the symbolics switch to Pynac.

Anyway, not a huge deal, but pointing it out.


---

Comment by ppurka created at 2012-07-14 00:58:15

Updated patch to the changes introduced in #11775. Otherwise, typeset was broken.


---

Comment by kini created at 2012-07-26 09:08:04

Changing status from positive_review to needs_work.


---

Comment by kini created at 2012-07-26 09:08:04

Patch needs rebasing on #13109 - doing that now.


---

Comment by kini created at 2012-07-26 10:28:13

Hmm. There is a failing doctest caused by #11775. Did you attempt to fix doctests when you made try7, ppurka? Or is this failing doctest somehow new or caused by my rebasing? Looking at a diff between the try7 patch and my new try8 patch, I don't see anything suspicious...


---

Comment by kini created at 2012-07-26 11:01:00

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

Comment by ppurka created at 2012-07-26 15:47:42

Hmm.. I had updated to try7 exactly because it was failing the doctests and in the notebook. I thought I had fixed all the doctests. Updating try7 again  soon.


---

Comment by ppurka created at 2012-07-26 16:21:25

Updated try7. Please test.


---

Comment by ppurka created at 2012-07-26 16:21:25

Changing status from needs_work to needs_review.


---

Comment by ppurka created at 2012-08-03 10:07:13

updated the try7 patch again, to changes in #13109. To make the review easier, the diff between this and earlier patch [is here](https://github.com/ppurka/sage-patches/commit/f1253cc6d3f5d0051e5192d17678425b3029e879).


---

Comment by kini created at 2012-08-22 06:55:32

The patch has fuzz against 5.3.beta2.


---

Comment by kini created at 2012-08-22 07:00:33

The fuzz is caused by #13310 which was merged in 5.3.beta1 and is harmless.


---

Comment by kini created at 2012-08-22 07:01:55

Fixed.


---

Attachment

apply to $SAGE_ROOT/devel/sage


---

Comment by ppurka created at 2012-08-22 07:07:32

What thing needs "review" here?


---

Comment by kini created at 2012-08-22 07:18:37

Uh... hmm. The rebasing, I guess? Whatever, looks fine to me ;)


---

Comment by kini created at 2012-08-22 07:18:37

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-05 18:05:17

Resolution: fixed


---

Comment by novoselt created at 2012-09-19 16:14:01

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

Comment by jason created at 2012-09-19 16:22:17

Do you by chance see who changed it?  If it was me, I don't recall the motivation.  So +1 to making sure things work.


---

Comment by novoselt created at 2012-09-19 16:31:32

It is in the jumbo patch to Sage library uploaded by Keshav, I guess it is a flattening of others. Most of it was automatic, I imagine, but this part is definitely made by hand.


---

Comment by kini created at 2012-09-20 13:40:56

Another reason why we shouldn't flatten patches...


---

Comment by novoselt created at 2013-03-29 17:31:31

#14382 finally reverts the change, sorry for delay.
