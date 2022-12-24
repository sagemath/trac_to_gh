# Issue 6652: should not have algebra structure on streams

archive/issues_006652.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\ncombinat/species/stream.py has its origin in\n\n```\nsvn cat svn://svn.risc.uni-linz.ac.at/hemmecke/combinat/trunk/combinat/src/stream.as.nw\n```\n\nI designed the original Aldor domain `DataStream` as a container being an equivalent of an infinite array. Since the Stream can contain any objects, it makes no sense for the stream to provide a `__mul__` and `__add__` method. Any algebraic operations should be defined in a derived class.\n\nSuggestion: Remove `__add__`, `__mul__`, `_times_naive`, `stretch` and `_stretch_gen` from stream.py and put them into a more appropriate place in the class hierarchy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6652\n\n",
    "created_at": "2009-07-28T22:35:30Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "should not have algebra structure on streams",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6652",
    "user": "hemmecke"
}
```
Assignee: mhansen

CC:  sage-combinat

combinat/species/stream.py has its origin in

```
svn cat svn://svn.risc.uni-linz.ac.at/hemmecke/combinat/trunk/combinat/src/stream.as.nw
```

I designed the original Aldor domain `DataStream` as a container being an equivalent of an infinite array. Since the Stream can contain any objects, it makes no sense for the stream to provide a `__mul__` and `__add__` method. Any algebraic operations should be defined in a derived class.

Suggestion: Remove `__add__`, `__mul__`, `_times_naive`, `stretch` and `_stretch_gen` from stream.py and put them into a more appropriate place in the class hierarchy.

Issue created by migration from https://trac.sagemath.org/ticket/6652





---

archive/issue_comments_054602.json:
```json
{
    "body": "Changing assignee from mhansen to hemmecke.",
    "created_at": "2009-07-29T11:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54602",
    "user": "hemmecke"
}
```

Changing assignee from mhansen to hemmecke.



---

archive/issue_comments_054603.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-29T11:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54603",
    "user": "hemmecke"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054604.json:
```json
{
    "body": "Attachment [trac_6652_stream_without_algebra_knowledge_rhx.patch](tarball://root/attachments/some-uuid/ticket6652/trac_6652_stream_without_algebra_knowledge_rhx.patch) by hemmecke created at 2009-07-29 11:59:12",
    "created_at": "2009-07-29T11:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54604",
    "user": "hemmecke"
}
```

Attachment [trac_6652_stream_without_algebra_knowledge_rhx.patch](tarball://root/attachments/some-uuid/ticket6652/trac_6652_stream_without_algebra_knowledge_rhx.patch) by hemmecke created at 2009-07-29 11:59:12



---

archive/issue_comments_054605.json:
```json
{
    "body": "Changing keywords from \"\" to \"stream\".",
    "created_at": "2009-07-29T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54605",
    "user": "hivert"
}
```

Changing keywords from "" to "stream".



---

archive/issue_comments_054606.json:
```json
{
    "body": "The deleted code is completely redundant with some code in `generating_series.py`. \nIt is never used, and the design says that it must go in generating series. Therefore, \nI agree with Ralf that it should be deleted !\n\nPositive review. \n\nFlorent",
    "created_at": "2009-09-11T15:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54606",
    "user": "hivert"
}
```

The deleted code is completely redundant with some code in `generating_series.py`. 
It is never used, and the design says that it must go in generating series. Therefore, 
I agree with Ralf that it should be deleted !

Positive review. 

Florent



---

archive/issue_comments_054607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-11T16:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6652#issuecomment-54607",
    "user": "mvngu"
}
```

Resolution: fixed
