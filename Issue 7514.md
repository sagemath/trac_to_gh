# Issue 7514: rewrite load and attach

archive/issues_007514.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  slabbe robertwb ddrake\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7514\n\n",
    "created_at": "2009-11-22T08:12:38Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "rewrite load and attach",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7514",
    "user": "was"
}
```
Assignee: tbd

CC:  slabbe robertwb ddrake



Issue created by migration from https://trac.sagemath.org/ticket/7514





---

archive/issue_comments_063617.json:
```json
{
    "body": "Attachment [sagelib-7514.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514.patch) by was created at 2009-11-22 08:13:56\n\napply to the core sage library",
    "created_at": "2009-11-22T08:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63617",
    "user": "was"
}
```

Attachment [sagelib-7514.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514.patch) by was created at 2009-11-22 08:13:56

apply to the core sage library



---

archive/issue_comments_063618.json:
```json
{
    "body": "Attachment [sagenb-7514.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514.patch) by was created at 2009-11-22 08:16:59",
    "created_at": "2009-11-22T08:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63618",
    "user": "was"
}
```

Attachment [sagenb-7514.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514.patch) by was created at 2009-11-22 08:16:59



---

archive/issue_comments_063619.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T08:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63619",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063620.json:
```json
{
    "body": "Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.\n\nMaybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??\n\nS\u00e9bastien",
    "created_at": "2009-11-23T10:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63620",
    "user": "slabbe"
}
```

Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.

Maybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??

Sébastien



---

archive/issue_comments_063621.json:
```json
{
    "body": "> Can we attach a file already in the sage tree that we are editing?\n\n> I stopped using it because sometimes the changes in the file were not\n>  considered and I have been stopping sage and running sage -br ever since then. \n\nYou probably don't understand what attach does.  All it does is execfile the file that you attached.  There are situations where this happening might be perceived as \"the file were not considered\".  E.g., if you create an install F of a class Foo defined in a file a.py, then a.py is reloaded, the object F is *not* somehow magically modified in memory to be an instance of a the new Foo that was defined in the file a.py.    That's not how Python works, and it would be weird and confusing overall if things did work that way.",
    "created_at": "2009-11-23T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63621",
    "user": "was"
}
```

> Can we attach a file already in the sage tree that we are editing?

> I stopped using it because sometimes the changes in the file were not
>  considered and I have been stopping sage and running sage -br ever since then. 

You probably don't understand what attach does.  All it does is execfile the file that you attached.  There are situations where this happening might be perceived as "the file were not considered".  E.g., if you create an install F of a class Foo defined in a file a.py, then a.py is reloaded, the object F is *not* somehow magically modified in memory to be an instance of a the new Foo that was defined in the file a.py.    That's not how Python works, and it would be weird and confusing overall if things did work that way.



---

archive/issue_comments_063622.json:
```json
{
    "body": "Attachment [sagelib_7514-part2.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib_7514-part2.patch) by was created at 2009-12-02 03:52:21",
    "created_at": "2009-12-02T03:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63622",
    "user": "was"
}
```

Attachment [sagelib_7514-part2.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib_7514-part2.patch) by was created at 2009-12-02 03:52:21



---

archive/issue_comments_063623.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T21:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63623",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063624.json:
```json
{
    "body": "Replying to [comment:2 slabbe]:\n> Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.\n> \n> Maybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??\n> \n\nYou just have to *understand* what attach does.  It reloads the file via execfile into the global namespace when the file changes.  You can attach any file, in the tree or not.  But imagine this:   In the sage tree there is a file foo.py.  There is another file bar.py that does \"import foo\" and uses some code in foo.  If you attach foo.py (which results in exec'ing it in the global interpreter namespaces), then that will have no impact at all on bar.py.  \n\nThus for some problems attach works very nicely for library code, and for others it doesn't.  Which is which is clearer if you know what attach does.",
    "created_at": "2009-12-08T21:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63624",
    "user": "was"
}
```

Replying to [comment:2 slabbe]:
> Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.
> 
> Maybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??
> 

You just have to *understand* what attach does.  It reloads the file via execfile into the global namespace when the file changes.  You can attach any file, in the tree or not.  But imagine this:   In the sage tree there is a file foo.py.  There is another file bar.py that does "import foo" and uses some code in foo.  If you attach foo.py (which results in exec'ing it in the global interpreter namespaces), then that will have no impact at all on bar.py.  

Thus for some problems attach works very nicely for library code, and for others it doesn't.  Which is which is clearer if you know what attach does.



---

archive/issue_comments_063625.json:
```json
{
    "body": "Attachment [sagelib-7514_combined.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.patch) by mpatel created at 2009-12-09 23:20:51\n\nCombined *sage* repo patch.  Depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, #7482.",
    "created_at": "2009-12-09T23:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63625",
    "user": "mpatel"
}
```

Attachment [sagelib-7514_combined.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.patch) by mpatel created at 2009-12-09 23:20:51

Combined *sage* repo patch.  Depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, #7482.



---

archive/issue_comments_063626.json:
```json
{
    "body": "I've attached a combined \"sagelib\" patch.  It depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, and #7482.\n\nOut of curiosity:  What if we \"overload\" `import` by keeping a stack of all imported modules.  When a watched file changes, we reload it and all modules loaded since the watched file was first loaded?  Would this be useful in some situations?",
    "created_at": "2009-12-10T01:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63626",
    "user": "mpatel"
}
```

I've attached a combined "sagelib" patch.  It depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, and #7482.

Out of curiosity:  What if we "overload" `import` by keeping a stack of all imported modules.  When a watched file changes, we reload it and all modules loaded since the watched file was first loaded?  Would this be useful in some situations?



---

archive/issue_comments_063627.json:
```json
{
    "body": "With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:\n\n```\n        sage -t  devel/sage/sage/misc/sageinspect.py # 3 doctests failed\n        sage -t  devel/sage/sage/misc/preparser.py # 10 doctests failed\n        sage -t  devel/sage/sage/misc/reset.pyx # 2 doctests failed\n        sage -t  devel/sage/sage/misc/session.pyx # 1 doctests failed\n```\n\nShould we stop doctesting most (all?) of `sage/server`?",
    "created_at": "2009-12-10T02:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63627",
    "user": "mpatel"
}
```

With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:

```
        sage -t  devel/sage/sage/misc/sageinspect.py # 3 doctests failed
        sage -t  devel/sage/sage/misc/preparser.py # 10 doctests failed
        sage -t  devel/sage/sage/misc/reset.pyx # 2 doctests failed
        sage -t  devel/sage/sage/misc/session.pyx # 1 doctests failed
