# Issue 3482: create a pickle jar

archive/issues_003482.json:
```json
{
    "body": "Assignee: robertwb\n\nThis is easy to use -- so the docstrings at the bottom of sage/structure/sage_object.pyx.\n\n```\nsage.structure.sage_object.picklejar?\n```\n\nand \n\n```\nsage.structure.sage_object.unpickle_all?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3482\n\n",
    "created_at": "2008-06-20T06:17:40Z",
    "labels": [
        "coercion",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "create a pickle jar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3482",
    "user": "was"
}
```
Assignee: robertwb

This is easy to use -- so the docstrings at the bottom of sage/structure/sage_object.pyx.

```
sage.structure.sage_object.picklejar?
```

and 

```
sage.structure.sage_object.unpickle_all?
```


Issue created by migration from https://trac.sagemath.org/ticket/3482





---

archive/issue_comments_024533.json:
```json
{
    "body": "Attachment [sage-3482.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482.patch) by was created at 2008-06-20 06:27:41",
    "created_at": "2008-06-20T06:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24533",
    "user": "was"
}
```

Attachment [sage-3482.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482.patch) by was created at 2008-06-20 06:27:41



---

archive/issue_comments_024534.json:
```json
{
    "body": ":-)\n\nHi, it turns out that *all* 465 pickles in sage-3.0.3 made on opteron 64-bit linux unpickle fine on 32-bit osx intel.",
    "created_at": "2008-06-20T17:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24534",
    "user": "was"
}
```

:-)

Hi, it turns out that *all* 465 pickles in sage-3.0.3 made on opteron 64-bit linux unpickle fine on 32-bit osx intel.



---

archive/issue_comments_024535.json:
```json
{
    "body": "Please change the environment variable to start with SAGE; these should all be consistent.  Also, why is it not SAGE_PICKLE_JAR_ROOT in keeping with the convention?\n\nThe doctests do not show what filename a particular object is given, nor does it demonstrate a failing load.  If the idea is figure out what class cannot be reconstituted, that's not enough.  Also, it would be nice to test unpickling a class that no longer exists in the library.\n\nIn addition, the code doesn't return the unpickled objects -- say a dict or similar.  Why not?\n\nI say this is not done yet.",
    "created_at": "2008-06-20T21:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24535",
    "user": "ncalexan"
}
```

Please change the environment variable to start with SAGE; these should all be consistent.  Also, why is it not SAGE_PICKLE_JAR_ROOT in keeping with the convention?

The doctests do not show what filename a particular object is given, nor does it demonstrate a failing load.  If the idea is figure out what class cannot be reconstituted, that's not enough.  Also, it would be nice to test unpickling a class that no longer exists in the library.

In addition, the code doesn't return the unpickled objects -- say a dict or similar.  Why not?

I say this is not done yet.



---

archive/issue_comments_024536.json:
```json
{
    "body": "> Please change the environment variable to start with SAGE; \n> these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT \n> in keeping with the convention?\n\nHow about SAGE_PICKLE_JAR?  That's simple and easy to remember. \n\n> The doctests do not show what filename a particular object is given, nor \n> does it demonstrate a failing load. If the idea is figure out what class \n> cannot be reconstituted, that's not enough. \n\nThe idea is that one would unpickle the object in the current released\nversion of sage, which would allow one to find out anything you want\nabout it.   I could change the filename to be some nice-ified version of\ntype(obj), with a number appended in case of duplicates.  Would you prefer that?\n\n> Also, it would be nice to \n> test unpickling a class that no longer exists in the library.\n\nHow?  \n\n> In addition, the code doesn't return the unpickled objects -- say a \n> dict or similar. Why not?\n\nSimplicity.   What would be the point of returning the unpickled objects?\nWhich code are you talking about?     The point\nis to get a list of the objects that don't unpickle, so one can investigate\nfurther and see what major/minor change to the library caused the objects\nto no longer unpickle.",
    "created_at": "2008-06-22T00:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24536",
    "user": "was"
}
```

> Please change the environment variable to start with SAGE; 
> these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT 
> in keeping with the convention?

How about SAGE_PICKLE_JAR?  That's simple and easy to remember. 

> The doctests do not show what filename a particular object is given, nor 
> does it demonstrate a failing load. If the idea is figure out what class 
> cannot be reconstituted, that's not enough. 

The idea is that one would unpickle the object in the current released
version of sage, which would allow one to find out anything you want
about it.   I could change the filename to be some nice-ified version of
type(obj), with a number appended in case of duplicates.  Would you prefer that?

> Also, it would be nice to 
> test unpickling a class that no longer exists in the library.

How?  

> In addition, the code doesn't return the unpickled objects -- say a 
> dict or similar. Why not?

Simplicity.   What would be the point of returning the unpickled objects?
Which code are you talking about?     The point
is to get a list of the objects that don't unpickle, so one can investigate
further and see what major/minor change to the library caused the objects
to no longer unpickle.



---

archive/issue_comments_024537.json:
```json
{
    "body": "A suggestion: maybe the file should actually store a triple, `(dumps(x), repr(x), repr(parent(x)))` (maybe also repr(type(x)) and repr(type(parent(x)))).  The repr's would serve two purposes: in case a pickle fails to unpickle in a new version, this is useful for figuring out where to look; and repr(x) and repr(parent(x)) can be recomputed in the new version of Sage and compared to the pickled version, as a minimal check that unpickling actually gave the correct object.\n\nThe downside is that changing the printing of an object would start to make the pickle jar tests fail; there would have to be a way of updating the printing in previous-version pickle jars (without changing the previous dumps(x)).",
    "created_at": "2008-06-22T20:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24537",
    "user": "cwitty"
}
```

A suggestion: maybe the file should actually store a triple, `(dumps(x), repr(x), repr(parent(x)))` (maybe also repr(type(x)) and repr(type(parent(x)))).  The repr's would serve two purposes: in case a pickle fails to unpickle in a new version, this is useful for figuring out where to look; and repr(x) and repr(parent(x)) can be recomputed in the new version of Sage and compared to the pickled version, as a minimal check that unpickling actually gave the correct object.

The downside is that changing the printing of an object would start to make the pickle jar tests fail; there would have to be a way of updating the printing in previous-version pickle jars (without changing the previous dumps(x)).



---

archive/issue_comments_024538.json:
```json
{
    "body": "> A suggestion: maybe the file should actually store a triple, \n> (dumps(x), repr(x), repr(parent(x))) (maybe also repr(type(x))\n> and repr(type(parent(x)))). The repr's would serve two purposes: \n>in case a pickle fails to unpickle in a new version, this is useful \n> for figuring out where to look; and repr(x) and repr(parent(x)) \n> can be recomputed in the new version of Sage and compared to the \n> pickled version, as a minimal check that unpickling actually gave the correct object.\n\n> The downside is that changing the printing of an object would \n> start to make the pickle jar tests fail; there would have to \n> be a way of updating the printing in previous-version pickle jars \n> (without changing the previous dumps(x)).\n\n\nI think it would be better would be to have two files:\n\n```\n   a.sobj  -- pickled version of x\n   a.txt  -- a line with type(x); rest of file has repr(x)\n```\n\nMany objects don't have parents, and the above addresses the\n\"updating the pickle jar\" problem you cite above.  Also,\none can always get at a.txt without having to deal with\npickle at all.",
    "created_at": "2008-06-23T13:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24538",
    "user": "was"
}
```

> A suggestion: maybe the file should actually store a triple, 
> (dumps(x), repr(x), repr(parent(x))) (maybe also repr(type(x))
> and repr(type(parent(x)))). The repr's would serve two purposes: 
>in case a pickle fails to unpickle in a new version, this is useful 
> for figuring out where to look; and repr(x) and repr(parent(x)) 
> can be recomputed in the new version of Sage and compared to the 
> pickled version, as a minimal check that unpickling actually gave the correct object.

> The downside is that changing the printing of an object would 
> start to make the pickle jar tests fail; there would have to 
> be a way of updating the printing in previous-version pickle jars 
> (without changing the previous dumps(x)).


I think it would be better would be to have two files:

```
   a.sobj  -- pickled version of x
   a.txt  -- a line with type(x); rest of file has repr(x)
