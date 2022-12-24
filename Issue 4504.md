# Issue 4504: Sage's .spkg extension

archive/issues_004504.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: .spkg extension, Sage packages\n\nAt [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/3b877b874eda9e62), it's suggested that there should be a README.txt file to briefly explain the .spkg extension of Sage packages and pointers to more info.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4504\n\n",
    "created_at": "2008-11-12T22:52:44Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Sage's .spkg extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4504",
    "user": "mvngu"
}
```
Assignee: tba

Keywords: .spkg extension, Sage packages

At [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/3b877b874eda9e62), it's suggested that there should be a README.txt file to briefly explain the .spkg extension of Sage packages and pointers to more info.

Issue created by migration from https://trac.sagemath.org/ticket/4504





---

archive/issue_comments_033373.json:
```json
{
    "body": "brief info on the .spkg extension",
    "created_at": "2008-11-12T22:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33373",
    "user": "mvngu"
}
```

brief info on the .spkg extension



---

archive/issue_comments_033374.json:
```json
{
    "body": "Attachment [trac_4504.patch](tarball://root/attachments/some-uuid/ticket4504/trac_4504.patch) by mvngu created at 2008-11-12 23:00:07\n\nThe patch **trac_4504.patch** creates a new file to briefly explain Sage's .spkg files. It also contains pointers to more info on the structure of Sage packages. It was created using sage-3.1.4 and the new file to be created by this patch should be\n\n```\nSAGE_ROOT/spkg/README.txt\n```\n",
    "created_at": "2008-11-12T23:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33374",
    "user": "mvngu"
}
```

Attachment [trac_4504.patch](tarball://root/attachments/some-uuid/ticket4504/trac_4504.patch) by mvngu created at 2008-11-12 23:00:07

The patch **trac_4504.patch** creates a new file to briefly explain Sage's .spkg files. It also contains pointers to more info on the structure of Sage packages. It was created using sage-3.1.4 and the new file to be created by this patch should be

```
SAGE_ROOT/spkg/README.txt
```




---

archive/issue_comments_033375.json:
```json
{
    "body": "Changing assignee from tba to mvngu.",
    "created_at": "2008-11-12T23:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33375",
    "user": "mvngu"
}
```

Changing assignee from tba to mvngu.



---

archive/issue_comments_033376.json:
```json
{
    "body": "Looks fine. Thumbs up!",
    "created_at": "2008-11-13T00:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33376",
    "user": "GeorgSWeber"
}
```

Looks fine. Thumbs up!



---

archive/issue_comments_033377.json:
```json
{
    "body": "This won't work since it will not survive an -sdist. I am not quit sure where to best stick it, but somewhere in the doc or the global README.txt would be easier.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T00:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33377",
    "user": "mabshoff"
}
```

This won't work since it will not survive an -sdist. I am not quit sure where to best stick it, but somewhere in the doc or the global README.txt would be easier.

Cheers,

Michael



---

archive/issue_comments_033378.json:
```json
{
    "body": "Changing assignee from mvngu to @williamstein.",
    "created_at": "2008-11-13T05:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33378",
    "user": "@williamstein"
}
```

Changing assignee from mvngu to @williamstein.



---

archive/issue_comments_033379.json:
```json
{
    "body": "1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!\n\n2. Michael -- the file is in the right place.  The solution is to modify the -sdist command so that it copies the new README.txt file into the right place.   This will have to be done as a patch to the hg_scripts directory (SAGE_ROOT/local/bin/).\n\n3. One thing that concerns me is it would also be good to have a different README.txt for binaries (i.e., bdist), since then spkg/standard has all the same spkg's, but they are empty!\n\nWilliam",
    "created_at": "2008-11-13T05:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33379",
    "user": "@williamstein"
}
```

1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!

2. Michael -- the file is in the right place.  The solution is to modify the -sdist command so that it copies the new README.txt file into the right place.   This will have to be done as a patch to the hg_scripts directory (SAGE_ROOT/local/bin/).

3. One thing that concerns me is it would also be good to have a different README.txt for binaries (i.e., bdist), since then spkg/standard has all the same spkg's, but they are empty!

William



---

archive/issue_comments_033380.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> 1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!\n\n\nBefore making the patch, I loaded up a console Sage session and investigated all the `hg_*` family of commands. But I wasn't able to find one that would allow me to work with the directory `SAGE_ROOT/spkg`. So from the `SAGE_ROOT` directory, I executed the command `hg init`, created the file `SAGE_ROOT/spkg/README.txt`, and executed the command `hg add spkg/README.txt`. Then I edited that README.txt file with the text:\n\n```\nSage packages \n============= \n\nThis directory contains core Sage packages.  Sage packages are \ndistributed as .spkg files, which are .tar.bz2 files (or tar files) \nbut have the extension .spkg to discourage confusion.  Although Sage \npackages are packed using tar and/or bzip2, please note that .spkg \nfiles contain control information (installation scripts and metadata) \nthat are necessary for building and installing them.  For more \ninformation on the structure of .spkg files, please refer to the Sage \nDeveloper's Guide in your local installation of Sage at \n\nSAGE_ROOT/devel/doc-main/html/prog/index.html \n\nor visit the URL \n\nhttp://www.sagemath.org/doc/prog \n\nAdditional Sage packages can be found at \n\nhttp://www.sagemath.org/download-packages.html \n```\n\nI then used mercurial to create the above patch. It was very careless of me not to mention that earlier. Sorry, folks. But if you're having trouble applying the patch, then perhaps you or the release manager can create the file `SAGE_ROOT/spkg/README.txt` with the above text.",
    "created_at": "2008-11-13T22:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33380",
    "user": "mvngu"
}
```

Replying to [comment:4 was]:
> 1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!


Before making the patch, I loaded up a console Sage session and investigated all the `hg_*` family of commands. But I wasn't able to find one that would allow me to work with the directory `SAGE_ROOT/spkg`. So from the `SAGE_ROOT` directory, I executed the command `hg init`, created the file `SAGE_ROOT/spkg/README.txt`, and executed the command `hg add spkg/README.txt`. Then I edited that README.txt file with the text:

```
Sage packages 
============= 

