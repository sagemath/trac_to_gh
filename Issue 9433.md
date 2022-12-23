# Issue 9433: Put more files under revision control.

archive/issues_009433.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was ddrake kcrisman leif\n\nPut the text files in $SAGE_ROOT, and also the text files in spkg, under revision control.  (See the discussion at the end of #9351.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9433\n\n",
    "created_at": "2010-07-06T00:02:39Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "title": "Put more files under revision control.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9433",
    "user": "jhpalmieri"
}
```
Assignee: tbd

CC:  was ddrake kcrisman leif

Put the text files in $SAGE_ROOT, and also the text files in spkg, under revision control.  (See the discussion at the end of #9351.)

Issue created by migration from https://trac.sagemath.org/ticket/9433





---

archive/issue_comments_090048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T00:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90048",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090049.json:
```json
{
    "body": "I'm marking this as \"needs review\", but consider this patch experimental.",
    "created_at": "2010-07-06T00:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90049",
    "user": "jhpalmieri"
}
```

I'm marking this as "needs review", but consider this patch experimental.



---

archive/issue_comments_090050.json:
```json
{
    "body": "A little explanation: this patch creates a directory \"other-scripts\" in SAGE_ROOT/local/bin.  This new directory contains a brief README.txt and also subdirectories \"root\" and \"spkg\".  \"root\" contains the text files from SAGE_ROOT.  The only one with any changes is README.txt which explains how these files are under revision control.  Similarly, \"spkg\" contains various text files from SAGE_ROOT/spkg, and the only one with any changes is README.txt.",
    "created_at": "2010-07-06T00:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90050",
    "user": "jhpalmieri"
}
```

A little explanation: this patch creates a directory "other-scripts" in SAGE_ROOT/local/bin.  This new directory contains a brief README.txt and also subdirectories "root" and "spkg".  "root" contains the text files from SAGE_ROOT.  The only one with any changes is README.txt which explains how these files are under revision control.  Similarly, "spkg" contains various text files from SAGE_ROOT/spkg, and the only one with any changes is README.txt.



---

archive/issue_comments_090051.json:
```json
{
    "body": "This probably needs to be rebased.  When people are ready to look at it, let me know and I'll see what I can do.",
    "created_at": "2010-07-06T03:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90051",
    "user": "jhpalmieri"
}
```

This probably needs to be rebased.  When people are ready to look at it, let me know and I'll see what I can do.



---

archive/issue_comments_090052.json:
```json
{
    "body": "rebased against 4.5.alpha4 + #9456",
    "created_at": "2010-07-08T15:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90052",
    "user": "jhpalmieri"
}
```

rebased against 4.5.alpha4 + #9456



---

archive/issue_comments_090053.json:
```json
{
    "body": "Attachment\n\nNew approach, after a [discussion on sage-devel](http://groups.google.com/group/sage-devel/t/3ba410046ae641f8): create a new repo at the top level tracking the appropriate files.  I'm attaching a new version of the patch for the scripts repo.  Someone -- the release manager, I guess -- also needs to create the top level repo, because I don't know how to do this in such a way that it can be posted on a ticket.  Here are the instructions:\n\n- move the attached file \"hgignore\" to SAGE_ROOT/.hgignore\n- cd $SAGE_ROOT\n- hg init .\n- hg add .hgignore COPYING.txt README.txt makefile sage sage-python\n- cd spkg\n- hg add README.txt gen_html install pipestatus \n- cd standard\n- hg add README.txt deps libdist_filelist newest_version\n- hg add notes.txt numeric-24.2.txt\n\n(I don't know if we really need these last two files, but this is probably not the ticket for making such decisions.)  Finally, do\n\n- hg commit\n\nWhen you run \"sage -sdist ...\" it should add a tag for the new version of Sage.\n\nThis does not create a new spkg for the files in SAGE_ROOT, since those files have to be in place when you unpack the sage tar file.  But it creates the repository so that people can post patches to the trac server, etc.",
    "created_at": "2010-07-08T22:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90053",
    "user": "jhpalmieri"
}
```

Attachment

New approach, after a [discussion on sage-devel](http://groups.google.com/group/sage-devel/t/3ba410046ae641f8): create a new repo at the top level tracking the appropriate files.  I'm attaching a new version of the patch for the scripts repo.  Someone -- the release manager, I guess -- also needs to create the top level repo, because I don't know how to do this in such a way that it can be posted on a ticket.  Here are the instructions:

- move the attached file "hgignore" to SAGE_ROOT/.hgignore
- cd $SAGE_ROOT
- hg init .
- hg add .hgignore COPYING.txt README.txt makefile sage sage-python
- cd spkg
- hg add README.txt gen_html install pipestatus 
- cd standard
- hg add README.txt deps libdist_filelist newest_version
- hg add notes.txt numeric-24.2.txt

(I don't know if we really need these last two files, but this is probably not the ticket for making such decisions.)  Finally, do

- hg commit

When you run "sage -sdist ..." it should add a tag for the new version of Sage.

This does not create a new spkg for the files in SAGE_ROOT, since those files have to be in place when you unpack the sage tar file.  But it creates the repository so that people can post patches to the trac server, etc.



---

archive/issue_comments_090054.json:
```json
{
    "body": "Looking with my eyes, this looks good.  I don't have time to test right now.  The test would be to take a clean Sage, do the above, then do \"sage -sdist ...\" and make sure that in the sdist the above is all still there.",
    "created_at": "2010-07-08T22:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90054",
    "user": "was"
}
```

Looking with my eyes, this looks good.  I don't have time to test right now.  The test would be to take a clean Sage, do the above, then do "sage -sdist ..." and make sure that in the sdist the above is all still there.



---

archive/issue_comments_090055.json:
```json
{
    "body": "main repo: add \"hg_root\" command to Sage",
    "created_at": "2010-07-09T00:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90055",
    "user": "jhpalmieri"
}
```

main repo: add "hg_root" command to Sage



---

archive/issue_comments_090056.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:5 was]:\n> The test would be to take a clean Sage, do the above, then do \"sage -sdist ...\" and make sure that in the sdist the above is all still there. \n\nThis works for me, but other people should definitely look at it carefully.",
    "created_at": "2010-07-09T04:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90056",
    "user": "jhpalmieri"
}
```

Attachment

Replying to [comment:5 was]:
> The test would be to take a clean Sage, do the above, then do "sage -sdist ..." and make sure that in the sdist the above is all still there. 

This works for me, but other people should definitely look at it carefully.



---

archive/issue_comments_090057.json:
```json
{
    "body": "This probably needs work: how will it work with \"sage -upgrade\"?",
    "created_at": "2010-07-22T04:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90057",
    "user": "jhpalmieri"
}
```

This probably needs work: how will it work with "sage -upgrade"?



---

archive/issue_comments_090058.json:
```json
{
    "body": "Here's a new version of the patch for the scripts repo.  I think this should deal with upgrading: the script \"sage-upgrade\" now runs \"sage --hg branch\" from SAGE_ROOT, and if this fails, it assumes that there is no Mercurial repository and creates it.",
    "created_at": "2010-07-26T20:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90058",
    "user": "jhpalmieri"
}
```

Here's a new version of the patch for the scripts repo.  I think this should deal with upgrading: the script "sage-upgrade" now runs "sage --hg branch" from SAGE_ROOT, and if this fails, it assumes that there is no Mercurial repository and creates it.



---

archive/issue_comments_090059.json:
```json
{
    "body": "This may need to be changed if #9609 is merged: the directions here, and also the modified \"sage-upgrade\" script, refer to files which would be deleted by #9609.",
    "created_at": "2010-07-27T14:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90059",
    "user": "jhpalmieri"
}
```

This may need to be changed if #9609 is merged: the directions here, and also the modified "sage-upgrade" script, refer to files which would be deleted by #9609.



---

archive/issue_comments_090060.json:
```json
{
    "body": "New version, rebased against #9609.",
    "created_at": "2010-07-28T02:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90060",
    "user": "jhpalmieri"
}
```

New version, rebased against #9609.



---

archive/issue_comments_090061.json:
```json
{
    "body": "In sage-sdist, where you have `# copy sage root repo over`, why not just clone the repo? That will take care of copying all the necessary files, and if we add or remove files tracked by the repo, we won't need to mess with sage-sdist. I'm thinking that something like\n\n```\ncd $SAGE_ROOT \nhg clone --pull . DEST_DIR\n```\n\nUsing --pull means that it doesn't use hardlinks in the clone; I *think* there would be no problem with using hardlinks, but it's unlikely to make a big difference. The clone will include a hgrc file that points to where it came from: it would look something like this:\n\n```\n[paths]\ndefault = /home/foo/sage-whatever\n```\n\nWe could simply delete the file, or just leave it, since it would not negatively affect anything (except running `hg pull` from SAGE_ROOT, which you wouldn't do anyway).\n\nSo, all the `cp -p` lines could be just\n\n```\nhg clone --pull . $TMP\nrm $TMP/.hg/hgrc\n```\n\nand files added or removed to the repo would get copied correctly without changing any scripts.",
    "created_at": "2010-07-28T06:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90061",
    "user": "ddrake"
}
```

In sage-sdist, where you have `# copy sage root repo over`, why not just clone the repo? That will take care of copying all the necessary files, and if we add or remove files tracked by the repo, we won't need to mess with sage-sdist. I'm thinking that something like

```
cd $SAGE_ROOT 
hg clone --pull . DEST_DIR
```

Using --pull means that it doesn't use hardlinks in the clone; I *think* there would be no problem with using hardlinks, but it's unlikely to make a big difference. The clone will include a hgrc file that points to where it came from: it would look something like this:

```
[paths]
default = /home/foo/sage-whatever
```

We could simply delete the file, or just leave it, since it would not negatively affect anything (except running `hg pull` from SAGE_ROOT, which you wouldn't do anyway).

So, all the `cp -p` lines could be just

```
hg clone --pull . $TMP
rm $TMP/.hg/hgrc
```

and files added or removed to the repo would get copied correctly without changing any scripts.



---

archive/issue_comments_090062.json:
```json
{
    "body": "new version, using \"hg clone\". apply to scripts repo.",
    "created_at": "2010-07-28T15:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90062",
    "user": "jhpalmieri"
}
```

new version, using "hg clone". apply to scripts repo.



---

archive/issue_comments_090063.json:
```json
{
    "body": "Attachment\n\nnew version, using \"hg clone\". apply to scripts repo.",
    "created_at": "2010-07-28T17:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90063",
    "user": "jhpalmieri"
}
```

Attachment

new version, using "hg clone". apply to scripts repo.



---

archive/issue_comments_090064.json:
```json
{
    "body": "Attachment\n\nNote that if you use \"hg clone ...\" to copy the repo, you have to do it earlier in the process: it apparently needs to be done with an empty directory, so in sage-sdist it is now done right after creating $TMP.",
    "created_at": "2010-07-28T17:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90064",
    "user": "jhpalmieri"
}
```

Attachment

Note that if you use "hg clone ..." to copy the repo, you have to do it earlier in the process: it apparently needs to be done with an empty directory, so in sage-sdist it is now done right after creating $TMP.



---

archive/issue_comments_090065.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-07T06:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90065",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090066.json:
```json
{
    "body": "If I\n\n* Build the forthcoming Sage 4.5.2 (which is just 4.5.2.rc1 + #9226) from source.\n* Follow the steps in the description.\n* `./sage -sdist 4.5.99`\n\n`hg log` in the \"root\" repo now gives\n\n```\nchangeset:   1:0fea58e94942\ntag:         tip\nuser:        Mitesh Patel <qed777@gmail.com>\ndate:        Fri Aug 06 21:40:23 2010 -0700\nsummary:     Added tag 4.5.99 for changeset 4c1f4320f743\n\nchangeset:   0:4c1f4320f743\ntag:         4.5.99\nuser:        Mitesh Patel <qed777@gmail.com>\ndate:        Fri Aug 06 21:33:45 2010 -0700\nsummary:     Initial Sage \"root\" repository\n```\n\n\nThe new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.",
    "created_at": "2010-08-07T06:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90066",
    "user": "mpatel"
}
```

If I

* Build the forthcoming Sage 4.5.2 (which is just 4.5.2.rc1 + #9226) from source.
* Follow the steps in the description.
* `./sage -sdist 4.5.99`

`hg log` in the "root" repo now gives

```
changeset:   1:0fea58e94942
tag:         tip
user:        Mitesh Patel <qed777@gmail.com>
date:        Fri Aug 06 21:40:23 2010 -0700
summary:     Added tag 4.5.99 for changeset 4c1f4320f743

changeset:   0:4c1f4320f743
tag:         4.5.99
user:        Mitesh Patel <qed777@gmail.com>
date:        Fri Aug 06 21:33:45 2010 -0700
summary:     Initial Sage "root" repository
```


The new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.



---

archive/issue_comments_090067.json:
```json
{
    "body": "I also noticed\n\n* `SAGE_ROOT/ipython` and `SAGE_ROOT/sage-README-osx.txt` are missing from the new source and binary distributions.\n* An extra `SAGE_ROOT/sage-python` after unpacking `sage-4.5.99.tar`.",
    "created_at": "2010-08-07T07:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90067",
    "user": "mpatel"
}
```

I also noticed

* `SAGE_ROOT/ipython` and `SAGE_ROOT/sage-README-osx.txt` are missing from the new source and binary distributions.
* An extra `SAGE_ROOT/sage-python` after unpacking `sage-4.5.99.tar`.



---

archive/issue_comments_090068.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-08T22:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90068",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090069.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> The new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.\n\nRight, I didn't do this right.  In the new patch, the root repo is not modified at all by sage-make_devel_packages; instead, sage-sdist clones it, tags it, and commits the new tag, while sage-bdist just clones it.\n\n> I also noticed\n>\n>  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.\n\nThe missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:\n\n```\nif [ \"$UNAME\" = \"Darwin\" ]; then\n    ...\n    cp sage/local/bin/sage-README-osx.txt README.txt\n    ...\n```\n\nPerhaps we can close #6938 if this gets merged?\n\n>  * An extra SAGE_ROOT/sage-python after unpacking sage-4.5.99.tar.\n\nThis was intentional.  Before this, the file sage-python was stored in the scripts repo and then unpacked to the top level.  I'm not sure why this was done, but I wanted to keep the end result as close as possible to what it was before.",
    "created_at": "2010-08-08T22:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90069",
    "user": "jhpalmieri"
}
```

Replying to [comment:15 mpatel]:
> The new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.

Right, I didn't do this right.  In the new patch, the root repo is not modified at all by sage-make_devel_packages; instead, sage-sdist clones it, tags it, and commits the new tag, while sage-bdist just clones it.

> I also noticed
>
>  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.

The missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:

```
if [ "$UNAME" = "Darwin" ]; then
    ...
    cp sage/local/bin/sage-README-osx.txt README.txt
    ...
