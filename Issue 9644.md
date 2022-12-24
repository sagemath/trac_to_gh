# Issue 9644: Make Sage run even when $SAGE_ROOT contains spaces

archive/issues_009644.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  @kcrisman @nexttime @dandrake @haraldschilly mvngu\n\nReported by Dan on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/3694601bc3de1a80):\n\n```\nThis is an observation about the pre-compiled binaries for Mac OS.\n\nIf the (unpacked) sage disk image directory is saved in a folder that has a\nspace character in its name, for example:\n\n$HOME/Applications/my folder\n\nThen sage will not load properly when the \"sage\" executable is clicked. The\nterminal session begins, but the application doesn't load successfully.\n\nChanging the parent directory name to \"my_folder\" resolved this issue.\n\nWhile using space characters in directory names probably isn't all that common\nin UNIX or Linux installations, it is more common in Mac OS installations.\nPerhaps the installation instructions could be updated to mention this issue? \n```\n\n\nThis actually appears to be a more general problem:\n\n```sh\n$ hostname\nsage.math.washington.edu\n$ pwd\n/mnt/usb1/scratch/mpatel/tmp/my sage\n$ ./sage\nError setting environment variables by running /mnt/usb1/scratch/mpatel/tmp/my sage/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel).\ncat: /bin/sage-banner: No such file or directory\nmkdir: cannot create directory `': No such file or directory\ncp: cannot create directory `/ipython': Permission denied\nTraceback (most recent call last):\n  File \"./sage-cleaner\", line 25, in <module>\n    DOT_SAGE = os.environ['DOT_SAGE']\n  File \"/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/UserDict.py\", line 22, in __getitem__\n    raise KeyError(key)\nKeyError: 'DOT_SAGE'\n**********************************************************************\nWelcome to IPython. I will try to create a personal configuration directory\nwhere you can customize many aspects of IPython's functionality in:\n\n/ipython\nInitializing from configuration /mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/UserConfig\nWARNING: \n\nThere was a problem with the installation:\n[Errno 13] Permission denied: '/ipython'\nTry to correct it or contact the developers if you think it's a bug.\nIPython will proceed with builtin defaults.\nPlease press <RETURN> to start IPython.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9644\n\n",
    "created_at": "2010-07-30T01:15:46Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Make Sage run even when $SAGE_ROOT contains spaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9644",
    "user": "@qed777"
}
```
Assignee: @jasongrout

CC:  @kcrisman @nexttime @dandrake @haraldschilly mvngu

Reported by Dan on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/3694601bc3de1a80):

```
This is an observation about the pre-compiled binaries for Mac OS.

If the (unpacked) sage disk image directory is saved in a folder that has a
space character in its name, for example:

$HOME/Applications/my folder

Then sage will not load properly when the "sage" executable is clicked. The
terminal session begins, but the application doesn't load successfully.

Changing the parent directory name to "my_folder" resolved this issue.

While using space characters in directory names probably isn't all that common
in UNIX or Linux installations, it is more common in Mac OS installations.
Perhaps the installation instructions could be updated to mention this issue? 
```


This actually appears to be a more general problem:

```sh
$ hostname
sage.math.washington.edu
$ pwd
/mnt/usb1/scratch/mpatel/tmp/my sage
$ ./sage
Error setting environment variables by running /mnt/usb1/scratch/mpatel/tmp/my sage/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel).
cat: /bin/sage-banner: No such file or directory
mkdir: cannot create directory `': No such file or directory
cp: cannot create directory `/ipython': Permission denied
Traceback (most recent call last):
  File "./sage-cleaner", line 25, in <module>
    DOT_SAGE = os.environ['DOT_SAGE']
  File "/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/UserDict.py", line 22, in __getitem__
    raise KeyError(key)
KeyError: 'DOT_SAGE'
**********************************************************************
Welcome to IPython. I will try to create a personal configuration directory
where you can customize many aspects of IPython's functionality in:

/ipython
Initializing from configuration /mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/UserConfig
WARNING: 