```

Many objects don't have parents, and the above addresses the
"updating the pickle jar" problem you cite above.  Also,
one can always get at a.txt without having to deal with
pickle at all.



---

archive/issue_comments_024539.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> > Please change the environment variable to start with SAGE; \n> > these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT \n> > in keeping with the convention?\n> \n> How about SAGE_PICKLE_JAR?  That's simple and easy to remember.\n\nI agree, sounds good.\n\n > > The doctests do not show what filename a particular object is given, nor \n> > does it demonstrate a failing load. If the idea is figure out what class \n> > cannot be reconstituted, that's not enough. \n> \n> The idea is that one would unpickle the object in the current released\n> version of sage, which would allow one to find out anything you want\n> about it.   I could change the filename to be some nice-ified version of\n> type(obj), with a number appended in case of duplicates.  Would you prefer that?\n\nMaybe?  I don't understand how this is supposed to work.  This dumps a directory of random looking pickles.  (I can't see how to identify any of the outputs.)  I update sage.  Some things don't load -- but I don't have any way to identify what they were supposed to be!  How on earth could you debug it?\n\n> > Also, it would be nice to \n> > test unpickling a class that no longer exists in the library.\n> \n> How?\n\nCreate a class A, pickle it, then del A.  Something like:\n\n\n```\nsage: class TestClass: pass\n....: \nsage: test = TestClass()\nsage: loads(dumps(test))\n<__main__.TestClass instance at 0xca06940>\nsage: s = dumps(test)\nsage: del test\nsage: del TestClass\nsage: loads(s)\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n/Users/ncalexan/sage_object.pyx in sage.structure.sage_object.loads (sage/structure/sage_object.c:5491)()\n\n<type 'exceptions.RuntimeError'>: FakeModule object has no attribute 'TestClass'\ninvalid data stream\ninvalid load key, 'x'.\nUnable to load pickled data.\n```\n\n\n> \n> > In addition, the code doesn't return the unpickled objects -- say a \n> > dict or similar. Why not?\n> \n> Simplicity.   What would be the point of returning the unpickled objects?\n> Which code are you talking about?     The point\n> is to get a list of the objects that don't unpickle, so one can investigate\n> further and see what major/minor change to the library caused the objects\n> to no longer unpickle.\n\nHow does one get that list?  No matter what else happens, the doctests don't show what happens on failure and how one uses this to debug.  That's what they are there for.\n\nNick",
    "created_at": "2008-06-24T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24539",
    "user": "ncalexan"
}
```

