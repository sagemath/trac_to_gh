# Issue 8473: Make .sws files clickable

Issue created by migration from https://trac.sagemath.org/ticket/8473

Original creator: olazo

Original creation time: 2010-03-07 04:15:40

Assignee: was

It would be great for those of us who have installed Sage to be able
to double click on these files and have sage open them in the
notebook.

Supoorting a command on the likes of


```
sage -notebook /path/to/worksheet.sws
```


would be a very good step in this direction


---

Comment by mpatel created at 2010-03-08 00:41:44

Ticket #693 is related.


---

Comment by kcrisman created at 2010-09-08 15:08:43

What would be needed for this?  #693 shows that it's possible to know whether the notebook is running and then open the browser or not based on this.  And `http://foo.sagenb.org/home/me/upload_worksheet` shows that there is a script to take a .sws file and send it straight to the browser.    So I say this is definitely doable by someone who knows these scripts.  Is this right?


---

Comment by kcrisman created at 2010-09-08 15:12:43

This also led to the following - #9875.


---

Comment by iandrus created at 2010-12-29 12:16:24

Changing status from new to needs_review.


---

Comment by iandrus created at 2010-12-29 12:16:24

Depends on #693

I have added support for uploading from a file:// url in order to support `sage --notebook upload=FILE.sws`.  The sagenb patch allows this, and the extcode patch adds support to the Mac application.  I had to support file urls so that the upload url could be given as a GET rather than a POST request, and hence be passed to any browser.

The Mac app has a new option to automatically start the server when a sws file is opened.  I'm not sure anyone would ever want to turn this off, so I can remove it if it's not useful.


---

Comment by iandrus created at 2010-12-29 12:30:54

I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.


---

Comment by iandrus created at 2010-12-29 12:30:54

Changing assignee from was to iandrus.


---

Comment by kcrisman created at 2010-12-29 17:37:04

Replying to [comment:6 iandrus]:
> I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.
But I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...


---

Comment by iandrus created at 2010-12-29 17:55:59

Replying to [comment:7 kcrisman]:
> Replying to [comment:6 iandrus]:
> > I should note I only allow file urls when running on localhost because otherwise it doesn't make much sense and could be a security hole.
> But I can imagine people definitely wanting to upload an sws file to a Sage instance running only in their browser, i.e. from xyz.sagenb.org.  And we already allow arbitrary code in a Sage notebook instance!  So I don't know whether this would be any less secure than the current situation...

I was probably unclear.  With a file url, it would grab the file from the server rather than the local machine, so it's probably not what people want or expect at all.  e.g. if you try to upload file:///home/iandrus/sage/sws1.sws, this will only work if the machine the server is running on also has a file at /home/iandrus/sage/sws1.sws, and then only if the file is the same.  

It might be nice to add some way to upload a file to a remote server programmatically, but I think that entails logging in and then sending off a POST request from a script, so it has a different feel.  I tried writing a simple script using curl a while ago, but I couldn't get it to work for some reason.  Perhaps someone knows of a better/different way to accomplish it.

You are right about the security hole though, it's probably the least of our worries :-)


---

Attachment


---

Comment by iandrus created at 2011-01-04 14:37:25

Added urlencoding so that files with special characters will work okay.


---

Comment by kcrisman created at 2011-01-11 04:13:22

I'd like to test this, but I'm reluctant to do so until someone who knows something about the notebook takes a look at # 693.  Bug days folks?


---

Attachment

I added zip and txt files to the Mac App as well as support (icons etc.) for Cython files.


---

Comment by kcrisman created at 2011-03-25 03:04:53

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

Comment by kcrisman created at 2011-03-25 03:09:58

This doesn't even work - it asks for a password:

```
notebook(r'''/Users/.../MAT338Day1-2011.sws''',require_login=False)
```

while `notebook()` continues to work fine.  I would view this as a bug in the case of this syntax.


---

Comment by kcrisman created at 2011-03-25 03:09:58

Changing status from needs_review to needs_work.


---

Comment by iandrus created at 2011-03-25 05:59:27

Replying to [comment:13 kcrisman]:
> I can taste it now that you reviewed #693.    This is great stuff, good work.

:-)

> Okay, needs work because this option isn't documented.  Ordinarily I wouldn't be as strict with NB stuff because so little of it is documented anyway, but I think it is key that `notebook?` tells us what happens.  

Good point.  I have added documentation for `notebook?`.  Does it need documentation in `sage --advanced` as well?