There was a problem with the installation:
[Errno 13] Permission denied: '/ipython'
Try to correct it or contact the developers if you think it's a bug.
IPython will proceed with builtin defaults.
Please press <RETURN> to start IPython.
```


Issue created by migration from https://trac.sagemath.org/ticket/9644





---

archive/issue_comments_093477.json:
```json
{
    "body": "After applying \n\n```diff\ndiff --git a/sage-sage b/sage-sage\n--- a/sage-sage\n+++ b/sage-sage\n@@ -127,7 +127,7 @@ usage_advanced() {\n     exit 1\n }\n \n-. $SAGE_ROOT/local/bin/sage-env   1>/dev/null 2>/dev/null\n+. \"$SAGE_ROOT/local/bin/sage-env\"   1>/dev/null 2>/dev/null\n \n if [ $? -ne 0 ]; then\n    echo \"Error setting environment variables by running $SAGE_ROOT/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel).\"\n```\n\nI get\n\n```python\n$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nls: cannot access /mnt/usb1/scratch/mpatel/tmp/my: No such file or directory\nls: cannot access sage/devel/sage: Not a directory\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n| Sage Version 4.5.2.rc0, Release Date: 2010-07-28                   |\n| Type notebook() for the GUI, and license() for information.        |\n/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/mnt/usb1/scratch/mpatel/tmp/my sage/ipy_profile_sage.py in <module>()\n     14     from sage.misc.interpreter import attached_files\n     15 \n---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())\n     17     if branch:\n     18         print branch\n\n/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in branch_current_hg()\n   1877     i = s.rfind('->')\n   1878     if i == -1:\n-> 1879         raise RuntimeError, \"unable to determine branch?!\"\n   1880     s = s[i+2:]\n   1881     i = s.find('-')\n\nRuntimeError: unable to determine branch?!\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\nsage: \n```\n",
    "created_at": "2010-07-30T01:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93477",
    "user": "@qed777"
}
```

After applying 

```diff
diff --git a/sage-sage b/sage-sage
--- a/sage-sage
+++ b/sage-sage
@@ -127,7 +127,7 @@ usage_advanced() {
     exit 1
 }
 
-. $SAGE_ROOT/local/bin/sage-env   1>/dev/null 2>/dev/null
+. "$SAGE_ROOT/local/bin/sage-env"   1>/dev/null 2>/dev/null
 
 if [ $? -ne 0 ]; then
    echo "Error setting environment variables by running $SAGE_ROOT/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel)."
```

I get

```python
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
ls: cannot access /mnt/usb1/scratch/mpatel/tmp/my: No such file or directory
ls: cannot access sage/devel/sage: Not a directory
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.5.2.rc0, Release Date: 2010-07-28                   |
| Type notebook() for the GUI, and license() for information.        |
/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/mnt/usb1/scratch/mpatel/tmp/my sage/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in branch_current_hg()
   1877     i = s.rfind('->')
   1878     if i == -1:
-> 1879         raise RuntimeError, "unable to determine branch?!"
   1880     s = s[i+2:]
   1881     i = s.find('-')

RuntimeError: unable to determine branch?!
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage: 
```




---

archive/issue_comments_093478.json:
```json
{
    "body": "<flame>\n\n**R T F M ! ** ;-)\n\n(Milestone Sage 6.0)\n\n</flame>\n\nIt is well documented that `$SAGE_ROOT` (and therefore `$SAGE_LOCAL` **must not** contain spaces; I only wondered a few times if this is checked/catched anywhere, since almost all scripts (especially `spkg-install` scripts) blindly rely on this. So changing this (allowing spaces) is a big task, which is IMHO not worth doing now. It is *in general* a bad idea to put spaces in *path* names (filenames are a little different/less problematic).\n\n-Leif",
    "created_at": "2010-07-30T01:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93478",
    "user": "@nexttime"
}
```

<flame>

**R T F M ! ** ;-)

(Milestone Sage 6.0)

</flame>

It is well documented that `$SAGE_ROOT` (and therefore `$SAGE_LOCAL` **must not** contain spaces; I only wondered a few times if this is checked/catched anywhere, since almost all scripts (especially `spkg-install` scripts) blindly rely on this. So changing this (allowing spaces) is a big task, which is IMHO not worth doing now. It is *in general* a bad idea to put spaces in *path* names (filenames are a little different/less problematic).

-Leif



---

archive/issue_comments_093479.json:
```json
{
    "body": "Ok, it could perhaps be documented in more prominent places, but it's (still) twice in `$SAGE_ROOT/README.txt`, the second time a bit to mild:\n\n```\n...\nMORE DETAILED INSTRUCTIONS TO BUILD FROM SOURCE\n-----------------------------------------------\n...\n3. Extract the Sage source tarball and cd into a directory with no\n   spaces in it. [...]\n\n...\n\nRELOCATION\n----------\n\nYou *should* be able to move the sage-x.y.z directory anywhere you\nwant. If you copy the sage script or make a symbolic link to it, you\nshould modify the script to reflect this (as instructed at the top of\nthe script). It is best if the path to Sage does not have any spaces in\nit.\n...\n```\n\n\nAnd afair it is (or at least has been at some time) better documented in the Installation Guide.\n\nSo I would open two tickets (one could be this with changed title):\n\n* Make sure `$SAGE_ROOT` does not contain spaces, e.g. in `sage-env` (blocker).\n\n* Improve documentation (CAPSLOCK? Add/move remarks to top of files.)",
    "created_at": "2010-07-30T02:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93479",
    "user": "@nexttime"
}
```

Ok, it could perhaps be documented in more prominent places, but it's (still) twice in `$SAGE_ROOT/README.txt`, the second time a bit to mild:

```
...
MORE DETAILED INSTRUCTIONS TO BUILD FROM SOURCE
-----------------------------------------------
...
3. Extract the Sage source tarball and cd into a directory with no
   spaces in it. [...]

