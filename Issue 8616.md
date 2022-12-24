# Issue 8616: Symbolic type checking and expression parcing module

archive/issues_008616.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robert.marik novoselt\n\nKeywords: symbolic, type, subexpression\n\nProvides unified interface for standard python types and sage specific types.\nTreats everything as symbolic expression which allows to check its type, take\noperator and operands and extract subexpressions by given types.\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/f2ba2198dc5b79ed\n\nIssue created by migration from https://trac.sagemath.org/ticket/8616\n\n",
    "created_at": "2010-03-27T20:26:08Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "Symbolic type checking and expression parcing module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8616",
    "user": "yuri.k"
}
```
Assignee: burcin

CC:  robert.marik novoselt

Keywords: symbolic, type, subexpression

Provides unified interface for standard python types and sage specific types.
Treats everything as symbolic expression which allows to check its type, take
operator and operands and extract subexpressions by given types.

http://groups.google.com/group/sage-devel/browse_thread/thread/f2ba2198dc5b79ed

Issue created by migration from https://trac.sagemath.org/ticket/8616





---

archive/issue_comments_078075.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-27T20:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78075",
    "user": "yuri.k"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078076.json:
```json
{
    "body": "Attachment [trac_8616_symbolic_sage.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage.patch) by yuri.k created at 2010-03-27 20:34:00\n\nsymbolic sage module",
    "created_at": "2010-03-27T20:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78076",
    "user": "yuri.k"
}
```

Attachment [trac_8616_symbolic_sage.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage.patch) by yuri.k created at 2010-03-27 20:34:00

symbolic sage module



---

archive/issue_comments_078077.json:
```json
{
    "body": "Attachment [trac_8616_symbolic_sage.2.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage.2.patch) by yuri.k created at 2010-03-27 20:34:04\n\nsymbolic sage module",
    "created_at": "2010-03-27T20:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78077",
    "user": "yuri.k"
}
```

Attachment [trac_8616_symbolic_sage.2.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage.2.patch) by yuri.k created at 2010-03-27 20:34:04

symbolic sage module



---

archive/issue_comments_078078.json:
```json
{
    "body": "Hm I have the following error after installing the patch\n\n```\nImportError: No module named mtype\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nAnd there is no mtype.* file in sage/symmbolic in my Sage 4.3.4",
    "created_at": "2010-03-28T13:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78078",
    "user": "robert.marik"
}
```

Hm I have the following error after installing the patch

```
ImportError: No module named mtype
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

And there is no mtype.* file in sage/symmbolic in my Sage 4.3.4



---

archive/issue_comments_078079.json:
```json
{
    "body": "Attachment [trac_8616_symbolic_sage_correct.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage_correct.patch) by yuri.k created at 2010-03-28 17:50:14",
    "created_at": "2010-03-28T17:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78079",
    "user": "yuri.k"
}
```

Attachment [trac_8616_symbolic_sage_correct.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage_correct.patch) by yuri.k created at 2010-03-28 17:50:14



---

archive/issue_comments_078080.json:
```json
{
    "body": "Attachment [trac_8616_symbolic_sage_correct2.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage_correct2.patch) by yuri.k created at 2010-03-29 09:50:08\n\nmore precise autodetect of independent variable",
    "created_at": "2010-03-29T09:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78080",
    "user": "yuri.k"
}
```

Attachment [trac_8616_symbolic_sage_correct2.patch](tarball://root/attachments/some-uuid/ticket8616/trac_8616_symbolic_sage_correct2.patch) by yuri.k created at 2010-03-29 09:50:08

more precise autodetect of independent variable



---

archive/issue_comments_078081.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-10T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78081",
    "user": "robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078082.json:
```json
{
    "body": "Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does \"mtype\" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps \"*.integer\" would be better. \n\nIn any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.",
    "created_at": "2010-04-10T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78082",
    "user": "robertwb"
}
```

Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does "mtype" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps "*.integer" would be better. 

In any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.



---

archive/issue_comments_078083.json:
```json
{
    "body": "Replying to [comment:10 robertwb]:\n> Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does \"mtype\" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps \"*.integer\" would be better. \n>\n\n_ wildcard is used in scala. * is used for multiply operator. desolve module is really bad it is beter to completly rewrite it, but sage doesn't have enough functions to start doing it. mtype is the firs step. It helps to deal with symbolical expression.\n\n> In any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.\n\nI absolutely agree with you. It is much better to have class hierarchy or at least some common interface which can help to define type. And wraps or mixins should be used for Python types. But I did mtype class to concentrate attention on existing problem - sage is almost useless for complex symbolical computations (it is my opinion as well as  opinion of my colleagues) It is hard for people who are new to python. You shouldn't use mtype, but it is good to do smth about this problem in sage.\n\nI made sketch to solve some simple de problems I write some common functions in mtype, which can be easily rewritten to extract only diff operators. So just use it if you want to.\n\nI finished with sage for this year, now I need to do smth real. I'm sorry I can't afford to spend some more time to finish this improvements.",
    "created_at": "2010-04-10T21:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78083",
    "user": "yuri.k"
}
```

Replying to [comment:10 robertwb]:
> Thank you for working on desolve, that module is in need of a lot of help. I'm really not seeing what mtype has to do with it though (and what does "mtype" mean? wtype, stype, ... are equally obscure). Also _ for a wildcard is very non-standard notation, perhaps "*.integer" would be better. 
>

_ wildcard is used in scala. * is used for multiply operator. desolve module is really bad it is beter to completly rewrite it, but sage doesn't have enough functions to start doing it. mtype is the firs step. It helps to deal with symbolical expression.

> In any case, my main issue with this patch is that a huge list of isinstance statements is not the way to implement this--it's brittle and requires the module to know about everything in Sage. If we need an mtype (operator, ...), it should be done OO style, with tests just for a few of the builtin types (and even then it could be cleaner, using their names.

I absolutely agree with you. It is much better to have class hierarchy or at least some common interface which can help to define type. And wraps or mixins should be used for Python types. But I did mtype class to concentrate attention on existing problem - sage is almost useless for complex symbolical computations (it is my opinion as well as  opinion of my colleagues) It is hard for people who are new to python. You shouldn't use mtype, but it is good to do smth about this problem in sage.

I made sketch to solve some simple de problems I write some common functions in mtype, which can be easily rewritten to extract only diff operators. So just use it if you want to.

I finished with sage for this year, now I need to do smth real. I'm sorry I can't afford to spend some more time to finish this improvements.



---

archive/issue_comments_078084.json:
```json
{
    "body": "Changing title to more accurately reflect what it's about.",
    "created_at": "2011-06-14T17:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8616#issuecomment-78084",
    "user": "kcrisman"
}
```

Changing title to more accurately reflect what it's about.
