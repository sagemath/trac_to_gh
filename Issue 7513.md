# Issue 7513: Update Mercurial to 1.4

archive/issues_007513.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif jdemeyer\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7513\n\n",
    "created_at": "2009-11-22T06:23:45Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Update Mercurial to 1.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7513",
    "user": "mhansen"
}
```
Assignee: tbd

CC:  leif jdemeyer



Issue created by migration from https://trac.sagemath.org/ticket/7513





---

archive/issue_comments_063599.json:
```json
{
    "body": "Changing keywords from \"\" to \"hg spkg\".",
    "created_at": "2010-09-01T17:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63599",
    "user": "leif"
}
```

Changing keywords from "" to "hg spkg".



---

archive/issue_comments_063600.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-01T23:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63600",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063601.json:
```json
{
    "body": "Attachment [trac_7513-clean_up_spkg-install_SPKG.txt-reviewer.patch](tarball://root/attachments/some-uuid/ticket7513/trac_7513-clean_up_spkg-install_SPKG.txt-reviewer.patch) by leif created at 2010-11-02 06:37:29\n\nSPKG reviewer patch, based on Jeroen's changes.",
    "created_at": "2010-11-02T06:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63601",
    "user": "leif"
}
```

Attachment [trac_7513-clean_up_spkg-install_SPKG.txt-reviewer.patch](tarball://root/attachments/some-uuid/ticket7513/trac_7513-clean_up_spkg-install_SPKG.txt-reviewer.patch) by leif created at 2010-11-02 06:37:29

SPKG reviewer patch, based on Jeroen's changes.



---

archive/issue_comments_063602.json:
```json
{
    "body": "I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)\n\nJeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).\n\nThen I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.\n\nJeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)",
    "created_at": "2010-11-02T06:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63602",
    "user": "leif"
}
```

I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)

Jeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).

Then I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.

Jeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)



---

archive/issue_comments_063603.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)\nSince the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).\n\n> Jeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).\nThanks for spotting this.\n\n> Then I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.\n> \n> Jeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)\nThanks for looking more carefully at this, I just wanted a new spkg quickly :-)",
    "created_at": "2010-11-02T10:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63603",
    "user": "jdemeyer"
}
```

Replying to [comment:6 leif]:
> I originally wanted to give it immediately a positive review, though `patches/posix.py.patch` (which is redundant and for reference only) had not been updated, but just the line numbers changed. (I haven't updated it either.)
Since the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).

> Jeroen's changes look fine, except `spkg-install` still tried to copy an obsolete, now removed patch (to `setup.py`).
Thanks for spotting this.

> Then I took a closer look at the rest (including `SPKG.txt`), which ended up in my reviewer patch.
> 
> Jeroen, if you agree with my changes, please merge them into the spkg, and I can give it positive review. ;-)
Thanks for looking more carefully at this, I just wanted a new spkg quickly :-)



---

archive/issue_comments_063604.json:
```json
{
    "body": "Leif, I added some minor changes (`7513_review_review.patch`) and posted the resulting spkg at [http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg).  Please review.",
    "created_at": "2010-11-02T10:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63604",
    "user": "jdemeyer"
}
```

Leif, I added some minor changes (`7513_review_review.patch`) and posted the resulting spkg at [http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/mercurial-1.6.4.p0.spkg).  Please review.



---

archive/issue_comments_063605.json:
```json
{
    "body": "Apply on top of leif's patch",
    "created_at": "2010-11-02T10:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63605",
    "user": "jdemeyer"
}
```

Apply on top of leif's patch



---

archive/issue_comments_063606.json:
```json
{
    "body": "Attachment [7513_review_review.patch](tarball://root/attachments/some-uuid/ticket7513/7513_review_review.patch) by leif created at 2010-11-02 10:49:09\n\nReplying to [comment:7 jdemeyer]:\n> Since the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).\n\nObviously. Florent recently complained about a patch of mine that wasn't based on vanilla and so (just) the line numbers changed s.t. Mercurial operated more verbosely than usual. ;-)\n\nIn general it's better to also touch the diffs, or keep them in full sync with the patched files; I've come across spkgs where apparently obsolete files were copied over; and it's confusing when there are dead old patches that do not reflect the current differences.\n \n> Thanks for looking more carefully at this, I just wanted a new spkg quickly :-)\n\nWell, the ticket's first (opening) anniversary is close...",
    "created_at": "2010-11-02T10:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63606",
    "user": "leif"
}
```