```

Should we stop doctesting most (all?) of `sage/server`?



---

archive/issue_comments_063628.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:\n\nThree tests fail in `sagenb.misc.sageinpect`.  Please see #7650.\n\n> Should we stop doctesting most (all?) of `sage/server`?\n\nPlease see #7534.",
    "created_at": "2009-12-10T12:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63628",
    "user": "mpatel"
}
```

Replying to [comment:8 mpatel]:
> With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:

Three tests fail in `sagenb.misc.sageinpect`.  Please see #7650.

> Should we stop doctesting most (all?) of `sage/server`?

Please see #7534.



---

archive/issue_comments_063629.json:
```json
{
    "body": "I noticed\n\n```python\nsage: f = 1\nsage: save(f, 'f')\nsage: attach('f.sobj')\nTraceback (most recent call last)\n...\nValueError: argument (='f.sobj') to load or attach must have extension py, sage, or pyx                             \nsage: attached_files()\n['f.sobj']\n```\n\n\nQuestions about loading/attaching Cython files:\n\n* Can they only be loaded once, if they haven't changed?  For example: If `zzz.pyx` contains `print 'Zzz!'`, I see\n\n```python\nsage: load('zzz.pyx')\nCompiling zzz.pyx...\nZzz!\nsage: load('zzz.pyx')\nsage: load('zzz.pyx')\nsage: # Now I edit zzz.pyx\nsage: load('zzz.pyx')\nCompiling zzz.pyx...\nAwake!\n```\n\n\n* Can they access existing objects?  For example: If I put\n\n```python\ntry:\n    b += 1\nexcept:\n    b = 10\nprint b\n```\n\n\n    in a .pyx file, loading the file always sets `b` to 10, even if it's already defined.\n\nDisclaimer:  I'm still quite ignorant about Cython.",
    "created_at": "2009-12-28T13:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63629",
    "user": "mpatel"
}
```

I noticed

```python
sage: f = 1
sage: save(f, 'f')
sage: attach('f.sobj')
Traceback (most recent call last)
...
ValueError: argument (='f.sobj') to load or attach must have extension py, sage, or pyx                             
sage: attached_files()
['f.sobj']
```


Questions about loading/attaching Cython files:

* Can they only be loaded once, if they haven't changed?  For example: If `zzz.pyx` contains `print 'Zzz!'`, I see

```python
sage: load('zzz.pyx')
Compiling zzz.pyx...
Zzz!
sage: load('zzz.pyx')
sage: load('zzz.pyx')
sage: # Now I edit zzz.pyx
sage: load('zzz.pyx')
Compiling zzz.pyx...
Awake!
```


* Can they access existing objects?  For example: If I put

```python
try:
    b += 1
