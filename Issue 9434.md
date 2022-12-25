# Issue 9434: Stop greping for a non-existent sage-banner

archive/issues_009434.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jhpalmieri\n\nIn install.log, we often see:\n\n\n```\ndrkirkby@hawk:~/f/sage-4.5.alpha3$ grep sage-banner install.log\ngrep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner\ngrep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner\ngrep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner\ngrep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner\nsage_scripts-4.5.alpha3/.hg/store/data/sage-banner.i\nsage_scripts-4.5.alpha3/sage-banner\ndrkirkby@hawk:~/f/sage-4.5.alpha3$ \n```\n\n\nI think this is probably due to some code in sage-sage\n\n\n```\nif [ \"$1\" = '-v' -o \"$1\" = '-version' -o \"$1\" = '--version' ]; then\n    cat \"$SAGE_LOCAL/bin/sage-banner\" | grep -i \"version\" | sed \"s/\\| //\" | sed \"s/ *\\|//\"\n    exit $?\nfi\n```\n\n\nThis will obviously fail if sage-banner does not exist. \n\nAlso\n* There is an useless use of 'cat'. Perhaps the author was hoping to get a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html) (Well worth a read - it's both funny and educational.) \n* There is an an unnecessary use of double-quotes around 'version'. \n\nThe following will save a few bytes of disk space and a few CPU cycles, as it will invoke one less process. \n\n\n```\n    grep -i version \"$SAGE_LOCAL/bin/sage-banner\" | sed \"s/\\| //\" | sed \"s/ *\\|//\"\n```\n\n\nMore importantly, we should check that sage-banner exists before doing this, so it does not produce potentially confusing error messages. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9434\n\n",
    "created_at": "2010-07-06T06:50:04Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Stop greping for a non-existent sage-banner",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9434",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jhpalmieri

In install.log, we often see:


```
drkirkby@hawk:~/f/sage-4.5.alpha3$ grep sage-banner install.log
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
sage_scripts-4.5.alpha3/.hg/store/data/sage-banner.i
sage_scripts-4.5.alpha3/sage-banner
drkirkby@hawk:~/f/sage-4.5.alpha3$ 
```


I think this is probably due to some code in sage-sage


```
if [ "$1" = '-v' -o "$1" = '-version' -o "$1" = '--version' ]; then
    cat "$SAGE_LOCAL/bin/sage-banner" | grep -i "version" | sed "s/\| //" | sed "s/ *\|//"
    exit $?
fi
```


This will obviously fail if sage-banner does not exist. 

Also
* There is an useless use of 'cat'. Perhaps the author was hoping to get a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html) (Well worth a read - it's both funny and educational.) 
* There is an an unnecessary use of double-quotes around 'version'. 

The following will save a few bytes of disk space and a few CPU cycles, as it will invoke one less process. 


```
    grep -i version "$SAGE_LOCAL/bin/sage-banner" | sed "s/\| //" | sed "s/ *\|//"
```


More importantly, we should check that sage-banner exists before doing this, so it does not produce potentially confusing error messages. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9434





---

archive/issue_comments_090099.json:
```json
{
    "body": "Well, reading carefully, your error messages can't come from `sage-sage`... (I know you haven't had much sleep... ;-) )\n\nBtw, there are more superfluous quotes.\n\nIf you want to save another \"redundant\" process invocation (there are in general many), at the expense of losing some parallelism, substitute\n\n```\n... | sed \"s/\\| //\" | sed \"s/ *\\|//\"\n```\n\nby\n\n```\n... | sed -e \"s/\\| //\" -e \"s/ *\\|//\"\n```\n\n\n(The whole line could be replaced by a single invocation of `sed`.)",
    "created_at": "2010-07-06T11:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90099",
    "user": "https://github.com/nexttime"
}
```

Well, reading carefully, your error messages can't come from `sage-sage`... (I know you haven't had much sleep... ;-) )

Btw, there are more superfluous quotes.

If you want to save another "redundant" process invocation (there are in general many), at the expense of losing some parallelism, substitute

```
... | sed "s/\| //" | sed "s/ *\|//"
```

by

```
... | sed -e "s/\| //" -e "s/ *\|//"
```


(The whole line could be replaced by a single invocation of `sed`.)



---

archive/issue_comments_090100.json:
```json
{
    "body": "Just for the record:\n\n```sh\ngrep -c \"^grep:\" install.log\n```\n\ngives me zero for both sequential and parallel builds of Sage 4.5.alpha4 (Ubuntu 9.04).",
    "created_at": "2010-07-10T05:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90100",
    "user": "https://github.com/nexttime"
}
```

Just for the record:

```sh
grep -c "^grep:" install.log
```

gives me zero for both sequential and parallel builds of Sage 4.5.alpha4 (Ubuntu 9.04).



---

archive/issue_comments_090101.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-07-10T06:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90101",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_090102.json:
```json
{
    "body": "Hi leif\n* I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing. \n* Yes, there are loads of unneeded quotes in this bit of Sage. \n* Interesting that you don't see this error message - I'm not the only one that gets it. I forget who posted the log with this, and commented on it, but someone did. \n\nI'll have to look at this, but its not exactly the most serious Sage bug. \n\nDave",
    "created_at": "2010-07-10T06:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90102",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi leif
* I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing. 
* Yes, there are loads of unneeded quotes in this bit of Sage. 
* Interesting that you don't see this error message - I'm not the only one that gets it. I forget who posted the log with this, and commented on it, but someone did. 

I'll have to look at this, but its not exactly the most serious Sage bug. 

Dave



---

archive/issue_comments_090103.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n>  * I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing.\n\nYes, though I love cats. One of my favorites is:\n\n```sh\nsed -n \"/[Vv]ersion/s/ *| *//gp\" $SAGE_LOCAL/bin/sage-banner\n```\n\n(Spaces in `$SAGE_LOCAL` are forbidden, otherwise we'd need quotes there.)\n\nNote that the original version gives two lines for non-finals; it does **not** remove the vertical bars (nor the whitespace) because the pipe symbol is \"superfluously\" escaped: :)\n\n```sh\nleif64@portland:~/Sage/sage-4.5.alpha4-serial$ ./sage -v\n* Warning: this is a prerelease version, and it may be unstable.     *\n```\n\n| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |\nMore important, the discussion is still somewhat off-topic or off-ticket, since - as mentioned - the error messages do not originate from `sage-sage`, so the issue has to be fixed elsewhere.\n\n> I'll have to look at this, but its not exactly the most serious Sage bug.\n\nObviously, I agree.",
    "created_at": "2010-07-10T09:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90103",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 drkirkby]:
>  * I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing.

Yes, though I love cats. One of my favorites is:

```sh
sed -n "/[Vv]ersion/s/ *| *//gp" $SAGE_LOCAL/bin/sage-banner
```

(Spaces in `$SAGE_LOCAL` are forbidden, otherwise we'd need quotes there.)

Note that the original version gives two lines for non-finals; it does **not** remove the vertical bars (nor the whitespace) because the pipe symbol is "superfluously" escaped: :)

```sh
leif64@portland:~/Sage/sage-4.5.alpha4-serial$ ./sage -v
* Warning: this is a prerelease version, and it may be unstable.     *
```

| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |
More important, the discussion is still somewhat off-topic or off-ticket, since - as mentioned - the error messages do not originate from `sage-sage`, so the issue has to be fixed elsewhere.

> I'll have to look at this, but its not exactly the most serious Sage bug.

Obviously, I agree.



---

archive/issue_comments_090104.json:
```json
{
    "body": "I think I've found the *real* culprit:\n\n```sh\n    # Mark that the new package has been installed. \n    # This file will eventually be a certificate like in OS X.\n    echo \"PACKAGE NAME: $PKG_NAME\" > \"$PKG_NAME\"\n    echo \"INSTALL DATE: `date`\" >> \"$PKG_NAME\"\n    echo \"UNAME: `uname -a`\" >> \"$PKG_NAME\"\n    echo \"Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`\" >> \"$PKG_NAME\"\n    echo \"Successfully installed $PKG_NAME\"\n```\n\n(This is from `sage-spkg`.)",
    "created_at": "2010-07-12T23:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90104",
    "user": "https://github.com/nexttime"
}
```

I think I've found the *real* culprit:

```sh
    # Mark that the new package has been installed. 
    # This file will eventually be a certificate like in OS X.
    echo "PACKAGE NAME: $PKG_NAME" > "$PKG_NAME"
    echo "INSTALL DATE: `date`" >> "$PKG_NAME"
    echo "UNAME: `uname -a`" >> "$PKG_NAME"
    echo "Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`" >> "$PKG_NAME"
    echo "Successfully installed $PKG_NAME"