```

Perhaps we can close #6938 if this gets merged?

>  * An extra SAGE_ROOT/sage-python after unpacking sage-4.5.99.tar.

This was intentional.  Before this, the file sage-python was stored in the scripts repo and then unpacked to the top level.  I'm not sure why this was done, but I wanted to keep the end result as close as possible to what it was before.



---

archive/issue_comments_090070.json:
```json
{
    "body": "> > I also noticed\n> >\n> >  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.\n> \n> The missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:\n> {{{\n> if [ \"$UNAME\" = \"Darwin\" ]; then\n>     ...\n>     cp sage/local/bin/sage-README-osx.txt README.txt\n>     ...\n> }}}\n> Perhaps we can close #6938 if this gets merged?\n\nAs one of the people involved on that ticket, that is fine. The problem is that #6938 does not currently have positive review! So I think that would be necessary first, or something else indicating that the solution proposed there is correct. Maybe 'merge' that ticket at the same time as this one, for whatever it's worth.\n\nSounds like you agree :) In fact, notice that once that is removed, that file will only appear ABOVE the SAGE_ROOT directory, in the place a normal README would occur in a dmg or bundle, so it does work properly (I've tested this numerous times",
    "created_at": "2010-08-09T13:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90070",
    "user": "kcrisman"
}
```

> > I also noticed
> >
> >  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.
> 
> The missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:
> {{{
> if [ "$UNAME" = "Darwin" ]; then
>     ...
>     cp sage/local/bin/sage-README-osx.txt README.txt
>     ...
> }}}
> Perhaps we can close #6938 if this gets merged?

As one of the people involved on that ticket, that is fine. The problem is that #6938 does not currently have positive review! So I think that would be necessary first, or something else indicating that the solution proposed there is correct. Maybe 'merge' that ticket at the same time as this one, for whatever it's worth.

Sounds like you agree :) In fact, notice that once that is removed, that file will only appear ABOVE the SAGE_ROOT directory, in the place a normal README would occur in a dmg or bundle, so it does work properly (I've tested this numerous times



---

archive/issue_comments_090071.json:
```json
{
    "body": "I realized there was another problem with the previous patch: while it would work when upgrading from a Sage build with no root repo, it wouldn't do anything when upgrading a Sage build with an existing root repo.  The new patch constructs a sage_root spkg file, but this file only gets used during upgrading.  So it is installed in the script \"sage-upgrade\", but it does not appear in spkg/standard/deps.",
    "created_at": "2010-08-09T14:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90071",
    "user": "jhpalmieri"
}
```

I realized there was another problem with the previous patch: while it would work when upgrading from a Sage build with no root repo, it wouldn't do anything when upgrading a Sage build with an existing root repo.  The new patch constructs a sage_root spkg file, but this file only gets used during upgrading.  So it is installed in the script "sage-upgrade", but it does not appear in spkg/standard/deps.



---

archive/issue_comments_090072.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-10T02:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90072",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090073.json:
```json
{
    "body": "This still doesn't deal with upgrading very well.  I need to think about how to do this and work on it for a while in a place where I have a better internet connection.  I may have something in a few days.  Meanwhile, if anyone has suggestions for how to deal with upgrades, I would like to hear them.  The issues:\n\n- currently, I don't even know what happens with \"sage -upgrade ...\" if SAGE_ROOT/makefile is changed, for example.  Does anything happen?\n\n- does it matter whether we install the new sage_root spkg before or after the sage_scripts spkg?  The patch here affects the sage-upgrade script, but the new version won't get run during an upgrade anyway.\n\n- is it good enough to just install the new sage_root spkg?  I think it might be, but I might be confused.  Anyway, I think I need time to play with it and test it out.",
    "created_at": "2010-08-10T02:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90073",
    "user": "jhpalmieri"
}
```

This still doesn't deal with upgrading very well.  I need to think about how to do this and work on it for a while in a place where I have a better internet connection.  I may have something in a few days.  Meanwhile, if anyone has suggestions for how to deal with upgrades, I would like to hear them.  The issues:

- currently, I don't even know what happens with "sage -upgrade ..." if SAGE_ROOT/makefile is changed, for example.  Does anything happen?

- does it matter whether we install the new sage_root spkg before or after the sage_scripts spkg?  The patch here affects the sage-upgrade script, but the new version won't get run during an upgrade anyway.

- is it good enough to just install the new sage_root spkg?  I think it might be, but I might be confused.  Anyway, I think I need time to play with it and test it out.



---

archive/issue_comments_090074.json:
```json
{
    "body": "This seems to work for me, with one slight glitch: if I run \"sage -upgrade\" on a copy of sage which does not yet include the root repo, it lists the spkg's to be upgraded and asks me \"do you really want to continue\", then it does some stuff, and then it lists just the root_repo spkg and asks me again if I want to continue.  The issue is that, before it has installed some of the upgraded packages, it doesn't know what to do with the root_repo spkg, so it doesn't get installed the first time through.  I don't see any way around this, but it's a one-time problem.",
    "created_at": "2010-08-11T19:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90074",
    "user": "jhpalmieri"
}
```

This seems to work for me, with one slight glitch: if I run "sage -upgrade" on a copy of sage which does not yet include the root repo, it lists the spkg's to be upgraded and asks me "do you really want to continue", then it does some stuff, and then it lists just the root_repo spkg and asks me again if I want to continue.  The issue is that, before it has installed some of the upgraded packages, it doesn't know what to do with the root_repo spkg, so it doesn't get installed the first time through.  I don't see any way around this, but it's a one-time problem.



---

archive/issue_comments_090075.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-11T19:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90075",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090076.json:
```json
{
    "body": "Ooops, I once had been aware of this ticket, but forgot to cc me...\n\nBefore doing this, can we rename `makefile` to `Makefile`?",
    "created_at": "2010-09-13T08:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90076",
    "user": "leif"
}
```

Ooops, I once had been aware of this ticket, but forgot to cc me...

Before doing this, can we rename `makefile` to `Makefile`?



---

archive/issue_comments_090077.json:
```json
{
    "body": "> Before doing this, can we rename makefile to Makefile?\n\nI have no problems with that.  Are there ever any (good) reasons for using `makefile` instead of `Makefile`?",
    "created_at": "2010-09-13T18:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90077",
    "user": "jhpalmieri"
}
```

> Before doing this, can we rename makefile to Makefile?

I have no problems with that.  Are there ever any (good) reasons for using `makefile` instead of `Makefile`?



---

archive/issue_comments_090078.json:
```json
{
    "body": "Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?\n\nAlso a candidate for renaming (`README.MacOS_X.txt` or alike).\n\nFrom the attached `hg_script`:\n\n```sh\n...\n$hg add .hgignore .hgtags COPYING.txt README.txt makefile sage sage-python\ncd ipython\n$hg add *.py ipythonrc*\n...\n```\n\n\n`sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.",
    "created_at": "2010-09-13T19:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90078",
    "user": "leif"
}
```

Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?

Also a candidate for renaming (`README.MacOS_X.txt` or alike).

From the attached `hg_script`:

```sh
...
$hg add .hgignore .hgtags COPYING.txt README.txt makefile sage sage-python
cd ipython
$hg add *.py ipythonrc*
...
```


`sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.



---

archive/issue_comments_090079.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?\n\nIt shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)\n\n> `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.\n\nThis is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.  Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?",
    "created_at": "2010-09-13T19:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90079",
    "user": "jhpalmieri"
}
```

Replying to [comment:25 leif]:
> Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?

It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)

> `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.

This is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.  Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?



---

archive/issue_comments_090080.json:
```json
{
    "body": "Replying to [comment:26 jhpalmieri]:\n> Replying to [comment:25 leif]:\n> > Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?\n> \n> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)\n\nCorrect.",
    "created_at": "2010-09-13T20:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90080",
    "user": "kcrisman"
}
```

Replying to [comment:26 jhpalmieri]:
> Replying to [comment:25 leif]:
> > Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?
> 
> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)

Correct.



---

archive/issue_comments_090081.json:
```json
{
    "body": "Replying to [comment:26 jhpalmieri]:\n> Replying to [comment:25 leif]:\n> > Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?\n> \n> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)\n\nMissed that.\n\n> > `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.\n> \n> This is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.\n\nThat, too... :/\n\n> Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?\n\nPerhaps...\n\nSorry for the noise.",
    "created_at": "2010-09-13T20:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90081",
    "user": "leif"
}
```

Replying to [comment:26 jhpalmieri]:
> Replying to [comment:25 leif]:
> > Should `sage-README-osx.txt` be ignored (i.e. **not** be under revision control)?
> 
> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the **parent** directory of SAGE_ROOT when you make a dmg file on a Mac.)

Missed that.

> > `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.
> 
> This is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.

That, too... :/

> Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?

Perhaps...

Sorry for the noise.



---

archive/issue_comments_090082.json:
```json
{
    "body": "I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the \"plain\" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).\n\nWhat about release notes (in the top-level directory)?",
    "created_at": "2010-09-16T12:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90082",
    "user": "leif"
}
```

I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).

What about release notes (in the top-level directory)?



---

archive/issue_comments_090083.json:
```json
{
    "body": "Replying to [comment:29 leif]:\n> I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the \"plain\" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).\nThat's a good idea.  Be sure not to hold this one up too long ;)\n> What about release notes (in the top-level directory)?\nThat definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.",
    "created_at": "2010-09-16T13:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90083",
    "user": "kcrisman"
}
```

Replying to [comment:29 leif]:
> I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).
That's a good idea.  Be sure not to hold this one up too long ;)
> What about release notes (in the top-level directory)?
That definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.



---

archive/issue_comments_090084.json:
```json
{
    "body": "Replying to [comment:30 kcrisman]:\n> Replying to [comment:29 leif]:\n> > I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the \"plain\" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).\n> That's a good idea.  Be sure not to hold this one up too long ;)\n\nI don't think adding this needs great effort... We already have `devel/sage/sage/version.py`, which looks like this:\n\n```python\n\"\"\"nodoctests\"\"\"\nversion='4.6.alpha1'; date='2010-09-15'\n```\n\n\n> > What about release notes (in the top-level directory)?\n> That definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though\n\nDoesn't have to be under revision control (i.e. could be in `.hgignore`); it IMHO shouldn't be too lengthy, perhaps just contain the most recent changes (e.g. tickets merged since last final, with a reference to a complete version elsewhere).\n\n> - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.\n\nI think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really \"human\"-(means user-)readable, if we intend that.",
    "created_at": "2010-09-16T13:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90084",
    "user": "leif"
}
```

Replying to [comment:30 kcrisman]:
> Replying to [comment:29 leif]:
> > I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).
> That's a good idea.  Be sure not to hold this one up too long ;)

I don't think adding this needs great effort... We already have `devel/sage/sage/version.py`, which looks like this:

```python
"""nodoctests"""
version='4.6.alpha1'; date='2010-09-15'
```


> > What about release notes (in the top-level directory)?
> That definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though

Doesn't have to be under revision control (i.e. could be in `.hgignore`); it IMHO shouldn't be too lengthy, perhaps just contain the most recent changes (e.g. tickets merged since last final, with a reference to a complete version elsewhere).

> - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.

I think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really "human"-(means user-)readable, if we intend that.



---

archive/issue_comments_090085.json:
```json
{
    "body": "Those ideas seem reasonable, but probably I'm not the one to make the call, since I'm not doing the work.\n\n> > - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.\n> \n> I think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really \"human\"-(means user-)readable, if we intend that.\n\nThe hard part is, but at least in theory the \"known issues\" and \"new features\" sections and things like that are supposed to be human-generated.  mvngu used to make great categorized ones, but likely hasn't had the time lately.  I think they are more human-readable than some I've seen in other programs, though :)",
    "created_at": "2010-09-16T13:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90085",
    "user": "kcrisman"
}
```

Those ideas seem reasonable, but probably I'm not the one to make the call, since I'm not doing the work.

> > - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.
> 
> I think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really "human"-(means user-)readable, if we intend that.

The hard part is, but at least in theory the "known issues" and "new features" sections and things like that are supposed to be human-generated.  mvngu used to make great categorized ones, but likely hasn't had the time lately.  I think they are more human-readable than some I've seen in other programs, though :)



---

archive/issue_comments_090086.json:
```json
{
    "body": "I think that for release notes, we could just have a document which says something like \"Please see http://sagemath.org/mirror/src/changelogs/sage-$VERSION.txt for a list of recent changes.\"  Or we could use the link \"http://sagemath.org/mirror/src/changelogs/\" and then we wouldn't have to update it.  This also provides easy access to older changelogs (which the $VERSION.txt doesn't, and notice it's just a text file -- no links to the parent directory or older changelogs).  Opinions?  We could also add the link \"http://wiki.sagemath.org/ReleaseTours/\", although this hasn't been updated in a while.\n\nI like the generic option better.  But notice that this file won't be auto-generated by \"sage -sdist\" or any other script, and it should probably be under revision control.  This is not the right ticket for adding new files to the top directory, or for modifying existing files, so I think this should go elsewhere.\n\nI also agree that a VERSION.txt file is a good idea.  Since we can automatically generate this, and since it shouldn't be under revision control, I think we can do it on this ticket.  It should just require modifying sage-sdist and sage-bdist.  I'll try towork on this some time soon.",
    "created_at": "2010-09-16T15:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90086",
    "user": "jhpalmieri"
}
```

I think that for release notes, we could just have a document which says something like "Please see http://sagemath.org/mirror/src/changelogs/sage-$VERSION.txt for a list of recent changes."  Or we could use the link "http://sagemath.org/mirror/src/changelogs/" and then we wouldn't have to update it.  This also provides easy access to older changelogs (which the $VERSION.txt doesn't, and notice it's just a text file -- no links to the parent directory or older changelogs).  Opinions?  We could also add the link "http://wiki.sagemath.org/ReleaseTours/", although this hasn't been updated in a while.

I like the generic option better.  But notice that this file won't be auto-generated by "sage -sdist" or any other script, and it should probably be under revision control.  This is not the right ticket for adding new files to the top directory, or for modifying existing files, so I think this should go elsewhere.

I also agree that a VERSION.txt file is a good idea.  Since we can automatically generate this, and since it shouldn't be under revision control, I think we can do it on this ticket.  It should just require modifying sage-sdist and sage-bdist.  I'll try towork on this some time soon.



---

archive/issue_comments_090087.json:
```json
{
    "body": "As a first step, just add `VERSION.txt` to `.hgignore` (here). ;-)\n\nMy intention (perhaps as a developer) regarding \"release notes\" (whatever the file is called) also was *not* to have to search trac or some web page(s) (or query Mercurial) just to see which tickets have recently been merged...\n\nFor users, of course a more abstract description would be better (bugs fixed, packages newly included or upgraded, new features etc.)",
    "created_at": "2010-09-16T15:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90087",
    "user": "leif"
}
```

As a first step, just add `VERSION.txt` to `.hgignore` (here). ;-)

My intention (perhaps as a developer) regarding "release notes" (whatever the file is called) also was *not* to have to search trac or some web page(s) (or query Mercurial) just to see which tickets have recently been merged...

For users, of course a more abstract description would be better (bugs fixed, packages newly included or upgraded, new features etc.)



---

archive/issue_comments_090088.json:
```json
{
    "body": "I've opened up #9922 for adding release notes.  For VERSION.txt, I think we (meaning me) should do the whole thing on this ticket: add it to `.hgignore`, create it in `sage-sdist`, and make sure it gets copied by `sage-bdist`, or else the whole thing should go on another ticket.  If I don't get to it on this one, then I'll open a ticket describing the steps (including adding it to `.hgignore`) -- I don't really see the point in doing one piece of it here.",
    "created_at": "2010-09-16T21:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90088",
    "user": "jhpalmieri"
}
```

I've opened up #9922 for adding release notes.  For VERSION.txt, I think we (meaning me) should do the whole thing on this ticket: add it to `.hgignore`, create it in `sage-sdist`, and make sure it gets copied by `sage-bdist`, or else the whole thing should go on another ticket.  If I don't get to it on this one, then I'll open a ticket describing the steps (including adding it to `.hgignore`) -- I don't really see the point in doing one piece of it here.



---

archive/issue_comments_090089.json:
```json
{
    "body": "Should we update `VERSION.txt` after successful upgrades?  Or maybe have separate fields for the original version (and whether it was a binary) and the current version?  Or even keep a brief upgrade history?",
    "created_at": "2010-09-16T22:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90089",
    "user": "mpatel"
}
```

Should we update `VERSION.txt` after successful upgrades?  Or maybe have separate fields for the original version (and whether it was a binary) and the current version?  Or even keep a brief upgrade history?



---

archive/issue_comments_090090.json:
```json
{
    "body": "I've attached a new version of hg_script which rename 'makefile' to 'Makefile' if it hasn't already been done.  (I thought I also had to modify root-spkg-install, but I don't think I do: once the repo has been made via hg_script, it will have 'Makefile' in it, not 'makefile'.)\n\nI also think mpatel has a good point about VERSION.txt.  I think there are possible design decisions to be made about how to create that file, what should go in it, how to modify it, etc., so I think it should go another ticket.  It could piggy-back on #9922, I think.  I'm going to change the description of that ticket to include this.",
    "created_at": "2010-09-17T01:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90090",
    "user": "jhpalmieri"
}
```

I've attached a new version of hg_script which rename 'makefile' to 'Makefile' if it hasn't already been done.  (I thought I also had to modify root-spkg-install, but I don't think I do: once the repo has been made via hg_script, it will have 'Makefile' in it, not 'makefile'.)

I also think mpatel has a good point about VERSION.txt.  I think there are possible design decisions to be made about how to create that file, what should go in it, how to modify it, etc., so I think it should go another ticket.  It could piggy-back on #9922, I think.  I'm going to change the description of that ticket to include this.



---

archive/issue_comments_090091.json:
```json
{
    "body": "Regarding all this VERSION.txt stuff, I think we should stay on task here. This ticket is about putting existing files under version control. Adding new files \"while we're at it\" is, IMHO, an unnecessary distraction.\n\nOnce SAGE_ROOT is in a Mercurial repo, we can add new files by just creating a ticket, attaching a patch, and getting a positive review. Let's get that repo there first!",
    "created_at": "2010-09-17T03:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90091",
    "user": "ddrake"
}
```

Regarding all this VERSION.txt stuff, I think we should stay on task here. This ticket is about putting existing files under version control. Adding new files "while we're at it" is, IMHO, an unnecessary distraction.

Once SAGE_ROOT is in a Mercurial repo, we can add new files by just creating a ticket, attaching a patch, and getting a positive review. Let's get that repo there first!



---

archive/issue_comments_090092.json:
```json
{
    "body": "fixes problems found by mpatel. apply to scripts repo",
    "created_at": "2010-09-24T17:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90092",
    "user": "jhpalmieri"
}
```

fixes problems found by mpatel. apply to scripts repo



---

archive/issue_comments_090093.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-24T17:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90093",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_090094.json:
```json
{
    "body": "A lot of environment variables should be quoted (`$SAGE_ROOT`, `$TMP`, `$OPT` etc. in most commands).\n\nNeeds rebasing in case #9896 gets merged... (or the other way around)",
    "created_at": "2010-09-24T17:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90094",
    "user": "leif"
}
```

A lot of environment variables should be quoted (`$SAGE_ROOT`, `$TMP`, `$OPT` etc. in most commands).

Needs rebasing in case #9896 gets merged... (or the other way around)



---

archive/issue_comments_090095.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-24T18:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90095",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090096.json:
```json
{
    "body": "`root-spkg-install` also needs work:\n\n```sh\n...\n    if [ -e makefile ]; then\n        cp makefile \"$TARGET\"/Makefile\n    else\n        cp Makefile \"$TARGET\"\n    fi\n    if [ ! -d \"$TARGET/skpg\" ]; then\n        mkdir \"$TARGET/spkg\"\n    fi\n    if [ ! -d \"$TARGET/skpg/standard\" ]; then\n        mkdir \"$TARGET/spkg/standard\"\n...\n```\n\nWe'd better use `-f` than `-e`, `s/skpg/spkg/g`.",
    "created_at": "2010-09-24T18:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90096",
    "user": "leif"
}
```

`root-spkg-install` also needs work:

```sh
...
    if [ -e makefile ]; then
        cp makefile "$TARGET"/Makefile
    else
        cp Makefile "$TARGET"
    fi
    if [ ! -d "$TARGET/skpg" ]; then
        mkdir "$TARGET/spkg"
    fi
    if [ ! -d "$TARGET/skpg/standard" ]; then
        mkdir "$TARGET/spkg/standard"
