# Issue 2872: 3d graphics can't be saved to a file

archive/issues_002872.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe bug is described below.  To fix this and close this ticket, just slightly\nrefactor the code in sage/sage/plot/plot3d/base.pyx so that save to png on a 3d image\nsaves the tachyon rendered file, gives an sobj on an sobj or no extension, and \ngives an error on all other extension.   This will be all one gets initially.\n\nAnother *later* ticket should -- if possible -- make it possible to get the static\nimage from jmol (if possible).\n\n```\nOn Thu, Apr 10, 2008 at 11:42 AM, Hector Villafuerte wrote:\n> \n>  Hi,\n>  I noticed the following (inconsistent?) behavior: saving 2D plots\n>  works as expected (a graphic file is stored), but saving 3D plots\n>  gives .sobj files instead (see sample code below). Is there a way to\n>  save 3D plots from the Notebook? By the way, I know how to save them\n>  using jMol's GUI (as reached from Sage terminal), but the idea is to\n>  be able to script this.\n>\n\nThis is a bug.  There's currently no easy nice way to script\nsaving 3d graphics using Tachyon.   If you do the following\n\n  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5, viewer='tachyon')\n  sage: p.show(filename='a', viewer='tachyon')\n\nthen the file a.png will be produced but unfortunately a browser window\nwill also appear showing this file.\n\n\n>  --\n>   Hector\n>  \n>  \n>  sage: p = point([(k,k^2) for k in [0..10]])\n>  sage: p.save(DATA+'plot2d.png')\n>  sage: type(p)\n>  <class 'sage.plot.plot.Graphics'>\n>  \n>  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5)\n>  sage: p.save(DATA+'plot3d-1.png')\n>  sage: type(p)\n>  <class 'sage.plot.plot3d.base.Graphics3dGroup'>\n>  \n>  sage: p = point3d([(k,k^2,0) for k in [0..10]], size=5, viewer='tachyon')\n>  sage: p.save(DATA+'plot3d-2.png')\n>  sage: type(p)\n>  <class 'sage.plot.plot3d.base.Graphics3dGroup'>\n\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2872\n\n",
    "created_at": "2008-04-10T20:14:29Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "3d graphics can't be saved to a file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2872",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/2872





---

archive/issue_comments_019666.json:
```json
{
    "body": "Another nice description of the problem by Jason Grout:\n\n```\nThis has come up before---p.save() for 2d graphics tries\nto save an image.  p.save() for 3d graphics doesn't try to save an\nimage.  It's an inconsistency.  One way to get fix this is to override\nthe 3d graphics save routine to do what the 2d graphics save routine\ndoes---look at the file extension and if it is a recognized image\nextension, save the image; otherwise, save a Sage sobj pickle.  This is\nalso why 3d things don't work with animate().  animate() expects to be\nable to do p.save('test.png') and have a graphic image test.png saved\nout to disk.\n\nYou can save a 3d graphics by hand by plotting in jmol and either\nselecting \"Get Image\" next to the image, which converts to jpg, or if\nyou're doing this from the command line, you can select File|Export from\nthe java viewer that pops up.  That's rather laborious for creating an\nanimation, though.\n\nTo get an image using tachyon, use show() with filename and viewer\nparameters:\n\nsage: show(sphere(), filename='test',viewer='tachyon')\n\nYou can use that trick to make a .save() method for 3d graphics (maybe\nTransformGroup class or something?) that behaves like the 2d graphics\nsave.  Then animate should work.\n\nI don't have time to do this right now, but I think this should give\nsomeone enough information to be able to fix things if they are interested.\n\nThanks,\n```",
    "created_at": "2009-09-10T15:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19666",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_019667.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T02:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19667",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019668.json:
```json
{
    "body": "The attached patch implements this feature as described. When a filename ending in an image format extension is passed to save (several formats are supported through PIL), Tachyon is used to render the Graphics3d.\n\nI had to factor some code out of show() into _process_viewing_options(), but hopefully that won't break anything (and I think it makes show() much cleaner).\n\nI think this is ready for review.",
    "created_at": "2010-01-17T02:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19668",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

The attached patch implements this feature as described. When a filename ending in an image format extension is passed to save (several formats are supported through PIL), Tachyon is used to render the Graphics3d.

I had to factor some code out of show() into _process_viewing_options(), but hopefully that won't break anything (and I think it makes show() much cleaner).

I think this is ready for review.



---

archive/issue_comments_019669.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-17T19:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19669",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_019670.json:
```json
{
    "body": "Works perfectly, but it may be worth adding a short docstring for `_process_viewing_options()` for developers. Also, PIL supports JPEG, so perhaps that should be added as well. '.tif' should also be accepted. It may be worth nothing that PIL requires libjpeg and libtiff to be present when compiled in order to support JPEG and TIFF.",
    "created_at": "2010-01-17T19:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19670",
    "user": "https://github.com/TimDumol"
}
```

Works perfectly, but it may be worth adding a short docstring for `_process_viewing_options()` for developers. Also, PIL supports JPEG, so perhaps that should be added as well. '.tif' should also be accepted. It may be worth nothing that PIL requires libjpeg and libtiff to be present when compiled in order to support JPEG and TIFF.



---

archive/issue_comments_019671.json:
```json
{
    "body": "Attachment [trac_2872.patch](tarball://root/attachments/some-uuid/ticket2872/trac_2872.patch) by wcauchois created at 2010-01-19 00:00:51\n\nbased on sage 4.3.1.rc0",
    "created_at": "2010-01-19T00:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19671",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_2872.patch](tarball://root/attachments/some-uuid/ticket2872/trac_2872.patch) by wcauchois created at 2010-01-19 00:00:51

based on sage 4.3.1.rc0



---

archive/issue_comments_019672.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T00:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19672",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T08:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19673",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019674.json:
```json
{
    "body": "Nice. Followup patch looks good and works great for me.",
    "created_at": "2010-01-20T08:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19674",
    "user": "https://github.com/robertwb"
}
```

Nice. Followup patch looks good and works great for me.



---

archive/issue_comments_019675.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-20T08:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19675",
    "user": "https://github.com/robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_019676.json:
```json
{
    "body": "Trivial failure in sage/plot/plot3d/base.pyx\n\n```\n    sage: G.texture_set()\nExpected:\n    set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])\nGot:\n    set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])\n```",
    "created_at": "2010-01-20T08:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19676",
    "user": "https://github.com/robertwb"
}
```

