# Issue 2565: [with patch, positive review logging is extremely broken

archive/issues_002565.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: log, logging, html, dvi\n\nThe logging facilities in misc/log.py are extremely broken.\n\nThe DVI logger produces a symlink to `$SAGE_ROOT/devel/doc/commontex/macros.tex`. There's no devel/doc directory; there's no doc/commontex directory anywhere in the Sage tree, and there's no file macros.tex anywhere in the Sage tree!\n\nThe optional directory that can be specified in the constructor does not actually accept a directory name. If you try `L.('/tmp')` it will fail, because it tries to create a directory such as `/tmp-2008-blah`, which fails because I'm running Sage as a user and can't create directories in the root directory.\n\nThe HTML logger works a bit better, but when starting it, it does not find the `xdg-open` command, even though that is installed on my system.\n\nThe view() command should allow the user to specify a viewer; it's silly that the only way to tell Sage which viewer to use is with an environment variable.\n\nIt would also be nice if there was a text logger available in log.py. I know there's the IPython logging system, but it would be nice if those text-based logging capabilities were available from log.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2565\n\n",
    "closed_at": "2008-03-27T07:50:46Z",
    "created_at": "2008-03-17T04:45:21Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review logging is extremely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2565",
    "user": "https://github.com/dandrake"
}
```
Assignee: cwitty

Keywords: log, logging, html, dvi

The logging facilities in misc/log.py are extremely broken.

The DVI logger produces a symlink to `$SAGE_ROOT/devel/doc/commontex/macros.tex`. There's no devel/doc directory; there's no doc/commontex directory anywhere in the Sage tree, and there's no file macros.tex anywhere in the Sage tree!

The optional directory that can be specified in the constructor does not actually accept a directory name. If you try `L.('/tmp')` it will fail, because it tries to create a directory such as `/tmp-2008-blah`, which fails because I'm running Sage as a user and can't create directories in the root directory.

The HTML logger works a bit better, but when starting it, it does not find the `xdg-open` command, even though that is installed on my system.

The view() command should allow the user to specify a viewer; it's silly that the only way to tell Sage which viewer to use is with an environment variable.

It would also be nice if there was a text logger available in log.py. I know there's the IPython logging system, but it would be nice if those text-based logging capabilities were available from log.py.

Issue created by migration from https://trac.sagemath.org/ticket/2565





---

archive/issue_events_005992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-17T04:51:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2565#event-5992"
}
```



---

archive/issue_comments_017446.json:
```json
{
    "body": "The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) since it depends on a bunch of files that aren't shipped with Sage, so it cannot possibly work. The patch also fixes DVI viewing by removing the symlink to macros.tex; a simple example of the output compiled without any extra files, so removing that from the generated TeX file seems okay for now.\n\nI am also seeing a problem where the output and input are off by 1: the output from command #n is shown in the generated file after comment #n+1.",
    "created_at": "2008-03-17T11:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17446",
    "user": "https://github.com/dandrake"
}
```

The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) since it depends on a bunch of files that aren't shipped with Sage, so it cannot possibly work. The patch also fixes DVI viewing by removing the symlink to macros.tex; a simple example of the output compiled without any extra files, so removing that from the generated TeX file seems okay for now.

I am also seeing a problem where the output and input are off by 1: the output from command #n is shown in the generated file after comment #n+1.



---

archive/issue_comments_017447.json:
```json
{
    "body": "Hi Dan,\n\nplease attach mercurial patches so that you can get credited for them automatically in the repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-17T12:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Dan,

please attach mercurial patches so that you can get credited for them automatically in the repo.

Cheers,

Michael



---

archive/issue_events_005993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-17T12:06:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2565#event-5993"
}
```



---

