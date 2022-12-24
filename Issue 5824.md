# Issue 5824: Move DSage to its own spkg

archive/issues_005824.json:
```json
{
    "body": "Assignee: yi\n\nDSage isn't actively maintained and not working too well. Since its coverage is basically zero (0.7%) move it to its own spkg and provide hooks that make current code work. These hooks should be deprecated instantly. \n\nNote the effect on coverage for 3.4.1.rc4:\n\nBefore:\n\n```\nOverall weighted coverage score:  68.2%\nTotal number of functions:  22947\nWe need  401 more function to get to 70% coverage.\nWe need 1549 more function to get to 75% coverage.\nWe need 2696 more function to get to 80% coverage.\n```\n\nAfter:\n\n```\nOverall weighted coverage score:  69.8%\nTotal number of functions:  22432\nWe need   45 more function to get to 70% coverage.\nWe need 1166 more function to get to 75% coverage.\nWe need 2288 more function to get to 80% coverage.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5824\n\n",
    "created_at": "2009-04-19T07:46:30Z",
    "labels": [
        "dsage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Move DSage to its own spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5824",
    "user": "mabshoff"
}
```
Assignee: yi

DSage isn't actively maintained and not working too well. Since its coverage is basically zero (0.7%) move it to its own spkg and provide hooks that make current code work. These hooks should be deprecated instantly. 

Note the effect on coverage for 3.4.1.rc4:

Before:

```
Overall weighted coverage score:  68.2%
Total number of functions:  22947
We need  401 more function to get to 70% coverage.
We need 1549 more function to get to 75% coverage.
We need 2696 more function to get to 80% coverage.
```

After:

```
Overall weighted coverage score:  69.8%
Total number of functions:  22432
We need   45 more function to get to 70% coverage.
We need 1166 more function to get to 75% coverage.
We need 2288 more function to get to 80% coverage.
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5824





---

archive/issue_comments_045774.json:
```json
{
    "body": "> To do the move one must also pay careful attention to the unit tests, -sdist, -bdist and setup.py.\n\n\nAlternatively it could be removed, but have its setup.py configured so it installs into exactly the same place as now.  Then all testing code would work exactly the same as before.  The main difference is that one would no longer see this when starting Sage:\n\n```\nchanging mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_setup.py to 755\nchanging mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/spkg-debian-maybe to 755\nchanging mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_worker.py to 755\n```\n",
    "created_at": "2009-04-19T19:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45774",
    "user": "was"
}
```

> To do the move one must also pay careful attention to the unit tests, -sdist, -bdist and setup.py.


Alternatively it could be removed, but have its setup.py configured so it installs into exactly the same place as now.  Then all testing code would work exactly the same as before.  The main difference is that one would no longer see this when starting Sage:

```
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_setup.py to 755
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/spkg-debian-maybe to 755
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_worker.py to 755
```




---

archive/issue_comments_045775.json:
```json
{
    "body": "patch to apply to main sage library (hg_sage.apply(...)); this deletes all of dsage from the main library",
    "created_at": "2009-04-19T19:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45775",
    "user": "was"
}
```

patch to apply to main sage library (hg_sage.apply(...)); this deletes all of dsage from the main library



---

archive/issue_comments_045776.json:
```json
{
    "body": "Attachment [dsage-1.0.spkg](tarball://root/attachments/some-uuid/ticket5824/dsage-1.0.spkg) by was created at 2009-04-19 20:00:29\n\nthis is dsage as a complete self-contained spkg",
    "created_at": "2009-04-19T20:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45776",
    "user": "was"
}
```

Attachment [dsage-1.0.spkg](tarball://root/attachments/some-uuid/ticket5824/dsage-1.0.spkg) by was created at 2009-04-19 20:00:29

this is dsage as a complete self-contained spkg



---

archive/issue_comments_045777.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket5824/install) by was created at 2009-04-19 20:01:58\n\nreplace SAGE_ROOT/spkg/install by the attached file",
    "created_at": "2009-04-19T20:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45777",
    "user": "was"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket5824/install) by was created at 2009-04-19 20:01:58

replace SAGE_ROOT/spkg/install by the attached file



---

archive/issue_comments_045778.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket5824/deps) by was created at 2009-04-19 20:03:21\n\nreplace SAGE_ROOT/spkg/standard/deps by the attached file",
    "created_at": "2009-04-19T20:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45778",
    "user": "was"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket5824/deps) by was created at 2009-04-19 20:03:21

replace SAGE_ROOT/spkg/standard/deps by the attached file



---

