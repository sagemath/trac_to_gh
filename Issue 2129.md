# Issue 2129: implement "sage -t" for .pyx files

archive/issues_002129.json:
```json
{
    "body": "Assignee: failure\n\n\n```\n'm having some trouble doctesting non sage files. The only things I\ncould find in the Programming Guide were:\n\n 4.3.1 Testing .py, .pyx and .sage Files\n\n    Run sage -t <filename.py> to test that all code examples in\n    filename.py. Similar remarks apply to .sage and\n    .pyx files.\n\nand\n\n 5.3.8 Doctests\n\n    If x.pyx is a Cython file, then you can do\n\n     sage -t x.pyx\n\n    to test all the examples in the documentation strings in x.pyx.\n\nBut this does not seem to be sufficient. One question: what about\n.spyx files? Here is an experiment done on version 2.10.1 that shows\nthat some clarification (if not some coding) is desirable:\n\nCreate a file hello.py with contents:\n\n def hello():\n     \"\"\"\n     Return a friendly string.\n\n     EXAMPLES:\n     sage: hello()\n     Goodbye!\n     \"\"\"\n     return 'Hello!'\n\nMake copies of the file called\n\n hello.sage\n hello.pyx\n hello.spyx\n\nand then run the commands\n\n $ sage -t hello.sage  # reports correctly that 'Hello' is not\n'Goodbye'\n $ sage -t hello.py    # NameError: name 'hello' is not defined\n $ sage -t hello.pyx   # NameError: name 'hello' is not defined\n $ sage -t hello.spyx  # blithely reports incorrectly that all tests\npass\n\nFollowing a hint in the Programming Guide, in the case of hello.py,\nafter changing the EXAMPLES section so it reads\n\n EXAMPLES:\n sage: from hello import *\n sage: hello()\n Goodbye!\n\nthe correct behaviour is recovered. Applying the same change to\nhello.pyx is not the right thing to do, since the import will grab the\nfunction out of the module hello.py. However, after changing the name\nof the file to hello2.pyx and the function to hello2, we encounter\nthe same NameError.\n\n -- Kate Minola\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2129\n\n",
    "created_at": "2008-02-09T19:33:42Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "implement \"sage -t\" for .pyx files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2129",
    "user": "@williamstein"
}
```
Assignee: failure


```
'm having some trouble doctesting non sage files. The only things I
could find in the Programming Guide were:

 4.3.1 Testing .py, .pyx and .sage Files

    Run sage -t <filename.py> to test that all code examples in
    filename.py. Similar remarks apply to .sage and
    .pyx files.

and

 5.3.8 Doctests

    If x.pyx is a Cython file, then you can do

     sage -t x.pyx

    to test all the examples in the documentation strings in x.pyx.

But this does not seem to be sufficient. One question: what about
.spyx files? Here is an experiment done on version 2.10.1 that shows
that some clarification (if not some coding) is desirable:

Create a file hello.py with contents:

 def hello():
     """
     Return a friendly string.

     EXAMPLES:
     sage: hello()
     Goodbye!
     """
     return 'Hello!'

Make copies of the file called

 hello.sage
 hello.pyx
 hello.spyx

and then run the commands

 $ sage -t hello.sage  # reports correctly that 'Hello' is not
'Goodbye'
 $ sage -t hello.py    # NameError: name 'hello' is not defined
 $ sage -t hello.pyx   # NameError: name 'hello' is not defined
 $ sage -t hello.spyx  # blithely reports incorrectly that all tests
pass

Following a hint in the Programming Guide, in the case of hello.py,
after changing the EXAMPLES section so it reads

 EXAMPLES:
 sage: from hello import *
 sage: hello()
 Goodbye!

the correct behaviour is recovered. Applying the same change to
hello.pyx is not the right thing to do, since the import will grab the
function out of the module hello.py. However, after changing the name
of the file to hello2.pyx and the function to hello2, we encounter
the same NameError.

 -- Kate Minola