archive/issue_events_005994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-17T12:06:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2565#event-5994"
}
```



---

archive/issue_comments_017448.json:
```json
{
    "body": "Mercurial patch attached. I just learned about patch queues and did a 'qdiff' instead of 'export qtip'. :)\n\nThe patch, btw, is against 2.10.3.",
    "created_at": "2008-03-18T00:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17448",
    "user": "https://github.com/dandrake"
}
```

Mercurial patch attached. I just learned about patch queues and did a 'qdiff' instead of 'export qtip'. :)

The patch, btw, is against 2.10.3.



---

archive/issue_comments_017449.json:
```json
{
    "body": "The attached patch fixes all issues mentioned in the report, and adds a text logger.\n\nThere is an off-by-one error in the IPython input/output history; I don't know if that is a genuine bug, but I had to account for it, and it was tricky.",
    "created_at": "2008-03-19T05:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17449",
    "user": "https://github.com/dandrake"
}
```

The attached patch fixes all issues mentioned in the report, and adds a text logger.

There is an off-by-one error in the IPython input/output history; I don't know if that is a genuine bug, but I had to account for it, and it was tricky.



---

archive/issue_comments_017450.json:
```json
{
    "body": "Replying to [comment:2 ddrake]:\n> The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) w.\n\n\nHi Dan, thanks for seeing this. Could you completely remove this class (log_mathml)? It's not that useful anymore.\n\nThe patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved\n\n```\nsage: log_text()\nLogging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt\n```",
    "created_at": "2008-03-27T04:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17450",
    "user": "https://github.com/dfdeshom"
}
```

Replying to [comment:2 ddrake]:
> The `log.patch.1` patch fixes the directory problems and the xdg-open problem. It also removes the MathML logger (by commenting it out and removing from all.py) w.


Hi Dan, thanks for seeing this. Could you completely remove this class (log_mathml)? It's not that useful anymore.

The patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved

```
sage: log_text()
Logging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt
```



---

archive/issue_comments_017451.json:
```json
{
    "body": "Replying to [comment:7 dfdeshom]:\n> The patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved\n\n{{{\nsage: log_text()\nLogging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt\n}}}\n> \n\n\nI've added the message, removed the MathML logger, and will update the patch momentarily. As for the paths, it's not necessary to use relative paths: you can do\n\n```\nsage: log_text('/tmp')\n```\nand you get a directory in the `/tmp` directory. If you don't begin the path with a slash, it gets put into your home directory: doing `log_text('foo')` logs into a directory like `/home/drake/foo/log-2008-03-27-151949`.",
    "created_at": "2008-03-27T06:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17451",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:7 dfdeshom]:
> The patch looks good and the logger works! I have 2 requests: it would be nice if the docs specified that the log directory has to be a *relative* path. Also: when you instantiate the logger, you could return a message saying where the log file is being saved

{{{
sage: log_text()
Logging all commands to ~/custom/sage/log/log-2008-03-26-202848/logfile.txt
}}}
> 


I've added the message, removed the MathML logger, and will update the patch momentarily. As for the paths, it's not necessary to use relative paths: you can do

```
sage: log_text('/tmp')
```
and you get a directory in the `/tmp` directory. If you don't begin the path with a slash, it gets put into your home directory: doing `log_text('foo')` logs into a directory like `/home/drake/foo/log-2008-03-27-151949`.



---

archive/issue_comments_017452.json:
```json
{
    "body": "Attachment [log.patch.1](tarball://root/attachments/some-uuid/ticket2565/log.patch.1) by @dandrake created at 2008-03-27 06:40:37",
    "created_at": "2008-03-27T06:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17452",
    "user": "https://github.com/dandrake"
}
```

Attachment [log.patch.1](tarball://root/attachments/some-uuid/ticket2565/log.patch.1) by @dandrake created at 2008-03-27 06:40:37



---

archive/issue_comments_017453.json:
```json
{
    "body": "Both issues have been addressed:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |\n| Type notebook() for the GUI, and license() for information.        |\nsage: log_text()\nNow logging to /home/mabshoff/.sage/log/log-2008-03-27-004430/sagelog.txt\nText Logger\nsage:\nExiting SAGE (CPU time 0m0.01s, Wall time 0m7.41s).\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |\n| Type notebook() for the GUI, and license() for information.        |\nsage: log_text(\"/tmp\")\nNow logging to /tmp/log-2008-03-27-004454/sagelog.txt\nText Logger\nsage:\nExiting SAGE (CPU time 0m0.02s, Wall time 0m8.70s).\n```\nSo: positive review!",
    "created_at": "2008-03-27T07:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Both issues have been addressed:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |
| Type notebook() for the GUI, and license() for information.        |
sage: log_text()
Now logging to /home/mabshoff/.sage/log/log-2008-03-27-004430/sagelog.txt
Text Logger
sage:
Exiting SAGE (CPU time 0m0.01s, Wall time 0m7.41s).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11.alpha1, Release Date: 2008-03-22                 |
| Type notebook() for the GUI, and license() for information.        |
sage: log_text("/tmp")
Now logging to /tmp/log-2008-03-27-004454/sagelog.txt
Text Logger
sage:
Exiting SAGE (CPU time 0m0.02s, Wall time 0m8.70s).
```
So: positive review!



---

archive/issue_comments_017454.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-27T07:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17454",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_events_005995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-27T07:50:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2565#event-5995"
}
```



---

archive/issue_comments_017455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-27T07:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2565#issuecomment-17455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