archive/issue_comments_045779.json:
```json
{
    "body": "If we're deprecating dsage, I think we should remove its section from the tutorial.  (Remove the file 'distributed.rst' and delete the appropriate line from 'index.rst'.) I can provide a patch if you think it's a good idea.\n\nI've never been convinced that it belonged there anyway, but that's another issue...",
    "created_at": "2009-04-19T20:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45779",
    "user": "jhpalmieri"
}
```

If we're deprecating dsage, I think we should remove its section from the tutorial.  (Remove the file 'distributed.rst' and delete the appropriate line from 'index.rst'.) I can provide a patch if you think it's a good idea.

I've never been convinced that it belonged there anyway, but that's another issue...



---

archive/issue_comments_045780.json:
```json
{
    "body": "I would prefer to install the DSage.spkg outside the tree for various reasons:\n\n* As is it still counts against our coverage.\n* Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.\n* Sage 4.0 seems to be a good point to have the separation, so I am all for it getting done in the next 4 weeks :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T23:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45780",
    "user": "mabshoff"
}
```

I would prefer to install the DSage.spkg outside the tree for various reasons:

* As is it still counts against our coverage.
* Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.
* Sage 4.0 seems to be a good point to have the separation, so I am all for it getting done in the next 4 weeks :)

Cheers,

Michael



---

archive/issue_comments_045781.json:
```json
{
    "body": ">    * As is it still counts against our coverage.\n\nNo it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.\n\n>    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.\n\nI strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.",
    "created_at": "2009-04-19T23:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45781",
    "user": "was"
}
```

>    * As is it still counts against our coverage.

No it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.

>    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.

I strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.



---

archive/issue_comments_045782.json:
```json
{
    "body": "Michael did have one interesting point in chat, which is that if you do\n\n```\nrm -rf devel/sage/build\n```\n\nthen dsage is gone too, so it has to be reinstalled.\n\nNote that `sage -ba` does not do `rm -rf devel/sage/build`, but instead just touches all cython files.",
    "created_at": "2009-04-19T23:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45782",
    "user": "was"
}
```

Michael did have one interesting point in chat, which is that if you do

```
rm -rf devel/sage/build
```

then dsage is gone too, so it has to be reinstalled.

Note that `sage -ba` does not do `rm -rf devel/sage/build`, but instead just touches all cython files.



---

archive/issue_comments_045783.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> >    * As is it still counts against our coverage.\n> \n> No it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.\n\nYes, I am wrong on that point.\n\n> >    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.\n> \n> I strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.\n> \n\nI had assumed wrongly as above that the DSage code would end up in devel/sage which it clearly doesn't, so I am wrong again. \n\nWhat I do not like is subpackages installing into a tree in site-packages, i.e. the latest twisted does that with web2 I believe. \n\nThe main question whether we do this or not is:\n\n* Are we going to fix/rewrite DSage? In that case it should stay in the tree.\n* If we are going to deprecate it we should move it to its own spkg and add deprecation warnings. The question then is what is going to happen after DSage and I don't think there is a clear answer to that question yet.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T00:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45783",
    "user": "mabshoff"
}
```

Replying to [comment:6 was]:
> >    * As is it still counts against our coverage.
> 
> No it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.

Yes, I am wrong on that point.

> >    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.
> 
> I strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.
> 

I had assumed wrongly as above that the DSage code would end up in devel/sage which it clearly doesn't, so I am wrong again. 

What I do not like is subpackages installing into a tree in site-packages, i.e. the latest twisted does that with web2 I believe. 

The main question whether we do this or not is:

* Are we going to fix/rewrite DSage? In that case it should stay in the tree.
* If we are going to deprecate it we should move it to its own spkg and add deprecation warnings. The question then is what is going to happen after DSage and I don't think there is a clear answer to that question yet.

Cheers,

Michael



---

archive/issue_comments_045784.json:
```json
{
    "body": "Attachment [trac_5824-part2.patch](tarball://root/attachments/some-uuid/ticket5824/trac_5824-part2.patch) by was created at 2009-04-20 02:05:21\n\napply this to the hg_sage repo right after trac_5824.patch; it updates setup.py",
    "created_at": "2009-04-20T02:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45784",
    "user": "was"
}
```

Attachment [trac_5824-part2.patch](tarball://root/attachments/some-uuid/ticket5824/trac_5824-part2.patch) by was created at 2009-04-20 02:05:21

apply this to the hg_sage repo right after trac_5824.patch; it updates setup.py



---

archive/issue_comments_045785.json:
```json
{
    "body": "Positive review. Some of the files removed had some slight rejects, but I rebased the patch :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45785",
    "user": "mabshoff"
}
```

Positive review. Some of the files removed had some slight rejects, but I rebased the patch :)

Cheers,

Michael



---

archive/issue_comments_045786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T10:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45786",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045787.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T10:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5824#issuecomment-45787",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
