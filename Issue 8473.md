# Issue 8473: Make .sws files clickable

archive/issues_008473.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt would be great for those of us who have installed Sage to be able\nto double click on these files and have sage open them in the\nnotebook.\n\nSupoorting a command on the likes of\n\n```\nsage -notebook /path/to/worksheet.sws\n```\n\nwould be a very good step in this direction\n\nIssue created by migration from https://trac.sagemath.org/ticket/8473\n\n",
    "created_at": "2010-03-07T04:15:40Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make .sws files clickable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8473",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: @williamstein

It would be great for those of us who have installed Sage to be able
to double click on these files and have sage open them in the
notebook.

Supoorting a command on the likes of

```
sage -notebook /path/to/worksheet.sws
```

would be a very good step in this direction

Issue created by migration from https://trac.sagemath.org/ticket/8473





---

archive/issue_comments_076186.json:
```json
{
    "body": "Ticket #693 is related.",
    "created_at": "2010-03-08T00:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76186",
    "user": "https://github.com/qed777"
}
```

Ticket #693 is related.



---

archive/issue_comments_076187.json:
```json
{
    "body": "What would be needed for this?  #693 shows that it's possible to know whether the notebook is running and then open the browser or not based on this.  And `http://foo.sagenb.org/home/me/upload_worksheet` shows that there is a script to take a .sws file and send it straight to the browser.    So I say this is definitely doable by someone who knows these scripts.  Is this right?",
    "created_at": "2010-09-08T15:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76187",
    "user": "https://github.com/kcrisman"
}
```

What would be needed for this?  #693 shows that it's possible to know whether the notebook is running and then open the browser or not based on this.  And `http://foo.sagenb.org/home/me/upload_worksheet` shows that there is a script to take a .sws file and send it straight to the browser.    So I say this is definitely doable by someone who knows these scripts.  Is this right?



---

archive/issue_comments_076188.json:
```json
{
    "body": "This also led to the following - #9875.",
    "created_at": "2010-09-08T15:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76188",
    "user": "https://github.com/kcrisman"
}
```

This also led to the following - #9875.



---

archive/issue_comments_076189.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-29T12:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76189",
    "user": "https://github.com/gvol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076190.json:
```json
{
    "body": "Depends on #693\n\nI have added support for uploading from a file:// url in order to support `sage --notebook upload=FILE.sws`.  The sagenb patch allows this, and the extcode patch adds support to the Mac application.  I had to support file urls so that the upload url could be given as a GET rather than a POST request, and hence be passed to any browser.\n\nThe Mac app has a new option to automatically start the server when a sws file is opened.  I'm not sure anyone would ever want to turn this off, so I can remove it if it's not useful.",
    "created_at": "2010-12-29T12:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76190",
    "user": "https://github.com/gvol"
}
```

Depends on #693

I have added support for uploading from a file:// url in order to support `sage --notebook upload=FILE.sws`.  The sagenb patch allows this, and the extcode patch adds support to the Mac application.  I had to support file urls so that the upload url could be given as a GET rather than a POST request, and hence be passed to any browser.

The Mac app has a new option to automatically start the server when a sws file is opened.  I'm not sure anyone would ever want to turn this off, so I can remove it if it's not useful.



---

archive/issue_comments_076191.json:
```json
{
    "body": "I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.",
    "created_at": "2010-12-29T12:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76191",
    "user": "https://github.com/gvol"
}
```

I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.



---

archive/issue_comments_076192.json:
```json
{
    "body": "Changing assignee from @williamstein to @gvol.",
    "created_at": "2010-12-29T12:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76192",
    "user": "https://github.com/gvol"
}
```

Changing assignee from @williamstein to @gvol.



---

