# Issue 8442: Lie Methods and Related Combinatorics (tutorial)

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2010-03-05 03:08:27

Assignee: mvngu

CC:  sage-combinat niles




---

Attachment

This patch adds a tutorial about Lie Methods and Related Combinatorics to Sage.

Apply the patch and also copy the file wcf1.png into $SAGE_ROOT/devel/sage-queue/doc/en/lie/. Then you can build the documentation with the commands:

sage -docbuild lie html

sage -docbuild lie pdf

There is supposed to be a chapter on Crystals but that is not written yet.


---

Comment by bump created at 2010-03-05 03:16:00

Changing assignee from mvngu to bump.


---

Attachment


---

Attachment


---

Comment by bump created at 2010-03-09 04:38:01

Changing status from new to needs_review.


---

Comment by bump created at 2010-03-11 18:15:19

Lie methods and related combinatorics tutorial


---

Attachment

Revised to take into account changes in #8414.


---

Comment by mvngu created at 2010-03-12 22:50:21

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-03-12 22:50:21

I'm rebasing [trac_8442_lie_documentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442_lie_documentation.patch) on top of the prerequisites at #8470.


---

Attachment

rebased Lie tutorial


---

Attachment

reviewer patch


---

Comment by mvngu created at 2010-03-13 07:39:10

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-03-13 07:39:10

I have rebased Dan's patch; see the result at [trac_8442-lie-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-lie-rebased.patch). I have also attached a reviewer patch that makes substantial clean-ups in terms of style and consistency. Changes include:

 1. Remove the use of ":math:". That is not necessary, as the Sage docbuilder can handle typeset mathematics without that syntax. Also, the resulting text is easier to read without heaps of ":math:" scattered throughout a ReST document.
 1. Some stylistic clean-ups.
 1. Make the formatting consistent.
 1. Using the syntax ".. MATH::" to center math expressions.

Both Dan's rebased patch and my reviewer patch need reviewing. This ticket now depends on #8468.


---

Comment by bump created at 2010-03-13 18:45:27

Looks very good after the rebased patch and the reviewer's patch.

The three .png files must be in `doc/en/thematic_tutorials/static/` .

The patch will require minor revision if #8414 is not merged. (There
is also a dependence on #8411 but less important.) If this proves
necessary I will provide a revision. It is a matter of changing "space"
back to "lattice" in a few places.

I give a positive review to the rebased and reviewer's patch. I am not
changing the patch status since I am the author of the original patch.


---

Attachment

Additional patch taking into account changes in #8414


---

Comment by bump created at 2010-03-24 22:50:37

Due to changes in #8414, there is an additional small patch called trac_8442-weyl_groups-revision.patch.


---

Comment by mjordan7 created at 2010-05-05 19:49:54

Looks good! I tested it fine using the three latest patches and the three PNG files. Pictures were inserted properly and looked fine.
~Mark


---

Comment by mjordan7 created at 2010-05-14 19:50:49

Changing status from needs_review to needs_work.


---

Comment by mjordan7 created at 2010-05-14 19:50:49

Tested with Sage Version 4.4.2.alpha0, Release Date: 2010-05-08 and index.rst under thematic tutorials fails to apply now.
~Mark


---

Attachment


---

Comment by bump created at 2010-05-15 04:05:12

I have uploaded the patch trac_8442-lie-rebased-to-4.4.2.alpha0.

This contains the three patches:


```
trac_8442-lie-rebased.patch 
trac_8442-reviewer.patch-reviewer patch
trac_8442-weyl_groups-revision.patch
```


The purpose of this patch is simply to address mjordan's comment that the patch does not apply cleanly. In order to accomplish a clean this the patch
adds files doc/en/thematic_tutorials/index.rst and bibliography.rst.
These files presume that three other thematic tutorials will also be included in sage - otherwise they will produce broken links. 

The release manager may prefer to work with the original three patches.

Note that in addition to the patch three .png files must be included.


---

Comment by bump created at 2010-05-15 04:05:12

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment


---

