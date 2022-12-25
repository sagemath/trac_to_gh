# Issue 5994: singular.version() yields an error when first called, has no doctest, and has a strange output imo

archive/issues_005994.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kedlaya\n\nKeywords: singular version\n\nFirst of all, `singular.version()` does not work. When one starts sage and calls it, there is an error:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: singular.version()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (795, 0))\n| Sage Version 3.4.1, Release Date: 2009-04-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/SimonKing/.sage/temp/sage.math.washington.edu/10897/_home_SimonKing__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in version(self)\n   1012         EXAMPLES:\n   1013         \"\"\"\n-> 1014         return singular_version()\n   1015\n   1016     def _function_class(self):\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in singular_version()\n   1807     EXAMPLES:\n   1808     \"\"\"\n-> 1809     return singular.eval('system(\"--version\");')\n   1810\n   1811\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)\n    541\n    542         if s.find(\"error\") != -1 or s.find(\"Segment fault\") != -1:\n--> 543             raise RuntimeError, 'Singular error:\\n%s'%s\n    544\n    545         if get_verbose() > 0:\n\nRuntimeError: Singular error:\n   ? cannot open `help.cnf`\nSingular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08\nwith\n        factory(@(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),\n        GMP(4.2),NTL(5.4.2),static readline,Plural,DBM,\n        namespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325\n        CC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,\n        CXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))\nargv[0]   :     Singular-3-0-4\nSearchPath:     /usr/local/sage/local/LIB\nSingular  :     /usr/local/sage/local/bin/Singular-3-0-4\nBinDir    :     /usr/local/sage/local/bin\nRootDir   :     /usr/local/sage/local\nDefaultDir:     /usr/local/sage/local\nInfoFile  :\nIdxFile   :\nHtmlDir   :\nManualUrl :     http://www.singular.uni-kl.de/Manual/3-0-4\nExDir     :\nPath      :     /usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games\nEmacsDir  :\nAvailable HelpBrowsers: dummy, emacs,\nCurrent HelpBrowser: dummy\n   ? error occurred in STDIN line 3: `system(\"--version\");`\n```\n\n\nSecondly, neither `singular.version` nor `singular_version` have doc tests.\n\nThirdly, if it is called again, it kind of works:\n\n```\nsage: singular.version()\n'Singular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08\\nwith\\n\\tfactory(@(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),\\n\\tGMP(4.2),NTL(5.4.2),static readline,Plural,DBM,\\n\\tnamespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325\\n\\tCC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,\\n\\tCXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))\\nargv[0]   :\\tSingular-3-0-4\\nSearchPath:\\t/usr/local/sage/local/LIB\\nSingular  :\\t/usr/local/sage/local/bin/Singular-3-0-4\\nBinDir    :\\t/usr/local/sage/local/bin\\nRootDir   :\\t/usr/local/sage/local\\nDefaultDir:\\t/usr/local/sage/local\\nInfoFile  :\\t\\nIdxFile   :\\t\\nHtmlDir   :\\t\\nManualUrl :\\thttp://www.singular.uni-kl.de/Manual/3-0-4\\nExDir     :\\t\\nPath      :\\t/usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games\\nEmacsDir  :\\t\\nAvailable HelpBrowsers: dummy, emacs, \\nCurrent HelpBrowser: dummy '\n```\n\n\nFinally, I believe that the output of `singular.version` is nasty. If I ask for the version of Singular, I expect to get, say, a tuple of integers, for example:\n\n```\nsage: def my_singular_version():\n....:     return tuple([Integer(x) for x in singular.eval('system(\"version\")')])\n....:\nsage: my_singular_version()\n(3, 0, 4, 4)\n```\n\n\nI suggest to remake `singular.version` so that it returns a tuple of integers, rather than a cryptic string.\n\nProblem though: Would this break code?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5994\n\n",
    "created_at": "2009-05-06T09:46:52Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.5",
    "title": "singular.version() yields an error when first called, has no doctest, and has a strange output imo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5994",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @williamstein

CC:  @kedlaya

Keywords: singular version

First of all, `singular.version()` does not work. When one starts sage and calls it, there is an error:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.version()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (795, 0))
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/10897/_home_SimonKing__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in version(self)
   1012         EXAMPLES:
   1013         """
-> 1014         return singular_version()
   1015
   1016     def _function_class(self):

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in singular_version()
   1807     EXAMPLES:
   1808     """
-> 1809     return singular.eval('system("--version");')
   1810
   1811

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)
    541
    542         if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 543             raise RuntimeError, 'Singular error:\n%s'%s
    544
    545         if get_verbose() > 0:

RuntimeError: Singular error:
   ? cannot open `help.cnf`
Singular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08
with
        factory(@(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),
        GMP(4.2),NTL(5.4.2),static readline,Plural,DBM,
        namespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325
        CC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,
        CXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))