This directory contains core Sage packages.  Sage packages are 
distributed as .spkg files, which are .tar.bz2 files (or tar files) 
but have the extension .spkg to discourage confusion.  Although Sage 
packages are packed using tar and/or bzip2, please note that .spkg 
files contain control information (installation scripts and metadata) 
that are necessary for building and installing them.  For more 
information on the structure of .spkg files, please refer to the Sage 
Developer's Guide in your local installation of Sage at 

SAGE_ROOT/devel/doc-main/html/prog/index.html 

or visit the URL 

http://www.sagemath.org/doc/prog 

Additional Sage packages can be found at 

http://www.sagemath.org/download-packages.html 
```

I then used mercurial to create the above patch. It was very careless of me not to mention that earlier. Sorry, folks. But if you're having trouble applying the patch, then perhaps you or the release manager can create the file `SAGE_ROOT/spkg/README.txt` with the above text.



---

archive/issue_comments_033381.json:
```json
{
    "body": "A possible solution would be to put this file in another location, and adapt \"sage -sdist\" so that it is copied to the intended place.\n\nThen we would need another \"README.txt\" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in \"another location\", and copied by \"sage -bdist\" to the very same place.\n\nI don't think this is a ticket to prevent 3.2 from going out, so I bump the Milestone up.",
    "created_at": "2008-11-14T22:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33381",
    "user": "GeorgSWeber"
}
```

A possible solution would be to put this file in another location, and adapt "sage -sdist" so that it is copied to the intended place.

Then we would need another "README.txt" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in "another location", and copied by "sage -bdist" to the very same place.

I don't think this is a ticket to prevent 3.2 from going out, so I bump the Milestone up.



---

archive/issue_comments_033382.json:
```json
{
    "body": "Replying to [comment:6 GeorgSWeber]:\n> Then we would need another \"README.txt\" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in \"another location\", and copied by \"sage -bdist\" to the very same place.\n\n\nI'm not at all familiar with binary distros of Sage, since I've never got hold of a copy of a binary release. So in that sense, I'm not exactly sure how to go about writing the README.txt that you suggest. But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch.",
    "created_at": "2008-11-20T22:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33382",
    "user": "mvngu"
}
```

Replying to [comment:6 GeorgSWeber]:
> Then we would need another "README.txt" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in "another location", and copied by "sage -bdist" to the very same place.


I'm not at all familiar with binary distros of Sage, since I've never got hold of a copy of a binary release. So in that sense, I'm not exactly sure how to go about writing the README.txt that you suggest. But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch.



---

archive/issue_comments_033383.json:
```json
{
    "body": ">But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch. \nNot really --- in a binary distro, the files \"sage_scripts-3.2.spgk\" and so on all exist, but they are all empty files. The \"spkg/standard\" directory then looks pretty much the same as the \"spkg/installed\" directory, there is no real data contained in it except for the list of names of empty files. Which is confusing and deserves some kind of explanatory \"README.txt\", which would have to explain this.",
    "created_at": "2008-11-21T11:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33383",
    "user": "GeorgSWeber"
}
```

>But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch. 
Not really --- in a binary distro, the files "sage_scripts-3.2.spgk" and so on all exist, but they are all empty files. The "spkg/standard" directory then looks pretty much the same as the "spkg/installed" directory, there is no real data contained in it except for the list of names of empty files. Which is confusing and deserves some kind of explanatory "README.txt", which would have to explain this.



---

archive/issue_comments_033384.json:
```json
{
    "body": "BTW --- if you have a sage src distro, just issue \"sage -bdist my_version\" and a binary distribution will be built. You can look at it then (in \"$SAGE_ROOT/dist/\" if I remember correctly).",
    "created_at": "2008-11-21T12:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33384",
    "user": "GeorgSWeber"
}
```

BTW --- if you have a sage src distro, just issue "sage -bdist my_version" and a binary distribution will be built. You can look at it then (in "$SAGE_ROOT/dist/" if I remember correctly).



---

archive/issue_comments_033385.json:
```json
{
    "body": "Attachment [trac_4504-spkg-src.tex](tarball://root/attachments/some-uuid/ticket4504/trac_4504-spkg-src.tex) by mvngu created at 2008-12-06 01:50:25\n\nexplain .spkg files for source distros",
    "created_at": "2008-12-06T01:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33385",
    "user": "mvngu"
}
```

Attachment [trac_4504-spkg-src.tex](tarball://root/attachments/some-uuid/ticket4504/trac_4504-spkg-src.tex) by mvngu created at 2008-12-06 01:50:25

explain .spkg files for source distros



---

archive/issue_comments_033386.json:
```json
{
    "body": "explain .spkg for binary distros",
    "created_at": "2008-12-06T01:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33386",
    "user": "mvngu"
}
```

explain .spkg for binary distros



---

archive/issue_comments_033387.json:
```json
{
    "body": "Attachment [trac_4504-spkg-bin.tex](tarball://root/attachments/some-uuid/ticket4504/trac_4504-spkg-bin.tex) by mvngu created at 2008-12-06 02:08:59\n\nThe files **trac_4504-spkg-src.tex** and **trac_4504-spkg-bin.tex** are readme files that briefly explain Sage's .spkg extensions. Due to some stupidity on my part, I named them with the \".tex\" extension and forgot to change the \".tex\" to \".txt\". Sorry folks.\n\n\n\nThe file **trac_4504-spkg-src.tex** gives some brief explanation about files with the .spkg extension as part of their name. That is, **trac_4504-spkg-src.tex** is a replacement for **trac_4504.patch**, so we can ignore **trac_4504.patch**. For source distributions of Sage, **trac_4504-spkg-src.tex** should be renamed to \"README.txt\" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.\n\n\n\nThe file **trac_4504-spkg-bin.tex** gives some brief explanation about the empty .spkg files found in binary distributions of Sage. For binary distributions of Sage, **trac_4504-spkg-bin.tex** should be renamed to \"README.txt\" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.",
    "created_at": "2008-12-06T02:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33387",
    "user": "mvngu"
}
```

Attachment [trac_4504-spkg-bin.tex](tarball://root/attachments/some-uuid/ticket4504/trac_4504-spkg-bin.tex) by mvngu created at 2008-12-06 02:08:59

The files **trac_4504-spkg-src.tex** and **trac_4504-spkg-bin.tex** are readme files that briefly explain Sage's .spkg extensions. Due to some stupidity on my part, I named them with the ".tex" extension and forgot to change the ".tex" to ".txt". Sorry folks.



The file **trac_4504-spkg-src.tex** gives some brief explanation about files with the .spkg extension as part of their name. That is, **trac_4504-spkg-src.tex** is a replacement for **trac_4504.patch**, so we can ignore **trac_4504.patch**. For source distributions of Sage, **trac_4504-spkg-src.tex** should be renamed to "README.txt" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.



The file **trac_4504-spkg-bin.tex** gives some brief explanation about the empty .spkg files found in binary distributions of Sage. For binary distributions of Sage, **trac_4504-spkg-bin.tex** should be renamed to "README.txt" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.



---

archive/issue_comments_033388.json:
```json
{
    "body": "Hi,\n\nRight now in a fresh install of sage-3.2.2.alpha0, there is a README.txt file in spkg/standard/.  It is simply an OLD out-of-date version of the README.txt file in SAGE_ROOT.  I think it should be completely deleted.  Then a file README.txt in the spkg directory should be created with two short sections, and those sections should contain the text mvngu wrote.  That's it.\n\nI'm not convinced about having all the extra infrastructure for two separate readme's for the source and binary versions of Sage.  Even if that is a good idea, it could be a separate ticket, since as is, this ticket would not be in \"with patch; needs review\" status if that extra stuff has to be done. \n\nSo in short, I suggest doing the following:\n1. (see attached patch trac_4504_scripts.patch) Add the line\n\n```\ncp -p $PKGDIR/README.txt $TMP/$PKGDIR/\n```\n\nas line 64 of local/bin/sage-sdist. The analogue of this is currently already done in sage-bdist (line 90).  \n\n2. Delete spkg/standard/README.txt\n\n3. Make a new spkg/README.txt file that has two sections, one for each of Minh's patches. \n\nBy the way, it's been suggested above that the spkg/standard/*.spkg files are empty in a bdist.  They aren't empty. They contain the single sentence: \"Placeholder spkg file so this binary version of Sage knows this package version used when installing Sage.\"\n\n\nAlso, I have issues with the actual wording of mvngu's patch, which is:\n\n```\n4 \tIf you've downloaded a binary distribution of Sage, you'd likely see\n5 \ta number of files with the extension \".spkg\" under the directory\n6 \tSAGE_ROOT/spkg. In a binary distribution of Sage, such files are empty\n7 \tfiles and you don't need to do anything about them. Just ignore such\n8 \tfiles for the moment.\n9 \t\n10 \tHowever, note that in a source distribution of Sage, .spkg files under\n11 \tSAGE_ROOT/spkg are core Sage packages, which extend Sage's\n12 \tfunctionalities.\n```\n\n\nFirst, there are no spkg files in SAGE_ROOT/spkg; they are in SAGE_ROOT/spkg/standard/.\nSecond, it's not \"likely\" -- they will always be there with probability 1.\nThird, they aren't empty, as mentioned above. \nFourth, in the case of source they don't \"extend Sage's functionalities\", they *are* the source code that defines Sage.    So I would replace all the above with:\n\n```\nThe directories SAGE_ROOT/spkg/standard and SAGE_ROOT/spkg/optional contain spkg's.  \nIn a source install, these are all Sage spkg files (actually .tar or .tar.bz2 files), which are the source code that defines Sage.  In a binary install some of these may be small placeholder files to save space.\n```\n",
    "created_at": "2008-12-06T21:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33388",
    "user": "@williamstein"
}
```

Hi,

Right now in a fresh install of sage-3.2.2.alpha0, there is a README.txt file in spkg/standard/.  It is simply an OLD out-of-date version of the README.txt file in SAGE_ROOT.  I think it should be completely deleted.  Then a file README.txt in the spkg directory should be created with two short sections, and those sections should contain the text mvngu wrote.  That's it.

I'm not convinced about having all the extra infrastructure for two separate readme's for the source and binary versions of Sage.  Even if that is a good idea, it could be a separate ticket, since as is, this ticket would not be in "with patch; needs review" status if that extra stuff has to be done. 

So in short, I suggest doing the following:
1. (see attached patch trac_4504_scripts.patch) Add the line

```
cp -p $PKGDIR/README.txt $TMP/$PKGDIR/
```

as line 64 of local/bin/sage-sdist. The analogue of this is currently already done in sage-bdist (line 90).  

2. Delete spkg/standard/README.txt

3. Make a new spkg/README.txt file that has two sections, one for each of Minh's patches. 

By the way, it's been suggested above that the spkg/standard/*.spkg files are empty in a bdist.  They aren't empty. They contain the single sentence: "Placeholder spkg file so this binary version of Sage knows this package version used when installing Sage."


Also, I have issues with the actual wording of mvngu's patch, which is:

```
4 	If you've downloaded a binary distribution of Sage, you'd likely see
5 	a number of files with the extension ".spkg" under the directory
6 	SAGE_ROOT/spkg. In a binary distribution of Sage, such files are empty
7 	files and you don't need to do anything about them. Just ignore such
8 	files for the moment.
9 	
10 	However, note that in a source distribution of Sage, .spkg files under
11 	SAGE_ROOT/spkg are core Sage packages, which extend Sage's
12 	functionalities.
```


First, there are no spkg files in SAGE_ROOT/spkg; they are in SAGE_ROOT/spkg/standard/.
Second, it's not "likely" -- they will always be there with probability 1.
Third, they aren't empty, as mentioned above. 
Fourth, in the case of source they don't "extend Sage's functionalities", they *are* the source code that defines Sage.    So I would replace all the above with:

```
The directories SAGE_ROOT/spkg/standard and SAGE_ROOT/spkg/optional contain spkg's.  
In a source install, these are all Sage spkg files (actually .tar or .tar.bz2 files), which are the source code that defines Sage.  In a binary install some of these may be small placeholder files to save space.
```




---

archive/issue_comments_033389.json:
```json
{
    "body": "Attachment [trac_4504_scripts_sdist.patch](tarball://root/attachments/some-uuid/ticket4504/trac_4504_scripts_sdist.patch) by @williamstein created at 2008-12-06 21:50:24",
    "created_at": "2008-12-06T21:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33389",
    "user": "@williamstein"
}
```

Attachment [trac_4504_scripts_sdist.patch](tarball://root/attachments/some-uuid/ticket4504/trac_4504_scripts_sdist.patch) by @williamstein created at 2008-12-06 21:50:24



---

archive/issue_comments_033390.json:
```json
{
    "body": "The attached file **trac_4504-draft2.txt** is a revised draft of a README file explaining Sage's .spkg extension. This second draft has been re-worded and incorporates suggestions by [comment:12 was]. Draft 2 replaces **trac_4504-spkg-src.tex** and **trac_4504-spkg-bin.tex**. \n\n\n\nSo at the moment, the job of the reviewer(s) is to review the patch **trac_4504_scripts_sdist.patch** and the text file **trac_4504-draft2.txt**.",
    "created_at": "2008-12-07T21:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33390",
    "user": "mvngu"
}
```

The attached file **trac_4504-draft2.txt** is a revised draft of a README file explaining Sage's .spkg extension. This second draft has been re-worded and incorporates suggestions by [comment:12 was]. Draft 2 replaces **trac_4504-spkg-src.tex** and **trac_4504-spkg-bin.tex**. 



So at the moment, the job of the reviewer(s) is to review the patch **trac_4504_scripts_sdist.patch** and the text file **trac_4504-draft2.txt**.



---

archive/issue_comments_033391.json:
```json
{
    "body": "Is it worth changing\n\n```\nSAGE_ROOT/devel/doc-main/html/prog/index.html \n```\n\nto\n\n```\nSAGE_ROOT/doc/prog/index.html \n```\n\nin the various places in which this occurs?",
    "created_at": "2008-12-09T22:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33391",
    "user": "@jhpalmieri"
}
```

Is it worth changing

```
SAGE_ROOT/devel/doc-main/html/prog/index.html 
```

to

```
SAGE_ROOT/doc/prog/index.html 
```

in the various places in which this occurs?



---

archive/issue_comments_033392.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> Is it worth changing\n> {{{\n> SAGE_ROOT/devel/doc-main/html/prog/index.html \n> }}}\n> to\n> {{{\n> SAGE_ROOT/doc/prog/index.html \n> }}}\n> in the various places in which this occurs?\n\n\nI don't have a copy of Sage with me at the moment, but I think `SAGE_ROOT/doc` is a symbolic link to `SAGE_ROOT/devel/doc-main`. If in the future the official documentation is moved to somewhere else, say `SAGE_ROOT/path/to/doc-main`, then I would expect that `SAGE_ROOT/doc` would still point to `SAGE_ROOT/path/to/doc-main`. If that is the case, and a reason for having a symbolic link to doc-main, then we should use the symbolic link instead of the path to doc-main.",
    "created_at": "2008-12-09T22:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33392",
    "user": "mvngu"
}
```