```

(This is from `sage-spkg`.)



---

archive/issue_comments_090105.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> I think I've found the *real* culprit:\n> {{{\n> #!sh\n>     # Mark that the new package has been installed. \n>     # This file will eventually be a certificate like in OS X.\n>     echo \"PACKAGE NAME: $PKG_NAME\" > \"$PKG_NAME\"\n>     echo \"INSTALL DATE: `date`\" >> \"$PKG_NAME\"\n>     echo \"UNAME: `uname -a`\" >> \"$PKG_NAME\"\n>     echo \"Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`\" >> \"$PKG_NAME\"\n>     echo \"Successfully installed $PKG_NAME\"\n> }}}\n> (This is from `sage-spkg`.)\n\n\nYes, it looks like you have. It seems the author was not trying to win a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html). \n\nDo you have any idea why some people do not see this error message? If you can produce a patch, I can test it. \n\nDave",
    "created_at": "2010-07-12T23:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90105",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:5 leif]:
> I think I've found the *real* culprit:
> {{{
> #!sh
>     # Mark that the new package has been installed. 
>     # This file will eventually be a certificate like in OS X.
>     echo "PACKAGE NAME: $PKG_NAME" > "$PKG_NAME"
>     echo "INSTALL DATE: `date`" >> "$PKG_NAME"
>     echo "UNAME: `uname -a`" >> "$PKG_NAME"
>     echo "Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`" >> "$PKG_NAME"
>     echo "Successfully installed $PKG_NAME"
> }}}
> (This is from `sage-spkg`.)


Yes, it looks like you have. It seems the author was not trying to win a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html). 

Do you have any idea why some people do not see this error message? If you can produce a patch, I can test it. 

Dave



---

archive/issue_comments_090106.json:
```json
{
    "body": "Since sage-spkg is in spkg/base and in sage_scripts, while sage-banner is only in sage_scripts, you should see this message for any spkgs installed before sage-scripts.  In the most recent version of Sage, deps should install sage_scripts right at the beginning:\n\n```\nBASE = $(INST)/$(PREREQ) $(INST)/$(DIR) $(INST)/$(SAGE_BZIP2)\n\n# Also install scripts before we continue with other spkgs\nBASE += $(INST)/$(SAGE_SCRIPTS)\n```\n\nSo I hope this problem has already been taken care of.  Installing sage_scripts itself looks like the only possible problem.",
    "created_at": "2010-07-12T23:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90106",
    "user": "https://github.com/jhpalmieri"
}
```

Since sage-spkg is in spkg/base and in sage_scripts, while sage-banner is only in sage_scripts, you should see this message for any spkgs installed before sage-scripts.  In the most recent version of Sage, deps should install sage_scripts right at the beginning:

```
BASE = $(INST)/$(PREREQ) $(INST)/$(DIR) $(INST)/$(SAGE_BZIP2)

# Also install scripts before we continue with other spkgs
BASE += $(INST)/$(SAGE_SCRIPTS)
```

So I hope this problem has already been taken care of.  Installing sage_scripts itself looks like the only possible problem.



---

archive/issue_comments_090107.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> If you can produce a patch, I can test it.\n\nMilestone: Sage 5.0 ;-)\n\nI think a file containing (just) the Sage version number should be in `$SAGE_ROOT` anyhow; then we could `cat` that. (Testing for the existence of files is though not a bad idea...)",
    "created_at": "2010-07-12T23:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90107",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:6 drkirkby]:
> If you can produce a patch, I can test it.

Milestone: Sage 5.0 ;-)

I think a file containing (just) the Sage version number should be in `$SAGE_ROOT` anyhow; then we could `cat` that. (Testing for the existence of files is though not a bad idea...)



---

archive/issue_comments_090108.json:
```json
{
    "body": "Here's an attempt at fixing this.  Three comments: \n\n- It stores the current Sage version in SAGE_ROOT/VERSION.txt, as suggested by Leif -- see #9922.\n- Right now, upgrading just adds the new version to the top, with \"Updated from\" and then the old version, so if you've somehow managed to update 6 times, the file will have 7 lines in it, recording the full update history.\n- It uses cat.  Sorry, Dave.",
    "created_at": "2010-09-29T21:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90108",
    "user": "https://github.com/jhpalmieri"
}
```

Here's an attempt at fixing this.  Three comments: 

- It stores the current Sage version in SAGE_ROOT/VERSION.txt, as suggested by Leif -- see #9922.
- Right now, upgrading just adds the new version to the top, with "Updated from" and then the old version, so if you've somehow managed to update 6 times, the file will have 7 lines in it, recording the full update history.
- It uses cat.  Sorry, Dave.



---

archive/issue_comments_090109.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-29T21:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90109",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090110.json:
```json
{
    "body": "To be more precise: with the patch, in a non-upgrade, the file SAGE_ROOT/VERSION.txt will look like this:\n\n```\nSage version: 4.6.alpha2, Release date: 2010-09-29\n```\n\nI haven't tested the upgrade script yet, but it should produce\n\n```\nSage version: 4.6.alpha2, Release date: 2010-09-29\nUpgraded from Sage version: 4.6.alpha1, Release date: 2010-09-18\nUpgraded from ...\n```\n",
    "created_at": "2010-09-29T21:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90110",
    "user": "https://github.com/jhpalmieri"
}
```

To be more precise: with the patch, in a non-upgrade, the file SAGE_ROOT/VERSION.txt will look like this:

```
Sage version: 4.6.alpha2, Release date: 2010-09-29
```

I haven't tested the upgrade script yet, but it should produce

```
Sage version: 4.6.alpha2, Release date: 2010-09-29
Upgraded from Sage version: 4.6.alpha1, Release date: 2010-09-18
Upgraded from ...
```




---

archive/issue_comments_090111.json:
```json
{
    "body": "Hmmm, besides I don't like the date format string (which is *local* time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.\n\nDo you intentionally export `OLD_VERSION`?\n\nA non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.\n\nI'd prefer having *\"Sage version: ... [Last] Upgraded from: ...\"* on a single line (at least in the log).",
    "created_at": "2010-09-29T21:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90111",
    "user": "https://github.com/nexttime"
}
```

Hmmm, besides I don't like the date format string (which is *local* time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.

Do you intentionally export `OLD_VERSION`?

A non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.

I'd prefer having *"Sage version: ... [Last] Upgraded from: ..."* on a single line (at least in the log).



---

archive/issue_comments_090112.json:
```json
{
    "body": "You could use\n\n```sh\n    ...\n    if [ -f \"$SAGE_ROOT/VERSION.txt\" ]; then\n        sed -i -e \"1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\\nUpdated from $OLD_VERSION\"\n    else\n        ...\n```\n\nto avoid `cat` ... ;-)\n\n(Perhaps omit the newline, i.e. replace it by e.g. two spaces.)",
    "created_at": "2010-09-29T21:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90112",
    "user": "https://github.com/nexttime"
}
```

You could use

```sh
    ...
    if [ -f "$SAGE_ROOT/VERSION.txt" ]; then
        sed -i -e "1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\nUpdated from $OLD_VERSION"
    else
        ...