```


Issue created by migration from https://trac.sagemath.org/ticket/2129





---

archive/issue_comments_013968.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T23:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13968",
    "user": "@malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_013969.json:
```json
{
    "body": "Attachment [trac_2129-scripts.patch](tarball://root/attachments/some-uuid/ticket2129/trac_2129-scripts.patch) by @williamstein created at 2009-01-24 13:57:14",
    "created_at": "2009-01-24T13:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13969",
    "user": "@williamstein"
}
```

Attachment [trac_2129-scripts.patch](tarball://root/attachments/some-uuid/ticket2129/trac_2129-scripts.patch) by @williamstein created at 2009-01-24 13:57:14



---

archive/issue_comments_013970.json:
```json
{
    "body": "Note that one of the originally reported problems is still not solved -- doctesting .pyx files outside the tree.  I'm not sure how to fix this, but it would be nice.\n\nI manually updated the patch for 3.4 and added trac_2129-scripts-v3_4.patch, but I need someone to check that I did it correctly.  Specifically, I am not sure the patch applies cleanly.  With these changes, I am able to doctest .spyx files outside the Sage tree, a valuable tool for me right now.",
    "created_at": "2009-03-12T00:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13970",
    "user": "@rhinton"
}
```

Note that one of the originally reported problems is still not solved -- doctesting .pyx files outside the tree.  I'm not sure how to fix this, but it would be nice.

I manually updated the patch for 3.4 and added trac_2129-scripts-v3_4.patch, but I need someone to check that I did it correctly.  Specifically, I am not sure the patch applies cleanly.  With these changes, I am able to doctest .spyx files outside the Sage tree, a valuable tool for me right now.



---

archive/issue_comments_013971.json:
```json
{
    "body": "Attachment [trac_2129-scripts-v3_4.patch](tarball://root/attachments/some-uuid/ticket2129/trac_2129-scripts-v3_4.patch) by @rhinton created at 2009-03-12 00:34:53",
    "created_at": "2009-03-12T00:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13971",
    "user": "@rhinton"
}
```

Attachment [trac_2129-scripts-v3_4.patch](tarball://root/attachments/some-uuid/ticket2129/trac_2129-scripts-v3_4.patch) by @rhinton created at 2009-03-12 00:34:53



---

archive/issue_comments_013972.json:
```json
{
    "body": "Attachment [trac_2129.spyx](tarball://root/attachments/some-uuid/ticket2129/trac_2129.spyx) by @rhinton created at 2009-03-13 15:47:29\n\n.spyx file with a doctest that fails (since previous doctesting blithely reported all tests pass)",
    "created_at": "2009-03-13T15:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13972",
    "user": "@rhinton"
}
```

Attachment [trac_2129.spyx](tarball://root/attachments/some-uuid/ticket2129/trac_2129.spyx) by @rhinton created at 2009-03-13 15:47:29

.spyx file with a doctest that fails (since previous doctesting blithely reported all tests pass)



---

archive/issue_comments_013973.json:
```json
{
    "body": "This applies cleanly to my sage-3.4 build, so positive review on the rebase.\n\nI also tested it with the spyx file rhinton uploaded, and everything seems to work correctly.",
    "created_at": "2009-03-13T15:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13973",
    "user": "@jasongrout"
}
```

This applies cleanly to my sage-3.4 build, so positive review on the rebase.

I also tested it with the spyx file rhinton uploaded, and everything seems to work correctly.



---

archive/issue_comments_013974.json:
```json
{
    "body": "Merged trac_2129-scripts-v3_4.patch in Sage 3.4.1.alpha0. \n\nRyan: You posted only a diff, I committed the patch in your name. \n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13974",
    "user": "mabshoff"
}
```

Merged trac_2129-scripts-v3_4.patch in Sage 3.4.1.alpha0. 

Ryan: You posted only a diff, I committed the patch in your name. 

Cheers,

Michael



---

archive/issue_comments_013975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T08:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2129#issuecomment-13975",
    "user": "mabshoff"
}
```

Resolution: fixed