Replying to [comment:14 jhpalmieri]:
> Is it worth changing
> {{{
> SAGE_ROOT/devel/doc-main/html/prog/index.html 
> }}}
> to
> {{{
> SAGE_ROOT/doc/prog/index.html 
> }}}
> in the various places in which this occurs?


I don't have a copy of Sage with me at the moment, but I think `SAGE_ROOT/doc` is a symbolic link to `SAGE_ROOT/devel/doc-main`. If in the future the official documentation is moved to somewhere else, say `SAGE_ROOT/path/to/doc-main`, then I would expect that `SAGE_ROOT/doc` would still point to `SAGE_ROOT/path/to/doc-main`. If that is the case, and a reason for having a symbolic link to doc-main, then we should use the symbolic link instead of the path to doc-main.



---

archive/issue_comments_033393.json:
```json
{
    "body": "Target time for the review: January 14th",
    "created_at": "2008-12-29T21:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33393",
    "user": "GeorgSWeber"
}
```

Target time for the review: January 14th



---

archive/issue_comments_033394.json:
```json
{
    "body": "Review: Looks good, but I have to test it against 3.3.alpha0 yet.",
    "created_at": "2009-01-20T23:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33394",
    "user": "GeorgSWeber"
}
```

Review: Looks good, but I have to test it against 3.3.alpha0 yet.