```

to avoid `cat` ... ;-)

(Perhaps omit the newline, i.e. replace it by e.g. two spaces.)



---

archive/issue_comments_090113.json:
```json
{
    "body": "And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.",
    "created_at": "2010-09-29T21:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90113",
    "user": "https://github.com/nexttime"
}
```

And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.



---

archive/issue_comments_090114.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n> Hmmm, besides I don't like the date format string (which is *local* time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.\n> \n> Do you intentionally export `OLD_VERSION`?\n\nRight, I'll fix these.\n\n> A non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.\n> \n> I'd prefer having *\"Sage version: ... [Last] Upgraded from: ...\"* on a single line (at least in the log).\n\nNote that the Sage version doesn't appear in the log: it should only appear in the files in spkg/installed/.  But maybe a single line is cleaner.\n\n> And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.\n\nWe can add VERSION.txt to .hgignore; I think that should do it.",
    "created_at": "2010-09-29T22:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90114",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:11 leif]:
> Hmmm, besides I don't like the date format string (which is *local* time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.
> 
> Do you intentionally export `OLD_VERSION`?

Right, I'll fix these.

> A non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.
> 
> I'd prefer having *"Sage version: ... [Last] Upgraded from: ..."* on a single line (at least in the log).

Note that the Sage version doesn't appear in the log: it should only appear in the files in spkg/installed/.  But maybe a single line is cleaner.

> And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.

We can add VERSION.txt to .hgignore; I think that should do it.



---

archive/issue_comments_090115.json:
```json
{
    "body": "scripts repo",
    "created_at": "2010-09-29T22:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90115",
    "user": "https://github.com/jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_090116.json:
```json
{
    "body": "Attachment [trac_9434-VERSION.txt.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION.txt.patch) by @jhpalmieri created at 2010-09-29 22:12:45\n\nThe new patch also modifies sage-make_devel_packages: when preparing the scripts package, it no longer indiscriminately copies all *.txt files from SAGE_ROOT into the scripts spkg, it just copies COPYING.txt and README.txt.  (Thus it won't copy VERSION.txt.)",
    "created_at": "2010-09-29T22:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90116",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9434-VERSION.txt.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION.txt.patch) by @jhpalmieri created at 2010-09-29 22:12:45

The new patch also modifies sage-make_devel_packages: when preparing the scripts package, it no longer indiscriminately copies all *.txt files from SAGE_ROOT into the scripts spkg, it just copies COPYING.txt and README.txt.  (Thus it won't copy VERSION.txt.)



---

archive/issue_comments_090117.json:
```json
{
    "body": "I wouldn't call `sage` in `sage-upgrade`. Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)\n\nRather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.\n\nAs noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).\n\nWe'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)\n\n----\n\n*\"While you're at it\"*<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?",
    "created_at": "2010-09-29T23:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90117",
    "user": "https://github.com/nexttime"
}
```

I wouldn't call `sage` in `sage-upgrade`. Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)

Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.

As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).

We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)

----

*"While you're at it"*<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?



---

archive/issue_comments_090118.json:
```json
{
    "body": "P.S.: See also #9905 (for the date format).",
    "created_at": "2010-09-29T23:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90118",
    "user": "https://github.com/nexttime"
}
```

P.S.: See also #9905 (for the date format).



---

archive/issue_comments_090119.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> You could use\n> {{{\n> #!sh\n>     ...\n>     if [ -f \"$SAGE_ROOT/VERSION.txt\" ]; then\n>         sed -i -e \"1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\\nUpdated from $OLD_VERSION\"\n>     else\n>         ...\n> }}}\n> to avoid `cat` ... ;-)\n> \n> (Perhaps omit the newline, i.e. replace it by e.g. two spaces.)\n> \n\nBut that would be an even bigger mistake than to use an unnecessary cat, as you are making use of non-POSIX options to `sed` - see [POSIX specifiction of sed](http://www.opengroup.org/onlinepubs/009695399/utilities/sed.html) I can guarantee that will fail on Solaris and AIX and probably other Unix systems too. \n\nDave",
    "created_at": "2010-09-30T05:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90119",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 leif]:
> You could use
> {{{
> #!sh
>     ...
>     if [ -f "$SAGE_ROOT/VERSION.txt" ]; then
>         sed -i -e "1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\nUpdated from $OLD_VERSION"
>     else
>         ...
> }}}
> to avoid `cat` ... ;-)
> 
> (Perhaps omit the newline, i.e. replace it by e.g. two spaces.)
> 

But that would be an even bigger mistake than to use an unnecessary cat, as you are making use of non-POSIX options to `sed` - see [POSIX specifiction of sed](http://www.opengroup.org/onlinepubs/009695399/utilities/sed.html) I can guarantee that will fail on Solaris and AIX and probably other Unix systems too. 

Dave



---

archive/issue_comments_090120.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> I wouldn't call `sage` in `sage-upgrade`. \n\nI can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`, after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.\n\n> Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)\n\nThat makes sense.\n\n> Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.\n\nWhy?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.  I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.  If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.\n\n> As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).\n\nRight.\n\n> We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)\n\nHow about extracting it from VERSION.txt?  I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.\n\n> *\"While you're at it\"*<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?\n\nI don't have time to do this now.",
    "created_at": "2010-09-30T05:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90120",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:17 leif]:
> I wouldn't call `sage` in `sage-upgrade`. 

I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`, after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.

> Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)

That makes sense.

> Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.

Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.  I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.  If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.

> As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).

Right.

> We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)

How about extracting it from VERSION.txt?  I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.

> *"While you're at it"*<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?

I don't have time to do this now.



---

archive/issue_comments_090121.json:
```json
{
    "body": "I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like \n\n```\nINSTALL DATE: Tue Sep 21 12:48:53 PDT 2010\n```\n\nfrom a file in spkg/installed, I didn't touch any of that code, and I don't have time to deal with it now.  I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.",
    "created_at": "2010-09-30T05:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90121",
    "user": "https://github.com/jhpalmieri"
}
```

I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like 

```
INSTALL DATE: Tue Sep 21 12:48:53 PDT 2010
```

from a file in spkg/installed, I didn't touch any of that code, and I don't have time to deal with it now.  I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.



---

archive/issue_comments_090122.json:
```json
{
    "body": "Replying to [comment:21 jhpalmieri]:\n> I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like \n> {{{\n> INSTALL DATE: Tue Sep 21 12:48:53 PDT 2010\n> }}}\n> from a file in spkg/installed, I didn't touch any of that code,\n\nI didn't mean that. (At least not for this ticket, since #9905 addresses this.)\n\n> I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.\n\nIt should simply be UTC. (`date -u +\"%Y-%m-%d\"` or better `date -u +\"%Y-%m-%d %Z\"` to include \"UTC\". One could also print the UTC verbatim, without `%Z`...)",
    "created_at": "2010-09-30T06:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90122",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:21 jhpalmieri]:
> I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like 
> {{{
> INSTALL DATE: Tue Sep 21 12:48:53 PDT 2010
> }}}
> from a file in spkg/installed, I didn't touch any of that code,

I didn't mean that. (At least not for this ticket, since #9905 addresses this.)

> I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.

It should simply be UTC. (`date -u +"%Y-%m-%d"` or better `date -u +"%Y-%m-%d %Z"` to include "UTC". One could also print the UTC verbatim, without `%Z`...)



---

archive/issue_comments_090123.json:
```json
{
    "body": "Replying to [comment:20 jhpalmieri]:\n> Replying to [comment:17 leif]:\n> > I wouldn't call `sage` in `sage-upgrade`. \n> \n> I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,\n\n`sage-upgrade` isn't \"the end\" of the upgrade process (it's called by `sage-sage`),\nand calling the \"new\" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.\n\n> after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.\n\nThis is done later, and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.\n\n> > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.\n> \n> Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.\n\nI didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (*not* in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.\n \n> I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.\n\nSee above.\n\n> If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.\n\nWell, `VERSION.txt` shouldn't be under revision control.\n \n> > As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).\n> \n> Right.\n> \n> > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)\n> \n> How about extracting it from VERSION.txt?\n\nExtracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.\n\n> I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.\n\nI'll take a look at it.",
    "created_at": "2010-09-30T06:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90123",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 jhpalmieri]:
> Replying to [comment:17 leif]:
> > I wouldn't call `sage` in `sage-upgrade`. 
> 
> I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,

`sage-upgrade` isn't "the end" of the upgrade process (it's called by `sage-sage`),
and calling the "new" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.

> after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.

This is done later, and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.

> > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.
> 
> Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.

I didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (*not* in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.
 
> I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.

See above.

> If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.

Well, `VERSION.txt` shouldn't be under revision control.
 
> > As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).
> 
> Right.
> 
> > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)
> 
> How about extracting it from VERSION.txt?

Extracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.

> I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.

I'll take a look at it.



---

archive/issue_comments_090124.json:
```json
{
    "body": "Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful. It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May? It's more confusing, as different parts of the world use different order for the month and day. \n\nOne other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind. \n\nBTW John, I've nothing against the use of `cat` as sometimes it is needed, but things like \n\n`cat filename | grep foobar`\n\nare a bit silly when \n\n`grep foobar filename`\n\nwill work, is shorter, and does not create an extra process. \n\nI've got to submit a job application today, so doing lots with Sage is not on my priority list today. Hence I wont be reviewing things for the rest of the day. \n\ndave",
    "created_at": "2010-09-30T07:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90124",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful. It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May? It's more confusing, as different parts of the world use different order for the month and day. 

One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind. 

BTW John, I've nothing against the use of `cat` as sometimes it is needed, but things like 

`cat filename | grep foobar`

are a bit silly when 

`grep foobar filename`

will work, is shorter, and does not create an extra process. 

I've got to submit a job application today, so doing lots with Sage is not on my priority list today. Hence I wont be reviewing things for the rest of the day. 

dave



---

archive/issue_comments_090125.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Replying to [comment:20 jhpalmieri]:\n> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.\n> \n> I'll take a look at it.\n\nOk, if we supply a separate file in the upgrade path. The code is a *bit* complicated though.",
    "created_at": "2010-09-30T07:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90125",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:23 leif]:
> Replying to [comment:20 jhpalmieri]:
> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.
> 
> I'll take a look at it.

Ok, if we supply a separate file in the upgrade path. The code is a *bit* complicated though.



---

archive/issue_comments_090126.json:
```json
{
    "body": "Replying to [comment:24 drkirkby]:\n> Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful.\n\nThat depends on the locale and isn't easily sortable or grepable. (I thought you had to deal with airlines; you know every date is always UTC there, regardless of any daylight saving or whatever.)\n\n> It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May?\n\nI'm aware there are some <censored> people writing 2010/28/02, but with slashes, not dashes.\n\n\n> One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.\n\nDetecting such is easier with the date format we have. ;-)\n\nBut I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date.",
    "created_at": "2010-09-30T07:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90126",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:24 drkirkby]:
> Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful.

That depends on the locale and isn't easily sortable or grepable. (I thought you had to deal with airlines; you know every date is always UTC there, regardless of any daylight saving or whatever.)

> It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May?

I'm aware there are some <censored> people writing 2010/28/02, but with slashes, not dashes.


> One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.

Detecting such is easier with the date format we have. ;-)

But I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date.



---

archive/issue_comments_090127.json:
```json
{
    "body": "Replying to [comment:26 leif]:\n\n> > One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.\n> \n> Detecting such is easier with the date format we have. ;-)\n> \n> But I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date. \n>  \n\nIf we nagged users their version of Sage was very old, we would not have the problems there are with the Debian distribution, and some other distributions of Sage. I think more than a year old and you do seriously need to nag them! \n\nDave",
    "created_at": "2010-09-30T07:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90127",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:26 leif]:

> > One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.
> 
> Detecting such is easier with the date format we have. ;-)
> 
> But I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date. 
>  

If we nagged users their version of Sage was very old, we would not have the problems there are with the Debian distribution, and some other distributions of Sage. I think more than a year old and you do seriously need to nag them! 

Dave



---

archive/issue_comments_090128.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Replying to [comment:20 jhpalmieri]:\n> > Replying to [comment:17 leif]:\n> > > I wouldn't call `sage` in `sage-upgrade`. \n> > \n> > I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,\n> \n> `sage-upgrade` isn't \"the end\" of the upgrade process (it's called by `sage-sage`),\n> and calling the \"new\" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.\n> \n> > after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.\n> \n> This is done later\n\nWhere?  sage-upgrade gets called twice in sage-sage, but that's basically all that happens when you run \"sage -upgrade\", isn't it?  I guess running it twice means that VERSION.txt may end up being wrong; I'll have to fix that.\n\n> , and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.\n> \n> > > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.\n> > \n> > Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.\n> \n> I didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (*not* in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.\n\nVERSION.txt is written to SAGE_ROOT by sage-sdist, so it's present in the Sage tarball.  It will therefore also be available in the upgrade path.\n\n> > I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.\n> \n> See above.\n> \n> > If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.\n> \n> Well, `VERSION.txt` shouldn't be under revision control.\n>  \n> > > As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).\n> > \n> > Right.\n> > \n> > > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)\n> > \n> > How about extracting it from VERSION.txt?\n> \n> Extracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.\n\nAlthough we can't get the release date from it, we could also use the *file name* for the main Sage repo, for example.\n\n> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.\n> \n> I'll take a look at it.\n\nReplying to [comment:25 leif]:\n> Ok, if we supply a separate file in the upgrade path. \n\n(See above: the file VERSION.txt gets written to SAGE_ROOT by sage-sdist, so it will be there.)\n\n> The code is a *bit* complicated though.\n\nIt's straightforward, but long: first you extract the old version from VERSION.txt, then you download the new VERSION.txt and extract the new version, then you produce the updated VERSION.txt.  I need to check whether the new version matches the beginning of the old version, in case this is the second time sage-upgrade is run.  \n\nFinally, I think having \"UTC\" at the end of the date looks a little silly when it's just a date, no time, but I've included it.\n\nHere's a new patch.",
    "created_at": "2010-09-30T15:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90128",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:23 leif]:
> Replying to [comment:20 jhpalmieri]:
> > Replying to [comment:17 leif]:
> > > I wouldn't call `sage` in `sage-upgrade`. 
> > 
> > I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,
> 
> `sage-upgrade` isn't "the end" of the upgrade process (it's called by `sage-sage`),
> and calling the "new" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.
> 
> > after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.
> 
> This is done later

Where?  sage-upgrade gets called twice in sage-sage, but that's basically all that happens when you run "sage -upgrade", isn't it?  I guess running it twice means that VERSION.txt may end up being wrong; I'll have to fix that.

> , and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.
> 
> > > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.
> > 
> > Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.
> 
> I didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (*not* in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.

VERSION.txt is written to SAGE_ROOT by sage-sdist, so it's present in the Sage tarball.  It will therefore also be available in the upgrade path.

> > I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.
> 
> See above.
> 
> > If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.
> 
> Well, `VERSION.txt` shouldn't be under revision control.
>  
> > > As noted, the version file should be updated *before* `spkg/install` is called (and that's also before a new scripts spkg gets installed).
> > 
> > Right.
> > 
> > > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)
> > 
> > How about extracting it from VERSION.txt?
> 
> Extracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.

Although we can't get the release date from it, we could also use the *file name* for the main Sage repo, for example.

> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.
> 
> I'll take a look at it.

Replying to [comment:25 leif]:
> Ok, if we supply a separate file in the upgrade path. 

(See above: the file VERSION.txt gets written to SAGE_ROOT by sage-sdist, so it will be there.)

> The code is a *bit* complicated though.

It's straightforward, but long: first you extract the old version from VERSION.txt, then you download the new VERSION.txt and extract the new version, then you produce the updated VERSION.txt.  I need to check whether the new version matches the beginning of the old version, in case this is the second time sage-upgrade is run.  

Finally, I think having "UTC" at the end of the date looks a little silly when it's just a date, no time, but I've included it.

Here's a new patch.



---

archive/issue_comments_090129.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-11T20:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90129",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090130.json:
```json
{
    "body": "This needs to be rebased (and perhaps coordinated with #9433?):\n\n```\npatching file sage-make_devel_packages\npatching file sage-sdist\npatching file sage-spkg\npatching file sage-update\nHunk #1 succeeded at 344 (offset 35 lines).\nHunk #2 FAILED at 380.\n1 out of 2 hunks FAILED -- saving rejects to file sage-update.rej\npatching file sage-upgrade\nHunk #1 succeeded at 35 (offset 4 lines).\n```\n",
    "created_at": "2010-11-11T20:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90130",
    "user": "https://github.com/jdemeyer"
}
```

This needs to be rebased (and perhaps coordinated with #9433?):

```
patching file sage-make_devel_packages
patching file sage-sdist
patching file sage-spkg
patching file sage-update
Hunk #1 succeeded at 344 (offset 35 lines).
Hunk #2 FAILED at 380.
1 out of 2 hunks FAILED -- saving rejects to file sage-update.rej
patching file sage-upgrade
Hunk #1 succeeded at 35 (offset 4 lines).
```




---

archive/issue_comments_090131.json:
```json
{
    "body": "Attachment [trac_9434-VERSION.txt.v2.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION.txt.v2.patch) by @jhpalmieri created at 2010-11-11 21:00:41\n\nversion 2: replaces earlier patch. scripts repo",
    "created_at": "2010-11-11T21:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90131",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9434-VERSION.txt.v2.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION.txt.v2.patch) by @jhpalmieri created at 2010-11-11 21:00:41

version 2: replaces earlier patch. scripts repo



---

archive/issue_comments_090132.json:
```json
{
    "body": "Here's a rebased version.  As far as coordinating with #9433, some rebasing may be required, and I can add \"VERSION.txt\" to the .hgignore file in the new Sage repo.  I'll make the change to .hgignore now, but I'm going to wait for any rebasing until one or the other ticket has at least a positive review.",
    "created_at": "2010-11-11T21:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90132",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a rebased version.  As far as coordinating with #9433, some rebasing may be required, and I can add "VERSION.txt" to the .hgignore file in the new Sage repo.  I'll make the change to .hgignore now, but I'm going to wait for any rebasing until one or the other ticket has at least a positive review.



---

archive/issue_comments_090133.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-11T21:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90133",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090134.json:
```json
{
    "body": "Replying to [comment:28 jhpalmieri]:\n> Finally, I think having \"UTC\" at the end of the date looks a little silly when it's just a date, no time.\n\nI agree, this should be removed.  This just looks so strange:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage:\n```\n\n| Sage Version 4.6.1.alpha3, Release Date: 2010-11-26 UTC            |\n| Type notebook() for the GUI, and license() for information.        |\nThe patch looks okay to me (apart from this minor UTC issue).  I will do some more testing (also upgrade).",
    "created_at": "2010-11-26T12:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90134",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:28 jhpalmieri]:
> Finally, I think having "UTC" at the end of the date looks a little silly when it's just a date, no time.

