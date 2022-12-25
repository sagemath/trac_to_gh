# Issue 5533: Recompiling .spyx files changes class

archive/issues_005533.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  cwitty\n\nApparently, recompiling a .spyx file creates a new module and/or creates a new dummy class.  This gets in the way of pickling.  For example, start from a command prompt and follow the instructions using the attached junk7.spyx.\n\n```\nsage  # at the command prompt, start Sage\nsage: load 'junk7.spyx'\nsage: # make an insignificant change to junk7.spyx so it will recompile...\nsage: load 'junk7.spyx'\nsage: MyClass().greet()\nGreetings!\nsage: import pickle\nsage: fi = file('junk7.pjr', 'w')\nsage: pickle.dump(MyClass(), fi)\nsage: fi.close()\nsage: exit  # returns to the command line\n\nsage  # now restart sage from the command line\nsage: load 'junk7.spyx'\nsage: import pickle\nsage: fi = file('junk7.pjr', 'r')\nsage: tmp = pickle.load(fi)\n---------------------------------------------------------------------------\nImportError\n...\nImportError: No module named _home_ryan_uva_prng_well_sage_junk7_spyx_1\n```\n\nSo the error is trying to import the module.  Apparently compiling a .spyx file creates a new Python module each time?  Other than exiting Sage every time I want to recompile, I don't see a way around this problem -- or a way to fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5533\n\n",
    "created_at": "2009-03-16T19:41:11Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Recompiling .spyx files changes class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5533",
    "user": "https://github.com/rhinton"
}
```
Assignee: cwitty

CC:  cwitty

Apparently, recompiling a .spyx file creates a new module and/or creates a new dummy class.  This gets in the way of pickling.  For example, start from a command prompt and follow the instructions using the attached junk7.spyx.

```
sage  # at the command prompt, start Sage
sage: load 'junk7.spyx'
sage: # make an insignificant change to junk7.spyx so it will recompile...
sage: load 'junk7.spyx'
sage: MyClass().greet()
Greetings!
sage: import pickle
sage: fi = file('junk7.pjr', 'w')
sage: pickle.dump(MyClass(), fi)
sage: fi.close()
sage: exit  # returns to the command line

sage  # now restart sage from the command line
sage: load 'junk7.spyx'
sage: import pickle
sage: fi = file('junk7.pjr', 'r')
sage: tmp = pickle.load(fi)
---------------------------------------------------------------------------
ImportError
...
ImportError: No module named _home_ryan_uva_prng_well_sage_junk7_spyx_1
```

So the error is trying to import the module.  Apparently compiling a .spyx file creates a new Python module each time?  Other than exiting Sage every time I want to recompile, I don't see a way around this problem -- or a way to fix it.

Issue created by migration from https://trac.sagemath.org/ticket/5533





---

archive/issue_comments_042937.json:
```json
{
    "body": "Defines a dummy class for pickling/unpickling test",
    "created_at": "2009-03-16T19:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5533#issuecomment-42937",
    "user": "https://github.com/rhinton"
}
```

Defines a dummy class for pickling/unpickling test



---

archive/issue_comments_042938.json:
```json
{
    "body": "Attachment [junk7.spyx](tarball://root/attachments/some-uuid/ticket5533/junk7.spyx) by mabshoff created at 2009-04-23 08:05:05",
    "created_at": "2009-04-23T08:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5533#issuecomment-42938",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [junk7.spyx](tarball://root/attachments/some-uuid/ticket5533/junk7.spyx) by mabshoff created at 2009-04-23 08:05:05
