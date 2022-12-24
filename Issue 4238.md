# Issue 4238: option to create local .so file for .spyx modules

archive/issues_004238.json:
```json
{
    "body": "Assignee: @williamstein\n\nLoading an .spyx file requires a recompile for each new startup of Sage. There should be a way to save the .so file locally and load it like a module. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4238\n\n",
    "created_at": "2008-10-02T19:33:58Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "option to create local .so file for .spyx modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4238",
    "user": "@robertwb"
}
```
Assignee: @williamstein

Loading an .spyx file requires a recompile for each new startup of Sage. There should be a way to save the .so file locally and load it like a module. 

Issue created by migration from https://trac.sagemath.org/ticket/4238





---

archive/issue_comments_030802.json:
```json
{
    "body": "Original patch from David Fu",
    "created_at": "2008-10-02T19:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30802",
    "user": "@robertwb"
}
```

Original patch from David Fu



---

archive/issue_comments_030803.json:
```json
{
    "body": "Attachment [local_so_doctests.patch](tarball://root/attachments/some-uuid/ticket4238/local_so_doctests.patch) by @robertwb created at 2008-10-02 19:39:38\n\nget doctests passing",
    "created_at": "2008-10-02T19:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30803",
    "user": "@robertwb"
}
```

Attachment [local_so_doctests.patch](tarball://root/attachments/some-uuid/ticket4238/local_so_doctests.patch) by @robertwb created at 2008-10-02 19:39:38

get doctests passing



---

archive/issue_comments_030804.json:
```json
{
    "body": "The one question I have is if we should have a new global function for this behavior, or just provide it as an option to the cython function.",
    "created_at": "2008-10-02T19:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30804",
    "user": "@robertwb"
}
```

The one question I have is if we should have a new global function for this behavior, or just provide it as an option to the cython function.



---

archive/issue_comments_030805.json:
```json
{
    "body": "This is a duplicate of #909, which I am closing.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-03T00:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30805",
    "user": "mabshoff"
}
```

This is a duplicate of #909, which I am closing.

Cheers,

Michael



---

archive/issue_comments_030806.json:
```json
{
    "body": "I searched for a similar ticket, but I guess I didn't throw in the right keywords. Crazy how I think 3-digit trac tickets are \"low\" now...",
    "created_at": "2008-10-03T09:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30806",
    "user": "@robertwb"
}
```

I searched for a similar ticket, but I guess I didn't throw in the right keywords. Crazy how I think 3-digit trac tickets are "low" now...



---

archive/issue_comments_030807.json:
```json
{
    "body": "First and foremost: I do give this patch a positive review, get this code in!\n\nBut the only reason is that it is the first new code in the spyx/load/attach for quite some time. This area is in a sorrow state, several tickets are open addressing different symptoms of the same cause:\nIt's all still nothing but a quick and dirty hack.\n\nWe will have problems with this new patch, consider the following scenario:\nTwo files foo.spyx and bar.sage, where bar.sage imports sth from foo.spyx.\n1. User creates local foo.so\n2. User is happy, until he needs in bar.sage a change in sth\n3. User attaches foo.spyx and develops the needed change\n4. User exits Sage\n5. User reenters Sage\n6. User loads bar.sage and wonders why the hell sth displays the old behaviour ...\n\nOf course \"User\" forgot\" to re-create the local foo.so, so the old one was taken.\nBut it is counter-intuitive that anyone should have to remember to do that manually, since the Sage had all information it needed to update the local foo.so itself!\n\nIn spite of this patch being so error-prone, without doing small steps in at least some patches, it seems that nothing would move here. So again, positive review.\n\nAt last for the question of a \"new global function\":\nWell, the Right Thing (TM) to do here would be to introduce proper dependency handling in the load/attach code, probably best done with the help of a tool like Scons. Then, using attach/load just like one does right now, \"behind the scenes\" there would happen a bit more magic. To the end that whenever the sourcecode of some .spyx and anything else didn't change, a respective .so would already exist and be used (which is quick, as desired); and whenever the sourcecode --- or some other dependency of the .spyx, like e.g. a C library! --- did change, everything needed would happen automatically.\n\nSo, in an ideal world, the question about \"global function or not\" should be utterly superfluous. This problem \"always long starting times due to recompilation done every time\" just wouldn't exist!\nBut we live in a real world, with limited resources ...\nSo let's add just another hack that at least relieves some of the pain for some of us.",
    "created_at": "2008-10-05T19:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30807",
    "user": "GeorgSWeber"
}
```

First and foremost: I do give this patch a positive review, get this code in!

But the only reason is that it is the first new code in the spyx/load/attach for quite some time. This area is in a sorrow state, several tickets are open addressing different symptoms of the same cause:
It's all still nothing but a quick and dirty hack.

We will have problems with this new patch, consider the following scenario:
Two files foo.spyx and bar.sage, where bar.sage imports sth from foo.spyx.
1. User creates local foo.so
2. User is happy, until he needs in bar.sage a change in sth
3. User attaches foo.spyx and develops the needed change
4. User exits Sage
5. User reenters Sage
6. User loads bar.sage and wonders why the hell sth displays the old behaviour ...

Of course "User" forgot" to re-create the local foo.so, so the old one was taken.
But it is counter-intuitive that anyone should have to remember to do that manually, since the Sage had all information it needed to update the local foo.so itself!

In spite of this patch being so error-prone, without doing small steps in at least some patches, it seems that nothing would move here. So again, positive review.

At last for the question of a "new global function":
Well, the Right Thing (TM) to do here would be to introduce proper dependency handling in the load/attach code, probably best done with the help of a tool like Scons. Then, using attach/load just like one does right now, "behind the scenes" there would happen a bit more magic. To the end that whenever the sourcecode of some .spyx and anything else didn't change, a respective .so would already exist and be used (which is quick, as desired); and whenever the sourcecode --- or some other dependency of the .spyx, like e.g. a C library! --- did change, everything needed would happen automatically.

So, in an ideal world, the question about "global function or not" should be utterly superfluous. This problem "always long starting times due to recompilation done every time" just wouldn't exist!
But we live in a real world, with limited resources ...
So let's add just another hack that at least relieves some of the pain for some of us.



---

archive/issue_comments_030808.json:
```json
{
    "body": "local_so_doctests.patch will likely break on Cygwin, but I guess it will be easy enough to fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T22:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30808",
    "user": "mabshoff"
}
```

local_so_doctests.patch will likely break on Cygwin, but I guess it will be easy enough to fix.

Cheers,

Michael



---

archive/issue_comments_030809.json:
```json
{
    "body": "Merged both patches in Sage 3.1.3.alpha3",
    "created_at": "2008-10-07T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30809",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.3.alpha3



---

archive/issue_comments_030810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4238#issuecomment-30810",
    "user": "mabshoff"
}
```

Resolution: fixed