I agree, this should be removed.  This just looks so strange:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:
```

| Sage Version 4.6.1.alpha3, Release Date: 2010-11-26 UTC            |
| Type notebook() for the GUI, and license() for information.        |
The patch looks okay to me (apart from this minor UTC issue).  I will do some more testing (also upgrade).



---

archive/issue_comments_090135.json:
```json
{
    "body": "Attachment [9434_no_UTC.patch](tarball://root/attachments/some-uuid/ticket9434/9434_no_UTC.patch) by @jdemeyer created at 2010-11-26 22:42:45\n\nReviewer scripts patch, apply on top of previous",
    "created_at": "2010-11-26T22:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90135",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9434_no_UTC.patch](tarball://root/attachments/some-uuid/ticket9434/9434_no_UTC.patch) by @jdemeyer created at 2010-11-26 22:42:45

Reviewer scripts patch, apply on top of previous



---

archive/issue_comments_090136.json:
```json
{
    "body": "Changing keywords from \"\" to \"scripts VERSION.txt\".",
    "created_at": "2010-11-26T22:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90136",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "scripts VERSION.txt".



---

archive/issue_comments_090137.json:
```json
{
    "body": "positive_review to everything except for my patch.",
    "created_at": "2010-11-26T22:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90137",
    "user": "https://github.com/jdemeyer"
}
```

positive_review to everything except for my patch.



---

archive/issue_comments_090138.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-27T00:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90138",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090139.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> positive_review to everything except for my patch.\n\nI'm giving a positive review to your patch, and so setting this to positive review.",
    "created_at": "2010-11-27T00:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90139",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:32 jdemeyer]:
> positive_review to everything except for my patch.

I'm giving a positive review to your patch, and so setting this to positive review.



---

archive/issue_comments_090140.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-02T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90140",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009589.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-02T16:09:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9434#event-9589"
}
```



---

archive/issue_comments_090141.json:
```json
{
    "body": "I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.",
    "created_at": "2010-12-08T17:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90141",
    "user": "https://github.com/qed777"
}
```

I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.



---

archive/issue_comments_090142.json:
```json
{
    "body": "Replying to [comment:35 mpatel]:\n> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.\n\nDoes `download_file(\"VERSION.txt\")` attempt to download a non-existent file, e.g.,\n\n http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt\n\n?  The successful upgrades I've done from 4.6 to 4.6.1.alpha3 somehow avoid this problem --- after the upgrade, `SAGE_ROOT` does not contain a `VERSION.txt`.  But upgrades that failed I cannot resume:\n\n```\n$ ./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3\n[...]\nhttp://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt --> VERSION.txt [.]\nFailed to download 'http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt'.\nAbort.\n$ \n```\n",
    "created_at": "2010-12-14T04:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90142",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:35 mpatel]:
> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.

Does `download_file("VERSION.txt")` attempt to download a non-existent file, e.g.,

 http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt

?  The successful upgrades I've done from 4.6 to 4.6.1.alpha3 somehow avoid this problem --- after the upgrade, `SAGE_ROOT` does not contain a `VERSION.txt`.  But upgrades that failed I cannot resume:

```
$ ./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3
[...]
http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt --> VERSION.txt [.]
Failed to download 'http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt'.
Abort.
$ 
```




---

archive/issue_comments_090143.json:
```json
{
    "body": "> Does download_file(\"VERSION.txt\") attempt to download a non-existent file\n\nI think that might be the problem.  I thought we tested this with upgrades, but obviously not well enough.  How about a patch like this:\n\n```diff\ndiff -r 6e07658dbbd6 -r b35cea7f82c9 sage-sdist\n--- a/sage-sdist\n+++ b/sage-sdist\n@@ -58,6 +58,9 @@ cp -LRp Makefile *.txt *.sage sage ipyth\n STD=standard\n mkdir $TMP/$PKGDIR\n mkdir $TMP/$PKGDIR/$STD\n+# Put VERSION.txt in a directory available for download during the\n+# update process.  (See sage-update.)\n+cp VERSION.txt $TMP/$PKGDIR/$STD/.VERSION.txt\n cp -p $PKGDIR/$STD/deps $TMP/$PKGDIR/$STD/\n cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/\n cp -p $PKGDIR/$STD/newest_version $TMP/$PKGDIR/$STD/\ndiff -r 6e07658dbbd6 -r b35cea7f82c9 sage-update\n--- a/sage-update\n+++ b/sage-update\n@@ -351,11 +351,16 @@ def do_update():\n         version_file.close()\n     else:\n         old_version = \"\"\n-    download_file(\"VERSION.txt\")\n-    version_file = open(\"VERSION.txt\")\n+    download_file(\"standard/.VERSION.txt\")\n+    version_file = open(\".VERSION.txt\")\n     new_version = version_file.read()\n     new_version = new_version.strip()  # remove trailing newline\n     version_file.close()\n+    try:\n+        os.remove(os.path.join(SPKG_ROOT, \"standard\", \".VERSION.txt\"))\n+    except OSError:\n+        pass\n+    os.rename(\".VERSION.txt\", os.path.join(SPKG_ROOT, \"standard\", \".VERSION.txt\"))\n     # sage-upgrade, hence sage-update, gets run twice during the\n     # upgrade process.  If old_version starts with new_version, then\n     # this should be the second time through, so don't update the\n```\n\n(The \"try ... except\" block is probably not necessary except on Windows, but it feels safer this way, and who knows, we might eventually support Windows.)\n\nI've created two upgrade paths which include this (one, version \"V0\", to test upgrading from anything else to this, and then the second, version \"V1\", to try upgrading from version \"V0\"):\n\n- [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/)\n- [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/)\n\nWe can open up a new ticket with a formally attached patch if this seems like the right approach.  I won't have much time to work on this, though: I have to focus on grading exams and getting ready for next quarter's classes.",
    "created_at": "2010-12-14T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90143",
    "user": "https://github.com/jhpalmieri"
}
```

> Does download_file("VERSION.txt") attempt to download a non-existent file

I think that might be the problem.  I thought we tested this with upgrades, but obviously not well enough.  How about a patch like this:

```diff
diff -r 6e07658dbbd6 -r b35cea7f82c9 sage-sdist
--- a/sage-sdist
+++ b/sage-sdist
@@ -58,6 +58,9 @@ cp -LRp Makefile *.txt *.sage sage ipyth
 STD=standard
 mkdir $TMP/$PKGDIR
 mkdir $TMP/$PKGDIR/$STD
+# Put VERSION.txt in a directory available for download during the
+# update process.  (See sage-update.)
+cp VERSION.txt $TMP/$PKGDIR/$STD/.VERSION.txt
 cp -p $PKGDIR/$STD/deps $TMP/$PKGDIR/$STD/
 cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/
 cp -p $PKGDIR/$STD/newest_version $TMP/$PKGDIR/$STD/
diff -r 6e07658dbbd6 -r b35cea7f82c9 sage-update
--- a/sage-update
+++ b/sage-update
@@ -351,11 +351,16 @@ def do_update():
         version_file.close()
     else:
         old_version = ""
-    download_file("VERSION.txt")
-    version_file = open("VERSION.txt")
+    download_file("standard/.VERSION.txt")
+    version_file = open(".VERSION.txt")
     new_version = version_file.read()
     new_version = new_version.strip()  # remove trailing newline
     version_file.close()
+    try:
+        os.remove(os.path.join(SPKG_ROOT, "standard", ".VERSION.txt"))
+    except OSError:
+        pass
+    os.rename(".VERSION.txt", os.path.join(SPKG_ROOT, "standard", ".VERSION.txt"))
     # sage-upgrade, hence sage-update, gets run twice during the
     # upgrade process.  If old_version starts with new_version, then
     # this should be the second time through, so don't update the
```

(The "try ... except" block is probably not necessary except on Windows, but it feels safer this way, and who knows, we might eventually support Windows.)

I've created two upgrade paths which include this (one, version "V0", to test upgrading from anything else to this, and then the second, version "V1", to try upgrading from version "V0"):

- [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/)
- [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/)

We can open up a new ticket with a formally attached patch if this seems like the right approach.  I won't have much time to work on this, though: I have to focus on grading exams and getting ready for next quarter's classes.



---

archive/issue_comments_090144.json:
```json
{
    "body": "(This patch is to be applied on top of 4.6.1.alpha3.)",
    "created_at": "2010-12-14T06:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90144",
    "user": "https://github.com/jhpalmieri"
}
```

(This patch is to be applied on top of 4.6.1.alpha3.)



---

archive/issue_comments_090145.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-12-14T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90145",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_090146.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-12-14T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90146",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_009590.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-14T08:13:07Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9434#event-9590"
}
```



---

archive/issue_comments_090147.json:
```json
{
    "body": "Reopening this because of the issue mentioned.",
    "created_at": "2010-12-14T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90147",
    "user": "https://github.com/jdemeyer"
}
```