archive/issue_comments_076193.json:
```json
{
    "body": "Replying to [comment:6 iandrus]:\n> I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.\n\nBut I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...",
    "created_at": "2010-12-29T17:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76193",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:6 iandrus]:
> I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.

But I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...



---

archive/issue_comments_076194.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Replying to [comment:6 iandrus]:\n> > I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.\n\n> But I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...\n\nI was probably unclear.  With a file url, it would grab the file from the server rather than the local machine, so it's probably not what people want or expect at all.  e.g. if you try to upload file:///home/iandrus/sage/sws1.sws, this will only work if the machine the server is running on also has a file at /home/iandrus/sage/sws1.sws, and then only if the file is the same.  \n\nIt might be nice to add some way to upload a file to a remote server programmatically, but I think that entails logging in and then sending off a POST request from a script, so it has a different feel.  I tried writing a simple script using curl a while ago, but I couldn't get it to work for some reason.  Perhaps someone knows of a better/different way to accomplish it.\n\nYou are right about the security hole though, it's probably the least of our worries :-)",
    "created_at": "2010-12-29T17:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76194",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:7 kcrisman]:
> Replying to [comment:6 iandrus]:
> > I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.

> But I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...

I was probably unclear.  With a file url, it would grab the file from the server rather than the local machine, so it's probably not what people want or expect at all.  e.g. if you try to upload file:///home/iandrus/sage/sws1.sws, this will only work if the machine the server is running on also has a file at /home/iandrus/sage/sws1.sws, and then only if the file is the same.  

It might be nice to add some way to upload a file to a remote server programmatically, but I think that entails logging in and then sending off a POST request from a script, so it has a different feel.  I tried writing a simple script using curl a while ago, but I couldn't get it to work for some reason.  Perhaps someone knows of a better/different way to accomplish it.

You are right about the security hole though, it's probably the least of our worries :-)



---

archive/issue_comments_076195.json:
```json
{
    "body": "Attachment [trac_8473-sagenb.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-sagenb.patch) by @gvol created at 2011-01-04 14:36:47",
    "created_at": "2011-01-04T14:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76195",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_8473-sagenb.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-sagenb.patch) by @gvol created at 2011-01-04 14:36:47



---

archive/issue_comments_076196.json:
```json
{
    "body": "Added urlencoding so that files with special characters will work okay.",
    "created_at": "2011-01-04T14:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76196",
    "user": "https://github.com/gvol"
}
```

Added urlencoding so that files with special characters will work okay.



---

archive/issue_comments_076197.json:
```json
{
    "body": "I'd like to test this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at # 693.  Bug days folks?",
    "created_at": "2011-01-11T04:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76197",
    "user": "https://github.com/kcrisman"
}
```

I'd like to test this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at # 693.  Bug days folks?



---

archive/issue_comments_076198.json:
```json
{
    "body": "Attachment [trac_8473-extcode.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-extcode.patch) by @gvol created at 2011-03-12 16:28:44\n\nI added zip and txt files to the Mac App as well as support (icons etc.) for Cython files.",
    "created_at": "2011-03-12T16:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76198",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_8473-extcode.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-extcode.patch) by @gvol created at 2011-03-12 16:28:44

I added zip and txt files to the Mac App as well as support (icons etc.) for Cython files.



---

archive/issue_comments_076199.json:
```json
{
    "body": "I can taste it now that you reviewed #693.    This is great stuff, good work.\n\nOkay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  \n\nI also have a couple questions, but they just indicate my lack of knowledge. \n* I don't understand this change.  More precisely, we now have the default `startpath = ''`, but that isn't the same as `\\`.  Will that matter somewhere for non-uploading situations?\n\n```\n                        browse_to(old_interface, old_port, old_secure, '/') \n                        browse_to(old_interface, old_port, old_secure, startpath)\n```\n* You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.\n* Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\\ sheet.sws'\n* I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!\n\nI'd be inclined to separate the new notebook functionality from adding clickable sws files to the Sage App, for review purposes but also because this would have to be part of a new SageNB package, and it would be nice to separate those things out.  The logistics are already complicated enough for things.",
    "created_at": "2011-03-25T03:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76199",
    "user": "https://github.com/kcrisman"
}
```

I can taste it now that you reviewed #693.    This is great stuff, good work.

Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  

I also have a couple questions, but they just indicate my lack of knowledge. 
* I don't understand this change.  More precisely, we now have the default `startpath = ''`, but that isn't the same as `\`.  Will that matter somewhere for non-uploading situations?

```
                        browse_to(old_interface, old_port, old_secure, '/') 
                        browse_to(old_interface, old_port, old_secure, startpath)