> I also have a couple questions, but they just indicate my lack of knowledge. 
>  * I don't understand this change.  More precisely, we now have the default `startpath = ''`, but that isn't the same as `\`.  Will that matter somewhere for non-uploading situations?
> {{{
>                         browse_to(old_interface, old_port, old_secure, '/') 
>                         browse_to(old_interface, old_port, old_secure, startpath)
> }}}

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

Comment by iandrus created at 2011-03-25 06:07:58

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-03-25 15:16:33

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

Comment by kcrisman created at 2011-03-25 15:44:20

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

Comment by kcrisman created at 2011-03-25 15:44:20

Changing status from needs_review to needs_work.


---

Comment by iandrus created at 2011-03-25 17:26:54

Replying to [comment:18 kcrisman]:
> I think that the extra `/` is causing problems, though.  Here are two things.  The second one works.
> {{{
> Downloads/sage-4.7.alpha1/sage -n upload="/Users/.../MAT338Day1-2011.sws"
> Downloads/sage-4.7.alpha1/sage -n upload="Users/.../MAT338Day1-2011.sws"
> }}}
> I think that one too many `/`s is messing things up.  But the first one IS the full path to the file, so this could be very confusing.  After all,
> {{{
> Downloads/sage-4.7.alpha1/sage -n upload="~/Downloads/MAT338Day1-2011.sws"
> }}}
> gives 
> {{{
> exceptions.IOError: [Errno 2] No such file or directory: '/~/Downloads/MAT338Day1-2011.sws'
> }}}
> So we can't use that syntax for the local directory either.  Clearly the extra `/` isn't helping.

Hmm.  The extra `/` doesn't cause a problem on my machine, but I have noticed differences in URL handling on earlier version of OS X, so I'll go ahead a remove it.


---

Attachment


---

Comment by kcrisman created at 2011-03-30 15:33:06

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-04-02 02:12:12

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

Comment by iandrus created at 2011-04-09 20:11:01

Replying to [comment:22 kcrisman]:
> Ivan, is it very hard to catch a certain kind of error?  I get 

```
exceptions.IOError: [Errno 2] No such file or directory: 'Users/.../MAT338Day1-2011.sws'
```

> if I try to upload it with 

```
sage -n upload="Users/.../MAT338Day1-2011.sws"
```


That's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)

> If I try to upload with 

```
sage -n upload="/Users/.../MAT338Day1-2011.sws"
```

> I get 

```
The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.
```


I was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?

> So here is what works for me.
>  * old patch, not including first slash.
> Here is what doesn't work.
>  * old patch with a slash.
>  * new patch with or without slash.
> I'm confused.  I really wanted to get this all reviewed but have no idea what is going on, of course.

I don't understand why the old patch would work but not the new one.  If it's not the same problem as above then maybe you could try `sage --notebook upload=`localhost/Users/...`  That also works for me and it may work better on older versions of OS X.


---

Comment by kcrisman created at 2011-04-15 16:58:41

> That's what I would expect.  Such a thing shouldn't work--that it did before is a mistake :-)
Okay!
> The resource /upload_worksheet?url=file:///Users/.../MAT338Day1-2011.sws cannot be found.
> I was finally able to reproduce this.  I'm seeing this problem when Sage.app is set to be my browser (so it is logged in) and I run `sage --notebook upload=...` from the command line.  In this case SAGE_BROWSER isn't set correctly so it tries to open the upload page in Safari which isn't logged in.  If I then login in Safari and upload again it works.  Is this the same problem you are seeing?

Aha.  Well, I don't have Sage.app even on one of the computers any more (though the icons remain for sws files! what's up with that?), but what did the trick was starting the notebook, getting the error message, leaving the notebook running, and then uploading with the correct syntax a second time.  

How do I even check if !SAGE_BROWSER is set?  I can't use the command line of that terminal while the server is running, and a new terminal won't have it defined, presumably.

Anyway, this makes me more hopeful this is doable; however, there should not be any connection between having once downloaded the app bundle (perhaps immediately trashed, even) and this syntax working.


---

Comment by kcrisman created at 2011-04-15 16:58:41

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-08-01 21:11:49

This needs to be (slightly) rebased for #10652.  I can't tell immediately whether the extra filetypes allowed there need any other changes to this patch - my sense is probably not?  Anyway, that shouldn't be too hard.

Yeah, the problem on the computer where this doesn't work quite right is probably the same as yours - because I also have a nonstandard browser (well, Firefox) as default there.  Switching the default browser to Safari removes the problem.

I really want to give this positive review so that I can review #11026, #10556, and #10555, but it seems like it's not great that one would have to use Safari on Mac for this to work properly (and who knows on other systems where I haven't tested this?).

What's particularly odd is that `sage-open` (in the scripts directory) is getting the correct browser for me, as far as I can tell, in either case (Safari or FF).  But the way sage/misc/viewer.py operates is a little mysterious - `sage-native-execute` shouldn't have to run `sage-open` on OS X. 

Any thoughts?  I'm sorry for the delay in reviewing this, I was busy with Cygwin and running the workshop in my Sage time this summer.


---

Comment by kcrisman created at 2011-08-02 02:48:08

See #11026 for another weird type of error with uploading that only seems to manifest itself with the app part.


---