...

RELOCATION
----------

You *should* be able to move the sage-x.y.z directory anywhere you
want. If you copy the sage script or make a symbolic link to it, you
should modify the script to reflect this (as instructed at the top of
the script). It is best if the path to Sage does not have any spaces in
it.
...
```


And afair it is (or at least has been at some time) better documented in the Installation Guide.

So I would open two tickets (one could be this with changed title):

* Make sure `$SAGE_ROOT` does not contain spaces, e.g. in `sage-env` (blocker).

* Improve documentation (CAPSLOCK? Add/move remarks to top of files.)



---

archive/issue_comments_093480.json:
```json
{
    "body": "Ouch, I just realized the scripting \"logic\" is completely insane:\n\nWhile `sage-env` is intended to be **sourced** (rather than called), and `sage-sage` does this,\n\n* `sage-sage` redirects stdout and stderr while sourcing `sage-env` to `/dev/null`, though `sage-env` eventually outputs (valuable) error messages\n* `sage-sage` tests its \"exit status\", though it is sourced, not called\n* `sage-env` actually **exits** with 1 on error\n\nSo even when an error is detected in `sage-env`, the user will never see the error message, but Sage will simply \"silently\" exit.\n\nArgh...",
    "created_at": "2010-07-30T04:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93480",
    "user": "@nexttime"
}
```

Ouch, I just realized the scripting "logic" is completely insane:

While `sage-env` is intended to be **sourced** (rather than called), and `sage-sage` does this,

* `sage-sage` redirects stdout and stderr while sourcing `sage-env` to `/dev/null`, though `sage-env` eventually outputs (valuable) error messages
* `sage-sage` tests its "exit status", though it is sourced, not called
* `sage-env` actually **exits** with 1 on error

So even when an error is detected in `sage-env`, the user will never see the error message, but Sage will simply "silently" exit.

Argh...



---

archive/issue_comments_093481.json:
```json
{
    "body": "With the attached patch I get:\n\n```sh\nleif@portland:~/Sage /sage-4.5.2.alpha0-j12$ ./sage\nError: The path to the Sage directory ($SAGE_ROOT) MUST NOT contain spaces.\nIt is currently \"/home/leif/Sage /sage-4.5.2.alpha0-j12\".\nYou must correct this by moving Sage (or renaming some directories) first.\nExiting now...\nleif@portland:~/Sage /sage-4.5.2.alpha0-j12$ \n```\n\n(Note the spaces in the path, I simply renamed a component of the path to my Sage directories.)",
    "created_at": "2010-07-30T04:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93481",
    "user": "@nexttime"
}
```

With the attached patch I get:

```sh
leif@portland:~/Sage /sage-4.5.2.alpha0-j12$ ./sage
Error: The path to the Sage directory ($SAGE_ROOT) MUST NOT contain spaces.
It is currently "/home/leif/Sage /sage-4.5.2.alpha0-j12".
You must correct this by moving Sage (or renaming some directories) first.
Exiting now...
leif@portland:~/Sage /sage-4.5.2.alpha0-j12$ 
```

(Note the spaces in the path, I simply renamed a component of the path to my Sage directories.)



---

archive/issue_comments_093482.json:
```json
{
    "body": "The error message could of course be a bit more friendly, for example:\n\n  *\"**Please** correct this by moving Sage (or renaming some directories) first.\"*",
    "created_at": "2010-07-30T05:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93482",
    "user": "@nexttime"
}
```

The error message could of course be a bit more friendly, for example:

  *"**Please** correct this by moving Sage (or renaming some directories) first."*



---

archive/issue_comments_093483.json:
```json
{
    "body": "An alternative, perhaps simpler, but \"less efficient\" test for spaces would be:\n\n```sh\n    [ `echo \"X${SAGE_ROOT}X\" | wc -w` -ne 1 ]\n```\n\n(This one catches leading and trailing blanks, too, like the shell function in the patch when called properly. But we usually have leading and trailing slashs/path separators in `$SAGE_ROOT` anyway.)",
    "created_at": "2010-07-30T07:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93483",
    "user": "@nexttime"
}
```

An alternative, perhaps simpler, but "less efficient" test for spaces would be:

```sh
    [ `echo "X${SAGE_ROOT}X" | wc -w` -ne 1 ]