Attachment [7513_review_review.patch](tarball://root/attachments/some-uuid/ticket7513/7513_review_review.patch) by leif created at 2010-11-02 10:49:09

Replying to [comment:7 jdemeyer]:
> Since the patch still applies perfectly fine, I don't think it is a problem that the line numbers don't match (note that I created `patches/posix.py` from `patches/posix.py.patch`, not the other way around).

Obviously. Florent recently complained about a patch of mine that wasn't based on vanilla and so (just) the line numbers changed s.t. Mercurial operated more verbosely than usual. ;-)

In general it's better to also touch the diffs, or keep them in full sync with the patched files; I've come across spkgs where apparently obsolete files were copied over; and it's confusing when there are dead old patches that do not reflect the current differences.
 
> Thanks for looking more carefully at this, I just wanted a new spkg quickly :-)

Well, the ticket's first (opening) anniversary is close...



---

archive/issue_comments_063607.json:
```json
{
    "body": "Yes, I forgot to suggest you removing the code commented out.\n\nReviewed reviewer's patch looks ok.\n\nI wasn't sure if quoting the '`$`' was intended or not, but assumed the latter. Giving the effective filename would IMHO be ok, too.\n\nGoing to check the new spkg...",
    "created_at": "2010-11-02T10:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63607",
    "user": "leif"
}
```

Yes, I forgot to suggest you removing the code commented out.

Reviewed reviewer's patch looks ok.

I wasn't sure if quoting the '`$`' was intended or not, but assumed the latter. Giving the effective filename would IMHO be ok, too.

Going to check the new spkg...



---

archive/issue_comments_063608.json:
```json
{
    "body": "Ooops, did you patch/upload the wrong package?\n\nI have a completely different upstream src now... (and the size decreased significantly)",
    "created_at": "2010-11-02T11:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63608",
    "user": "leif"
}
```

Ooops, did you patch/upload the wrong package?

I have a completely different upstream src now... (and the size decreased significantly)



---

archive/issue_comments_063609.json:
```json
{
    "body": "Changing assignee from tbd to leif.",
    "created_at": "2010-11-02T11:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63609",
    "user": "leif"
}
```

Changing assignee from tbd to leif.



---

archive/issue_comments_063610.json:
```json
{
    "body": "Yep, it's the old one again:\n\n```sh\nFinished installing mercurial-1.6.4.p0.spkg\n\nreal\t0m2.384s\nuser\t0m1.960s\nsys\t0m0.430s\nleif@quadriga:~/Sage/sage-4.6$ ./sage -hg --version\nMercurial Distributed SCM (version 1.3.1)\n\nCopyright (C) 2005-2009 Matt Mackall <mpm@selenic.com> and others\nThis is free software; see the source for copying conditions. There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n```\n",
    "created_at": "2010-11-02T11:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63610",
    "user": "leif"
}
```

Yep, it's the old one again:

```sh
Finished installing mercurial-1.6.4.p0.spkg

real	0m2.384s
user	0m1.960s
sys	0m0.430s
leif@quadriga:~/Sage/sage-4.6$ ./sage -hg --version
Mercurial Distributed SCM (version 1.3.1)

Copyright (C) 2005-2009 Matt Mackall <mpm@selenic.com> and others
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```




---

archive/issue_comments_063611.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n> Ooops, did you patch/upload the wrong package?\n> \n> I have a completely different upstream src now... (and the size decreased significantly)\n\nYou are totally right, I forgot to update the `src/` directory when making the new spkg.  I automated this for the PARI spkg and forgot that not every spkg does this automatically :-)",
    "created_at": "2010-11-02T11:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63611",
    "user": "jdemeyer"
}
```

Replying to [comment:11 leif]:
> Ooops, did you patch/upload the wrong package?
> 
> I have a completely different upstream src now... (and the size decreased significantly)

You are totally right, I forgot to update the `src/` directory when making the new spkg.  I automated this for the PARI spkg and forgot that not every spkg does this automatically :-)



---

archive/issue_comments_063612.json:
```json
{
    "body": "Should be fixed now, sorry for this...",
    "created_at": "2010-11-02T11:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63612",
    "user": "jdemeyer"
}
```

Should be fixed now, sorry for this...



---

archive/issue_comments_063613.json:
```json
{
    "body": "\n```\n! patches/setup.py\n! patches/setup.py.patch\n```\n\n;-)",
    "created_at": "2010-11-02T11:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63613",
    "user": "leif"
}
```


```
! patches/setup.py
! patches/setup.py.patch
```

;-)



---

archive/issue_comments_063614.json:
```json
{
    "body": "Next attempt...",
    "created_at": "2010-11-02T11:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63614",
    "user": "jdemeyer"
}
```

Next attempt...



---

archive/issue_comments_063615.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-02T11:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63615",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7513#issuecomment-63616",
    "user": "jdemeyer"
}
```

Resolution: fixed