Comment by kcrisman created at 2011-08-02 12:30:50

I'm getting some other weird behavior, which I think is the same as the previous comment, but I can't be sure because it occurred in a different situation and a different computer.  I get "The resource /upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws cannot be found." when going to

```
http://localhost:8000/upload_worksheet?url=file:///Users/karl-dietercrisman/Desktop/Test.sws
```

This is after a message about FF not opening because there is already one running.    It seems to happen when a separate Mac app is open (not necessarily with server running).


---

Comment by kcrisman created at 2011-08-02 12:34:04

Summary:
 * Still 'needs work'.
 * Needs some kind of respecting of different browsers, though not necessarily universal.
 * Should still work if using a Mac app with #11026?

But I'm excited about this.


---

Comment by kcrisman created at 2012-01-24 02:42:47

This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).

I figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.


---

Comment by kcrisman created at 2012-01-24 02:45:23

Also, those patches should probably be merged into one?  Anyway, I found at least one error there - 

```
``http://localhost:8000/upload`` or to fetching
```

but in the new notebook apparently (?) it's port 8080.


---

Comment by iandrus created at 2012-01-24 07:46:37

Replying to [comment:31 kcrisman]:
> Also, those patches should probably be merged into one?  

Yes.  I'm not sure if I can do that now that I have pushed to github though.

> Anyway, I found at least one error there - 
> {{{
> ``http://localhost:8000/upload`` or to fetching
> }}}
> but in the new notebook apparently (?) it's port 8080.

Fixed, thanks.


---

Comment by iandrus created at 2012-01-24 07:57:16

Replying to [comment:30 kcrisman]:
> This is a [pull request at the sagenb github site](https://github.com/sagemath/sagenb/pull/31).
> 
> I figure this goes back to 'needs review' once (if) it's clarified what patches would still be needed here.

We shouldn't need any of these patches here since the extcode patch was moved to #11026.


---

Comment by kcrisman created at 2012-06-01 18:02:23

I've put this on a more accurate upstream report, given the pull request that has to be reviewed.


---

Comment by kcrisman created at 2012-06-11 21:03:21

The version on the pull request works, at any rate, though it doesn't seem to check correctly for when a server is already running.


---

Comment by kcrisman created at 2012-06-14 17:43:47

See [the pull request](https://github.com/sagemath/sagenb/pull/31) for more discussion.  It seems to be working great!  Just need to check out the new code.


---

Comment by kcrisman created at 2012-06-14 19:12:56

Okay, the upstream looks good with the one exception of [this issue](https://github.com/sagemath/sagenb/pull/31#issuecomment-6336374) when `automatic_login=False` but there is still an `upload` to be done.  

Leaving as "needs work" and moving milestone to 5.2 since it depends on #11080 in some sense, though only on the upstream end so not putting it in dependencies.


---

Comment by kcrisman created at 2012-06-14 19:12:56

Changing priority from minor to major.


---

Comment by kcrisman created at 2012-06-14 19:48:56

Okay, this was resolved within a half hour!  Unfortunately, then it took over five minutes to even get back on Trac for me.

I don't know exactly how this works; we don't make an spkg in this case.  I'm putting positive review, but it depends on exactly when this gets from upstream to sage - Jeroen, if you feel comfortable doing so, put it on sage-pending.  I just don't want it to get lost.


---

Comment by kcrisman created at 2012-06-14 19:48:56

Changing status from needs_work to positive_review.


---

Comment by kini created at 2012-06-15 00:17:06

I've merged the pull request :)


---

Comment by jdemeyer created at 2012-06-15 21:09:02

Not really sure what to do either, where is the spkg containing this fix going to end up?


---

Comment by kini created at 2012-06-15 21:30:17

It will end up at #13121.


---

Comment by jhpalmieri created at 2012-06-23 15:46:18

I'm having problems with this. I've posted comments at the [pull request](https://github.com/sagemath/sagenb/pull/31).


---

Comment by kcrisman created at 2012-06-26 13:36:19

The main issue there was resolved at [this pull request](https://github.com/sagemath/sagenb/issues/76), so this is fine.


---

Comment by kcrisman created at 2012-06-27 15:11:00

Actually, that was only an issue, not a pull request - it's actually solved at [this pull request](https://github.com/sagemath/sagenb/pull/78), with discussion at [this issue](https://github.com/sagemath/sagenb/issues/76).  See [here](https://github.com/sagemath/sagenb/pull/31#issuecomment-6525903) for the original problem encountered.


---

Comment by jdemeyer created at 2012-07-09 20:04:17

I'm assuming nothing here needs to be merged?


---

Comment by jdemeyer created at 2012-07-09 20:04:17

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2012-07-09 20:11:18

Sorry, I got confused because #13121 "depends" on this.


---

Comment by jdemeyer created at 2012-07-09 20:12:10

Resolution: duplicate
