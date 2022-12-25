# Issue 7911: scilab interface is missing in the notebook dropdown menu

archive/issues_007911.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu\n\nKeywords: scilab,notebook\n\nThe dropdown menu that shows the different interfaces is missing scilab.\n\nUsing %scilab in a notebook cell works though\n\nIssue created by migration from https://trac.sagemath.org/ticket/7911\n\n",
    "created_at": "2010-01-12T18:20:31Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "scilab interface is missing in the notebook dropdown menu",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7911",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: @williamstein

CC:  mvngu

Keywords: scilab,notebook

The dropdown menu that shows the different interfaces is missing scilab.

Using %scilab in a notebook cell works though

Issue created by migration from https://trac.sagemath.org/ticket/7911





---

archive/issue_comments_068679.json:
```json
{
    "body": "Attachment [trac_7911-missing_scilab.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-missing_scilab.patch) by @qed777 created at 2010-01-25 14:52:05\n\nAdd scilab to drop-down list.  sagenb repo.",
    "created_at": "2010-01-25T14:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68679",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7911-missing_scilab.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-missing_scilab.patch) by @qed777 created at 2010-01-25 14:52:05

Add scilab to drop-down list.  sagenb repo.



---

archive/issue_comments_068680.json:
```json
{
    "body": "I think we just need to add `'scilab (optional)'` to the `SYSTEMS` list in `notebook.py`.  But I can't test the patch, since I don't have Scilab installed.",
    "created_at": "2010-01-25T14:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68680",
    "user": "https://github.com/qed777"
}
```

I think we just need to add `'scilab (optional)'` to the `SYSTEMS` list in `notebook.py`.  But I can't test the patch, since I don't have Scilab installed.



---

archive/issue_comments_068681.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T14:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68681",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068682.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-01-25T14:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68682",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to minor.



---

archive/issue_events_018934.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T14:54:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7911#event-18934"
}
```



---

archive/issue_comments_068683.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T14:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68683",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068684.json:
```json
{
    "body": "Patch had errors for sage-4.3.2-alpha0\n\napplying trac_7911-missing_scilab.patch\nunable to find 'sagenb/notebook/notebook.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sagenb/notebook/notebook.py.rej\npatch failed, unable to continue (try -v)\nsagenb/notebook/notebook.py: No such file or directory\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7911-missing_scilab.patch",
    "created_at": "2010-01-31T14:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68684",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Patch had errors for sage-4.3.2-alpha0

applying trac_7911-missing_scilab.patch
unable to find 'sagenb/notebook/notebook.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file sagenb/notebook/notebook.py.rej
patch failed, unable to continue (try -v)
sagenb/notebook/notebook.py: No such file or directory
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7911-missing_scilab.patch



---

archive/issue_comments_068685.json:
```json
{
    "body": "To which repository did you try to apply the patch?",
    "created_at": "2010-01-31T14:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68685",
    "user": "https://github.com/qed777"
}
```

To which repository did you try to apply the patch?



---

archive/issue_comments_068686.json:
```json
{
    "body": "I'm changing this back to \"needs review.\"\n\nWe should make it easier to develop for the notebook.",
    "created_at": "2010-01-31T23:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68686",
    "user": "https://github.com/qed777"
}
```

I'm changing this back to "needs review."

We should make it easier to develop for the notebook.



---

archive/issue_comments_068687.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-31T23:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68687",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068688.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> To which repository did you try to apply the patch?\n\n\nI applied the patch to the alpha0 version of sage on my local PC - built from source (if thats what you meant). I installed scilab yesterday so Im in a position to try reviewing the ticket again if you want (if you want to take this offline contact me at \"bw7890 at gmail dot com\")",
    "created_at": "2010-02-01T11:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68688",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Replying to [comment:3 mpatel]:
> To which repository did you try to apply the patch?


I applied the patch to the alpha0 version of sage on my local PC - built from source (if thats what you meant). I installed scilab yesterday so Im in a position to try reviewing the ticket again if you want (if you want to take this offline contact me at "bw7890 at gmail dot com")



---

archive/issue_comments_068689.json:
```json
{
    "body": "Attachment [trac_7911-missing_scilab.2.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-missing_scilab.2.patch) by @qed777 created at 2010-02-01 12:35:57\n\nSame as previous, except for SageNB 0.6.  Apply just one of these.  sagenb repo.",
    "created_at": "2010-02-01T12:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68689",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7911-missing_scilab.2.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-missing_scilab.2.patch) by @qed777 created at 2010-02-01 12:35:57

Same as previous, except for SageNB 0.6.  Apply just one of these.  sagenb repo.