```

(This one catches leading and trailing blanks, too, like the shell function in the patch when called properly. But we usually have leading and trailing slashs/path separators in `$SAGE_ROOT` anyway.)



---

archive/issue_comments_093484.json:
```json
{
    "body": "I know there was one bit of code in sage which removed one space, but not multiple ones. i.e. \n\n\n```\nsed 's/ //' \n```\n\n\nrather than \n\n\n```\nsed 's/ //g'\n```\n\n\nI changed the one occurrence I spotted, but there might be others lucking. \n\nOf course, the best way to solve this is to not have any hacks like this, and just get Sage to build with spaces in paths. If things are quoted properly, this should be possible. \n\nPerhaps there should be an environment variable that can be used to bypass that hack which removes spaces. Then we could slowly find the packages that have problems and correct them one by one. Once they were all corrected, the hack could be removed and Sage would build on paths with spaces in them. \n\nDave",
    "created_at": "2010-07-30T10:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93484",
    "user": "drkirkby"
}
```

I know there was one bit of code in sage which removed one space, but not multiple ones. i.e. 


```
sed 's/ //' 
```


rather than 


```
sed 's/ //g'
```


I changed the one occurrence I spotted, but there might be others lucking. 

Of course, the best way to solve this is to not have any hacks like this, and just get Sage to build with spaces in paths. If things are quoted properly, this should be possible. 

Perhaps there should be an environment variable that can be used to bypass that hack which removes spaces. Then we could slowly find the packages that have problems and correct them one by one. Once they were all corrected, the hack could be removed and Sage would build on paths with spaces in them. 

Dave



---

archive/issue_comments_093485.json:
```json
{
    "body": "Gives error message on spaces in $SAGE_ROOT. (Draft, but functional. Slightly more friendly.) Apply to scripts repo.",
    "created_at": "2010-07-30T14:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93485",
    "user": "@nexttime"
}
```

Gives error message on spaces in $SAGE_ROOT. (Draft, but functional. Slightly more friendly.) Apply to scripts repo.



---

archive/issue_comments_093486.json:
```json
{
    "body": "Attachment [trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch](tarball://root/attachments/some-uuid/ticket9644/trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch) by @nexttime created at 2010-07-30 14:36:07\n\nWe could require people who update/provide new spkgs to at least check if the upstream supports spaces in path names (I really doubt all will), and to harden the corresponding Sage scripts in that way. But I expect this to be a long lasting process, rather than a goal for any release in the nearer future.\n\nAnd I have absolutely no idea which \"inner\" parts of Sage (i.e. Python code) might break on spaces in file or path names.\n\nOf course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.",
    "created_at": "2010-07-30T14:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93486",
    "user": "@nexttime"
}
```

Attachment [trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch](tarball://root/attachments/some-uuid/ticket9644/trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch) by @nexttime created at 2010-07-30 14:36:07

We could require people who update/provide new spkgs to at least check if the upstream supports spaces in path names (I really doubt all will), and to harden the corresponding Sage scripts in that way. But I expect this to be a long lasting process, rather than a goal for any release in the nearer future.

And I have absolutely no idea which "inner" parts of Sage (i.e. Python code) might break on spaces in file or path names.

Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.



---

archive/issue_comments_093487.json:
```json
{
    "body": "> \n> Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.\n\nAnd THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.  \n\nAnyway, I'm glad to see this wasn't a platform-specific issue.  Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.  (The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?)",
    "created_at": "2010-07-30T15:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93487",
    "user": "@kcrisman"
}
```

> 
> Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.

And THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.  

Anyway, I'm glad to see this wasn't a platform-specific issue.  Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.  (The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?)



---

archive/issue_comments_093488.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T16:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93488",
    "user": "@nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093489.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> > \n> > Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.\n> \n> And THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.\n\nAlthough the README.txt (and other scattered pieces of information) are rarely changed/current, I really thought this was a well-known issue, since I came across that in the documentation many times. (I think it once was better placed, s.t. nobody could miss it, though people tend to read READMEs and installation guides - if at all - *after* they run into problems... ;-) )\n\n> [...] Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.\n\nYes, that's what I was thinking of, too.\n\n> The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?\n\nAs long as it fits onto a 80x25 screen... Feel free to add a \"reviewer patch\" or make some suggestion and I'll update the patch. I'm quite sure then this could get into 4.5.2.\n\nSomeone volunteering for a revised README?\n\nHarald, ideas for the web page?",
    "created_at": "2010-07-30T16:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93489",
    "user": "@nexttime"
}
```