argv[0]   :     Singular-3-0-4
SearchPath:     /usr/local/sage/local/LIB
Singular  :     /usr/local/sage/local/bin/Singular-3-0-4
BinDir    :     /usr/local/sage/local/bin
RootDir   :     /usr/local/sage/local
DefaultDir:     /usr/local/sage/local
InfoFile  :
IdxFile   :
HtmlDir   :
ManualUrl :     http://www.singular.uni-kl.de/Manual/3-0-4
ExDir     :
Path      :     /usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
EmacsDir  :
Available HelpBrowsers: dummy, emacs,
Current HelpBrowser: dummy
   ? error occurred in STDIN line 3: `system("--version");`
```


Secondly, neither `singular.version` nor `singular_version` have doc tests.

Thirdly, if it is called again, it kind of works:

```
sage: singular.version()
'Singular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08\nwith\n\tfactory(@(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),\n\tGMP(4.2),NTL(5.4.2),static readline,Plural,DBM,\n\tnamespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325\n\tCC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,\n\tCXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))\nargv[0]   :\tSingular-3-0-4\nSearchPath:\t/usr/local/sage/local/LIB\nSingular  :\t/usr/local/sage/local/bin/Singular-3-0-4\nBinDir    :\t/usr/local/sage/local/bin\nRootDir   :\t/usr/local/sage/local\nDefaultDir:\t/usr/local/sage/local\nInfoFile  :\t\nIdxFile   :\t\nHtmlDir   :\t\nManualUrl :\thttp://www.singular.uni-kl.de/Manual/3-0-4\nExDir     :\t\nPath      :\t/usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games\nEmacsDir  :\t\nAvailable HelpBrowsers: dummy, emacs, \nCurrent HelpBrowser: dummy '
```


Finally, I believe that the output of `singular.version` is nasty. If I ask for the version of Singular, I expect to get, say, a tuple of integers, for example:

```
sage: def my_singular_version():
....:     return tuple([Integer(x) for x in singular.eval('system("version")')])
....:
sage: my_singular_version()
(3, 0, 4, 4)
```


I suggest to remake `singular.version` so that it returns a tuple of integers, rather than a cryptic string.

Problem though: Would this break code?

Issue created by migration from https://trac.sagemath.org/ticket/5994





---

archive/issue_comments_047541.json:
```json
{
    "body": "Remark:\n\nApparently the problem is on the side of Singular.\n\nIn Singular, freshly started, when you do\n\n```\n> system(\"--version\");\n```\n\nthere is the error (it says \"? cannot open `help.cnf`\"). \nIf you repeat, no error.\n\nIf people think that my suggestion would break code, I suggest to have a new method `singular.version_number()`.",
    "created_at": "2009-05-06T09:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47541",
    "user": "https://github.com/simon-king-jena"
}
```

Remark:

Apparently the problem is on the side of Singular.

In Singular, freshly started, when you do

```
> system("--version");
```

there is the error (it says "? cannot open `help.cnf`"). 
If you repeat, no error.

If people think that my suggestion would break code, I suggest to have a new method `singular.version_number()`.



---

archive/issue_comments_047542.json:
```json
{
    "body": "Replying to [comment:1 SimonKing]:\n> Apparently the problem is on the side of Singular.\n\nAnd meanwhile it is reported upstream. \n\nI do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).",
    "created_at": "2009-05-06T12:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47542",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:1 SimonKing]:
> Apparently the problem is on the side of Singular.

And meanwhile it is reported upstream. 

I do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).



---

