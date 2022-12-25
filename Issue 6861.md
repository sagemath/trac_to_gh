# Issue 6861: allow users to test Sage script using system-wide Sage installation

archive/issues_006861.json:
```json
{
    "body": "Assignee: tbd\n\nAt least in Sage 4.1.1, a regular user cannot run tests on their own Sage scripts using a system-wide installation of Sage. Doing so would result in a permission error:\n\n```\n[mvngu@mod mvngu]$ cat demo.sage \nprint 2\n[mvngu@mod mvngu]$ sage -t demo.sage \nTraceback (most recent call last):\n  File \"/usr/local/sage/local/bin/sage-test\", line 49, in <module>\n    os.makedirs(TMP)\n  File \"/usr/local/sage/local/lib/python/os.py\", line 157, in makedirs\n    mkdir(name, mode)\nOSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'\n```\n\nThat is due to the testing script writing temporary data to a temporary directory under the system-wide Sage installation. A work around is to have one's own local installation of Sage under one's home directory. But it would be nice if the test script would write temporary data to the user's `DOT_SAGE` directory, i.e. `$HOME/.sage`. This problem was reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/af6d95445f76cbe9) thread.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6861\n\n",
    "created_at": "2009-09-02T04:47:07Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "allow users to test Sage script using system-wide Sage installation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

At least in Sage 4.1.1, a regular user cannot run tests on their own Sage scripts using a system-wide installation of Sage. Doing so would result in a permission error:

```
[mvngu@mod mvngu]$ cat demo.sage 
print 2
[mvngu@mod mvngu]$ sage -t demo.sage 
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/sage-test", line 49, in <module>
    os.makedirs(TMP)
  File "/usr/local/sage/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'
```

That is due to the testing script writing temporary data to a temporary directory under the system-wide Sage installation. A work around is to have one's own local installation of Sage under one's home directory. But it would be nice if the test script would write temporary data to the user's `DOT_SAGE` directory, i.e. `$HOME/.sage`. This problem was reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/af6d95445f76cbe9) thread.

Issue created by migration from https://trac.sagemath.org/ticket/6861





---

archive/issue_comments_056485.json:
```json
{
    "body": "Attachment [trac_6861-sage-test-in-dotsage.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861-sage-test-in-dotsage.patch) by @jasongrout created at 2009-09-02 21:16:42",
    "created_at": "2009-09-02T21:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56485",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_6861-sage-test-in-dotsage.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861-sage-test-in-dotsage.patch) by @jasongrout created at 2009-09-02 21:16:42



---

archive/issue_comments_056486.json:
```json
{
    "body": "Attachment [trac_6861-sage-test-in-dotsage.2.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861-sage-test-in-dotsage.2.patch) by @jasongrout created at 2009-09-02 21:17:18\n\nThe two files above are identical.  One can be deleted.",
    "created_at": "2009-09-02T21:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56486",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_6861-sage-test-in-dotsage.2.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861-sage-test-in-dotsage.2.patch) by @jasongrout created at 2009-09-02 21:17:18

The two files above are identical.  One can be deleted.



---

archive/issue_comments_056487.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n\nIn addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`).",
    "created_at": "2009-09-03T07:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56487",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:1 jason]:

In addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`).



---

archive/issue_comments_056488.json:
```json
{
    "body": "Replying to [comment:2 fwclarke]:\n> Replying to [comment:1 jason]:\n> \n> In addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`). \n\n\nYou sound like you know what needs to be done.  Please, please post a patch.",
    "created_at": "2009-09-03T07:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56488",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 fwclarke]:
> Replying to [comment:1 jason]:
> 
> In addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`). 


You sound like you know what needs to be done.  Please, please post a patch.



---

archive/issue_comments_056489.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> You sound like you know what needs to be done.  Please, please post a patch.\n\nWill do, but not immediately; there are a few things I don't quite understand, and I'm off to the day-job now.",
    "created_at": "2009-09-03T07:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56489",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:3 jason]:
> You sound like you know what needs to be done.  Please, please post a patch.

Will do, but not immediately; there are a few things I don't quite understand, and I'm off to the day-job now.



---

archive/issue_comments_056490.json:
```json
{
    "body": "Replying to [comment:4 fwclarke]:\n \n> There are a few things I don't quite understand ...\n\nIt seems to me that if (because of the changed definition of `SAGE_TESTDIR`) the directory `~/.sage/tmp` is to be used for testing system files, then logically it should also be used for testing users' own files.  This requires a few more changes.    \n\nIt also seems worthwhile to active the function `delete_tmpfiles` in `sage-doctest`; at present this function does nothing.  The obvious things is for it to get called if the doctest succeeds without any failures, but at present the method of counting the number of failures is defective.\n\nI have implemented these ideas and am testing the code.  A patch will follow soon.",
    "created_at": "2009-09-05T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56490",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:4 fwclarke]:
 
> There are a few things I don't quite understand ...

It seems to me that if (because of the changed definition of `SAGE_TESTDIR`) the directory `~/.sage/tmp` is to be used for testing system files, then logically it should also be used for testing users' own files.  This requires a few more changes.    

It also seems worthwhile to active the function `delete_tmpfiles` in `sage-doctest`; at present this function does nothing.  The obvious things is for it to get called if the doctest succeeds without any failures, but at present the method of counting the number of failures is defective.

I have implemented these ideas and am testing the code.  A patch will follow soon.



---

archive/issue_comments_056491.json:
```json
{
    "body": "The new patch, which incorporates the change in the earlier patch, also includes the changes made in the patch at #6668.",
    "created_at": "2009-09-05T22:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56491",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The new patch, which incorporates the change in the earlier patch, also includes the changes made in the patch at #6668.



---

archive/issue_comments_056492.json:
```json
{
    "body": "replaces earlier patches",
    "created_at": "2009-09-05T22:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56492",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

replaces earlier patches



---

archive/issue_comments_056493.json:
```json
{
    "body": "Attachment [trac_6861_new.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861_new.patch) by fwclarke created at 2009-09-10 19:11:06\n\nI have added an extra patch (to be applied after trac_6861_new.patch) which deals with a problem in testing files specified by their full path name, as [discussed](http://groups.google.com/group/sage-devel/browse_thread/thread/6295a62c30f5edca) in sage-devel.",
    "created_at": "2009-09-10T19:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56493",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_6861_new.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861_new.patch) by fwclarke created at 2009-09-10 19:11:06

I have added an extra patch (to be applied after trac_6861_new.patch) which deals with a problem in testing files specified by their full path name, as [discussed](http://groups.google.com/group/sage-devel/browse_thread/thread/6295a62c30f5edca) in sage-devel.



---

archive/issue_comments_056494.json:
```json
{
    "body": "Attachment [trac_6861_extra.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861_extra.patch) by fwclarke created at 2009-09-10 19:12:13\n\napply after trac_6861_new.patch",
    "created_at": "2009-09-10T19:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56494",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_6861_extra.patch](tarball://root/attachments/some-uuid/ticket6861/trac_6861_extra.patch) by fwclarke created at 2009-09-10 19:12:13

apply after trac_6861_new.patch



---

archive/issue_comments_056495.json:
```json
{
    "body": "Patches work perfectly, and I've run several dozen doctests without any problems. Temporary files are deleted as promised. Nice job guys. Positive review.",
    "created_at": "2009-09-23T12:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56495",
    "user": "https://github.com/TimDumol"
}
```

Patches work perfectly, and I've run several dozen doctests without any problems. Temporary files are deleted as promised. Nice job guys. Positive review.



---

archive/issue_comments_056496.json:
```json
{
    "body": "Merged in the script repository.",
    "created_at": "2009-09-24T11:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in the script repository.



---

archive/issue_comments_056497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T11:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007094.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T11:02:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6861#event-7094"
}
```



---

archive/issue_comments_056498.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.



---

archive/issue_comments_056499.json:
```json
{
    "body": "See #7079 for a case where the current ticket breaks parallel doctesting.",
    "created_at": "2009-09-30T07:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6861#issuecomment-56499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #7079 for a case where the current ticket breaks parallel doctesting.