Comment by mvngu created at 2010-05-15 07:11:41

In addition to applying cleanly, the thematic tutorials must also show up on the standard documentation and be linked from there. I have uploaded the patch [trac_8442-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch) in order to configure the documentation build system to link to the thematic tutorials. The patch [trac_8442-lie-rebased-4.4.2.rc0.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-lie-rebased-4.4.2.rc0.patch) is a rebase of Dan's patch against Sage 4.4.2.rc0. This rebase also configures the doc build system to build the Lie tutorial. The situation now is that anyone but myself can sign off on the two latest patches I uploaded. That is, anyone but myself need to only review those two patches. See the ticket description for instruction on how to apply patches on this ticket.


---

Comment by rbeezer created at 2010-05-24 03:16:01

This is a very impressive contribution to the documentation and will be a great example for the thematic section.  Applied #8464, the two patches, and the added the three PNG's.  Everything applied and built cleanly, once I caught the proper location for the three PNG files.

However, running doctests produced 22 errors across several of the files.  On 4.4.2.rc0


```
sage -t doc/en/thematic_tutorials/lie
```


yields


```
The following tests failed:


        sage -t  "devel/sage-main/doc/en/thematic_tutorials/lie/weyl_groups.rst"
        sage -t  "devel/sage-main/doc/en/thematic_tutorials/lie/weight_ring.rst"
        sage -t  "devel/sage-main/doc/en/thematic_tutorials/lie/crystals.rst"
        sage -t  "devel/sage-main/doc/en/thematic_tutorials/lie/weyl_character_ring.rst" # Exception from doctest framework
        sage -t  "devel/sage-main/doc/en/thematic_tutorials/lie/branching_rules.rst"
```


I did not investigate the source of the failures very carefully, Many of them were of the "name 'foo' not defined" variety rather than mis-matched outputs.  Hopefully this isn't a false alarm.

I'd be happy to give this another look after somebody investigates/fixes the doctests.

Rob


---

Comment by rbeezer created at 2010-05-24 03:16:01

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-06-23 17:40:24

In addition to the doctest failures, here are some other issues:

The documentation page that you get by clicking "help" in the notebook, then "fast static versions ...", does not look good with the new section on thematic tutorials: I don't think the three-column layout looks good.

The command `\mathfrak` is not recognized by jsMath, so if you make the documentation with the `--jsmath` flag, it has a lot of errors.