```
* You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.
* Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\ sheet.sws'
* I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!

I'd be inclined to separate the new notebook functionality from adding clickable sws files to the Sage App, for review purposes but also because this would have to be part of a new SageNB package, and it would be nice to separate those things out.  The logistics are already complicated enough for things.



---

archive/issue_comments_076200.json:
```json
{
    "body": "This doesn't even work - it asks for a password:\n\n```\nnotebook(r'''/Users/.../MAT338Day1-2011.sws''',require_login=False)\n```\nwhile `notebook()` continues to work fine.  I would view this as a bug in the case of this syntax.",
    "created_at": "2011-03-25T03:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76200",
    "user": "https://github.com/kcrisman"
}
```

This doesn't even work - it asks for a password:

```
notebook(r'''/Users/.../MAT338Day1-2011.sws''',require_login=False)
```
while `notebook()` continues to work fine.  I would view this as a bug in the case of this syntax.



---

archive/issue_comments_076201.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-25T03:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76201",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076202.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> I can taste it now that you reviewed #693.    This is great stuff, good work.\n\n\n:-)\n\n> Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  \n\n\nGood point.  I have added documentation for `notebook?`.  Does it need documentation in `sage --advanced` as well?\n\n> I also have a couple questions, but they just indicate my lack of knowledge. \n> * I don't understand this change.  More precisely, we now have the default `startpath = ''`, but that isn't the same as `\\`.  Will that matter somewhere for non-uploading situations?\n> \n> ```\n>                         browse_to(old_interface, old_port, old_secure, '/') \n>                         browse_to(old_interface, old_port, old_secure, startpath)\n> ```\n\n\nI don't think that should matter, but I changed it to `'/'` since it makes more sense.  In an earlier version of the patch I think I appended to `startpath` and that's why it was empty.\n\n>  * You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.\n\n\nYou are right, there was a bug there.  I need it both places.  Thanks.\n\n>  * Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\\ sheet.sws'\n\n\nYes.  They have to be escaped for the shell so that they appear as one argument.  That's the same as any argument to `sage -n`.  However, I should point out that the syntax is `sage -n upload=\"/path/to work sheet.sws\"`.  I guess that's why we need documentation, eh? :-)\n\n>  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!\n\n\nI think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.\n\n> I'd be inclined to separate the new notebook functionality from adding clickable sws files to the Sage App, for review purposes but also because this would have to be part of a new SageNB package, and it would be nice to separate those things out.  The logistics are already complicated enough for things.\n\n\nThat's probably a good idea.  I'll split the extcode off into another ticket.",
    "created_at": "2011-03-25T05:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76202",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:13 kcrisman]:
> I can taste it now that you reviewed #693.    This is great stuff, good work.


:-)

> Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  


Good point.  I have added documentation for `notebook?`.  Does it need documentation in `sage --advanced` as well?

> I also have a couple questions, but they just indicate my lack of knowledge. 
> * I don't understand this change.  More precisely, we now have the default `startpath = ''`, but that isn't the same as `\`.  Will that matter somewhere for non-uploading situations?
> 
> ```
>                         browse_to(old_interface, old_port, old_secure, '/') 
>                         browse_to(old_interface, old_port, old_secure, startpath)
> ```


I don't think that should matter, but I changed it to `'/'` since it makes more sense.  In an earlier version of the patch I think I appended to `startpath` and that's why it was empty.

>  * You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.


You are right, there was a bug there.  I need it both places.  Thanks.

>  * Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\ sheet.sws'


Yes.  They have to be escaped for the shell so that they appear as one argument.  That's the same as any argument to `sage -n`.  However, I should point out that the syntax is `sage -n upload="/path/to work sheet.sws"`.  I guess that's why we need documentation, eh? :-)

>  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!


I think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.

> I'd be inclined to separate the new notebook functionality from adding clickable sws files to the Sage App, for review purposes but also because this would have to be part of a new SageNB package, and it would be nice to separate those things out.  The logistics are already complicated enough for things.


That's probably a good idea.  I'll split the extcode off into another ticket.



---

archive/issue_comments_076203.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-25T06:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76203",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076204.json:
```json
{
    "body": "> > Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  \n\n> \n> Good point.  I have added documentation for `notebook?`.  Does it need documentation in `sage --advanced` as well?\n\nNo, because that says the options are as in `notebook()` in the command line, which covers it.\n> >  * You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.\n \n> \n> You are right, there was a bug there.  I need it both places.  Thanks.\n\nGood.\n> >  * Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\\ sheet.sws'\n \n> \n> Yes.  They have to be escaped for the shell so that they appear as one argument.  That's the same as any argument to `sage -n`.  However, I should point out that the syntax is `sage -n upload=\"/path/to work sheet.sws\"`.  I guess that's why we need documentation, eh? :-)\n  \nHah!  But it's nice that this also works.\n> >  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!\n \n> \n> I think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.\nHmm.  So if I use the upload= syntax I should be okay?",
    "created_at": "2011-03-25T15:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76204",
    "user": "https://github.com/kcrisman"
}
```

> > Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  

> 
> Good point.  I have added documentation for `notebook?`.  Does it need documentation in `sage --advanced` as well?

No, because that says the options are as in `notebook()` in the command line, which covers it.
> >  * You said you added something to fix special character issues, but I don't know where that is, other than the place where you import urllib - but you only do that in the case that someone needs to log in.  Is that the only place it's needed?  This could just be my ignorance speaking.
 
> 
> You are right, there was a bug there.  I need it both places.  Thanks.

Good.
> >  * Looks like file names with spaces have to be escaped with the syntax `./sage -n /path/to/work\ sheet.sws'
 
> 
> Yes.  They have to be escaped for the shell so that they appear as one argument.  That's the same as any argument to `sage -n`.  However, I should point out that the syntax is `sage -n upload="/path/to work sheet.sws"`.  I guess that's why we need documentation, eh? :-)
  
