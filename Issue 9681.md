# Issue 9681: Missing dependancy in spkg/standard/deps for zn_poly.

archive/issues_009681.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  ddrake mpatel leif jhpalmieri\n\nThe zn_poly package lists in `SPKG.txt` the only dependencies are GMP, but this is not true, as zn_poly's configure script has in it:\n\n\n```\n/configure --gmp-prefix=\"$SAGE_LOCAL\" --ntl-prefix=\"$SAGE_LOCAL\" \\\n            --prefix=\"$SAGE_LOCAL\" --cflags=\"$CFLAGS\" --ldflags=\"$LDFLAGS\"\n```\n\n\nLooking at $SAGE_ROOT/spkg/standard/deps, I see: \n\n\n```\n$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR)\n        $(INSTALL) \"$(SAGE_SPKG) $(ZNPOLY) 2>&1\" \"tee -a $(SAGE_LOGS)/$(ZNPOLY).log\"\n```\n\n\nthen looking at MPIR I see the dependencies are only BASE and ICONV. But ICONV only depends on BASE, so there is nothing to force ntl to build before zn_poly.\n\nI am aware of two other changes that are desirable in the 'deps' file too, as they add clarity. \n\n* #9464 \n* #9637 \n\nThese might as well be fixed at the same time. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9681\n\n",
    "created_at": "2010-08-04T00:32:03Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "Missing dependancy in spkg/standard/deps for zn_poly.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9681",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  ddrake mpatel leif jhpalmieri

The zn_poly package lists in `SPKG.txt` the only dependencies are GMP, but this is not true, as zn_poly's configure script has in it:


```
/configure --gmp-prefix="$SAGE_LOCAL" --ntl-prefix="$SAGE_LOCAL" \
            --prefix="$SAGE_LOCAL" --cflags="$CFLAGS" --ldflags="$LDFLAGS"
```


Looking at $SAGE_ROOT/spkg/standard/deps, I see: 


```
$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR)
        $(INSTALL) "$(SAGE_SPKG) $(ZNPOLY) 2>&1" "tee -a $(SAGE_LOGS)/$(ZNPOLY).log"
```


then looking at MPIR I see the dependencies are only BASE and ICONV. But ICONV only depends on BASE, so there is nothing to force ntl to build before zn_poly.

I am aware of two other changes that are desirable in the 'deps' file too, as they add clarity. 

* #9464 
* #9637 

These might as well be fixed at the same time. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9681





---

archive/issue_comments_094113.json:
```json
{
    "body": "Attachment\n\nUpdated deps file, which solves this major problem and corrects two minor ones in #9464 and #9637",
    "created_at": "2010-08-04T00:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94113",
    "user": "drkirkby"
}
```

Attachment

Updated deps file, which solves this major problem and corrects two minor ones in #9464 and #9637



---

archive/issue_comments_094114.json:
```json
{
    "body": "Attachment\n\nUnifier diff file for $SAGE_ROOT/spkg/standard/deps",
    "created_at": "2010-08-04T00:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94114",
    "user": "drkirkby"
}
```

Attachment

Unifier diff file for $SAGE_ROOT/spkg/standard/deps



---

archive/issue_comments_094115.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-04T00:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94115",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094116.json:
```json
{
    "body": "I've attached an updated 'deps' file, which fixed this major problem and two minor ones - #9464 and #9637. If this ticket is merged, then  #9464 and #9637 can be closed as fixed. \n\nDave",
    "created_at": "2010-08-04T00:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94116",
    "user": "drkirkby"
}
```

I've attached an updated 'deps' file, which fixed this major problem and two minor ones - #9464 and #9637. If this ticket is merged, then  #9464 and #9637 can be closed as fixed. 

Dave



---

archive/issue_comments_094117.json:
```json
{
    "body": "It was only by chance I found this, while trying to resolve a 64-bit Solaris issue, which is #9358. \n\nI'm adding the two release managers to the ticket, as I believe this should be a blocker. \n\nDave",
    "created_at": "2010-08-04T01:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94117",
    "user": "drkirkby"
}
```

It was only by chance I found this, while trying to resolve a 64-bit Solaris issue, which is #9358. 

I'm adding the two release managers to the ticket, as I believe this should be a blocker. 

Dave



---

archive/issue_comments_094118.json:
```json
{
    "body": "Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure).",
    "created_at": "2010-08-04T07:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94118",
    "user": "robertwb"
}
```

Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure).



---

archive/issue_comments_094119.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure). \n\nSome rather subtle problems have been caused by dependencies which have not been correct - I'm thinking in particular of William's failure on OS X to compile some Fortran code, when in fact it was due to the fortran package being dependent on python for a very simple script. The strange thing about that was everyone else had no problems, including me, using William's script on bsd.math. \n\nI would have thought anything that had the potential to mis-compile would be a blocker personally, but that's a personal opinion of course. \n\nDave",
    "created_at": "2010-08-04T08:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94119",
    "user": "drkirkby"
}
```

Replying to [comment:7 robertwb]:
> Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure). 

Some rather subtle problems have been caused by dependencies which have not been correct - I'm thinking in particular of William's failure on OS X to compile some Fortran code, when in fact it was due to the fortran package being dependent on python for a very simple script. The strange thing about that was everyone else had no problems, including me, using William's script on bsd.math. 

I would have thought anything that had the potential to mis-compile would be a blocker personally, but that's a personal opinion of course. 

Dave



---

archive/issue_comments_094120.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-08-04T23:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94120",
    "user": "drkirkby"
}
```

Resolution: wontfix



---

archive/issue_comments_094121.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2010-08-04T23:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94121",
    "user": "drkirkby"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_094122.json:
```json
{
    "body": "Apparently NTL is not needed unless one makes those targets, so this is a non-issue.",
    "created_at": "2010-08-04T23:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9681#issuecomment-94122",
    "user": "drkirkby"
}
```

Apparently NTL is not needed unless one makes those targets, so this is a non-issue.
