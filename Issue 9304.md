# Issue 9304: trac #8218 (finite_rings) broke all my pickles!

archive/issues_009304.json:
```json
{
    "body": "Assignee: @williamstein\n\nI have a lot of pickles here (in the data directory):\n\nhttp://sage.math.washington.edu/home/wstein/db/modsym/\n\nAll the ones without \"aplist\" in their name were broken by trac #8218 which rearranged code without any backwards compatibility imports.    This should have never happened. Sigh.\n\nAnyway, my pickles are fixed by just adding back one file. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9304\n\n",
    "created_at": "2010-06-22T06:33:00Z",
    "labels": [
        "component: pickling",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "trac #8218 (finite_rings) broke all my pickles!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9304",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

I have a lot of pickles here (in the data directory):

http://sage.math.washington.edu/home/wstein/db/modsym/

All the ones without "aplist" in their name were broken by trac #8218 which rearranged code without any backwards compatibility imports.    This should have never happened. Sigh.

Anyway, my pickles are fixed by just adding back one file. 

Issue created by migration from https://trac.sagemath.org/ticket/9304





---

archive/issue_comments_087490.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T06:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87490",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087491.json:
```json
{
    "body": "Attachment [trac_9304-alternative.patch](tarball://root/attachments/some-uuid/ticket9304/trac_9304-alternative.patch) by @loefflerd created at 2010-06-28 18:25:08",
    "created_at": "2010-06-28T18:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87491",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9304-alternative.patch](tarball://root/attachments/some-uuid/ticket9304/trac_9304-alternative.patch) by @loefflerd created at 2010-06-28 18:25:08



---

archive/issue_comments_087492.json:
```json
{
    "body": "This is arguably my fault, since I reviewed #8218. Anyway, we have a much nicer way of fixing unpickling problems now, without all of these annoying file stubs lying around. \n\n```\nsage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')\nAttempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj\nLoading: [..................................................]\n((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)\n```\n\n\nYou know better than I do whether that's the right output, but at least it isn't raising an error.",
    "created_at": "2010-06-28T18:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87492",
    "user": "https://github.com/loefflerd"
}
```

This is arguably my fault, since I reviewed #8218. Anyway, we have a much nicer way of fixing unpickling problems now, without all of these annoying file stubs lying around. 

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)
```


You know better than I do whether that's the right output, but at least it isn't raising an error.



---

archive/issue_comments_087493.json:
```json
{
    "body": "What would be a good way to test this for review?",
    "created_at": "2010-10-12T11:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87493",
    "user": "https://github.com/JohnCremona"
}
```

What would be a good way to test this for review?



---

archive/issue_comments_087494.json:
```json
{
    "body": "Hi John,\n\nTry running the command \n\n```\nsage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')\n```\n\n\nwith and without the patch (either one!) applied. Without the patch you'll get an error similar to the one Salman Baig reports on sage-devel ([here](http://groups.google.co.uk/group/sage-devel/browse_thread/thread/f208f9d1548564ee/d989b029608fa6ee)). With the patch it should load fine.",
    "created_at": "2010-10-12T12:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87494",
    "user": "https://github.com/loefflerd"
}
```

Hi John,

Try running the command 

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
```


with and without the patch (either one!) applied. Without the patch you'll get an error similar to the one Salman Baig reports on sage-devel ([here](http://groups.google.co.uk/group/sage-devel/browse_thread/thread/f208f9d1548564ee/d989b029608fa6ee)). With the patch it should load fine.



---

archive/issue_comments_087495.json:
```json
{
    "body": "With either patch the load is OK but does give a deprecation warning:\n\n```\nsage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')\nAttempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj\nLoading: [..................................................]\n/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n  exec code_obj in self.user_global_ns, self.user_ns\n((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)\n```\n\nwhich is exactly the same warning as I get without the patch.  Am I doing something stupid here?\n\nOf the two patches, I prefer the second (\"alternative\") since it implements a more general method, and does not need to create that little dummy (almost) file.",
    "created_at": "2010-10-12T13:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87495",
    "user": "https://github.com/JohnCremona"
}
```

With either patch the load is OK but does give a deprecation warning:

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
  exec code_obj in self.user_global_ns, self.user_ns
((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)
```