Hah!  But it's nice that this also works.
> >  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!
 
> 
> I think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.
Hmm.  So if I use the upload= syntax I should be okay?



---

archive/issue_comments_076205.json:
```json
{
    "body": "> > >  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!\n \n> > \n> > I think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.\n\n\nYeah, you're right - I found a random new sagenb folder there! \n\nOne thing that happens is that your thing checks whether ANY other Sage server is running with the same folder of worksheets.  But I had a different Sage version already running through my usual !sage_notebook.sagenb, and that caused an error since it didn't have the syntax, I guess.  I don't know that that's a bug.\n\nI think that the extra `/` is causing problems, though.  Here are two things.  The second one works.\n\n```\nDownloads/sage-4.7.alpha1/sage -n upload=\"/Users/.../MAT338Day1-2011.sws\"\nDownloads/sage-4.7.alpha1/sage -n upload=\"Users/.../MAT338Day1-2011.sws\"\n```\nI think that one too many `/`s is messing things up.  But the first one IS the full path to the file, so this could be very confusing.  After all,\n\n```\nDownloads/sage-4.7.alpha1/sage -n upload=\"~/Downloads/MAT338Day1-2011.sws\"\n```\ngives \n\n```\nexceptions.IOError: [Errno 2] No such file or directory: '/~/Downloads/MAT338Day1-2011.sws'\n```\nSo we can't use that syntax for the local directory either.  Clearly the extra `/` isn't helping.",
    "created_at": "2011-03-25T15:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76205",
    "user": "https://github.com/kcrisman"
}
```

> > >  * I also discovered what might be a bug, or maybe it's a feature... trying to upload a file via `./sage -n /path/to/sws.sws` asks for a new password for admin.  That is really annoying, esp. if this is only supposed to work on a local machine anyway!
 
> > 
> > I think what's happening here is it's starting a new notebook server with /path/to/sws.sws as it's directory or something.  I think that's why it's asking for a password.


Yeah, you're right - I found a random new sagenb folder there! 

One thing that happens is that your thing checks whether ANY other Sage server is running with the same folder of worksheets.  But I had a different Sage version already running through my usual !sage_notebook.sagenb, and that caused an error since it didn't have the syntax, I guess.  I don't know that that's a bug.

I think that the extra `/` is causing problems, though.  Here are two things.  The second one works.

```
Downloads/sage-4.7.alpha1/sage -n upload="/Users/.../MAT338Day1-2011.sws"
Downloads/sage-4.7.alpha1/sage -n upload="Users/.../MAT338Day1-2011.sws"
```
I think that one too many `/`s is messing things up.  But the first one IS the full path to the file, so this could be very confusing.  After all,

```
Downloads/sage-4.7.alpha1/sage -n upload="~/Downloads/MAT338Day1-2011.sws"
```
gives 

```
exceptions.IOError: [Errno 2] No such file or directory: '/~/Downloads/MAT338Day1-2011.sws'
```
So we can't use that syntax for the local directory either.  Clearly the extra `/` isn't helping.



---

archive/issue_comments_076206.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-25T15:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76206",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076207.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> I think that the extra `/` is causing problems, though.  Here are two things.  The second one works.\n> \n> ```\n> Downloads/sage-4.7.alpha1/sage -n upload=\"/Users/.../MAT338Day1-2011.sws\"\n> Downloads/sage-4.7.alpha1/sage -n upload=\"Users/.../MAT338Day1-2011.sws\"\n> ```\n> I think that one too many `/`s is messing things up.  But the first one IS the full path to the file, so this could be very confusing.  After all,\n> \n> ```\n> Downloads/sage-4.7.alpha1/sage -n upload=\"~/Downloads/MAT338Day1-2011.sws\"\n> ```\n> gives \n> \n> ```\n> exceptions.IOError: [Errno 2] No such file or directory: '/~/Downloads/MAT338Day1-2011.sws'\n> ```\n> So we can't use that syntax for the local directory either.  Clearly the extra `/` isn't helping.\n\n\nHmm.  The extra `/` doesn't cause a problem on my machine, but I have noticed differences in URL handling on earlier version of OS X, so I'll go ahead a remove it.",
    "created_at": "2011-03-25T17:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76207",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:18 kcrisman]:
