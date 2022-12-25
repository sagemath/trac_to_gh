# Issue 9083: 'make distclean' fails to remove some files or directories.

archive/issues_009083.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nKeywords: beginner\n\nConventionally 'make distclean' removes all traces of a build process, leaving only the original files. \n\nHowever, at least the following four files or directories are being left after running 'make distclean'.\n\n\n```\n./.BUILDSTART \ndochtml.log\nspkg/install\nspkg/installed\n```\n\nThere is a section in the makefile\n\n```\ndistclean:\n        make clean\n        rm -rf local\n        rm -rf spkg/installed/*\n        rm -f install.log\n        rm -f test.log testall.log testlong.log ptest.log ptestlong.log\n        rm -rf data\n        rm -rf dist\n        rm -rf devel\n        rm -rf doc\n        rm -rf examples\n        rm -rf sage-python\n        rm -rf spkg/build\n        rm -rf spkg/archive\n        rm -rf ipython\n        rm -rf matplotlibrc\n        rm -rf tmp\n```\n\n\nThe two files and two directories need adding to that section. There may be other files created too. The way to find any new files or directories would be to \n\n* Extract the Sage tarball.\n* Build Sage fully. \n* Run the following two commands from the top level Sage directory.\n \n\n```\n$ 'make distclean'\n$ find . -mtime -2\n```\n\n\nThat will list any files or directories updated in the last two days. \n\nThe following files\n* sage-README-osx.txt\n* COPYING.txt\n* README.txt\n\nare having their modification times changed. I think that is undesirable, but that is another problem and the subject of #9082. So the changes to the makefile should not remove those 3 files, despite their recent modification times. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9083\n\n",
    "created_at": "2010-05-29T07:30:09Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "'make distclean' fails to remove some files or directories.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9083",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

Keywords: beginner

Conventionally 'make distclean' removes all traces of a build process, leaving only the original files. 

However, at least the following four files or directories are being left after running 'make distclean'.


```
./.BUILDSTART 
dochtml.log
spkg/install
spkg/installed
```

There is a section in the makefile

```
distclean:
        make clean
        rm -rf local
        rm -rf spkg/installed/*
        rm -f install.log
        rm -f test.log testall.log testlong.log ptest.log ptestlong.log
        rm -rf data
        rm -rf dist
        rm -rf devel
        rm -rf doc
        rm -rf examples
        rm -rf sage-python
        rm -rf spkg/build
        rm -rf spkg/archive
        rm -rf ipython
        rm -rf matplotlibrc
        rm -rf tmp
```


The two files and two directories need adding to that section. There may be other files created too. The way to find any new files or directories would be to 

* Extract the Sage tarball.
* Build Sage fully. 
* Run the following two commands from the top level Sage directory.
 

```
$ 'make distclean'
$ find . -mtime -2
```


That will list any files or directories updated in the last two days. 

The following files
* sage-README-osx.txt
* COPYING.txt
* README.txt

are having their modification times changed. I think that is undesirable, but that is another problem and the subject of #9082. So the changes to the makefile should not remove those 3 files, despite their recent modification times. 



Issue created by migration from https://trac.sagemath.org/ticket/9083





---

archive/issue_comments_084180.json:
```json
{
    "body": "patch for SAGE_ROOT/makefile",
    "created_at": "2010-06-01T07:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84180",
    "user": "https://github.com/dandrake"
}
```

patch for SAGE_ROOT/makefile



---

archive/issue_comments_084181.json:
```json
{
    "body": "Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket9083/makefile.patch) by @dandrake created at 2010-06-01 07:55:34\n\nThe attached patch removes .BUILDSTART, dochtml.log, spkg/install, and spkg/installed. It's a regular unified diff, since SAGE_ROOT isn't in a Mercurial repo.\n\nHrm, I see the \"beginner\" tag...I hope I'm not stepping on any beginner's toes here! Although changing files in SAGE_ROOT is a bit strange, since they're not version controlled.",
    "created_at": "2010-06-01T07:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84181",
    "user": "https://github.com/dandrake"
}
```

