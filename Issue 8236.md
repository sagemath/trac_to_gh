# Issue 8236: installing spkg from remote location must leave a spkg (placeholder) in spkg/

archive/issues_008236.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nKeywords: spkg, installation\n\nWhen one does sage -f (or -i) from a remote location, the\nspkg file is not stored locally in the appropriate place,\neven if an upgrade of a standard spkg has taken place.\nAs a result, the script spkg/standard/newest_version may fail\nto detect that the upgrade has taken place.\n\nAs a solution, one can either store the full downloaded spkg, or\njust a placeholder with (almost) the same name as the spkg file.\n\nOr, perhaps, sage -i (-f) can call spkg/standard/newest_version to see if an upgrade is happening, and act accordingly.\n\nThis bug has cost me and wdj hours of wasted time, see #8229.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8236\n\n",
    "created_at": "2010-02-11T05:41:08Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "installing spkg from remote location must leave a spkg (placeholder) in spkg/",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8236",
    "user": "https://github.com/dimpase"
}
```
Assignee: GeorgSWeber

Keywords: spkg, installation

When one does sage -f (or -i) from a remote location, the
spkg file is not stored locally in the appropriate place,
even if an upgrade of a standard spkg has taken place.
As a result, the script spkg/standard/newest_version may fail
to detect that the upgrade has taken place.

As a solution, one can either store the full downloaded spkg, or
just a placeholder with (almost) the same name as the spkg file.

Or, perhaps, sage -i (-f) can call spkg/standard/newest_version to see if an upgrade is happening, and act accordingly.

This bug has cost me and wdj hours of wasted time, see #8229.

Issue created by migration from https://trac.sagemath.org/ticket/8236





---

archive/issue_comments_072630.json:
```json
{
    "body": "This issue was discussed here:\n[http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77](http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77)\n\nin a nutshell, newest_version should not be used for these tasks, \nand a new script has to be written.",
    "created_at": "2010-03-29T10:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72630",
    "user": "https://github.com/dimpase"
}
```

This issue was discussed here:
[http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77](http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77)

in a nutshell, newest_version should not be used for these tasks, 
and a new script has to be written.



---

archive/issue_comments_072631.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-03-29T10:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72631",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_072632.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-12-29T23:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72632",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072633.json:
```json
{
    "body": "It's not exactly clear what this bug is about, but given the many changes to `sage-spkg`, it's a good bet to assume that it's fixed.",
    "created_at": "2013-12-29T23:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72633",
    "user": "https://github.com/jdemeyer"
}
```

It's not exactly clear what this bug is about, but given the many changes to `sage-spkg`, it's a good bet to assume that it's fixed.



---

archive/issue_comments_072634.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-29T23:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72634",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072635.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-01-04T02:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8236#issuecomment-72635",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