> I think that the extra `/` is causing problems, though.  Here are two things.  The second one works.
> 
> ```
> Downloads/sage-4.7.alpha1/sage -n upload="/Users/.../MAT338Day1-2011.sws"
> Downloads/sage-4.7.alpha1/sage -n upload="Users/.../MAT338Day1-2011.sws"
> ```
> I think that one too many `/`s is messing things up.  But the first one IS the full path to the file, so this could be very confusing.  After all,
> 
> ```
> Downloads/sage-4.7.alpha1/sage -n upload="~/Downloads/MAT338Day1-2011.sws"
> ```
> gives 
> 
> ```
> exceptions.IOError: [Errno 2] No such file or directory: '/~/Downloads/MAT338Day1-2011.sws'
> ```
> So we can't use that syntax for the local directory either.  Clearly the extra `/` isn't helping.


Hmm.  The extra `/` doesn't cause a problem on my machine, but I have noticed differences in URL handling on earlier version of OS X, so I'll go ahead a remove it.



---

archive/issue_comments_076208.json:
```json
{
    "body": "Attachment [trac_8473-sagenb.2.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-sagenb.2.patch) by @kcrisman created at 2011-03-30 15:33:06",
    "created_at": "2011-03-30T15:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76208",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8473-sagenb.2.patch](tarball://root/attachments/some-uuid/ticket8473/trac_8473-sagenb.2.patch) by @kcrisman created at 2011-03-30 15:33:06



---

archive/issue_comments_076209.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-30T15:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76209",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076210.json:
```json
{
    "body": "Ivan, is it very hard to catch a certain kind of error?  I get \n\n```\nexceptions.IOError: [Errno 2] No such file or directory: 'Users/.../MAT338Day1-2011.sws'\n```\nif I try to upload it with \n\n```\nsage -n upload=\"Users/.../MAT338Day1-2011.sws\"\n```\nIf I try to upload with \n\n```\nsage -n upload=\"/Users/.../MAT338Day1-2011.sws\"\n```\nI get \n\n```\nThe resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.\n```\nThe same if I do \n\n```\nsage: notebook(upload=\"...\")\n```\nSo here is what works for me.\n* old patch, not including first slash.\nHere is what doesn't work.\n* old patch with a slash.\n* new patch with or without slash.\nI'm confused.  I really wanted to get this all reviewed but have no idea what is going on, of course.",
    "created_at": "2011-04-02T02:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76210",
    "user": "https://github.com/kcrisman"
}
```

Ivan, is it very hard to catch a certain kind of error?  I get 

```
exceptions.IOError: [Errno 2] No such file or directory: 'Users/.../MAT338Day1-2011.sws'
```
if I try to upload it with 

```
sage -n upload="Users/.../MAT338Day1-2011.sws"
```
If I try to upload with 

```
sage -n upload="/Users/.../MAT338Day1-2011.sws"
```
I get 

```
The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.
```
The same if I do 

```
sage: notebook(upload="...")
```
So here is what works for me.
* old patch, not including first slash.
Here is what doesn't work.
* old patch with a slash.
* new patch with or without slash.
I'm confused.  I really wanted to get this all reviewed but have no idea what is going on, of course.



---

archive/issue_comments_076211.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> Ivan, is it very hard to catch a certain kind of error?  I get \n\n{{{\nexceptions.IOError: [Errno 2] No such file or directory: 'Users/.../MAT338Day1-2011.sws'\n}}}\n> if I try to upload it with \n\n{{{\nsage -n upload=\"Users/.../MAT338Day1-2011.sws\"\n}}}\n\nThat's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)\n\n> If I try to upload with \n\n{{{\nsage -n upload=\"/Users/.../MAT338Day1-2011.sws\"\n}}}\n> I get \n\n{{{\nThe resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.\n}}}\n\nI was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?\n\n> So here is what works for me.\n> * old patch, not including first slash.\n> Here is what doesn't work.\n> * old patch with a slash.\n> * new patch with or without slash.\n> I'm confused.  I really wanted to get this all reviewed but have no idea what is going on, of course.\n\n\nI don't understand why the old patch would work but not the new one.  If it's not the same problem as above then maybe you could try `sage --notebook upload=`localhost/Users/...`  That also works for me and it may work better on older versions of OS X.",
    "created_at": "2011-04-09T20:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76211",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:22 kcrisman]:
> Ivan, is it very hard to catch a certain kind of error?  I get 

{{{
exceptions.IOError: [Errno 2] No such file or directory: 'Users/.../MAT338Day1-2011.sws'
}}}
> if I try to upload it with 

{{{
sage -n upload="Users/.../MAT338Day1-2011.sws"
}}}

That's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)

> If I try to upload with 

{{{
sage -n upload="/Users/.../MAT338Day1-2011.sws"
}}}
> I get 

{{{
The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.
}}}

I was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?

> So here is what works for me.
> * old patch, not including first slash.
> Here is what doesn't work.
> * old patch with a slash.
> * new patch with or without slash.
> I'm confused.  I really wanted to get this all reviewed but have no idea what is going on, of course.


