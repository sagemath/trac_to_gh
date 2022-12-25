# Issue 5019: sage -gdb is broken on OSX when using branches

archive/issues_005019.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is a followup to #4991: When running `sage -gdb` on OSX with branches the following failure occurs:\n\n```\n...\n. done\nReading symbols for shared libraries warning: Could not find object file \"/Users/wstein/sage-3.2.3/devel/sage-main/build/temp.macosx-10.3-i386-2.5/sage/ext/interactive_constructors_c.o\" - no debug information available for \"sage/ext/interactive_constructors_c.c\".\n\n. done\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Users/wstein/sage/local/lib/python2.5/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/Users/wstein/ipy_profile_sage.py in <module>()\n     14     from sage.misc.interpreter import attached_files\n     15 \n---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())\n     17     if branch:\n     18         print branch\n\n/Users/wstein/sage/local/lib/python2.5/site-packages/sage/misc/misc.pyc in branch_current_hg()\n   1502     i = s.rfind('->')\n   1503     if i == -1:\n-> 1504         raise RuntimeError, \"unable to determine branch?!\"\n   1505     s = s[i+2:]\n   1506     i = s.find('-')\n\nRuntimeError: unable to determine branch?!\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\nsage: \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5019\n\n",
    "created_at": "2009-01-19T02:05:15Z",
    "labels": [
        "component: misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -gdb is broken on OSX when using branches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

This is a followup to #4991: When running `sage -gdb` on OSX with branches the following failure occurs:

```
...
. done
Reading symbols for shared libraries warning: Could not find object file "/Users/wstein/sage-3.2.3/devel/sage-main/build/temp.macosx-10.3-i386-2.5/sage/ext/interactive_constructors_c.o" - no debug information available for "sage/ext/interactive_constructors_c.c".

. done
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/wstein/sage/local/lib/python2.5/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/Users/wstein/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/Users/wstein/sage/local/lib/python2.5/site-packages/sage/misc/misc.pyc in branch_current_hg()
   1502     i = s.rfind('->')
   1503     if i == -1:
-> 1504         raise RuntimeError, "unable to determine branch?!"
   1505     s = s[i+2:]
   1506     i = s.find('-')

RuntimeError: unable to determine branch?!
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage: 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5019





---

archive/issue_comments_038164.json:
```json
{
    "body": "No longer relevant?",
    "created_at": "2015-04-13T14:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5019#issuecomment-38164",
    "user": "https://github.com/mezzarobba"
}
```

No longer relevant?



---

archive/issue_comments_038165.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T14:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5019#issuecomment-38165",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-11-04T14:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5019#issuecomment-38166",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005263.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-11-04T22:18:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5019#event-5263"
}
```



---

archive/issue_comments_038167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-11-04T22:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5019#issuecomment-38167",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
