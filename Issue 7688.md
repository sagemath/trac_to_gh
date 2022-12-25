# Issue 7688: Remove byte-compiled files from extcode

archive/issues_007688.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @ohanar\n\nThere are a few Python byte-compiled files included in the Sage source distribution:\n\n```\njdemeyer@sage:/release/sage-5.4.rc1$ find . -name '*.pyc' |xargs file\n./spkg/standard/extcode/sagebuild/build/__init__.pyc:               python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/action.pyc:                 python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/all.pyc:                    python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/compiler.pyc:               python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/compilers/__init__.pyc:     python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/compilers/all.pyc:          python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/compilers/cython.pyc:       python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/compilers/gcc.pyc:          python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/config.pyc:                 python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/dependencies.pyc:           python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/enviroment.pyc:             python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/filewalker.pyc:             python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/optionmanager.pyc:          python 2.5 byte-compiled\n./spkg/standard/extcode/sagebuild/build/taskmanager.pyc:            python 2.5 byte-compiled\n./spkg/standard/scipy/src/doc/sphinxext/docscrape.pyc:              data\n./spkg/standard/scipy/src/doc/sphinxext/docscrape_sphinx.pyc:       data\n./spkg/standard/scipy/src/doc/sphinxext/numpydoc.pyc:               data\n./spkg/standard/scipy/src/doc/sphinxext/plot_directive.pyc:         data\n./spkg/standard/singular/src/dyn_modules/openmath/context.pyc:      python 2.4 byte-compiled\n./spkg/standard/singular/src/dyn_modules/openmath/omexceptions.pyc: python 2.4 byte-compiled\n./spkg/standard/singular/src/dyn_modules/python/perf.pyc:           python 2.3 byte-compiled\n```\n\nWe should at least remove the ones in extcode, which aren't used anyway.\n\n**Apply** [attachment:7688_extcode_pyc.patch] to `devel/ext` and **run** (these files aren't under revision control):\n\n```\nrm -rf devel/ext/sagebuild\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7688\n\n",
    "closed_at": "2012-10-14T18:55:53Z",
    "created_at": "2009-12-15T19:34:22Z",
    "labels": [
        "component: distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Remove byte-compiled files from extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7688",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @ohanar

There are a few Python byte-compiled files included in the Sage source distribution:

```
jdemeyer@sage:/release/sage-5.4.rc1$ find . -name '*.pyc' |xargs file
./spkg/standard/extcode/sagebuild/build/__init__.pyc:               python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/action.pyc:                 python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/all.pyc:                    python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/compiler.pyc:               python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/compilers/__init__.pyc:     python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/compilers/all.pyc:          python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/compilers/cython.pyc:       python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/compilers/gcc.pyc:          python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/config.pyc:                 python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/dependencies.pyc:           python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/enviroment.pyc:             python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/filewalker.pyc:             python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/optionmanager.pyc:          python 2.5 byte-compiled
./spkg/standard/extcode/sagebuild/build/taskmanager.pyc:            python 2.5 byte-compiled
./spkg/standard/scipy/src/doc/sphinxext/docscrape.pyc:              data
./spkg/standard/scipy/src/doc/sphinxext/docscrape_sphinx.pyc:       data
./spkg/standard/scipy/src/doc/sphinxext/numpydoc.pyc:               data
./spkg/standard/scipy/src/doc/sphinxext/plot_directive.pyc:         data
./spkg/standard/singular/src/dyn_modules/openmath/context.pyc:      python 2.4 byte-compiled
./spkg/standard/singular/src/dyn_modules/openmath/omexceptions.pyc: python 2.4 byte-compiled
./spkg/standard/singular/src/dyn_modules/python/perf.pyc:           python 2.3 byte-compiled
```

We should at least remove the ones in extcode, which aren't used anyway.

**Apply** [attachment:7688_extcode_pyc.patch] to `devel/ext` and **run** (these files aren't under revision control):

```
rm -rf devel/ext/sagebuild
```

Issue created by migration from https://trac.sagemath.org/ticket/7688





---

archive/issue_comments_065852.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-05T09:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65852",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065853.json:
```json
{
    "body": "Shouldn't we keep the DS_Store line for OSX? Or maybe replace it with something like\n\n```\n(^|/)\\.DS_Store$\n(^|/)\\._\\.DS_Store$\n```",
    "created_at": "2012-10-05T19:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65853",
    "user": "https://github.com/ohanar"
}
```

Shouldn't we keep the DS_Store line for OSX? Or maybe replace it with something like

```
(^|/)\.DS_Store$
(^|/)\._\.DS_Store$
```



---

archive/issue_comments_065854.json:
```json
{
    "body": "`devel/sage/.hgignore` has\n\n```\n(^|/)\\.DS_Store$\n```\nWould that be okay?",
    "created_at": "2012-10-05T19:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65854",
    "user": "https://github.com/jdemeyer"
}
```

`devel/sage/.hgignore` has

```
(^|/)\.DS_Store$
```
Would that be okay?



---

archive/issue_comments_065855.json:
```json
{
    "body": "Replying to [comment:4 ohanar]:\n> Shouldn't we keep the DS_Store line for OSX?\n\nI was thinking that DS_Store files shouldn't end up in the actual shipped spkgs.  But of course, `.hgignore` is also used for end-user installations.  So we should probably keep it indeed.",
    "created_at": "2012-10-05T19:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65855",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:4 ohanar]:
> Shouldn't we keep the DS_Store line for OSX?

I was thinking that DS_Store files shouldn't end up in the actual shipped spkgs.  But of course, `.hgignore` is also used for end-user installations.  So we should probably keep it indeed.



---

archive/issue_comments_065856.json:
```json
{
    "body": "Patch updated, with `.DS_Store` put back in `.hgignore`.",
    "created_at": "2012-10-08T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65856",
    "user": "https://github.com/jdemeyer"
}
```

Patch updated, with `.DS_Store` put back in `.hgignore`.



---

archive/issue_comments_065857.json:
```json
{
    "body": "Apply to EXTCODE",
    "created_at": "2012-10-08T08:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65857",
    "user": "https://github.com/jdemeyer"
}
```

Apply to EXTCODE



---

archive/issue_comments_065858.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-13T16:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65858",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065859.json:
```json
{
    "body": "Attachment [7688_extcode_pyc.patch](tarball://root/attachments/some-uuid/ticket7688/7688_extcode_pyc.patch) by @ohanar created at 2012-10-13 16:45:46\n\nOk, everything looks good to me.",
    "created_at": "2012-10-13T16:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65859",
    "user": "https://github.com/ohanar"
}
```

Attachment [7688_extcode_pyc.patch](tarball://root/attachments/some-uuid/ticket7688/7688_extcode_pyc.patch) by @ohanar created at 2012-10-13 16:45:46

Ok, everything looks good to me.



---

archive/issue_events_018365.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-14T18:55:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7688#event-18365"
}
```



---

archive/issue_comments_065860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-10-14T18:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65860",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