Replying to [comment:11 kcrisman]:
> > 
> > Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.
> 
> And THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.

Although the README.txt (and other scattered pieces of information) are rarely changed/current, I really thought this was a well-known issue, since I came across that in the documentation many times. (I think it once was better placed, s.t. nobody could miss it, though people tend to read READMEs and installation guides - if at all - *after* they run into problems... ;-) )

> [...] Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.

Yes, that's what I was thinking of, too.

> The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?

As long as it fits onto a 80x25 screen... Feel free to add a "reviewer patch" or make some suggestion and I'll update the patch. I'm quite sure then this could get into 4.5.2.

Someone volunteering for a revised README?

Harald, ideas for the web page?



---

archive/issue_comments_093490.json:
```json
{
    "body": "Oh, perhaps the Makefile or `spkg/install` should get some early check, too.",
    "created_at": "2010-07-30T16:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93490",
    "user": "@nexttime"
}
```

Oh, perhaps the Makefile or `spkg/install` should get some early check, too.



---

archive/issue_comments_093491.json:
```json
{
    "body": "Well, it's possible to add anything somewhere on the webpage, but I think it doesn't look good, or is professional, to list bugs on a download page (especially because it is never read just like the readme).\n\nI don't know the exact problem, but I'm for adding a check at the \"sage\" script itself -- ahh, i've just seen that above -- and to the early scripts when starting to build sage.",
    "created_at": "2010-07-30T16:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93491",
    "user": "@haraldschilly"
}
```

Well, it's possible to add anything somewhere on the webpage, but I think it doesn't look good, or is professional, to list bugs on a download page (especially because it is never read just like the readme).

I don't know the exact problem, but I'm for adding a check at the "sage" script itself -- ahh, i've just seen that above -- and to the early scripts when starting to build sage.



---

archive/issue_comments_093492.json:
```json
{
    "body": "The [Installation Guide](http://www.sagemath.org/doc/installation/) definitely needs to be updated, too:\n\n  *[...] Make sure there are no spaces in the directory name under which you build. Running from a directory with spaces in its name is supported but discouraged. Building is not possible, since several of the components do not build if there are spaces in the path. [...]*\n\n(This snippet is actually from [*Steps to Install from Source*](http://www.sagemath.org/doc/installation/source.html#steps-to-install-from-source).)",
    "created_at": "2010-07-31T14:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93492",
    "user": "@nexttime"
}
```