...
```

We'd better use `-f` than `-e`, `s/skpg/spkg/g`.



---

archive/issue_comments_090097.json:
```json
{
    "body": "P.S.: Instead of\n\n```sh\nif [ ! -d foo ]; then\n    mkdir foo\nfi\n```\n\nyou can simply do\n\n```sh\nmkdir -p foo\n```\n",
    "created_at": "2010-09-24T18:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90097",
    "user": "leif"
}
```

P.S.: Instead of

```sh
if [ ! -d foo ]; then
    mkdir foo
fi
```

you can simply do

```sh
mkdir -p foo
```




---

archive/issue_comments_090098.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T18:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90098",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090099.json:
```json
{
    "body": "Okay, I've fixed root-spkg-install, although I could probably just have one line\n\n```\nmkdir -p \"$TARGET/spkg/standard\"\n```\n\ninstead of two\n\n```\nmkdir -p \"$TARGET/spkg\"\nmkdir -p \"$TARGET/spkg/standard\"\n```\n\nI've also quoted every variable in sight in the scripts patch.",
    "created_at": "2010-09-24T18:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90099",
    "user": "jhpalmieri"
}
```

Okay, I've fixed root-spkg-install, although I could probably just have one line

```
mkdir -p "$TARGET/spkg/standard"
```

instead of two

```
mkdir -p "$TARGET/spkg"
mkdir -p "$TARGET/spkg/standard"
```

I've also quoted every variable in sight in the scripts patch.



---

archive/issue_comments_090100.json:
```json
{
    "body": "Okay, `test -e` shouldn't be a problem with `bash`, only (despite being POSIX) with some Solaris' `/bin/sh`.",
    "created_at": "2010-09-24T19:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90100",
    "user": "leif"
}
```

Okay, `test -e` shouldn't be a problem with `bash`, only (despite being POSIX) with some Solaris' `/bin/sh`.



---

archive/issue_comments_090101.json:
```json
{
    "body": "You don't have to quote variable expansions in normal assignments like `foo=$BAR` or `echo`s, but never mind.\n\nAlso, `test -d foo` is superfluous if you `rm -rf foo`. (\"force\" also implies not raising an error if the directory doesn't exist.)\n\nI'll have to take a closer look regarding (quoting) `$OPT`; this might be wrong in some cases.",
    "created_at": "2010-09-24T19:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90101",
    "user": "leif"
}
```

You don't have to quote variable expansions in normal assignments like `foo=$BAR` or `echo`s, but never mind.

Also, `test -d foo` is superfluous if you `rm -rf foo`. ("force" also implies not raising an error if the directory doesn't exist.)

I'll have to take a closer look regarding (quoting) `$OPT`; this might be wrong in some cases.



---

archive/issue_comments_090102.json:
```json
{
    "body": "There are some quotes missing at the end of `sage-make_devel_packages` (in the newly included part.)\n\nQuoting `$OPT` **currently** works, since it is\n\n```sh\nOPT=\"pPR\"\n```\n\nbut it is a bad idea to omit the dash(es) in `OPT` and prepend it to the expansion.\n\nI.e., it should be\n\n```sh\nOPT=\"-pPR\"\n\n...\n\ncp $OPT ... # NOT quoted\n\n...\n\ncp -L $OPT ... # also NOT quoted\n```\n\n\nAnd I'd suggest renaming `OPT` to `CP_OPTS`.",
    "created_at": "2010-09-24T20:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90102",
    "user": "leif"
}
```

There are some quotes missing at the end of `sage-make_devel_packages` (in the newly included part.)

Quoting `$OPT` **currently** works, since it is

```sh
OPT="pPR"
```

but it is a bad idea to omit the dash(es) in `OPT` and prepend it to the expansion.

I.e., it should be

```sh
OPT="-pPR"

...

cp $OPT ... # NOT quoted

...

cp -L $OPT ... # also NOT quoted
```


And I'd suggest renaming `OPT` to `CP_OPTS`.



---

archive/issue_comments_090103.json:
```json
{
    "body": "> There are some quotes missing at the end of sage-make_devel_packages (in the newly included part.)\n\nOops, I don't know how I missed those.  Anyway, here are new versions.  This changes \"OPT\" to \"CP_OPT\" and includes the hyphen.",
    "created_at": "2010-09-24T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90103",
    "user": "jhpalmieri"
}
```

> There are some quotes missing at the end of sage-make_devel_packages (in the newly included part.)

Oops, I don't know how I missed those.  Anyway, here are new versions.  This changes "OPT" to "CP_OPT" and includes the hyphen.



---

archive/issue_comments_090104.json:
```json
{
    "body": "I'm attaching new versions of `root-spkg-install` and `hg_script` which omit the file `SAGE_ROOT/sage-python`.  I asked about this [on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/13b4632773e3122c#) and no one demanded that it be kept.",
    "created_at": "2010-09-24T22:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90104",
    "user": "jhpalmieri"
}
```

I'm attaching new versions of `root-spkg-install` and `hg_script` which omit the file `SAGE_ROOT/sage-python`.  I asked about this [on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/13b4632773e3122c#) and no one demanded that it be kept.



---

archive/issue_comments_090105.json:
```json
{
    "body": "Attachment\n\nscript to initialize repository. for use by the release manager.",
    "created_at": "2010-09-24T22:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90105",
    "user": "jhpalmieri"
}
```

Attachment

script to initialize repository. for use by the release manager.



---

archive/issue_comments_090106.json:
```json
{
    "body": "Attachment\n\nthe file SAGE_ROOT/spkg/root-spkg-install",
    "created_at": "2010-09-24T22:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90106",
    "user": "jhpalmieri"
}
```

Attachment

the file SAGE_ROOT/spkg/root-spkg-install



---

archive/issue_comments_090107.json:
```json
{
    "body": "Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, and \"sage\" should be \"Sage\" in the messages, the patches and attached files now look fine (with the one exception below).\n\nIn my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least \"consistent\". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)\n\nBut `sage-upgrade` should in any case check that\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log\"\n```\n\nworked before calling `./install`.\n\nI also wonder if this shouldn't (yet) be\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a \\\"$SAGE_ROOT\\\"/spkg/logs/$ROOT_REPO.log\"\n```\n\n(Not tested; the side effects of `pipestatus` are quite weird.)\n\nI haven't yet applied the patches or fully checked the functionality; at least I didn't find errors in the latest attachments. :)\n\nBtw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)",
    "created_at": "2010-09-25T01:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90107",
    "user": "leif"
}
```

Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, and "sage" should be "Sage" in the messages, the patches and attached files now look fine (with the one exception below).

In my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least "consistent". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)

But `sage-upgrade` should in any case check that

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

worked before calling `./install`.

I also wonder if this shouldn't (yet) be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a \"$SAGE_ROOT\"/spkg/logs/$ROOT_REPO.log"
```

(Not tested; the side effects of `pipestatus` are quite weird.)

I haven't yet applied the patches or fully checked the functionality; at least I didn't find errors in the latest attachments. :)

Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)



---

archive/issue_comments_090108.json:
```json
{
    "body": "Replying to [comment:49 leif]:\n> I also wonder if this shouldn't (yet) be\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a \\\"$SAGE_ROOT\\\"/spkg/logs/$ROOT_REPO.log\"\n```\n\n(Not tested; the side effects of `pipestatus` are quite weird.)\n\nThe above doesn't work; it should be\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a $$SAGE_ROOT/spkg/logs/$ROOT_REPO.log\"\n```\n\n(since `SAGE_ROOT` is in the environment anyway).",
    "created_at": "2010-09-25T01:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90108",
    "user": "leif"
}
```

Replying to [comment:49 leif]:
> I also wonder if this shouldn't (yet) be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a \"$SAGE_ROOT\"/spkg/logs/$ROOT_REPO.log"
```

(Not tested; the side effects of `pipestatus` are quite weird.)

The above doesn't work; it should be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $$SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

(since `SAGE_ROOT` is in the environment anyway).



---

archive/issue_comments_090109.json:
```json
{
    "body": "Ouch. Forget my last comment... (i.e. the \"solution\") :D",
    "created_at": "2010-09-25T01:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90109",
    "user": "leif"
}
```

Ouch. Forget my last comment... (i.e. the "solution") :D



---

archive/issue_comments_090110.json:
```json
{
    "body": "Finally :) it should be:\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log\"\n```\n",
    "created_at": "2010-09-25T01:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90110",
    "user": "leif"
}
```

Finally :) it should be:

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log"
```




---

archive/issue_comments_090111.json:
```json
{
    "body": "Replying to [comment:49 leif]:\n> Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, \n\nSince this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.  When Sage works with spaces in the path, if this hasn't been merged yet, I can fix it then.\n\n> and \"sage\" should be \"Sage\" in the messages, \n\nI'll fix that.  You mean messages like \"Error building the sage source code package\" or  \"Error copying sage root repository\", right?\n\n> In my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least \"consistent\". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)\n> \n> But `sage-upgrade` should in any case check that\n\n```sh\n./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log\"\n```\n\n> worked before calling `./install`.\n\nYou're right, I thought about this before, but didn't do it.\n\n> Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)\n\nI'm not sure what you mean by \"base packages\".  The `sage-upgrade` script will certainly upgrade the sage-root spkg. Let's see, the sage-update script will download any new spkg, including any sage-root spkg. Then it gets installed in sage-upgrade before the other spkgs, in case it changes deps or spkg/install.\n\nShould I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...\n\nRe the \"pipestatus\" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)",
    "created_at": "2010-09-25T01:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90111",
    "user": "jhpalmieri"
}
```

Replying to [comment:49 leif]:
> Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, 

Since this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.  When Sage works with spaces in the path, if this hasn't been merged yet, I can fix it then.

> and "sage" should be "Sage" in the messages, 

I'll fix that.  You mean messages like "Error building the sage source code package" or  "Error copying sage root repository", right?

> In my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least "consistent". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)
> 
> But `sage-upgrade` should in any case check that

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

> worked before calling `./install`.

You're right, I thought about this before, but didn't do it.

> Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)

I'm not sure what you mean by "base packages".  The `sage-upgrade` script will certainly upgrade the sage-root spkg. Let's see, the sage-update script will download any new spkg, including any sage-root spkg. Then it gets installed in sage-upgrade before the other spkgs, in case it changes deps or spkg/install.

Should I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...

Re the "pipestatus" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)



---

archive/issue_comments_090112.json:
```json
{
    "body": "Replying to [comment:53 jhpalmieri]:\n> Replying to [comment:49 leif]:\n> > Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, \n> \n> Since this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.\n\nYes, this is (and was meant) a non-issue, I only mentioned it for completeness. ;-)\n\n> > and \"sage\" should be \"Sage\" in the messages, \n> \n> I'll fix that.  You mean messages like \"Error building the sage source code package\" or  \"Error copying sage root repository\", right?\n\nYes.\n\n> > Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)\n> \n> I'm not sure what you mean by \"base packages\".\n\nThe packages /files in `spkg/base`, also referred to by `$(BASE)` in the Makefile (`deps`).\n\n> The `sage-upgrade` script will certainly upgrade the sage-root spkg.\n\nYes, of course. (`sage-update` currently doesn't attempt to upgrade anything from `spkg/base`.)\n\n> Should I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...\n\nI have no opinion on that.\n \n> Re the \"pipestatus\" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)\n\nThis again just referred to *spaces in SAGE_ROOT*. (My last suggestions would work with such.)",
    "created_at": "2010-09-25T01:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90112",
    "user": "leif"
}
```

Replying to [comment:53 jhpalmieri]:
> Replying to [comment:49 leif]:
> > Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, 
> 
> Since this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.

Yes, this is (and was meant) a non-issue, I only mentioned it for completeness. ;-)

> > and "sage" should be "Sage" in the messages, 
> 
> I'll fix that.  You mean messages like "Error building the sage source code package" or  "Error copying sage root repository", right?

Yes.

> > Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)
> 
> I'm not sure what you mean by "base packages".

The packages /files in `spkg/base`, also referred to by `$(BASE)` in the Makefile (`deps`).

> The `sage-upgrade` script will certainly upgrade the sage-root spkg.

Yes, of course. (`sage-update` currently doesn't attempt to upgrade anything from `spkg/base`.)

> Should I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...

I have no opinion on that.
 
> Re the "pipestatus" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)

This again just referred to *spaces in SAGE_ROOT*. (My last suggestions would work with such.)



---

archive/issue_comments_090113.json:
```json
{
    "body": "apply to scripts repo",
    "created_at": "2010-09-25T02:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90113",
    "user": "jhpalmieri"
}
```

apply to scripts repo



---

archive/issue_comments_090114.json:
```json
{
    "body": "Attachment\n\nfor reference only: diff between v2 and v3 patches.",
    "created_at": "2010-09-25T02:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90114",
    "user": "jhpalmieri"
}
```

Attachment

for reference only: diff between v2 and v3 patches.



---

archive/issue_comments_090115.json:
```json
{
    "body": "Attachment\n\nHere are new versions; the only difference with any content (i.e., other than capitalization, I think) is from sage-upgrade:\n\n```diff\n-./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log\"\n+./pipestatus \"sage-spkg $ROOT_REPO 2>&1\" \"tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log\"\n+\n+if [ $? -ne 0 ]; then\n+    echo \"Error installing Sage root repository.\"\n+    exit 1\n+fi\n```\n\n\nI don't know why base packages don't get upgraded.  That's for another ticket.\n\n> Should I create an upgrade path on sage.math?\n\nI meant so that people could test \"sage -upgrade\".   I'll do this pretty soon.",
    "created_at": "2010-09-25T02:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90115",
    "user": "jhpalmieri"
}
```

Attachment

Here are new versions; the only difference with any content (i.e., other than capitalization, I think) is from sage-upgrade:

```diff
-./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
+./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log"
+
+if [ $? -ne 0 ]; then
+    echo "Error installing Sage root repository."
+    exit 1
+fi
```


I don't know why base packages don't get upgraded.  That's for another ticket.

> Should I create an upgrade path on sage.math?

I meant so that people could test "sage -upgrade".   I'll do this pretty soon.



---

archive/issue_comments_090116.json:
```json
{
    "body": "Attachment\n\nrebased for 4.6.1.alpha0",
    "created_at": "2010-11-05T11:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90116",
    "user": "ddrake"
}
```

Attachment

rebased for 4.6.1.alpha0



---

archive/issue_comments_090117.json:
```json
{
    "body": "Attachment\n\nrebased for 4.6.1.alpha0",
    "created_at": "2010-11-05T11:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90117",
    "user": "ddrake"
}
```

Attachment

rebased for 4.6.1.alpha0



---

archive/issue_comments_090118.json:
```json
{
    "body": "I rebased the above two patches. The main Sage repo one is fine, but the scripts patch had rejects on some huge hunks and it took a while to manually put them in. Someone should check over the \"-rebased\" patch and make sure I did everything correctly.",
    "created_at": "2010-11-05T11:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90118",
    "user": "ddrake"
}
```

I rebased the above two patches. The main Sage repo one is fine, but the scripts patch had rejects on some huge hunks and it took a while to manually put them in. Someone should check over the "-rebased" patch and make sure I did everything correctly.



---

archive/issue_comments_090119.json:
```json
{
    "body": "Hi Dan,\n\nThanks for working on this.  The Sage repo patch looks good.  Skimming the scripts patch, the only issue I see with the rebasing is that I think $PKGDIR should be quoted in the following (this is lines 39-41 in sage-sdist):\n\n```\ncp \"$SAGE_ROOT\"/local/bin/sage-spkg $PKGDIR/base/ \ncp \"$SAGE_ROOT\"/local/bin/sage-env  $PKGDIR/base/ \ncp \"$SAGE_ROOT\"/local/bin/sage-make_relative $PKGDIR/base/ \n```\n\nI'll look at this more carefully when I have time.",
    "created_at": "2010-11-05T17:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90119",
    "user": "jhpalmieri"
}
```

Hi Dan,

Thanks for working on this.  The Sage repo patch looks good.  Skimming the scripts patch, the only issue I see with the rebasing is that I think $PKGDIR should be quoted in the following (this is lines 39-41 in sage-sdist):

```
cp "$SAGE_ROOT"/local/bin/sage-spkg $PKGDIR/base/ 
cp "$SAGE_ROOT"/local/bin/sage-env  $PKGDIR/base/ 
cp "$SAGE_ROOT"/local/bin/sage-make_relative $PKGDIR/base/ 
```

I'll look at this more carefully when I have time.



---

archive/issue_comments_090120.json:
```json
{
    "body": "I also found the following corrections to be added to the part of the patch for sage-bdist:\n\n```diff\ndiff -r fa7bc24587ef sage-bdist\n--- a/sage-bdist\tFri Sep 24 19:13:24 2010 -0700\n+++ b/sage-bdist\tFri Nov 05 14:45:36 2010 -0700\n@@ -46,16 +46,15 @@\n if [ $? -ne 0 ]; then\n     echo \"Error copying Sage root repository.\"\n     exit 1\n+fi\n \n rm \"$TMP\"/.hg/hgrc\n echo \"Done copying root repository.\"\n \n-mkdir \"$TMP\"\n-\n cd \"$SAGE_ROOT\"\n \n echo \"Copying files over to tmp directory\"\n-cp -$CP_OPT examples local data \"$TMP\"/\n+cp $CP_OPT examples local data \"$TMP\"/\n \n if [ -d devel/sage-main ]; then\n    echo \"Copying Sage library over\"\n@@ -63,7 +62,6 @@\n    cp -L $CP_OPT devel/sagenb-main \"$TMP\"/devel/sagenb-main\n    cp -L $CP_OPT devel/sage-main \"$TMP\"/devel/sage-main\n    cd \"$TMP\"/devel\n-   cd $TMP/devel\n    ln -s sage-main sage\n    ln -s sagenb-main sagenb\n    cd sage\n```\n\nI'm posting a \"v4\" patch including this and the above change in sage-sdist (quoting \"$PKGDIR\").",
    "created_at": "2010-11-05T21:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90120",
    "user": "jhpalmieri"
}
```

I also found the following corrections to be added to the part of the patch for sage-bdist:

```diff
diff -r fa7bc24587ef sage-bdist
--- a/sage-bdist	Fri Sep 24 19:13:24 2010 -0700
+++ b/sage-bdist	Fri Nov 05 14:45:36 2010 -0700
@@ -46,16 +46,15 @@
 if [ $? -ne 0 ]; then
     echo "Error copying Sage root repository."
     exit 1