except:
    b = 10
print b
```


    in a .pyx file, loading the file always sets `b` to 10, even if it's already defined.

Disclaimer:  I'm still quite ignorant about Cython.



---

archive/issue_comments_063630.json:
```json
{
    "body": "Attachment [sagenb-7514.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514.2.patch) by mpatel created at 2009-12-28 17:10:46\n\nFixed doctest failures.  Replaces previous.",
    "created_at": "2009-12-28T17:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63630",
    "user": "mpatel"
}
```

Attachment [sagenb-7514.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514.2.patch) by mpatel created at 2009-12-28 17:10:46

Fixed doctest failures.  Replaces previous.



---

archive/issue_comments_063631.json:
```json
{
    "body": "Fixed doctest failures.  Depends on Sage 4.3, #7483, #7482.  Replaces previous.",
    "created_at": "2009-12-28T17:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63631",
    "user": "mpatel"
}
```

Fixed doctest failures.  Depends on Sage 4.3, #7483, #7482.  Replaces previous.



---

archive/issue_comments_063632.json:
```json
{
    "body": "Attachment [sagelib-7514_combined.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.2.patch) by mpatel created at 2009-12-28 18:22:45\n\nThe latest patches should fix the doctests and the `attached_files` problem mentioned above.  I changed `attach t` to `attach(t)`, since the doctesting framework appears to use a Python interpreter, i.e., *not* IPython, to run the examples.  I also weakened [somewhat] the tests for `preparser.modified_attached_files`.  Is there an IPython doctesting mode?\n\nI'm not sure about the Cython file reload problem.  Should we set `use_cache=True` when loading .pyx files explicitly?\n\nOn globals:  I see that a Cython file `foo.pyx` is compiled to a module and loaded via `from foo import *`.\n\nCan someone else please help to review this ticket?",
    "created_at": "2009-12-28T18:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63632",
    "user": "mpatel"
}
```

Attachment [sagelib-7514_combined.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.2.patch) by mpatel created at 2009-12-28 18:22:45

The latest patches should fix the doctests and the `attached_files` problem mentioned above.  I changed `attach t` to `attach(t)`, since the doctesting framework appears to use a Python interpreter, i.e., *not* IPython, to run the examples.  I also weakened [somewhat] the tests for `preparser.modified_attached_files`.  Is there an IPython doctesting mode?

I'm not sure about the Cython file reload problem.  Should we set `use_cache=True` when loading .pyx files explicitly?

On globals:  I see that a Cython file `foo.pyx` is compiled to a module and loaded via `from foo import *`.

Can someone else please help to review this ticket?



---

archive/issue_comments_063633.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-28T18:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63633",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063634.json:
```json
{
    "body": "Fix(?) loading of .spyx files.  Add preparser.py to reference manual.  Replaces previous.",
    "created_at": "2009-12-28T21:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63634",
    "user": "mpatel"
}
```

Fix(?) loading of .spyx files.  Add preparser.py to reference manual.  Replaces previous.



---

archive/issue_comments_063635.json:
```json
{
    "body": "Attachment [sagelib-7514_combined.3.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.3.patch) by was created at 2009-12-31 17:34:42",
    "created_at": "2009-12-31T17:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63635",
    "user": "was"
}
```

Attachment [sagelib-7514_combined.3.patch](tarball://root/attachments/some-uuid/ticket7514/sagelib-7514_combined.3.patch) by was created at 2009-12-31 17:34:42



---

archive/issue_comments_063636.json:
```json
{
    "body": "Attachment [sagenb-7514-rebase.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase.patch) by was created at 2009-12-31 17:51:05\n\nrebased against sagenb-0.4.8 + trac #7483.",
    "created_at": "2009-12-31T17:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63636",
    "user": "was"
}
```

Attachment [sagenb-7514-rebase.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase.patch) by was created at 2009-12-31 17:51:05

rebased against sagenb-0.4.8 + trac #7483.



---

archive/issue_comments_063637.json:
```json
{
    "body": "trac 7514 sagenb-part2: proper tracebacks; make source code introspection of functions defined in \\ the notebook finally work in the notebook; properly cleanup worksheet files when notebook server is killed.",
    "created_at": "2009-12-31T19:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63637",
    "user": "was"
}
```

trac 7514 sagenb-part2: proper tracebacks; make source code introspection of functions defined in \ the notebook finally work in the notebook; properly cleanup worksheet files when notebook server is killed.



---

archive/issue_comments_063638.json:
```json
{
    "body": "Attachment [sagenb-7514-rebase-part2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part2.patch) by was created at 2009-12-31 19:35:03\n\nRight now the files that one must apply are:\n\n\n```\nTo Sage Library:\n sagelib-7514_combined.3.patch \n\nTo Notebook:\n sagenb-7514-rebase.patch  \n sagenb-7514-rebase-part2.patch\n```\n",
    "created_at": "2009-12-31T19:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63638",
    "user": "was"
}
```

Attachment [sagenb-7514-rebase-part2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part2.patch) by was created at 2009-12-31 19:35:03

Right now the files that one must apply are:


```
To Sage Library:
 sagelib-7514_combined.3.patch 

