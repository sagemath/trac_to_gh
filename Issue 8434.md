# Issue 8434: sage -g uses user's PYTHONPATH

archive/issues_008434.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  alexanderdreyer\n\nHi alltogether,\nI currently work with the sage-4.3.3-linux-64bit-opensuse_11.1_x86_64-x86_64-Linux.tar.gz binary from sagemath.org on SuSE 11.1/x86_64.\n\n```\n./sage\n./sage -b\n```\n\ninstalls stuff the users PYTHONPATH, not in the corresponding path of sage.\n\nFor instance, see:\n\n```\nbyte-compiling /u/d/dreyer/.local//lib/python2.6/site-packages/sage/ext/gen_interpreters.py to gen_interpreters.pyc\nrunning install_egg_info\nWriting /u/d/dreyer/.local//lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n```\n\n\nI think, sage should overwrite PYTHONPATH in its own environment, doesn't it?\n\nRegards,\n  Alexander Dreyer\n\nIssue created by migration from https://trac.sagemath.org/ticket/8434\n\n",
    "created_at": "2010-03-04T09:32:46Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -g uses user's PYTHONPATH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8434",
    "user": "PolyBoRi"
}
```
Assignee: GeorgSWeber

CC:  alexanderdreyer

Hi alltogether,
I currently work with the sage-4.3.3-linux-64bit-opensuse_11.1_x86_64-x86_64-Linux.tar.gz binary from sagemath.org on SuSE 11.1/x86_64.

```
./sage
./sage -b
```

installs stuff the users PYTHONPATH, not in the corresponding path of sage.

For instance, see:

```
byte-compiling /u/d/dreyer/.local//lib/python2.6/site-packages/sage/ext/gen_interpreters.py to gen_interpreters.pyc
running install_egg_info
Writing /u/d/dreyer/.local//lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
```


I think, sage should overwrite PYTHONPATH in its own environment, doesn't it?

Regards,
  Alexander Dreyer

Issue created by migration from https://trac.sagemath.org/ticket/8434





---

archive/issue_comments_075702.json:
```json
{
    "body": "Hello, I think this is just the same as #9536. Its fix should cures this problem.\n\nRegards,\n\n    Alexander",
    "created_at": "2010-08-19T06:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75702",
    "user": "@alexanderdreyer"
}
```

Hello, I think this is just the same as #9536. Its fix should cures this problem.

Regards,

    Alexander



---

archive/issue_comments_075703.json:
```json
{
    "body": "`./sage -b` uses the right path here.",
    "created_at": "2014-03-05T23:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75703",
    "user": "@a-andre"
}
```

`./sage -b` uses the right path here.



---

archive/issue_comments_075704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-05T23:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75704",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075705.json:
```json
{
    "body": "* `src/bin/sage-env:371...` changes `PYTHONPATH` and `PYTHONHOME` if it has found its own python, so the original `PYTHONPATH` gets used if there is no Sage python, which seems reasonable\n* `src/bin/sage-spkg:161...` does some sanitizing *after sourcing the env, if I'm not mistaken\n\nNo additional appearance of `PYTHONPATH` in `src/`. Let's assume that the env is always sourced, so the ticket seems invalid to me.",
    "created_at": "2014-03-24T16:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75705",
    "user": "@rwst"
}
```

* `src/bin/sage-env:371...` changes `PYTHONPATH` and `PYTHONHOME` if it has found its own python, so the original `PYTHONPATH` gets used if there is no Sage python, which seems reasonable
* `src/bin/sage-spkg:161...` does some sanitizing *after sourcing the env, if I'm not mistaken

No additional appearance of `PYTHONPATH` in `src/`. Let's assume that the env is always sourced, so the ticket seems invalid to me.



---

archive/issue_comments_075706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-24T16:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75706",
    "user": "@rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075707.json:
```json
{
    "body": "This was long, long time ago (perhaps even in a galaxy far, far away ...). So I assume the issue was just fixed meanwhile by incidence the. So feel free to close this now.",
    "created_at": "2014-03-25T11:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75707",
    "user": "@alexanderdreyer"
}
```

This was long, long time ago (perhaps even in a galaxy far, far away ...). So I assume the issue was just fixed meanwhile by incidence the. So feel free to close this now.



---

archive/issue_comments_075708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-31T12:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8434#issuecomment-75708",
    "user": "@vbraun"
}
```

Resolution: fixed
