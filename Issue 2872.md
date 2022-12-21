# Issue 2872: 3d graphics can't be saved to a file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-10 20:14:29

Assignee: was

The bug is described below.  To fix this and close this ticket, just slightly
refactor the code in sage/sage/plot/plot3d/base.pyx so that save to png on a 3d image
saves the tachyon rendered file, gives an sobj on an sobj or no extension, and 
gives an error on all other extension.   This will be all one gets initially.

Another *later* ticket should -- if possible -- make it possible to get the static
image from jmol (if possible).


```
On Thu, Apr 10, 2008 at 11:42 AM, Hector Villafuerte wrote:
> 
>  Hi,
>  I noticed the following (inconsistent?) behavior: saving 2D plots
>  works as expected (a graphic file is stored), but saving 3D plots
>  gives .sobj files instead (see sample code below). Is there a way to
>  save 3D plots from the Notebook? By the way, I know how to save them
>  using jMol's GUI (as reached from Sage terminal), but the idea is to
>  be able to script this.
>

This is a bug.  There's currently no easy nice way to script
saving 3d graphics using Tachyon.   If you do the following

  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5, viewer='tachyon')
  sage: p.show(filename='a', viewer='tachyon')

then the file a.png will be produced but unfortunately a browser window
will also appear showing this file.


>  --
>   Hector
>  
>  
>  sage: p = point([(k,k^2) for k in [0..10]])
>  sage: p.save(DATA+'plot2d.png')
>  sage: type(p)
>  <class 'sage.plot.plot.Graphics'>
>  
>  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5)
>  sage: p.save(DATA+'plot3d-1.png')
>  sage: type(p)
>  <class 'sage.plot.plot3d.base.Graphics3dGroup'>
>  
>  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5, viewer='tachyon')
>  sage: p.save(DATA+'plot3d-2.png')
>  sage: type(p)
>  <class 'sage.plot.plot3d.base.Graphics3dGroup'>


```



---

Comment by was created at 2009-09-10 15:24:32

Another nice description of the problem by Jason Grout:

```
This has come up before---p.save() for 2d graphics tries
to save an image.  p.save() for 3d graphics doesn't try to save an
image.  It's an inconsistency.  One way to get fix this is to override
the 3d graphics save routine to do what the 2d graphics save routine
does---look at the file extension and if it is a recognized image
extension, save the image; otherwise, save a Sage sobj pickle.  This is
also why 3d things don't work with animate().  animate() expects to be
able to do p.save('test.png') and have a graphic image test.png saved
out to disk.

You can save a 3d graphics by hand by plotting in jmol and either
selecting "Get Image" next to the image, which converts to jpg, or if
you're doing this from the command line, you can select File|Export from
the java viewer that pops up.  That's rather laborious for creating an
animation, though.

To get an image using tachyon, use show() with filename and viewer
parameters:

sage: show(sphere(), filename='test',viewer='tachyon')

You can use that trick to make a .save() method for 3d graphics (maybe
TransformGroup class or something?) that behaves like the 2d graphics
save.  Then animate should work.

I don't have time to do this right now, but I think this should give
someone enough information to be able to fix things if they are interested.

Thanks,
```



---

Comment by wcauchois created at 2010-01-17 02:33:19

Changing status from new to needs_review.


---

Comment by wcauchois created at 2010-01-17 02:33:19

The attached patch implements this feature as described. When a filename ending in an image format extension is passed to save (several formats are supported through PIL), Tachyon is used to render the Graphics3d.

I had to factor some code out of show() into _process_viewing_options(), but hopefully that won't break anything (and I think it makes show() much cleaner).

I think this is ready for review.


---

Comment by timdumol created at 2010-01-17 19:55:40

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-17 19:55:40

Works perfectly, but it may be worth adding a short docstring for `_process_viewing_options()` for developers. Also, PIL supports JPEG, so perhaps that should be added as well. '.tif' should also be accepted. It may be worth nothing that PIL requires libjpeg and libtiff to be present when compiled in order to support JPEG and TIFF.


---

Attachment

based on sage 4.3.1.rc0


---

Comment by wcauchois created at 2010-01-19 00:01:35

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-20 08:45:46

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-20 08:45:46

Nice. Followup patch looks good and works great for me.


---

Comment by robertwb created at 2010-01-20 08:57:22

Changing status from positive_review to needs_work.


---

Comment by robertwb created at 2010-01-20 08:57:22

Trivial failure in sage/plot/plot3d/base.pyx


```
    sage: G.texture_set()
Expected:
    set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
Got:
    set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
```



---