---

archive/issue_comments_033395.json:
```json
{
    "body": "Hi Michael,\n\nthis can go as-is into 3.3. There are three things to do:\n\nA) Delete the \"README.txt\" file (no repo) under $SAGE_ROOT/spkg/standard/\n\nB) Copy the \"trac_4504-draft2.txt\" as \"README.txt\" file under $SAGE_ROOT/spkg/\n   (this is intentionally one directory \"above\" where the old file was)\n\nC) Apply the patch \"trac_4504_scripts_sdist.patch\" from William to /local/bin\n\nTested with 3.3.rc0.\n\nCheers, gsw",
    "created_at": "2009-02-14T23:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33395",
    "user": "GeorgSWeber"
}
```

Hi Michael,

this can go as-is into 3.3. There are three things to do:

A) Delete the "README.txt" file (no repo) under $SAGE_ROOT/spkg/standard/

B) Copy the "trac_4504-draft2.txt" as "README.txt" file under $SAGE_ROOT/spkg/
   (this is intentionally one directory "above" where the old file was)

C) Apply the patch "trac_4504_scripts_sdist.patch" from William to /local/bin

Tested with 3.3.rc0.

Cheers, gsw



---

archive/issue_comments_033396.json:
```json
{
    "body": "I consider this patch too risky since it has to be tested via sdisting given the issue that is fixes, so better luck post 3.3 :(\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T01:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33396",
    "user": "mabshoff"
}
```