Reopening this because of the issue mentioned.



---

archive/issue_comments_090148.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2010-12-14T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90148",
    "user": "https://github.com/jdemeyer"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_090149.json:
```json
{
    "body": "Using `download_file(\"../VERSION.txt\")` may also work (I've tested this only once).\n\nFor me, the upgrades that failed were parallel spkg builds.  But some parallel spkg upgrades did \"succeed,\" i.e., modulo SageNB not being upgraded.  (Were there any other packages not upgraded?)\nAll purely serial and parallel-only-within-spkg upgrades \"succeeded.\"\n\nCould when the new `sage_scripts` package is installed matter for either the `VERSION.txt` discrepancy or the apparently separate SageNB problem?",
    "created_at": "2010-12-14T15:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90149",
    "user": "https://github.com/qed777"
}
```

Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

For me, the upgrades that failed were parallel spkg builds.  But some parallel spkg upgrades did "succeed," i.e., modulo SageNB not being upgraded.  (Were there any other packages not upgraded?)
All purely serial and parallel-only-within-spkg upgrades "succeeded."

Could when the new `sage_scripts` package is installed matter for either the `VERSION.txt` discrepancy or the apparently separate SageNB problem?



---

archive/issue_comments_090150.json:
```json
{
    "body": "Replying to [comment:40 mpatel]:\n> Using `download_file(\"../VERSION.txt\")` may also work (I've tested this only once).\n\nIf that's true, it's probably a better solution (but it needs to be tested properly).",
    "created_at": "2010-12-14T16:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90150",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:40 mpatel]:
> Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

If that's true, it's probably a better solution (but it needs to be tested properly).



---

archive/issue_comments_090151.json:
```json
{
    "body": "Replying to [comment:40 mpatel]:\n> Using `download_file(\"../VERSION.txt\")` may also work (I've tested this only once).\n\nI would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like \"http://boxen.math.washington.edu/sage/spkg/../COPYING.txt\", the file is not found.  I think the same would be true of VERSION.txt: I don't think the top-level directory is available on the official Sage mirrors.",
    "created_at": "2010-12-14T18:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90151",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:40 mpatel]:
> Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

I would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like "http://boxen.math.washington.edu/sage/spkg/../COPYING.txt", the file is not found.  I think the same would be true of VERSION.txt: I don't think the top-level directory is available on the official Sage mirrors.



---

archive/issue_comments_090152.json:
```json
{
    "body": "Replying to [comment:42 jhpalmieri]:\n> Replying to [comment:40 mpatel]:\n> > Using `download_file(\"../VERSION.txt\")` may also work (I've tested this only once).\n> \n> I would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like \"http://boxen.math.washington.edu/sage/spkg/../COPYING.txt\", the file is not found.\n\nWell, the file is not found because it doesn't actually exist.  So your comment doesn't really prove anything.",
    "created_at": "2010-12-14T19:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90152",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:40 mpatel]:
> > Using `download_file("../VERSION.txt")` may also work (I've tested this only once).
> 
> I would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like "http://boxen.math.washington.edu/sage/spkg/../COPYING.txt", the file is not found.

Well, the file is not found because it doesn't actually exist.  So your comment doesn't really prove anything.



---

archive/issue_comments_090153.json:
```json
{
    "body": "I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.",
    "created_at": "2010-12-14T19:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90153",
    "user": "https://github.com/jdemeyer"
}
```

I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.



---

archive/issue_comments_090154.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-12-14T19:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90154",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_090155.json:
```json
{
    "body": "Replying to [comment:44 jdemeyer]:\n> I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.\n\nI think that on the official Sage mirrors, none of the top-level files (makefile or Makefile, COPYING.txt, etc.) are available for download via the URLs in the sage-update script.  So if we have VERSION.txt only in the top-level, it won't be available for download (unless the scripts which make the official release available are rewritten). That is, after Sage 4.6.1 is released, running \"sage -upgrade\" with no arguments will fail to download VERSION.txt because that file won't be anywhere on the server.\n\nI could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...",
    "created_at": "2010-12-14T19:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90155",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:44 jdemeyer]:
> I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.

I think that on the official Sage mirrors, none of the top-level files (makefile or Makefile, COPYING.txt, etc.) are available for download via the URLs in the sage-update script.  So if we have VERSION.txt only in the top-level, it won't be available for download (unless the scripts which make the official release available are rewritten). That is, after Sage 4.6.1 is released, running "sage -upgrade" with no arguments will fail to download VERSION.txt because that file won't be anywhere on the server.

I could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...



---

archive/issue_comments_090156.json:
```json
{
    "body": "Here is the patch quoted above.  I think this will work, and I don't think that downloading \"../VERSION.txt\" will.  I'm marking it as needing review, but if anyone wants to try a different approach, please go ahead.",
    "created_at": "2010-12-14T19:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90156",
    "user": "https://github.com/jhpalmieri"
}
```

Here is the patch quoted above.  I think this will work, and I don't think that downloading "../VERSION.txt" will.  I'm marking it as needing review, but if anyone wants to try a different approach, please go ahead.



---

archive/issue_comments_090157.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-14T19:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90157",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090158.json:
```json
{
    "body": "Replying to [comment:45 jhpalmieri]:\n> I could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...\n\nDoes this mean that `Makefile` will never get upgraded?  That doesn't sound good, especially given #9799, #10156.",
    "created_at": "2010-12-14T20:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90158",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:45 jhpalmieri]:
> I could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...

Does this mean that `Makefile` will never get upgraded?  That doesn't sound good, especially given #9799, #10156.



---

archive/issue_comments_090159.json:
```json
{
    "body": "Well, I think `Makefile` never gets run during an upgrade, so while it doesn't get upgraded, that doesn't affect the upgrade process.  I suppose if someone ran \"sage -upgrade ...\" and then did \"make clean\" and \"make\", it would use the old version of `Makefile` (or `makefile`), but the spkgs should be up to date.  (This is yet another reason to work on getting #9433 merged...)",
    "created_at": "2010-12-14T23:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90159",
    "user": "https://github.com/jhpalmieri"
}
```

Well, I think `Makefile` never gets run during an upgrade, so while it doesn't get upgraded, that doesn't affect the upgrade process.  I suppose if someone ran "sage -upgrade ..." and then did "make clean" and "make", it would use the old version of `Makefile` (or `makefile`), but the spkgs should be up to date.  (This is yet another reason to work on getting #9433 merged...)



---

archive/issue_comments_090160.json:
```json
{
    "body": "Replying to [comment:35 mpatel]:\n> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.\n\nJust for the record (from IRC):\n\n```\n<kini>\n  er... I just ran `sage -upgrade` (from 4.6) to see if it would pull a development version\n  - sage told me that everything was already upgraded, and it exited without seeming to do\n  anything but now when I load sage it's telling me I have 4.6.rc0\n  odd\n  curiouser and curiouser\n  sage.misc.banner.banner() returns the correct, 4.6 banner\n  ... hm\n  so apparently `sage -version` just cats a text file,  $SAGE_ROOT/local/bin/sage-banner\n  odd, my $SAGE_ROOT/local/bin repository's files are for some reason marked as descended\n  from 4.6.rc0\n  well, never mind\n```\n\n\n8)",
    "created_at": "2010-12-16T03:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90160",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:35 mpatel]:
> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a *possible* problem involving `VERSION.txt` and failed upgrades.

Just for the record (from IRC):

```
<kini>
  er... I just ran `sage -upgrade` (from 4.6) to see if it would pull a development version
  - sage told me that everything was already upgraded, and it exited without seeming to do
  anything but now when I load sage it's telling me I have 4.6.rc0
  odd
  curiouser and curiouser
  sage.misc.banner.banner() returns the correct, 4.6 banner
  ... hm
  so apparently `sage -version` just cats a text file,  $SAGE_ROOT/local/bin/sage-banner
  odd, my $SAGE_ROOT/local/bin repository's files are for some reason marked as descended
  from 4.6.rc0
  well, never mind
```


8)



---

archive/issue_comments_090161.json:
```json
{
    "body": "1) Why not rename/copy the file \"SAGE_ROOT/spkg/standard/.VERSION.txt\" to \"SAGE_ROOT/VERSION.txt\" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.\n\n2) I would *not* make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.\n\n3) I would copy using `cp -p`.",
    "created_at": "2010-12-16T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90161",
    "user": "https://github.com/jdemeyer"
}
```

1) Why not rename/copy the file "SAGE_ROOT/spkg/standard/.VERSION.txt" to "SAGE_ROOT/VERSION.txt" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.

2) I would *not* make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.

3) I would copy using `cp -p`.



---

archive/issue_comments_090162.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-16T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90162",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090163.json:
```json
{
    "body": "Replying to [comment:50 jdemeyer]:\n> 1) Why not rename/copy the file \"SAGE_ROOT/spkg/standard/.VERSION.txt\" to \"SAGE_ROOT/VERSION.txt\" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.\n\nI agree that the top-level VERSION.txt should be the same as spkg/standard/VERSION.txt, which was not the case in my previous patch.  I've fixed that so that once the top-level file is created, it's copied to spkg/standard.  (The top-level file contains upgrade information, and since upgrade info may be helpful in tracking down problems, we should keep that one rather than the downloaded one.)\n\n> 2) I would *not* make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.\n\nOkay.\n \n> 3) I would copy using `cp -p`.\n\nGood idea.\n\nI'm attaching two patches, one of which just fixes these issues.  The other patch, which could be applied on top of the others, does a little miscellaneous clean-up in sage-update, using `os.path.join(x,y)` instead of `\"%s/%s\" %(x,y)`.  Feel free to ignore the second patch completely; it is entirely optional right now.",
    "created_at": "2010-12-16T21:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90163",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:50 jdemeyer]:
> 1) Why not rename/copy the file "SAGE_ROOT/spkg/standard/.VERSION.txt" to "SAGE_ROOT/VERSION.txt" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.

I agree that the top-level VERSION.txt should be the same as spkg/standard/VERSION.txt, which was not the case in my previous patch.  I've fixed that so that once the top-level file is created, it's copied to spkg/standard.  (The top-level file contains upgrade information, and since upgrade info may be helpful in tracking down problems, we should keep that one rather than the downloaded one.)

> 2) I would *not* make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.