I don't understand why the old patch would work but not the new one.  If it's not the same problem as above then maybe you could try `sage --notebook upload=`localhost/Users/...`  That also works for me and it may work better on older versions of OS X.



---

archive/issue_comments_076212.json:
```json
{
    "body": "> That's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)\n\nOkay!\n> The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.\n> I was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?\n\n\nAha.  Well, I don't have Sage.app even on one of the computers any more (though the icons remain for sws files! what's up with that?), but what did the trick was starting the notebook, getting the error message, leaving the notebook running, and then uploading with the correct syntax a second time.  \n\nHow do I even check if !SAGE_BROWSER is set?  I can't use the command line of that terminal while the server is running, and a new terminal won't have it defined, presumably.\n\nAnyway, this makes me more hopeful this is doable; however, there should not be any connection between having once downloaded the app bundle (perhaps immediately trashed, even) and this syntax working.",
    "created_at": "2011-04-15T16:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76212",
    "user": "https://github.com/kcrisman"
}
```

> That's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)

Okay!
> The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.
> I was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?


Aha.  Well, I don't have Sage.app even on one of the computers any more (though the icons remain for sws files! what's up with that?), but what did the trick was starting the notebook, getting the error message, leaving the notebook running, and then uploading with the correct syntax a second time.  

How do I even check if !SAGE_BROWSER is set?  I can't use the command line of that terminal while the server is running, and a new terminal won't have it defined, presumably.

Anyway, this makes me more hopeful this is doable; however, there should not be any connection between having once downloaded the app bundle (perhaps immediately trashed, even) and this syntax working.



---

archive/issue_comments_076213.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-15T16:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76213",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076214.json:
```json
{
    "body": "This needs to be (slightly) rebased for #10652.  I can't tell immediately whether the extra filetypes allowed there need any other changes to this patch - my sense is probably not?  Anyway, that shouldn't be too hard.\n\nYeah, the problem on the computer where this doesn't work quite right is probably the same as yours - because I also have a nonstandard browser (well, Firefox) as default there.  Switching the default browser to Safari removes the problem.\n\nI really want to give this positive review so that I can review #11026, #10556, and #10555, but it seems like it's not great that one would have to use Safari on Mac for this to work properly (and who knows on other systems where I haven't tested this?).\n\nWhat's particularly odd is that `sage-open` (in the scripts directory) is getting the correct browser for me, as far as I can tell, in either case (Safari or FF).  But the way sage/misc/viewer.py operates is a little mysterious - `sage-native-execute` shouldn't have to run `sage-open` on OS X. \n\nAny thoughts?  I'm sorry for the delay in reviewing this, I was busy with Cygwin and running the workshop in my Sage time this summer.",
    "created_at": "2011-08-01T21:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76214",
    "user": "https://github.com/kcrisman"
}
```

This needs to be (slightly) rebased for #10652.  I can't tell immediately whether the extra filetypes allowed there need any other changes to this patch - my sense is probably not?  Anyway, that shouldn't be too hard.

Yeah, the problem on the computer where this doesn't work quite right is probably the same as yours - because I also have a nonstandard browser (well, Firefox) as default there.  Switching the default browser to Safari removes the problem.

I really want to give this positive review so that I can review #11026, #10556, and #10555, but it seems like it's not great that one would have to use Safari on Mac for this to work properly (and who knows on other systems where I haven't tested this?).

What's particularly odd is that `sage-open` (in the scripts directory) is getting the correct browser for me, as far as I can tell, in either case (Safari or FF).  But the way sage/misc/viewer.py operates is a little mysterious - `sage-native-execute` shouldn't have to run `sage-open` on OS X. 

Any thoughts?  I'm sorry for the delay in reviewing this, I was busy with Cygwin and running the workshop in my Sage time this summer.



---

archive/issue_comments_076215.json:
```json
{
    "body": "See #11026 for another weird type of error with uploading that only seems to manifest itself with the app part.",
    "created_at": "2011-08-02T02:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76215",
    "user": "https://github.com/kcrisman"
}
```

See #11026 for another weird type of error with uploading that only seems to manifest itself with the app part.



---

archive/issue_comments_076216.json:
```json
{
    "body": "I'm getting some other weird behavior, which I think is the same as the previous comment, but I can't be sure because it occurred in a different situation and a different computer.  I get \"The resource /upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws cannot be found.\" when going to\n\n```\nhttp://localhost:8000/upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws\n```\nThis is after a message about FF not opening because there is already one running.    It seems to happen when a separate Mac app is open (not necessarily with server running).",
    "created_at": "2011-08-02T12:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76216",
    "user": "https://github.com/kcrisman"
}
```

I'm getting some other weird behavior, which I think is the same as the previous comment, but I can't be sure because it occurred in a different situation and a different computer.  I get "The resource /upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws cannot be found." when going to

```
http://localhost:8000/upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws
```
This is after a message about FF not opening because there is already one running.    It seems to happen when a separate Mac app is open (not necessarily with server running).



---

archive/issue_comments_076217.json:
```json
{
    "body": "Summary:\n* Still 'needs work'.\n* Needs some kind of respecting of different browsers, though not necessarily universal.\n* Should still work if using a Mac app with #11026?\n\nBut I'm excited about this.",
    "created_at": "2011-08-02T12:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76217",
    "user": "https://github.com/kcrisman"
}
```

Summary:
* Still 'needs work'.
* Needs some kind of respecting of different browsers, though not necessarily universal.
* Should still work if using a Mac app with #11026?

But I'm excited about this.



---

archive/issue_comments_076218.json:
```json
{
    "body": "This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).\n\nI figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.",
    "created_at": "2012-01-24T02:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76218",
    "user": "https://github.com/kcrisman"
}
```

This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).

I figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.



---

archive/issue_comments_076219.json:
```json
{
    "body": "Also, those patches should probably be merged into one?  Anyway, I found at least one error there - \n\n```\n``http://localhost:8000/upload`` or to fetching\n```\nbut in the new notebook apparently (?) it's port 8080.",
    "created_at": "2012-01-24T02:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76219",
    "user": "https://github.com/kcrisman"
}
```

Also, those patches should probably be merged into one?  Anyway, I found at least one error there - 

```
``http://localhost:8000/upload`` or to fetching
```
but in the new notebook apparently (?) it's port 8080.



---

archive/issue_comments_076220.json:
```json
{
    "body": "Replying to [comment:31 kcrisman]:\n> Also, those patches should probably be merged into one?  \n\n\nYes.  I'm not sure if I can do that now that I have pushed to github though.\n\n> Anyway, I found at least one error there - \n> \n> ```\n> ``http://localhost:8000/upload`` or to fetching\n> ```\n> but in the new notebook apparently (?) it's port 8080.\n\n\nFixed, thanks.",
    "created_at": "2012-01-24T07:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76220",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:31 kcrisman]:
