# Issue 5271: clean up jmol-11.6.16.spkg from #2873

archive/issues_005271.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout\n\njmol-11.6.16.spkg from #2873 was **not** based on the latest upstream jmol.spkg. While taking a closer look I found all kind of other odd things, so I moved the updated spkg to a new ticker. The spkg can be found at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/jmol-11.6.16.p0.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5271\n\n",
    "created_at": "2009-02-14T14:30:46Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "clean up jmol-11.6.16.spkg from #2873",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5271",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  @jasongrout

jmol-11.6.16.spkg from #2873 was **not** based on the latest upstream jmol.spkg. While taking a closer look I found all kind of other odd things, so I moved the updated spkg to a new ticker. The spkg can be found at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/jmol-11.6.16.p0.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5271





---

archive/issue_comments_040466.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T14:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40466",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040467.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-14T15:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40467",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_040468.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T15:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40468",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040469.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T15:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40469",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040470.json:
```json
{
    "body": "I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!",
    "created_at": "2009-02-15T05:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40470",
    "user": "@jasongrout"
}
```

I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!



---

archive/issue_comments_040471.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!\n\nWell, it was well worth the update of jmol, I was just not happy at that point that I had to resolve what had happened. Note that the faulty .hgignore that lead to many files being ignored by hg was my fault, but I still do not understand how that happened since I assumed that there was just one directory to be ignore. Anyway, this spkg is much cleaner, conforms with the standard packaging rules, i.e. bits in src. Note that I also blame the reviewed for not catching it, too, since I expect reviewers of spkgs to verify in the repo that the history is not partially truncated. But I do it with *every* spkg anyway :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T06:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5271#issuecomment-40471",
    "user": "mabshoff"
}
```

Replying to [comment:4 jason]:
> I based my changes on the jmol spkg that was sitting in my 3.3alpha3 tree, so I'm surprised it wasn't the latest.  Anyways, thanks for noticing this and taking care of it!

Well, it was well worth the update of jmol, I was just not happy at that point that I had to resolve what had happened. Note that the faulty .hgignore that lead to many files being ignored by hg was my fault, but I still do not understand how that happened since I assumed that there was just one directory to be ignore. Anyway, this spkg is much cleaner, conforms with the standard packaging rules, i.e. bits in src. Note that I also blame the reviewed for not catching it, too, since I expect reviewers of spkgs to verify in the repo that the history is not partially truncated. But I do it with *every* spkg anyway :)

Cheers,

Michael