Also, I would suggest creating a directory `doc/en/thematic_tutorials/media/` (just like in the `reference` directory, and we put pictures there.   Wherever the pictures go, they need to be included in SAGE_ROOT/devel/sage/MANIFEST.in so they get included in the Sage library spkg -- you need a line like

```
recursive-include doc/en/thematic_tutorials/media *
```


By the way, you can include the png files in the patch by using the command

```
$ hg add (path to file)/standard1.png
$ hg commit ...
$ hg export -g ...
```

(See [http://trac.sagemath.org/sage_trac/ticket/9074#comment:4](http://trac.sagemath.org/sage_trac/ticket/9074#comment:4) for a similar explanation.)


---

Comment by jhpalmieri created at 2010-07-28 01:36:25

If #8465 gets merged, then trac_8442-config.patch will not be needed.


---

Attachment


---

Attachment

I have added two revised patches:


```
trac_8442-lie-rebased-4.5.2.patch
trac_8442-png-files.patch
```


By mistake I added the first patch twice.

These address most of the problems found by rbeezer and jhpalmieri.

* Now passes `sage -t`

* New `doc/en/thematic_tutorials/media/*png`

* `doc/en/thematic_tutorials/*png` added to MANIFEST.in

* `.png` files are in a patch.

The one matter I did not try to address is the problem with jsMath. Is there a jsMath way to get fraktur fonts?


---

Comment by bump created at 2010-08-22 16:11:16

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-08-22 20:19:18

Replying to [comment:20 bump]:
> The one matter I did not try to address is the problem with jsMath. Is there a jsMath way to get fraktur fonts?

MathJAX is slated to replace jsMath.  It has been released, but I can't guess at how much work it will be to get it into the notebook.
http://trac.sagemath.org/sage_trac/ticket/9774

It would appear from the discussion below that Fraktur fonts will be possible (maybe standard) then.
http://meta.mathoverflow.net/discussion/473/help-test-mathjax/

It seems Fraktur is available now for jsMath, but maybe we don't ship that with the notebook?
http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/welcome.html

I'll look closer at reviewing this again when I've got a bit more time.

Rob


---

Comment by bump created at 2010-09-04 19:10:50

Changing status from needs_review to needs_work.


---

Comment by bump created at 2010-09-04 19:10:50

I just discovered that after the patch this still does *not* pass sage -t.

Maybe I uploaded the wrong patch.

I am changing the status back to needs_work.

Dan


---

Comment by bump created at 2010-09-05 13:19:04

Evidently I made a mercurial mistake and uploaded the wrong patch. (I probably forgot to commit before exporting.)

Furthermore, the fraktur problem is serious enough that it needs to be fixed. Unfortunately frakture jsmath fonts are available but not installed by default. Perhaps the best short-term option is to find another font.

Finally, I can make use of the information here:

http://groups.google.com/group/sage-devel/msg/086441965eb4f20b

to improve the document. This addresses the cause of many of the failures.
I am leaving the status needs_work for the time being.


---

Comment by bump created at 2010-09-09 00:14:13

I am posting corrected files that pass `sage -t` with sage-4.5.3.

Regarding the --jsmath issue, the \mathfrak problem is not the end of the story. There are further problems. Matrices of size > 2 look awful with jsmath, and in the section crystals.rst there are some tableaux. I tried two different methods of creating these in tex. One failed since jsmath doesn't know \raisebox, and the other (based on arrays) failed since jsmath doesn't know \hline.

I therefore feel it is better not to try revising the files to work with jsmath. I recommend building them without jsmath and can revisit the issue after the switch to mathjax. The built documentation (with dvipng) is here:

http://match.stanford.edu/bump/thematic_tutorials/lie.html

I am changing the status back to needs_review.


---

Comment by bump created at 2010-09-09 00:14:13

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-09-09 00:34:13

Replying to [comment:25 bump]:
> Matrices of size > 2 look awful with jsmath, and in the section crystals.rst there are some tableaux. I tried two different methods of creating these in tex. One failed since jsmath doesn't know \raisebox, and the other (based on arrays) failed since jsmath doesn't know \hline.

Hi Dan,

I've had good luck with jsMath if I use \begin{tabular}\end{tabular} and then wrap individual entries with dollar signs.  Then the \hline's seem to workout OK.  The PDF doesn't really seem to suffer too much from this abuse.

I don't know if MathJAX or jsMath will ever be too happy about a \raisebox - the notion of a precise length doesn't always translate from printed page to web page very well.

Anyway, I didn't even look at your tableau, but you might experiment with a single one using the tabular environment and decide from there.

Rob


---

Comment by bump created at 2010-09-09 04:07:37

> I've had good luck with jsMath if I use \begin{tabular}\end{tabular} and then wrap individual entries with dollar signs. Then the \hline's seem to workout OK. The PDF doesn't really seem to suffer too much from this abuse.

Can you give an example?

My hope is that the patch can be reviewed without making jsmath a prerequisite. The doc looks good with dvipng, but not so good with jsmath. I could substitute another font for fraktur (I tried mathbf), and I could try again with your suggestion for making tableaux, and I could try to overlook the fact that the large matrices really awful with mathjs, but given that the dvipng doc looks fine, I'd rather leave it as it is and revisit the issue when mathjax rolls in.

Dan


---

Comment by jhpalmieri created at 2010-09-09 04:37:35

I almost always use the `--jsmath` option for docbuilding because it's faster than not using it.  I would guess that some other people do the same.  We really try to avoid warnings when building the docs, so I don't know if this should get a positive review if it doesn't build right with jsmath, especially since there is an easy fix: use something other than mathfrak.

Wait, here's an idea: we can add a jsMath macro (as [described here](http://www.math.union.edu/~dpvc/jsMath/authors/macros.html)) to define `\mathfrak` in jsMath to be boldface, for example.  Since this is defined in jsMath, it doesn't override the ordinary definition if you're not using the jsmath option.  This is easy to do: we just patch the configuration file for the thematic tutorials document.  I'm attaching a patch.


---

Attachment

avoid jsmath errors about mathfrak


---

Comment by bump created at 2010-09-09 20:24:37

I have revised the patch. The resulting patch produces a tutorial that looks OK with both dvipng and jsmath. This addressed three problems.

(1) For \mathfrak, it includes trac_8442-mathfrak.patch (thanks!)

(2) The problems with matrices turned out to be only on a particular machine. On this machine, every browser I've tried (firefox, seamonkey and konqueror) makes jsmath matrices look very broken. But the same html looks OK on other machines.

(3) For the tableaux, I hand-made png images for all of these. I also did some other rewriting of the section on crystals.

Thanks to jhpalmieri and rbeezer for feedback.

Dan


---

Comment by rbeezer created at 2010-09-09 21:01:56

Hi Dan,

I think I was a bit too cavalier.  I've been converting a lot of Latex to jsMath (using the tex4ht converter) and switching to tabular solves lots of gotchas, but I don't think I can make that approach work directly.  In other words, no - I don't have an example, despite trying quite a few things last night.  I hope I didn't send you on too wild of a goose chase.

On the plus side, `MathJax` looks good - I've been fiddling with it (outside of the notebook).

I think PNGs are a good compromise.  I've been helping Tom Judson with his open source textbook and he's redone the diagrams in tikz.  There's code in the CVS version of PGF that will "externalize" the graphics.  So the PDF has "native" diagrams, and the web page versions suck in the externalized PNG graphics versions as images.  Real similar to your workaround here.

Rob


---

Comment by bump created at 2010-09-10 00:34:56

I reposted the two relevant patches, trac_8442-png-files.patch and trac_8442-rebased-4.5.3.patch.

I made some further changes to crystals.rst and I found that one of the png files had been obsoleted by the revisions, hence removed it from the distributed files.

Dan


---

Comment by bump created at 2010-09-10 23:17:23

Thematic tutorial: Lie methods and related combinatorics


---

Attachment

I uploaded a new version with minor polishing here and there.


---

Comment by bump created at 2010-09-10 23:22:16

You may find versions of this tutorial made with both dvipng and jsmath here and here:

http://match.stanford.edu/bump/thematic_tutorials/lie.html
http://match.stanford.edu/bump/thematic_tutorials-js/lie.html


---

Comment by bump created at 2010-09-26 17:40:12

Thematic Tutorial: Lie methods and related combinatorics


---

Attachment

With sage-4.6.alpha1 the patch needed rebasing. I did this, then made a couple of other changes which I think are improvements. I removed the material about intertwining operators, which seems too specialized for a document like this.  I will make available this elsewhere. I added a new section called Integration showing how to compute some integrals over Lie groups.

I updated the links at:

http://match.stanford.edu/bump/thematic_tutorials/lie.html  

http://match.stanford.edu/bump/thematic_tutorials-js/lie.html


---

Comment by jhpalmieri created at 2010-11-02 20:49:19

This looks like an amazing document to include with Sage.  Thanks for working on it.

First, all doctests pass for me.

I get three warnings when building the docs, two of which anyone can fix:

```
/Applications/sage/devel/sage/doc/en/thematic_tutorials/lie/weyl_character_ring.rst:397: (WARNING/2) Title underline too short.

Integration
-------
/Applications/sage/devel/sage/doc/en/thematic_tutorials/lie/weyl_character_ring.rst:397: (WARNING/2) Title underline too short.

Integration
-------
```

The third one I think Dan has to do:

```
/Applications/sage/devel/sage/doc/en/thematic_tutorials/lie/weyl_groups.rst:: WARNING: citation not found: BumpNakasuji2010
```


A few questions and comments about the text: first, the style in the Sage documentation is to use `\Bold{C`} for the complex numbers, and similarly for R and Q.  This is more of an issue for docstrings for methods, functions, etc., but you might consider changing it.

In introduction.rst, 

```
For example, we could take `G = SU(n)`,
`\mathfrak{g} = \mathfrak{sl}(n, \mathbb{R})`,
`\mathfrak{g}_{\mathbb{C}} = \mathfrak{sl}(n, \mathbb{C})` and
`G = SL(n, \mathbb{C})`.
```

Should the last "G" be "G_{\mathbb{C}}" (or "G_{\Bold{C}}")?

In lie_basics.rst, on line 141: `However Parabolic subgroups do not exist for compact Lie groups.`  Don't capitalize "Parabolic".

On line 150: 

```
Such a type is implemented in Sage as a pair ``[`X`,r]``
}}}  
I would use plain quotes around the X, not backquotes: ```['X',r]```

A few lines later:
{{{
The exceptional types are::

    ['G',2],  ['F',4],  ['E',6], ['E',7] or ['E',8].
}}}
The indented block is verbatim text, so spacing matters.  The inconsistency between double-spacing and single-spacing looks odd to me, and I would just put single spaces after all of the commas.

weyl_character_ring.rst, line 239, `with Cartan type `['B',r]``: I would use double back quotes here instead of single ones.


---

Comment by jhpalmieri created at 2010-11-02 20:49:19

Changing status from needs_review to needs_work.


---

Comment by bump created at 2010-11-02 23:57:36

#8442: Thematic tutorial on Lie methods and related combinatorics


---

Attachment


---

Comment by bump created at 2010-11-03 00:00:49

Changing status from needs_work to needs_review.


---

Comment by bump created at 2010-11-03 00:02:36

All jhpalmieri's comments are good. I have updated the patch and reposted it as trac_8442-rebased-4.6.1.patch.


---

Comment by jhpalmieri created at 2010-11-06 22:11:28

I'm attaching a patch to fix the spacing in one table in lie_basics.rst.  All tests pass, and with the extra patch, the docs build in both html and pdf formats.

I'm not a Lie algebra expert, nor an expert in Sage's implementation of Lie algebras.  Can someone else take a look at this and (I hope) positively review it soon)?  It would be nice to get this merged.


---

Comment by jhpalmieri created at 2010-11-06 22:11:53

apply on top of other patches


---

Attachment


---

Comment by bump created at 2010-12-09 13:48:09

It appears that the buildbot is trying to apply all 17 patches.

http://sage.math.washington.edu:21100/ticket/8442/

Most of these are superceded, though only admin can actually remove them. As far as I know the three patches


```
 trac_8442-rebased-4.6.1.patch
 trac_8442-png-files.patch
 trac_8442-ref-spacing.patch
```


should apply cleanly.


---

Comment by jhpalmieri created at 2010-12-15 18:45:41

To the buildbot: apply

 - trac_8442-rebased-4.6.1.patch
 - trac_8442-png-files.patch
 - trac_8442-ref-spacing.patch


---

Comment by dimpase created at 2010-12-16 08:23:08

Changing status from needs_review to needs_info.


---

Comment by dimpase created at 2010-12-16 08:23:08

I'd like to give it a positive review, but I still might like to 
know more about few related things:

One is about a way to connecting Lie functionality in GAP to the one in Sage. Anything on this?

It would also be good if anything is said regarding the optional Sage package lie (by Marc van Leeuween). Is it right that basically anything doable in lie can be done in Sage?
In particular, lie can compute decompositions of, say, a tensor product of two representations into irreducibles. It's not clear to me whether one can do this in Sage (without lie).

Dmitrii


---

Comment by bump created at 2010-12-16 13:31:33

> One is about a way to connecting Lie functionality in GAP to the one in Sage. Anything on this?

One issue with GAP on Sage is that the interface needs a lot of work. There is a lot of power in GAP that can't be accessed from Sage because of this.

The Lie theory in Sage is mostly written from scratch. But here is an example where GAP is
involved in the background. We have a class for WeylGroups in weyl_group.py. This
class inherits from MatrixGroup_gens which in turn inherits from MatrixGroup_gap. So
GAP is involved in Weyl Groups.

> It would also be good if anything is said regarding the optional Sage package lie (by Marc van Leeuween). Is it right that basically anything doable in lie can be done in Sage? In particular, lie can compute decompositions of, say, a tensor product of two representations into irreducibles. It's not clear to me whether one can do this in Sage (without lie).

I am not sure whether everything that is doable with LiE is doable with Sage but I do think that anything that is needed from LiE is either in Sage already or (if needed) should be reimplemented. What is in Sage is a pretty complete toolkit for finite-dimensional representations of Lie groups. Decomposing a tensor product into irreducibles is just the multiplication in the WeylCharacterRing. This is addressed in the tutorial. See:

http://match.stanford.edu/bump/thematic_tutorials-js/lie/weyl_character_ring.html#tensor-products-of-representations

Have a look also at the branching rules.

http://match.stanford.edu/bump/thematic_tutorials-js/lie/branching_rules.html

LiE has some functionality for working with Kazhdan-Lusztig polynomials, but that is in Sage, as fast as LiE (though not as fast as Coxeter3). LiE has alternate methods of computing Weyl Characters including use of Demazure characters. Some version of the Demazure character is in the crystal code, but it would also be easy and perhaps useful to add a method to the WeightRing. But it is not urgently needed. Sage uses the Freudenthal multiplicity formula to compute the character.


---

Comment by dimpase created at 2010-12-16 14:10:51

Replying to [comment:45 bump]:


> > It would also be good if anything is said regarding the optional Sage package lie (by Marc van Leeuween). Is it right that basically anything doable in lie can be done in Sage? In particular, lie can compute decompositions of, say, a tensor product of two representations into irreducibles. It's not clear to me whether one can do this in Sage (without lie).
> 
> I am not sure whether everything that is doable with LiE is doable with Sage but I do think that anything that is needed from LiE is either in Sage already or (if needed) should be reimplemented. What is in Sage is a pretty complete toolkit for finite-dimensional representations of Lie groups. Decomposing a tensor product into irreducibles is just the multiplication in the WeylCharacterRing. This is addressed in the tutorial. See:
> 
> http://match.stanford.edu/bump/thematic_tutorials-js/lie/weyl_character_ring.html#tensor-products-of-representations


One particular thing I was able to do using Lie was to compute things in classical invariant theory, such as the dimension of the space of invariants of degree k
of the m-ary form of degree d (for fixed k,m,d). Basically, that meant computing certain symmetric power of certain representation of GL_m (or SL_m), and finding out whether there was a 1-dimensional sub-representation.

Is this doable in Sage?
Thanks!


---

Comment by bump created at 2010-12-16 16:21:41

> Basically, that meant computing certain symmetric power of certain representation of GL_m (or SL_m), and finding out whether there was a 1-dimensional sub-representation. 

For symmetric (or exterior) square you can use the frobenius_schur_indicator method. For higher symmetric powers, here is a way. Suppose we want to compute the symmetric 5-th power of the 8-dimensional adjoint representation of SL(3). The relevant groups are SL(3) and SL(8), so we need Weyl Character rings A2 and A7.


```
sage: A2=WeylCharacterRing("A2",style="coroots")
sage: A7=WeylCharacterRing("A7",style="coroots",cache="true")
sage: s = A7.fundamental_weights()[1]
sage: A7(5*s)
A7(5,0,0,0,0,0,0)
sage: A7(5*s)
A7(5,0,0,0,0,0,0)
sage: A7(5*s).degree()
792
```


This is the symmetric 5-th power of the standard representation of SL(8), which we want to branch down to SL(3) along the adjoint representation, which is a homomorphism SL(3) --> SL(8). So we create the adjoint representation, then branch the symmetric 5-th power representation of SL(8) down to SL(3).


```
sage: ad=A2(1,1); ad.degree()
8
sage: A7(5*s).branch(A2,rule=branching_rule_from_plethysm(ad,"A7"))
A2(0,0) + 2*A2(1,1) + A2(0,3) + A2(3,0) + 2*A2(2,2) + A2(1,4) + A2(4,1) + 2*A2(3,3) + A2(2,5) + A2(5,2) + A2(4,4) + A2(5,5)
```


There is your decomposition into irreducibles. You can see that there is a copy of the trivial representation.


---

Comment by bump created at 2010-12-16 16:31:33

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2010-12-18 03:21:36

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-12-18 03:21:36

Replying to [comment:49 bump]:
Very nice! Positive review. 
(IMHO it would be nice to have your last example included in the tutorial, but I'd leave it to you to decide whether to do this.)

Dmitrii


---

Comment by bump created at 2010-12-18 13:22:52

> Replying to bump: Very nice! Positive review. (IMHO it would be nice to have your last example included in the tutorial, but I'd leave it to you to decide whether to do this.)

I will make a patch for this. Perhaps it should be a separate ticket so as not to further delay this one.


---

Comment by bump created at 2010-12-21 01:15:30

I just noticed that the trac_8442-png-files containing the .png files is not
the right patch!

The files are in the wrong directory (should be doc/en/thematic_tutorials/media)
and some of the images are missing. I am puzzled as to how this happened since
everything was built and tested.

I am changing the status back to needs_work until I can fix this.


---

Comment by bump created at 2010-12-21 01:15:30

Changing status from positive_review to needs_work.


---

Comment by bump created at 2010-12-21 01:26:39

I replaced the file trac_8442-png-files.patch, and am restoring the status to positive_review.

The correct file is 52266 bytes.


---

Comment by bump created at 2010-12-21 01:26:39

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-13 05:46:49

Setting milestone to sage-feature because of #8470.


---

Comment by bump created at 2011-01-13 13:59:50

> Setting milestone to sage-feature because of #8470.

At some point Minh Nguyen added the words "needs to be coordinated with #8470" to the description. However #8470 has not been touched for 8 months. It appears to me that #8470 is an orphaned ticket.

I propose that the milestone for this patch should be changed back to 4.6.2.


---

Comment by dimpase created at 2011-01-13 17:08:23

Replying to [comment:57 bump]:
> > Setting milestone to sage-feature because of #8470.
> 
> At some point Minh Nguyen added the words "needs to be coordinated with #8470" to the description. However #8470 has not been touched for 8 months. It appears to me that #8470 is an orphaned ticket.
> 
> I propose that the milestone for this patch should be changed back to 4.6.2.
> 
> 
I second this. #8470 is a meta-ticket meant for coordinating documentation. Closing the current ticket is a prereq to closing it. So, please close the current ticket, which in no ways depends on #8470.


---

Comment by jdemeyer created at 2011-01-22 20:18:22

Please add ticket number to commit message of [attachment:trac_8442-png-files.patch]


---

Comment by jdemeyer created at 2011-01-22 20:18:22

Changing status from positive_review to needs_work.


---

Attachment

8442: png files


---

Comment by bump created at 2011-01-23 19:25:18

Changing status from needs_work to positive_review.


---

Comment by bump created at 2011-01-23 19:25:18

> Please add ticket number to commit message of trac_8442-png-files.patch

Done.


---

Attachment


---

Comment by jdemeyer created at 2011-01-27 13:58:45

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-27 13:58:45

Added [attachment:8442_manifest.patch], still needs testing.


---

Comment by dimpase created at 2011-01-27 15:04:41

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2011-01-27 15:04:41

Replying to [comment:64 jdemeyer]:
> Added [attachment:8442_manifest.patch], still needs testing.

just tested, it works. I also edited the description to mention this patch too.


---

Comment by dimpase created at 2011-01-27 15:05:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-28 08:48:05

Resolution: fixed