I consider this patch too risky since it has to be tested via sdisting given the issue that is fixes, so better luck post 3.3 :(

Cheers,

Michael



---

archive/issue_comments_033397.json:
```json
{
    "body": "Understandable. Given that we do not need a rebase for 3.4.1, and the \"minor\" priority of this ticket, a wise decision. Good luck for 3.3!\n\nCheers, gsw",
    "created_at": "2009-02-15T10:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33397",
    "user": "GeorgSWeber"
}
```

Understandable. Given that we do not need a rebase for 3.4.1, and the "minor" priority of this ticket, a wise decision. Good luck for 3.3!

Cheers, gsw



---

archive/issue_comments_033398.json:
```json
{
    "body": "Replying to [comment:21 GeorgSWeber]:\n> Understandable. Given that we do not need a rebase for 3.4.1, and the \"minor\" priority of this ticket, a wise decision. Good luck for 3.3!\n\nWell, there will be non-trivial work done on -sdist and -bdist in 3.4, so this time might also go in. We will see.\n\n> Cheers, gsw\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T10:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33398",
    "user": "mabshoff"
}
```

Replying to [comment:21 GeorgSWeber]:
> Understandable. Given that we do not need a rebase for 3.4.1, and the "minor" priority of this ticket, a wise decision. Good luck for 3.3!

Well, there will be non-trivial work done on -sdist and -bdist in 3.4, so this time might also go in. We will see.

> Cheers, gsw

Cheers,

Michael



---

archive/issue_comments_033399.json:
```json
{
    "body": "I think some parts of **trac_4504-draft2.txt** needs to be rewritten to take into account changes in where the doc directory has been moved to in the Sage 3.4.x series. I intend to do a 3rd draft some time in the next few days, unless someone beats me to it.",
    "created_at": "2009-03-19T02:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33399",
    "user": "mvngu"
}
```

I think some parts of **trac_4504-draft2.txt** needs to be rewritten to take into account changes in where the doc directory has been moved to in the Sage 3.4.x series. I intend to do a 3rd draft some time in the next few days, unless someone beats me to it.



---

archive/issue_comments_033400.json:
```json
{
    "body": "updated 2nd draft",
    "created_at": "2009-03-24T09:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33400",
    "user": "mvngu"
}
```

updated 2nd draft



---

archive/issue_comments_033401.json:
```json
{
    "body": "Attachment [trac_4504-draft2.txt](tarball://root/attachments/some-uuid/ticket4504/trac_4504-draft2.txt) by mvngu created at 2009-03-24 09:31:08\n\nThe file **trac_4504-draft2.txt** is an updated 2nd draft to reflect changes in where the standard documentation is now located since Sage 3.4.",
    "created_at": "2009-03-24T09:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33401",
    "user": "mvngu"
}
```

Attachment [trac_4504-draft2.txt](tarball://root/attachments/some-uuid/ticket4504/trac_4504-draft2.txt) by mvngu created at 2009-03-24 09:31:08

The file **trac_4504-draft2.txt** is an updated 2nd draft to reflect changes in where the standard documentation is now located since Sage 3.4.



---

archive/issue_comments_033402.json:
```json
{
    "body": "Yep, positive review (again).\n\nThe patch from William still applies as-is to Sage-3.4. (See me A-B-C step procedure above.)\n\nCheers,\ngsw",
    "created_at": "2009-03-24T20:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33402",
    "user": "GeorgSWeber"
}
```

Yep, positive review (again).

The patch from William still applies as-is to Sage-3.4. (See me A-B-C step procedure above.)

Cheers,
gsw



---

archive/issue_comments_033403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T04:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33403",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_033404.json:
```json
{
    "body": "Merged trac_4504_scripts_sdist.patch and trac_4504-draft2.txt in 4.0.1.alpha0.",
    "created_at": "2009-06-01T04:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4504#issuecomment-33404",
    "user": "@mwhansen"
}
```

Merged trac_4504_scripts_sdist.patch and trac_4504-draft2.txt in 4.0.1.alpha0.
