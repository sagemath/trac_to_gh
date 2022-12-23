# Issue 4191: Update eclib to eclib-20080310.p6.spkg

archive/issues_004191.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: eclib\n\nI applied the patch supplied by Arnaud Bergeron to use ${MAKE} instead of make.  At the same time I changed one line in src/g0n/Makefile, adding ecnf to PROGS since otherwise that binary was being left behind after \"make veryclean\".\n\nI seem to remember that mabsoff said that the effect would be negligible since my Makefiles use gnu-isms anyway, but here it is.\n\nSee also #3358.\n\nI just checked that this installs ok on a fresh 3.1.3.alpha1 build.  A fresh spkg is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4191\n\n",
    "created_at": "2008-09-24T14:54:48Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "Update eclib to eclib-20080310.p6.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4191",
    "user": "cremona"
}
```
Assignee: mabshoff

Keywords: eclib

I applied the patch supplied by Arnaud Bergeron to use ${MAKE} instead of make.  At the same time I changed one line in src/g0n/Makefile, adding ecnf to PROGS since otherwise that binary was being left behind after "make veryclean".

I seem to remember that mabsoff said that the effect would be negligible since my Makefiles use gnu-isms anyway, but here it is.

See also #3358.

I just checked that this installs ok on a fresh 3.1.3.alpha1 build.  A fresh spkg is attached.

Issue created by migration from https://trac.sagemath.org/ticket/4191





---

archive/issue_comments_030417.json:
```json
{
    "body": "John,\n\nplease do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at\n\nhttp://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T20:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4191#issuecomment-30417",
    "user": "mabshoff"
}
```

John,

please do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at

http://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg

Cheers,

Michael



---

archive/issue_comments_030418.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> John,\n> \n> please do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at\n> \n> http://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg\n> \n> Cheers,\n> \n> Michael\n\nVery sorry, I knew I would do something wrong.  Next time I'll just put it somewhere and put in a link.  Now I have a sagemath account that will be easier.",
    "created_at": "2008-09-24T20:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4191#issuecomment-30418",
    "user": "cremona"
}
```

Replying to [comment:2 mabshoff]:
> John,
> 
> please do not attach spkgs since the trac install (and all attachments) are backed up daily and a 1.5mb spkg is rather large. So I have deleted the spkg and it is now at
> 
> http://sage.math.washington.edu/home/mabshoff/eclib-20080310.p6.spkg
> 
> Cheers,
> 
> Michael

Very sorry, I knew I would do something wrong.  Next time I'll just put it somewhere and put in a link.  Now I have a sagemath account that will be easier.



---

archive/issue_comments_030419.json:
```json
{
    "body": "Everything looks good. I deleted on stray SPKG.txt~ from the main directory. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-25T00:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4191#issuecomment-30419",
    "user": "mabshoff"
}
```

Everything looks good. I deleted on stray SPKG.txt~ from the main directory. Positive review.

Cheers,

Michael



---

archive/issue_comments_030420.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-25T00:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4191#issuecomment-30420",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-25T00:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4191#issuecomment-30421",
    "user": "mabshoff"
}
```

Resolution: fixed