archive/issue_comments_047543.json:
```json
{
    "body": "Replying to [comment:2 SimonKing]:\n> Replying to [comment:1 SimonKing]:\n> And meanwhile it is reported upstream. \n> \n> I do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).\n\n\"Upstream\" answered, and it seems that the problem is fixed in the official release. \n\nI could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?\n\nBut there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.",
    "created_at": "2009-05-06T12:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47543",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 SimonKing]:
> Replying to [comment:1 SimonKing]:
> And meanwhile it is reported upstream. 
> 
> I do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).

"Upstream" answered, and it seems that the problem is fixed in the official release. 

I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.



---

archive/issue_comments_047544.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> \n> \"Upstream\" answered, and it seems that the problem is fixed in the official release. \n> \n> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?\n\nWe can probably wait until after Sage Days 15 for this?\n \n> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.\n\nMy personal preference would be for it to return a tuple of integers, but we could give it an optional argument `with_build_info=True` (or `verbatim=True` or something similar) to make it return the lengthy string.",
    "created_at": "2009-05-06T12:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47544",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:3 SimonKing]:
> 
> "Upstream" answered, and it seems that the problem is fixed in the official release. 
> 
> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

We can probably wait until after Sage Days 15 for this?
 
> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.

My personal preference would be for it to return a tuple of integers, but we could give it an optional argument `with_build_info=True` (or `verbatim=True` or something similar) to make it return the lengthy string.



---

archive/issue_comments_047545.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?\n\nThe \"Opinions?\" bit should be two lines lower. Sorry.\n\nIt turned out that the error occurs in *any* ***Sage-built*** Singular version that I know: Singular 3-0-4 on sage.math, on two of my computers, in Oberwolfach, and Singular 3-1-0-Beta on sage.math and on one of my computers. \n\nIf Singular is not built by Sage, then the error apparently does not occur: With Singular 3-0-3 (very old) on one of my machines, Singular-3-1-0-Beta on my machine (same sources, modulo the usual patches, as the sage-built version!), and Singular-3-1-0 official release in Oberwolfach.\n\nSo, after all, it seems to me that it is all Sage's fault.\n\n\n> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.\n\nHere is where I want to know some \"Opinions\"...",
    "created_at": "2009-05-06T13:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47545",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it *does* occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

The "Opinions?" bit should be two lines lower. Sorry.

It turned out that the error occurs in *any* ***Sage-built*** Singular version that I know: Singular 3-0-4 on sage.math, on two of my computers, in Oberwolfach, and Singular 3-1-0-Beta on sage.math and on one of my computers. 

If Singular is not built by Sage, then the error apparently does not occur: With Singular 3-0-3 (very old) on one of my machines, Singular-3-1-0-Beta on my machine (same sources, modulo the usual patches, as the sage-built version!), and Singular-3-1-0 official release in Oberwolfach.

So, after all, it seems to me that it is all Sage's fault.


> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.

Here is where I want to know some "Opinions"...



---

archive/issue_comments_047546.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T13:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47546",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047547.json:
```json
{
    "body": "The attached patch fixes the output format for version to be more consistent with the other interfaces, e.g., `gp.version()`.  It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.",
    "created_at": "2010-01-18T13:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47547",
    "user": "https://github.com/williamstein"
}
```

The attached patch fixes the output format for version to be more consistent with the other interfaces, e.g., `gp.version()`.  It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.



---

archive/issue_comments_047548.json:
```json
{
    "body": "Attachment [trac_5994.patch](tarball://root/attachments/some-uuid/ticket5994/trac_5994.patch) by @simon-king-jena created at 2010-01-18 13:15:46\n\nReplying to [comment:6 was]:\n> It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.  \n\nNote that I originally thought that the issue with help files is a problem of Singular, and clearly a bug: I mean, you ask for the version number and get an error; you ask again, and it works! It had reported it upstream.\n\nBut then the impression came across (see my last post) that it only occurs in Singular if it is built by Sage. In this case, it could be a problem with the patched version in Sage, which might be worth another ticket.\n\nCheers,\nSimon",
    "created_at": "2010-01-18T13:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47548",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_5994.patch](tarball://root/attachments/some-uuid/ticket5994/trac_5994.patch) by @simon-king-jena created at 2010-01-18 13:15:46

Replying to [comment:6 was]:
> It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.  

Note that I originally thought that the issue with help files is a problem of Singular, and clearly a bug: I mean, you ask for the version number and get an error; you ask again, and it works! It had reported it upstream.

But then the impression came across (see my last post) that it only occurs in Singular if it is built by Sage. In this case, it could be a problem with the patched version in Sage, which might be worth another ticket.

Cheers,
Simon



---

archive/issue_comments_047549.json:
```json
{
    "body": "I think the first time you ask for the version, singular fires up its help system, and reports a bug about it not being properly configured by *us* for such use.  Then it doesn't report that again, since it already did.  I think it is very sensible behavior by Singular.\n\nSo can you review this?",
    "created_at": "2010-01-18T22:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47549",
    "user": "https://github.com/williamstein"
}
```

I think the first time you ask for the version, singular fires up its help system, and reports a bug about it not being properly configured by *us* for such use.  Then it doesn't report that again, since it already did.  I think it is very sensible behavior by Singular.

So can you review this?



---

archive/issue_comments_047550.json:
```json
{
    "body": "For the record, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error. There is actually a `help.cnf` file in the singular sources (, but it doesn't seem to get installed. Its contents don't look to be particularly relevant for sage at first glance, though.",
    "created_at": "2010-01-19T04:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47550",
    "user": "https://github.com/wjp"
}
```

For the record, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error. There is actually a `help.cnf` file in the singular sources (, but it doesn't seem to get installed. Its contents don't look to be particularly relevant for sage at first glance, though.



---

archive/issue_comments_047551.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> So can you review this?\n\nI'd like to, but the sage-4.3.1.alpha1 that I had built on sage-math seems broken. It used to work, but when I did `./sage -br main`, it failed with \n\n```\nImportError: /usr/lib/libstdc++.so.6: version `GLIBCXX_3.4.11' not found (required by /home/SimonKing/SAGE/sage-4.3.1.alpha1/local/lib/libgmpxx.so.3)\n```\n\n\nMight `./sage -ba` work?\n\nAnyway, I'd like to see one more doc test, that checks consistency with another way of getting the version number -- just for consistency:\n\n```\nsage: tuple([Integer(c) for c in singular.eval('system(\"version\")')][:3] == singular.version()[0]\nTrue\n```\n",
    "created_at": "2010-01-19T09:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47551",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:8 was]:
> So can you review this?

I'd like to, but the sage-4.3.1.alpha1 that I had built on sage-math seems broken. It used to work, but when I did `./sage -br main`, it failed with 

```
ImportError: /usr/lib/libstdc++.so.6: version `GLIBCXX_3.4.11' not found (required by /home/SimonKing/SAGE/sage-4.3.1.alpha1/local/lib/libgmpxx.so.3)
```


Might `./sage -ba` work?

Anyway, I'd like to see one more doc test, that checks consistency with another way of getting the version number -- just for consistency:

```
sage: tuple([Integer(c) for c in singular.eval('system("version")')][:3] == singular.version()[0]
True
```




---

archive/issue_comments_047552.json:
```json
{
    "body": "Replying to [comment:10 SimonKing]:\n> ...\n> {{{\n> sage: tuple([Integer(c) for c in singular.eval('system(\"version\")')][:3] == singular.version()[0]\n> True\n> }}}\n\nOops, apparently I forgot a closing bracket on the left hand side. Anyway, you know what this prospective doc-test is supposed to do...",
    "created_at": "2010-01-19T09:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47552",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:10 SimonKing]:
> ...
> {{{
> sage: tuple([Integer(c) for c in singular.eval('system("version")')][:3] == singular.version()[0]
> True
> }}}

Oops, apparently I forgot a closing bracket on the left hand side. Anyway, you know what this prospective doc-test is supposed to do...



---

archive/issue_comments_047553.json:
```json
{
    "body": "Replying to [comment:10 SimonKing]:\n> \n> Might `./sage -ba` work?\n> \n\nIt did not work. I fear that I have to start from scratch, so that it will take some hours before I will be able to review the patch.",
    "created_at": "2010-01-19T10:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47553",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:10 SimonKing]:
> 
> Might `./sage -ba` work?
> 

It did not work. I fear that I have to start from scratch, so that it will take some hours before I will be able to review the patch.



---

archive/issue_comments_047554.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-19T15:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47554",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_047555.json:
```json
{
    "body": "OK, meanwhile I built sage-4.3.1.rc1\n\nThe patch applies cleanly.\n\nHowever, I don't like the doc tests, and I think the return value is wrong.\n\nThe tests check that the first version number is 3. OK, it will eventually change, but not in the near future. \n\nThen they test that the version number is of length 3. Can we rely on it? There used to be two-digit versions. \n\nIn fact, the \"official\" version number seems to be four digits, not three:\n\n```\nsage: singular.eval('system(\"version\")')\n'3104'\n```\n\n\nHence, the first return value of singular.version() should be (3,1,0,4) not (3,1,0). \nNote that according to the Singular homepage there is a version 3-1-0-6 available, so, the last digit does play a role.\n\nSo, my questions are:\n\n* How important is it to have doc tests that remain valid if the Singular version changes?\n* Do we take the patch level version number of Singular serious?",
    "created_at": "2010-01-19T15:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47555",
    "user": "https://github.com/simon-king-jena"
}
```

OK, meanwhile I built sage-4.3.1.rc1

The patch applies cleanly.

However, I don't like the doc tests, and I think the return value is wrong.

The tests check that the first version number is 3. OK, it will eventually change, but not in the near future. 

Then they test that the version number is of length 3. Can we rely on it? There used to be two-digit versions. 

In fact, the "official" version number seems to be four digits, not three:

```
sage: singular.eval('system("version")')
'3104'
```


Hence, the first return value of singular.version() should be (3,1,0,4) not (3,1,0). 
Note that according to the Singular homepage there is a version 3-1-0-6 available, so, the last digit does play a role.

So, my questions are:

* How important is it to have doc tests that remain valid if the Singular version changes?
* Do we take the patch level version number of Singular serious?



---

archive/issue_comments_047556.json:
```json
{
    "body": "Replying to [comment:13 SimonKing]:\n> > So, my questions are:\n> \n>  * How important is it to have doc tests that remain valid if the Singular version changes?\n>  * Do we take the patch level version number of Singular serious?\n\nIs there an answer, yet?",
    "created_at": "2010-07-05T12:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47556",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:13 SimonKing]:
> > So, my questions are:
> 
>  * How important is it to have doc tests that remain valid if the Singular version changes?
>  * Do we take the patch level version number of Singular serious?

Is there an answer, yet?



---

archive/issue_comments_047557.json:
```json
{
    "body": "-- bump --\n\nFirst question: Do we want that `singular.version()` works? Currently, it fails when first called.\n\nSecond question: Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?",
    "created_at": "2011-05-28T09:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47557",
    "user": "https://github.com/simon-king-jena"
}
```

-- bump --

First question: Do we want that `singular.version()` works? Currently, it fails when first called.

Second question: Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?



---

archive/issue_comments_047558.json:
```json
{
    "body": "It shouldn't hurt to install the `help.cnf` file though, in which case we wouldn't need (and *should* remove) the `try ... except RuntimeError ...` and a second try.",
    "created_at": "2011-08-07T20:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47558",
    "user": "https://github.com/nexttime"
}
```

It shouldn't hurt to install the `help.cnf` file though, in which case we wouldn't need (and *should* remove) the `try ... except RuntimeError ...` and a second try.



---

archive/issue_comments_047559.json:
```json
{
    "body": "Changing keywords from \"singular version\" to \"singular version help.cnf\".",
    "created_at": "2011-08-07T20:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47559",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "singular version" to "singular version help.cnf".



---

archive/issue_comments_047560.json:
```json
{
    "body": "Since he reported this again on a duplicate, #11519.",
    "created_at": "2011-08-07T20:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47560",
    "user": "https://github.com/nexttime"
}
```

Since he reported this again on a duplicate, #11519.



---

archive/issue_comments_047561.json:
```json
{
    "body": "Replying to [comment:15 SimonKing]:\n \n> Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?\n\nAs a default I would suggest output similar to `pari.version()`. But for now at least `kash_version()` and `r_version()` gives slightly different output...\n\nMaybe right way could be to remove them, and have something like `version('kash')` for one package and `version()` for all packages?",
    "created_at": "2015-07-17T06:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47561",
    "user": "https://github.com/jm58660"
}
```

Replying to [comment:15 SimonKing]:
 
> Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?

As a default I would suggest output similar to `pari.version()`. But for now at least `kash_version()` and `r_version()` gives slightly different output...

Maybe right way could be to remove them, and have something like `version('kash')` for one package and `version()` for all packages?



---

archive/issue_comments_047562.json:
```json
{
    "body": "Gosh, is that still not fixed? Sorry that I spoiled it by asking questions in comment:13 that nobody bothers to answer...",
    "created_at": "2015-09-06T14:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47562",
    "user": "https://github.com/simon-king-jena"
}
```

Gosh, is that still not fixed? Sorry that I spoiled it by asking questions in comment:13 that nobody bothers to answer...



---

archive/issue_comments_047563.json:
```json
{
    "body": "To repeat my questions:\n\n- How important is it to have doc tests that remain valid if the Singular version changes?\n\nMy answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.\n\n- Do we take the patch level version number of Singular serious? Respectively do we really want the current behaviour (singular.version() returns a lengthy string), or would we prefer to have it return a tuple of integers?\n\nMy answer: We have\n\n```\nsage: pari.version()\n[2, 8, 0]\nsage: r.version()\n((3, 2, 1), 'R version 3.2.1 (2015-06-18)')\nsage: gap.version()\n'4.7.8'\nsage: sage0.version()\n'SageMath Version 6.9.beta3, Release Date: 2015-08-21'\n```\n\nHence, the different interfaces have all kind of different output. Thus, the current behaviour should be fine, but the following output\n\n```\nsage: singular.eval('system(\"version\")')\n'3170'\n```\n\nwould be equally fine.\n\nMy suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional \"verbose=False\" argument, that allows to obtain the lengthy version string. And of course fix the error.",
    "created_at": "2015-09-06T15:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47563",
    "user": "https://github.com/simon-king-jena"
}
```

To repeat my questions:

- How important is it to have doc tests that remain valid if the Singular version changes?

My answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.

- Do we take the patch level version number of Singular serious? Respectively do we really want the current behaviour (singular.version() returns a lengthy string), or would we prefer to have it return a tuple of integers?

My answer: We have

```
sage: pari.version()
[2, 8, 0]
sage: r.version()
((3, 2, 1), 'R version 3.2.1 (2015-06-18)')
sage: gap.version()
'4.7.8'
sage: sage0.version()
'SageMath Version 6.9.beta3, Release Date: 2015-08-21'
```

Hence, the different interfaces have all kind of different output. Thus, the current behaviour should be fine, but the following output

```
sage: singular.eval('system("version")')
'3170'
```

would be equally fine.

My suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional "verbose=False" argument, that allows to obtain the lengthy version string. And of course fix the error.



---

archive/issue_comments_047564.json:
```json
{
    "body": "Replying to [comment:24 SimonKing]:\n> To repeat my questions:\n> \n> - How important is it to have doc tests that remain valid if the Singular version changes?\n> \n> My answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.\n\n+1\n\n> My suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional \"verbose=False\" argument, that allows to obtain the lengthy version string. And of course fix the error.\n\nSounds good. Somehow the output of `pari.version()` seems best for me. Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?",
    "created_at": "2015-09-06T15:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47564",
    "user": "https://github.com/jm58660"
}
```

Replying to [comment:24 SimonKing]:
> To repeat my questions:
> 
> - How important is it to have doc tests that remain valid if the Singular version changes?
> 
> My answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.

+1

> My suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional "verbose=False" argument, that allows to obtain the lengthy version string. And of course fix the error.

Sounds good. Somehow the output of `pari.version()` seems best for me. Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?



---

archive/issue_comments_047565.json:
```json
{
    "body": "Replying to [comment:25 jmantysalo]:\n> Sounds good. Somehow the output of `pari.version()` seems best for me.\n\nSlight problem: The patching level usually is not indicated by a number but by \"p\" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.\n\nFrom that perspective, the r-output is better.\n\n> Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?\n\nI didn't know about the existence of a `package_version.txt`. I wonder if we could access these data---after all, the package version of singular is \"3.1.7p1.p0\", but the version shown by `singular.eval('system(\"version\")')` is \"3170\". Similarly for r, it should be `3.2.1.p0`, not `(3,2,1)`.\n\nI guess it is time to do a bit bike shedding at sage-devel.",
    "created_at": "2015-09-06T17:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47565",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:25 jmantysalo]:
> Sounds good. Somehow the output of `pari.version()` seems best for me.

Slight problem: The patching level usually is not indicated by a number but by "p" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.

From that perspective, the r-output is better.

> Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?

I didn't know about the existence of a `package_version.txt`. I wonder if we could access these data---after all, the package version of singular is "3.1.7p1.p0", but the version shown by `singular.eval('system("version")')` is "3170". Similarly for r, it should be `3.2.1.p0`, not `(3,2,1)`.

I guess it is time to do a bit bike shedding at sage-devel.



---

archive/issue_comments_047566.json:
```json
{
    "body": "Replying to [comment:26 SimonKing]:\n \n> Slight problem: The patching level usually is not indicated by a number but by \"p\" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.\n> \n> From that perspective, the r-output is better.\n\nTrue.\n\nAs a system admin I should be able to answer fast to questions \"What is the version of ... in our server ...?\". For that it is not so important what is the format. But it gives a little unprofessional feeling if I get `(1,2,3)` from `foo.version()` and `[1,2,3]` from `bar.version()`.",
    "created_at": "2015-09-07T06:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47566",
    "user": "https://github.com/jm58660"
}
```

Replying to [comment:26 SimonKing]:
 
> Slight problem: The patching level usually is not indicated by a number but by "p" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.
> 
> From that perspective, the r-output is better.

True.

As a system admin I should be able to answer fast to questions "What is the version of ... in our server ...?". For that it is not so important what is the format. But it gives a little unprofessional feeling if I get `(1,2,3)` from `foo.version()` and `[1,2,3]` from `bar.version()`.



---

archive/issue_comments_047567.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-09-10T09:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47567",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_047568.json:
```json
{
    "body": "I work around the bug that results in the error, and I think it is best to return both a version tuple on the one hand (so that one can easily test if the version is enough recent) and the complete version information as provided by Singular as a string.\n\nHopefully the reviewers agree...",
    "created_at": "2015-09-10T09:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47568",
    "user": "https://github.com/simon-king-jena"
}
```

I work around the bug that results in the error, and I think it is best to return both a version tuple on the one hand (so that one can easily test if the version is enough recent) and the complete version information as provided by Singular as a string.

Hopefully the reviewers agree...



---

archive/issue_comments_047569.json:
```json
{
    "body": "Why is it not possible to click on the attached branch an see the changes?",
    "created_at": "2015-09-10T09:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47569",
    "user": "https://github.com/simon-king-jena"
}
```

Why is it not possible to click on the attached branch an see the changes?



---

archive/issue_comments_047570.json:
```json
{
    "body": "Arrgh. I forgot to commit before pushing :-/",
    "created_at": "2015-09-10T09:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47570",
    "user": "https://github.com/simon-king-jena"
}
```

Arrgh. I forgot to commit before pushing :-/



---

archive/issue_comments_047571.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-10T09:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47571",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047572.json:
```json
{
    "body": "The error should be reported upstream and the comment in the code should link to this ticket and the upstream report.",
    "created_at": "2015-09-10T10:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47572",
    "user": "https://github.com/jdemeyer"
}
```

The error should be reported upstream and the comment in the code should link to this ticket and the upstream report.



---

archive/issue_comments_047573.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-09-10T10:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47573",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_047574.json:
```json
{
    "body": "I am not so sure if it requires an uptream report. The error is about a missing file, and according to comment:9, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.",
    "created_at": "2015-09-10T10:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47574",
    "user": "https://github.com/simon-king-jena"
}
```

I am not so sure if it requires an uptream report. The error is about a missing file, and according to comment:9, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.



---

archive/issue_comments_047575.json:
```json
{
    "body": "Replying to [comment:34 SimonKing]:\n> adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.\n\nThen that should be done instead of wrapping the call in a `try`/`except` block (which is a really ugly \"solution\")",
    "created_at": "2015-09-10T11:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47575",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:34 SimonKing]:
> adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.

Then that should be done instead of wrapping the call in a `try`/`except` block (which is a really ugly "solution")



---

archive/issue_comments_047576.json:
```json
{
    "body": "There is actually a `help.cnf` installed in\n\n```\n$SAGE_LOCAL/share/singular/LIB/help.cnf\n```\n\nso I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.\n\nIn any case, copying that file to `$SAGE_LOCAL/share/singular/help.cnf` would be a good solution for this ticket.",
    "created_at": "2015-09-10T11:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47576",
    "user": "https://github.com/jdemeyer"
}
```

There is actually a `help.cnf` installed in

```
$SAGE_LOCAL/share/singular/LIB/help.cnf
```

so I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.

In any case, copying that file to `$SAGE_LOCAL/share/singular/help.cnf` would be a good solution for this ticket.



---

archive/issue_comments_047577.json:
```json
{
    "body": "Replying to [comment:36 jdemeyer]:\n> There is actually a `help.cnf` installed in\n> {{{\n> $SAGE_LOCAL/share/singular/LIB/help.cnf\n> }}}\n> so I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.\n\nFrom reading [this change log](http://www.singular.uni-kl.de:8002/trac/changeset/46e5030de2b6094068cceec4cd764bad1a65a02c/git), I believe that .../share singular/LIB/ is the correct place.\n\nI'll file a ticket in the singular trac server. But for now, we need a work-around in Sage.",
    "created_at": "2015-09-10T12:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47577",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:36 jdemeyer]:
> There is actually a `help.cnf` installed in
> {{{
> $SAGE_LOCAL/share/singular/LIB/help.cnf
> }}}
> so I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.

From reading [this change log](http://www.singular.uni-kl.de:8002/trac/changeset/46e5030de2b6094068cceec4cd764bad1a65a02c/git), I believe that .../share singular/LIB/ is the correct place.

I'll file a ticket in the singular trac server. But for now, we need a work-around in Sage.



---

archive/issue_comments_047578.json:
```json
{
    "body": "I reported it [upstream](http://www.singular.uni-kl.de:8002/trac/ticket/740).",
    "created_at": "2015-09-10T12:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47578",
    "user": "https://github.com/simon-king-jena"
}
```

I reported it [upstream](http://www.singular.uni-kl.de:8002/trac/ticket/740).



---

archive/issue_comments_047579.json:
```json
{
    "body": "I stand corrected! There used to be `$SAGE_LOCAL/share/singular/help.cnf`, but it is gone. The only help.cnf found under $SAGE_ROOT is upstream/src/latest/Singular/LIB/help.cnf.\n\nSo, apparently we don't install it at all!",
    "created_at": "2015-09-10T12:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47579",
    "user": "https://github.com/simon-king-jena"
}
```

I stand corrected! There used to be `$SAGE_LOCAL/share/singular/help.cnf`, but it is gone. The only help.cnf found under $SAGE_ROOT is upstream/src/latest/Singular/LIB/help.cnf.

So, apparently we don't install it at all!



---

archive/issue_comments_047580.json:
```json
{
    "body": "Replying to [comment:39 SimonKing]:\n> So, apparently we don't install it at all!\nYou're right, this must have come from some earlier Singular version (note the date):\n\n```\n$ ls -l local/share/singular/LIB/help.cnf\n-rw-r--r-- 1 jdemeyer jdemeyer 3054 Oct 29  2014 local/share/singular/LIB/help.cnf\n```\n",
    "created_at": "2015-09-10T12:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47580",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:39 SimonKing]:
> So, apparently we don't install it at all!
You're right, this must have come from some earlier Singular version (note the date):

```
$ ls -l local/share/singular/LIB/help.cnf
-rw-r--r-- 1 jdemeyer jdemeyer 3054 Oct 29  2014 local/share/singular/LIB/help.cnf
```




---

archive/issue_comments_047581.json:
```json
{
    "body": "Replying to [comment:37 SimonKing]:\n> But for now, we need a work-around in Sage.\nI suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`",
    "created_at": "2015-09-10T12:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47581",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:37 SimonKing]:
> But for now, we need a work-around in Sage.
I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`



---

archive/issue_comments_047582.json:
```json
{
    "body": "Replying to [comment:41 jdemeyer]:\n> Replying to [comment:37 SimonKing]:\n> > But for now, we need a work-around in Sage.\n> I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`\n\nWhy not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?\n\nAlso, I'd like to know why Singular's Makefile does not install help.cnf. After all, if I understand correctly, it DOES install all the library files of Singular (which are in the same folder as help.cnf).\n\nHang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ? Do we need a new Singular package?",
    "created_at": "2015-09-10T12:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47582",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:41 jdemeyer]:
> Replying to [comment:37 SimonKing]:
> > But for now, we need a work-around in Sage.
> I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`

Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?

Also, I'd like to know why Singular's Makefile does not install help.cnf. After all, if I understand correctly, it DOES install all the library files of Singular (which are in the same folder as help.cnf).

Hang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ? Do we need a new Singular package?



---

archive/issue_comments_047583.json:
```json
{
    "body": "Upstream says that help.cnf should indeed be put into the same folder as all the other library files, i.e., local/share/singular/.",
    "created_at": "2015-09-10T12:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47583",
    "user": "https://github.com/simon-king-jena"
}
```

Upstream says that help.cnf should indeed be put into the same folder as all the other library files, i.e., local/share/singular/.



---

archive/issue_comments_047584.json:
```json
{
    "body": "Replying to [comment:42 SimonKing]:\n> Replying to [comment:41 jdemeyer]:\n> > Replying to [comment:37 SimonKing]:\n> > > But for now, we need a work-around in Sage.\n> > I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`\n> \n> Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?\nI don't really care much.\n\n> Hang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ?\nProbably you once extracted the tarball in `upstream`? It's not the package which does that...",
    "created_at": "2015-09-10T12:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47584",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:42 SimonKing]:
> Replying to [comment:41 jdemeyer]:
> > Replying to [comment:37 SimonKing]:
> > > But for now, we need a work-around in Sage.
> > I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`
> 
> Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?
I don't really care much.

> Hang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ?
Probably you once extracted the tarball in `upstream`? It's not the package which does that...



---

archive/issue_comments_047585.json:
```json
{
    "body": "Replying to [comment:44 jdemeyer]:\n> > Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?\n> I don't really care much.\n\nThen I guess we should do it in spkg-install.\n \n> Probably you once extracted the tarball in `upstream`? It's not the package which does that...\n\nCould be. I just deleted it and did \"sage -f singular\".",
    "created_at": "2015-09-10T13:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47585",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:44 jdemeyer]:
> > Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?
> I don't really care much.

Then I guess we should do it in spkg-install.
 
> Probably you once extracted the tarball in `upstream`? It's not the package which does that...

Could be. I just deleted it and did "sage -f singular".



---

archive/issue_comments_047586.json:
```json
{
    "body": "There's also `#sagemath` on freenode.  Just saying...",
    "created_at": "2015-09-10T13:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47586",
    "user": "https://github.com/nexttime"
}
```

There's also `#sagemath` on freenode.  Just saying...



---

archive/issue_comments_047587.json:
```json
{
    "body": "Replying to [comment:46 leif]:\n> There's also `#sagemath` on freenode.  Just saying...\n\nMeaning what?",
    "created_at": "2015-09-10T15:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47587",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:46 leif]:
> There's also `#sagemath` on freenode.  Just saying...

Meaning what?



---

archive/issue_comments_047588.json:
```json
{
    "body": "Replying to [comment:47 SimonKing]:\n> Replying to [comment:46 leif]:\n> > There's also `#sagemath` on freenode.  Just saying...\n> \n> Meaning what?\n\nOverfull inbox, TeX would have said. ;-)",
    "created_at": "2015-09-10T19:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47588",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:47 SimonKing]:
