# Issue 6938: sage-README-osx.txt is non-sensical for a source distribution.

archive/issues_006938.json:
```json
{
    "body": "Assignee: tba\n\nCC:  drkirkby\n\nThe file sage-README-osx.txt is very confusing. If someone downloads the source, the readme file indicates they have downloaded binaries. \n\nThere should perhaps be two README files - one for source, and one for binaries. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6938\n\n",
    "created_at": "2009-09-15T21:44:18Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "sage-README-osx.txt is non-sensical for a source distribution.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6938",
    "user": "drkirkby"
}
```
Assignee: tba

CC:  drkirkby

The file sage-README-osx.txt is very confusing. If someone downloads the source, the readme file indicates they have downloaded binaries. 

There should perhaps be two README files - one for source, and one for binaries. 

Issue created by migration from https://trac.sagemath.org/ticket/6938





---

archive/issue_comments_057348.json:
```json
{
    "body": "See also #5296.\n\nBy the way, I see two copies of the file \"sage-README-osx.txt\": \n\n- in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.\n- in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.",
    "created_at": "2010-03-31T16:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57348",
    "user": "jhpalmieri"
}
```

See also #5296.

By the way, I see two copies of the file "sage-README-osx.txt": 

- in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
- in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.



---

archive/issue_comments_057349.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> See also #5296.\n> \n> By the way, I see two copies of the file \"sage-README-osx.txt\": \n> \n>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.\n>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.\n> \n\nHmm.  But if both of these are not present in a source distribution, then where will it come from when sage -bdist is run?  It has to be somewhere, right?",
    "created_at": "2010-04-22T01:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57349",
    "user": "kcrisman"
}
```

Replying to [comment:2 jhpalmieri]:
> See also #5296.
> 
> By the way, I see two copies of the file "sage-README-osx.txt": 
> 
>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.
> 

Hmm.  But if both of these are not present in a source distribution, then where will it come from when sage -bdist is run?  It has to be somewhere, right?



---

archive/issue_comments_057350.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> See also #5296.\n> \n> By the way, I see two copies of the file \"sage-README-osx.txt\": \n> \n>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.\n>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.\n> \n\nOh yeah, this one is needed for sage-bdist - see line 92:\n\n```\n    cp sage/local/bin/sage-README-osx.txt README.txt\n```\n\nBut the one on the top level should be able to be safely removed, given that line in sage-bdist, methinks.  Whether the one in /local/bin should overwrite the usual README.txt is another question.  \n\nIncidentally, the usual README.txt maybe should be updated - for instance, Mac OS X is essentially fully supported now, correct?  And Fortran is now only included for OS X, not Linux, I believe. \n\nAnyway, the correct course of action for this ticket is to remove the (untracked?) top-level OSX README file, as far as I can tell.  How does one review this?",
    "created_at": "2010-04-22T02:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57350",
    "user": "kcrisman"
}
```

Replying to [comment:2 jhpalmieri]:
> See also #5296.
> 
> By the way, I see two copies of the file "sage-README-osx.txt": 
> 
>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.
> 

Oh yeah, this one is needed for sage-bdist - see line 92:

```
    cp sage/local/bin/sage-README-osx.txt README.txt
```

But the one on the top level should be able to be safely removed, given that line in sage-bdist, methinks.  Whether the one in /local/bin should overwrite the usual README.txt is another question.  

Incidentally, the usual README.txt maybe should be updated - for instance, Mac OS X is essentially fully supported now, correct?  And Fortran is now only included for OS X, not Linux, I believe. 

Anyway, the correct course of action for this ticket is to remove the (untracked?) top-level OSX README file, as far as I can tell.  How does one review this?



---

archive/issue_comments_057351.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-22T02:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57351",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057352.json:
```json
{
    "body": "One option might be to have a file \".README-OSX-binary.txt\" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt\n\nThe fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. \n\nDave",
    "created_at": "2010-04-22T11:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57352",
    "user": "drkirkby"
}
```

One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt

The fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. 

Dave



---

archive/issue_comments_057353.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-22T13:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57353",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057354.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> One option might be to have a file \".README-OSX-binary.txt\" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt\n> \n\nExcept for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). \n\n> The fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. \n> \n\nThat is also a good solution.  I'll try to work on this over the next week - isn't hard, just have to find time to do it.",
    "created_at": "2010-04-22T13:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57354",
    "user": "kcrisman"
}
```

Replying to [comment:5 drkirkby]:
> One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> 

Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 

> The fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. 
> 

That is also a good solution.  I'll try to work on this over the next week - isn't hard, just have to find time to do it.



---

archive/issue_comments_057355.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Replying to [comment:5 drkirkby]:\n> > One option might be to have a file \".README-OSX-binary.txt\" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt\n> > \n> \n> Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). \n\nThat was my whole point about using a dot - it would not be found easily. \n\nIf the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. \n\nIt would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. \n\nDave",
    "created_at": "2010-04-22T15:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57355",
    "user": "drkirkby"
}
```

Replying to [comment:6 kcrisman]:
> Replying to [comment:5 drkirkby]:
> > One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> > 
> 
> Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 

That was my whole point about using a dot - it would not be found easily. 

If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 

It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 

