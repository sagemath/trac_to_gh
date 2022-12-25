# Issue 6685: include pictures in the reference manual and notebook introspection

archive/issues_006685.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @qed777\n\nIncluding pictures in the documentation is easy: a new \"pictures\" directory in doc/en/reference and a quick patch to MANIFEST.in to make sure the contents of that directory are included in distributions.  Then in a docstring, a line like\n\n```\n.. image:: /pictures/sine.png\n```\n\nwill include that file when the reference manual is built.\n\nGetting those pictures included in docstrings in the notebook is trickier.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/60074982a58f1166?tvc=2) for some discussion.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6685\n\n",
    "created_at": "2009-08-07T17:35:35Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "include pictures in the reference manual and notebook introspection",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6685",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

CC:  @qed777

Including pictures in the documentation is easy: a new "pictures" directory in doc/en/reference and a quick patch to MANIFEST.in to make sure the contents of that directory are included in distributions.  Then in a docstring, a line like

```
.. image:: /pictures/sine.png
```

will include that file when the reference manual is built.

Getting those pictures included in docstrings in the notebook is trickier.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/60074982a58f1166?tvc=2) for some discussion.


Issue created by migration from https://trac.sagemath.org/ticket/6685





---

archive/issue_comments_054858.json:
```json
{
    "body": "Here's a patch.  It puts a picture in sage/plot/plot.py which you can see in the reference manual, and with a bit of work, in notebook introspection: type `sage.plot.plot?`.  The work is: you need to make a symlink from `SAGE_ROOT/doc/en/reference/pictures` to `SAGE_ROOT/doc/output/html/en/pictures`.  \n\nThings still to do: \n\n- do this symlink automatically, say when building the reference manual.  \n\n- possibly modify detex in misc/sagedoc.py to remove, or otherwise modify, \".. image::\" directives from command-line help.\n\n- at the moment, the cached version of the docstring (in .sage/sage_notebook/doc) doesn't have the correct URL for the image -- the html is scanned and modified each time it's displayed.  This shouldn't slow things down too much, but should we be saving the correct URL?\n\n- lots of testing.",
    "created_at": "2009-08-07T18:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54858",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  It puts a picture in sage/plot/plot.py which you can see in the reference manual, and with a bit of work, in notebook introspection: type `sage.plot.plot?`.  The work is: you need to make a symlink from `SAGE_ROOT/doc/en/reference/pictures` to `SAGE_ROOT/doc/output/html/en/pictures`.  

Things still to do: 

- do this symlink automatically, say when building the reference manual.  

- possibly modify detex in misc/sagedoc.py to remove, or otherwise modify, ".. image::" directives from command-line help.

- at the moment, the cached version of the docstring (in .sage/sage_notebook/doc) doesn't have the correct URL for the image -- the html is scanned and modified each time it's displayed.  This shouldn't slow things down too much, but should we be saving the correct URL?

- lots of testing.



---

archive/issue_comments_054859.json:
```json
{
    "body": "Okay, the patch now creates the symlink.  I say we don't worry about modifying `detex` right now; once we get this to work, we can think about that issue.",
    "created_at": "2009-08-07T20:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54859",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, the patch now creates the symlink.  I say we don't worry about modifying `detex` right now; once we get this to work, we can think about that issue.



---

archive/issue_comments_054860.json:
```json
{
    "body": "Attachment [trac_6685-first-draft.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-first-draft.patch) by @jhpalmieri created at 2009-08-07 21:07:46",
    "created_at": "2009-08-07T21:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54860",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6685-first-draft.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-first-draft.patch) by @jhpalmieri created at 2009-08-07 21:07:46



---

archive/issue_comments_054861.json:
```json
{
    "body": "Attempt to avoid symbolic links. Apply only this patch.",
    "created_at": "2009-08-07T22:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54861",
    "user": "https://github.com/qed777"
}
```

Attempt to avoid symbolic links. Apply only this patch.



---

archive/issue_comments_054862.json:
```json
{
    "body": "Attachment [trac_6685-ref_pictures_no_symlinks.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-ref_pictures_no_symlinks.patch) by @qed777 created at 2009-08-07 22:35:29\n\nIn an attempt to avoid potential problems with symlinks (cf. #5799, #6614), I've made some changes and attached a patch that\n* Uses the notebook server to map picture URLs.  (If necessary, I can later \"fix\" #4460 to use `/doc/static/pdf` instead of `/pdf`.)\n* Moves the virtual `pictures` directory to `doc/static/reference/`.\n* Drops `http://localhost:8000` from the substitution.\n* Breaks something, probably.\nFollowing the great mathematical tradition of generalization, shall we rename `pictures` to `media`?\n\nI wish Sphinx could already generate collapsible `div`s for a docstring's various sections (`EXAMPLES`, `TESTS`, etc.).",
    "created_at": "2009-08-07T22:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54862",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6685-ref_pictures_no_symlinks.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-ref_pictures_no_symlinks.patch) by @qed777 created at 2009-08-07 22:35:29

In an attempt to avoid potential problems with symlinks (cf. #5799, #6614), I've made some changes and attached a patch that
* Uses the notebook server to map picture URLs.  (If necessary, I can later "fix" #4460 to use `/doc/static/pdf` instead of `/pdf`.)
* Moves the virtual `pictures` directory to `doc/static/reference/`.
* Drops `http://localhost:8000` from the substitution.
* Breaks something, probably.
Following the great mathematical tradition of generalization, shall we rename `pictures` to `media`?

I wish Sphinx could already generate collapsible `div`s for a docstring's various sections (`EXAMPLES`, `TESTS`, etc.).



---

archive/issue_comments_054863.json:
```json
{
    "body": "A note to prospective reviewers and testers:  Upgrade to Sphinx v0.6.x (cf. #6586) to use [absolute image paths](http://sphinx.pocoo.org/rest.html#images).",
    "created_at": "2009-08-07T22:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54863",
    "user": "https://github.com/qed777"
}
```

A note to prospective reviewers and testers:  Upgrade to Sphinx v0.6.x (cf. #6586) to use [absolute image paths](http://sphinx.pocoo.org/rest.html#images).



---

archive/issue_comments_054864.json:
```json
{
    "body": "Looks good to me.  I have no opinion about \"pictures\" vs. \"media\".  Should we change the link in plot.py to `../../pictures/plot/cos_and_triangle.png`, so that it works with Sphinx 0.5.1?",
    "created_at": "2009-08-07T23:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54864",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  I have no opinion about "pictures" vs. "media".  Should we change the link in plot.py to `../../pictures/plot/cos_and_triangle.png`, so that it works with Sphinx 0.5.1?



---

archive/issue_comments_054865.json:
```json
{
    "body": "Should work with Sphinx 0.5.1.  Changed 'pictures' to 'media'.  Apply only this patch.",
    "created_at": "2009-08-08T00:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54865",
    "user": "https://github.com/qed777"
}
```

Should work with Sphinx 0.5.1.  Changed 'pictures' to 'media'.  Apply only this patch.



---

archive/issue_comments_054866.json:
```json
{
    "body": "Attachment [trac_6685-ref_pictures_no_symlinks_v2.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-ref_pictures_no_symlinks_v2.patch) by @qed777 created at 2009-08-08 00:10:11\n\nDone.  Auto-generating and adding all 2D images under `sage/plot/` seems to be less straightforward.",
    "created_at": "2009-08-08T00:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54866",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6685-ref_pictures_no_symlinks_v2.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-ref_pictures_no_symlinks_v2.patch) by @qed777 created at 2009-08-08 00:10:11

Done.  Auto-generating and adding all 2D images under `sage/plot/` seems to be less straightforward.



---

archive/issue_comments_054867.json:
```json
{
    "body": "I'm reviewing this patch and things look very good so far. I do have a couple comments:\n\nFirst, I like \"media\" for the directory, since we can now do video very easily in browsers like Firefox 3.5, so one can imagine having animations and so on in the reference manual.\n\nSecond, I'm not sure how I feel about including the binary file in the patch, and having hg track binary files. I'd rather have a nice way of specifying a way to produce the image. In the example you have in the reference manual, there's a sequence of Sage commands whose purpose is to produce the image we want to show. So can't we...use those commands to produce the image?\n\nPerhaps the goal of this ticket should just be to add *support* for including images in the documentation and we can worry about nice ways to produce those images later.",
    "created_at": "2009-08-26T02:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54867",
    "user": "https://github.com/dandrake"
}
```

I'm reviewing this patch and things look very good so far. I do have a couple comments:

First, I like "media" for the directory, since we can now do video very easily in browsers like Firefox 3.5, so one can imagine having animations and so on in the reference manual.

Second, I'm not sure how I feel about including the binary file in the patch, and having hg track binary files. I'd rather have a nice way of specifying a way to produce the image. In the example you have in the reference manual, there's a sequence of Sage commands whose purpose is to produce the image we want to show. So can't we...use those commands to produce the image?

Perhaps the goal of this ticket should just be to add *support* for including images in the documentation and we can worry about nice ways to produce those images later.



---

archive/issue_comments_054868.json:
```json
{
    "body": "By the way, and for what it's worth, #6694 was first motivated by the desire to interactively produce images for the reference manual.  It is a fun way to explore the many mathematical capabilities of Sage, although evaluating all cells can sometimes severely test a browser.\n\nBut adapting the docbuild and/or doctesting frameworks seems to be a significantly better approach for generating the images in bulk.  Does `sage -t`, when it's not invoked with `-randorder`, keep track of the index of a test cell in a module?  If so, perhaps we can retain any produced images, rename them in a systematic way, and splice appropriate `.. image::` tags into the docstrings.  Since this is invasive, we can make this a separate command, e.g., `sage -imagebuild`, for library authors.  Are regular expressions the safest way to check for and remove or update existing tags?\n\nAn alternative, possibly cleaner way is to extend Sphinx so that it generates and inserts an image dynamically, whenever it finds an `.. autoimage::` directive.  It may be simplest to include as a \"required option\" the precise code to make the image.  This will increase the time it takes to build the manual, unless we cache the figures effectively.  (Sphinx's [doctest extension](http://sphinx.pocoo.org/ext/doctest.html) may or may not help here.)\n\nSome library authors may wish to include a specific set of pictures in the reference manual, in part to showcase their code's abilities.  If a media file is not superfluous, but it takes a long time to generate with Sage, why not include and track it as a binary?  We could put some limits on file sizes or even offer to host them on sage.math and embed them in the manual.\n\nMy chief worry is maintaining the correctness and consistency of any pictures with the code examples.  Adding image diffs to doctesting (with some tolerance) might help, but we would still need to track the binary \"masters.\"  Anyway, this might force contributors to pay attention.",
    "created_at": "2009-08-26T11:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54868",
    "user": "https://github.com/qed777"
}
```

By the way, and for what it's worth, #6694 was first motivated by the desire to interactively produce images for the reference manual.  It is a fun way to explore the many mathematical capabilities of Sage, although evaluating all cells can sometimes severely test a browser.

But adapting the docbuild and/or doctesting frameworks seems to be a significantly better approach for generating the images in bulk.  Does `sage -t`, when it's not invoked with `-randorder`, keep track of the index of a test cell in a module?  If so, perhaps we can retain any produced images, rename them in a systematic way, and splice appropriate `.. image::` tags into the docstrings.  Since this is invasive, we can make this a separate command, e.g., `sage -imagebuild`, for library authors.  Are regular expressions the safest way to check for and remove or update existing tags?

An alternative, possibly cleaner way is to extend Sphinx so that it generates and inserts an image dynamically, whenever it finds an `.. autoimage::` directive.  It may be simplest to include as a "required option" the precise code to make the image.  This will increase the time it takes to build the manual, unless we cache the figures effectively.  (Sphinx's [doctest extension](http://sphinx.pocoo.org/ext/doctest.html) may or may not help here.)

Some library authors may wish to include a specific set of pictures in the reference manual, in part to showcase their code's abilities.  If a media file is not superfluous, but it takes a long time to generate with Sage, why not include and track it as a binary?  We could put some limits on file sizes or even offer to host them on sage.math and embed them in the manual.

My chief worry is maintaining the correctness and consistency of any pictures with the code examples.  Adding image diffs to doctesting (with some tolerance) might help, but we would still need to track the binary "masters."  Anyway, this might force contributors to pay attention.



---

archive/issue_comments_054869.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> Some library authors may wish to include a specific set of pictures in the reference manual, in part to showcase their code's abilities.  If a media file is not superfluous, but it takes a long time to generate with Sage, why not include and track it as a binary?  We could put some limits on file sizes or even offer to host them on sage.math and embed them in the manual.\n\nI'm not terribly opposed to tracking binaries, so in some situation it's the best thing to do, we should do it. The \"image doctest\" idea is one place where we obviously should do this.\n\n> My chief worry is maintaining the correctness and consistency of any pictures with the code examples.  Adding image diffs to doctesting (with some tolerance) might help, but we would still need to track the binary \"masters.\"  Anyway, this might force contributors to pay attention.  \n\nMaintaining correctness and consistency is a major reason why I'd prefer to have autogenerated stuff. If I've learned anything from the Sage doctesting philosophy, it's that you can never rely on people to \"just notice\" bugs and problems. The only thing people notice, it seems, is \"X failures in...\" at the end of a `make test` run!",
    "created_at": "2009-08-27T00:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54869",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:8 mpatel]:
> Some library authors may wish to include a specific set of pictures in the reference manual, in part to showcase their code's abilities.  If a media file is not superfluous, but it takes a long time to generate with Sage, why not include and track it as a binary?  We could put some limits on file sizes or even offer to host them on sage.math and embed them in the manual.

I'm not terribly opposed to tracking binaries, so in some situation it's the best thing to do, we should do it. The "image doctest" idea is one place where we obviously should do this.

> My chief worry is maintaining the correctness and consistency of any pictures with the code examples.  Adding image diffs to doctesting (with some tolerance) might help, but we would still need to track the binary "masters."  Anyway, this might force contributors to pay attention.  

Maintaining correctness and consistency is a major reason why I'd prefer to have autogenerated stuff. If I've learned anything from the Sage doctesting philosophy, it's that you can never rely on people to "just notice" bugs and problems. The only thing people notice, it seems, is "X failures in..." at the end of a `make test` run!



---

archive/issue_comments_054870.json:
```json
{
    "body": "I would note that we already include some binaries: there are pictures in the directory SAGE_ROOT/sage/doc/en/bordeaux_2008 (modpcurve.png and birch.png).\n\nI don't have any strong feelings about the particular picture included in the patch here; it was included as a test case, and I didn't put a lot of thought into finding a place in the reference manual where a picture would help but where that picture couldn't be easily (or quickly) autogenerated.  I certainly have in mind some applications -- triangulations of various topological spaces, to be used in the simplicial complexes code -- where I want to include pictures that can not be produced by Sage.\n\nWould it be better if I tried to find a more natural candidate for a picture?  Or (as ddrake suggested), get rid of the binary and just have a way to include pictures for now?  Then we can have a discussion on sage-devel, or wherever is appropriate, about just how many pictures (and other media) to include, and what criteria to use.\n\nThe idea of remotely hosting media is interesting, but I don't see a way to embed a remotely hosted image in reST: it looks like the image directive needs a path, not a URL.  (I know how to do it in html, certainly, but is there Sphinx/reST code which would let us pass a URL to an image directive?)",
    "created_at": "2009-08-27T02:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54870",
    "user": "https://github.com/jhpalmieri"
}
```

I would note that we already include some binaries: there are pictures in the directory SAGE_ROOT/sage/doc/en/bordeaux_2008 (modpcurve.png and birch.png).

I don't have any strong feelings about the particular picture included in the patch here; it was included as a test case, and I didn't put a lot of thought into finding a place in the reference manual where a picture would help but where that picture couldn't be easily (or quickly) autogenerated.  I certainly have in mind some applications -- triangulations of various topological spaces, to be used in the simplicial complexes code -- where I want to include pictures that can not be produced by Sage.

Would it be better if I tried to find a more natural candidate for a picture?  Or (as ddrake suggested), get rid of the binary and just have a way to include pictures for now?  Then we can have a discussion on sage-devel, or wherever is appropriate, about just how many pictures (and other media) to include, and what criteria to use.

The idea of remotely hosting media is interesting, but I don't see a way to embed a remotely hosted image in reST: it looks like the image directive needs a path, not a URL.  (I know how to do it in html, certainly, but is there Sphinx/reST code which would let us pass a URL to an image directive?)



---

archive/issue_comments_054871.json:
```json
{
    "body": "Attachment [trac_6685-proposal.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-proposal.patch) by @dandrake created at 2009-08-27 02:15:52\n\nLike the \"v2\" patch, but just adds support for including images",
    "created_at": "2009-08-27T02:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54871",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_6685-proposal.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-proposal.patch) by @dandrake created at 2009-08-27 02:15:52

Like the "v2" patch, but just adds support for including images



---

archive/issue_comments_054872.json:
```json
{
    "body": "There's two things going on here: one, the code that allows us to use the \"`.. image::`\" directives and have them work; two, the parts of the patch that actually change some docstrings to include some images. I'm giving this a positive review, and have split the \"v2\" patch into two patches:\n\n* attachment:trac_6685-proposal.patch includes just the parts from attachment:trac_6685-ref_pictures_no_symlinks_v2.patch that actually add the new support for image directives.\n* attachment:trac_6685-usage-examples.patch includes the binary image from the \"v2\" patch, as well as the change to the reference manual to include that image. I also added a second image and a change to a docstring that demonstrates that you can now include images and see them when viewing docstrings in the notebook -- try `plot?` with this patch applied.\n\nMy positive review certainly applies to the \"proposal\" patch and I think the release manager should merge it.\n\nI propose that we *not* merge the usage examples patch and just leave it here so people can see how the image inclusion stuff works. We can hash out elsewhere the details of how to autogenerate images, do image doctests, and so on. Thoughts?",
    "created_at": "2009-08-27T02:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54872",
    "user": "https://github.com/dandrake"
}
```

There's two things going on here: one, the code that allows us to use the "`.. image::`" directives and have them work; two, the parts of the patch that actually change some docstrings to include some images. I'm giving this a positive review, and have split the "v2" patch into two patches:

* attachment:trac_6685-proposal.patch includes just the parts from attachment:trac_6685-ref_pictures_no_symlinks_v2.patch that actually add the new support for image directives.
* attachment:trac_6685-usage-examples.patch includes the binary image from the "v2" patch, as well as the change to the reference manual to include that image. I also added a second image and a change to a docstring that demonstrates that you can now include images and see them when viewing docstrings in the notebook -- try `plot?` with this patch applied.

My positive review certainly applies to the "proposal" patch and I think the release manager should merge it.

I propose that we *not* merge the usage examples patch and just leave it here so people can see how the image inclusion stuff works. We can hash out elsewhere the details of how to autogenerate images, do image doctests, and so on. Thoughts?



---

archive/issue_comments_054873.json:
```json
{
    "body": "Attachment [trac_6685-usage-examples.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-usage-examples.patch) by @dandrake created at 2009-08-27 05:50:04\n\nOops, I didn't see this before.\n\nReplying to [comment:10 jhpalmieri]:\n> I don't have any strong feelings about the particular picture included in the patch here; it was included as a test case, and I didn't put a lot of thought into finding a place in the reference manual where a picture would help but where that picture couldn't be easily (or quickly) autogenerated.  I certainly have in mind some applications -- triangulations of various topological spaces, to be used in the simplicial complexes code -- where I want to include pictures that can not be produced by Sage.\n\nI like this idea, since if Sage can't produce the graphic, we need to track the image file. How about you find one of your applications and put up a patch here (to be applied on top of the \"proposal\" patch), and then we can ignore the usage-examples patch?\n\n> The idea of remotely hosting media is interesting, but I don't see a way to embed a remotely hosted image in reST: it looks like the image directive needs a path, not a URL.  (I know how to do it in html, certainly, but is there Sphinx/reST code which would let us pass a URL to an image directive?)\n\nRemote hosting sounds nice, but I'd like to keep the documentation self-contained, so that one can have everything available while, say, working on a laptop on an airplane. Although I wouldn't mind if a nonessential bit was linked, and something in the text said that the bit won't show up unless you have a network connection. Then one could include, say, a really big video file. Although all of this is moot if we can't figure out how to get the links into the docs! (I certainly don't know how.)",
    "created_at": "2009-08-27T05:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54873",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_6685-usage-examples.patch](tarball://root/attachments/some-uuid/ticket6685/trac_6685-usage-examples.patch) by @dandrake created at 2009-08-27 05:50:04

Oops, I didn't see this before.

Replying to [comment:10 jhpalmieri]:
> I don't have any strong feelings about the particular picture included in the patch here; it was included as a test case, and I didn't put a lot of thought into finding a place in the reference manual where a picture would help but where that picture couldn't be easily (or quickly) autogenerated.  I certainly have in mind some applications -- triangulations of various topological spaces, to be used in the simplicial complexes code -- where I want to include pictures that can not be produced by Sage.

I like this idea, since if Sage can't produce the graphic, we need to track the image file. How about you find one of your applications and put up a patch here (to be applied on top of the "proposal" patch), and then we can ignore the usage-examples patch?

> The idea of remotely hosting media is interesting, but I don't see a way to embed a remotely hosted image in reST: it looks like the image directive needs a path, not a URL.  (I know how to do it in html, certainly, but is there Sphinx/reST code which would let us pass a URL to an image directive?)

Remote hosting sounds nice, but I'd like to keep the documentation self-contained, so that one can have everything available while, say, working on a laptop on an airplane. Although I wouldn't mind if a nonessential bit was linked, and something in the text said that the bit won't show up unless you have a network connection. Then one could include, say, a really big video file. Although all of this is moot if we can't figure out how to get the links into the docs! (I certainly don't know how.)



---

archive/issue_comments_054874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T10:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054875.json:
```json
{
    "body": "Merged `trac_6685-proposal.patch`.\n\n\n\nWhile doctesting with the above patch, I had the following failure:\n\n```\nsage -t -long devel/sage-main/sage/misc/getusage.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/misc/getusage.py\", line 69:\n    sage: get_memory_usage(t)          # amount of memory more than when we defined t.\nExpected:\n    0.0\nGot:\n    0.34375\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_getusage.py\n\t [2.5 s]\n```\n\nThis is the same failure as that reported in #6819. I'm merging patches and testing on sage.math at a time when it has about 3 GB of free RAM out of a total of 120 GB. As far as I can tell, the failure is not due to the above patch. One can doctest the file `sage/misc/getusage.py` with or without the patch and still occasionally gets that failure.",
    "created_at": "2009-08-30T10:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6685-proposal.patch`.



While doctesting with the above patch, I had the following failure:

```
sage -t -long devel/sage-main/sage/misc/getusage.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/misc/getusage.py", line 69:
    sage: get_memory_usage(t)          # amount of memory more than when we defined t.
Expected:
    0.0
Got:
    0.34375
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_getusage.py
	 [2.5 s]
```

This is the same failure as that reported in #6819. I'm merging patches and testing on sage.math at a time when it has about 3 GB of free RAM out of a total of 120 GB. As far as I can tell, the failure is not due to the above patch. One can doctest the file `sage/misc/getusage.py` with or without the patch and still occasionally gets that failure.



---

archive/issue_comments_054876.json:
```json
{
    "body": "Replying to Dan Drake and John Palmieri:\n\nGood points.  Should we inquire about a contributed sage.math repository on sage-devel?  If we cannot or prefer not to embed, we can include links to the supplemental material.  To minimize the possibility of broken links, we could set up pages for different subject areas and point to them.  \n\nTo embed almost anything, use the [raw](http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through) directive:\n\n```\n.. raw:: html\n\n   <img src=\"http://www.sagemath.org/pix/sage_logo_new.png\">\n```\n\nIf this is too permissive, we could extend Sphinx with an `embed` directive, say.",
    "created_at": "2009-08-30T12:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54876",
    "user": "https://github.com/qed777"
}
```

Replying to Dan Drake and John Palmieri:

Good points.  Should we inquire about a contributed sage.math repository on sage-devel?  If we cannot or prefer not to embed, we can include links to the supplemental material.  To minimize the possibility of broken links, we could set up pages for different subject areas and point to them.  

To embed almost anything, use the [raw](http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through) directive:

```
.. raw:: html

   <img src="http://www.sagemath.org/pix/sage_logo_new.png">
```

If this is too permissive, we could extend Sphinx with an `embed` directive, say.



---

archive/issue_comments_054877.json:
```json
{
    "body": "I've opened #6847 for plot automatons.",
    "created_at": "2009-08-30T13:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6685#issuecomment-54877",
    "user": "https://github.com/qed777"
}
```

I've opened #6847 for plot automatons.