> Also, those patches should probably be merged into one?  


Yes.  I'm not sure if I can do that now that I have pushed to github though.

> Anyway, I found at least one error there - 
> 
> ```
> ``http://localhost:8000/upload`` or to fetching
> ```
> but in the new notebook apparently (?) it's port 8080.


Fixed, thanks.



---

archive/issue_comments_076221.json:
```json
{
    "body": "Replying to [comment:30 kcrisman]:\n> This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).\n> \n> I figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.\n\n\nWe shouldn't need any of these patches here since the extcode patch was moved to #11026.",
    "created_at": "2012-01-24T07:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76221",
    "user": "https://github.com/gvol"
}
```

Replying to [comment:30 kcrisman]:
> This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).
> 
> I figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.


We shouldn't need any of these patches here since the extcode patch was moved to #11026.



---

archive/issue_comments_076222.json:
```json
{
    "body": "I've put this on a more accurate upstream report, given the pull request that has to be reviewed.",
    "created_at": "2012-06-01T18:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76222",
    "user": "https://github.com/kcrisman"
}
```

I've put this on a more accurate upstream report, given the pull request that has to be reviewed.



---

archive/issue_comments_076223.json:
```json
{
    "body": "The version on the pull request works, at any rate, though it doesn't seem to check correctly for when a server is already running.",
    "created_at": "2012-06-11T21:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76223",
    "user": "https://github.com/kcrisman"
}
```

The version on the pull request works, at any rate, though it doesn't seem to check correctly for when a server is already running.



---

archive/issue_comments_076224.json:
```json
{
    "body": "See [the pull request](https://github.com/sagemath/sagenb/pull/31) for more discussion.  It seems to be working great!  Just need to check out the new code.",
    "created_at": "2012-06-14T17:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76224",
    "user": "https://github.com/kcrisman"
}
```