---

archive/issue_comments_068690.json:
```json
{
    "body": "The notebook is now actually a [separate project](http://nb.sagemath.org/), with it's own \"sagenb\" repository.  (I'm assuming that you didn't apply the patch to this repository.  In any case, absolutely no offense is intended.)  Since you built Sage from source, there should be a ~20 MB file `$SAGE_ROOT/spkg/standard/sagenb-0.6.spkg`, where `$SAGE_ROOT` is the distribution's base install directory.  To test the patch, try, e.g., \n\n```sh\nmkdir tmp\ncd tmp\ntar jxvf $SAGE_ROOT/spkg/standard/sagenb-0.6.spkg  # [1]\ncd sagenb-0.6/src/sagenb\nsage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-missing_scilab.2.patch  # [2, 3]\nsage -hg qpush\nsage -python setup.py install     # [4]\n```\nThen start the notebook and see if/how I messed up. :)  You can run the notebook doctests with `sage -t -sagenb`.\n\nBy the way, if you'd like to apply the patch to the upcoming SageNB release (0.7.x), get the spkg from #8051 and use the first patch above.\n\n* ![1] To install an spkg directly, use, e.g., `sage -f sagenb-0.6.spkg`.\n* ![2] This assumes you've enabled the [Mercurial Queues](http://wiki.sagemath.org/MercurialQueues?highlight=%28queues%29) extension.\n* ![3] If your system already has a relatively recent version of Mercurial installed, you can substitute `hg` for `sage -hg`.\n* ![4] Or run `sage -python setup.py develop` to work \"in place.\"  This is great for experimenting.\n\nPlease let me know if you have any questions.",
    "created_at": "2010-02-01T13:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68690",
    "user": "https://github.com/qed777"
}
```

The notebook is now actually a [separate project](http://nb.sagemath.org/), with it's own "sagenb" repository.  (I'm assuming that you didn't apply the patch to this repository.  In any case, absolutely no offense is intended.)  Since you built Sage from source, there should be a ~20 MB file `$SAGE_ROOT/spkg/standard/sagenb-0.6.spkg`, where `$SAGE_ROOT` is the distribution's base install directory.  To test the patch, try, e.g., 

```sh
mkdir tmp
cd tmp
tar jxvf $SAGE_ROOT/spkg/standard/sagenb-0.6.spkg  # [1]
cd sagenb-0.6/src/sagenb
sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-missing_scilab.2.patch  # [2, 3]
sage -hg qpush
sage -python setup.py install     # [4]
```
Then start the notebook and see if/how I messed up. :)  You can run the notebook doctests with `sage -t -sagenb`.

By the way, if you'd like to apply the patch to the upcoming SageNB release (0.7.x), get the spkg from #8051 and use the first patch above.

* ![1] To install an spkg directly, use, e.g., `sage -f sagenb-0.6.spkg`.
* ![2] This assumes you've enabled the [Mercurial Queues](http://wiki.sagemath.org/MercurialQueues?highlight=%28queues%29) extension.
* ![3] If your system already has a relatively recent version of Mercurial installed, you can substitute `hg` for `sage -hg`.
* ![4] Or run `sage -python setup.py develop` to work "in place."  This is great for experimenting.

Please let me know if you have any questions.



---

archive/issue_comments_068691.json:
```json
{
    "body": "\"Uncompressed sagenb-0.6.spkg in tmp\", etc (as suggested) and (1) there were no patch errors and (2) ran doctests - all passed :-)\n\nStarted the notebook using $SAGE_ROOT/sage and found \"scilab (optional)\" is magically now present! \n\nI tried a simple scilab command in the scilab console to make sure scilab was ok (I used eye(3,3) ), then tried it in the notebook and got\n\n```\n\neye(3)\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_3.py\", line 4, in <module>\n    print _support_.syseval(scilab, ur\\u0027\\u0027\\u0027eye(3,3)\\u0027\\u0027\\u0027, \\u0027/home/ross/.sage/sage_notebook.sagenb/home/admin/65/cells/1\\u0027)\n  File \"\", line 1, in <module>\n    \n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg/sagenb/misc/support.py\", line 470, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\nTypeError: eval() takes exactly 2 non-keyword arguments (3 given)\n```\n\nLet me know if I skipped something. (And definitely no offence taken - you left very good instructions - thanks :-)",
    "created_at": "2010-02-01T14:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68691",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

"Uncompressed sagenb-0.6.spkg in tmp", etc (as suggested) and (1) there were no patch errors and (2) ran doctests - all passed :-)

