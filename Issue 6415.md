# Issue 6415: "sage -t foo.pyx" should not by default dynamically build foo.so

archive/issues_006415.json:
```json
{
    "body": "Assignee: tbd\n\nRecently (during Sage Days 12 ?!) the doctesting code was changed so that \"sage -t\" on a certain class of *.pyx files now is broken.\nEspecially, they now get not only copied to some temp directory, but it is attempted to build dynamically the *.so extension out of them, as if they were all files to be loaded/attached.\nThis almost certainly must fail, if e.g. you have installed a package under $SAGE_ROOT/local/lib/python/site-packages/, with Cython extensions, building which needs certain libraries, additional C sources, special compiler flags, and so on.\n(And where one \"imports\" the functionality, not loads/attaches it.)\n\nPreviously, doctesting was very well suited to this situation, but is no more.\n\nSo the current (Sage 4.0.2) doctesting code should be enhanced in e.g. one of the following ways:\n\n1) If \"dynamically building\" of an extension fails, just \"try\" to import the functionality as a fallback (in other words: use a prebuilt *.so if one exists, and you can't build a fresh one)\n\n2) Change to the old behaviour, and additionally try build dynamically an extension only if it is missing and/or seems to be outdated compared to the *.pyx file\n\n3) Use the old/new behaviour depending on whether \".../site-packages/...\" is in the path of the *.pyx-file, or not.\n\nAt the core of these problems of course is the fact that there is no standard way to store the build information (not to talk of the \"full\" dependency information) for a Cython source file.\nThe Sage project e.g. invented its own custom-made monolithic \"module_list.py\" on the one hand, its custom-made #clib, #cinclude, ... pragmas on the other hand, but all this does not at all work smoothly together.\nLet alone being usable in Sage-related Cython projects which address a broader audience, and are thus placed under .../site-packages/.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6415\n\n",
    "created_at": "2009-06-25T21:28:29Z",
    "labels": [
        "component: doctest",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -t foo.pyx\" should not by default dynamically build foo.so",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6415",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: tbd

Recently (during Sage Days 12 ?!) the doctesting code was changed so that "sage -t" on a certain class of *.pyx files now is broken.
Especially, they now get not only copied to some temp directory, but it is attempted to build dynamically the *.so extension out of them, as if they were all files to be loaded/attached.
This almost certainly must fail, if e.g. you have installed a package under $SAGE_ROOT/local/lib/python/site-packages/, with Cython extensions, building which needs certain libraries, additional C sources, special compiler flags, and so on.
(And where one "imports" the functionality, not loads/attaches it.)

Previously, doctesting was very well suited to this situation, but is no more.

So the current (Sage 4.0.2) doctesting code should be enhanced in e.g. one of the following ways:

1) If "dynamically building" of an extension fails, just "try" to import the functionality as a fallback (in other words: use a prebuilt *.so if one exists, and you can't build a fresh one)

2) Change to the old behaviour, and additionally try build dynamically an extension only if it is missing and/or seems to be outdated compared to the *.pyx file

3) Use the old/new behaviour depending on whether ".../site-packages/..." is in the path of the *.pyx-file, or not.

At the core of these problems of course is the fact that there is no standard way to store the build information (not to talk of the "full" dependency information) for a Cython source file.
The Sage project e.g. invented its own custom-made monolithic "module_list.py" on the one hand, its custom-made #clib, #cinclude, ... pragmas on the other hand, but all this does not at all work smoothly together.
Let alone being usable in Sage-related Cython projects which address a broader audience, and are thus placed under .../site-packages/.

Issue created by migration from https://trac.sagemath.org/ticket/6415





---

archive/issue_comments_051414.json:
```json
{
    "body": "I ran into this today, but it seems that the -force_lib option solves the issue (it did for me, at least). Am I right?",
    "created_at": "2011-05-24T09:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51414",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

I ran into this today, but it seems that the -force_lib option solves the issue (it did for me, at least). Am I right?



---

archive/issue_comments_051415.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2011-05-25T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51415",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_051416.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-05-25T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51416",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing priority from major to minor.



---

archive/issue_comments_051417.json:
```json
{
    "body": "Hi Stefan,\ngood catch! Yes, I do think the issue of this ticket currently is solvable this way, i.e. alternative 1) of the description is actually (May 2011) implemented halfways.\n\n(No automatism yet, but there's this additional command-line option to forcefully use already existing prebuilt \"Python extension\" .so-files).\n\nIf this ticket bit-rots another two years, it should be closed as \"Won't Fix\".\n\nCheers,\nGeorg",
    "created_at": "2011-05-25T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51417",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi Stefan,
good catch! Yes, I do think the issue of this ticket currently is solvable this way, i.e. alternative 1) of the description is actually (May 2011) implemented halfways.

(No automatism yet, but there's this additional command-line option to forcefully use already existing prebuilt "Python extension" .so-files).

If this ticket bit-rots another two years, it should be closed as "Won't Fix".

Cheers,
Georg



---

archive/issue_comments_051418.json:
```json
{
    "body": "Changing assignee from tbd to GeorgSWeber.",
    "created_at": "2011-05-25T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51418",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing assignee from tbd to GeorgSWeber.



---

archive/issue_comments_051419.json:
```json
{
    "body": "Well, it's been almost another two years.  ;-)\n\nWhat's the status of this ticket after #12415?  Are the problems still present?",
    "created_at": "2013-03-14T21:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51419",
    "user": "https://github.com/roed314"
}
```

Well, it's been almost another two years.  ;-)

What's the status of this ticket after #12415?  Are the problems still present?



---

archive/issue_comments_051420.json:
```json
{
    "body": "Changing component from doctest to doctest framework.",
    "created_at": "2013-03-28T23:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51420",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to doctest framework.



---

archive/issue_comments_051421.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-28T23:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51421",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051422.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-28T23:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51422",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051423.json:
```json
{
    "body": "`sage -t foo.pyx` building the module is a feature not a bug.",
    "created_at": "2013-03-28T23:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51423",
    "user": "https://github.com/roed314"
}
```

`sage -t foo.pyx` building the module is a feature not a bug.



---

archive/issue_comments_051424.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-03-29T19:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6415#issuecomment-51424",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix



---

archive/issue_events_006659.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-29T19:01:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6415",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6415#event-6659"
}
```
