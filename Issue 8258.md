# Issue 8258: get "make documentation" relocation-safe

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2010-02-13 21:47:26

Assignee: mvngu

CC:  jhpalmieri

As of Sage-4.3.2 (and since quite some versions before now), if you newly install Sage from a binary distribution, and type "make" in the SAGE_ROOT directory, then the build process will re-create all of the documentation, although this had been part of the bdist already, and the contents didn't change and will be the same.

To be crystal clear: this ticket is not about detaching the creation of the docs from the make/build process (that is the topic of trac ticket #7943).

This ticket here is about the annoying fact that Sphinx (?) obviously uses mechanisms to detect whether to rebuild the ReST docs or not, that are insufficient in important use cases for Sage!

Another use case is simple relocation (hence the name of the ticket). I just tested it, having completed one (superfluous) make run as described above, then move this entire Sage install to some other directory, type make (the focus *is* on the documentation part here) again --- and it's Groundhog Day again ... (re-building all of this documentation takes on my 2 GHz, 2GB machine more than one and a half hours!)

I guess cloning is "only" just another instance suffering from the same basic problem, i.e. correctly deciding whether the contents of documentation files are outdated and have to be rebuilt --- or not.

Probably one can use some functionalities provided by SCons, e.g. like using MD5 hashes instead of timestamps, or like using a decent database to store the metadata (instead of pickling), to resolve the issue.

(I do think that we need to rewrite ourselves some of the respective parts of Sphinx here. I don't think that would be many lines of code, though, and possibly upstream considers to incorporate these changes.)


---

Comment by hivert created at 2010-02-13 22:06:25

After a cloning, the script `sage-clone` issues a 

```
sage -docbuild --update-mtimes reference html
```

which seems to solve the problem (at least for me) see #7796.

Florent


---

Comment by GeorgSWeber created at 2010-02-14 12:38:08

Hi Florent,

yes, I know that many people already put quite some effort into this, and I know that command

```
sage -docbuild --update-mtimes reference html
```

because on my computer, it more often hangs than not.

Since its introduction, I got used to issue a "CTRL-C" every time after a "sage-clone"; there has been more than one discussion / message thread on sage-devel about that. But since it seems to work fine for at least some other people (including you), I chose not to (re-)open a ticket to revert this behaviour.

Let me say it again, this ticket here is about a slightly different issue. You can test it easily yourself. Just take some Sage install (let's say a Sage 4.3.2 version) of yours, do a "make" in the SAGE_ROOT directory, so the documentation is up to date.

Then just move the Sage install to some different place in your file tree (drag-and-drop from a GUI), i.e. create e.g. a directory "test/" side-by-side to this Sage install, and then move this full Sage tree one level lower in the directory hierarchy, now under "test/". No file date/time stamps updating whatsoever, just a full plain "move". (If you wish, you can issue "./sage" there, and you'll see some message about .pyc files to be relocated.)

Now, issue "make" again in the SAGE_ROOT in its new location, and alas, *all* of the documentation gets built over again.

This latter behaviour clearly exposes some basic design flaw in the way Sphinx seems to store/interpret its metadata; at least in view of common use cases for Sage.
(This "relocation" will happen almost certainly for anyone installing a Sage binary distribution.)

I do think this relocation issue must be fixed. (Of course I also hope, that in the course of doing so, more light is shed on the "sage-clone" issues still left, but for me, that is only a second step, after this first one.)


Cheers, Georg


---

Attachment

Use hashes instead of mtimes to get outdated docs.  Not a patch.


---

Comment by mpatel created at 2010-02-19 08:04:08

I've attached a modified

    `SAGE_LOCAL/lib/python/site-packages/Sphinx-*/sphinx/environment.py`

that uses hashes instead of modification times to `get_outdated_docs`.  Be sure to delete the relevant `environment.pickle` (or all of `SAGE_DOC/output/doctrees`) first.

This may be enough for cloning.  Still to do: Make `builders/html.py` use hashes, too.


---

Comment by mpatel created at 2010-02-19 08:07:29

I'll make a new spkg after we sort out #7448 and #8244.


---

Comment by mpatel created at 2010-02-19 08:49:35

Replying to [comment:3 mpatel]:
> This may be enough for cloning.
To test this, please disable the `update-mtimes` command in `SAGE_ROOT/local/bin/sage-clone`!


---

Comment by hivert created at 2010-02-19 09:00:47

Replying to [comment:4 mpatel]:
> I'll make a new spkg after we sort out #7448 and #8244.

Hi ! I'm close to have what I believe is the final fix for #7448. Is it Ok to just post a patch to `autodoc.py` there ? If I can avoid, I'd rather not learning yet how to build a spkg :-)


---

Comment by mpatel created at 2010-02-19 09:37:51

Sounds good.  I can make a spkg later.


---

Comment by mkoeppe created at 2021-09-10 06:50:50

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2021-09-10 06:50:50

outdated, should close


---

Comment by jhpalmieri created at 2021-09-10 15:54:08

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-10 17:33:19

Resolution: invalid