Started the notebook using $SAGE_ROOT/sage and found "scilab (optional)" is magically now present! 

I tried a simple scilab command in the scilab console to make sure scilab was ok (I used eye(3,3) ), then tried it in the notebook and got

```

eye(3)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_3.py", line 4, in <module>
    print _support_.syseval(scilab, ur\u0027\u0027\u0027eye(3,3)\u0027\u0027\u0027, \u0027/home/ross/.sage/sage_notebook.sagenb/home/admin/65/cells/1\u0027)
  File "", line 1, in <module>
    
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg/sagenb/misc/support.py", line 470, in syseval
    return system.eval(cmd, sage_globals, locals = sage_globals)
TypeError: eval() takes exactly 2 non-keyword arguments (3 given)
```

Let me know if I skipped something. (And definitely no offence taken - you left very good instructions - thanks :-)



---

archive/issue_comments_068692.json:
```json
{
    "body": "Minor addendum - I actually typed eye(3,3) (this returns a 3x3 identity matrix)",
    "created_at": "2010-02-01T14:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68692",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Minor addendum - I actually typed eye(3,3) (this returns a 3x3 identity matrix)



---

archive/issue_comments_068693.json:
```json
{
    "body": "Make `scilab.eval` accept extra non-keyword arguments.  **sage** repository.",
    "created_at": "2010-02-02T20:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68693",
    "user": "https://github.com/qed777"
}
```

Make `scilab.eval` accept extra non-keyword arguments.  **sage** repository.



---

archive/issue_comments_068694.json:
```json
{
    "body": "Attachment [trac_7911-sage_scilab.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-sage_scilab.patch) by @qed777 created at 2010-02-02 20:57:22\n\nWe may need to update the Scilab interface (and its `optional` doctests).  I've posted a [attachment:trac_7911-sage_scilab.patch workaround patch] to the main Sage library.  I'm not sure it's the best way to proceed --- we should get some expert input ---  but it seems to work.  Let me know what happens.\n\nTo apply the patch:\n\n```\ncd $SAGE_ROOT/devel/sage/\nhg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-sage_scilab.patch\nhg qpush\nsage -b    # This rebuilds the updated files.\n```",
    "created_at": "2010-02-02T20:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68694",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7911-sage_scilab.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-sage_scilab.patch) by @qed777 created at 2010-02-02 20:57:22

We may need to update the Scilab interface (and its `optional` doctests).  I've posted a [attachment:trac_7911-sage_scilab.patch workaround patch] to the main Sage library.  I'm not sure it's the best way to proceed --- we should get some expert input ---  but it seems to work.  Let me know what happens.

To apply the patch:

```
cd $SAGE_ROOT/devel/sage/
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-sage_scilab.patch
hg qpush
sage -b    # This rebuilds the updated files.
```



---

