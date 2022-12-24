# Issue 4523: browser cache not cleared when restarting the worksheet

archive/issues_004523.json:
```json
{
    "body": "Assignee: boothby\n\nFrom an email on sage-devel:\n\nThe problem is not in your code.  I think the problem is in your browser caching the image.  When Sage creates the image, it gives it the same name.  Your browser thinks that it is the same image as before, so it doesn't bother to update the image.  If you refresh the page after you first see the wrong image, you'll see the right image appear.\n\nYou'll see the same problem if you have two cells:\n\n`f(x) = x^2`\n\nand \n\n`plot(f, (x, 1, 2))`\n\n\n1. Evaluate the two cells, so you get a plot\n2. Restart the worksheet\n3. Change the function\n4. Evaluate the two cells again.  Notice you get the same plot.\n5. Hit Refresh in the browser.  Now the plot updates.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4523\n\n",
    "created_at": "2008-11-14T16:28:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "browser cache not cleared when restarting the worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4523",
    "user": "jason"
}
```
Assignee: boothby

From an email on sage-devel:

The problem is not in your code.  I think the problem is in your browser caching the image.  When Sage creates the image, it gives it the same name.  Your browser thinks that it is the same image as before, so it doesn't bother to update the image.  If you refresh the page after you first see the wrong image, you'll see the right image appear.

You'll see the same problem if you have two cells:

`f(x) = x^2`

and 

`plot(f, (x, 1, 2))`


1. Evaluate the two cells, so you get a plot
2. Restart the worksheet
3. Change the function
4. Evaluate the two cells again.  Notice you get the same plot.
5. Hit Refresh in the browser.  Now the plot updates.


Issue created by migration from https://trac.sagemath.org/ticket/4523





---

archive/issue_comments_033570.json:
```json
{
    "body": "This is fixed by adding a Last-Modified header to the response.",
    "created_at": "2009-01-19T08:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4523#issuecomment-33570",
    "user": "mhansen"
}
```

This is fixed by adding a Last-Modified header to the response.



---

archive/issue_comments_033571.json:
```json
{
    "body": "Attachment [trac_4523.patch](tarball://root/attachments/some-uuid/ticket4523/trac_4523.patch) by ddrake created at 2009-01-19 23:49:22\n\nFor anyone who doesn't want to read the patch, the new code adds the time (in seconds since the epoch) to the URL for each image, so the browser fetches image.png?1232408438 (or whatever the time is), and since that URL will change if one evaluates the cell at least one second later, the browser should pick up the new image.\n\nI tested this with Firefox (Ubuntu, XP), IE7, IE8 beta, and Opera (Ubuntu and XP) and can no longer reproduce the bug. Positive review.\n\n(BTW, at 23:31:30 UTC on February 13, 2009, the Unix time will be 1234567890.)",
    "created_at": "2009-01-19T23:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4523#issuecomment-33571",
    "user": "ddrake"
}
```

Attachment [trac_4523.patch](tarball://root/attachments/some-uuid/ticket4523/trac_4523.patch) by ddrake created at 2009-01-19 23:49:22

For anyone who doesn't want to read the patch, the new code adds the time (in seconds since the epoch) to the URL for each image, so the browser fetches image.png?1232408438 (or whatever the time is), and since that URL will change if one evaluates the cell at least one second later, the browser should pick up the new image.

I tested this with Firefox (Ubuntu, XP), IE7, IE8 beta, and Opera (Ubuntu and XP) and can no longer reproduce the bug. Positive review.

(BTW, at 23:31:30 UTC on February 13, 2009, the Unix time will be 1234567890.)



---

archive/issue_comments_033572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4523#issuecomment-33572",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033573.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4523#issuecomment-33573",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
