# Issue 9082: Some unnecessary files being modified

archive/issues_009082.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  dimpase jdemeyer\n\nKeywords: beginner\n\nWhen one build sage, the modification times of the following 3 files are changed. \n\n\n```\n./README.txt\n./COPYING.txt\n./sage-README-osx.txt\n```\n\n\nWhilst not a major problem in itself, it does mean that 'make distclean' does not return the source tree to its original state. \n\nIf one runs\n\n```\n$ 'make distclean'\n$ find . -mtime -2\n```\n\nit will list all files modified in the last two days. Those files should not modified but they are. Some files created in the build process are not being removed, but they should be. That will be the subject of another ticket.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9082\n\n",
    "created_at": "2010-05-29T07:28:36Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Some unnecessary files being modified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9082",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  dimpase jdemeyer

Keywords: beginner

When one build sage, the modification times of the following 3 files are changed. 


```
./README.txt
./COPYING.txt
./sage-README-osx.txt
```


Whilst not a major problem in itself, it does mean that 'make distclean' does not return the source tree to its original state. 

If one runs

```
$ 'make distclean'
$ find . -mtime -2
```

it will list all files modified in the last two days. Those files should not modified but they are. Some files created in the build process are not being removed, but they should be. That will be the subject of another ticket.




Issue created by migration from https://trac.sagemath.org/ticket/9082





---

archive/issue_comments_084309.json:
```json
{
    "body": "The other relevant ticket is #9083. These are two different but related problems, since\n\n* The modification of unnecessary files. \n* Failing to remove files or directories with 'make distclean'\n\nboth result in 'make distclean' not doing what it should do.",
    "created_at": "2010-05-29T07:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84309",
    "user": "drkirkby"
}
```

The other relevant ticket is #9083. These are two different but related problems, since

* The modification of unnecessary files. 
* Failing to remove files or directories with 'make distclean'

both result in 'make distclean' not doing what it should do.



---

archive/issue_comments_084310.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"makefile\".",
    "created_at": "2014-02-11T17:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84310",
    "user": "rws"
}
```

Changing keywords from "beginner" to "makefile".



---

archive/issue_comments_084311.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-10-28T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84311",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084312.json:
```json
{
    "body": "This ticket seems outdated. I propose to close it",
    "created_at": "2016-10-28T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84312",
    "user": "mkoeppe"
}
```

This ticket seems outdated. I propose to close it



---

archive/issue_comments_084313.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-10-28T12:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84313",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084314.json:
```json
{
    "body": "Agreed. This is no longer the case; besides, the 1st file is renamed and became README.md, and the 3rd file is gone.",
    "created_at": "2016-10-28T12:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84314",
    "user": "dimpase"
}
```

Agreed. This is no longer the case; besides, the 1st file is renamed and became README.md, and the 3rd file is gone.



---

archive/issue_comments_084315.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-01-21T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9082#issuecomment-84315",
    "user": "vbraun"
}
```

Resolution: invalid
