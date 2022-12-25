# Issue 8898: some files in sage-4.4.{0,1} have dos line ending instead of a unix line ending

archive/issues_008898.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @fredrik-johansson\n\nthe following 4 files in the sage spkg have dos line ending rather than unix ones:\nsage/libs/mpmath/ext_impl.pxd\nsage/libs/mpmath/ext_main.pyx\nsage/libs/mpmath/ext_main.pxd\nsage/libs/mpmath/ext_libmp.pyx\n\nI found about this while trying to build sage with python-2.6.5\nwhich absolutely refused to parse these files as is.\nNot sure how to submit a patch for line endings.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8898\n\n",
    "created_at": "2010-05-05T23:01:42Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "some files in sage-4.4.{0,1} have dos line ending instead of a unix line ending",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8898",
    "user": "https://github.com/kiwifb"
}
```
Assignee: @aghitza

CC:  @fredrik-johansson

the following 4 files in the sage spkg have dos line ending rather than unix ones:
sage/libs/mpmath/ext_impl.pxd
sage/libs/mpmath/ext_main.pyx
sage/libs/mpmath/ext_main.pxd
sage/libs/mpmath/ext_libmp.pyx

I found about this while trying to build sage with python-2.6.5
which absolutely refused to parse these files as is.
Not sure how to submit a patch for line endings.

Issue created by migration from https://trac.sagemath.org/ticket/8898





---

archive/issue_comments_081690.json:
```json
{
    "body": "Some files under `sage/logic/` also have DOS line ending.",
    "created_at": "2010-05-05T23:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Some files under `sage/logic/` also have DOS line ending.



---

archive/issue_comments_081691.json:
```json
{
    "body": "just checked sage/logic/booleval.py is actually in \"mac format\" in sage-4.4\nI will check sage-4.4.1 later.\nBut those are pure python files, they may be ok but cython with\npython-2.6.5 refused to deal with the other 4.",
    "created_at": "2010-05-05T23:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81691",
    "user": "https://github.com/kiwifb"
}
```

just checked sage/logic/booleval.py is actually in "mac format" in sage-4.4
I will check sage-4.4.1 later.
But those are pure python files, they may be ok but cython with
python-2.6.5 refused to deal with the other 4.



---

archive/issue_comments_081692.json:
```json
{
    "body": "Changing assignee from @aghitza to @jasongrout.",
    "created_at": "2010-09-02T09:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81692",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to @jasongrout.



---

archive/issue_comments_081693.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-09-02T09:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81693",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_081694.json:
```json
{
    "body": "The attached patch converts the following files to use Unix line endings:\n\n* `sage/libs/mpmath/ext_impl.pxd`\n* `sage/libs/mpmath/ext_main.pyx`\n* `sage/libs/mpmath/ext_main.pxd`\n* `sage/libs/mpmath/ext_libmp.pyx`\n* `sage/logic/booleval.py`\n\nI used the Perl script at\n\nhttp://www.obviously.com/tech_tips/dos2unix.html\n\nto convert to Unix end lines. Fredrik Johansson is a main developer of mpmath. I have CC'd him so he is aware of this Unix line endings issue.",
    "created_at": "2010-09-07T11:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The attached patch converts the following files to use Unix line endings:

* `sage/libs/mpmath/ext_impl.pxd`
* `sage/libs/mpmath/ext_main.pyx`
* `sage/libs/mpmath/ext_main.pxd`
* `sage/libs/mpmath/ext_libmp.pyx`
* `sage/logic/booleval.py`

I used the Perl script at

http://www.obviously.com/tech_tips/dos2unix.html

to convert to Unix end lines. Fredrik Johansson is a main developer of mpmath. I have CC'd him so he is aware of this Unix line endings issue.



---

archive/issue_comments_081695.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2010-09-07T11:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_081696.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-07T11:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81696",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081697.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-11T09:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81697",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081698.json:
```json
{
    "body": "sage/libs/mpmath/ext_impl.pxd at least as been changed since this patch has been posted. It may need rebasing for all 4 files.",
    "created_at": "2010-11-11T09:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81698",
    "user": "https://github.com/kiwifb"
}
```

sage/libs/mpmath/ext_impl.pxd at least as been changed since this patch has been posted. It may need rebasing for all 4 files.



---

archive/issue_comments_081699.json:
```json
{
    "body": "Attachment [trac_8898-unix-endlines.2.patch](tarball://root/attachments/some-uuid/ticket8898/trac_8898-unix-endlines.2.patch) by @kiwifb created at 2010-11-11 09:48:47\n\nupdate of the patch based on sage-4.6",
    "created_at": "2010-11-11T09:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81699",
    "user": "https://github.com/kiwifb"
}
```

Attachment [trac_8898-unix-endlines.2.patch](tarball://root/attachments/some-uuid/ticket8898/trac_8898-unix-endlines.2.patch) by @kiwifb created at 2010-11-11 09:48:47

update of the patch based on sage-4.6



---

archive/issue_comments_081700.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-11T09:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81700",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081701.json:
```json
{
    "body": "OK - so I updated the patch (but could not delete the old one, I don't have the\nright to do it).\n\nThis fairly trivial patch now needs a review.",
    "created_at": "2010-11-11T09:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81701",
    "user": "https://github.com/kiwifb"
}
```

OK - so I updated the patch (but could not delete the old one, I don't have the
right to do it).

This fairly trivial patch now needs a review.



---

archive/issue_comments_081702.json:
```json
{
    "body": "I have tested the patch with python-2.6.6 and sage-on-gentoo - everything fine here.",
    "created_at": "2010-11-11T10:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81702",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```

I have tested the patch with python-2.6.6 and sage-on-gentoo - everything fine here.



---

archive/issue_comments_081703.json:
```json
{
    "body": "Attachment [trac-8898_unix-endlines.patch](tarball://root/attachments/some-uuid/ticket8898/trac-8898_unix-endlines.patch) by mvngu created at 2010-11-11 10:57:57\n\nHere are some problems with [attachment:trac_8898-unix-endlines.2.patch]:\n\n* It fails to apply on Sage 4.6.1.alpha0; I got the following failure:\n {{{\n[mvngu`@`sage sage-main]$ pwd\n/dev/shm/mvngu/sage-4.6.1.alpha0/devel/sage-main\n[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8898/trac_8898-unix-endlines.2.patch && hg qpush \nadding trac_8898-unix-endlines.2.patch to series file\napplying trac_8898-unix-endlines.2.patch\npatching file sage/libs/mpmath/ext_main.pyx\nHunk #1 FAILED at 0\n1 out of 1 hunks FAILED -- saving rejects to file sage/libs/mpmath/ext_main.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8898-unix-endlines.2.patch\n }}}\n\n* The attachment [attachment:trac_8898-unix-endlines.2.patch] doesn't convert the file `sage/logic/booleval.py` to use Unix line ending.\n\nMy rebased patch should take care of the above issues for Sage 4.6.1.alpha0. See the ticket description for which patch to apply.",
    "created_at": "2010-11-11T10:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac-8898_unix-endlines.patch](tarball://root/attachments/some-uuid/ticket8898/trac-8898_unix-endlines.patch) by mvngu created at 2010-11-11 10:57:57

Here are some problems with [attachment:trac_8898-unix-endlines.2.patch]:

* It fails to apply on Sage 4.6.1.alpha0; I got the following failure:
 {{{
[mvngu`@`sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.6.1.alpha0/devel/sage-main
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8898/trac_8898-unix-endlines.2.patch && hg qpush 
adding trac_8898-unix-endlines.2.patch to series file
applying trac_8898-unix-endlines.2.patch
patching file sage/libs/mpmath/ext_main.pyx
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/mpmath/ext_main.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8898-unix-endlines.2.patch
 }}}

* The attachment [attachment:trac_8898-unix-endlines.2.patch] doesn't convert the file `sage/logic/booleval.py` to use Unix line ending.

My rebased patch should take care of the above issues for Sage 4.6.1.alpha0. See the ticket description for which patch to apply.



---

archive/issue_comments_081704.json:
```json
{
    "body": "Sorry I missed sage/logic/booleval.py somehow. In any case this one is no bother\nand is only included for consistency. It doesn't prevent building the way the other\ndo and it is usable. I also didn't see there was a change affecting this in 4.6.1.alpha0. I will test it shortly and report.",
    "created_at": "2010-11-12T08:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81704",
    "user": "https://github.com/kiwifb"
}
```

Sorry I missed sage/logic/booleval.py somehow. In any case this one is no bother
and is only included for consistency. It doesn't prevent building the way the other
do and it is usable. I also didn't see there was a change affecting this in 4.6.1.alpha0. I will test it shortly and report.



---

archive/issue_comments_081705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-12T22:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81705",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081706.json:
```json
{
    "body": "4.6.1.alpha0 took me for a little ride.\nAnyway, Minh's new patch applies cleanly to 4.6.1.alpha0 and it compiles\ncleanly with a python-2.6.5 install as expected. sage starts without problems.\nFor safety I also did a run of sage -t --long in the sage/libs/mpmath/ and\nsage/logic/ and everything ran ok.\n\nI am putting this back to positive review, hopefully no one messed up with those\nfiles in alpha1 so it will apply cleanly there as well.",
    "created_at": "2010-11-12T22:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81706",
    "user": "https://github.com/kiwifb"
}
```

4.6.1.alpha0 took me for a little ride.
Anyway, Minh's new patch applies cleanly to 4.6.1.alpha0 and it compiles
cleanly with a python-2.6.5 install as expected. sage starts without problems.
For safety I also did a run of sage -t --long in the sage/libs/mpmath/ and
sage/logic/ and everything ran ok.

I am putting this back to positive review, hopefully no one messed up with those
files in alpha1 so it will apply cleanly there as well.



---

archive/issue_comments_081707.json:
```json
{
    "body": "Script to do the changes (to be executed in SAGE_ROOT/devel/sage)",
    "created_at": "2010-11-13T16:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81707",
    "user": "https://github.com/jdemeyer"
}
```

Script to do the changes (to be executed in SAGE_ROOT/devel/sage)



---

archive/issue_comments_081708.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-13T16:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81708",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081709.json:
```json
{
    "body": "Attachment [8898.sh](tarball://root/attachments/some-uuid/ticket8898/8898.sh) by @jdemeyer created at 2010-11-13 16:23:16",
    "created_at": "2010-11-13T16:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81709",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [8898.sh](tarball://root/attachments/some-uuid/ticket8898/8898.sh) by @jdemeyer created at 2010-11-13 16:23:16



---

archive/issue_comments_081710.json:
```json
{
    "body": "Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.",
    "created_at": "2010-11-13T16:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81710",
    "user": "https://github.com/jdemeyer"
}
```

Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.



---

archive/issue_comments_081711.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-13T16:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81711",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081712.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.\n\n\nNo complaints here. As I initially said my main concern are the cython files.\nI'll be happy if a fix goes in script or patch.",
    "created_at": "2010-11-13T17:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81712",
    "user": "https://github.com/kiwifb"
}
```

Replying to [comment:12 jdemeyer]:
> Any complaints if I execute the script [attachment:8898.sh] instead of applying the patch?  The script also fixes some more files.


No complaints here. As I initially said my main concern are the cython files.
I'll be happy if a fix goes in script or patch.



---

archive/issue_comments_081713.json:
```json
{
    "body": "I am building 4.6.1.alpha2 which includes the fix. cython parsed everything\nwithout trouble using python-2.6.5 and compilation is now underway.\nSo it looks good to me.",
    "created_at": "2010-11-14T09:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81713",
    "user": "https://github.com/kiwifb"
}
```

I am building 4.6.1.alpha2 which includes the fix. cython parsed everything
without trouble using python-2.6.5 and compilation is now underway.
So it looks good to me.



---

archive/issue_comments_081714.json:
```json
{
    "body": "Fran\u00e7ois, I am interpreting your post as a positive review, okay?",
    "created_at": "2010-11-14T15:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81714",
    "user": "https://github.com/jdemeyer"
}
```

François, I am interpreting your post as a positive review, okay?



---

archive/issue_comments_081715.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-14T15:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81715",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081716.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Fran\u00e7ois, I am interpreting your post as a positive review, okay?\n\n\nOK, the build finished successfully, so yes positive review.",
    "created_at": "2010-11-14T18:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81716",
    "user": "https://github.com/kiwifb"
}
```

Replying to [comment:15 jdemeyer]:
> François, I am interpreting your post as a positive review, okay?


OK, the build finished successfully, so yes positive review.



---

archive/issue_events_021714.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-15T23:24:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8898#event-21714"
}
```



---

archive/issue_comments_081717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8898#issuecomment-81717",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