Attachment [makefile.patch](tarball://root/attachments/some-uuid/ticket9083/makefile.patch) by @dandrake created at 2010-06-01 07:55:34

The attached patch removes .BUILDSTART, dochtml.log, spkg/install, and spkg/installed. It's a regular unified diff, since SAGE_ROOT isn't in a Mercurial repo.

Hrm, I see the "beginner" tag...I hope I'm not stepping on any beginner's toes here! Although changing files in SAGE_ROOT is a bit strange, since they're not version controlled.



---

archive/issue_comments_084182.json:
```json
{
    "body": "I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line\n\n\n```\n\trm -rf spkg/installed/*\n```\n\n\ncan actually be removed, as your \n\n\n```\n\trm -rf spkg/installed\n```\n\n\nwill do it, but it does not make much difference. \n\nI've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. \n\nDave",
    "created_at": "2010-06-01T08:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84182",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line


```
	rm -rf spkg/installed/*
```


can actually be removed, as your 


```
	rm -rf spkg/installed
```


will do it, but it does not make much difference. 

I've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. 

Dave



---

archive/issue_comments_084183.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-06-01T08:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84183",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_084184.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-01T08:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84184",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084185.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line\n> \n> {{{\n> \trm -rf spkg/installed/*\n> }}}\n> \n> can actually be removed, as your \n> \n> {{{\n> \trm -rf spkg/installed\n> }}}\n> \n> will do it, but it does not make much difference.\n\nI think those actually are different because of the trailing slash -- if we do\n\n```\nrm -rf spkg/installed*\n```\n\nI think that will get everything, right? If so, I can change the patch.\n> \n> I've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. \n> \n> Dave",
    "created_at": "2010-06-01T09:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84185",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:2 drkirkby]:
> I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line
> 
> {{{
> 	rm -rf spkg/installed/*
> }}}
> 
> can actually be removed, as your 
> 
> {{{
> 	rm -rf spkg/installed
> }}}
> 
> will do it, but it does not make much difference.

I think those actually are different because of the trailing slash -- if we do

```
rm -rf spkg/installed*
```

I think that will get everything, right? If so, I can change the patch.
> 
> I've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. 
> 
> Dave



---

archive/issue_comments_084186.json:
```json
{
    "body": "Replying to [comment:4 ddrake]:\n> Replying to [comment:2 drkirkby]:\n> > I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line\n> > \n> > {{{\n> > \trm -rf spkg/installed/*\n> > }}}\n> > \n> > can actually be removed, as your \n> > \n> > {{{\n> > \trm -rf spkg/installed\n> > }}}\n> > \n> > will do it, but it does not make much difference.\n> \n> I think those actually are different because of the trailing slash -- if we do\n> {{{\n> rm -rf spkg/installed*\n> }}}\n> I think that will get everything, right? If so, I can change the patch.\n\nThe trailing slash should make no difference\n\n\n```\nrm -rf spkg/installed\n```\n\n\nwill remove the directory spkg/installed and of course anything in any subdirectory of spkg/installed. \n\nIn contrast\n\n\n```\nrm -rf spkg/installed*\n```\n\n\nwould remove anything starting with spkg/installed, such as \n\n\n```\nspkg/installeda\nspkg/installedb\nspkg/installedc\nspkg/installed-but-do-not-delete-this-directory\n```\n\n \nI have removed the 'beginner' tag. \n\nDave",
    "created_at": "2010-06-01T22:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84186",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:4 ddrake]:
> Replying to [comment:2 drkirkby]:
> > I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line
> > 
> > {{{
> > 	rm -rf spkg/installed/*
> > }}}
> > 
> > can actually be removed, as your 
> > 
> > {{{
> > 	rm -rf spkg/installed
> > }}}
> > 
> > will do it, but it does not make much difference.
> 
> I think those actually are different because of the trailing slash -- if we do
> {{{
> rm -rf spkg/installed*
> }}}
> I think that will get everything, right? If so, I can change the patch.

The trailing slash should make no difference


```
rm -rf spkg/installed
```


will remove the directory spkg/installed and of course anything in any subdirectory of spkg/installed. 

In contrast


```
rm -rf spkg/installed*
```


would remove anything starting with spkg/installed, such as 


```
spkg/installeda
spkg/installedb
spkg/installedc
spkg/installed-but-do-not-delete-this-directory
```

 
I have removed the 'beginner' tag. 

Dave



---

archive/issue_comments_084187.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"\".",
    "created_at": "2010-06-01T22:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84187",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing keywords from "beginner" to "".



---

archive/issue_comments_084188.json:
```json
{
    "body": "I think that the directory spkg/optional should also be removed.",
    "created_at": "2010-06-21T22:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84188",
    "user": "https://github.com/jhpalmieri"
}
```

I think that the directory spkg/optional should also be removed.



---

archive/issue_comments_084189.json:
```json
{
    "body": "Attachment [makefile](tarball://root/attachments/some-uuid/ticket9083/makefile) by @jhpalmieri created at 2010-06-27 05:38:24\n\nthe file SAGE_ROOT/makefile",
    "created_at": "2010-06-27T05:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84189",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [makefile](tarball://root/attachments/some-uuid/ticket9083/makefile) by @jhpalmieri created at 2010-06-27 05:38:24

the file SAGE_ROOT/makefile



---

archive/issue_comments_084190.json:
```json
{
    "body": "Attachment [makefile-new.patch](tarball://root/attachments/some-uuid/ticket9083/makefile-new.patch) by @jhpalmieri created at 2010-06-27 05:38:44\n\ndiff between original makefile and the one I attached",
    "created_at": "2010-06-27T05:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84190",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [makefile-new.patch](tarball://root/attachments/some-uuid/ticket9083/makefile-new.patch) by @jhpalmieri created at 2010-06-27 05:38:44

diff between original makefile and the one I attached



---

archive/issue_comments_084191.json:
```json
{
    "body": "Here's a new version of \"makefile\" along with \"makefile-new.patch\" which is the diff between the current makefile and the new version.  Rebased against 4.5.alpha0.",
    "created_at": "2010-06-27T05:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84191",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new version of "makefile" along with "makefile-new.patch" which is the diff between the current makefile and the new version.  Rebased against 4.5.alpha0.



---

archive/issue_comments_084192.json:
```json
{
    "body": "By the way, we shouldn't remove spkg/install, because this file is there when you first unpack the Sage tar file, and it is used when you type \"make\": when you run \"make\" from SAGE_ROOT, the following command gets executed:\n\n```\ncd spkg && ./install all 2>&1 | tee -a ../install.log\n```\n\nAdmittedly, I think the file spkg/install gets overwritten when the sage_scripts spkg gets installed, but if the release manager has done their job right, the new file should be identical to the old one.  Regardless, removing it will break \"make\" for Sage.",
    "created_at": "2010-06-27T05:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84192",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, we shouldn't remove spkg/install, because this file is there when you first unpack the Sage tar file, and it is used when you type "make": when you run "make" from SAGE_ROOT, the following command gets executed:

```
cd spkg && ./install all 2>&1 | tee -a ../install.log
```

Admittedly, I think the file spkg/install gets overwritten when the sage_scripts spkg gets installed, but if the release manager has done their job right, the new file should be identical to the old one.  Regardless, removing it will break "make" for Sage.



---

archive/issue_comments_084193.json:
```json
{
    "body": "Also delete `docpdf.log`.",
    "created_at": "2010-07-07T05:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84193",
    "user": "https://github.com/qed777"
}
```

Also delete `docpdf.log`.



---

archive/issue_comments_084194.json:
```json
{
    "body": "Attachment [makefile.2](tarball://root/attachments/some-uuid/ticket9083/makefile.2) by @qed777 created at 2010-07-07 05:06:59\n\nDiff of `makefile.2` vs. 4.5.alpha4.",
    "created_at": "2010-07-07T05:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84194",
    "user": "https://github.com/qed777"
}
```

Attachment [makefile.2](tarball://root/attachments/some-uuid/ticket9083/makefile.2) by @qed777 created at 2010-07-07 05:06:59

Diff of `makefile.2` vs. 4.5.alpha4.



---

archive/issue_comments_084195.json:
```json
{
    "body": "Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket9083/makefile.diff) by @qed777 created at 2010-07-07 05:09:35\n\nI've attached a reviewer's update that also deletes `docpdf.log`.",
    "created_at": "2010-07-07T05:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84195",
    "user": "https://github.com/qed777"
}
```

Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket9083/makefile.diff) by @qed777 created at 2010-07-07 05:09:35

I've attached a reviewer's update that also deletes `docpdf.log`.



---

archive/issue_comments_084196.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> I've attached a reviewer's update that also deletes `docpdf.log`.\n\nThat change looks good to me.",
    "created_at": "2010-07-07T05:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84196",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:9 mpatel]:
> I've attached a reviewer's update that also deletes `docpdf.log`.

That change looks good to me.



---

archive/issue_comments_084197.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-07T06:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84197",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084198.json:
```json
{
    "body": "To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.",
    "created_at": "2010-07-07T06:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84198",
    "user": "https://github.com/qed777"
}
```

To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.



---

archive/issue_events_022261.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T23:39:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9083#event-22261"
}
```



---

archive/issue_comments_084199.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.\n\nDone, in 4.5.2.alpha1.",
    "created_at": "2010-07-22T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84199",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:12 mpatel]:
> To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.

Done, in 4.5.2.alpha1.



---

archive/issue_comments_084200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9083#issuecomment-84200",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