which is exactly the same warning as I get without the patch.  Am I doing something stupid here?

Of the two patches, I prefer the second ("alternative") since it implements a more general method, and does not need to create that little dummy (almost) file.



---

archive/issue_comments_087496.json:
```json
{
    "body": "Changing keywords from \"\" to \"pickling\".",
    "created_at": "2010-10-12T13:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87496",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "pickling".



---

archive/issue_comments_087497.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-10-12T13:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87497",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_087498.json:
```json
{
    "body": "That's weird: it really shouldn't work without the patch! If I run that command in a clean 4.6.alpha3 build, I get the same DeprecationWarning but it's followed by `ImportError: No module named integer_mod_ring`. Did you try running it *before* installing either patch? \n\nIf you install William's patch, build, and then qpop it and build again, the file it re-creates will still be lurking in your build directory. If that's the case try switching to a clean branch to see the `ImportError`.",
    "created_at": "2010-10-12T13:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87498",
    "user": "https://github.com/loefflerd"
}
```

That's weird: it really shouldn't work without the patch! If I run that command in a clean 4.6.alpha3 build, I get the same DeprecationWarning but it's followed by `ImportError: No module named integer_mod_ring`. Did you try running it *before* installing either patch? 

If you install William's patch, build, and then qpop it and build again, the file it re-creates will still be lurking in your build directory. If that's the case try switching to a clean branch to see the `ImportError`.



---

archive/issue_comments_087499.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-12T13:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87499",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_087500.json:
```json
{
    "body": "I think you are right.  I tried it before applying patches, saw that something was not right but did not copy the output.  When I tried again after removing the patches (using hg qpop and sage -br) it still works!\n\nBut I just tried again on another machine, still 4.6.alpha3, and with no patches the load command gives\n\n```\nsage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')\nAttempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj\nLoading: [..................................................]\n/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n  exec code_obj in self.user_global_ns, self.user_ns\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/home/jec/sage-4.6.alpha3/devel/sage-main/<ipython console> in <module>()\n\n/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7486)()\n\n/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9052)()\n\n/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.unpickle_global (sage/structure/sage_object.c:8659)()\n\nImportError: No module named integer_mod_ring\n```\n\n\nIt's a mystery that popping the patches left a setup in which the load works;  and that left open the possibility that the only reason why the second patch worked was that the effect of the first patch was still around (!) so on the second machine I applied the second patch without previously applying the first, and that still worked.\n\nMoreover, then popping the second patch put the system back properly (the load again fails).\n\nSo I am giving the *second* patch a positive review.",
    "created_at": "2010-10-12T13:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87500",
    "user": "https://github.com/JohnCremona"
}
```

I think you are right.  I tried it before applying patches, saw that something was not right but did not copy the output.  When I tried again after removing the patches (using hg qpop and sage -br) it still works!

But I just tried again on another machine, still 4.6.alpha3, and with no patches the load command gives

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
  exec code_obj in self.user_global_ns, self.user_ns
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/jec/sage-4.6.alpha3/devel/sage-main/<ipython console> in <module>()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7486)()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9052)()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.unpickle_global (sage/structure/sage_object.c:8659)()

ImportError: No module named integer_mod_ring
```


It's a mystery that popping the patches left a setup in which the load works;  and that left open the possibility that the only reason why the second patch worked was that the effect of the first patch was still around (!) so on the second machine I applied the second patch without previously applying the first, and that still worked.

Moreover, then popping the second patch put the system back properly (the load again fails).

So I am giving the *second* patch a positive review.



---

archive/issue_comments_087501.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-12T13:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87501",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87502",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009462.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2010-11-01T10:06:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9304#event-9462"
}
```



---

archive/issue_comments_087503.json:
```json
{
    "body": "Merged alternative patch",
    "created_at": "2010-11-01T10:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9304#issuecomment-87503",
    "user": "https://github.com/jdemeyer"
}
```

Merged alternative patch