Okay.
 
> 3) I would copy using `cp -p`.

Good idea.

I'm attaching two patches, one of which just fixes these issues.  The other patch, which could be applied on top of the others, does a little miscellaneous clean-up in sage-update, using `os.path.join(x,y)` instead of `"%s/%s" %(x,y)`.  Feel free to ignore the second patch completely; it is entirely optional right now.



---

archive/issue_comments_090164.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-16T21:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90164",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090165.json:
```json
{
    "body": "Attachment [trac_9434-VERSION-update.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION-update.patch) by @jhpalmieri created at 2010-12-16 21:26:11\n\nscripts repo; apply on top of other patches",
    "created_at": "2010-12-16T21:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90165",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9434-VERSION-update.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-VERSION-update.patch) by @jhpalmieri created at 2010-12-16 21:26:11

scripts repo; apply on top of other patches



---

archive/issue_comments_090166.json:
```json
{
    "body": "Attachment [trac_9434-os.path.join.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-os.path.join.patch) by @jhpalmieri created at 2010-12-16 21:27:08\n\nscripts repo; this patch is optional, so reviewing it should have lower priority",
    "created_at": "2010-12-16T21:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90166",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9434-os.path.join.patch](tarball://root/attachments/some-uuid/ticket9434/trac_9434-os.path.join.patch) by @jhpalmieri created at 2010-12-16 21:27:08

scripts repo; this patch is optional, so reviewing it should have lower priority



---

archive/issue_comments_090167.json:
```json
{
    "body": "The patches look good to me, but I need to do more testing before this can get positive review.",
    "created_at": "2010-12-17T14:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90167",
    "user": "https://github.com/jdemeyer"
}
```

The patches look good to me, but I need to do more testing before this can get positive review.



---

archive/issue_comments_090168.json:
```json
{
    "body": "I just created new upgrade paths for further testing: I took a vanilla version of 4.6.1.alpha3 and applied \"trac_9434-VERSION-update.patch\", then did \"./sage -sdist 4.6.1.V0\" and \"./sage -sdist 4.6.1.V1\".  Then I applied \"trac_9434-os.path.join.patch\" and did \"./sage -sdist 4.6.1.W0\" and \"./sage -sdist 4.6.1.W1\".  The resulting upgrade paths are\n\n-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/\n-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/\n-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W0/  (with os.path.join patch)\n-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W1/  (with os.path.join patch)",
    "created_at": "2010-12-17T16:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90168",
    "user": "https://github.com/jhpalmieri"
}
```

I just created new upgrade paths for further testing: I took a vanilla version of 4.6.1.alpha3 and applied "trac_9434-VERSION-update.patch", then did "./sage -sdist 4.6.1.V0" and "./sage -sdist 4.6.1.V1".  Then I applied "trac_9434-os.path.join.patch" and did "./sage -sdist 4.6.1.W0" and "./sage -sdist 4.6.1.W1".  The resulting upgrade paths are

-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/
-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/
-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W0/  (with os.path.join patch)
-  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W1/  (with os.path.join patch)



---

archive/issue_comments_090169.json:
```json
{
    "body": "I'm also testing with the upgrade path [http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/](http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/) (including also other tickets such as #10176).\n\nI currently get the following problem (building an \"nameless\" package), still investigating:\n\n```\n/mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/pipestatus \"sage-spkg ${SAGE_SPKG_OPTS}  2>&1\" \"tee -a /mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/logs/.log\"\n```\n",
    "created_at": "2010-12-18T09:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90169",
    "user": "https://github.com/jdemeyer"
}
```

I'm also testing with the upgrade path [http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/](http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/) (including also other tickets such as #10176).

I currently get the following problem (building an "nameless" package), still investigating:

```
/mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/pipestatus "sage-spkg ${SAGE_SPKG_OPTS}  2>&1" "tee -a /mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/logs/.log"
```




---

archive/issue_comments_090170.json:
```json
{
    "body": "Looks good to me (\"merged\" changed to rc0 because there is an additional patch).",
    "created_at": "2010-12-19T09:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90170",
    "user": "https://github.com/jdemeyer"
}
```

Looks good to me ("merged" changed to rc0 because there is an additional patch).



---

archive/issue_events_009591.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-19T09:33:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9434#event-9591"
}
```



---

archive/issue_comments_090171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-19T09:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9434#issuecomment-90171",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