Trivial failure in sage/plot/plot3d/base.pyx

```
    sage: G.texture_set()
Expected:
    set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
Got:
    set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
```



---

archive/issue_comments_019677.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> Trivial failure in sage/plot/plot3d/base.pyx\n> \n> \n> ```\n>     sage: G.texture_set()\n> Expected:\n>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])\n> Got:\n>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])\n> ```\n\n\nThis doctest failure has been in base.pyx for a long time. I fixed it in #7985. It is not related to the changes in this ticket.\n\nThanks for being a thorough reviewer :).",
    "created_at": "2010-01-20T09:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19677",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:6 robertwb]:
> Trivial failure in sage/plot/plot3d/base.pyx
> 
> 
> ```
>     sage: G.texture_set()
> Expected:
>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
> Got:
>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
> ```


This doctest failure has been in base.pyx for a long time. I fixed it in #7985. It is not related to the changes in this ticket.

Thanks for being a thorough reviewer :).



---

archive/issue_comments_019678.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T11:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19678",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019679.json:
```json
{
    "body": "It passes for me in sage-4.3.rc1. I'm putting this back to positive review.",
    "created_at": "2010-01-20T11:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19679",
    "user": "https://github.com/TimDumol"
}
```

It passes for me in sage-4.3.rc1. I'm putting this back to positive review.



---

archive/issue_comments_019680.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T11:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19680",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019681.json:
```json
{
    "body": "Applied to 4.3.2, the patch yields\n\n```\nFile \"/mnt/usb1/scratch/release/sage-4.3.3.alpha0/devel/sage/sage/plot/plot3d/base.pyx\", line 1395:\n    sage: G.texture_set()\nExpected:\n    set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])\nGot:\n    set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])\n```",
    "created_at": "2010-02-10T14:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19681",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_019682.json:
```json
{
    "body": "This is on sage.math.  The patch queue:\n\n```\ntrac_8219.patch\ntrac_3683-upgrade_moinmoin.patch\ntrac_8183-French_pdf.patch\ntrac_8190-docbuild.patch\ntrac_8184-eclib.patch\ntrac_8184-indentation.patch\ntrac_8155.patch\ntrac_8124-selmer-nf.review.patch\ntrac_7575.patch\ntrac_7575-followup.patch\ntrac_8189-hg.patch\ntrac_7935.patch\ntrac_7935b.2.patch\ntrac_6296.patch\ntrac_6296-part2.patch\ntrac6942_jordan.patch\ntrac6942_jordan_tests.patch\ntrac_6942-reviewer.patch\ntrac_8128-latex_cell_unicode.patch\ntrac_7313-multiline.patch\ntrac_8203-doc.patch\ntrac_8206_developer-doc.patch\ntrac_7944-dev-guide.patch\ntrac-8211.patch\ntrac_8044-categories_finite_groups-nt.patch\ntrac_8215_empty_word-sl.patch\ntrac_8186_length_handling-sl.patch\ntrac_8186_minor_doc_changes-abm.patch\ntrac_8140-sturmian-sl.patch\ntrac_8140-doc_fixes-abm.patch\ntrac_8140_cf-arg-sl.patch\ntrac_8093_palindromes_prefixes-abm.patch\ntrac_8093_doc_fixes-sl.patch\ntrac_7978_crystal_cleanup-as.2.patch\ntrac_6775-disjoint_set-sl.patch\n7580_fixes_and_extensions_total.patch\ntrac_8120-uniquerep_hash-fh.patch\ntrac_8212-minimal_weight_poly_defining_GF2n.patch\n6199-fast-int-mul-all.patch\ntrac_8188.patch\ntrac_8138-one_column_index-v2.patch\ntrac_8209-mathtt.3.patch\ntrac_8199-dev-guide.patch\ntrac_7947.patch\ntrac_7793-zorder-disk.patch\ntrac_4838-vd.patch\ntrac_8082.patch\ntrac-8004-region_plot.patch\ntrac_6878_exclude.patch\ntrac_2872.patch                  # You are here!\n8185-numerical-noise.patch\ntrac_8180-kpsewhich.patch\n```",
    "created_at": "2010-02-10T14:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19682",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_019683.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-10T14:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19683",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_019684.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> Applied to 4.3.2, the patch yields\n> \n> \n> ```\n> File \"/mnt/usb1/scratch/release/sage-4.3.3.alpha0/devel/sage/sage/plot/plot3d/base.pyx\", line 1395:\n>     sage: G.texture_set()\n> Expected:\n>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])\n> Got:\n>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])\n> ```\n\n\nI don't get it, wasn't #7985 merged? I get no such doctest failure with Sage 4.3.1, which I downloaded from the website.",
    "created_at": "2010-02-10T23:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19684",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:10 mpatel]:
> Applied to 4.3.2, the patch yields
> 
> 
> ```
> File "/mnt/usb1/scratch/release/sage-4.3.3.alpha0/devel/sage/sage/plot/plot3d/base.pyx", line 1395:
>     sage: G.texture_set()
> Expected:
>     set([Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
> Got:
>     set([Texture(texture816, red, ff0000), Texture(texture817, yellow, ffff00)])
> ```


I don't get it, wasn't #7985 merged? I get no such doctest failure with Sage 4.3.1, which I downloaded from the website.



---

archive/issue_comments_019685.json:
```json
{
    "body": "The \"new\" failure seems to be in a different place (line 1395 vs. 758).",
    "created_at": "2010-02-10T23:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19685",
    "user": "https://github.com/qed777"
}
```

The "new" failure seems to be in a different place (line 1395 vs. 758).



---

archive/issue_comments_019686.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> The \"new\" failure seems to be in a different place (line 1395 vs. 758).\n\n\nI see. So there's another nefarious texture_set() doctest that isn't consistent across runs. I'll open a ticket and fix this one too.",
    "created_at": "2010-02-11T00:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19686",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:13 mpatel]:
> The "new" failure seems to be in a different place (line 1395 vs. 758).


I see. So there's another nefarious texture_set() doctest that isn't consistent across runs. I'll open a ticket and fix this one too.



---

archive/issue_comments_019687.json:
```json
{
    "body": "If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.",
    "created_at": "2010-02-11T00:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19687",
    "user": "https://github.com/qed777"
}
```

If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.



---

archive/issue_comments_019688.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.\n\n\nHmm... that's a good idea. But its too late. I already wasted one of our precious ticket numbers on this tiny tiny patch... see #8235.\n\nDo you think you could review it real quick?",
    "created_at": "2010-02-11T01:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19688",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:15 mpatel]:
> If the fix is similar to that at #7985, feel free to add the patch here and add a comment requesting a review.


Hmm... that's a good idea. But its too late. I already wasted one of our precious ticket numbers on this tiny tiny patch... see #8235.

Do you think you could review it real quick?



---

archive/issue_comments_019689.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-11T10:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19689",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_019690.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T10:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19690",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006566.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:03:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2872#event-6566"
}
```



---

archive/issue_comments_019691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2872#issuecomment-19691",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