The [Installation Guide](http://www.sagemath.org/doc/installation/) definitely needs to be updated, too:

  *[...] Make sure there are no spaces in the directory name under which you build. Running from a directory with spaces in its name is supported but discouraged. Building is not possible, since several of the components do not build if there are spaces in the path. [...]*

(This snippet is actually from [*Steps to Install from Source*](http://www.sagemath.org/doc/installation/source.html#steps-to-install-from-source).)



---

archive/issue_comments_093493.json:
```json
{
    "body": "An aside: For this special situation:\n\n1. Build Sage with no spaces in `SAGE_ROOT`.\n2. Rename `SAGE_ROOT` to contain space(s).\n\nthe patches [here](http://sage.math.washington.edu/home/mpatel/trac/9644) should get Sage to start and get `sage -b`, `sage -clone`, `sage -docbuild`, and `sage -t(p)` commands to work.  Except for some SYMPOW and GAP-related tests, the long doctests pass.  It's likely that fixing these components requires spkg updates.\n\nI'm sure there are other problems to fix, and these patches certainly won't allow Sage to build with spaces in `SAGE_ROOT`.  But the exercise suggests that to fix most (all?) Python code, we should focus on system calls, e.g., `os.{popen*,system}`, `subprocess.{call,Popen}`, etc.  Of course, we can open other tickets for these changes.",
    "created_at": "2010-08-01T09:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93493",
    "user": "@qed777"
}
```

An aside: For this special situation:

1. Build Sage with no spaces in `SAGE_ROOT`.
2. Rename `SAGE_ROOT` to contain space(s).

the patches [here](http://sage.math.washington.edu/home/mpatel/trac/9644) should get Sage to start and get `sage -b`, `sage -clone`, `sage -docbuild`, and `sage -t(p)` commands to work.  Except for some SYMPOW and GAP-related tests, the long doctests pass.  It's likely that fixing these components requires spkg updates.

I'm sure there are other problems to fix, and these patches certainly won't allow Sage to build with spaces in `SAGE_ROOT`.  But the exercise suggests that to fix most (all?) Python code, we should focus on system calls, e.g., `os.{popen*,system}`, `subprocess.{call,Popen}`, etc.  Of course, we can open other tickets for these changes.



---

archive/issue_comments_093494.json:
```json
{
    "body": "Thanks, Leif.  I'd like to focus, for now, on releasing 4.5.3 and then on the PARI upgrade for 4.6.alpha0.  I'll try to work on this ticket after 4.5.3 is out.",
    "created_at": "2010-08-20T08:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93494",
    "user": "@qed777"
}
```

Thanks, Leif.  I'd like to focus, for now, on releasing 4.5.3 and then on the PARI upgrade for 4.6.alpha0.  I'll try to work on this ticket after 4.5.3 is out.



---

archive/issue_comments_093495.json:
```json
{
    "body": "Btw: If you want to have fun, try *compiling* Sage with `-O2` contained in `$SAGE_ROOT`.\n\n(It's `libgcrypt` that fails IIRC.)",
    "created_at": "2010-08-20T11:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93495",
    "user": "@nexttime"
}
```

Btw: If you want to have fun, try *compiling* Sage with `-O2` contained in `$SAGE_ROOT`.

(It's `libgcrypt` that fails IIRC.)



---

archive/issue_comments_093496.json:
```json
{
    "body": "This looks good to me; positive review for \"trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch\". Trying to get Sage to work with spaces in the path can go on another ticket.  Meanwhile, I'm attaching a patch for the installation guide.",
    "created_at": "2010-09-21T21:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93496",
    "user": "@jhpalmieri"
}
```

This looks good to me; positive review for "trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch". Trying to get Sage to work with spaces in the path can go on another ticket.  Meanwhile, I'm attaching a patch for the installation guide.



---

archive/issue_comments_093497.json:
```json
{
    "body": "John's happy with Leif's patch. I'm happy with John's changes to the installation guide. So positive review.",
    "created_at": "2010-09-21T22:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93497",
    "user": "drkirkby"
}
```

John's happy with Leif's patch. I'm happy with John's changes to the installation guide. So positive review.



---

archive/issue_comments_093498.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-21T22:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93498",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093499.json:
```json
{
    "body": "Thanks, everyone, for working on this.",
    "created_at": "2010-09-21T22:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93499",
    "user": "@qed777"
}
```

Thanks, everyone, for working on this.



---

archive/issue_comments_093500.json:
```json
{
    "body": "So we are all happy. :)\n\nMinor correction: Swap *from* and *to* in *\"Another approach is to create a symbolic link ...\"*.\n(This has been in before. IIRC there are somewhere more instances of that, but never mind.)",
    "created_at": "2010-09-21T23:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93500",
    "user": "@nexttime"
}
```

So we are all happy. :)

Minor correction: Swap *from* and *to* in *"Another approach is to create a symbolic link ..."*.
(This has been in before. IIRC there are somewhere more instances of that, but never mind.)



---

archive/issue_comments_093501.json:
```json
{
    "body": "How about this?",
    "created_at": "2010-09-21T23:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93501",
    "user": "@jhpalmieri"
}
```

How about this?



---

archive/issue_comments_093502.json:
```json
{
    "body": "Thanks, very good.",
    "created_at": "2010-09-21T23:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93502",
    "user": "@nexttime"
}
```

Thanks, very good.



---

archive/issue_comments_093503.json:
```json
{
    "body": "The invocation of sage-env from the top-level makefile is causing errors.  On sage.math:\n\n```\n. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log\nlocal/bin/sage-env: 70: Syntax error: Bad function name\nmake: *** [ptestlong] Error 2\n```\n\nOn my mac:\n\n```\n. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log\nlocal/bin/sage-env: line 77: `contains-spaces': not a valid identifier\nmake: *** [ptestlong] Error 2\n```\n\nOn t2.math:\n\n```\n. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log\n/bin/sh: contains-spaces: is not an identifier\nmake: *** [ptestlong] Error 1\n```\n\nIn all cases, changing \"contains-spaces\" to \"contains_spaces\" seems to fix the problem.  I'm attaching a small patch to do this.  (On Solaris systems, I also see a new warning, presumably because we're not redirecting output to /dev/null: after typing \"make ptestlong\", I see\n\n```\nBuild finished.  The built documents can be found in /scratch/palmieri/sage-4.5.3.rc0/devel/sage/doc/output/html/fr/a_tour_of_sage\n. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log\n/bin/sh: source: not found\nTesting that Sage starts...\nYes, Sage starts.\nTesting that Sage starts...\nYes, Sage starts.\nGlobal iterations: 1\nFile iterations: 1\n```\n\nNote the line `/bin/sh: source: not found`.  Is this important?  If so, we should deal with it on another ticket...)",
    "created_at": "2010-09-22T18:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93503",
    "user": "@jhpalmieri"
}
```

The invocation of sage-env from the top-level makefile is causing errors.  On sage.math:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
local/bin/sage-env: 70: Syntax error: Bad function name
make: *** [ptestlong] Error 2
```

On my mac:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
local/bin/sage-env: line 77: `contains-spaces': not a valid identifier
make: *** [ptestlong] Error 2
```

On t2.math:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
/bin/sh: contains-spaces: is not an identifier
make: *** [ptestlong] Error 1
```

In all cases, changing "contains-spaces" to "contains_spaces" seems to fix the problem.  I'm attaching a small patch to do this.  (On Solaris systems, I also see a new warning, presumably because we're not redirecting output to /dev/null: after typing "make ptestlong", I see

```
Build finished.  The built documents can be found in /scratch/palmieri/sage-4.5.3.rc0/devel/sage/doc/output/html/fr/a_tour_of_sage
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
/bin/sh: source: not found
Testing that Sage starts...
Yes, Sage starts.
Testing that Sage starts...
Yes, Sage starts.
Global iterations: 1
File iterations: 1
```

Note the line `/bin/sh: source: not found`.  Is this important?  If so, we should deal with it on another ticket...)



---

archive/issue_comments_093504.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-22T18:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93504",
    "user": "@jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093505.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-22T18:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93505",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093506.json:
```json
{
    "body": "Thanks, I wanted to make exactly the same change weeks ago... (replacing the dash in the name by an underscore).\n\nAlso, `source` should be replaced by `.` (period). (At #9960 or here.)\n\n(Note that this error message has always been there; you just had to look into `/dev/null`... ;-) Redirecting `stderr` to Nirvana is rarely a good idea.)\n\n----\n\nAlthough the Makefile shouldn't break the assumption that we're using `bash`; so either `sage-env` should be removed there, or the line should be `bash -c ...`, or `/usr/bin/env bash -c ...`. There are various ways to fix that.\n\nI wonder if `sage-starts` shouldn't use `bash` (instead of `sh`) and itself source `sage-env`; then we could drop `. local/bin/sage-env &&` from `TESTPRELIMS`. (This would IMHO be cleaner.)",
    "created_at": "2010-09-22T20:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93506",
    "user": "@nexttime"
}
```

Thanks, I wanted to make exactly the same change weeks ago... (replacing the dash in the name by an underscore).

Also, `source` should be replaced by `.` (period). (At #9960 or here.)

(Note that this error message has always been there; you just had to look into `/dev/null`... ;-) Redirecting `stderr` to Nirvana is rarely a good idea.)

----

Although the Makefile shouldn't break the assumption that we're using `bash`; so either `sage-env` should be removed there, or the line should be `bash -c ...`, or `/usr/bin/env bash -c ...`. There are various ways to fix that.

I wonder if `sage-starts` shouldn't use `bash` (instead of `sh`) and itself source `sage-env`; then we could drop `. local/bin/sage-env &&` from `TESTPRELIMS`. (This would IMHO be cleaner.)



---

archive/issue_comments_093507.json:
```json
{
    "body": "The changes look fine. \n\nThe `/bin/sh: [`](../tree/master/`) is quite a common error. We should not solve it by redirecting stderr to /dev/null, but removing the word `source` and replacing it with a dot. I suspect there are many instances of this lucking around. The problem is the command does not exist in `/bin/sh` but does in `bash` See below. \n\nHere my default shell is `bash`, so `source` exists as a built in shell command. \n\n```\nkirkby@t2:64 ~$ source\n-bash: source: filename argument required\nsource: usage: source filename [arguments]\n```\n\n\nNow change my shell to /bin/sh\n\n\n```\nkirkby@t2:64 ~$ sh\n$ source\nsource: not found\n$ \n```\n\n\nI'd prefer to use the more portable `.` (dot) which will achieve the same, but is not a bashism. These should certainly be addressed on another ticket. The fact they  are not producing any known errors, makes me wonder how important it is to source the files in the first place!",
    "created_at": "2010-09-22T20:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93507",
    "user": "drkirkby"
}
```

The changes look fine. 

The `/bin/sh: [`](../tree/master/`) is quite a common error. We should not solve it by redirecting stderr to /dev/null, but removing the word `source` and replacing it with a dot. I suspect there are many instances of this lucking around. The problem is the command does not exist in `/bin/sh` but does in `bash` See below. 

Here my default shell is `bash`, so `source` exists as a built in shell command. 

```
kirkby@t2:64 ~$ source
-bash: source: filename argument required
source: usage: source filename [arguments]
```


Now change my shell to /bin/sh


```
kirkby@t2:64 ~$ sh
$ source
source: not found
$ 
```


I'd prefer to use the more portable `.` (dot) which will achieve the same, but is not a bashism. These should certainly be addressed on another ticket. The fact they  are not producing any known errors, makes me wonder how important it is to source the files in the first place!



---

archive/issue_comments_093508.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T20:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93508",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093509.json:
```json
{
    "body": "Sourcing `sage-env` in the Makefile is only needed to set up `SAGE_ROOT` for `sage-starts`, which calls a Python script (`sage-location`).\n\nThe other Sage scripts source `sage-env` themselves.\n\nAs said before, best would be to change `sage-starts` (and the Makefile) on another ticket; replacing `source` by `.` could be done at #9960 I think.\n\nAn even nicer solution would just \"source\" `sage-env` from the *Python* script (by invoking a shell that does this and echoes the necessary variables), also removing `. sage-env &&` from the Makefile.\n\n\nYou can hardly touch a piece of Sage without experiencing other things to fix... ;-)",
    "created_at": "2010-09-22T21:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93509",
    "user": "@nexttime"
}
```

Sourcing `sage-env` in the Makefile is only needed to set up `SAGE_ROOT` for `sage-starts`, which calls a Python script (`sage-location`).

The other Sage scripts source `sage-env` themselves.

As said before, best would be to change `sage-starts` (and the Makefile) on another ticket; replacing `source` by `.` could be done at #9960 I think.

An even nicer solution would just "source" `sage-env` from the *Python* script (by invoking a shell that does this and echoes the necessary variables), also removing `. sage-env &&` from the Makefile.


You can hardly touch a piece of Sage without experiencing other things to fix... ;-)



---

archive/issue_comments_093510.json:
```json
{
    "body": "Could someone please update the commit strings of the \"installation\" and \"ref\" patches to be a bit more descriptive and restore the positive review?",
    "created_at": "2010-09-29T07:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93510",
    "user": "@qed777"
}
```

Could someone please update the commit strings of the "installation" and "ref" patches to be a bit more descriptive and restore the positive review?



---

archive/issue_comments_093511.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-29T07:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93511",
    "user": "@qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093512.json:
```json
{
    "body": "Attachment [trac_9644-scripts-ref.patch](tarball://root/attachments/some-uuid/ticket9644/trac_9644-scripts-ref.patch) by @jhpalmieri created at 2010-09-29 16:47:43\n\napply on top of other scripts patch",
    "created_at": "2010-09-29T16:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93512",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9644-scripts-ref.patch](tarball://root/attachments/some-uuid/ticket9644/trac_9644-scripts-ref.patch) by @jhpalmieri created at 2010-09-29 16:47:43

apply on top of other scripts patch



---

archive/issue_comments_093513.json:
```json
{
    "body": "Here are new commit strings.  Can we restore the positive review now?",
    "created_at": "2010-09-29T16:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93513",
    "user": "@jhpalmieri"
}
```

Here are new commit strings.  Can we restore the positive review now?



---

archive/issue_comments_093514.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-29T16:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93514",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093515.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-29T21:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93515",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093516.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-09-29T21:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93516",
    "user": "@qed777"
}
```

Thanks!



---

archive/issue_comments_093517.json:
```json
{
    "body": "I've updated some Wiki pages a while ago.\n\nHarald said we shouldn't \"announce bugs\" on the download pages; I think a simple comment on where to currently not install Sage shouldn't be interpreted as such.",
    "created_at": "2010-09-29T21:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93517",
    "user": "@nexttime"
}
```

I've updated some Wiki pages a while ago.

Harald said we shouldn't "announce bugs" on the download pages; I think a simple comment on where to currently not install Sage shouldn't be interpreted as such.



---

archive/issue_comments_093518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T23:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9644#issuecomment-93518",
    "user": "@qed777"
}
```

Resolution: fixed
