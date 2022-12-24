# Issue 9614: "-sdist" should complain or fail when run in a "-bdist" copy of Sage

archive/issues_009614.json:
```json
{
    "body": "Assignee: tbd\n\nA \"bdisted\" copy of Sage contains only placeholders for spkg files, and does not include the directory SAGE_ROOT/spkg/base. This means it is impossible for \"sage -sdist\" to work on such a copy of Sage unless the sdist script somehow downloads the necessary files.\n\nThe sdist script should detect this problem and fail in this situation, preferably with instructions to the user for fixing it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9614\n\n",
    "created_at": "2010-07-28T01:29:52Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "\"-sdist\" should complain or fail when run in a \"-bdist\" copy of Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9614",
    "user": "ddrake"
}
```
Assignee: tbd

A "bdisted" copy of Sage contains only placeholders for spkg files, and does not include the directory SAGE_ROOT/spkg/base. This means it is impossible for "sage -sdist" to work on such a copy of Sage unless the sdist script somehow downloads the necessary files.

The sdist script should detect this problem and fail in this situation, preferably with instructions to the user for fixing it.

Issue created by migration from https://trac.sagemath.org/ticket/9614





---

archive/issue_comments_093100.json:
```json
{
    "body": "Attachment [trac_9614.patch](tarball://root/attachments/some-uuid/ticket9614/trac_9614.patch) by ddrake created at 2010-07-28 02:09:51\n\napply to scripts repo",
    "created_at": "2010-07-28T02:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93100",
    "user": "ddrake"
}
```

Attachment [trac_9614.patch](tarball://root/attachments/some-uuid/ticket9614/trac_9614.patch) by ddrake created at 2010-07-28 02:09:51

apply to scripts repo



---

archive/issue_comments_093101.json:
```json
{
    "body": "My proposed changes are attached. I've changed 'sage -bdist' to create an empty file spkg/standard/.from_bdist. \"sage -sdist\" looks for that file, and exits if it finds it. It prints some instructions as it fails; I think the instructions are correct, but please check to make sure.\n\nWe could try to have -sdist download the necessary files and put them in, but that would require always having a downloadable source for many versions of Sage on the web, and wouldn't do any good to someone working without a net connection. Telling the user how to fix the problem seems more effective in this case.",
    "created_at": "2010-07-28T02:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93101",
    "user": "ddrake"
}
```

My proposed changes are attached. I've changed 'sage -bdist' to create an empty file spkg/standard/.from_bdist. "sage -sdist" looks for that file, and exits if it finds it. It prints some instructions as it fails; I think the instructions are correct, but please check to make sure.

We could try to have -sdist download the necessary files and put them in, but that would require always having a downloadable source for many versions of Sage on the web, and wouldn't do any good to someone working without a net connection. Telling the user how to fix the problem seems more effective in this case.



---

archive/issue_comments_093102.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T02:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93102",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093103.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-01T01:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93103",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093104.json:
```json
{
    "body": "I've made that mistake before and I wished that sage-sdist would have complained. This fix looks good to me! Applies fine on Sage-4.6.2.alpha3.",
    "created_at": "2011-02-01T01:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93104",
    "user": "vbraun"
}
```

I've made that mistake before and I wished that sage-sdist would have complained. This fix looks good to me! Applies fine on Sage-4.6.2.alpha3.



---

archive/issue_comments_093105.json:
```json
{
    "body": "Changing component from distribution to scripts.",
    "created_at": "2011-02-01T08:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93105",
    "user": "jdemeyer"
}
```

Changing component from distribution to scripts.



---

archive/issue_comments_093106.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-07T08:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9614#issuecomment-93106",
    "user": "jdemeyer"
}
```

Resolution: fixed