+fi
 
 rm "$TMP"/.hg/hgrc
 echo "Done copying root repository."
 
-mkdir "$TMP"
-
 cd "$SAGE_ROOT"
 
 echo "Copying files over to tmp directory"
-cp -$CP_OPT examples local data "$TMP"/
+cp $CP_OPT examples local data "$TMP"/
 
 if [ -d devel/sage-main ]; then
    echo "Copying Sage library over"
@@ -63,7 +62,6 @@
    cp -L $CP_OPT devel/sagenb-main "$TMP"/devel/sagenb-main
    cp -L $CP_OPT devel/sage-main "$TMP"/devel/sage-main
    cd "$TMP"/devel
-   cd $TMP/devel
    ln -s sage-main sage
    ln -s sagenb-main sagenb
    cd sage
```

I'm posting a "v4" patch including this and the above change in sage-sdist (quoting "$PKGDIR").



---

archive/issue_comments_090121.json:
```json
{
    "body": "Attachment\n\nrebased for 4.6.1.alpha0",
    "created_at": "2010-11-05T21:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90121",
    "user": "jhpalmieri"
}
```

Attachment

rebased for 4.6.1.alpha0



---

archive/issue_comments_090122.json:
```json
{
    "body": "I used my rebased patches and 4.6.1.alpha0 to initialize the root repo; I sdisted that and the resulting thing has the correct root repo and built fine -- so everything here seems to work \"going forward\"; I haven't tested any upgrading yet.",
    "created_at": "2010-11-05T22:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90122",
    "user": "ddrake"
}
```

I used my rebased patches and 4.6.1.alpha0 to initialize the root repo; I sdisted that and the resulting thing has the correct root repo and built fine -- so everything here seems to work "going forward"; I haven't tested any upgrading yet.



---

archive/issue_comments_090123.json:
```json
{
    "body": "I'm working on providing an upgrade path (or two) for testing.  I'll post here when I have links.",
    "created_at": "2010-11-05T22:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90123",
    "user": "jhpalmieri"
}
```

I'm working on providing an upgrade path (or two) for testing.  I'll post here when I have links.



---

archive/issue_comments_090124.json:
```json
{
    "body": "Okay for testing upgrading:\n\n```\n./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/\n```\n\nThis first upgrade path is just a vanilla version of 4.6.1.alpha0, plus the new root repo.\n\n```\n./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha1/\n```\n\nThe second upgrade path contains everything from the first one, plus a change to the top-level README.txt file.  This is so we can test upgrading to a plain root repo, then from there to a modified version.  So upgrading to \"...9433.alpha0\" followed by \"...9433.alpha1\" should work, as well as just upgrading straight to \"...9433.alpha1\".\n\nI think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).",
    "created_at": "2010-11-06T00:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90124",
    "user": "jhpalmieri"
}
```

Okay for testing upgrading:

```
./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/
```

This first upgrade path is just a vanilla version of 4.6.1.alpha0, plus the new root repo.

```
./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha1/
```

The second upgrade path contains everything from the first one, plus a change to the top-level README.txt file.  This is so we can test upgrading to a plain root repo, then from there to a modified version.  So upgrading to "...9433.alpha0" followed by "...9433.alpha1" should work, as well as just upgrading straight to "...9433.alpha1".

I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).



---

archive/issue_comments_090125.json:
```json
{
    "body": "One issue: if you upgrade a version of Sage containing \"makefile\", then you end up with both \"makefile\" and \"Makefile\" when you're done.  We can just delete \"$SAGE_ROOT/makefile\" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?",
    "created_at": "2010-11-06T03:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90125",
    "user": "jhpalmieri"
}
```

One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?



---

archive/issue_comments_090126.json:
```json
{
    "body": "Hmmm, this doesn't work for upgrades from older versions (<=4.5), and as you mentioned, behaves strange on newer versions >=4.5.1.\n\nWe **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).\n\nWhat's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.\n\nIf so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our \"real\" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).\n\nBtw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.\n\nThis way we would always do the whole build with the new one, and not switch the version during the installation (after the new scripts spkg has been installed).\n\nAnother reason to keep the repos separate, and not as Robert B. suggested on sage-devel, merge them all into an even larger, monolithic one.\n\n(To avoid trouble with getting overwritten, a script can always clone itself and then `exec` this copy, passing it a parameter such that it knows if it's the clone or the original, similar to `fork()`. We should IMHO do this for a few scripts involved in upgrading and the build process. Therefore, the chain or stack of called rather than `exec`'ed scripts shouldn't be deep.)",
    "created_at": "2010-11-06T04:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90126",
    "user": "leif"
}
```

Hmmm, this doesn't work for upgrades from older versions (<=4.5), and as you mentioned, behaves strange on newer versions >=4.5.1.

We **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).

What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.

If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).

Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.

This way we would always do the whole build with the new one, and not switch the version during the installation (after the new scripts spkg has been installed).

Another reason to keep the repos separate, and not as Robert B. suggested on sage-devel, merge them all into an even larger, monolithic one.

(To avoid trouble with getting overwritten, a script can always clone itself and then `exec` this copy, passing it a parameter such that it knows if it's the clone or the original, similar to `fork()`. We should IMHO do this for a few scripts involved in upgrading and the build process. Therefore, the chain or stack of called rather than `exec`'ed scripts shouldn't be deep.)



---

archive/issue_comments_090127.json:
```json
{
    "body": "Replying to [comment:63 jhpalmieri]:\n> One issue: if you upgrade a version of Sage containing \"makefile\", then you end up with both \"makefile\" and \"Makefile\" when you're done.  We can just delete \"$SAGE_ROOT/makefile\" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?\n\nRename it to `Makefile.old`?",
    "created_at": "2010-11-06T04:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90127",
    "user": "leif"
}
```

Replying to [comment:63 jhpalmieri]:
> One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?

Rename it to `Makefile.old`?



---

archive/issue_comments_090128.json:
```json
{
    "body": "Replying to [comment:62 jhpalmieri]:\n> I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).\n\nAccording to the comment you refer to, this should read *\"upgrade from a version **without** a Sage root repo\"*.",
    "created_at": "2010-11-06T04:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90128",
    "user": "leif"
}
```

Replying to [comment:62 jhpalmieri]:
> I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).

According to the comment you refer to, this should read *"upgrade from a version **without** a Sage root repo"*.



---

archive/issue_comments_090129.json:
```json
{
    "body": "Replying to [comment:64 leif]:\n> We **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).\n\nI'm not sure what \"the rest\" refers to here.\n\n> What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.\n\nOkay, I think I can do that.\n\n> If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our \"real\" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).\n\nI don't want to put it there because in a non-upgrade, it's already installed as part of the download. \n \n> Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.\n\nThat's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?\n\n\nReplying to [comment:65 leif]:\n> Replying to [comment:63 jhpalmieri]:\n> > One issue: if you upgrade a version of Sage containing \"makefile\", then you end up with both \"makefile\" and \"Makefile\" when you're done.  We can just delete \"$SAGE_ROOT/makefile\" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?\n> \n> Rename it to `Makefile.old`?\n\nThat sounds good to me. \n\nReplying to [comment:66 leif]:\n> Replying to [comment:62 jhpalmieri]:\n> > I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).\n> \n> According to the comment you refer to, this should read *\"upgrade from a version **without** a Sage root repo\"*.\n\nYes, that's what I meant to say.  Sorry for any confusion.",
    "created_at": "2010-11-06T06:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90129",
    "user": "jhpalmieri"
}
```

Replying to [comment:64 leif]:
> We **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).

I'm not sure what "the rest" refers to here.

> What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.

Okay, I think I can do that.

> If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).

I don't want to put it there because in a non-upgrade, it's already installed as part of the download. 
 
> Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.

That's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?


Replying to [comment:65 leif]:
> Replying to [comment:63 jhpalmieri]:
> > One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?
> 
> Rename it to `Makefile.old`?

That sounds good to me. 

Replying to [comment:66 leif]:
> Replying to [comment:62 jhpalmieri]:
> > I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).
> 
> According to the comment you refer to, this should read *"upgrade from a version **without** a Sage root repo"*.

Yes, that's what I meant to say.  Sorry for any confusion.



---

archive/issue_comments_090130.json:
```json
{
    "body": "Replying to [comment:67 jhpalmieri]:\n> Replying to [comment:64 leif]:\n> > We **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).\n> \n> I'm not sure what \"the rest\" refers to here.\n\nWell, the files that were previously downloaded (`deps` and `newest_version`, too). But also downloading `sage-env` (and e.g. `sage-spkg`) is not a bad idea.\n\n(I also plan to download `upgrade-notes.txt` and `pre-upgrade-script.sh` first, such that the user (and we) can make an informed choice.)\n\n\n\n> > What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.\n> \n> Okay, I think I can do that.\n> \n> > If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our \"real\" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).\n> \n> I don't want to put it there because in a non-upgrade, it's already installed as part of the download.\n\nWell, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.\n\n`hg incoming <source repo>` returns 1 if there's nothing to pull, 0 if there are changes to pull, other values on errors, so you could change it to:\n\n```sh\n...\nif [ -d \"$TARGET\"/.hg ]; then\n\n    # Merge the repository, rather than overwrite changes that the\n    # user may have made.\n    cd \"$TARGET\"\n    hg ci  # Don't know if we should check in unconditionally,\n           # so perhaps move this below the if-elif-fi.\n    # should check for errors here\n    \n    hg incoming \"$CUR\"  # perhaps redirect output\n    if [ $? -eq 1 ]; then\n        # No changes to pull\n        exit 0\n    elif [ $? -ne 0 ]; then\n        # Some error, report...\n        exit 1\n    fi\n    # $? = 0: Changes to pull...\n    hg pull \"$CUR\"\n    hg merge tip\n    hg ci -m \"Check-in during upgrade of Sage.\"\n    hg update\n    # Add error checks above, too.\n\nelse\n    ...\n```\n\n\n(Or you could add a rule to `deps` that tests its presence / the need to pull first, before calling `sage-spkg`. But if we one day generate `deps`, this would be less optimal.)\n\n\n\n> > Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.\n> \n> That's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?\n\nYes, see above. Once we have this ticket in, it will be easier (or at least safer) to make such changes. :-)\n\n\nP.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)",
    "created_at": "2010-11-06T08:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90130",
    "user": "leif"
}
```

Replying to [comment:67 jhpalmieri]:
> Replying to [comment:64 leif]:
> > We **have to** download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).
> 
> I'm not sure what "the rest" refers to here.

Well, the files that were previously downloaded (`deps` and `newest_version`, too). But also downloading `sage-env` (and e.g. `sage-spkg`) is not a bad idea.

(I also plan to download `upgrade-notes.txt` and `pre-upgrade-script.sh` first, such that the user (and we) can make an informed choice.)



> > What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. *There* we have to make a distinction on if we are upgrading.
> 
> Okay, I think I can do that.
> 
> > If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).
> 
> I don't want to put it there because in a non-upgrade, it's already installed as part of the download.

Well, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.

`hg incoming <source repo>` returns 1 if there's nothing to pull, 0 if there are changes to pull, other values on errors, so you could change it to:

```sh
...
if [ -d "$TARGET"/.hg ]; then

    # Merge the repository, rather than overwrite changes that the
    # user may have made.
    cd "$TARGET"
    hg ci  # Don't know if we should check in unconditionally,
           # so perhaps move this below the if-elif-fi.
    # should check for errors here
    
    hg incoming "$CUR"  # perhaps redirect output
    if [ $? -eq 1 ]; then
        # No changes to pull
        exit 0
    elif [ $? -ne 0 ]; then
        # Some error, report...
        exit 1
    fi
    # $? = 0: Changes to pull...
    hg pull "$CUR"
    hg merge tip
    hg ci -m "Check-in during upgrade of Sage."
    hg update
    # Add error checks above, too.

else
    ...