Replying to [comment:5 was]:
> > Please change the environment variable to start with SAGE; 
> > these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT 
> > in keeping with the convention?
> 
> How about SAGE_PICKLE_JAR?  That's simple and easy to remember.

I agree, sounds good.

 > > The doctests do not show what filename a particular object is given, nor 
> > does it demonstrate a failing load. If the idea is figure out what class 
> > cannot be reconstituted, that's not enough. 
> 
> The idea is that one would unpickle the object in the current released
> version of sage, which would allow one to find out anything you want
> about it.   I could change the filename to be some nice-ified version of
> type(obj), with a number appended in case of duplicates.  Would you prefer that?

Maybe?  I don't understand how this is supposed to work.  This dumps a directory of random looking pickles.  (I can't see how to identify any of the outputs.)  I update sage.  Some things don't load -- but I don't have any way to identify what they were supposed to be!  How on earth could you debug it?

> > Also, it would be nice to 
> > test unpickling a class that no longer exists in the library.
> 
> How?

Create a class A, pickle it, then del A.  Something like:


```
sage: class TestClass: pass
....: 
sage: test = TestClass()
sage: loads(dumps(test))
<__main__.TestClass instance at 0xca06940>
sage: s = dumps(test)
sage: del test
sage: del TestClass
sage: loads(s)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/sage_object.pyx in sage.structure.sage_object.loads (sage/structure/sage_object.c:5491)()

<type 'exceptions.RuntimeError'>: FakeModule object has no attribute 'TestClass'
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```


> 
> > In addition, the code doesn't return the unpickled objects -- say a 
> > dict or similar. Why not?
> 
> Simplicity.   What would be the point of returning the unpickled objects?
> Which code are you talking about?     The point
> is to get a list of the objects that don't unpickle, so one can investigate
> further and see what major/minor change to the library caused the objects
> to no longer unpickle.

How does one get that list?  No matter what else happens, the doctests don't show what happens on failure and how one uses this to debug.  That's what they are there for.

Nick



---

archive/issue_comments_024540.json:
```json
{
    "body": "Attachment [sage-3482-part2.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482-part2.patch) by was created at 2008-07-06 17:57:10\n\nthis addresses the referee's remarks.",
    "created_at": "2008-07-06T17:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24540",
    "user": "was"
}
```

Attachment [sage-3482-part2.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482-part2.patch) by was created at 2008-07-06 17:57:10

this addresses the referee's remarks.



---

archive/issue_comments_024541.json:
```json
{
    "body": "Attachment [pickle_jar-3.0.3.tar.bz2](tarball://root/attachments/some-uuid/ticket3482/pickle_jar-3.0.3.tar.bz2) by was created at 2008-07-06 19:16:44\n\nan official pickle jar from sage-3.0.3 made on ubuntu 64-bit (sagemath.org)",
    "created_at": "2008-07-06T19:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24541",
    "user": "was"
}
```

Attachment [pickle_jar-3.0.3.tar.bz2](tarball://root/attachments/some-uuid/ticket3482/pickle_jar-3.0.3.tar.bz2) by was created at 2008-07-06 19:16:44

an official pickle jar from sage-3.0.3 made on ubuntu 64-bit (sagemath.org)



---

archive/issue_comments_024542.json:
```json
{
    "body": "Attachment [sage-3482-part3.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482-part3.patch) by was created at 2008-07-06 19:37:28",
    "created_at": "2008-07-06T19:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24542",
    "user": "was"
}
```

Attachment [sage-3482-part3.patch](tarball://root/attachments/some-uuid/ticket3482/sage-3482-part3.patch) by was created at 2008-07-06 19:37:28



---

archive/issue_comments_024543.json:
```json
{
    "body": "I still want to see doctests that show a failing unpickle, but this is still good and should be applied.  Positive review from me.",
    "created_at": "2008-07-06T20:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24543",
    "user": "ncalexan"
}
```

I still want to see doctests that show a failing unpickle, but this is still good and should be applied.  Positive review from me.



---

archive/issue_comments_024544.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T03:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24544",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024545.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T03:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24545",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024546.json:
```json
{
    "body": "Attachment [pickle_jar-3.0.5.tar.bz2](tarball://root/attachments/some-uuid/ticket3482/pickle_jar-3.0.5.tar.bz2) by was created at 2008-07-29 15:21:22",
    "created_at": "2008-07-29T15:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3482#issuecomment-24546",
    "user": "was"
}
```

Attachment [pickle_jar-3.0.5.tar.bz2](tarball://root/attachments/some-uuid/ticket3482/pickle_jar-3.0.5.tar.bz2) by was created at 2008-07-29 15:21:22