Dave



---

archive/issue_comments_057356.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> Replying to [comment:6 kcrisman]:\n> > Replying to [comment:5 drkirkby]:\n> > > One option might be to have a file \".README-OSX-binary.txt\" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt\n> > > \n> > \n> > Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). \n> \n> That was my whole point about using a dot - it would not be found easily. \n> \n> If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. \n> \n> It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. \n\nI understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.",
    "created_at": "2010-04-22T17:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57356",
    "user": "kcrisman"
}
```

Replying to [comment:7 drkirkby]:
> Replying to [comment:6 kcrisman]:
> > Replying to [comment:5 drkirkby]:
> > > One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> > > 
> > 
> > Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 
> 
> That was my whole point about using a dot - it would not be found easily. 
> 
> If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 
> 
> It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 

I understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.



---

archive/issue_comments_057357.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Replying to [comment:7 drkirkby]:\n> > That was my whole point about using a dot - it would not be found easily. \n> > \n> > If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. \n> > \n> > It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. \n> \n> I understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.\n\nIt's one option, but I suspect a simpler one is to just have the one file be a bit more explicit about what is relevant to a source distribution, and what is relevant to a binary distribution. \n\nI'm not overly concerned whether it is done in one file, two files, or whether any files are semi-hidden by the use of a dot in front of their name. But the current version is rather confusing.",
    "created_at": "2010-04-22T18:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57357",
    "user": "drkirkby"
}
```

Replying to [comment:8 kcrisman]:
> Replying to [comment:7 drkirkby]:
> > That was my whole point about using a dot - it would not be found easily. 
> > 
> > If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 
> > 
> > It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 
> 
> I understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.

It's one option, but I suspect a simpler one is to just have the one file be a bit more explicit about what is relevant to a source distribution, and what is relevant to a binary distribution. 

I'm not overly concerned whether it is done in one file, two files, or whether any files are semi-hidden by the use of a dot in front of their name. But the current version is rather confusing.



---

archive/issue_comments_057358.json:
```json
{
    "body": "Okay, this is mostly fixed by simply removing the README-osx file from the top directory.  There is no HG for this, so it has to be removed by hand.\n\nThe place the one in /local/bin is copied to is in fact the top directory in a dmg/tgz only when bdisted, which is definitely very appropriate for this file!    \n\nSo I don't think there is a need for any other changes, since any binary would be distributed with the OS X readme, but renamed to README.txt, in that very top directory, where anyone could read it.  They would only have to read the usual README.txt in the sage/ directory if they wanted that sort of information, in which case the information in the OS X README is superfluous (i.e., they know how to use Terminal already).  \n\nDoes that make any sense?  My point is we don't need a separate README for any other purpose.  I'm marking this needs review.  I'm putting myself as an \"author\", but since I didn't actually write anything, if the reviewer disagrees then they can just make me a reviewer.\n\nTo release manager: Upon positive review, remove the sage-README-osx.txt in the top directory, leave the one in local/bin/ alone!",
    "created_at": "2010-04-28T18:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57358",
    "user": "kcrisman"
}
```

Okay, this is mostly fixed by simply removing the README-osx file from the top directory.  There is no HG for this, so it has to be removed by hand.

The place the one in /local/bin is copied to is in fact the top directory in a dmg/tgz only when bdisted, which is definitely very appropriate for this file!    

So I don't think there is a need for any other changes, since any binary would be distributed with the OS X readme, but renamed to README.txt, in that very top directory, where anyone could read it.  They would only have to read the usual README.txt in the sage/ directory if they wanted that sort of information, in which case the information in the OS X README is superfluous (i.e., they know how to use Terminal already).  

Does that make any sense?  My point is we don't need a separate README for any other purpose.  I'm marking this needs review.  I'm putting myself as an "author", but since I didn't actually write anything, if the reviewer disagrees then they can just make me a reviewer.

To release manager: Upon positive review, remove the sage-README-osx.txt in the top directory, leave the one in local/bin/ alone!



---

archive/issue_comments_057359.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T18:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57359",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057360.json:
```json
{
    "body": "If #9433 is merged, this should probably get positive review and marked as merged.  Of course, one could just merge this first anyway, before revision control is implemented :)",
    "created_at": "2010-08-11T13:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57360",
    "user": "kcrisman"
}
```

If #9433 is merged, this should probably get positive review and marked as merged.  Of course, one could just merge this first anyway, before revision control is implemented :)



---

archive/issue_comments_057361.json:
```json
{
    "body": "I'll give this a positive review.  To the release manager: delete the file sage-README-osx.txt in the top directory.\n\nI think doing this won't have any effect on #9433.  If #9433 gets merged first, on the other hand, then this should automatically be taken care of.",
    "created_at": "2010-08-11T20:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57361",
    "user": "jhpalmieri"
}
```

I'll give this a positive review.  To the release manager: delete the file sage-README-osx.txt in the top directory.

I think doing this won't have any effect on #9433.  If #9433 gets merged first, on the other hand, then this should automatically be taken care of.



---

archive/issue_comments_057362.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-11T20:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57362",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6938#issuecomment-57363",
    "user": "mpatel"
}
```

Resolution: fixed