```


(Or you could add a rule to `deps` that tests its presence / the need to pull first, before calling `sage-spkg`. But if we one day generate `deps`, this would be less optimal.)



> > Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.
> 
> That's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?

Yes, see above. Once we have this ticket in, it will be easier (or at least safer) to make such changes. :-)


P.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)



---

archive/issue_comments_090131.json:
```json
{
    "body": "Replying to [comment:68 leif]:\n\nDownloading these various files in sage-update seems to at least partly defeat the purpose of the new repo, but anyway.\n\n> Replying to [comment:67 jhpalmieri]:\n\n> > I don't want to put it [deps] because in a non-upgrade, it's already installed as part of the download.\n> \n> Well, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.\n\nIf we put it in deps, I guess it gets installed at the end?  I was tempted to make it part of BASE, but then during an upgrade, any changes to the Sage root repo would mean that everything would be rebuilt, which would be annoying.  The only issue is if there is an upgrade to a script like \"pipestatus\" which is in the root repo, is used in the upgrade process, and is not downloaded in sage-update.\n\n> P.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)\n\nI think I'll switch to running \"hg verify\".",
    "created_at": "2010-11-06T15:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90131",
    "user": "jhpalmieri"
}
```

Replying to [comment:68 leif]:

Downloading these various files in sage-update seems to at least partly defeat the purpose of the new repo, but anyway.

> Replying to [comment:67 jhpalmieri]:

> > I don't want to put it [deps] because in a non-upgrade, it's already installed as part of the download.
> 
> Well, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.

If we put it in deps, I guess it gets installed at the end?  I was tempted to make it part of BASE, but then during an upgrade, any changes to the Sage root repo would mean that everything would be rebuilt, which would be annoying.  The only issue is if there is an upgrade to a script like "pipestatus" which is in the root repo, is used in the upgrade process, and is not downloaded in sage-update.

> P.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)

I think I'll switch to running "hg verify".



---

archive/issue_comments_090132.json:
```json
{
    "body": "Okay, here's a new scripts patch (with no changes to sage-update or sage-upgrade), along with new \"deps\" and \"install\".  I've updated the upgrade paths I listed above; I'm adding them to the ticket description.  I am still building Sage 4.4; when that's done, I'll test upgrading it.",
    "created_at": "2010-11-06T17:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90132",
    "user": "jhpalmieri"
}
```

Okay, here's a new scripts patch (with no changes to sage-update or sage-upgrade), along with new "deps" and "install".  I've updated the upgrade paths I listed above; I'm adding them to the ticket description.  I am still building Sage 4.4; when that's done, I'll test upgrading it.



---

archive/issue_comments_090133.json:
```json
{
    "body": "the file SAGE_ROOT/spkg/install",
    "created_at": "2010-11-06T17:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90133",
    "user": "jhpalmieri"
}
```

the file SAGE_ROOT/spkg/install



---

archive/issue_comments_090134.json:
```json
{
    "body": "Attachment\n\ndiff between current install and new one; for reference only",
    "created_at": "2010-11-06T17:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90134",
    "user": "jhpalmieri"
}
```

Attachment

diff between current install and new one; for reference only



---

archive/issue_comments_090135.json:
```json
{
    "body": "Attachment\n\nthe file SAGE_ROOT/spkg/root-spkg-install",
    "created_at": "2010-11-06T17:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90135",
    "user": "jhpalmieri"
}
```

Attachment

the file SAGE_ROOT/spkg/root-spkg-install



---

archive/issue_comments_090136.json:
```json
{
    "body": "Attachment\n\npatch for scripts repo",
    "created_at": "2010-11-06T17:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90136",
    "user": "jhpalmieri"
}
```

Attachment

patch for scripts repo



---

archive/issue_comments_090137.json:
```json
{
    "body": "the file SAGE_ROOT/spkg/standard/deps",
    "created_at": "2010-11-06T18:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90137",
    "user": "jhpalmieri"
}
```

the file SAGE_ROOT/spkg/standard/deps



---

archive/issue_comments_090138.json:
```json
{
    "body": "Attachment\n\ndiff between current deps and new one; for reference only",
    "created_at": "2010-11-06T18:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90138",
    "user": "jhpalmieri"
}
```

Attachment

diff between current deps and new one; for reference only



---

archive/issue_comments_090139.json:
```json
{
    "body": "Attachment\n\nFor what it's worth, I've done the following successfully with the current versions:\n\n- build from scratch (\"./sage -sdist ...\" produced the tar file [http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar](http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar))\n- upgrade from 4.6.1.alpha0, and then upgrade again to the version with a modified root repo\n- same, but started from 4.4\n\nThis was all on sage.math.  I also tested 4.6.1.alpha0 on OS X 10.6 with no problems.\n\nI'm testing \"./sage -bdist ...\", which I forgot to do earlier.  I'm also testing a build from scratch on another platform.",
    "created_at": "2010-11-07T00:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90139",
    "user": "jhpalmieri"
}
```

Attachment

For what it's worth, I've done the following successfully with the current versions:

- build from scratch ("./sage -sdist ..." produced the tar file [http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar](http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar))
- upgrade from 4.6.1.alpha0, and then upgrade again to the version with a modified root repo
- same, but started from 4.4

This was all on sage.math.  I also tested 4.6.1.alpha0 on OS X 10.6 with no problems.

I'm testing "./sage -bdist ...", which I forgot to do earlier.  I'm also testing a build from scratch on another platform.



---

archive/issue_comments_090140.json:
```json
{
    "body": "Is this ticket now really ready for review? (if not, please change status to needs_work).",
    "created_at": "2010-11-07T17:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90140",
    "user": "jdemeyer"
}
```

Is this ticket now really ready for review? (if not, please change status to needs_work).



---

archive/issue_comments_090141.json:
```json
{
    "body": "Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.",
    "created_at": "2010-11-07T17:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90141",
    "user": "jdemeyer"
}
```

Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.



---

archive/issue_comments_090142.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-07T17:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90142",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090143.json:
```json
{
    "body": "Can the people involved in this ticket give their opinion about #10231? (informally, the patch is not yet ready for review)  If you agree with #10231, we need to coordinate this ticket with it.",
    "created_at": "2010-11-07T17:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90143",
    "user": "jdemeyer"
}
```

Can the people involved in this ticket give their opinion about #10231? (informally, the patch is not yet ready for review)  If you agree with #10231, we need to coordinate this ticket with it.



---

archive/issue_comments_090144.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-07T18:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90144",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090145.json:
```json
{
    "body": "Replying to [comment:75 jdemeyer]:\n> Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.\n\nI'm not sure what you mean: the file \"root-spkg-install\" is completely new to this ticket, and is not part of any pre-existing repo.  So there's nothing to patch.  I'm flipping this back to \"needs review\".\n\nRegarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.",
    "created_at": "2010-11-07T18:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90145",
    "user": "jhpalmieri"
}
```

Replying to [comment:75 jdemeyer]:
> Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.

I'm not sure what you mean: the file "root-spkg-install" is completely new to this ticket, and is not part of any pre-existing repo.  So there's nothing to patch.  I'm flipping this back to "needs review".

Regarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.



---

archive/issue_comments_090146.json:
```json
{
    "body": "Replying to [comment:77 jhpalmieri]:\n> Replying to [comment:75 jdemeyer]:\n> > Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.\n> \n> I'm not sure what you mean: the file \"root-spkg-install\" is completely new to this ticket, and is not part of any pre-existing repo.\n\nIn that case, sorry for the noise.",
    "created_at": "2010-11-07T20:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90146",
    "user": "jdemeyer"
}
```

Replying to [comment:77 jhpalmieri]:
> Replying to [comment:75 jdemeyer]:
> > Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.
> 
> I'm not sure what you mean: the file "root-spkg-install" is completely new to this ticket, and is not part of any pre-existing repo.

In that case, sorry for the noise.



---

archive/issue_comments_090147.json:
```json
{
    "body": "Replying to [comment:77 jhpalmieri]:\n> Regarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.\n\nWell, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).\n\nPersonally, I simply don't see the need for merging sage, sage_scripts, extcode, examples,... into one big spkg.  So there is some disagreement on this.  But this disagreement should not stop us from doing something to which most people seemed to agree: not repackaging extcode and examples with every new Sage version (which is exactly what I want to accomplish with #10231).",
    "created_at": "2010-11-07T20:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90147",
    "user": "jdemeyer"
}
```

Replying to [comment:77 jhpalmieri]:
> Regarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.

Well, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).

Personally, I simply don't see the need for merging sage, sage_scripts, extcode, examples,... into one big spkg.  So there is some disagreement on this.  But this disagreement should not stop us from doing something to which most people seemed to agree: not repackaging extcode and examples with every new Sage version (which is exactly what I want to accomplish with #10231).



---

archive/issue_comments_090148.json:
```json
{
    "body": "Replying to [comment:79 jdemeyer]:\n> Well, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).\n\nNot too much discussion of that proposal.  You suggested it, and a few people liked the idea.  On the other hand, a few people made the counter-proposal to merge all of the repositories.  If we end up merging everything, then doing #10231 first will make more work: whatever is involved in that, and then the merge, as opposed to just the merge.  So I'd like to see more of a consensus about which direction to go before putting much effort into #10231.\n\nThis ticket seems like a separate issue, and regardless of everything else, the Sage root repo should remain separate from the others, because it should already be installed when you unpack the Sage tar ball.  Perhaps its role should increase, including files like sage-env and sage-spkg, but that's for another ticket.  I hope this ticket can get a positive review soon, and then if anyone feels like working on #10231 (or on a possible merge of the repos), they can base their work on this ticket and other tickets which touch sage-sdist and related files.",
    "created_at": "2010-11-07T23:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90148",
    "user": "jhpalmieri"
}
```

Replying to [comment:79 jdemeyer]:
> Well, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).

Not too much discussion of that proposal.  You suggested it, and a few people liked the idea.  On the other hand, a few people made the counter-proposal to merge all of the repositories.  If we end up merging everything, then doing #10231 first will make more work: whatever is involved in that, and then the merge, as opposed to just the merge.  So I'd like to see more of a consensus about which direction to go before putting much effort into #10231.

This ticket seems like a separate issue, and regardless of everything else, the Sage root repo should remain separate from the others, because it should already be installed when you unpack the Sage tar ball.  Perhaps its role should increase, including files like sage-env and sage-spkg, but that's for another ticket.  I hope this ticket can get a positive review soon, and then if anyone feels like working on #10231 (or on a possible merge of the repos), they can base their work on this ticket and other tickets which touch sage-sdist and related files.



---

archive/issue_comments_090149.json:
```json
{
    "body": "Replying to [comment:62 jhpalmieri]:\n> Okay for testing upgrading:\n> {{{\n> ./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/\n> }}}\n\nI've tried twice with 4.6 using the above command, and despite the upgrade appearing to work, I get this when I start Sage:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from implicit_surface import ImplicitSurface\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from implicit_surface import ImplicitSurface\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from interpolators import polygon_spline, complex_cubic_spline\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from interpolators import polygon_spline, complex_cubic_spline\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility\n  from hmm  import DiscreteHiddenMarkovModel\n/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility\n  from hmm  import DiscreteHiddenMarkovModel\nsage: \n```\n",
    "created_at": "2010-11-09T01:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90149",
    "user": "ddrake"
}
```

Replying to [comment:62 jhpalmieri]:
> Okay for testing upgrading:
> {{{
> ./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/
> }}}

I've tried twice with 4.6 using the above command, and despite the upgrade appearing to work, I get this when I start Sage:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
sage: 
```




---

archive/issue_comments_090150.json:
```json
{
    "body": "Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.",
    "created_at": "2010-11-09T01:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90150",
    "user": "kcrisman"
}
```

Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.



---

archive/issue_comments_090151.json:
```json
{
    "body": "Replying to [comment:82 kcrisman]:\n> Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.\n\nThat fixed it! Thanks. The first upgrade works fine now; I'm testing the second.",
    "created_at": "2010-11-09T02:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90151",
    "user": "ddrake"
}
```

Replying to [comment:82 kcrisman]:
> Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.

That fixed it! Thanks. The first upgrade works fine now; I'm testing the second.



---

archive/issue_comments_090152.json:
```json
{
    "body": "Replying to [comment:62 jhpalmieri]:\n> Okay for testing upgrading:\n\nI started with 4.6, and both upgrade paths work fine: first to \"9433.alpha0\", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.",
    "created_at": "2010-11-10T01:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90152",
    "user": "ddrake"
}
```

Replying to [comment:62 jhpalmieri]:
> Okay for testing upgrading:

I started with 4.6, and both upgrade paths work fine: first to "9433.alpha0", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.



---

archive/issue_comments_090153.json:
```json
{
    "body": "Replying to [comment:84 ddrake]:\n> Replying to [comment:62 jhpalmieri]:\n> > Okay for testing upgrading:\n> \n> I started with 4.6, and both upgrade paths work fine: first to \"9433.alpha0\", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.\n\nBoth upgrade paths also work when upgrading from 4.3.5. (I'm using 64-bit Ubuntu 10.04.)",
    "created_at": "2010-11-10T07:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90153",
    "user": "ddrake"
}
```

Replying to [comment:84 ddrake]:
> Replying to [comment:62 jhpalmieri]:
> > Okay for testing upgrading:
> 
> I started with 4.6, and both upgrade paths work fine: first to "9433.alpha0", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.