archive/issue_comments_068695.json:
```json
{
    "body": "Theres new (but different errors) :-(\n\nTo confirm them as reproducible, I \n\n* started from a pristine (backup) build,\n\n* did only the \"sage -python setup.py install\" again, \n\n* started the notebook to confirm scilab dropdown option had been added (it was),\n\n* quit the notebook (and sage) and added the new patch (as per your 4 line tip),\n\n* checked scilab opens ok and can do eye(3,3) then I closed it and \n\n* restarted Sage and the notebook and selected the scilab option from the dropdown\n\nI then tested both eye(3,3) and 1+1 (both resulted in the following error)\n\n```\nTraceback (click to the left of this block for traceback)\n...\nRuntimeError: Unable to start scilab\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_4.py\", line 4, in <module>\n    print _support_.syseval(scilab, ur\\u0027\\u0027\\u00271+1\\u0027\\u0027\\u0027, \\u0027/home/ross/.sage/sage_notebook.sagenb/home/admin/66/cells/2\\u0027)\n  File \"\", line 1, in <module>\n    \n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg/sagenb/misc/support.py\", line 470, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/scilab.py\", line 274, in eval\n    s = Expect.eval(self, command, **kwds).replace(\"\\x1b[?1l\\x1b>\",\"\").strip()\n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 983, in eval\n    return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 637, in _eval_line\n    self._start()\n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/scilab.py\", line 261, in _start\n    Expect._start(self)\n  File \"/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 472, in _start\n    raise RuntimeError, \"Unable to start %s\"%self.__name\nRuntimeError: Unable to start scilab\n```",
    "created_at": "2010-02-03T12:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68695",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Theres new (but different errors) :-(

To confirm them as reproducible, I 

* started from a pristine (backup) build,

* did only the "sage -python setup.py install" again, 

* started the notebook to confirm scilab dropdown option had been added (it was),

* quit the notebook (and sage) and added the new patch (as per your 4 line tip),

* checked scilab opens ok and can do eye(3,3) then I closed it and 

* restarted Sage and the notebook and selected the scilab option from the dropdown

I then tested both eye(3,3) and 1+1 (both resulted in the following error)

```
Traceback (click to the left of this block for traceback)
...
RuntimeError: Unable to start scilab

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_4.py", line 4, in <module>
    print _support_.syseval(scilab, ur\u0027\u0027\u00271+1\u0027\u0027\u0027, \u0027/home/ross/.sage/sage_notebook.sagenb/home/admin/66/cells/2\u0027)
  File "", line 1, in <module>
    
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg/sagenb/misc/support.py", line 470, in syseval
    return system.eval(cmd, sage_globals, locals = sage_globals)
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/scilab.py", line 274, in eval
    s = Expect.eval(self, command, **kwds).replace("\x1b[?1l\x1b>","").strip()
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 983, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
    self._start()
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/scilab.py", line 261, in _start
    Expect._start(self)
  File "/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 472, in _start
    raise RuntimeError, "Unable to start %s"%self.__name
RuntimeError: Unable to start scilab
```



---

archive/issue_comments_068696.json:
```json
{
    "body": "What happens if you run `scilab -nogui` at a shell prompt?  It possible that Sage can't find `scilab` in the search `PATH`.\n\nTo get some additional data:\n\n```sh\ncd $SAGE_ROOT\nsage -t -optional devel/sage/sage/interfaces/scilab.py\n```\nWith Scilab 5.2.0 on Linux, I get failures at lines 19, 123, 157, 340, and 505.  With the worksheet system set to `sage` (in the drop-down menu), evaluating `scilab('1 + 1')`, `scilab.eval('1 + 1')`, or\n\n```py\n%scilab\n1 + 1\n```\ngives the expected answer, as does evaluating `1+1` with the worksheet system set to `scilab`.  Evaluating `scilab('1 + 1')` and `scilab.eval('1 + 1')` at the Sage command-line also works.",
    "created_at": "2010-02-04T05:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68696",
    "user": "https://github.com/qed777"
}
```

What happens if you run `scilab -nogui` at a shell prompt?  It possible that Sage can't find `scilab` in the search `PATH`.

To get some additional data:

```sh
cd $SAGE_ROOT
sage -t -optional devel/sage/sage/interfaces/scilab.py
```
With Scilab 5.2.0 on Linux, I get failures at lines 19, 123, 157, 340, and 505.  With the worksheet system set to `sage` (in the drop-down menu), evaluating `scilab('1 + 1')`, `scilab.eval('1 + 1')`, or

```py
%scilab
1 + 1
```
gives the expected answer, as does evaluating `1+1` with the worksheet system set to `scilab`.  Evaluating `scilab('1 + 1')` and `scilab.eval('1 + 1')` at the Sage command-line also works.



---

archive/issue_comments_068697.json:
```json
{
    "body": "I dont think we have a path problem because \"scilab -nogui\" works with the 1+1 example ... other than a complaint about the -nogui switch i.e.\n\n```\nStartup execution:\n  loading initial environment\n !--error 999 \nScilab 'GUI' module disabled in -nogui or -nwni mode.at line     117 of function toolboxes called by :  \ntoolboxes(SCI+'/contrib');\nline     2 of exec file called by :    \n  exec(SCI+'/contrib/loader.sce');\nline   127 of exec file called by :    \nexec('SCI/etc/scilab.start',-1);;\n \n \n-->1+1\n ans  =\n \n    2.  \n```\n(a \"benign\" error/warning couldnt possibly be the problem could it!?)\n\nsage -t threw MANY errors (i.e. more than those listed)\n\nThe scilab('1+1') and eval.scilab('1+1') with scilab selected in notebook, all reported \"cant start scilab\".\n\nThis \"couldnt start scilab\" \n\n```\n%scilab\n1+1\n```\n\nand the 3 lines of code in a cell \n\n```\n-----------------\n#!py\n%scilab\n1+1\n-----------------          \t\n```\n\nreturned\n\n```\nTraceback (click to the left of this block for traceback)\n...\nSyntaxError: invalid syntax\n\nTraceback (most recent call last):    %scilab\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmp7iOaVh/___code___.py\", line 3\n    %scilab\n    ^\nSyntaxError: invalid syntax\n\n```\n\n(Im almost wondering if the error being thrown about -nogui IS the problem)",
    "created_at": "2010-02-04T06:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68697",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

I dont think we have a path problem because "scilab -nogui" works with the 1+1 example ... other than a complaint about the -nogui switch i.e.

```
Startup execution:
  loading initial environment
 !--error 999 
Scilab 'GUI' module disabled in -nogui or -nwni mode.at line     117 of function toolboxes called by :  
toolboxes(SCI+'/contrib');
line     2 of exec file called by :    
  exec(SCI+'/contrib/loader.sce');
line   127 of exec file called by :    
exec('SCI/etc/scilab.start',-1);;
 
 
-->1+1
 ans  =
 
    2.  
```
(a "benign" error/warning couldnt possibly be the problem could it!?)

sage -t threw MANY errors (i.e. more than those listed)

The scilab('1+1') and eval.scilab('1+1') with scilab selected in notebook, all reported "cant start scilab".

This "couldnt start scilab" 

```
%scilab
1+1
```

and the 3 lines of code in a cell 

```
-----------------
#!py
%scilab
1+1
-----------------          	
```

returned

```
Traceback (click to the left of this block for traceback)
...
SyntaxError: invalid syntax

Traceback (most recent call last):    %scilab
  File "", line 1, in <module>
    
  File "/tmp/tmp7iOaVh/___code___.py", line 3
    %scilab
    ^
SyntaxError: invalid syntax

```

(Im almost wondering if the error being thrown about -nogui IS the problem)



---

archive/issue_comments_068698.json:
```json
{
    "body": "Replying to [comment:12 rossk]:\n> (Im almost wondering if the error being thrown about -nogui IS the problem)\n\n\nIt's quite possible.  Which OS and Scilab version are you using?",
    "created_at": "2010-02-04T07:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68698",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:12 rossk]:
> (Im almost wondering if the error being thrown about -nogui IS the problem)


It's quite possible.  Which OS and Scilab version are you using?



---

archive/issue_comments_068699.json:
```json
{
    "body": "```\n$ uname -a \nLinux gauss 2.6.31-18-generic #55-Ubuntu SMP Fri Jan 8 14:55:26 UTC 2010 i686 GNU/Linux\n\n$ scilab -version \nScilab version \"5.1.0.1239693280\" scilab-5.1.1\n```",
    "created_at": "2010-02-04T07:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68699",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

```
$ uname -a 
Linux gauss 2.6.31-18-generic #55-Ubuntu SMP Fri Jan 8 14:55:26 UTC 2010 i686 GNU/Linux

$ scilab -version 
Scilab version "5.1.0.1239693280" scilab-5.1.1
```



---

archive/issue_comments_068700.json:
```json
{
    "body": "I'm not sure what's wrong.  Have you tried reinstalling Scilab or installing the [latest version](http://www.scilab.org/download/index_download.php?page=release)?",
    "created_at": "2010-02-04T08:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68700",
    "user": "https://github.com/qed777"
}
```

I'm not sure what's wrong.  Have you tried reinstalling Scilab or installing the [latest version](http://www.scilab.org/download/index_download.php?page=release)?



---

archive/issue_comments_068701.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> I'm not sure what's wrong.  Have you tried reinstalling Scilab or installing the [latest version](http://www.scilab.org/download/index_download.php?page=release)?\n\n\nIll start again to make sure. Ill get+build the latest sage and scilab\n\nThen Ill do \n\n```\ncd ~/sagenb-0.6/src/sagenb\n~/sage4.3.2rc0/sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-missing_scilab.2.patch \n~/sage4.3.2rc0/sage -hg qpush\n~/sage4.3.2rc0/sage -python setup.py install\n```\nThat should do it, shouldnt it?\n\n(BTW if you can, can you explain or refer me to an explanation of the only line I dont understand i.e. \"sage -python setup.py install\"? How does this command get code from sagenb-0.6/src/sagenb into my sage distribution in ~/sage4.3.2rc0 ?",
    "created_at": "2010-02-04T09:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68701",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Replying to [comment:15 mpatel]:
> I'm not sure what's wrong.  Have you tried reinstalling Scilab or installing the [latest version](http://www.scilab.org/download/index_download.php?page=release)?


Ill start again to make sure. Ill get+build the latest sage and scilab

Then Ill do 

```
cd ~/sagenb-0.6/src/sagenb
~/sage4.3.2rc0/sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7911/trac_7911-missing_scilab.2.patch 
~/sage4.3.2rc0/sage -hg qpush
~/sage4.3.2rc0/sage -python setup.py install
```
That should do it, shouldnt it?

(BTW if you can, can you explain or refer me to an explanation of the only line I dont understand i.e. "sage -python setup.py install"? How does this command get code from sagenb-0.6/src/sagenb into my sage distribution in ~/sage4.3.2rc0 ?



---

archive/issue_comments_068702.json:
```json
{
    "body": "I don't think you need to rebuild / reinstall Sage, if the \"non-Scilab\" parts appear to work as expected.  Moreover, the notebook patch isn't strictly necessary to make the Scilab interface work --- just to list the new system in the drop-down menu.\n\nThe `sage -python setup.py install` command should copy the notebook files in `SAGE_ROOT/local/lib/python/site-packages/sage-*-py2.6.egg`, where * = 0.6 in this case.  `sage -python` (`sage -ipython`) runs the Sage distribution's Python (IPython) intepreter, which searches for packages in `SAGE_ROOT/local/lib/python`, instead of `/usr/lib/python2.x`.\n\nIt may be a false lead, but the 999 error is interesting because Sage runs `scilab -nogui` in the background.  I don't get this error with 64-bit 5.2, 64-bit 5.1.1, or 32-bit 5.1.1 (I didn't try any other versions) on 64-bit Linux, but I've been wrong before, and it could be irrelevant.",
    "created_at": "2010-02-04T12:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68702",
    "user": "https://github.com/qed777"
}
```

I don't think you need to rebuild / reinstall Sage, if the "non-Scilab" parts appear to work as expected.  Moreover, the notebook patch isn't strictly necessary to make the Scilab interface work --- just to list the new system in the drop-down menu.

The `sage -python setup.py install` command should copy the notebook files in `SAGE_ROOT/local/lib/python/site-packages/sage-*-py2.6.egg`, where * = 0.6 in this case.  `sage -python` (`sage -ipython`) runs the Sage distribution's Python (IPython) intepreter, which searches for packages in `SAGE_ROOT/local/lib/python`, instead of `/usr/lib/python2.x`.

It may be a false lead, but the 999 error is interesting because Sage runs `scilab -nogui` in the background.  I don't get this error with 64-bit 5.2, 64-bit 5.1.1, or 32-bit 5.1.1 (I didn't try any other versions) on 64-bit Linux, but I've been wrong before, and it could be irrelevant.



---

archive/issue_comments_068703.json:
```json
{
    "body": "First, thanks for saving me all that work (and the explanation :-)\n\n1) I installed scilab 5.2.0 (and I modified my path to include its binary path) and in running it I tried \"scilab -nogui\" and guess what... (it found scilab on the path and) NO ERROR!\n\n2) Fired up the notebook, selected \"scilab (optional)\" then tried \"1+1\" and got...\n\n...an error :-( \n\nBut something was different, my spider-sense was tingling...  ;-)\n\nI had forgot to export the new path (to scilab) in the terminal I was running Sage in.\n\nI did that and... voila!\n\nThe following worked\n\n```\n# \"scilab (optional)\" selected from dropdown\n1+1\n------\neye(3,3)\n------\n# \"sage\" selected\n%scilab\n1+1\n------\nscilab('eye(3,3)')\n------\n% scilab\n1+1\n------\n# only format that didnt work under \"sage\" dropdown was...\neval.scilab('1+1')\n          \t\n\nTraceback (click to the left of this block for traceback)\n...\nAttributeError: 'builtin_function_or_method' object has no attribute\n'scilab'\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_8.py\", line 4, in <module>\n    open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"ZXZhbC5zY2lsYWIoJzErMScp\"),globals())+\"\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpScHOqE/___code___.py\", line 2, in <module>\n    eval.scilab(\\u00271+1\\u0027)\n  File \"\", line 1, in <module>\n    \nAttributeError: 'builtin_function_or_method' object has no attribute 'scilab'\n```\n\nNow pls let me know what other checks I need to do and how to do some doc tests (all doc test might wait till I get a sage account soon)",
    "created_at": "2010-02-04T15:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68703",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

First, thanks for saving me all that work (and the explanation :-)

1) I installed scilab 5.2.0 (and I modified my path to include its binary path) and in running it I tried "scilab -nogui" and guess what... (it found scilab on the path and) NO ERROR!

2) Fired up the notebook, selected "scilab (optional)" then tried "1+1" and got...

...an error :-( 

But something was different, my spider-sense was tingling...  ;-)

I had forgot to export the new path (to scilab) in the terminal I was running Sage in.

I did that and... voila!

The following worked

```
# "scilab (optional)" selected from dropdown
1+1
------
eye(3,3)
------
# "sage" selected
%scilab
1+1
------
scilab('eye(3,3)')
------
% scilab
1+1
------
# only format that didnt work under "sage" dropdown was...
eval.scilab('1+1')
          	

Traceback (click to the left of this block for traceback)
...
AttributeError: 'builtin_function_or_method' object has no attribute
'scilab'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_8.py", line 4, in <module>
    open("___code___.py","w").write("# -*- coding: utf-8 -*-\n" + _support_.preparse_worksheet_cell(base64.b64decode("ZXZhbC5zY2lsYWIoJzErMScp"),globals())+"\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpScHOqE/___code___.py", line 2, in <module>
    eval.scilab(\u00271+1\u0027)
  File "", line 1, in <module>
    
AttributeError: 'builtin_function_or_method' object has no attribute 'scilab'
```

Now pls let me know what other checks I need to do and how to do some doc tests (all doc test might wait till I get a sage account soon)



---

archive/issue_comments_068704.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-05T01:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68704",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068705.json:
```json
{
    "body": "That's great!  (`eval.scilab` should be `scilab.eval`.)\n\nWe should fix all doctests, i.e., ensure that\n\n```sh\ncd $SAGE_ROOT\nsage -t -optional devel/sage/sage/interfaces/scilab.py\n```\nyields no failures.  This will require improving the sage repository patch above.  I'm changing this ticket to \"needs work,\" for this reason.\n\nThe [developer's guide](http://www.sagemath.org/doc/developer/index.html) (4.3.2.rc0 includes #8147), the [wiki page on Mercurial queues](http://wiki.sagemath.org/MercurialQueues?highlight=%28queues%29), and [sage-devel](http://groups.google.com/group/sage-devel) might be useful.  Don't hesitate to ask, if you have questions.",
    "created_at": "2010-02-05T01:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68705",
    "user": "https://github.com/qed777"
}
```

That's great!  (`eval.scilab` should be `scilab.eval`.)

We should fix all doctests, i.e., ensure that

```sh
cd $SAGE_ROOT
sage -t -optional devel/sage/sage/interfaces/scilab.py
```
yields no failures.  This will require improving the sage repository patch above.  I'm changing this ticket to "needs work," for this reason.

The [developer's guide](http://www.sagemath.org/doc/developer/index.html) (4.3.2.rc0 includes #8147), the [wiki page on Mercurial queues](http://wiki.sagemath.org/MercurialQueues?highlight=%28queues%29), and [sage-devel](http://groups.google.com/group/sage-devel) might be useful.  Don't hesitate to ask, if you have questions.



---

archive/issue_comments_068706.json:
```json
{
    "body": "Actually, I think it's better to use this ticket just for the notebook drop-down menu patch and to create a new ticket, under the interfaces component, for the doctests.",
    "created_at": "2010-02-05T03:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68706",
    "user": "https://github.com/qed777"
}
```

Actually, I think it's better to use this ticket just for the notebook drop-down menu patch and to create a new ticket, under the interfaces component, for the doctests.



---

archive/issue_comments_068707.json:
```json
{
    "body": "Will do that suggested reading and confirm the doctests pass once you create that new ticket. Set me to reviewer on that ticket if you like (and I expect trac will send me an email to notify me it has been created?)",
    "created_at": "2010-02-05T13:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68707",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Will do that suggested reading and confirm the doctests pass once you create that new ticket. Set me to reviewer on that ticket if you like (and I expect trac will send me an email to notify me it has been created?)



---

archive/issue_comments_068708.json:
```json
{
    "body": "Also fix doctests.  Replaces previous **sage** repository patch.",
    "created_at": "2010-02-15T22:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68708",
    "user": "https://github.com/qed777"
}
```

Also fix doctests.  Replaces previous **sage** repository patch.



---

archive/issue_comments_068709.json:
```json
{
    "body": "Attachment [trac_7911-sage_scilab.2.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-sage_scilab.2.patch) by @qed777 created at 2010-02-15 22:29:39\n\nV2 of the sage repository patch should fix the failed doctests.  (I decided not to create a new ticket.)  It seems that parts of the Sage library have changed significantly since we last updated the Scilab interface.  It would be great to get feedback from an interface expert!\n\nI'm changing this ticket's component to 'interfaces.'",
    "created_at": "2010-02-15T22:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68709",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7911-sage_scilab.2.patch](tarball://root/attachments/some-uuid/ticket7911/trac_7911-sage_scilab.2.patch) by @qed777 created at 2010-02-15 22:29:39

V2 of the sage repository patch should fix the failed doctests.  (I decided not to create a new ticket.)  It seems that parts of the Sage library have changed significantly since we last updated the Scilab interface.  It would be great to get feedback from an interface expert!

I'm changing this ticket's component to 'interfaces.'



---

archive/issue_comments_068710.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-15T22:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68710",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068711.json:
```json
{
    "body": "Changing component from notebook to interfaces.",
    "created_at": "2010-02-15T22:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68711",
    "user": "https://github.com/qed777"
}
```

Changing component from notebook to interfaces.



---

archive/issue_comments_068712.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-18T01:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68712",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068713.json:
```json
{
    "body": "Tested this under sage-4.3.2 and 0.7.4 of the notebook. Requires scilab-5.2 or higher! \n\n\nNotebook and scilab interface doctests pass.\n\n\nMany Scilab statements work under each of the following options:\n\n\n(a) the \"scilab (optional)\" dropdown, as well as with\n\n \n(b) \"%scilab\" directive on first line of a notebook cell and with\n\n \n(c) scilab('<scilab-statement>') and\n\n \n(d) scilab.eval('<scilab-statement>')\n\n\nA couple of issues are likely to result in new tickets.\n\n \n\nISSUE (1)\n\n\nThe use of the scilab built-in constants: %e, %i, %pi etc cause errors\nwhen they are the first expression in a statement in options (a)\nand (b) above i.e.  %e + 1, %pi /4 crash under (a) and (b) - but are ok when using options (c)\nand  (d)\n\n\n(A workaround  until  a fix  is  created  is avoiding  these\nconstants at the beginning of a line i.e. reordering where possible or\nprefixing with 0 i.e.  instead of \"%e + 1\", use \"1 + %e\"  or \"0 + %e + 1\")\n\n\nISSUE (2)\n\n\nThe  scilab  interface doesn't look like it's documented.  One  based  on  the  matlab\ndocumentation [1] should do the job (and given I suggested it maybe that should fall to me :)\n\n\n[1] http://www.sagemath.org/doc/reference/sage/interfaces/matlab.html\n\nThese 2 issues  are new tickets whereas  this ticket solves  its stated goals (hence the positive review)",
    "created_at": "2010-02-18T01:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68713",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Tested this under sage-4.3.2 and 0.7.4 of the notebook. Requires scilab-5.2 or higher! 


Notebook and scilab interface doctests pass.


Many Scilab statements work under each of the following options:


(a) the "scilab (optional)" dropdown, as well as with

 
(b) "%scilab" directive on first line of a notebook cell and with

 
(c) scilab('<scilab-statement>') and

 
(d) scilab.eval('<scilab-statement>')


A couple of issues are likely to result in new tickets.

 

ISSUE (1)


The use of the scilab built-in constants: %e, %i, %pi etc cause errors
when they are the first expression in a statement in options (a)
and (b) above i.e.  %e + 1, %pi /4 crash under (a) and (b) - but are ok when using options (c)
and  (d)


(A workaround  until  a fix  is  created  is avoiding  these
constants at the beginning of a line i.e. reordering where possible or
prefixing with 0 i.e.  instead of "%e + 1", use "1 + %e"  or "0 + %e + 1")


ISSUE (2)


The  scilab  interface doesn't look like it's documented.  One  based  on  the  matlab
documentation [1] should do the job (and given I suggested it maybe that should fall to me :)


[1] http://www.sagemath.org/doc/reference/sage/interfaces/matlab.html

These 2 issues  are new tickets whereas  this ticket solves  its stated goals (hence the positive review)



---

archive/issue_comments_068714.json:
```json
{
    "body": "#7418 may help with the first problem.",
    "created_at": "2010-02-18T01:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68714",
    "user": "https://github.com/qed777"
}
```

#7418 may help with the first problem.



---

archive/issue_comments_068715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T22:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_018935.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-18T22:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7911#event-18935"
}
```



---

archive/issue_comments_068716.json:
```json
{
    "body": "Merged [trac_7911-sage_scilab.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7911/trac_7911-sage_scilab.2.patch) in the Sage library.",
    "created_at": "2010-02-18T22:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_7911-sage_scilab.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7911/trac_7911-sage_scilab.2.patch) in the Sage library.



---

archive/issue_comments_068717.json:
```json
{
    "body": "I'm merging [attachment:trac_7911-missing_scilab.patch] into SageNB 0.7.5.2.  See #8435.",
    "created_at": "2010-03-04T22:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7911#issuecomment-68717",
    "user": "https://github.com/qed777"
}
```

I'm merging [attachment:trac_7911-missing_scilab.patch] into SageNB 0.7.5.2.  See #8435.
