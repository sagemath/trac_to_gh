# Issue 8105: LaTex to Sage worksheet conversion system

Issue created by migration from https://trac.sagemath.org/ticket/8105

Original creator: rbeezer

Original creation time: 2010-01-28 04:55:08

Assignee: tbd

CC:  jason ddrake jhpalmieri robert.marik kcrisman

This is an experimental process for converting Latex documents into Sage worksheets.

Attached archive contains code, configuration files, templates and hints to begin using the system.  See README.txt to get started.

Over time, this should get easier through automation of some of the tasks, and more general with cross-worksheet linking.


---

Attachment

Code like the following, added to the Python script, will automate the cut/paste final step, producing a Sage worksheet as the final output.  (Ignore the line outputting W's cells.)

Note that the `.edit_save()` method needs a title as the first line of the string, and this clobbers the title given in the initialization.


```
sage: nb = sage.server.notebook.notebook.Notebook("/tmp")
sage: W = nb.create_new_worksheet('A Weird Worksheet', 'admin')
sage: W.edit_save('Weirder Title\n`2+3\n///\n5\n`')
sage: W
[Cell 0; in=2+3, out=
5]
sage: nb.export_worksheet(W.filename(), "/tmp/weird.sws", verbose=False)
sage: nb.delete()
```



---

Comment by ddrake created at 2010-01-28 09:00:11

This is nice! It worked on the example file.

Now you should put that stuff into Mercurial and put it up on bitbucket.org so Jason and I can hack on it and send you patches. :)

I am guessing that you'd like this to eventually be an optional spkg, which might let the user do something like

```
sage -tex2sws foo.tex
```

which would spit out a proper .sws file. Sound right?


---

Attachment

The notebook code above works for the *old* notebook.  But I've added the right code for the *new* notebook and have the script creating an sws file as output.

So there are now just two inputs to the script (see the README), and one less manual step, but at the small cost that you now need Sage in your path.  Though one could install the new notebook locally and have the script run as pure Python rather than within Sage.

There's now a Mercurial repo in the archive, and I'll work on a bitbucket site soon.


---

Comment by rbeezer created at 2010-01-30 07:20:23

Dan,

Thanks for the testing!  Yes, some sort of optional package that allows for a simple one-step conversion should be the eventual goal.  Next step will be to hack up something that will allow for cross-worksheet links to work and try to convert something book-length.

Can you tell me what you used for the tex4ht routines?  Custom install, or something provided by a distribution?  Either answer will be interesting.  Thanks.

Rob

Replying to [comment:2 ddrake]:
> This is nice! It worked on the example file.
> 
> Now you should put that stuff into Mercurial and put it up on bitbucket.org so Jason and I can hack on it and send you patches. :)
> 
> I am guessing that you'd like this to eventually be an optional spkg, which might let the user do something like
> {{{
> sage -tex2sws foo.tex
> }}}
> which would spit out a proper .sws file. Sound right?


---

Comment by ddrake created at 2010-01-30 14:54:53

Replying to [comment:4 rbeezer]:
> Can you tell me what you used for the tex4ht routines?  Custom install, or something provided by a distribution?  Either answer will be interesting.  Thanks.

I have TeXLive 2009 installed, separately from the Ubuntu package manager. TeXLive includes its own little package manager ("tlmgr") and I used that to install tex4ht -- I just searched for it, and hit "install".


---

Comment by rbeezer created at 2010-01-31 01:05:09

Changing assignee from tbd to rbeezer.


---

Comment by rbeezer created at 2010-01-31 01:05:09

I've built a wiki page with some examples and I'll put code up at bitbucket soon.

The third example on the wiki page shows some odd behavior if anybody is interested in current roadblocks.

http://wiki.sagemath.org/devel/LatexToWorksheet


---

Comment by robert.marik created at 2010-01-31 23:02:57

Nice idea, thanks.

The oposite sws -> LaTeX conversion can be done with [sws2tex](http://bitbucket.org/whuss/sws2tex/), see [example](http://user.mendelu.cz/marik/sage/skolka.pdf).


---

Attachment


---

Comment by rbeezer created at 2010-02-01 05:10:47

Hi Robert,

Thanks for the reminder, I'd forgotten about that.  I added these links to the wiki page I have going.

Rob

Replying to [comment:9 robert.marik]:
> The oposite sws -> LaTeX conversion can be done with [sws2tex](http://bitbucket.org/whuss/sws2tex/), see [example](http://user.mendelu.cz/marik/sage/skolka.pdf).


---

Comment by rbeezer created at 2010-02-01 05:18:22

I've got graphics written in tikz being converted to SVG by tex4ht and then the custom conversion script puts them in the data directory of the worksheet.  However, while the worksheet *looks* good, the Javascript (or something) is not working and the code cells will not evaluate (even though this works in other examples).  But progress nonetheless.


---

Comment by robert.marik created at 2010-02-01 14:10:23

the version which does not replace \infty etc. by unicode characters


---

Attachment

I looked briefly at the converter. Two ideas: 

* \infty and other characters are replaced by unicode characters. I fixed this few years before using \HCode command, see the attached tex4ht-sage.cfg file. Another solution has been suggested by [Eitan Gurari](http://groups.google.cz/group/comp.text.tex/browse_thread/thread/221b01a29dc59745/f16d44bca4d0f20a). I remember that when I worked on my [materials](http://user.mendelu.cz/marik/mat-web/mat-web.html) (sorry for Czech language), I had to fix also align and similar enviroments. You can see my [jsmath config file](http://user.mendelu.cz/marik/latex/marik-jsmath.4ht)

* $\lim_{x\to\infty}$ hangs the compilation. Commenting out \usepackage{syntax} and two following lines solves the problem - but breaks other things, of course :)


---

Comment by robert.marik created at 2010-02-01 15:18:51

Replying to [comment:12 robert.marik]:
> * $\lim_{x\to\infty}$ hangs the compilation. Commenting out \usepackage{syntax} and two following lines solves the problem - but breaks other things, of course :)

this second problem seems to be limited to older installations of TeX, texlive2009 works fine.


---

Attachment


---

Comment by rbeezer created at 2010-02-04 05:29:39

Begin with latex source that includes tikz graphics, use the tools here, and the graphics become SVG files that are included in the data directory of the worksheet.  My problems with this earlier were due to a stray newline in the title.  See the wiki page for the working example and source.


---

Comment by rbeezer created at 2010-02-04 05:41:03

Replying to [comment:13 robert.marik]:
> this second problem seems to be limited to older installations of TeX, texlive2009 works fine.

Hi Robert,

Thanks for testing this out.  I've been basically using tex4ht from source, for the reasons you mentioned above.

My current example uses some tkz-graph code, which builds on the tikz package.

tex4ht complains about some of this code (which I do not think is a surprise since I have no reason to believe tex4ht has any extra support for tkz-graph)


```
l.197 --- TeX4ht warning --- missing \Configure{HColor}{col_lab_a11}{...} (in LaTeX: rgb 0 0 0) --- 
```


this is tkz-graph code to color a vertex label (I think).  I get garbage in the CSS file produced by tex4ht, but everything seems to work - but the labels are absent from the SVG graphics meant for the worksheet.

Do you have lots of experience configuring tex4ht?  It seems a bit of a black art to me sometimes.

Rob


---

Comment by rbeezer created at 2010-02-07 23:30:11

I've updated this considerably over the weekend.  Wiki page now contains my entire linear algebra book as a tar archive of linked worksheets.  There are instructions for creating a scratch notebook and inserting these worksheets into this notebook.

The bitbucket repository is updated, the README.txt is updated and the calling command has changed.  This is now reasonably stable for converting to a single worksheet as an sws file.  Multiple worksheets is still experimental since there is no notebook support.

I'm going to stop posting snapshots here on the assumption that folks can clone and pull from the bitbucket repo - correct me if that is wrong.

I'll probably get a general announcement out later today, and ship Robert an example of the tkz-graph code.

Any testing would be appreciated.  Thanks for everybody's interest.

Rob


---

Attachment

tkz-graph example unrecognized by tex4ht


---

Comment by rbeezer created at 2010-02-08 03:16:04

Robert,

I've posted on the ticket a small example of a combinatorial graph that htlatex complains about, though it does produce a legitimate HTML file and an SVG graphic, though lacking vertex labels.  The calling command is in a comment in the file.  You'll see three complaints, one per vertex, then repeated on each of the three passes.

If you flip the "worksheet" switch it should produce a good PDF version.

Learning how to configure tex4ht to handle this sort of thing would be real helpful.  Thanks for offering to look at this.

Rob


---

Comment by robert.marik created at 2010-02-09 18:53:04

Rob, 

I sent you the answer to your email. In short: disable 

```
\SetVertexNoLabel
```

For example, adding something like 

```
\let\SetVertexNoLabel\relax
```

near the end of preamble helps. 

Adding the same to the config file for tex4ht should help as well (config fie not tested).

I wonder, if it is possible to check Typeset button and execute all cells in worksheet before saving into sws file.


---

Comment by robert.marik created at 2010-02-10 10:32:41

Concerning Typeset button and my previous message:

```
W.set_pretty_print('true')
```

probably [does](http://www.sagemath.org/doc/reference/sagenb/notebook/worksheet.html#sagenb.notebook.worksheet.Worksheet.set_pretty_print) the magic.

I asked about evaluating all cells in sagenb [forum](http://groups.google.cz/group/sage-notebook/browse_thread/thread/649c845f39a0a528#)


---

Comment by robert.marik created at 2010-02-17 22:41:08

New [tex4ht-sage.cfg](http://user.mendelu.cz/marik/sage/tex4ht-sage.cfg) file

With this file the input is the same as for SageTeX. See
[example.tex](http://user.mendelu.cz/marik/sage/example.tex) (from SageTeX distribution, fixed only some whitespaces), [PDF](http://user.mendelu.cz/marik/sage/example.pdf) produced by pdflatex and [sws](http://user.mendelu.cz/marik/sage/example.sws) produced by 

```
latex -interaction=nonstopmode example
sage example.sage
htlatex example.tex "tex4ht-sage.cfg"
./tex2sws.py
```

You get input fileds from commands like \sage{},  \sagestr{}, \sageplot{}. You get also dolars as delimiters for inline math.


---

Comment by robert.marik created at 2010-02-20 21:35:23

Using the attached file jsmath-noexpand.4ht and adding \input{jsmath-noexpand.4ht} to tex4ht-sage.cfg prevents TeX4ht to replace expressions like \int or \alpha by unicode characters and functions like \cos remain intact and are not replaced by \mathop{cos}. 

All this gives better rendering in the browser.


---

Attachment


---

Comment by rbeezer created at 2010-02-20 21:58:32

Replying to [comment:21 robert.marik]:
> Using the attached file jsmath-noexpand.4ht and adding \input{jsmath-noexpand.4ht} to tex4ht-sage.cfg prevents TeX4ht to replace expressions like \int or \alpha by unicode characters and functions like \cos remain intact and are not replaced by \mathop{cos}. 
> 
> All this gives better rendering in the browser.

Thanks, Robert.  that sounds great.  I'll try to get it incorporated later today.  I'm close to having something stable put together for others to test, and which I'll use to add a few more examples to the wiki.

Rob


---

Comment by rbeezer created at 2010-02-28 06:59:19

Recent changes:

(1) Command-line switches, so conversion is not restricted to working directory.

(2) Support for SageTeX (by Robert Marik, very impressive).

(3) Better support for more graphic types.

(4) A pure Python script for greater portability and faster startup.

This should work quite well now for converting article-length latex docs into Sage worksheets.  Multi-section documents (books) are probably busted at the moment due to making single worksheets work better, but it'll come back.

Rob


---

Comment by kcrisman created at 2014-09-18 16:56:25

Hey Rob - I note that you kept working on this until 2011/12.  Think it's ready for inclusion in Sage proper, given that you've moved on to the XML stuff?


---

Comment by kcrisman created at 2014-12-09 02:27:42

See #17473 about sws2tex.