Comment by wcauchois created at 2010-01-20 09:29:11

Replying to [comment:6 robertwb]:
> Trivial failure in sage/plot/plot3d/base.pyx
> 
> {{{
>     sage: G.texture_set()
> Expected:
>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
> Got:
>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
> }}}

This doctest failure has been in base.pyx for a long time. I fixed it in #7985. It is not related to the changes in this ticket.

Thanks for being a thorough reviewer :).


---

Comment by timdumol created at 2010-01-20 11:39:31

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-20 11:39:31

It passes for me in sage-4.3.rc1. I'm putting this back to positive review.


---

Comment by timdumol created at 2010-01-20 11:39:36

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 14:57:11

Applied to 4.3.2, the patch yields


```
File "/mnt/usb1/scratch/release/sage-4.3.3.alpha0/devel/sage/sage/plot/plot3d/base.pyx", line 1395:
    sage: G.texture_set()
Expected:
    set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
Got:
    set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
```



---

Comment by mpatel created at 2010-02-10 14:58:37

This is on sage.math.  The patch queue:

```
trac_8219.patch
trac_3683-upgrade_moinmoin.patch
trac_8183-French_pdf.patch
trac_8190-docbuild.patch
trac_8184-eclib.patch
trac_8184-indentation.patch
trac_8155.patch
trac_8124-selmer-nf.review.patch
trac_7575.patch
trac_7575-followup.patch
trac_8189-hg.patch
trac_7935.patch
trac_7935b.2.patch
trac_6296.patch
trac_6296-part2.patch
trac6942_jordan.patch
trac6942_jordan_tests.patch
trac_6942-reviewer.patch
trac_8128-latex_cell_unicode.patch
trac_7313-multiline.patch
trac_8203-doc.patch
trac_8206_developer-doc.patch
trac_7944-dev-guide.patch
trac-8211.patch
trac_8044-categories_finite_groups-nt.patch
trac_8215_empty_word-sl.patch
trac_8186_length_handling-sl.patch
trac_8186_minor_doc_changes-abm.patch
trac_8140-sturmian-sl.patch
trac_8140-doc_fixes-abm.patch
trac_8140_cf-arg-sl.patch
trac_8093_palindromes_prefixes-abm.patch
trac_8093_doc_fixes-sl.patch
trac_7978_crystal_cleanup-as.2.patch
trac_6775-disjoint_set-sl.patch
7580_fixes_and_extensions_total.patch
trac_8120-uniquerep_hash-fh.patch
trac_8212-minimal_weight_poly_defining_GF2n.patch
6199-fast-int-mul-all.patch
trac_8188.patch
trac_8138-one_column_index-v2.patch
trac_8209-mathtt.3.patch
trac_8199-dev-guide.patch
trac_7947.patch
trac_7793-zorder-disk.patch
trac_4838-vd.patch
trac_8082.patch
trac-8004-region_plot.patch
trac_6878_exclude.patch
trac_2872.patch                  # You are here!
8185-numerical-noise.patch
trac_8180-kpsewhich.patch
```



---

Comment by mpatel created at 2010-02-10 14:58:37

Changing status from positive_review to needs_work.


---

Comment by wcauchois created at 2010-02-10 23:10:15

Replying to [comment:10 mpatel]:
> Applied to 4.3.2, the patch yields
> 
> {{{
> File "/mnt/usb1/scratch/release/sage-4.3.3.alpha0/devel/sage/sage/plot/plot3d/base.pyx", line 1395:
>     sage: G.texture_set()
> Expected:
>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
> Got:
>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
> }}}

I don't get it, wasn't #7985 merged? I get no such doctest failure with Sage 4.3.1, which I downloaded from the website.


---

Comment by mpatel created at 2010-02-10 23:28:44

The "new" failure seems to be in a different place (line 1395 vs. 758).


---

Comment by wcauchois created at 2010-02-11 00:37:12

Replying to [comment:13 mpatel]:
> The "new" failure seems to be in a different place (line 1395 vs. 758).

I see. So there's another nefarious texture_set() doctest that isn't consistent across runs. I'll open a ticket and fix this one too.


---

Comment by mpatel created at 2010-02-11 00:41:27

If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.


---

Comment by wcauchois created at 2010-02-11 01:12:01

Replying to [comment:15 mpatel]:
> If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.

Hmm... that's a good idea. But its too late. I already wasted one of our precious ticket numbers on this tiny tiny patch... see #8235.

Do you think you could review it real quick?


---

Comment by mpatel created at 2010-02-11 10:11:32

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-11 10:11:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:03:54

Resolution: fixed