> Replying to [comment:46 leif]:
> > There's also `#sagemath` on freenode.  Just saying...
> 
> Meaning what?

Overfull inbox, TeX would have said. ;-)



---

archive/issue_comments_047589.json:
```json
{
    "body": "It seems the current agreement seems to be to modify spkg-install, so that it copies help.cnf from the singular sources to `$SAGE_SHARE/singular/`. What is the path to the singular sources while spkg-install is executed?",
    "created_at": "2015-09-11T09:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47589",
    "user": "https://github.com/simon-king-jena"
}
```

It seems the current agreement seems to be to modify spkg-install, so that it copies help.cnf from the singular sources to `$SAGE_SHARE/singular/`. What is the path to the singular sources while spkg-install is executed?



---

archive/issue_comments_047590.json:
```json
{
    "body": "Replying to [comment:49 SimonKing]:\n> What is the path to the singular sources while spkg-install is executed?\nIt's the current working directory.",
    "created_at": "2015-09-11T09:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47590",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:49 SimonKing]:
> What is the path to the singular sources while spkg-install is executed?
It's the current working directory.



---

archive/issue_comments_047591.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2016-10-24T09:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47591",
    "user": "https://github.com/jm58660"
}
```

Changing priority from major to minor.



---

archive/issue_comments_047592.json:
```json
{
    "body": "Error has gone away with Singular 4.\n\nI added doctest.\n\nWhat goes to output format, I think this should be changed in all `*_version()` commands at once. (Assuming somebody would care, which is propably not true.)\n----\nNew commits:",
    "created_at": "2016-10-24T09:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47592",
    "user": "https://github.com/jm58660"
}
```

Error has gone away with Singular 4.

I added doctest.

What goes to output format, I think this should be changed in all `*_version()` commands at once. (Assuming somebody would care, which is propably not true.)
----
New commits:



---

archive/issue_comments_047593.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-10-24T09:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47593",
    "user": "https://github.com/jm58660"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047594.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-10-26T17:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47594",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006248.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-11-02T19:20:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5994#event-6248"
}
```



---

archive/issue_comments_047595.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-02T19:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5994#issuecomment-47595",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