To Notebook:
 sagenb-7514-rebase.patch  
 sagenb-7514-rebase-part2.patch
```




---

archive/issue_comments_063639.json:
```json
{
    "body": "The file sagenb-7514-rebase-part2.patch fixes some serious issues.  In particular, it makes it so we get proper tracebacks on errors, which was broken without this patch by the new architecture (of doing everything in the worksheet process, etc.).  Also, source code introspection now works again for functions defined in the notebook, which many users wanted.  Finally, there was a little bug where pressing control-c to stop the notebook server didn't result in quitting all worksheet processes, hence they left junk around.",
    "created_at": "2009-12-31T19:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63639",
    "user": "was"
}
```

The file sagenb-7514-rebase-part2.patch fixes some serious issues.  In particular, it makes it so we get proper tracebacks on errors, which was broken without this patch by the new architecture (of doing everything in the worksheet process, etc.).  Also, source code introspection now works again for functions defined in the notebook, which many users wanted.  Finally, there was a little bug where pressing control-c to stop the notebook server didn't result in quitting all worksheet processes, hence they left junk around.



---

archive/issue_comments_063640.json:
```json
{
    "body": "* When I load/attach a .(s)pyx file in the notebook, `___code__.py` appears in the cell's output HTML.\n\n  * Minor: Should we make `attached_files()` in the notebook report, e.g.,\n\n```\n[DATA+'foo.py']\n```\n\n   instead of\n\n```\n['/full/path/to/foo.py']\n```\n\n\n* Typing `f??<TAB>` for a function `f` defined in the notebook shows its docstring but not its source code.  Is this related to ?? not working for Cython functions defined in cells or attached `DATA` files?\n\n* Should we make it possible to edit attached .pyx files, just as we can edit .py, .sage, .spyx, and .txt files?\n\n* Minor: `save_notebook` appears to be called twice on shutdown.  Is this a fail-safe behavior?",
    "created_at": "2010-01-01T03:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63640",
    "user": "mpatel"
}
```

* When I load/attach a .(s)pyx file in the notebook, `___code__.py` appears in the cell's output HTML.

  * Minor: Should we make `attached_files()` in the notebook report, e.g.,

```
[DATA+'foo.py']
```

   instead of

```
['/full/path/to/foo.py']
```


* Typing `f??<TAB>` for a function `f` defined in the notebook shows its docstring but not its source code.  Is this related to ?? not working for Cython functions defined in cells or attached `DATA` files?

* Should we make it possible to edit attached .pyx files, just as we can edit .py, .sage, .spyx, and .txt files?

* Minor: `save_notebook` appears to be called twice on shutdown.  Is this a fail-safe behavior?



---

archive/issue_comments_063641.json:
```json
{
    "body": "> When I load/attach a .(s)pyx file in the notebook, ___code__.py appears in \n> the cell's output HTML. \n\nThat's a bug.  I'll fix it soon. \n\n> Minor: Should we make attached_files() in the notebook report\n\nI'm not sure.  But I think this should be a separate ticket, since it would be a new feature. \n\n>     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. \n\nThat's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. \n\n> Minor: save_notebook appears to be called twice on shutdown. Is this a fail-safe behavior?\n\nThis has been the case forever.  It is not caused by this patch.  I don't think it is desirable.  Please do open a ticket. \n\nOK, so I'm going to fix the ___code___.py issue you reported above, triple check that f?? works, and if not, figure out what went wrong, then mark this as \"needs review\" again.",
    "created_at": "2010-01-01T04:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63641",
    "user": "was"
}
```

> When I load/attach a .(s)pyx file in the notebook, ___code__.py appears in 
> the cell's output HTML. 

That's a bug.  I'll fix it soon. 

> Minor: Should we make attached_files() in the notebook report

I'm not sure.  But I think this should be a separate ticket, since it would be a new feature. 

>     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. 

That's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. 

> Minor: save_notebook appears to be called twice on shutdown. Is this a fail-safe behavior?

This has been the case forever.  It is not caused by this patch.  I don't think it is desirable.  Please do open a ticket. 

OK, so I'm going to fix the ___code___.py issue you reported above, triple check that f?? works, and if not, figure out what went wrong, then mark this as "needs review" again.



---

archive/issue_comments_063642.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-01T04:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63642",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063643.json:
```json
{
    "body": "Replying to [comment:16 was]:\n> >     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. \n> \n> That's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. \n\nIt seems that just the last line of code is omitted.  The source displayed is the preparsed source, but I don't know if this is a problem.",
    "created_at": "2010-01-01T05:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63643",
    "user": "mpatel"
}
```

Replying to [comment:16 was]:
> >     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. 
> 
> That's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. 

It seems that just the last line of code is omitted.  The source displayed is the preparsed source, but I don't know if this is a problem.



---

archive/issue_comments_063644.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-01T05:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63644",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063645.json:
```json
{
    "body": "The attached patch (sagenb-7514-rebase-part3.patch) should:\n\n1. Fixed this: \"When I load/attach a .(s)pyx file in the notebook, _code.py appears in the cell's output HTML.\"\n\n2. Fixed this: \"Typing f??<TAB> for a function f defined in the notebook shows its docstring but not its source code.\"  Actually, this wasn't exactly broken... the last line of the docstring was missing.  I've added a newline to the end of the input file, and now the problem is gone.  This isn't a hack, since I think files are *supposed* to end with a newline, according to \"IEEE Standard 1003.1 (aka POSIX)\".   Note that this patch *only* adds support for f?? for functions specifically entered in input normal cells (not cython, not load/attached).  That's another issue.",
    "created_at": "2010-01-01T05:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63645",
    "user": "was"
}
```

The attached patch (sagenb-7514-rebase-part3.patch) should:

1. Fixed this: "When I load/attach a .(s)pyx file in the notebook, _code.py appears in the cell's output HTML."

2. Fixed this: "Typing f??<TAB> for a function f defined in the notebook shows its docstring but not its source code."  Actually, this wasn't exactly broken... the last line of the docstring was missing.  I've added a newline to the end of the input file, and now the problem is gone.  This isn't a hack, since I think files are *supposed* to end with a newline, according to "IEEE Standard 1003.1 (aka POSIX)".   Note that this patch *only* adds support for f?? for functions specifically entered in input normal cells (not cython, not load/attached).  That's another issue.



---

archive/issue_comments_063646.json:
```json
{
    "body": "Attachment [sagenb-7514-rebase-part3.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part3.patch) by was created at 2010-01-01 05:36:49",
    "created_at": "2010-01-01T05:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63646",
    "user": "was"
}
```

Attachment [sagenb-7514-rebase-part3.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part3.patch) by was created at 2010-01-01 05:36:49



---

archive/issue_comments_063647.json:
```json
{
    "body": "Attachment [sagenb-7514-rebase-part3.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part3.2.patch) by mpatel created at 2010-01-01 06:12:31\n\nTrivial docstring tweaks.  Replaces previous.",
    "created_at": "2010-01-01T06:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63647",
    "user": "mpatel"
}
```

Attachment [sagenb-7514-rebase-part3.2.patch](tarball://root/attachments/some-uuid/ticket7514/sagenb-7514-rebase-part3.2.patch) by mpatel created at 2010-01-01 06:12:31

Trivial docstring tweaks.  Replaces previous.



---

archive/issue_comments_063648.json:
```json
{
    "body": "Positive review.\n\nIf it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.",
    "created_at": "2010-01-01T06:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63648",
    "user": "mpatel"
}
```

Positive review.

If it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.



---

archive/issue_comments_063649.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-01T06:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63649",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063650.json:
```json
{
    "body": "Replying to [comment:19 mpatel]:\n> Positive review.\n> \n> If it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.\n\nI'll make a separate ticket instead.  We should include `load` and `attach` in the reference manual.",
    "created_at": "2010-01-01T06:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63650",
    "user": "mpatel"
}
```

Replying to [comment:19 mpatel]:
> Positive review.
> 
> If it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.

I'll make a separate ticket instead.  We should include `load` and `attach` in the reference manual.



---

archive/issue_comments_063651.json:
```json
{
    "body": "The preparsing function introduced in #7483 lacks a \"# -*- coding: utf-8 -*-\" header that prevents the notebook from evaluating any string that contains unicode. This is addressed in #7835.",
    "created_at": "2010-01-03T19:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63651",
    "user": "timdumol"
}
```

The preparsing function introduced in #7483 lacks a "# -*- coding: utf-8 -*-" header that prevents the notebook from evaluating any string that contains unicode. This is addressed in #7835.



---

archive/issue_comments_063652.json:
```json
{
    "body": "I've merged sagelib-7514_combined.patch in sage-4.3.1.alpha0.",
    "created_at": "2010-01-03T22:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63652",
    "user": "mhansen"
}
```

I've merged sagelib-7514_combined.patch in sage-4.3.1.alpha0.



---

archive/issue_comments_063653.json:
```json
{
    "body": "I merged the sagenb patches into sagenb-0.4.8.",
    "created_at": "2010-01-04T06:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63653",
    "user": "was"
}
```

I merged the sagenb patches into sagenb-0.4.8.



---

archive/issue_comments_063654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63654",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_063655.json:
```json
{
    "body": "The attachment [sagelib-7514_combined.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7514/sagelib-7514_combined.3.patch) in the Sage library.",
    "created_at": "2010-01-28T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7514#issuecomment-63655",
    "user": "mvngu"
}
```

The attachment [sagelib-7514_combined.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7514/sagelib-7514_combined.3.patch) in the Sage library.
