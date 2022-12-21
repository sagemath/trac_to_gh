# Issue 7700: Mysterious binary in sage-4.3.rc0/data/extcode/sage/ext/mac-app

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 01:39:55

Assignee: tbd

CC:  iandrus

This file:

```
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sage/ext/mac-app/Sage.app/Contents/MacOS/Sage
```


is a mysterious 80K binary program that does something.  Where did it come from?  What does it do?  Who made it?  How can I easily recreate it from source?    

If the answer is: "it's a binary from some random guy of the 'net that nobody knows"... then maybe we should be worried!

How to resolve this ticket:  For starters, add a README.txt to the directory: sage-4.3.rc0/data/extcode/sage/ext/mac-app that answers the above questions. 


---

Comment by was created at 2009-12-16 01:40:05

Changing priority from major to minor.


---

Comment by kcrisman created at 2009-12-18 13:23:24

My guess is that it is the thing that Platypus makes for Sage - it basically wraps the Terminal window in a nicer-looking window, I think.  I have cc:ed Ivan on this, since he is the one who made this, so hopefully he can answer it.   Note that it runs the very well-behaved script in Contents/Resources.

I have to say that don't really need Platypus to do all this, though it does look nicer.  Resources/English.lproj/MainMenu.nib is another, less mysterious, file that also is essentially impossible to edit using normal techniques.  It would be nice if there was documentation about exactly what was in both of them and how to recreate them, so I have slightly changed the summary.


---

Comment by kcrisman created at 2009-12-18 13:31:28

Changing component from packages to distribution.


---

Comment by kcrisman created at 2009-12-18 13:31:28

Even better would be if we could document how to use Xcode and InterfaceBuilder directly to do something like this (as opposed to the black box of Platypus.  "Platypus creates applications with a special binary that launches a specified script and captures its output."  One nice thing about it, on the other hand, is it should be able to easily create something that would take a .sage, .sws, or .py file and run it just by dropping it on the icon.

We should also have some sort of environment variable that would ask the user on start if they want notebook or command line, or something like that.  But of course now we're beyond this ticket; just recording the idea for now.

Also note that this doesn't affect most users, since we are not bdist-ing the app bundle by default yet.  Since this is really about the distribution of Sage in Mac, I'm also changing the component accordingly.


---

Comment by iandrus created at 2009-12-18 20:30:52

Changing assignee from tbd to iandrus.


---

Comment by iandrus created at 2009-12-18 20:30:52

It is in fact the actual program that platypus creates which handles the gui etc. of the application.  It just runs the script with the options in Resources/AppSettings.plist (though I guess I should read the platypus source to ensure that's all it does)

I will be happy to create a readme and a script to recreate these files (I thinking of adding it to sage -bdist, but I'm not sure that's the best place for it).  I'm taking finals right now so it may be a week or so before I get to it.

I would certainly not be opposed to a hand coded app, but platypus is definitely easier and since it's not clear how many people will actually use it I didn't want to spend too much time on it.

As for dropping files and having them open, that was what I wanted to work on next, but when I [asked on sage-devel about a month ago](http://groups.google.com/group/sage-devel/browse_thread/thread/b685a7396f627816/7ea17ebd69df26bd?lnk=gst&q=andrus#7ea17ebd69df26bd) I got no feedback, so I would definitely like to know what the desired behavior would be.


---

Comment by robertwb created at 2009-12-20 09:14:41

simple sage launcher


---

Attachment

An .app bundle can be dead simple without any binary blobs (except for the icon, of course). See attached, which is 3 folders and a 1-line bash script, and launches sage in a command line. This could be easy to adapt to do sage -notebook (and wouldn't even have to fire up terminal), and use a sage executable bundled with the app (e.g. in /Resources), though a bit of care should be taken to gracefully handle what happens when a notebook is already running, and what to do about quitting.


---

Comment by kcrisman created at 2009-12-20 23:20:44

I don't have time to look at it now, but there are definitely reasons why we have the longer script etc.  We used to have this as the thing but then iandrus packaged it more nicely, though of course with the platypus thing.  It's not clear to me how to fire up -notebook without the terminal.  You may want to look at previous discussions about this topic on other tickets.


---

Comment by was created at 2009-12-21 08:05:53

Thanks Robert!!


---

Comment by kcrisman created at 2009-12-21 13:30:44

Now that I have had a chance to look at it, I should clarify that the recommendation robertwb makes is more along the lines of the earlier suggestions that led to [http://trac.sagemath.org/sage_trac/ticket/4817](http://trac.sagemath.org/sage_trac/ticket/4817).  Is it possible to deal with all of the issues raised in tickets #5254, #5261, and #7546 without essentially doing all of the things done in them, with the exception of getting rid of the Platypus thing and putting in a script that tells Terminal to do the script at Contents/Resources/script?  

All the Platypus thing does is to run that script, but with a nice little window around it - you may want to try -bdisting with the appropriate app bundle variable set and seeing for yourself.  I don't know that we can avoid having the Terminal fire up without doing something equivalent to that, even without Platypus.


---

Comment by iandrus created at 2009-12-21 19:06:35

It's certainly easy to fire up a script in Terminal (though I personally don't like that since I tend to quit Terminal) and I think we could even do it with no output anywhere, but then you wouldn't be able to tell it to quit, which seems like a huge issue to me.  But if people really want it, perhaps we could make it depend on an environment variable--we don't have enough of those yet :)

Originally my dream was to have a "real" Mac Application.  i.e. something that will show up in the dock, have the console output if I want it, and have a web browser for actually running Sage notebooks.  Personally I hate having Sage mixed with my other browsing.  Right now I have a reasonable setup with the Sage launcher and a dedicated web browser, but it would be better if they were the same application.  That of course requires much more work: either writing our own application, extending Platypus to handle that situation (viz. web browsing), or modifying something like Prism to start up the notebook.  Last time I looked at Prism there were not even any hints as to how to build it despite several questions on the forum.

If the only problem is that we don't know where the binary came from, perhaps we should just include Platypus :)  The source is only 896k zipped and 2.4 MB unzipped, and we wouldn't even have to include it all!

Perhaps we should discuss it on sage-devel to see what people want and/or expect.


---

Comment by iandrus created at 2010-01-06 12:52:35

Information about the contents of Sage.app


---

Attachment

If this doesn't answer your questions, or you would like anything else let me know.


---

Comment by iandrus created at 2010-01-06 12:57:08

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-06 14:04:33

I like this a lot, at any rate!  Great work - makes it very clear what ALL the options are.


---

Comment by kcrisman created at 2010-01-06 14:04:33

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-07 06:48:59

I was just trying to address the myth that .app bundles are complicated, messy things--I agree that the script can (and should) do more. 

In terms of isolating the sage notebook from browsing, firefox has a -no-remote option that may be possible to use. It is also possible to start up to separate instances of Safari (by invoking the binary directly, though I haven't investigated how the two instances interact...)

In any case, this ticket is about documenting what exactly that is, and you've done a fine job, so +1 from me too.


---

Comment by rlm created at 2010-01-14 07:06:03

Resolution: fixed