Both upgrade paths also work when upgrading from 4.3.5. (I'm using 64-bit Ubuntu 10.04.)



---

archive/issue_comments_090154.json:
```json
{
    "body": "I just added \"VERSION.txt\" to the .hgignore file, for compatibility with #9434.",
    "created_at": "2010-11-11T21:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90154",
    "user": "jhpalmieri"
}
```

I just added "VERSION.txt" to the .hgignore file, for compatibility with #9434.



---

archive/issue_comments_090155.json:
```json
{
    "body": "Attachment\n\nUpdated spkg/install",
    "created_at": "2011-01-13T07:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90155",
    "user": "vbraun"
}
```

Attachment

Updated spkg/install



---

archive/issue_comments_090156.json:
```json
{
    "body": "Updated spkg/standard/deps",
    "created_at": "2011-01-13T07:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90156",
    "user": "vbraun"
}
```

Updated spkg/standard/deps



---

archive/issue_comments_090157.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T07:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90157",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090158.json:
```json
{
    "body": "Attachment\n\nAfter some rediffing I built it successfully on top of Sage-4.6.1.rc1 (identical to the Sage-4.6.1 release) with the following updated files:\n\n* `trac_9433-scripts.v5.patch` -> `trac_9433-scripts.v5.2.patch`\n* `install` -> `install.2`\n* `deps` -> `deps.2`\n\nI've changed the main ticket documentation accordingly. \n\nFor reference, here is a list of files in the root repository:\n\n```\n[vbraun@volker-two sage-4.6.1.vb2]$ hg st --all | grep -v '^I'\nC .hgignore\nC .hgtags\nC COPYING.txt\nC Makefile\nC README.txt\nC ipython/ipy_profile_sh.py\nC ipython/ipy_user_conf.py\nC ipython/ipythonrc\nC ipython/ipythonrc-math\nC ipython/ipythonrc-numeric\nC ipython/ipythonrc-physics\nC ipython/ipythonrc-pysh\nC ipython/ipythonrc-scipy\nC ipython/ipythonrc-tutorial\nC sage\nC spkg/README.txt\nC spkg/gen_html\nC spkg/install\nC spkg/pipestatus\nC spkg/root-spkg-install\nC spkg/standard/README.txt\nC spkg/standard/deps\nC spkg/standard/libdist_filelist\nC spkg/standard/newest_version\n```\n\n\nReally, any kind of root repository would be better than the caveman technology we have in place right now. I read through all the scripts and they do make sense to me. I built my private release using `sage -sdist <version>` and it compiled fine. You guys put a lot of effort into this ticket to make sure that nothing breaks, and I think it really is the time to integrate this with Sage. \n\nPositive review.\n\nJeroen, can you plug this into 4.6.2.alpha as soon as possible to give it as much exposure as possible?",
    "created_at": "2011-01-13T07:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90158",
    "user": "vbraun"
}
```

Attachment

After some rediffing I built it successfully on top of Sage-4.6.1.rc1 (identical to the Sage-4.6.1 release) with the following updated files:

* `trac_9433-scripts.v5.patch` -> `trac_9433-scripts.v5.2.patch`
* `install` -> `install.2`
* `deps` -> `deps.2`

I've changed the main ticket documentation accordingly. 

For reference, here is a list of files in the root repository:

```
[vbraun@volker-two sage-4.6.1.vb2]$ hg st --all | grep -v '^I'
C .hgignore
C .hgtags
C COPYING.txt
C Makefile
C README.txt
C ipython/ipy_profile_sh.py
C ipython/ipy_user_conf.py
C ipython/ipythonrc
C ipython/ipythonrc-math
C ipython/ipythonrc-numeric
C ipython/ipythonrc-physics
C ipython/ipythonrc-pysh
C ipython/ipythonrc-scipy
C ipython/ipythonrc-tutorial
C sage
C spkg/README.txt
C spkg/gen_html
C spkg/install
C spkg/pipestatus
C spkg/root-spkg-install
C spkg/standard/README.txt
C spkg/standard/deps
C spkg/standard/libdist_filelist
C spkg/standard/newest_version
```


Really, any kind of root repository would be better than the caveman technology we have in place right now. I read through all the scripts and they do make sense to me. I built my private release using `sage -sdist <version>` and it compiled fine. You guys put a lot of effort into this ticket to make sure that nothing breaks, and I think it really is the time to integrate this with Sage. 

Positive review.

Jeroen, can you plug this into 4.6.2.alpha as soon as possible to give it as much exposure as possible?



---

archive/issue_comments_090159.json:
```json
{
    "body": "Why do we need a `sage_root.spkg`?  I don't see a reason for a \"root repo\" to ever exist in tarball form.",
    "created_at": "2011-01-19T08:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90159",
    "user": "jdemeyer"
}
```

Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.



---

archive/issue_comments_090160.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-01-19T08:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90160",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_090161.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-19T09:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90161",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_090162.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-01-19T09:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90162",
    "user": "jdemeyer"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_090163.json:
```json
{
    "body": "If we do this, we really should also take care of the following **duplicate** files (files both in sage_scripts and in another repo):\n\n```\nREADME.txt\nspkg/install\nspkg/base/sage-spkg\nspkg/base/sage-env\nspkg/base/sage-make_relative\nspkg/base/sage-check-64 (added by the not-yet-merged #10303)\n```\n\n\nAlso, I think we should get rid of the `spkg/base` repo and merge it with the new root repo.",
    "created_at": "2011-01-19T09:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90163",
    "user": "jdemeyer"
}
```

If we do this, we really should also take care of the following **duplicate** files (files both in sage_scripts and in another repo):

```
README.txt
spkg/install
spkg/base/sage-spkg
spkg/base/sage-env
spkg/base/sage-make_relative
spkg/base/sage-check-64 (added by the not-yet-merged #10303)
```


Also, I think we should get rid of the `spkg/base` repo and merge it with the new root repo.



---

archive/issue_comments_090164.json:
```json
{
    "body": "Replying to [comment:88 jdemeyer]:\n> Why do we need a `sage_root.spkg`?  I don't see a reason for a \"root repo\" to ever exist in tarball form.\n\nThe way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade. Am I missing something?\n\nI agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.\n\nI'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.\n\nIf you agree with this then I'll make a followup ticket...",
    "created_at": "2011-01-19T17:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90164",
    "user": "vbraun"
}
```

Replying to [comment:88 jdemeyer]:
> Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.

The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade. Am I missing something?

I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.

I'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.

If you agree with this then I'll make a followup ticket...



---

archive/issue_comments_090165.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T17:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90165",
    "user": "vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090166.json:
```json
{
    "body": "Replying to [comment:92 vbraun]:\n> Replying to [comment:88 jdemeyer]:\n> > Why do we need a `sage_root.spkg`?  I don't see a reason for a \"root repo\" to ever exist in tarball form.\n> \n> The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.\nI have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...\n\n> I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.\nPersonally, I would rather like to clean this up as part of *this* ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.\n\n> I'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.\n> \n> If you agree with this then I'll make a followup ticket...\nSame answer as before: I prefer to do it in *this* ticket.",
    "created_at": "2011-01-19T20:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90166",
    "user": "jdemeyer"
}
```

Replying to [comment:92 vbraun]:
> Replying to [comment:88 jdemeyer]:
> > Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.
> 
> The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.
I have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...

> I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.
Personally, I would rather like to clean this up as part of *this* ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.

> I'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.
> 
> If you agree with this then I'll make a followup ticket...
Same answer as before: I prefer to do it in *this* ticket.



---

archive/issue_comments_090167.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-19T20:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90167",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090168.json:
```json
{
    "body": "Replying to [comment:93 jdemeyer]:\n> Replying to [comment:92 vbraun]:\n> > Replying to [comment:88 jdemeyer]:\n> > > Why do we need a `sage_root.spkg`?  I don't see a reason for a \"root repo\" to ever exist in tarball form.\n> > \n> > The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.\n> I have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...\n\nYes, that's the reason for its existence.\n\n> > I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.\n> Personally, I would rather like to clean this up as part of *this* ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.\n\nI think I don't understand. Once there is a SAGE_ROOT repo, then any follow-up ticket can just have a patch which needs to be applied to that repo, as opposed to manually patching `spkg/install` or `Makefile` or whatever. \n\nFor the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.\n\n(I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)",
    "created_at": "2011-01-19T20:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90168",
    "user": "jhpalmieri"
}
```

Replying to [comment:93 jdemeyer]:
> Replying to [comment:92 vbraun]:
> > Replying to [comment:88 jdemeyer]:
> > > Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.
> > 
> > The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.
> I have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...

Yes, that's the reason for its existence.

> > I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.
> Personally, I would rather like to clean this up as part of *this* ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.

I think I don't understand. Once there is a SAGE_ROOT repo, then any follow-up ticket can just have a patch which needs to be applied to that repo, as opposed to manually patching `spkg/install` or `Makefile` or whatever. 

For the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.

(I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)



---

archive/issue_comments_090169.json:
```json
{
    "body": "I'm with John here: Its easy to generate a patch that adds a new file to the `sage_root` repository. You don't have to do anything else for updates, the change will automatically make it into the next `sage_root` package. No more manually digging around to make a new source distribution :-)",
    "created_at": "2011-01-19T20:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90169",
    "user": "vbraun"
}
```

I'm with John here: Its easy to generate a patch that adds a new file to the `sage_root` repository. You don't have to do anything else for updates, the change will automatically make it into the next `sage_root` package. No more manually digging around to make a new source distribution :-)



---

archive/issue_comments_090170.json:
```json
{
    "body": "> For the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.\nAnd indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.\n\nI'd also like to put in a plug for sage-README-osx.txt finally being removed from $SAGE_ROOT. Apparently #6938 never got 'merged'...> (I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)",
    "created_at": "2011-01-19T20:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90170",
    "user": "kcrisman"
}
```

> For the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.
And indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.

I'd also like to put in a plug for sage-README-osx.txt finally being removed from $SAGE_ROOT. Apparently #6938 never got 'merged'...> (I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)



---

archive/issue_comments_090171.json:
```json
{
    "body": "Replying to [comment:96 kcrisman]:\n> And indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.\n\nIn general, I completely agree with your sentiment: too many times a patch has not been finished because it was not the \"optimal\" solution.  However, this only applies if the halfway-implemented patch makes the situation better.\n\nFor this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.  The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) and I'm afraid the current patch on this ticket will make it only worse.\n\nThis is not a ticket I want to \"rush\" into Sage.",
    "created_at": "2011-01-19T21:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90171",
    "user": "jdemeyer"
}
```

Replying to [comment:96 kcrisman]:
> And indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.

In general, I completely agree with your sentiment: too many times a patch has not been finished because it was not the "optimal" solution.  However, this only applies if the halfway-implemented patch makes the situation better.

For this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.  The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) and I'm afraid the current patch on this ticket will make it only worse.

This is not a ticket I want to "rush" into Sage.



---

archive/issue_comments_090172.json:
```json
{
    "body": "Replying to [comment:97 jdemeyer]:\n> This is not a ticket I want to \"rush\" into Sage.\n\nThis ticket has been worked on for 7 months and has almost 100 comments ;-)\n\nAnd every time I want to change something on this ticket I need half a day to rebuild sage, manually make half a dozen changes, test the source distribution. \n\nI can make the changes you wanted in comment:91 but there are a bunch of other files I want to move to the `sage_root` repository as well. Some of them might need some discussion on sage-devel first. How many more months should we wait until the main makefile is under revision control?",
    "created_at": "2011-01-19T21:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90172",
    "user": "vbraun"
}
```

Replying to [comment:97 jdemeyer]:
> This is not a ticket I want to "rush" into Sage.

This ticket has been worked on for 7 months and has almost 100 comments ;-)

And every time I want to change something on this ticket I need half a day to rebuild sage, manually make half a dozen changes, test the source distribution. 

I can make the changes you wanted in comment:91 but there are a bunch of other files I want to move to the `sage_root` repository as well. Some of them might need some discussion on sage-devel first. How many more months should we wait until the main makefile is under revision control?



---

archive/issue_comments_090173.json:
```json
{
    "body": "Replying to [comment:97 jdemeyer]:\n> For this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.\n\nIn what way is the SAGE_ROOT repo \"halfway-implemented\"? With these scripts and patches, the repo will exist and work for upgrades and new builds.\n\n> The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) \n\nMaybe you can manage -- but there's plenty of evidence that other release managers can't. Changing files in SAGE_ROOT currently takes a long time and is an extremely brittle process; why continue in this way?\n\nAnd even if there's no trouble actually changing files, we still have no version control for our basic makefile, README, and executable script. The only way to track changes is to download tarballs, unpack them, and compare files. Think about it: neither the basic file with which we build Sage (the makefile) nor the basic file with which one runs Sage (SAGE_ROOT/sage) are under any version control! That is crazy. Imagine if Firefox shipped with their \"firefox\" script not under version control.\n\n> and I'm afraid the current patch on this ticket will make it only worse.\n\nRight now to change the README:\n\n* make a backup copy\n* make your changes\n* manually run `diff -u` to produce a patch\n* upload *both* the new README and the patch to a ticket\n* upon positive review, hope that the release manager replaces the README file correctly and does `sage -sdist` in the right directory\n\nWith a SAGE_ROOT repo:\n\n* use the same procedure that one uses in the Sage library to produce a patch.\n* release manager uses same procedure as for the Sage library to merge the patch.\n\nPerhaps it's only me, but the current situation seems far worse.\n\nPlease, let's create the SAGE_ROOT repo and argue about merging repos after they actually exist.",
    "created_at": "2011-01-20T04:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90173",
    "user": "ddrake"
}
```

Replying to [comment:97 jdemeyer]:
> For this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.

In what way is the SAGE_ROOT repo "halfway-implemented"? With these scripts and patches, the repo will exist and work for upgrades and new builds.

> The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) 

Maybe you can manage -- but there's plenty of evidence that other release managers can't. Changing files in SAGE_ROOT currently takes a long time and is an extremely brittle process; why continue in this way?

And even if there's no trouble actually changing files, we still have no version control for our basic makefile, README, and executable script. The only way to track changes is to download tarballs, unpack them, and compare files. Think about it: neither the basic file with which we build Sage (the makefile) nor the basic file with which one runs Sage (SAGE_ROOT/sage) are under any version control! That is crazy. Imagine if Firefox shipped with their "firefox" script not under version control.

> and I'm afraid the current patch on this ticket will make it only worse.

Right now to change the README:

* make a backup copy
* make your changes
* manually run `diff -u` to produce a patch
* upload *both* the new README and the patch to a ticket
* upon positive review, hope that the release manager replaces the README file correctly and does `sage -sdist` in the right directory

With a SAGE_ROOT repo:

* use the same procedure that one uses in the Sage library to produce a patch.
* release manager uses same procedure as for the Sage library to merge the patch.

Perhaps it's only me, but the current situation seems far worse.

Please, let's create the SAGE_ROOT repo and argue about merging repos after they actually exist.



---

archive/issue_comments_090174.json:
```json
{
    "body": "Replying to [comment:99 ddrake]:\n>   * release manager uses same procedure as for the Sage library to merge the patch.\n\nWrong, because the `README` is actually already in a different repository, namely `sage_scripts`.  This is the issue of duplicate files that I mentioned above.",
    "created_at": "2011-01-20T08:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90174",
    "user": "jdemeyer"
}
```

Replying to [comment:99 ddrake]:
>   * release manager uses same procedure as for the Sage library to merge the patch.

Wrong, because the `README` is actually already in a different repository, namely `sage_scripts`.  This is the issue of duplicate files that I mentioned above.



---

archive/issue_comments_090175.json:
```json
{
    "body": "After applying the patches here, README.txt will be in the SAGE_ROOT repo, not the scripts repo.  The full list of files which will be tracked:\n\n -.hgignore .hgtags COPYING.txt README.txt Makefile sage\n- in the ipython directory: *.py, ipythonrc*\n- in the spkg directory: README.txt gen_html install pipestatus root-spkg-install\n- in the spkg/standard directory: README.txt deps libdist_filelist newest_version",
    "created_at": "2011-01-20T15:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90175",
    "user": "jhpalmieri"
}
```

After applying the patches here, README.txt will be in the SAGE_ROOT repo, not the scripts repo.  The full list of files which will be tracked:

 -.hgignore .hgtags COPYING.txt README.txt Makefile sage
- in the ipython directory: *.py, ipythonrc*
- in the spkg directory: README.txt gen_html install pipestatus root-spkg-install
- in the spkg/standard directory: README.txt deps libdist_filelist newest_version



---

archive/issue_comments_090176.json:
```json
{
    "body": "The `SAGE_ROOT/ipython` directory is **created** during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.",
    "created_at": "2011-01-20T16:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90176",
    "user": "jdemeyer"
}
```

The `SAGE_ROOT/ipython` directory is **created** during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.



---

archive/issue_comments_090177.json:
```json
{
    "body": "What's the reason for removing the quoting of `SAGE_ROOT` in `sage-spkg-install`?",
    "created_at": "2011-01-20T16:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90177",
    "user": "jdemeyer"
}
```

What's the reason for removing the quoting of `SAGE_ROOT` in `sage-spkg-install`?



---

archive/issue_comments_090178.json:
```json
{
    "body": "Replying to [comment:102 jdemeyer]:\n> The `SAGE_ROOT/ipython` directory is **created** during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.\n\nIt's just copied from whatever was there before.  Why not track those files in a repository?  Otherwise they're not tracked anywhere: what if we want to change any of them?  Also, if you decide to not include them in the repo, then you'll need to work on the scripts patch: put back the parts (in sage-sdist for example) which create those files.\n\n> What's the reason for removing the quoting of SAGE_ROOT in sage-spkg-install?\n\nThat was presumably just a mistake.",
    "created_at": "2011-01-20T16:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90178",
    "user": "jhpalmieri"
}
```

Replying to [comment:102 jdemeyer]:
> The `SAGE_ROOT/ipython` directory is **created** during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.

It's just copied from whatever was there before.  Why not track those files in a repository?  Otherwise they're not tracked anywhere: what if we want to change any of them?  Also, if you decide to not include them in the repo, then you'll need to work on the scripts patch: put back the parts (in sage-sdist for example) which create those files.

> What's the reason for removing the quoting of SAGE_ROOT in sage-spkg-install?

That was presumably just a mistake.



---

archive/issue_comments_090179.json:
```json
{
    "body": "The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.\n\nI'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:\n\n```\n[vbraun@volker-two ~]$ x=\"a b\"\n[vbraun@volker-two ~]$ y=$x/c\n[vbraun@volker-two ~]$ echo $y\na b/c\n```\n",
    "created_at": "2011-01-20T16:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90179",
    "user": "vbraun"
}
```

The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.

I'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:

```
[vbraun@volker-two ~]$ x="a b"
[vbraun@volker-two ~]$ y=$x/c
[vbraun@volker-two ~]$ echo $y
a b/c
```




---

archive/issue_comments_090180.json:
```json
{
    "body": "Replying to [comment:106 vbraun]:\n> The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.\nOkay, I see.  I got confused by the renaming of `sage-spkg-install` to `spkg-install`, so I didn't realize what the file `sage-spkg-install` was all about.\n\n> I'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:\n> {{{\n> [vbraun`@`volker-two ~]$ x=\"a b\"\n> [vbraun`@`volker-two ~]$ y=$x/c\n> [vbraun`@`volker-two ~]$ echo $y\n> a b/c\n> }}}\nI agree, but I think that having the quotes is clearer anyway.\n\nThis is most certainly a bug (in `sage-make_devel_packages`):\n\n```\n+if [ ! -f \"$PKG/sage_scripts-$SAGE_VERSION.spkg\" ]; then\n```\n",
    "created_at": "2011-01-20T16:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90180",
    "user": "jdemeyer"
}
```

Replying to [comment:106 vbraun]:
> The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.
Okay, I see.  I got confused by the renaming of `sage-spkg-install` to `spkg-install`, so I didn't realize what the file `sage-spkg-install` was all about.

> I'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:
> {{{
> [vbraun`@`volker-two ~]$ x="a b"
> [vbraun`@`volker-two ~]$ y=$x/c
> [vbraun`@`volker-two ~]$ echo $y
> a b/c
> }}}
I agree, but I think that having the quotes is clearer anyway.

This is most certainly a bug (in `sage-make_devel_packages`):

```
+if [ ! -f "$PKG/sage_scripts-$SAGE_VERSION.spkg" ]; then
```




---

archive/issue_comments_090181.json:
```json
{
    "body": "Upon closer investigation I found that the ipython directory is in the `sage_scripts` spkg, but ignored in the `sage_scripts` mercurial repository. So its even worse :-)",
    "created_at": "2011-01-20T17:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90181",
    "user": "vbraun"
}
```

Upon closer investigation I found that the ipython directory is in the `sage_scripts` spkg, but ignored in the `sage_scripts` mercurial repository. So its even worse :-)



---

archive/issue_comments_090182.json:
```json
{
    "body": "Attachment\n\nUpdated patch",
    "created_at": "2011-01-20T17:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90182",
    "user": "vbraun"
}
```

Attachment

Updated patch



---

archive/issue_comments_090183.json:
```json
{
    "body": "Ha, I beat you by 13 seconds! :-)",
    "created_at": "2011-01-20T17:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90183",
    "user": "jdemeyer"
}
```

Ha, I beat you by 13 seconds! :-)



---

archive/issue_comments_090184.json:
```json
{
    "body": "That was probably my typo in rebasing the patch to Sage-4.6.1 ;-)",
    "created_at": "2011-01-20T17:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90184",
    "user": "vbraun"
}
```

That was probably my typo in rebasing the patch to Sage-4.6.1 ;-)



---

archive/issue_comments_090185.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-20T17:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90185",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_090186.json:
```json
{
    "body": "Attachment\n\nI'm fine with all changes.",
    "created_at": "2011-01-20T23:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90186",
    "user": "vbraun"
}
```

Attachment

I'm fine with all changes.



---

archive/issue_comments_090187.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-20T23:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90187",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090188.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-21T03:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90188",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090189.json:
```json
{
    "body": "Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:\n\n\n```\n$ ./sage -upgrade http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root/\nDownloading packages from 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg'.\nReading package lists...  Done!\nThe following packages will be upgraded:\n\n    examples-4.6.2.sage_root extcode-4.6.2.sage_root\n    sage-4.6.2.sage_root sage_root-4.6.2.sage_root\n    sage_scripts-4.6.2.sage_root\n\n ** WARNING: This is a source-based upgrade, which could take hours,\n ** fail, and render your Sage install useless!!\n\nDo you want to continue [y/N]? y\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/examples-4.6.2.sage_root.spkg --> examples-4.6.2.sage_root.spkg [..................................................]\nDeleting old spkg 'examples-4.6.1.spkg'...\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/extcode-4.6.2.sage_root.spkg --> extcode-4.6.2.sage_root.spkg [..................................................]\nDeleting old spkg 'extcode-4.6.1.spkg'...\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage-4.6.2.sage_root.spkg --> sage-4.6.2.sage_root.spkg [..................................................]\nDeleting old spkg 'sage-4.6.1.spkg'...\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_root-4.6.2.sage_root.spkg --> sage_root-4.6.2.sage_root.spkg [..............]\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_scripts-4.6.2.sage_root.spkg --> sage_scripts-4.6.2.sage_root.spkg [..................................................]\nDeleting old spkg 'sage_scripts-4.6.1.spkg'...\nhttp://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt --> VERSION.txt [.]\nFailed to download 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt'.\nAbort.\n```\n",
    "created_at": "2011-01-21T03:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90189",
    "user": "jdemeyer"
}
```

Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:


```
$ ./sage -upgrade http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root/
Downloading packages from 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg'.
Reading package lists...  Done!
The following packages will be upgraded:

    examples-4.6.2.sage_root extcode-4.6.2.sage_root
    sage-4.6.2.sage_root sage_root-4.6.2.sage_root
    sage_scripts-4.6.2.sage_root

 ** WARNING: This is a source-based upgrade, which could take hours,
 ** fail, and render your Sage install useless!!

Do you want to continue [y/N]? y
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/examples-4.6.2.sage_root.spkg --> examples-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'examples-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/extcode-4.6.2.sage_root.spkg --> extcode-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'extcode-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage-4.6.2.sage_root.spkg --> sage-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'sage-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_root-4.6.2.sage_root.spkg --> sage_root-4.6.2.sage_root.spkg [..............]
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_scripts-4.6.2.sage_root.spkg --> sage_scripts-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'sage_scripts-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt --> VERSION.txt [.]
Failed to download 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt'.
Abort.
```




---

archive/issue_comments_090190.json:
```json
{
    "body": "Replying to [comment:115 jdemeyer]:\n> Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:\n\nThat's because when the scripts patch was rebased, lines like these were removed:\n\n```\n# Put VERSION.txt in a directory available for download during the \n# update process.  (See sage-update.) \ncp -p VERSION.txt $TMP/$PKGDIR/$STD/\n```\n\nI think that just restoring these lines should fix it .",
    "created_at": "2011-01-21T05:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90190",
    "user": "jhpalmieri"
}
```

Replying to [comment:115 jdemeyer]:
> Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:

That's because when the scripts patch was rebased, lines like these were removed:

```
# Put VERSION.txt in a directory available for download during the 
# update process.  (See sage-update.) 
cp -p VERSION.txt $TMP/$PKGDIR/$STD/
```

I think that just restoring these lines should fix it .



---

archive/issue_comments_090191.json:
```json
{
    "body": "patch for scripts repo",
    "created_at": "2011-01-21T05:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90191",
    "user": "jhpalmieri"
}
```

patch for scripts repo



---

archive/issue_comments_090192.json:
```json
{
    "body": "Attachment\n\nHere's a new patch for the scripts repo.",
    "created_at": "2011-01-21T05:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90192",
    "user": "jhpalmieri"
}
```

Attachment

Here's a new patch for the scripts repo.



---

archive/issue_comments_090193.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-21T05:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90193",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090194.json:
```json
{
    "body": "Yes that fixes it!",
    "created_at": "2011-01-21T19:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90194",
    "user": "vbraun"
}
```

Yes that fixes it!



---

archive/issue_comments_090195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-21T19:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90195",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090196.json:
```json
{
    "body": "For the record: I successfully upgraded a Sage-4.6.1 installation to Sage-4.6.2.alpha1.",
    "created_at": "2011-01-22T04:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90196",
    "user": "vbraun"
}
```

For the record: I successfully upgraded a Sage-4.6.1 installation to Sage-4.6.2.alpha1.



---

archive/issue_comments_090197.json:
```json
{
    "body": "Attachment\n\nSAGEROOT patch for testing, DO NOT APPLY",
    "created_at": "2011-01-22T20:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90197",
    "user": "jdemeyer"
}
```

Attachment

SAGEROOT patch for testing, DO NOT APPLY



---

archive/issue_comments_090198.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2011-01-23T13:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90198",
    "user": "jdemeyer"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_090199.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-26T22:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90199",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_090200.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-02-16T08:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90200",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090201.json:
```json
{
    "body": "Testing changes to root-spkg-install...",
    "created_at": "2011-02-16T08:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90201",
    "user": "jdemeyer"
}
```

Testing changes to root-spkg-install...



---

archive/issue_comments_090202.json:
```json
{
    "body": "It seems that the `SAGE_ROOT` repository requires a very recent of Mercurial.  With Mercurial version 1.6.4, I get\n\n```\n$ hg --version\nMercurial Distributed SCM (version 1.6.4)\n\nCopyright (C) 2005-2010 Matt Mackall <mpm@selenic.com> and others\nThis is free software; see the source for copying conditions. There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n$ hg commit\nabort: requirement 'dotencode' not supported!\n```\n\n\nI agree that a sufficiently recent version of Mercurial is shipped with Sage, but unless there is a good reason for this `dotencode` requirement, I would prefer if the root repo worked with Mercurial 1.3.1 like the other repos.",
    "created_at": "2011-02-16T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90202",
    "user": "jdemeyer"
}
```

It seems that the `SAGE_ROOT` repository requires a very recent of Mercurial.  With Mercurial version 1.6.4, I get

```
$ hg --version
Mercurial Distributed SCM (version 1.6.4)

Copyright (C) 2005-2010 Matt Mackall <mpm@selenic.com> and others
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$ hg commit
abort: requirement 'dotencode' not supported!
```


I agree that a sufficiently recent version of Mercurial is shipped with Sage, but unless there is a good reason for this `dotencode` requirement, I would prefer if the root repo worked with Mercurial 1.3.1 like the other repos.



---

archive/issue_comments_090203.json:
```json
{
    "body": "The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?",
    "created_at": "2011-02-16T09:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90203",
    "user": "jdemeyer"
}
```

The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?



---

archive/issue_comments_090204.json:
```json
{
    "body": "The file $SAGE_ROOT/spkg/root-spkg-install",
    "created_at": "2011-02-16T09:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90204",
    "user": "jdemeyer"
}
```

The file $SAGE_ROOT/spkg/root-spkg-install



---

archive/issue_comments_090205.json:
```json
{
    "body": "Attachment\n\ncreate root repository without dotencode",
    "created_at": "2011-02-16T10:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90205",
    "user": "vbraun"
}
```

Attachment

create root repository without dotencode



---

archive/issue_comments_090206.json:
```json
{
    "body": "Attachment\n\nI'm pretty sure that the `root-spkg-install` ought to be under revision control. I'm travelling right now, so I can't test it out myself.",
    "created_at": "2011-02-16T10:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90206",
    "user": "vbraun"
}
```

Attachment

I'm pretty sure that the `root-spkg-install` ought to be under revision control. I'm travelling right now, so I can't test it out myself.



---

archive/issue_comments_090207.json:
```json
{
    "body": "I don't think there is anything in the repository which should require a new version of Mercurial. According to [this page from the Mercurial wiki](http://mercurial.selenic.com/wiki/RequiresFile), if you create a repo with a newer version and then try to access it with an older version, you can see this message.  So I don't think it's anything specific about the root repo.\n\nI'll try to look into the root-spkg-install file issue.",
    "created_at": "2011-02-16T15:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90207",
    "user": "jhpalmieri"
}
```

I don't think there is anything in the repository which should require a new version of Mercurial. According to [this page from the Mercurial wiki](http://mercurial.selenic.com/wiki/RequiresFile), if you create a repo with a newer version and then try to access it with an older version, you can see this message.  So I don't think it's anything specific about the root repo.

I'll try to look into the root-spkg-install file issue.



---

archive/issue_comments_090208.json:
```json
{
    "body": "Okay, line 24 in `9433_hg_script.sh` is\n\n```\n( cd spkg && hg add README.txt gen_html install pipestatus root-spkg-install )\n```\n\nSo it looks like root-spkg-install should be tracked. Can you explain why you think it's not?\n\nAlso, I see that vbraun has a new version of this script which might avoid the dotencode issue...",
    "created_at": "2011-02-16T15:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90208",
    "user": "jhpalmieri"
}
```

Okay, line 24 in `9433_hg_script.sh` is

```
( cd spkg && hg add README.txt gen_html install pipestatus root-spkg-install )
```

So it looks like root-spkg-install should be tracked. Can you explain why you think it's not?

Also, I see that vbraun has a new version of this script which might avoid the dotencode issue...



---

archive/issue_comments_090209.json:
```json
{
    "body": "Yes, I tripped over the dotencode thing before when working with mercurial. We don't really need that, so its ok to switch it off for backward compatibility, at least for the next year or so.",
    "created_at": "2011-02-16T16:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90209",
    "user": "vbraun"
}
```

Yes, I tripped over the dotencode thing before when working with mercurial. We don't really need that, so its ok to switch it off for backward compatibility, at least for the next year or so.



---

archive/issue_comments_090210.json:
```json
{
    "body": "the file SAGE_ROOT/.hgignore, now including spkg-install",
    "created_at": "2011-02-16T21:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90210",
    "user": "jhpalmieri"
}
```

the file SAGE_ROOT/.hgignore, now including spkg-install



---

archive/issue_comments_090211.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:127 jdemeyer]:\n> The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?\n\nI now realize that you're talking about the file `spkg-install` in the actual spkg file.  This is just a copy of `root-spkg-install` made by `sage-make_devel_packages`, so we don't need to track it.  I'm going to add it to the `.hgignore` file (by adding `^spkg-install$`, so it only matches a file with exactly that name at the top level).  This change requires review.\n\nMeanwhile, I'm giving Volker's change to the hg_script a positive review: for me, it makes any errors about dotencode go away when I use an older version of Mercurial to access the repo.",
    "created_at": "2011-02-16T21:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90211",
    "user": "jhpalmieri"
}
```

Attachment

Replying to [comment:127 jdemeyer]:
> The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?

I now realize that you're talking about the file `spkg-install` in the actual spkg file.  This is just a copy of `root-spkg-install` made by `sage-make_devel_packages`, so we don't need to track it.  I'm going to add it to the `.hgignore` file (by adding `^spkg-install$`, so it only matches a file with exactly that name at the top level).  This change requires review.

Meanwhile, I'm giving Volker's change to the hg_script a positive review: for me, it makes any errors about dotencode go away when I use an older version of Mercurial to access the repo.



---

archive/issue_comments_090212.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-16T21:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90212",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090213.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-17T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90213",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090214.json:
```json
{
    "body": "About the `dotencode` requirement: the change in the shell script indeed \"fixes\" the actual root repository.  However, the created `sage-root` spkg still has a mercurial repository which requires `dotencode` (so, after sdist and make, you need a new version of `hg`).  Since none of the other spkgs have this behaviour, I think this still needs work.",
    "created_at": "2011-02-17T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90214",
    "user": "jdemeyer"
}
```

About the `dotencode` requirement: the change in the shell script indeed "fixes" the actual root repository.  However, the created `sage-root` spkg still has a mercurial repository which requires `dotencode` (so, after sdist and make, you need a new version of `hg`).  Since none of the other spkgs have this behaviour, I think this still needs work.



---

archive/issue_comments_090215.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-18T01:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90215",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090216.json:
```json
{
    "body": "I don't really understand this complaint.  After all, Sage is distributed with a version of Mercurial, and it is completely reasonable to require that version for repositories which are part of Sage.  It's easy enough to type \"sage -hg\" instead of \"hg\", or make an alias, or put the Sage version of hg in your $PATH.  I think this is more a problem with Mercurial -- why is it not backwards compatible?  Who merged this version of Mercurial into Sage?   Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  \n\nAlso, if you're going to start inventing rules about how an spkg should be prepared, you might consider putting those rules in the developer's guide, and perhaps discussing them and getting approval for them on sage-devel before imposing them.\n\nWe can add `--config format.dotencode=0` at various places in sage-sdist and sage-make_devel_packages, and I'm attaching a new version of the scripts patch to do this, but this is not a viable long-term solution: the version requirements of Mercurial for anyone who wants to make a new spkg for Sage need to be made public, not imposed at anyone's whim.",
    "created_at": "2011-02-18T01:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90216",
    "user": "jhpalmieri"
}
```

I don't really understand this complaint.  After all, Sage is distributed with a version of Mercurial, and it is completely reasonable to require that version for repositories which are part of Sage.  It's easy enough to type "sage -hg" instead of "hg", or make an alias, or put the Sage version of hg in your $PATH.  I think this is more a problem with Mercurial -- why is it not backwards compatible?  Who merged this version of Mercurial into Sage?   Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  

Also, if you're going to start inventing rules about how an spkg should be prepared, you might consider putting those rules in the developer's guide, and perhaps discussing them and getting approval for them on sage-devel before imposing them.

We can add `--config format.dotencode=0` at various places in sage-sdist and sage-make_devel_packages, and I'm attaching a new version of the scripts patch to do this, but this is not a viable long-term solution: the version requirements of Mercurial for anyone who wants to make a new spkg for Sage need to be made public, not imposed at anyone's whim.



---

archive/issue_comments_090217.json:
```json
{
    "body": "Attachment\n\npatch for scripts repo",
    "created_at": "2011-02-18T01:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90217",
    "user": "jhpalmieri"
}
```

Attachment

patch for scripts repo



---

archive/issue_comments_090218.json:
```json
{
    "body": "Replying to [comment:134 jhpalmieri]:\n> Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  \nI didn't know about this until looking at this ticket.\n\nWhy not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?",
    "created_at": "2011-02-18T08:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90218",
    "user": "jdemeyer"
}
```

Replying to [comment:134 jhpalmieri]:
> Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  
I didn't know about this until looking at this ticket.

Why not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?



---

archive/issue_comments_090219.json:
```json
{
    "body": "Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594.  It can still be unmerged if you think that's a good thing to do.  Then we would fall back to Mercurial 1.6.4.",
    "created_at": "2011-02-18T08:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90219",
    "user": "jdemeyer"
}
```

Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594.  It can still be unmerged if you think that's a good thing to do.  Then we would fall back to Mercurial 1.6.4.



---

archive/issue_comments_090220.json:
```json
{
    "body": "Replying to [comment:136 jdemeyer]:\n> Why not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?\n\nIt certainly could be done, but it makes the repo harder to maintain.  Suppose you want to add a new file to the repo.  If you clone, you just run \"hg add\" (or apply a patch which accomplishes this) and you're done.  If you manually copy everything over, as is done for the other repos, then you also have to modify sage-make_devel_packages, maybe root-spkg-install, maybe sage-sdist.  This is especially true for the root repo, where files need to be dealt with individually: it's not like the Sage repo where except for a handful of files, you just copy over an entire directory (devel/sage/sage/), and it's not like the scripts repo where except for a handful of files, you just copy over everything with a certain name (\"sage-*\").\n\nMaybe instead it could run \"hg manifest\" and then manually copy over the listed files.  But this seems really awkward when \"hg clone\" does exactly what is required.\n\n> Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594. It can still be unmerged if you think that's a good thing to do. Then we would fall back to Mercurial 1.6.4.\n\nI'm really not sure about this.  Perhaps it should be discussed on #10594.  The lack of backwards compatibility seems problematic to me.  I can try to post something there later today.",
    "created_at": "2011-02-18T19:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90220",
    "user": "jhpalmieri"
}
```

Replying to [comment:136 jdemeyer]:
> Why not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?

It certainly could be done, but it makes the repo harder to maintain.  Suppose you want to add a new file to the repo.  If you clone, you just run "hg add" (or apply a patch which accomplishes this) and you're done.  If you manually copy everything over, as is done for the other repos, then you also have to modify sage-make_devel_packages, maybe root-spkg-install, maybe sage-sdist.  This is especially true for the root repo, where files need to be dealt with individually: it's not like the Sage repo where except for a handful of files, you just copy over an entire directory (devel/sage/sage/), and it's not like the scripts repo where except for a handful of files, you just copy over everything with a certain name ("sage-*").

Maybe instead it could run "hg manifest" and then manually copy over the listed files.  But this seems really awkward when "hg clone" does exactly what is required.

> Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594. It can still be unmerged if you think that's a good thing to do. Then we would fall back to Mercurial 1.6.4.

I'm really not sure about this.  Perhaps it should be discussed on #10594.  The lack of backwards compatibility seems problematic to me.  I can try to post something there later today.



---

archive/issue_comments_090221.json:
```json
{
    "body": "Anything that creates a new mercurial repository will by default require dotencode. In particular, `$SAGE_LOCAL/bin/sage-clone` which is unrelated to this ticket. \n\nIt would be easy to add `--config format.dotencode=0` to all `hg init`, `hg clone` commands. But current distributions already picked up the new mercurial, so I don't see it as particularly pressing issue. Moreover, we have a suitable mercurial in Sage precisely because it is sometimes finky with old versions. I would be in favor of just using dotencode. If it causes a big problem then we can always revert the repository format, you just have to clone with `dotencode=0`.",
    "created_at": "2011-02-18T20:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90221",
    "user": "vbraun"
}
```

Anything that creates a new mercurial repository will by default require dotencode. In particular, `$SAGE_LOCAL/bin/sage-clone` which is unrelated to this ticket. 

It would be easy to add `--config format.dotencode=0` to all `hg init`, `hg clone` commands. But current distributions already picked up the new mercurial, so I don't see it as particularly pressing issue. Moreover, we have a suitable mercurial in Sage precisely because it is sometimes finky with old versions. I would be in favor of just using dotencode. If it causes a big problem then we can always revert the repository format, you just have to clone with `dotencode=0`.



---

archive/issue_comments_090222.json:
```json
{
    "body": "Testing distributions:\n\n1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc0 + this ticket\n2. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + some random stuff (#10688 and [attachment:9433_testing.patch])",
    "created_at": "2011-02-20T15:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90222",
    "user": "jdemeyer"
}
```

Testing distributions:

1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc0 + this ticket
2. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + some random stuff (#10688 and [attachment:9433_testing.patch])



---

archive/issue_comments_090223.json:
```json
{
    "body": "Upgrading sage-4.7.alpha0 -> sage-4.7.alpha1 fails because of uncommitted changes: during the install of `sage_root-4.7.alpha1.spkg`, I get an editor with\n\n```\nHG: Enter commit message.  Lines beginning with 'HG:' are removed.\nHG: Leave message empty to abort commit.\nHG: --\nHG: user: Jeroen Demeyer <jdemeyer@cage.ugent.be>\nHG: branch 'default'\nHG: changed spkg/install\nHG: changed spkg/standard/deps\n```\n\n\n`hg diff` gives:\n\n```\ndiff -r 1c44cedc9957 spkg/install\n--- a/spkg/install      Thu Feb 17 15:54:54 2011 +0000\n+++ b/spkg/install      Sun Feb 20 16:06:09 2011 +0100\n@@ -1,5 +1,7 @@\n #!/usr/bin/env bash\n\n+# TESTING PATCH\n+\n ###############################################################################\n # Check if pipestatus already exists, otherwise\n # create it to allow upgrade from Sage <4.5.  This is a temporary fix.\n@@ -422,9 +424,6 @@\n TERMCAP=`$newest termcap`\n export TERMCAP\n\n-WEAVE=`$newest weave`\n-export WEAVE\n-\n ZLIB=`$newest zlib`\n export ZLIB\n\n```\n\nand something similar for `spkg/standard/deps`.\n\nIt seems that `spkg/install` and `spkg/standard/deps` are changed by the upgrader before the Sage root repository is installed and that this causes trouble.",
    "created_at": "2011-02-20T15:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90223",
    "user": "jdemeyer"
}
```

Upgrading sage-4.7.alpha0 -> sage-4.7.alpha1 fails because of uncommitted changes: during the install of `sage_root-4.7.alpha1.spkg`, I get an editor with

```
HG: Enter commit message.  Lines beginning with 'HG:' are removed.
HG: Leave message empty to abort commit.
HG: --
HG: user: Jeroen Demeyer <jdemeyer@cage.ugent.be>
HG: branch 'default'
HG: changed spkg/install
HG: changed spkg/standard/deps
```


`hg diff` gives:

```
diff -r 1c44cedc9957 spkg/install
--- a/spkg/install      Thu Feb 17 15:54:54 2011 +0000
+++ b/spkg/install      Sun Feb 20 16:06:09 2011 +0100
@@ -1,5 +1,7 @@
 #!/usr/bin/env bash

+# TESTING PATCH
+
 ###############################################################################
 # Check if pipestatus already exists, otherwise
 # create it to allow upgrade from Sage <4.5.  This is a temporary fix.
@@ -422,9 +424,6 @@
 TERMCAP=`$newest termcap`
 export TERMCAP

-WEAVE=`$newest weave`
-export WEAVE
-
 ZLIB=`$newest zlib`
 export ZLIB

```

and something similar for `spkg/standard/deps`.

It seems that `spkg/install` and `spkg/standard/deps` are changed by the upgrader before the Sage root repository is installed and that this causes trouble.



---

archive/issue_comments_090224.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-20T15:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90224",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090225.json:
```json
{
    "body": "John (and/or Volker), do you have time to work on this in the coming week / 2 weeks?  If yes, I would like to merge this in sage-4.7.alpha0.  This ticket might require some more work to get it right, so it would be nice to know whether you have time.  Otherwise we can postpone this to a later Sage release.",
    "created_at": "2011-02-21T10:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90225",
    "user": "jdemeyer"
}
```

John (and/or Volker), do you have time to work on this in the coming week / 2 weeks?  If yes, I would like to merge this in sage-4.7.alpha0.  This ticket might require some more work to get it right, so it would be nice to know whether you have time.  Otherwise we can postpone this to a later Sage release.



---

archive/issue_comments_090226.json:
```json
{
    "body": "I'm around and am in favor of merging it asap.",
    "created_at": "2011-02-21T11:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90226",
    "user": "vbraun"
}
```

I'm around and am in favor of merging it asap.



---

archive/issue_comments_090227.json:
```json
{
    "body": "I have a fix to this problem which I am testing right now.  It looks good so far, and I'll post it later if it continues to look good.  (The fix is as follows: the script `sage-update` downloads new versions of several files, like `install` and `deps`; I'm now adding a command to commit the Sage root repo after doing this download.)",
    "created_at": "2011-02-21T15:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90227",
    "user": "jhpalmieri"
}
```

I have a fix to this problem which I am testing right now.  It looks good so far, and I'll post it later if it continues to look good.  (The fix is as follows: the script `sage-update` downloads new versions of several files, like `install` and `deps`; I'm now adding a command to commit the Sage root repo after doing this download.)



---

archive/issue_comments_090228.json:
```json
{
    "body": "Okay, I have two options; which is better?  In `sage-update`, the files install, deps, and newest_version might get changed.  We could:\n\n- commit the changes in `sage-update`, and then the changes will get committed again by `root-spkg-install` when the root repo spkg is installed.\n\n- or in `root-spkg-install`, we can overwrite any changes: do `hg pull ...` to pull from the new repo and then `hg update --clean` to discard any other changes.\n\nThe first of these adds a redundant commit message to the log file if the relevant files are changed.  The second discards all changes, including any other ones that the user may have made.  I don't know Mercurial well enough, but perhaps there is a better third choice?",
    "created_at": "2011-02-21T16:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90228",
    "user": "jhpalmieri"
}
```

Okay, I have two options; which is better?  In `sage-update`, the files install, deps, and newest_version might get changed.  We could:

- commit the changes in `sage-update`, and then the changes will get committed again by `root-spkg-install` when the root repo spkg is installed.

- or in `root-spkg-install`, we can overwrite any changes: do `hg pull ...` to pull from the new repo and then `hg update --clean` to discard any other changes.

The first of these adds a redundant commit message to the log file if the relevant files are changed.  The second discards all changes, including any other ones that the user may have made.  I don't know Mercurial well enough, but perhaps there is a better third choice?



---

archive/issue_comments_090229.json:
```json
{
    "body": "I'm in favor of the following third option:\n\n1. The first thing that `sage-update` should do is to commit any outstanding changes and, in particular, abort if there is a patch queue applied. So you are safe even if you forgot to commit your changes.\n2. Then `sage-update` overwrites some critical files for its operation. \n3. Finally, the `sage_root` spkg is installed and its `spkg-install` overwrites the remaining non-critical files in the root repository. I'd rather be guaranteed to have a clean slate after update than dying in the middle of the update because the attempted merge fails.\n\nSo if you had any uncommitted changes before updating, you'll end up with two commit messages. The more individual commits the better. The only drawback is that if you had made modifications to the root repository that you want to keep and you are not using patch queues, then you now have to extract your changes as a patch from the repository and apply that patch. I think thats acceptable since, I think, most developers use patch queues and I don't expect too frequent edits to the root repository.\n\nIf that doesn't convince you, I'd prefer option number 1 as my second choice :-)",
    "created_at": "2011-02-21T18:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90229",
    "user": "vbraun"
}
```

I'm in favor of the following third option:

1. The first thing that `sage-update` should do is to commit any outstanding changes and, in particular, abort if there is a patch queue applied. So you are safe even if you forgot to commit your changes.
2. Then `sage-update` overwrites some critical files for its operation. 
3. Finally, the `sage_root` spkg is installed and its `spkg-install` overwrites the remaining non-critical files in the root repository. I'd rather be guaranteed to have a clean slate after update than dying in the middle of the update because the attempted merge fails.

So if you had any uncommitted changes before updating, you'll end up with two commit messages. The more individual commits the better. The only drawback is that if you had made modifications to the root repository that you want to keep and you are not using patch queues, then you now have to extract your changes as a patch from the repository and apply that patch. I think thats acceptable since, I think, most developers use patch queues and I don't expect too frequent edits to the root repository.

If that doesn't convince you, I'd prefer option number 1 as my second choice :-)



---

archive/issue_comments_090230.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-21T20:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90230",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090231.json:
```json
{
    "body": "Here is a new version of the scripts patch.  The only change is in `sage-update`.  I updated the instructions, also: I'm not worrying about making the repo compatible with older versions of Mercurial right now.",
    "created_at": "2011-02-21T20:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90231",
    "user": "jhpalmieri"
}
```

Here is a new version of the scripts patch.  The only change is in `sage-update`.  I updated the instructions, also: I'm not worrying about making the repo compatible with older versions of Mercurial right now.



---

archive/issue_comments_090232.json:
```json
{
    "body": "Oh, also, I created some versions for testing upgrades:\n\n- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X0/\n- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X1/ (spkg/install changed)\n- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X2/ (Makefile changed)\n- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X3/ (Makefile and spkg/standard/deps changed)\n\nThe first of these is just 4.6.2.rc0 with the patches from this ticket applied.  In each of the other ones, one or two files have been modified, as indicated.  It's also worth testing by updating to the \"X0\" version, for example, then modifying a file tracked by the root repo (like README.txt) without committing the change, and then trying to update to \"X1\".  The update should abort.",
    "created_at": "2011-02-21T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90232",
    "user": "jhpalmieri"
}
```

Oh, also, I created some versions for testing upgrades:

- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X0/
- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X1/ (spkg/install changed)
- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X2/ (Makefile changed)
- http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X3/ (Makefile and spkg/standard/deps changed)

The first of these is just 4.6.2.rc0 with the patches from this ticket applied.  In each of the other ones, one or two files have been modified, as indicated.  It's also worth testing by updating to the "X0" version, for example, then modifying a file tracked by the root repo (like README.txt) without committing the change, and then trying to update to "X1".  The update should abort.



---

archive/issue_comments_090233.json:
```json
{
    "body": "I made a few minor cosmetic changes in the patch, and right now, the upgrade paths I mentioned use the old version, not the new one.  I'll have them updated in a few minutes.",
    "created_at": "2011-02-21T21:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90233",
    "user": "jhpalmieri"
}
```

I made a few minor cosmetic changes in the patch, and right now, the upgrade paths I mentioned use the old version, not the new one.  I'll have them updated in a few minutes.



---

archive/issue_comments_090234.json:
```json
{
    "body": "Okay, everything's updated now.",
    "created_at": "2011-02-21T21:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90234",
    "user": "jhpalmieri"
}
```

Okay, everything's updated now.



---

archive/issue_comments_090235.json:
```json
{
    "body": "I made new testing releases:\n\n1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc1 + this ticket\n2. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + #10688 + [attachment:9433_testing.patch]\n\nUpgrading sage-4.7.alpha0 -> sage-4.7.alpha1 succeeded this time.",
    "created_at": "2011-02-24T14:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90235",
    "user": "jdemeyer"
}
```

I made new testing releases:

1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc1 + this ticket
2. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + #10688 + [attachment:9433_testing.patch]

Upgrading sage-4.7.alpha0 -> sage-4.7.alpha1 succeeded this time.



---

archive/issue_comments_090236.json:
```json
{
    "body": "I've tried the update and it works beautifully. \n\nI think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail to commit with \n\n```\n[vbraun@volker-desktop sage-4.7.alpha0]$ mv ~/.hgrc ~/backup.hgrc\n[vbraun@volker-desktop sage-4.7.alpha0]$ hg commit -m \"test\"\nabort: no username supplied (see \"hg help config\")\n```\n\nSo whenever we commit to the root repo, we should specify a username explicitly. For example,\n\n```\nhg commit -u \"committed by sage -upgrade\" -m \"test\"\n```\n",
    "created_at": "2011-02-24T20:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90236",
    "user": "vbraun"
}
```

I've tried the update and it works beautifully. 

I think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail to commit with 

```
[vbraun@volker-desktop sage-4.7.alpha0]$ mv ~/.hgrc ~/backup.hgrc
[vbraun@volker-desktop sage-4.7.alpha0]$ hg commit -m "test"
abort: no username supplied (see "hg help config")
```

So whenever we commit to the root repo, we should specify a username explicitly. For example,

```
hg commit -u "committed by sage -upgrade" -m "test"
```




---

archive/issue_comments_090237.json:
```json
{
    "body": "patch for scripts repo",
    "created_at": "2011-02-25T05:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90237",
    "user": "jhpalmieri"
}
```

patch for scripts repo



---

archive/issue_comments_090238.json:
```json
{
    "body": "Attachment\n\nThe file $SAGE_ROOT/spkg/root-spkg-install",
    "created_at": "2011-02-25T05:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90238",
    "user": "jhpalmieri"
}
```

Attachment

The file $SAGE_ROOT/spkg/root-spkg-install



---

archive/issue_comments_090239.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:153 vbraun]:\n> I think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail\n\nI wouldn't have spotted this.  Good catch.  I have new patches which add \"-u ...\" to various commit commands: in sage-update and in root-spkg-install.  I haven't bothered with sage-sdist or sage-make_devel_packages, since these are done by the release manager who had better have a .hgrc file.  (Besides, there are already other \"hg commit\" commands in those scripts.)\n\nI've also updated my versions (4.6.2.X0 etc.) for testing upgrades with these changes.",
    "created_at": "2011-02-25T05:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90239",
    "user": "jhpalmieri"
}
```

Attachment

Replying to [comment:153 vbraun]:
> I think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail

I wouldn't have spotted this.  Good catch.  I have new patches which add "-u ..." to various commit commands: in sage-update and in root-spkg-install.  I haven't bothered with sage-sdist or sage-make_devel_packages, since these are done by the release manager who had better have a .hgrc file.  (Besides, there are already other "hg commit" commands in those scripts.)

I've also updated my versions (4.6.2.X0 etc.) for testing upgrades with these changes.



---

archive/issue_comments_090240.json:
```json
{
    "body": "I'm happy with it now. I tested upgrades without `~/.hgrc` and everything worked for me.",
    "created_at": "2011-02-25T17:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90240",
    "user": "vbraun"
}
```

I'm happy with it now. I tested upgrades without `~/.hgrc` and everything worked for me.



---

archive/issue_comments_090241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-25T17:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90241",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090242.json:
```json
{
    "body": "Agreed!  This will get merged in sage-4.7.alpha0.  I still expect breakage here and there, but that's what alpha versions are for.",
    "created_at": "2011-02-26T10:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90242",
    "user": "jdemeyer"
}
```

Agreed!  This will get merged in sage-4.7.alpha0.  I still expect breakage here and there, but that's what alpha versions are for.



---

archive/issue_comments_090243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-08T21:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9433#issuecomment-90243",
    "user": "jdemeyer"
}
```

Resolution: fixed