See [the pull request](https://github.com/sagemath/sagenb/pull/31) for more discussion.  It seems to be working great!  Just need to check out the new code.



---

archive/issue_comments_076225.json:
```json
{
    "body": "Okay, the upstream looks good with the one exception of [this issue](https://github.com/sagemath/sagenb/pull/31#issuecomment-6336374) when `automatic_login=False` but there is still an `upload` to be done.  \n\nLeaving as \"needs work\" and moving milestone to 5.2 since it depends on #11080 in some sense, though only on the upstream end so not putting it in dependencies.",
    "created_at": "2012-06-14T19:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76225",
    "user": "https://github.com/kcrisman"
}
```

Okay, the upstream looks good with the one exception of [this issue](https://github.com/sagemath/sagenb/pull/31#issuecomment-6336374) when `automatic_login=False` but there is still an `upload` to be done.  

Leaving as "needs work" and moving milestone to 5.2 since it depends on #11080 in some sense, though only on the upstream end so not putting it in dependencies.



---

archive/issue_events_020352.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-14T19:12:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "milestone": "sage-5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8473#event-20352"
}
```



---

archive/issue_comments_076226.json:
```json
{
    "body": "Okay, this was resolved within a half hour!  Unfortunately, then it took over five minutes to even get back on Trac for me.\n\nI don't know exactly how this works; we don't make an spkg in this case.  I'm putting positive review, but it depends on exactly when this gets from upstream to sage - Jeroen, if you feel comfortable doing so, put it on sage-pending.  I just don't want it to get lost.",
    "created_at": "2012-06-14T19:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76226",
    "user": "https://github.com/kcrisman"
}
```

Okay, this was resolved within a half hour!  Unfortunately, then it took over five minutes to even get back on Trac for me.

I don't know exactly how this works; we don't make an spkg in this case.  I'm putting positive review, but it depends on exactly when this gets from upstream to sage - Jeroen, if you feel comfortable doing so, put it on sage-pending.  I just don't want it to get lost.



---

archive/issue_comments_076227.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-14T19:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76227",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_076228.json:
```json
{
    "body": "I've merged the pull request :)",
    "created_at": "2012-06-15T00:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76228",
    "user": "https://github.com/kini"
}
```

I've merged the pull request :)



---

archive/issue_events_020353.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-15T21:07:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "milestone": "sage-5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8473#event-20353"
}
```



---

archive/issue_events_020354.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-15T21:07:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8473#event-20354"
}
```



---

archive/issue_comments_076229.json:
```json
{
    "body": "Not really sure what to do either, where is the spkg containing this fix going to end up?",
    "created_at": "2012-06-15T21:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76229",
    "user": "https://github.com/jdemeyer"
}
```

Not really sure what to do either, where is the spkg containing this fix going to end up?



---

archive/issue_comments_076230.json:
```json
{
    "body": "It will end up at #13121.",
    "created_at": "2012-06-15T21:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76230",
    "user": "https://github.com/kini"
}
```

It will end up at #13121.



---

archive/issue_comments_076231.json:
```json
{
    "body": "I'm having problems with this. I've posted comments at the [pull request](https://github.com/sagemath/sagenb/pull/31).",
    "created_at": "2012-06-23T15:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76231",
    "user": "https://github.com/jhpalmieri"
}
```

I'm having problems with this. I've posted comments at the [pull request](https://github.com/sagemath/sagenb/pull/31).



---

archive/issue_comments_076232.json:
```json
{
    "body": "The main issue there was resolved at [this pull request](https://github.com/sagemath/sagenb/issues/76), so this is fine.",
    "created_at": "2012-06-26T13:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76232",
    "user": "https://github.com/kcrisman"
}
```

The main issue there was resolved at [this pull request](https://github.com/sagemath/sagenb/issues/76), so this is fine.



---

archive/issue_comments_076233.json:
```json
{
    "body": "Actually, that was only an issue, not a pull request - it's actually solved at [this pull request](https://github.com/sagemath/sagenb/pull/78), with discussion at [this issue](https://github.com/sagemath/sagenb/issues/76).  See [here](https://github.com/sagemath/sagenb/pull/31#issuecomment-6525903) for the original problem encountered.",
    "created_at": "2012-06-27T15:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76233",
    "user": "https://github.com/kcrisman"
}
```

Actually, that was only an issue, not a pull request - it's actually solved at [this pull request](https://github.com/sagemath/sagenb/pull/78), with discussion at [this issue](https://github.com/sagemath/sagenb/issues/76).  See [here](https://github.com/sagemath/sagenb/pull/31#issuecomment-6525903) for the original problem encountered.



---

archive/issue_comments_076234.json:
```json
{
    "body": "I'm assuming nothing here needs to be merged?",
    "created_at": "2012-07-09T20:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76234",
    "user": "https://github.com/jdemeyer"
}
```

I'm assuming nothing here needs to be merged?



---

archive/issue_comments_076235.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-07-09T20:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76235",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_076236.json:
```json
{
    "body": "Sorry, I got confused because #13121 \"depends\" on this.",
    "created_at": "2012-07-09T20:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76236",
    "user": "https://github.com/jdemeyer"
}
```

Sorry, I got confused because #13121 "depends" on this.



---

archive/issue_comments_076237.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-09T20:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8473#issuecomment-76237",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_020355.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-09T20:12:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8473",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8473#event-20355"
}
```
