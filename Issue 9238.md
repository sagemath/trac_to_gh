# Issue 9238: J. Gutow's update to Jmol in the notebook...

Issue created by migration from Trac.

Original creator: gutow

Original creation time: 2010-06-14 16:06:19

Assignee: jason, was

CC:  timdumol kcrisman rkirov

I believe this drop-in set of javascript files now works.  Need testers!

Attached are replacement javascript files for jmol_lib.js and notebook_lib.js, which are located in sagenb/data/sage/js.  Changes to notebook_lib.js are just some added calls to functions in jmol_lib.js to let the javascript know when applets are closed.  The library jmol_lib.js is a complete rewrite.

Adds the following features to the notebook:

1) No more than 8 Jmols will be active at once.  This prevents running out of memory.  The user is provided with a link to wake up sleeping Jmols that they wish to manipulate.  Sleeping Jmols are replaced with a static image.

2) A spin on/off check box is now provided.

3) The user may choose among a number of display sizes.

4) In the function tab, the user may change function color and mesh color.

5) The "State" tab displays the Jmol script to get the Jmol display.  Eventually this will probably be hidden.  If we can get the notebook to store this user views would also transfer across sessions.


---

Attachment

jmol notebook javascript updates


---

Comment by jason created at 2010-06-14 17:30:07

Did you update the version of jmol in Sage as well?


---

Comment by gutow created at 2010-06-14 17:44:06

Replying to [comment:1 jason]:
> Did you update the version of jmol in Sage as well?
Jason,

Thanks!!! I forgot about that.  Yes, for all of this to work you need to use Jmol 11.8.  The latest release.  Should I add a .zip of the necessary applet files to the trac?

Jonathan


---

Comment by jason created at 2010-06-14 17:51:37

We should make a new spkg.  Is that what you did?  If not, then I can try to update the spkg to include the newest jmol if it's just a drop-in replacement for the old java files.


---

Comment by jason created at 2010-06-14 17:56:25

On the other hand, I didn't realize that jmol was just included in the sagenb spkg, so it'll probably be easier to update.  I'm CCing Tim, who has done some of the recent sagenb releases.

Yes, can you attach the updated jmol files as well, then (or if they're more than a megabyte or so, can you post a link to them?)

Thanks for all of this work!

Jason


---

Comment by gutow created at 2010-06-14 18:28:50

OK, I've posted a .zip archive with all the necessary Jmol stuff.  The link is now included in the trac ticket.  Sorry I forgot about that.

Jonathan


---

Comment by jason created at 2010-06-14 18:55:29

That zip file has a lot of __MACOSX and .DS_Store files...


---

Comment by gutow created at 2010-06-14 18:59:17

Replying to [comment:7 jason]:
> That zip file has a lot of __MACOSX and .DS_Store files...
Oops...It will still work, but I will clean it up and post an update later today.  People can try it with this, but look for a clean file tomorrow.

Jonathan


---

Comment by jason created at 2010-06-14 19:09:54

If you replace the existing jmol directory with the above zip, then you delete the "jmol" file inside that directory, which is necessary for the spkg to work.  The jmol file is:


```/bin/sh
#JMOL_HOME=`dirname "$0"`
JMOL_HOME="`"$SAGE_LOCAL"/bin/sage-pypkg-location sagenb`""/sagenb/data/jmol"

# Collect -D & -m options as java arguments
command=java
while [ `echo $1 | egrep '^-D|^-m' | wc -l` != 0 ]; do
        command="$command $1"
        shift
done

if [ -f ./Jmol.jar ] ; then
  jarpath=./Jmol.jar
elif [ -f $JMOL_HOME/Jmol.jar ] ; then
  jarpath=$JMOL_HOME/Jmol.jar
elif [ -f /usr/share/jmol/Jmol.jar ] ; then
  jarpath=/usr/share/jmol/Jmol.jar
else
  echo Jmol.jar not found
  exit
fi
$command -Xmx512m -jar $jarpath $`@`


```


Is that file still needed?  I think it probably makes jmol work from the command line for us.


---

Comment by gutow created at 2010-06-14 19:21:53

Hmmm...good eye!  I think you are correct.  I have never used Jmol from the command line.  It does look like the application is used.  I can certainly include that in the package as well as the shell script.  I thought that was the old Jmol linux shell script...I didn't even look inside....My bad.  When I clean things up I will get the necessary files for command line back in there.  I will do that this evening.  Let me know if you notice anything else.

Jonathan
Replying to [comment:9 jason]:
> If you replace the existing jmol directory with the above zip, then you delete the "jmol" file inside that directory, which is necessary for the spkg to work.  The jmol file is:
> 
> {{{
> #!/bin/sh
> #JMOL_HOME=`dirname "$0"`
> JMOL_HOME="`"$SAGE_LOCAL"/bin/sage-pypkg-location sagenb`""/sagenb/data/jmol"
> 
> # Collect -D & -m options as java arguments
> command=java
> while [ `echo $1 | egrep '<sup>-D|</sup>-m' | wc -l` != 0 ]; do
>         command="$command $1"
>         shift
> done
> 
> if [ -f ./Jmol.jar ] ; then
>   jarpath=./Jmol.jar
> elif [ -f $JMOL_HOME/Jmol.jar ] ; then
>   jarpath=$JMOL_HOME/Jmol.jar
> elif [ -f /usr/share/jmol/Jmol.jar ] ; then
>   jarpath=/usr/share/jmol/Jmol.jar
> else
>   echo Jmol.jar not found
>   exit
> fi
> $command -Xmx512m -jar $jarpath $`@`
> 
> 
> }}}
> 
> Is that file still needed?  I think it probably makes jmol work from the command line for us.


---

Comment by jason created at 2010-06-14 19:46:08

I've make a new sagenb-0.8.p3.spkg file that includes Jonathan's changes above (as an applied mercurial patch), plus the new jmol.  So to test this, all a person should have to do is:


```
sage -f http://sage.math.washington.edu/home/jason/sagenb-0.8.p3.spkg
```


It seems to work pretty well for me.  I wish the default was Medium Size instead of "small"


---

Comment by gutow created at 2010-06-14 19:58:51

Let's take some votes on the default size.  The problem with medium is that some people are still using screens as small as 800 x 600.  A 400 x 400 applet is likely to use more screen space than the user has allotted to the browser.  Maybe we should add a place where the user can set the default Jmol size in their notebook preferences?  At present it is just a variable set when jmol_lib.js is loaded.  We could certainly set it somewhere else in the web page.

Jonathan
Replying to [comment:11 jason]:
> It seems to work pretty well for me.  I wish the default was Medium Size instead of "small"


---

Comment by jason created at 2010-06-14 20:17:27

Replying to [comment:12 gutow]:
> Let's take some votes on the default size.  

I agree.


---

Comment by gutow created at 2010-06-14 20:33:19

The link to jmol.zip now leads to a clean zip archive (no .DS_Store files), with the jmol file (shell script) and  the Jmol.jar application file.  

Jason, I also wonder about your spkg name.  Wasn't the .py2.6 indicative of the python version?

Jonathan


---

Comment by jason created at 2010-06-14 20:39:33

Where is there a missing .py2.6?  I don't think I deleted anything with that name.

It's possible that whatever you are seeing happens at install time, rather in the source of the spkg, but I'm not sure what file you're talking about.


---

Comment by gutow created at 2010-06-14 20:45:50

I'm talking about this:
sagenb-0.8.p3.spkg
           ^^
In the download of sage 4.4.3 that I was looking at the notebook is included as an .egg in the directory structure.  I think I am confused by the .egg name versus the naming of the .spkg.  The .egg name is:

sagenb-0.8-py2.6.egg
           <sup>^</sup>^^
Since I've never built an egg or an spkg, I'm not sure of the significance.

Jonathan

Replying to [comment:15 jason]:
> Where is there a missing .py2.6?  I don't think I deleted anything with that name.
> 
> It's possible that whatever you are seeing happens at install time, rather in the source of the spkg, but I'm not sure what file you're talking about.


---

Comment by jason created at 2010-06-14 20:49:52

Ah.  What I did is create a new spkg, like in sage/spkg/standard/sagenb-0.8.p2.spkg.  When it installs into the python directory (using the "sage -f" command), the py2.6 egg stuff will be taken care of.


---

Comment by gutow created at 2010-06-14 20:54:58

Jason,

Once you've incorporated the new jmol.zip file, I suggest you update the description to include instructions on using your .spkg to test right near the top.  Or are your and I the only two who are going to look at this?

Jonathan


---

Comment by kcrisman created at 2010-06-14 21:00:31

No, you won't - pesky "someone else has already edited this page"!!!

Jonathan,

Sweet.  Great work!

Some comments upon a very small amount of testing (which is all I have time for right now).  I apologize for their telegraphic nature.

Popup 3dviewer is great.

Functions tab did not immediately have something in it, I had to click "request...", which is nonintuitive.  I understand if that step is necessary, but the message could be better; as it is, the person using it wouldn't necessarily realize that this would give mesh etc. info for each object (nice to do it separately, so so so nice).

Colorpicker in Functions tab: awesome.  

Initial size Small might be good for iPhone (if Jmol even works there?) but is a little on the small side for normal laptop/PC web browsing.   Can the browsing thing be detected for this?

There is an awful lot of space given to the info, not so much to the actual graphic.  Would it be possible to put that stuff below the image as opposed to on the right?  In fact, that stuff should not necessarily resize with the graphic...

State is cool for those of us who might want to access it, but it should default (when clicked upon) to creating a slider or something, or "click here for full" or something like that.  Otherwise the potential for really upsetting work flow is there, it changes the window size so much.

Sleep/Wake works great, might be nice to CSS those words into something less \texttt{}-ish.  Note that "Arbitrarily resizable in own window Get static image to save" looks like one command; maybe some <ul></ul> useful here?

Didn't break any old worksheets, though they all have this new little Jmol double window now, which makes sense.

This may be unrelated, but the axes seem to be in the wrong spots, at least in 

```
var('y')
P=plot3d(x^2+y^2,(x,-3,3),(y,-3,3))
Q=plot3d(sin(x^2+y^2),(x,-3,3),(y,-3,3))
show(P+Q)
```


I did *not* get to test having billions of applets open at the same time, unfortunately, but will be happy to do so if no one else can over the next week or two.  

One really interesting thing is this.  We had complaints about the snappiness of 3D interacts recently, but now I get almost instantaneous recomputation with 'small', which is great.  However

```
TypeError: Result of expression '(stateStr.match(re_modelinline))' [null] is not an object.
```

occurs if I change the size in an interact, and then move the slider.  Obviously, other things don't stay the same with an interact - say if I change one function to green, it goes back to blue after moving the slider, but there shouldn't be the error message (ideally).

But thank you!  This would be a big improvement.  Looking forward to being able to evaluate it properly - clearly a big change needs big testing.


---

Comment by gutow created at 2010-06-14 21:20:07

Replying to [comment:19 kcrisman]:
> Sweet.  Great work!
Glad you like it.
> 
> Some comments upon a very small amount of testing (which is all I have time for right now).  I apologize for their telegraphic nature.
> 
> Popup 3dviewer is great.
> 
> Functions tab did not immediately have something in it, I had to click "request...", which is nonintuitive.  I understand if that step is necessary, but the message could be better; as it is, the person using it wouldn't necessarily realize that this would give mesh etc. info for each object (nice to do it separately, so so so nice).
> 
You are correct that I could not originally get the information from Jmol on load because of timing issues.  I have an idea about this and will work on it a little.  In the meantime, I think you are correct that we need better instructions in this tab.
> Colorpicker in Functions tab: awesome.  
We use it for other Jmol stuff, but it was originally inspired by the needs of SAGE.
> 
> Initial size Small might be good for iPhone (if Jmol even works there?) but is a little on the small side for normal laptop/PC web browsing.   Can the browsing thing be detected for this?
> 
I believe we can get the surrounding window size.  I will look into that.  Maybe it should default to no more than 405 of width or height, whichever is higher?

> There is an awful lot of space given to the info, not so much to the actual graphic.  Would it be possible to put that stuff below the image as opposed to on the right?  In fact, that stuff should not necessarily resize with the graphic...
> 
I can play with the table formatting a little. I don't see any problems off the top of my head with it not resizing. I think underneath is a problem as the applet can be big enough that the controls will be off screen.

> State is cool for those of us who might want to access it, but it should default (when clicked upon) to creating a slider or something, or "click here for full" or something like that.  Otherwise the potential for really upsetting work flow is there, it changes the window size so much.
> 
Eventually I want it hidden.  But I think I can set it up to be scrolling....

> Sleep/Wake works great, might be nice to CSS those words into something less \texttt{}-ish.  Note that "Arbitrarily resizable in own window Get static image to save" looks like one command; maybe some <ul></ul> useful here?
> 
These are formatting issues that I can deal with easily.

> Didn't break any old worksheets, though they all have this new little Jmol double window now, which makes sense.
> 
Good!

> This may be unrelated, but the axes seem to be in the wrong spots, at least in 
> {{{
> var('y')
> P=plot3d(x<sup>2+y</sup>2,(x,-3,3),(y,-3,3))
> Q=plot3d(sin(x<sup>2+y</sup>2),(x,-3,3),(y,-3,3))
> show(P+Q)
> }}}
> 
That is likely to be a SAGE python bug as Jmol just draws lines where SAGE tells it to.  I will double check the parsing, but since the axes look correct for everything I've tried, I'm guessing something funny is passed to Jmol.

> I did *not* get to test having billions of applets open at the same time, unfortunately, but will be happy to do so if no one else can over the next week or two.  
> 
> One really interesting thing is this.  We had complaints about the snappiness of 3D interacts recently, but now I get almost instantaneous recomputation with 'small', which is great.
  
This is because I switched to using the incrementally loaded applet.  Thus only the parts needed are loaded.  This significantly reduces load time.


However
> {{{
> TypeError: Result of expression '(stateStr.match(re_modelinline))' [null] is not an object.
> }}}
> occurs if I change the size in an interact, and then move the slider.  Obviously, other things don't stay the same with an interact - say if I change one function to green, it goes back to blue after moving the slider, but there shouldn't be the error message (ideally).
> 
Is that completely reproducible?  I've seen it occasionally when javascript gets executed before the applets are completely loaded.  However, I've never seen any ill effects since things get reset later.  If it causes problems and you can pin it down, let me know.

Thanks for the initial testing.

Jonathan


---

Comment by kcrisman created at 2010-06-15 16:26:18

I want to point out that apparently Jmol won't load from the command line now.  I don't have time to revert the spkg right now, but at any rate things like

```
sage: point3d([0,0,1])
```

doesn't do anything now.  No applet, etc.


---

Comment by gutow created at 2010-06-15 16:59:12

Please check to see if the following two files are in the directory
sage/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol

Jmol.jar & Jmol (a shell script).

If they are not then try downloading the .spkg again to see if that fixes it.

If the files are there then there is something we don't understand or the path in the Jmol shell script is wrong.

Jonathan

Replying to [comment:23 kcrisman]:
> I want to point out that apparently Jmol won't load from the command line now.  I don't have time to revert the spkg right now, but at any rate things like
> {{{
> sage: point3d([0,0,1])
> }}}
> doesn't do anything now.  No applet, etc.


---

Comment by kcrisman created at 2010-06-15 17:02:19

Replying to [comment:24 gutow]:
> Please check to see if the following two files are in the directory
> sage/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol
> 
> Jmol.jar & Jmol (a shell script).
> 
Yup, both there (well, Jmol is jmol, but would that make the difference?).
> If the files are there then there is something we don't understand or the path in the Jmol shell script is wrong.
I want to emphasize things worked fine from the notebook.
> Replying to [comment:23 kcrisman]:
> > I want to point out that apparently Jmol won't load from the command line now.  I don't have time to revert the spkg right now, but at any rate things like
> > {{{
> > sage: point3d([0,0,1])
> > }}}
> > doesn't do anything now.  No applet, etc.


---

Comment by gutow created at 2010-06-15 17:42:28

Replying to [comment:25 kcrisman]:
I was correct it is a path issue caused by whomever set things up so that sagenb is inside an .egg with sage rather than simply its own directory structure.  It works fine if the following replacement is made in the shell file jmol:

JMOL_HOME="`"$SAGE_LOCAL"/bin/sage-pypkg-location sagenb`""sagenb/data/jmol"

is replaced by

JMOL_HOME="`"$SAGE_LOCAL"/bin/sage-pypkg-location sagenb`""sagenb-0.8-py2.6.egg/sagenb/data/jmol"

to account for the extra directory level that has been added.  Who do I ask about this?  I can fix the shell, but I want to make sure that the directory structure is supposed to have the .egg in it.

> Yup, both there (well, Jmol is jmol, but would that make the difference?).
> > If the files are there then there is something we don't understand or the path in the Jmol shell script is wrong.


---

Comment by gutow created at 2010-06-16 03:09:28

Jason,

Jmol.jar appears to be missing in the .spkg.  The .zip file on my site does have it.   You may want to rebuild the .spkg.  Maybe I need to learn to do this as well...where do I start?:)

Jonathan


---

Comment by gutow created at 2010-06-24 01:47:07

I've figured out how to make an spkg that only changes the files pertinent to Jmol.  Using this .spkg we should be able to test it against different versions of the notebook.  The only notebook specific file that is change is notebook_lib.js.  If using a notebook with changes to this file since Sage-4.4.3 a merge should be performed rather than a straight .spkg install.

I've have tried to address some of the issues mentioned above.  I still suggest installing to a test system.  A public example of this will also be available on my server (link to follow, once installed).

Version 1.1 of Jmol for Sage.  Install with command

sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg

or

./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg

depending on your command line syntax.

I'm also updating the ticket to show this instead of the first version.


---

Comment by gutow created at 2010-06-24 13:43:43

Example worksheet running on my test server is available here:

https://141.233.197.45:4443/home/pub/0/

Note the certificate is self-signed so you will get security warnings.  Don't worry about them.


---

Comment by gutow created at 2010-06-29 01:08:56

June 28, 2010---My server is down because of a power outage.  Hopefully, it wasn't killed and I will have it up again tomorrow.

Jonathan
Replying to [comment:29 gutow]:
> Example worksheet running on my test server is available here:
> 
> https://141.233.197.45:4443/home/pub/0/
> 
> Note the certificate is self-signed so you will get security warnings.  Don't worry about them.


---

Comment by gutow created at 2010-06-30 15:28:50

Server is back up.
Replying to [comment:30 gutow]:
> June 28, 2010---My server is down because of a power outage.  Hopefully, it wasn't killed and I will have it up again tomorrow.
>


---

Comment by gutow created at 2010-07-24 12:31:33

Working with 4.5


---

Comment by gutow created at 2010-09-05 19:48:35

There appears to be a javascript issue with the sleeping and waking. Sometimes when an applet is put to sleep the controls lose track of which applet they go with and stop modifying things.  I'm working on it.  There is probably an indexing error.


---

Comment by jason created at 2010-09-07 02:06:28

Thanks.  I'm keeping an eye on this; I believe that I now can review it officially relatively quickly (after the bug you mentioned is figured out).  So how about after the problem with sleeping/waking is figured out, another call for reviewers is sent to sage-devel, and I'll work on reviewing this more in-depth.

Thanks again for all of your work on this!


---

Comment by jason created at 2010-09-07 02:06:35

Changing status from new to needs_work.


---

Comment by gutow created at 2010-10-13 03:30:30

Changing status from needs_work to needs_review.


---

Comment by gutow created at 2010-10-13 03:30:30

Bug fixed.  Problem related to how the standard Jmol.js package interprets applet labels of zero.  The package version has been updated to 1.1.1.  This is fixed above so that nobody will download the wrong one.


---

Comment by jason created at 2010-10-13 03:47:06

Thanks!  I will try to look at this this next week.


---

Comment by jason created at 2010-10-13 03:47:50

CCing kcrisman, as it seems he'd be interested (or at least willing) to look at this as well.


---

Comment by gutow created at 2011-01-22 22:57:30

Changing assignee from jason, was to gutow.


---

Comment by kcrisman created at 2011-01-23 02:03:51

I tried installing this on a recent alpha of Sage:

```

Updating sagenb-0.8.10-py2.6.egg
removing old jmol_lib.js and notebook_lib.js…
New jmol_lib.js installed.
New notebook_lib.js installed.
removing Jmol*.jar and support files…
installing Jmol.jar and support files…
New Jmol*.jar and support files installed.

real	0m0.335s
user	0m0.012s
sys	0m0.075s
Successfully installed Jmol_for_SageNoteBook-1.1.1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing Jmol_for_SageNoteBook-1.1.1.spkg
```

So all seemed well.  But after ./sage -b, the Jmol applet now seems to be exactly as it was originally.  Did I miss something I was supposed to do other than ./sage -f this spkg?


---

Comment by gutow created at 2011-01-23 02:09:35

You beat me to finishing the update to the trac ticket.  Everything has been moved to the notebook google site.  This will not work with the latest release as the location of the notebook code has changed.  This .spkg will not properly update 4.6.1.

See http://code.google.com/p/sagenb/issues/detail?id=1  for details of what works with 4.6.1.  I will now finish updating this trac.

Sorry,
Jonathan
Replying to [comment:42 kcrisman]:
> I tried installing this on a recent alpha of Sage:
> {{{
> 
> Updating sagenb-0.8.10-py2.6.egg
> removing old jmol_lib.js and notebook_lib.js…
> New jmol_lib.js installed.
> New notebook_lib.js installed.
> removing Jmol*.jar and support files…
> installing Jmol.jar and support files…
> New Jmol*.jar and support files installed.
> 
> real	0m0.335s
> user	0m0.012s
> sys	0m0.075s
> Successfully installed Jmol_for_SageNoteBook-1.1.1
> Now cleaning up tmp files.
> Making Sage/Python scripts relocatable...
> Making script relocatable
> Finished installing Jmol_for_SageNoteBook-1.1.1.spkg
> }}}
> So all seemed well.  But after ./sage -b, the Jmol applet now seems to be exactly as it was originally.  Did I miss something I was supposed to do other than ./sage -f this spkg?


---

Comment by kcrisman created at 2011-01-23 02:31:02

Thanks for the clarification.  I have to say, since your ticket is the only listed 'issue' on that code.google.com site, I am not sure how useful that will be for people to help.  Of course, I've been against separating the sagenb out that much, because it becomes too easy to get out of the loop.

I have to say, though it now works, I'm still a little mystified, because the 'click to own 3d window' just gives a blank window (the Jmol doesn't appear, except brief Jmol logo), and if you click 'wake up' when it's already awake, it disappears too.  I wonder if they are related.  

But this will make it quite easy to review, at any rate, and hopefully that is just something silly I did.  This was with 4.6.2.alpha0.


---

Comment by gutow created at 2011-01-23 02:52:03

Replying to [comment:46 kcrisman]:
> Thanks for the clarification.  I have to say, since your ticket is the only listed 'issue' on that code.google.com site, I am not sure how useful that will be for people to help.  Of course, I've been against separating the sagenb out that much, because it becomes too easy to get out of the loop.
> 
I sort of wondered about that too, but since that is where the notebook is now hosted, I thought I should move this stuff there.

> I have to say, though it now works, I'm still a little mystified, because the 'click to own 3d window' just gives a blank window (the Jmol doesn't appear, except brief Jmol logo), and if you click 'wake up' when it's already awake, it disappears too.  I wonder if they are related.  
> 
Might be.  I can't reproduce it however on 4.6.1.  If I click the "Arbitrarily resizable in own window" it works fine from my server.  (Safari MacOSX, and FireFox with Linux.  There is a problem for logged in users with the way the notebook passes headers for Firefox on MacOS--this is long standing and probably part of Twisted.)  If you can send me more specifics I can try to track this down.  
> But this will make it quite easy to review, at any rate, and hopefully that is just something silly I did.  This was with 4.6.2.alpha0.
Thanks for looking at this.

Jonathan


---

Comment by kcrisman created at 2011-01-27 03:51:16

Here's a totally random (well, almost) question related to Jmol...  currently, I don't think we have a way of arranging several Jmols (or indeed any 3D graphics) in an array of some sort.  See [this ask.sagemath.org question](http://ask.sagemath.org/question/335/multiple-3d-plots-in-one-panel-graphics_array-and).  

Is this something that would even be conceivable with Jmol, or not?  I ask particularly because the new functionality seems to disallow the possibility of asking for "just" the graphic any more, which in retrospect perhaps is not so good - at least a keyword for `viewer='old_jmol'` or something could be useful.


---

Comment by gutow created at 2011-01-27 14:05:07

Essentially anything is possible if well defined.  It would be very easy to add a button that hides the controls or even in the notebook code allow for a parameter that launches Jmol without the controls and there is nothing that prevents making a table of Jmols.  The problem is we need a good definition of what is desired.  Should the 3-D plots in the table be static or live?  What about the size of the plots?  If they are live you can rapidly run up against browser memory constraints if the plots are too big.  I think this is doable, but would require some significant reworking of plot3d and the notebook code.  This is not my expertise. Almost everything I have done for this relates to the javascript code that supports Jmol in the notebook.

If we can get a specific list of desired behaviors, this might be a good summer project for a student.  I could certainly try to provide input on the javascript and Jmol control issues.
Replying to [comment:48 kcrisman]:
> Here's a totally random (well, almost) question related to Jmol...  currently, I don't think we have a way of arranging several Jmols (or indeed any 3D graphics) in an array of some sort.  See [this ask.sagemath.org question](http://ask.sagemath.org/question/335/multiple-3d-plots-in-one-panel-graphics_array-and).  
> 
> Is this something that would even be conceivable with Jmol, or not?  I ask particularly because the new functionality seems to disallow the possibility of asking for "just" the graphic any more, which in retrospect perhaps is not so good - at least a keyword for `viewer='old_jmol'` or something could be useful.


---

Comment by kcrisman created at 2011-02-22 17:49:46

Rather than do the spkg thing, I just dropped the appropriate files and directory exactly where they belonged in the sagenb tree.  

A brief tryout against 4.6.2.rc0 just now seems to have resolved the disappearance issues I had.  Right-clicking and 'About' gives the correct Jmol version.  

This needs more testing - I only have a few minutes between classes right now - but seems okay.  The only obvious issue is that when I click the help, I get that J. Gutow did this in Nov. 2009.  That should probably be changed, since it's now 2011 :)

For positive review, we need at least the following:

1. Testing on FF, Safari, IE
1. Testing on Linux, VM image on Windows, Mac
1. Making a sagenb spkg update that works properly

Related to this last, I am attaching a patch that is NOT the patch one would apply.  Making a new spkg would not be much harder.  The point is that .hgignore has `sagenb/data/jmol` in it, so that the only file that actually changes there is `jmol` itself, a script.  So the new spkg would have untracked changes in all the java files - probably a good thing, but worth being aware of.  Also, for some reason the way that I dropped the new files in did something weird, so that `sagenb/data/sage/js/jmol_lib.js` ends up only having +, not -, in its diff.

Also, I am going to post on sage-notebook to ask to just allow sagenb development on Trac for now.  No one has used the Google site except the author of this update!  Too confusing for now.


---

Comment by kcrisman created at 2011-02-22 17:50:35

I hate the wiki syntax here. 

Needs these things:

Testing on FF, Safari, IE.

Linux, VM on Windows, Mac

sagenb spkg update that works


---

Comment by kcrisman created at 2011-02-22 17:51:15

For review purposes only!  Diffs with previous files, apparently.


---

Attachment

>aware of.  Also, for some reason the way that I dropped the new files in did something weird, so that `sagenb/data/sage/js/jmol_lib.js` ends up only having +, not -, in its diff.

Not true, ignore this statement.


---

Comment by gutow created at 2011-02-22 18:20:19

So is there anything you guys need me to do.  Did I miss anything that isn't related to getting stuff into mercurial?
Jonathan
Replying to [comment:54 kcrisman]:
> >aware of.  Also, for some reason the way that I dropped the new files in did something weird, so that `sagenb/data/sage/js/jmol_lib.js` ends up only having +, not -, in its diff.
> 
> Not true, ignore this statement.


---

Comment by kcrisman created at 2011-02-22 20:00:10

Replying to [comment:55 gutow]:
> So is there anything you guys need me to do.  Did I miss anything that isn't related to getting stuff into mercurial?
> Jonathan

Well, of course it would be best if you could update the sagenb package.  But if you aren't familiar with HG, you shouldn't necessarily have to do this.  

The problem is that after sagenb became its own spkg, for a while there was a lot of activity and it was easy to update, but now the sagenb folks are much more dormant (with respect to sagenb, not in general) so one has to do this on one's own.  I hope to get some help making this spkg, though, and get people to test it/test it myself.


---

Comment by jason created at 2011-02-22 20:13:45

Just FYI, from the SPKG.txt file in devel/sagenb, here are the instructions for making a new sagenb spkg:


```
 * To release a new spkg, check that

   * All changes are committed.
   * .hgignore and MANIFEST.in are current.
   * The patch queue is clear.
   * The notebook runs.
   * The doctests pass: sage -t -sagenb
   * Test for ability to install without internet connection.
     Any dependencies that must be downloaded can be added in ./spkg-dist and in
serted
     in setup.py. Dependencies of dependencies need not be put in setup.py, but
     need to be put in ./spkg-dist.
   * The Selenium tests pass (optional, for now).

   Then,

   * Update the version in setup.py and commit this change.
   * Run spkg-dist.
   * Install and test the new spkg: sage -f dist/sagenb-*.spkg
```



---

Comment by kcrisman created at 2011-02-22 20:57:37

Thanks, Jason.  Just to confirm, one wouldn't need to use `./sage -pkg` to do this, just run `./path/to/it/spkg-dist`?  Also, I have no idea how to run Selenium tests!  Though this shouldn't really affect them, as there would be no changes to the notebook per se.


---

Comment by kcrisman created at 2011-02-22 21:10:25

Replying to [comment:58 kcrisman]:
> Thanks, Jason.  Just to confirm, one wouldn't need to use `./sage -pkg` to do this, just run `./path/to/it/spkg-dist`?  Also, I have no idea how to run Selenium tests!  Though this shouldn't really affect them, as there would be no changes to the notebook per se.
Answered my own question.  From `spkg-dist`:

```
# recent).  This script *does* need a sage executable to be in the PATH
# because we need to run "sage -pkg" below and also the "sdist" script
# runs "sage -python" and "sage -hg". -- Jeroen Demeyer
```



---

Comment by jason created at 2011-02-26 08:29:06

Some usage comments from playing with it again:

  * First, this is awesome!  Thanks for the huge amount of work you've put into it.
  * Under the Functions tab, clicking the link to get info from a sleeping JMOL gives an error and doesn't retrieve info
  * In firefox 3.6.13, OSX 10.6.6, changing the size of the applet to a smaller size seems to not recenter the image, so I end up with a smaller window that shows a corner of the object.  Sometimes changing the sizes back and forth several times leads to the object disappearing from the visible view.
  * (this may be hard)---it would be nice if there was some way for the java applet to gauge how much memory was left in the java system, so that instead of drawing a hard line of 5 awake applets, the applets could determine if they had enough memory to display, and if not, ask for another applet to go to sleep.
  * A lot of these next suggestions are for minimizing the interface the user has to interact with.  The purpose for this is to avoid confusing most users with a huge array of choices and options that they need to make.  The idea is to make most of these choices behind a right-click menu (if possible) so they are available to advanced users, but are not taking up space for most users.
  * When an applet is sleeping, it says "Sleeping...".  Maybe make that text instead say "Click to interact" and make it a link that is the same link as the "Wake this 3-D view" link is.
  * Is there a way to put the "Click to Sleep this 3-D view" and the "Help for Jmol 3-D viewer" in the right-click menu for the applet?
  * Can we make the display sizes and static image to save also links inside the jmol applet right-click menu?
  * Is the State box likely to be useful to lots of people?  If it is mainly a debug or developer thing, can we make it also a right-click menu thing?


---

Comment by jason created at 2011-02-26 08:33:08

I *love* the mesh feature.  It seems that sometimes I get artifacts in it, though.  For example, this code:

```
f(x,y)=x*cos(y)
plot3d(f,(x,-3,3),(y,-3,3))
```

produces an image like the attached "index.jpg" image (see attached files above).


---

Attachment

Those little white sparkles (artifacts in the mesh) seem to only happen at the intersection of mesh lines, if that helps diagnose what is going on.


---

Comment by gutow created at 2011-02-26 18:19:44

Replying to [comment:61 jason]:
Jason,

Thanks for all the comments.  I am still running a time deficit at the moment.  So probably cannot address any of these immediately.  Which are blockers?  If I know what to start on I may be able to squeeze a little time in between reviews and grading this week.

1)I think I know how to fix the issue with clicking links with sleeping applets.
2) The firefox problem cannot be fixed until the notebook passes information properly.  A number of things work poorly in FF on MacOS because the twisted server adds some html header information to files that are not html.  I've reported this as a bug long ago.  I don't know enough about the server to fix it easily.
3) Except for putting things in the right click menu most of your interface requests are doable.  How about a button that changes between an advanced options interface and a minimalist interface, rather than making them part of the right click menu?
Jonathan
> Some usage comments from playing with it again:
> 
>   * First, this is awesome!  Thanks for the huge amount of work you've put into it.
>   * Under the Functions tab, clicking the link to get info from a sleeping JMOL gives an error and doesn't retrieve info
>   * In firefox 3.6.13, OSX 10.6.6, changing the size of the applet to a smaller size seems to not recenter the image, so I end up with a smaller window that shows a corner of the object.  Sometimes changing the sizes back and forth several times leads to the object disappearing from the visible view.
>   * (this may be hard)---it would be nice if there was some way for the java applet to gauge how much memory was left in the java system, so that instead of drawing a hard line of 5 awake applets, the applets could determine if they had enough memory to display, and if not, ask for another applet to go to sleep.
>   * A lot of these next suggestions are for minimizing the interface the user has to interact with.  The purpose for this is to avoid confusing most users with a huge array of choices and options that they need to make.  The idea is to make most of these choices behind a right-click menu (if possible) so they are available to advanced users, but are not taking up space for most users.
>   * When an applet is sleeping, it says "Sleeping...".  Maybe make that text instead say "Click to interact" and make it a link that is the same link as the "Wake this 3-D view" link is.
>   * Is there a way to put the "Click to Sleep this 3-D view" and the "Help for Jmol 3-D viewer" in the right-click menu for the applet?
>   * Can we make the display sizes and static image to save also links inside the jmol applet right-click menu?
>   * Is the State box likely to be useful to lots of people?  If it is mainly a debug or developer thing, can we make it also a right-click menu thing?


---

Comment by gutow created at 2011-02-26 18:22:24

Replying to [comment:63 jason]:
> Those little white sparkles (artifacts in the mesh) seem to only happen at the intersection of mesh lines, if that helps diagnose what is going on.
I'll have to look into this.  That is a Jmol rendering issue.  A while back I know Bob Hanson tried to produce another way of making messes.  I haven't been able to get it to work reliably.  I'll put my head together with him, but this may take a while to fix.


---

Comment by jason created at 2011-02-26 21:04:01

I think these would resolve most of my concerns:

  * Under the Functions tab, clicking the link to get info from a sleeping JMOL gives an error and doesn't retrieve info 
  * When an applet is sleeping, it says "Sleeping...". Maybe make that text instead say "Click to interact" and make it a link that is the same link as the "Wake this 3-D view" link is. 
  * The controls to the right of the actual applet being hidden by default, with an "Advanced" button that makes the div slide out or slide back in.  We include jquery, so doing something with, for example, slideToggle (http://api.jquery.com/slideToggle/) might be really easy.


---

Comment by jason created at 2011-02-26 21:07:02

Actually, sliding in from the side might use one of:

  * http://api.jquery.com/animate/
  * http://jqueryui.com/docs/toggle/

See also http://www.learningjquery.com/2009/02/slide-elements-in-different-directions


---

Comment by jason created at 2011-02-26 21:07:54

(I might also look at how to toggle the advanced panel.  It would be, as you say, between grading exams from this week and normal work, probably sometime next week.


---

Comment by kcrisman created at 2011-02-26 21:17:14

Just a comment to Jonathan - William changed the description to have both sets of spkgs be 1.1.4, but I think that only one of them was supposed to be (to enable testing for sage > or < 4.5).  If that's so, please change the instructions back.  

Also still need

 * testing on Linux?  Or maybe Jason did that
 * at least SOME testing with a VM, if possible before release (?)
 * A new sagenb package, though that wouldn't be needed for positive review of this, it would just be needed for actually incorporating it :)


---

Comment by gutow created at 2011-02-27 21:31:19

Replying to [comment:69 kcrisman]:
> Just a comment to Jonathan - William changed the description to have both sets of spkgs be 1.1.4, but I think that only one of them was supposed to be (to enable testing for sage > or < 4.5).  If that's so, please change the instructions back.

You are correct.  I will change it back.  This is because I don't have an old install to test on and the package locations changed for the notebook.
  
> 
> Also still need
> 
>  * testing on Linux?  Or maybe Jason did that
I developed this on Linux, so this will work on Linux installs with a JVM that Jmol works in.  We only test against the Oracle/Sun JVM.

>  * at least SOME testing with a VM, if possible before release (?)
>  * A new sagenb package, though that wouldn't be needed for positive review of this, it would just be needed for actually incorporating it :)


---

Comment by jason created at 2011-03-01 04:34:19

apply after installing jmol spkg.  Apply to sagenb repository


---

Attachment

I attached a patch which adds an "Advanced Controls" button under the 3d applet which toggles the controls to the right.


---

Comment by kcrisman created at 2011-03-05 02:48:50

Third try... some comments from heavier testing.

 * For me, command line does not work.  I get a jmol window with 'zapped' and some other error message about a .sage/temp/....jmol file.  This could be because I just dragged in the files from the jmol spkg, but I wanted to be able to create a new sagenb spkg.  But changing the jmol script as indicated above didn't seem to help this.

 * Regular use seems to perform as advertised.

 * Jason's patch is necessary, works great.  However, it's worthless without changing that sleeping to a link to wake up, as Jason said, since not everyone will associate 'advanced' with waking up.

 * The smaller sizes don't seem to work so well with that patch.  It's hard to see what I mean until you try it.  It's possible for the miniature size to almost completely disappear.  Try spin on with that size - you'll get something coming in and out of view.

 * Heavy use is another matter.  I can get ALL kinds of horrible crashes (such as the ones that twice killed this comment, until I wised up and used a different browser for Trac) and other errors, some of which occurred above, others are new.  

The worst was when I was trying to open the page with 6 or 7 jmols, none of which I had evaluated, but were left over from earlier openings of the worksheet, and I tried to evaluate another cell and got a Java exception window that would not close, would not let me change focus to another browser window, and was completely full of security exceptions I did not understand.  Wow!  So we probably need to encourage people to be CAREFUL with this still.  

Interestingly, Chrome wouldn't even let me open it (and said, `Aw, snap` when it failed) because it spotted the problem early!  Actually, I find this to be a bug, because I never did open it, which didn't happen with FF and Safari.  It doesn't give the chance to just kill the script but still open the page.  Weird.


---

Comment by gutow created at 2011-03-05 17:57:12

Replying to [comment:74 kcrisman]:
OK.  Thanks for testing.  Two things:
1) I'm grading exams this weekend, but will try to look at this.
2) In order to look at what you are looking at I need to understand how I get things out of the mercurial system.  On a linux distro what would I need to set up?  

On the command line stuff.  We've had trouble because different operating systems use different protocols for opening java applications.  If you actually have a copy of the Jmol.jar (not JmolApplet.jar) then I will need more details about OS and so on.  This may relate to the fact that the location of the notebook code has changed.  I will look at that.

Jonathan
> Third try... some comments from heavier testing.
> 
>  * For me, command line does not work.  I get a jmol window with 'zapped' and some other error message about a .sage/temp/....jmol file.  This could be because I just dragged in the files from the jmol spkg, but I wanted to be able to create a new sagenb spkg.  But changing the jmol script as indicated above didn't seem to help this.
> 
>  * Regular use seems to perform as advertised.
> 
>  * Jason's patch is necessary, works great.  However, it's worthless without changing that sleeping to a link to wake up, as Jason said, since not everyone will associate 'advanced' with waking up.
> 
>  * The smaller sizes don't seem to work so well with that patch.  It's hard to see what I mean until you try it.  It's possible for the miniature size to almost completely disappear.  Try spin on with that size - you'll get something coming in and out of view.
> 
>  * Heavy use is another matter.  I can get ALL kinds of horrible crashes (such as the ones that twice killed this comment, until I wised up and used a different browser for Trac) and other errors, some of which occurred above, others are new.  
> 
> The worst was when I was trying to open the page with 6 or 7 jmols, none of which I had evaluated, but were left over from earlier openings of the worksheet, and I tried to evaluate another cell and got a Java exception window that would not close, would not let me change focus to another browser window, and was completely full of security exceptions I did not understand.  Wow!  So we probably need to encourage people to be CAREFUL with this still.  
> 
> Interestingly, Chrome wouldn't even let me open it (and said, `Aw, snap` when it failed) because it spotted the problem early!  Actually, I find this to be a bug, because I never did open it, which didn't happen with FF and Safari.  It doesn't give the chance to just kill the script but still open the page.  Weird.


---

Comment by kcrisman created at 2011-03-06 01:19:42

> OK.  Thanks for testing.  Two things:
> 1) I'm grading exams this weekend, but will try to look at this.
Well, first things first!  I was doing that until a few days ago.
> 2) In order to look at what you are looking at I need to understand how I get things out of the mercurial system.  On a linux distro what would I need to set up?  
I don't know what you need that for.  Luckily, it's all in Sage.  You can do

```
sage: hg_sagenb.[tab]
```

and everything is there, at least basic stuff.  In particular

```
sage: hg_sagenb.status()
```

and 

```
sage: hg_sagenb.import_patch('http://trac.sagemath.org...') 
```

are very useful.  This latter one MUST be used with the 'raw attachment', not just the link to the diff; you can just plug in the link to Jason's patch to see his contribution here.
> On the command line stuff.  We've had trouble because different operating systems use different protocols for opening java applications.  If you actually have a copy of the Jmol.jar (not JmolApplet.jar) then I will need more details about OS and so on.  This may relate to the fact that the location of the notebook code has changed.  I will look at that.
Yeah, you mention that.  I definitely have all the right stuff from that standpoint (e.g. Jmol.jar) but changing the `jmol` file (shell script) as you recommend above did not help with the 'zapped'.  

Jason, did your command line work?  I have the same setup as you, I think.  Maybe I should have just used the jmol spkg.


---

Comment by jason created at 2011-03-06 04:15:43

I can plot a 3d function from the command line.  A jmol instance pops up and I see and can interact with the plot.


---

Comment by jason created at 2011-03-06 04:29:10

I take that back---I had the old jmol installed.  I have the same thing that you have.  When I do this from the command line (OSX Snow Leopard):

```
sage: f(x,y)=x^2*y
sage: plot3d(f,(x,-3,3),(y,-3,3))
```


I get a jmol window that pops up, but the title bar says "zapped", the menu and title bar appear, but where the plot should be, it's only black with some red text.  The text says (where I've replaced my computer name with <MYCOMPUTERNAME>:

```
unrecognized file format for file /Users/grout/.sage/temp/<MYCOMPUTERNAME>/79036/tmp_0-size500.jmol

set defaultdirectory "/Users/grout/.sage/temp/<MYCOMPUTERNAME>/79036//tmp_0-size500.jmol.zip"

script SCRIPT
```



---

Comment by jason created at 2011-03-06 04:36:39

This is interesting.  Even though I get a black window and red text, if I click the "open" button in the upper left of the toolbar, and then select the tmp_0-size500.jmol
 file, and click the open button, the plot appears.  I'm not sure what is going on here.


---

Comment by gutow created at 2011-03-06 16:42:13

Replying to [comment:79 jason]:
Definitely a path issue.  Hope to finish my grading before dinner.  I will try to look at it this evening.
> This is interesting.  Even though I get a black window and red text, if I click the "open" button in the upper left of the toolbar, and then select the tmp_0-size500.jmol
>  file, and click the open button, the plot appears.  I'm not sure what is going on here.


---

Comment by kcrisman created at 2011-03-07 00:53:12

Okay, this is exactly what I was seeing as well.  Sorry I couldn't cut and paste it before - due to the crashing from heavy jmol testing!


---

Comment by gutow created at 2011-03-09 20:04:45

OK, I've traced the path issue with Jmol not launching from the command line.  There is an error in the path in the .jmol file created by SAGE.  Does anybody remember where in the code this is generated for the command line (not notebook)?  The issue is that  extra /'s are put into the path. (eg. ~/.sage//temp/..." instead of ~/.sage/temp/...".  If I can find where this is done in the code I can fix it.
Replying to [comment:81 kcrisman]:
> Okay, this is exactly what I was seeing as well.  Sorry I couldn't cut and paste it before - due to the crashing from heavy jmol testing!


---

Comment by kcrisman created at 2011-03-09 20:36:23

I'm not sure, but I think that 

```
sage: P = point3d((1,0,0))
sage: P.export_jmol?
```

might have what you are looking for.  I don't think it's the whole story, because I don't see the type of filename (including the size 500) that Jason is reporting, but at least it's a start.

Oh, and 

```

sage: search_src('jmol','size')
plot/plot3d/base.pyx:988:           figsize[0]. This is ignored for the jmol embedded renderer.
plot/plot3d/implicit_surface.pyx:69:# vertex_color/jmol_color), and output of size about n^2.
plot/plot3d/shapes2.py:750:        return ["draw %s DIAMETER %s {%s %s %s}\n%s" % (name, int(self.size), cen[0], cen[1], cen[2], self.texture.jmol_str('$' + name))]
server/notebook/cell.py:2246:                # If F ends in -size500.jmol then we make the viewer applet with size 500.
server/notebook/cell.py:2266:                #script = '<script>jmol_applet(%s, "%s");</script>%s' % (size, url, popup)
server/notebook/cell.py:2269:                script = '<div><script>jmol_applet(%s, "%s?%d");</script></div>' % (size, url, time.time())
```

suggests that maybe it's in server/notebook/cell.py, which is a little surprising, but line 2259 pretty much seals the deal:

```
                    jmol_script = jmol_script.replace('defaultdirectory "', 'defaultdirectory "' + self.url_to_self() + '/')
```

That looks like what you are describing.  Why is this called for non-notebook usage?


---

Comment by gutow created at 2011-03-09 21:09:51

Replying to [comment:83 kcrisman]:
I think what you've found is the stuff for the notebook, which does seem to be working.  I've found the following in the base.pyx file inside the plot3d directory, but am not sure what is going on.

```        
if 'filename' in kwds:
            filename = kwds['filename']
            del kwds['filename']
        else:
            filename = sage.misc.misc.tmp_filename()

        from sage.plot.plot import EMBEDDED_MODE, DOCTEST_MODE
        ext = None
[snip...]
        if DOCTEST_MODE or viewer=='jmol':
            # Temporary hack: encode the desired applet size in the end of the filename:
            # (This will be removed once we have dynamic resizing of applets in the browser.)
            base, ext = os.path.splitext(filename)
            fg = figsize[0]
            #if fg >= 2:
            #    fg = 2
            filename = '%s-size%s%s'%(base, fg*100, ext)
            ext = "jmol"
            archive_name = "%s.%s.zip" % (filename, ext)
            if EMBEDDED_MODE:
                # jmol doesn't seem to correctly parse the ?params part of a URL
                archive_name = "%s-%s.%s.zip" % (filename, randint(0, 1 << 30), ext)

            T = self._prepare_for_jmol(frame, axes, frame_aspect_ratio, aspect_ratio, zoom)
            T.export_jmol(archive_name, force_reload=EMBEDDED_MODE, zoom=zoom*100, **kwds)
            viewer_app = "sage-native-execute " + os.path.join(sage.misc.misc.SAGE_LOCAL, "bin/jmol")

            # We need a script to load the file
            f = open(filename + '.jmol', 'w')
            f.write('set defaultdirectory "%s"\n' % archive_name)
            f.write('script SCRIPT\n')
            f.close()
```


Somehow the building of "archive_name" is getting messed up.  I'm suspicious of 
 filename = sage.misc.misc.tmp_filename()
near the top or
 base, ext = os.path.splitext(filename)
in the viewer=='jmol' block.


---

Comment by kcrisman created at 2011-03-09 22:01:08

Oh, yeah, you've got it.  

```
sage: filename = sage.misc.misc.tmp_filename()
sage: filename
'/Users/<MYNAME>/.sage//temp/<MYCOMPUTERNAME>.local/77367//tmp_0'
```

and base gets that double slash.

But that part really comes from `sage.misc.misc.SAGE_TMP`, I think.

```
    while True:
        tmp = "%s/%s_%s"%(SAGE_TMP, name, __tmp_n)
        __tmp_n += 1
        if not os.path.exists(tmp):
            break
    return tmp
```


```
SAGE_TMP='%s/temp/%s/%s/'%(DOT_SAGE, HOSTNAME, os.getpid())
```


```
sage: sage.misc.misc.SAGE_TMP
'/Users/<MYNAME>/.sage//temp/<MYCOMPUTERNAME>.local/77367/'
```

which then has yet another / appended to it.  I guess this is helpful in the notebook?


---

Comment by jason created at 2011-03-09 22:28:29

Hmmm...it looks like those things should be using os.path.join, like this:

```
sage: os.path.join('test/','asdf')
'test/asdf'
sage: os.path.join('test','asdf')
'test/asdf'
```


Notice that there is no double-slash when using os.path.join.


---

Comment by jason created at 2011-03-09 22:29:18

In fact, why isn't that using the python tempfile module functions?


---

Comment by gutow created at 2011-03-09 23:01:20

OK, so this looks like a problem that will show up elsewhere too.  That double slash doesn't show up in the notebook because it uses different code.  Can this just be fixed or is this a bug/patch that needs to be checked elsewhere?


---

Comment by kcrisman created at 2011-03-10 01:15:34

Replying to [comment:86 jason]:
> Hmmm...it looks like those things should be using os.path.join, like this:
> {{{
> sage: os.path.join('test/','asdf')
> 'test/asdf'
> sage: os.path.join('test','asdf')
> 'test/asdf'
> }}}
Yeah, we had this problem with some of the temp files in e.g. R interface before.

As to the Python temp files, this is the system-wide `SAGE_TMP`, so you'd have to ask whoever wrote that why they didn't use builtin Python stuff - probably William or Tom or someone in prehistory...

As to Jonathan's question, I think this can just be fixed here for now, with a followup ticket for fixing it anyplace else it might cause problems.


---

Comment by kcrisman created at 2011-03-14 14:52:21

I successfully used os.path.join, but to no avail when it comes to the zapping.

In fact, after much playing around with this, I don't think it's the issue.  Remember the error message:

```
unrecognized file format for file /Users/grout/.sage/temp/<MYCOMPUTERNAME>/79036/tmp_0-size500.jmol

set defaultdirectory "/Users/grout/.sage/temp/<MYCOMPUTERNAME>/79036//tmp_0-size500.jmol.zip"

script SCRIPT
```

So jmol, while running, clearly resolves the // to /, otherwise it wouldn't give the correct error message.  (When the directory no longer existed, I got a !java.io.FileNotFoundException, quite different.)   And the directory that pops open when you use the open button is the correct directory.

So perhaps it's the 'unrecognized file format' that's the problem, in the sense of an unrecognized file format.   I'm continuing to dig; it seems that jmol's file recognizer/resolver is where the exception is thrown.


---

Comment by kcrisman created at 2011-03-14 14:52:21

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-03-14 15:45:31

Unfortunately, I can't afford to spend any more time on this, knowing as little about Jmol and Java as I do.  Here is some of the investigating I did, which _may_ be useful - hopefully it will be.  I suspect that there is something very subtle that changed in the newer Jmol (there have been changes) to this resolving business, and somehow the difference between the applet being used and just the standalone Jmol viewer must be involved.  

The changes made in `EMBEDDED_MODE=True` and the notebook code should not make a difference; the only substantive ones are that there is something random in the filename for the notebook, and the notebook rewrites the .jmol file to get the full url for the cell (as opposed to the full path to the file in the other case).  Neither of these should make a difference, right?

 * When Jmol looks to resolve the file, it 'smartly' actually reads the file and looks at the contents to see if it's one of a variety of accepted formats.
 * The code for this is [here](http://prodata.swmed.edu/CASP9/evaluation/jmol/src/org/jmol/adapter/smarter/Resolver.java), among other places (hopefully this isn't too old of a version - sadly, the sourceforge site requires one to download code, not browse, so this could all be based on something incorrect).
 * The only place there that this message occurs is in the following code, which means the !determineAtomSetCollectionReader has returned something with a newline character:

```
    } else {
      atomSetCollectionReaderName = determineAtomSetCollectionReader(
          bufferedReader, true);
      if (atomSetCollectionReaderName.indexOf("\n") >= 0)
        errMsg = "unrecognized file format for file " + fullName + "\n"
            + atomSetCollectionReaderName;
<snip>
    if (errMsg != null) {
      bufferedReader.close();
      return errMsg;
    }
```

 * Since the error message which is returned is the thing that Jason cut and pasted for us, you'll notice that the contents of our .jmol file itself is the output of the !determineAtomSetCollectionReader - so no surprise there is a `\n`, since after going through all the possible things, it returns the first several lines of the file, with `\n` in between lines.

```
    return (returnLines ? "\n" + lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" : null);
```

 * Of course, why this would work fine in the notebook AND when loading from the open window is completely mystifying to me.


---

Comment by gutow created at 2011-03-14 21:44:20

Replying to [comment:91 kcrisman]:
Thanks for digging.  I'm mystified too. As a state employee in Wisconsin, I'm rather busy right now, so haven't had much time to look at this.  I will try the os.path option and see if that works.  I know you don't think it does, but as you say it makes no sense.  When you open it with the open dialog you are using a properly formed path.  If I try the command line with the malformed path it does not work, but does from the command line with the proper path.

Maybe tonight or tomorrow.

Jonathan


---

Comment by gutow created at 2011-03-15 03:36:50

Replying to [comment:92 gutow]:
OK, I' verified that it still doesn't work with a good path on linux as well as MacOS.  I'll try a newer version of Jmol and some debugging. But that's all my time for today...


---

Comment by gutow created at 2011-03-15 04:21:54

Changing the extension on the .jmol file to .spt fixes the problem.  There is a specialized compressed file format that Jmol uses that is called a .jmol file.  We should consider putting everything in one of these, but I've been avoiding the effort while trying to get the interface to where people want it.  We should probably just change the file extension. Any objections?


---

Comment by jason created at 2011-03-15 04:56:30

You're the expert.  If you say so, and it works, I have no problem with changing the file extension!


---

Comment by kcrisman created at 2011-03-15 13:18:44

Replying to [comment:95 jason]:
> You're the expert.  If you say so, and it works, I have no problem with changing the file extension!
Agreed.  "The file can have any extension (though .spt is the acknowledged standard)."

The only conceivable objection I have is backwards compatibility, which I assume would only be the situation that if someone for some reason saved such a jmol file.  Otherwise as long as the functionality is precisely the same, I guess no problem.  This is great news.  

I still don't understand why it broke, though...


---

Comment by kcrisman created at 2011-03-15 15:15:26

I tried something like this, and it had the same response, except of course with spt instead of jmol.  But maybe I did something wrong and too naive.  Diff is attached, but only for reference.


---

Attachment

For reference only - do not apply.


---

Comment by gutow created at 2011-03-20 02:09:26

Replying to [comment:97 kcrisman]:
What you tried didn't work because you changed the extension on both files created by sage.  Adding the lines below after line 1115 to versin 4.6.2 ... plot3d/base.pyx makes Jmol work again from the command line on both Linux and MacOS:

            if not EMBEDDED_MODE:
                ext = "spt"#.spt is script extension
Sorry I haven't quite got the hang of using Mercurial yet.


---

Comment by gutow created at 2011-03-20 02:55:44

Replying to [comment:98 gutow]:
Oops! I really do have to get mercurial running...left out one line that needs changing...
the line 1116 needs to be replaced with
`f = open(filename + '.%s'%ext, 'w')`
 as well.
> Replying to [comment:97 kcrisman]:
> What you tried didn't work because you changed the extension on both files created by sage.  Adding the lines below after line 1115 to versin 4.6.2 ... plot3d/base.pyx makes Jmol work again from the command line on both Linux and MacOS:
> 
>             if not EMBEDDED_MODE:
>                 ext = "spt"#.spt is script extension
> Sorry I haven't quite got the hang of using Mercurial yet.


---

Comment by kcrisman created at 2011-03-21 12:52:34

Oh, ok - so I don't use the spt extension for everything, just the script itself, which calls the jmol zip archive.  I'll try that later today, and of course make a real patch for viewing if all goes well.


---

Comment by gutow created at 2011-03-21 13:32:38

Replying to [comment:100 kcrisman]:

Probably still won't work because of some problems with Jmol and the launch shell script.  I need help because I've got it working, but don't know how to make a patch that includes binary files (the necessary updated .jar files).  I've got a good patch for the updates to plot3d/base.pyx, but it doesn't fix everything without updates to the Jmol and its support files.  I'll upload the base.pyx patch below, but actually intended to add it to ticket 9232, which is about Jmol from the command line.  Do I need to build an .spkg for the Jmol stuff?


---

Comment by gutow created at 2011-03-21 13:35:59

plot3d/base.pyx fixes to launch Jmol from cmd line


---

Attachment

> Probably still won't work because of some problems with Jmol and the launch shell script.  I need help because I've got it working, but don't know how to make a patch that includes binary files (the necessary updated .jar files).  I've got a good patch for the updates to plot3d/base.pyx, but it doesn't fix everything without updates to the Jmol and its support files.  I'll upload the base.pyx patch below, but actually intended to add it to ticket 9232, which is about Jmol from the command line.  Do I need to build an .spkg for the Jmol stuff?

Hmm, those files are not being tracked by HG.  Otherwise any changes would be recorded, even binary ones.   But I think that we try not to track them because they are all binaries and we can't directly access them - hence the new spkg.

If the `isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;` stuff is just to fix the lighting in general, we could get that in a lot more quickly by simply opening another ticket, since it doesn't require a new SageNB package.  I *have* noticed that the top of surfaces was not well lit, as opposed to the bottom... but only in the notebook, not the command line, weirdly.  That part of this patch fixes that.  Any ideas as to what was going on with that?

But anything that is about changing those jmol files would have to be another package, though, I guess, because we don't track those files.  Why doesn't changing the extension just work 'out of the box'?


---

Comment by gutow created at 2011-03-21 16:02:43

Replying to [comment:102 kcrisman]:

> Hmm, those files are not being tracked by HG.  Otherwise any changes would be recorded, even binary ones.   But I think that we try not to track them because they are all binaries and we can't directly access them - hence the new spkg.

On  my machine I set it up to have hg track those files.  The patch I made does list them as being added or changed, but the binaries are not included, just the file names.  Thus the patch won't work.  I gather from what you are saying, an .spkg is the only way.  I can do that.  It will take a little time to reconfigure so that it is only updating the binary files.  The rest can be put in as a patch so it will be tracked properly.  (I'm getting less enthusiastic about hg...svn would  handle this with no problem).
> 
> If the `isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;` stuff is just to fix the lighting in general, we could get that in a lot more quickly by simply opening another ticket, since it doesn't require a new SageNB package.  I *have* noticed that the top of surfaces was not well lit, as opposed to the bottom... but only in the notebook, not the command line, weirdly.  That part of this patch fixes that.  Any ideas as to what was going on with that?

There was a bug in the version of Jmol things were originally written for, which meant the default lighting was fullylit (despite being documented as otherwise).  To update SAGE to a newer Jmol this needs to be accounted for.  The fix I put in is temporary.  I would like use a more complete and up-to-date file format for the generated .jmol files, but first I want to have basic stuff working.  Notebook vs command line depends on which version of the jmol_lib.js you have.  This fix is also in there.
> 
> But anything that is about changing those jmol files would have to be another package, though, I guess, because we don't track those files.  Why doesn't changing the extension just work 'out of the box'?

Changing the extension doesn't work out-of-the-box because of bugs in some versions of Jmol.  12.0.35 is the first 12.0.x series I could get this working with.  There are some newer versions, but the menu system has been damaged, so I am avoiding anything newer until we get that fixed.


---

Comment by kcrisman created at 2011-03-21 16:33:01

Yeah, we'd have to make a new spkg for that in any case.  We aren't interested in tracking them.  It surprises me that it doesn't include the binary files; we have other patches that do that.  I know nothing about relative merits of repository systems, though, so I can't comment on that.

I wonder if my default Sage somehow is using the new Jmol in the Sage installation I'm using to work on this?  Very odd.  Anyway, I understand that need for that fix for sure.  Thanks for keeping such careful track of which Jmol versions we can rely upon.  I hope we can get this sorted out in a week or two total; it would be really nice to finally have this finished, so that one could work on lower-level stuff which is perhaps actually easier to account for.


---

Comment by gutow created at 2011-03-22 15:16:59

Replying to [comment:104 kcrisman]:

OK, I've moved the fix to the launch on cmd to the existing trac 9232.  The fixes in that trac will have to be applied before any fixes to the new interface, but the new interface changes will now just be standard patches as they will only touch tracked files.  Please check out trac 9232.  I think we've got a complete fix.

I can now begin to work on addressing the notebook interface issues.  Hope to have a patch sometime today.


---

Comment by kcrisman created at 2011-03-22 16:11:19

See #9232 for Jmol at the command line.


---

Comment by gutow created at 2011-03-22 22:21:12

Patch of notebook_lib.js and jmol_lib.js for interactive enhancements to Jmol in notebook


---

Attachment

Ready for testing, but requires two steps.  Starting with a clean Sage 4.6.2:

 1. patch for Jmol at the command line. See [#9232](http://trac.sagemath.org/sage_trac/ticket/9232).
 1. Apply the patch trac_9238_interactive_js.patch above.

I have addressed the following issues (let me know if I've missed anything):

 * Addition of the ability to hide the "advanced controls".
 * Fix so that the advanced controls are hidden when the applet is asleep (no accidental calls to nonexistent applets).
 * Fix to issue of not properly loading all applets when a worksheet with a lot of applets is reopened (please check this one carefully).
 * Fixes to vocabulary and labels to make things clearer. 
 * Hidden the div with the State in it.  (Still there b/c I hope to be able to recreate the way the user left it on close, rather than starting fresh each time.)

Happy testing and thank you to those who do test!


---

Comment by gutow created at 2011-03-22 22:41:32

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-03-23 00:00:43

Does that mean that Jason's patch for hiding the advanced controls is subsumed in this?  It looks like it is, just checking.

Also, when you say it needs the patch for Jmol at command line in #9232, I assume that you also mean it needs the spkg/new Jmol files there.  You may want to then delete the instructions for testing that refer to loading previous versions of that spkg/new Jmol files above.  

Looking forward to trying this out!  Hopefully Jason can take some time to review the js stuff I'm not really qualified to while he's at Sage Days 29 :)


---

Comment by gutow created at 2011-03-23 01:29:47

Replying to [comment:108 kcrisman]:

> Does that mean that Jason's patch for hiding the advanced controls is subsumed in this?  It looks like it is, just checking.

Yes

> Also, when you say it needs the patch for Jmol at command line in #9232, I assume that you also mean it needs the spkg/new Jmol files there.  You may want to then delete the instructions for testing that refer to loading previous versions of that spkg/new Jmol files above.   Looking forward to trying this out!  Hopefully Jason can take some time to review the js stuff I'm not really qualified to while he's at Sage Days 29 :)

Yes, to get this all to work together  you need the complete update to Jmol.

I wasn't sure if it was appropriate to remove all the earlier stuff.  If your first pass at this looks pretty good.  I'll remove it.


---

Comment by kcrisman created at 2011-03-23 19:52:06

Update: This probably also requires the attachment called `trac_9232_notebook_fixes.patch` at #9232.   Or that could be combined into a total patch.  The issues with importing that patch should also be resolved.


---

Comment by kcrisman created at 2011-03-23 20:18:09

Replying to [comment:110 kcrisman]:
> Update: This probably also requires the attachment called `trac_9232_notebook_fixes.patch` at #9232.   Or that could be combined into a total patch. 
Now I think that might not be the case.  See below.

> The issues with importing that patch should also be resolved.

Okay, I experimented, and the change from angstrom to square root of umlaut O (which I think causes the problem) happens during the exporting of a patch.  See the sample I'm uploading next.  SO what needs to happen is for the sagenb package to 'manually' add this file, rather than by importing a patch, I guess?   

In fact, Jonathan, if there are no changes in the SageMenu.mnu file involved, we might want to let it remain untracked, except put a comment in the .hgignore file about _why_ it's untracked.  Unless you imagine needing to change it often (? I have no idea) it might be worth sparing the hassle over angstroms.  

Given Jonathan's comments, this could be some kind of Unicode bug on Mac...


---

Comment by kcrisman created at 2011-03-23 20:19:21

For reference only - do not apply, at least not until it's fixed!


---

Attachment

This [attachment:trac_9238-sagemenu-test.patch] is the offending change.  See line 361 and following where the weirdness begins.  But like I said, I don't think we actually need to add this to the repo; this is the vanilla version of this file already in Sage.


---

Comment by kcrisman created at 2011-03-23 20:24:14

To be more precise, adding JmolHelp.html sounds fine!  Just not the menu.


---

Comment by kcrisman created at 2011-03-23 20:28:34

And I've now checked, and there is NO difference between the files.  So maybe Jonathan can just add his JmolHelp.html and then we'll be set... as soon as someone who knows some Javascript reviews this :)  Otherwise I think we're finally on the way!


---

Attachment

Apply this as well


---

Comment by kcrisman created at 2011-03-23 20:54:26

After #9232, apply [attachment:trac_9238_interactive_js.patch] and [attachment:trac_9238-add-help.patch].


---

Comment by kcrisman created at 2011-03-23 21:26:53

Okay, in testing, it seems that 
 * The resizing of the "3-D display size: " is not working.
 * The pop-out window usually resizes appropriately, but for certain sizes that are just a little wider than tall, the image disappears.

I haven't noticed a lot of other problems as yet.  Lots of applets at once do seem to load properly.  Once in a while I have problems with some additional plot loading if I do an additional one, and once in a while a plot seems to disappear.  But the situation is certainly much better than before.


---

Comment by gutow created at 2011-03-23 21:41:10

Replying to [comment:116 kcrisman]:

> Okay, in testing, it seems that  * The resizing of the "3-D display size: " is not working. 
I assume you mean using the pop-up menu. I need OS, browser and java versions to work any more on that.  I've not seen what you describe.  
>* The pop-out window usually resizes appropriately, but for certain sizes that are just a little wider than tall, the image disappears. I haven't noticed a lot of other problems as yet.  Lots of applets at once do seem to load properly.  Once in a while I have problems with some additional plot loading if I do an additional one, and once in a while a plot seems to disappear.  But the situation is certainly much better than before.
This one is going to be very hard to track.  It sounds like I haven't quite figured out all the situations where there can be timing issues between the server and the notebook.  Again any specifics about how to reproduce would help.


---

Comment by gutow created at 2011-03-24 00:44:20

I've successfully run all the patches on a complete new Sage 4.6.2 installation with no errors.  I think we've got a clean working patch system now.  I've also added an example server people can visit to just review the interface.


---

Comment by gutow created at 2011-03-24 01:06:57

It appears that there are still some java memory issues if you have a lot of applets open and try to use the popup window that gives you a resizing view.  One possibility might be to sleep all applets in the main window when this is used.  I see this problem as not displaying the functions if the window is too big.


---

Comment by kcrisman created at 2011-03-24 01:35:49

> > Okay, in testing, it seems that  * The resizing of the "3-D display size: " is not working. 
> I assume you mean using the pop-up menu. 
No, I do not.  I'm referring to the advanced controls menu, where it says "3-D display size" and you can pick from four sizes. 
>I need OS, browser and java versions to work any more on that.  I've not seen what you describe.  

This is on Mac OS X.  With Safari 5.0.4 it doesn't seem to work at all, and does nothing bad.  With FF 3.6 it works, but has the same problems I mention somewhere above regarding the images not really fitting properly into the window.  

I wouldn't consider this a deal-breaker, but since it seems quite unreliable, maybe you can just comment that out for now until it's working more reliably?  As long as people can pop out the picture, that is the important thing.

> >* The pop-out window usually resizes appropriately, but for certain sizes that are just a little wider than tall, the image disappears. I haven't noticed a lot of other problems as yet.  Lots of applets at once do seem to load properly.  Once in a while I have problems with some additional plot loading if I do an additional one, and once in a while a plot seems to disappear.  But the situation is certainly much better than before.
> This one is going to be very hard to track.  It sounds like I haven't quite figured out all the situations where there can be timing issues between the server and the notebook.  Again any specifics about how to reproduce would help.
I think this is a small enough issue - only for certain window sizes and shapes - that it shouldn't block anything.

However, on FF if I pop it out, sometimes nothing at all shows up.  And in fact, just now it completely froze FF - as far as I know there weren't too many applets open, I just asked for it to pop up one too many times, maybe.

Is it possible that the extra applets from resizable pop-up windows could hog more Java memory than is supposed to be allowed? 

Sorry, that's the thing you just mentioned in your last comment.   Yes, I agree that something should be done with that.  It seems reasonable to perhaps sleep all applets in the main window except the same one, or maybe the last two.  

In fact, I wouldn't mind reducing from five 'awake' applets to four.   Anyway, this needs to be at least somewhat resolved, so 'needs work' for now.


---

Comment by kcrisman created at 2011-03-24 01:35:49

Changing status from needs_review to needs_work.


---

Comment by gutow created at 2011-03-24 02:53:22

Replying to [comment:120 kcrisman]:

I'm inclined to just remove the pop-up window initially.  I can keep working on it, but here are the issues:

 * I haven't been able to get anything working reliably in FF 3.X (and 4.0) on MacOS if the user is logged in.  I only get reliable applets that load if the worksheets are published.  I did a little sniffing around and found that the twisted server appends html header information to the script files with MacOS FF when the user is logged in.  I would need to do more investigating to provide a detailed bug report.  You can reproduce this by going to the example ([3-D Jmol examples](http://141.233.197.45:8888/home/pub/0)) and logging into the Test account (password: testing). I don't think this is the cause of the pop-up problem. 
 * The pop-up symptoms imply a JavaVM memory problem.  If you shrink the popup window down you will eventually get to a size where the image will display.  Unfortunately, different systems have different amounts of memory for the JavaVM, so it is very hard to predict how things will work.  I may be able to plug into the applet available memory information, but that will be somewhat involved, so not a rapid fix.
 * In short the server needs to be fixed before I can chase FF on MacOS problems.  I can address problems for FF on linux and windows, Webkit browsers (Safari) on MacOS, linux and windows.


---

Comment by kcrisman created at 2011-03-24 13:17:31

Okay, here are my recommendations.
 * To ensure good memory usage for many systems, reduce the number of 'awake' applets at any one time by one, to four.  Eventually this could be user-customizable, I suppose.
 * Remove the pull-down menu that says "3-D display size:" with different pixel sizes, as it either doesn't work or produces poor results.  In addition, at least in my testing on your server just now, I can't get the applet to sleep after I use that menu!  Pop-out still works in that case, though.
 * If it's not too hard, you could have the applets in main window sleep when you do a pop-out, except for the one you popped out (an instructor might want that smaller view immediately available after closing the pop-out window).

Otherwise I'm fine.

I think the pop-up windows are ok, actually.  It's a nice feature.  I have no problems making them when logged in.  The only issues are with the big resizing sometimes not working (but it's easy to find a size that does work) and that for some reason Command-W doesn't close the window.  Well, that doesn't work in MS Word, either, so no biggie.

>  the twisted server appends html header information to the script files with MacOS FF when the user is logged in.  I would need to do more investigating to provide a detailed bug report.  
Like I said, I didn't have this problem, even with your server and Mac FF, but you might as well put the info of where you found this info on the ticket somewhere.  Are you saying it's only with Mac, and only with FF, that this extra info is appended?

I'm going to test this on Safari again now, on an older Mac with FF, and then with IE and FF on my Windows Parallels.


---

Comment by kcrisman created at 2011-03-24 13:45:10

I'm baffled; now I do get the pull-down menu to work on Safari.  Anyway, the behavior of that is unreliable enough to warrant it not being used yet.  Plus, you can zoom in and out with scrolling - sort of like on Google maps.  Anyway.

Also, as a data point, Command-W does work to close the pop-out window on Safari.

One more *tiny* thing added to 'needs work':
 * Can you make it so that the "On?" checkbox is first, maybe even before the function name?  Otherwise it looks like we are asking to turn on the translucent, like with the mesh, which is confusing.


---

Comment by gutow created at 2011-03-24 14:34:31

Replying to [comment:122 kcrisman]:

> Okay, here are my recommendations. * To ensure good memory usage for many systems, reduce the number of 'awake' applets at any one time by one, to four.  Eventually this could be user-customizable, I suppose. * Remove the pull-down menu that says "3-D display size:" with different pixel sizes, as it either doesn't work or produces poor results.  In addition, at least in my testing on your server just now, I can't get the applet to sleep after I use that menu!

OK, I now see something like this in FF if I have lots of things (not just applets) open in FF 3.6.  I'm guessing another browser memory issue.  Doesn't reproduce in FF 4, which was just released.

> > the twisted server appends html header information to the script files with MacOS FF when the user is logged in.  I would need to do more investigating to provide a detailed bug report.
> Like I said, I didn't have this problem, even with your server and Mac FF, but you might as well put the info of where you found this info on the ticket somewhere.

Uh-Oh!  This is inconsistent behavior please post your MacOS, FF and JavaVM version #'s.

What I am seeing now is extra things appended to the filename sent to Jmol (I'd have to start a sniffer to check out the header stuff I've seen before).  So instead of a filename like "/home/Test/0/cells/1/sage0-size500.jmol" being passed to Jmol something like this is passed "/home/Test/0/cells/1/sage0-size500.jmol?1300976412".  So Jmol cannot find the data as that file doesn't exist.  Are you sure you don't see blank Jmols when you open the examples in FF when logged in to my example server?

Proper behavior is what I've seen with webkit browsers on MacOS and Linux.  Things work fine with FF on Linux as well.

The change in placement of the "on" checkbox for color can be changed.


---

Comment by kcrisman created at 2011-03-24 15:09:05

Replying to [comment:124 gutow]:
> Replying to [comment:122 kcrisman]:
> 
> > Okay, here are my recommendations. * To ensure good memory usage for many systems, reduce the number of 'awake' applets at any one time by one, to four.  Eventually this could be user-customizable, I suppose. * Remove the pull-down menu that says "3-D display size:" with different pixel sizes, as it either doesn't work or produces poor results.  In addition, at least in my testing on your server just now, I can't get the applet to sleep after I use that menu!
> 
> OK, I now see something like this in FF if I have lots of things (not just applets) open in FF 3.6.  I'm guessing another browser memory issue.  Doesn't reproduce in FF 4, which was just released.

Anyway, I still think that for now we can remove the pull-down menu (temporarily) if the pop-out window works ok.

> > > the twisted server appends html header information to the script files with MacOS FF when the user is logged in.  I would need to do more investigating to provide a detailed bug report.
> > Like I said, I didn't have this problem, even with your server and Mac FF, but you might as well put the info of where you found this info on the ticket somewhere.
> 
> Uh-Oh!  This is inconsistent behavior please post your MacOS, FF and JavaVM version #'s.

Hmm.  I have 10.6.7, FF 3.6.13, Jmol menu says I have Apple Java !1.6.0_24.

This time, it just totally froze FF.  Yes, blank Jmols.  But like I said, that didn't happen an hour ago.


---

Comment by gutow created at 2011-03-24 15:41:10

Replying to [comment:125 kcrisman]:

> Anyway, I still think that for now we can remove the pull-down menu (temporarily) if the pop-out window works ok.

But now we're both seeing that logged in users can't use FF (by the way I've seen this problem for a number of years even without any updates to Jmol or the notebook).  Can we recommend against using FF on MacOS as it doesn't work reliably anyway?

> > > > the twisted server appends html header information to the script files with MacOS FF when the user is logged in.  I would need to do more investigating to provide a detailed bug report.
> > > Like I said, I didn't have this problem, even with your server and Mac FF, but you might as well put the info of where you found this info on the ticket somewhere.
> > Uh-Oh!  This is inconsistent behavior please post your MacOS, FF and JavaVM version #'s.
> Hmm.  I have 10.6.7, FF 3.6.13, Jmol menu says I have Apple Java !1.6.0_24. This time, it just totally froze FF.  Yes, blank Jmols.  But like I said, that didn't happen an hour ago.

I'm testing against 10.6.6, but otherwise the same as you. (also just tested FF 3.6.14-same results). This gives me a little to go on, but I fear if we choose to call this a blocker we will be waiting for a significant notebook rewrite.  I could put in a browser check that pops up an alert for MacOS users telling them to use Safari if they have problems.


---

Comment by kcrisman created at 2011-03-24 16:58:04

> But now we're both seeing that logged in users can't use FF (by the way I've seen this problem for a number of years even without any updates to Jmol or the notebook).  Can we recommend against using FF on MacOS as it doesn't work reliably anyway?

No.  Way too many users default to FF on Mac OS, IIRC.

I tested this again on your server on two different Macs.  On the very old slow one (<1 GHz, FF 3.6.14), it was achingly slow, but no problems.  On my nice new one, I actually keep being able to freeze FF 3.6.13 with a wrong click here or there, but in general it worked; I didn't have empty Jmols.

In fact, the only empty Jmols I saw were ones that were just waiting to be seen; once I waited a little bit, they appeared.  Until I requested a function or something weird too early.  There must be some bad memory handling on FF 3.6 on Mac, maybe.  But the thing you are describing is not what I am seeing; certainly not trouble finding the Jmols themselves.  Can you borrow a colleague's Mac with FF to test this?

> I'm testing against 10.6.6, but otherwise the same as you. (also just tested FF 3.6.14-same results). This gives me a little to go on, but I fear if we choose to call this a blocker we will be waiting for a significant notebook rewrite.  I could put in a browser check that pops up an alert for MacOS users telling them to use Safari if they have problems.

I think that's not a bad idea.   As soon as a Java/Jmol is detected, if one has FF+Mac, the script for Jmol to the browser gives a little alert.  This shouldn't be default; lots of people use Sage without ever touching 3D plotting, and it could be confusing.


---

Comment by gutow created at 2011-03-24 17:13:55

Replying to [comment:127 kcrisman]:

> > Can we recommend against using FF on MacOS as it doesn't work reliably anyway?
> No. Way too many users default to FF on Mac OS, IIRC.

Makes sense.

> I tested this again on your server on two different Macs.  On the very old slow one (<1 GHz, FF 3.6.14), it was achingly slow, but no problems.  [snip. Can you borrow a colleague's Mac with FF to test this?

I'm in charge of about 30 computers for my department.  I've tried it on many of them with the same results.

> > I could put in a browser check that pops up an alert for MacOS users telling them to use Safari if they have problems.
> I think that's not a bad idea.   As soon as a Java/Jmol is detected, if one has FF+Mac, the script for Jmol to the browser gives a little alert.  This shouldn't be default; lots of people use Sage without ever touching 3D plotting, and it could be confusing.

So here are my priorities:

 1. Lower # of live Jmols (easy, I've got a place to do that.)
 1. Check Browser/OS combination before launch of first Jmol.  Pop alert if FF+MacOS.  Should I only do this for logged in users or always?
 1. Sleep all (or all but one) Jmol applet when pop-up Jmol is activated.

I'm just about to the end of my school break so I want to work on the highest priority things now.  Things will proceed much more slowly starting next week.


---

Comment by kcrisman created at 2011-03-24 19:28:25

> So here are my priorities:
Updated list:

 1. Lower # of live Jmols (easy, I've got a place to do that.)
 1. Check Browser/OS combination before launch of first Jmol.  Pop alert if FF+MacOS.  
 1. Sleep all (or all but one) Jmol applet when pop-up Jmol is activated.
 1. Remove pull-down menu for size of applet (pixel #)
 1. Move the 'On?' checkbox so it's clear what's being turned on.

As for the second one, whatever is easier for you is fine.  Are you _sure_ that this behavior was fairly frequent before?  I'd hate to have a lot of people complaining because we broke their Jmol.  I'm still perplexed by why you are so consistently getting these blank Jmols and I am not in FF.


---

Comment by kcrisman created at 2011-03-24 19:49:02

I just want to confirm that on another worksheet I just tried, I easily had five Jmols open in FF 3.6 on OS X 10.6 with no ill effects.  Adding a sixth slept the first.  I had to sleep one or two more in order to get the resizable window to open, but it worked fine.  

So I think that these things are the right list.  Alerting is ok but I don't know what's in the water there - maybe Lake Winnebago did something to your Java?  :)

Also, on Windows I don't get anything at all for IE 7.  Granted, IE 7 is old, and my guess is that this is just IE 7 in general, irrespective of the new Jmol.  I'll try later with a more current browser, and FF and Safari on that system.


---

Comment by gutow created at 2011-03-24 21:05:32

This really bothers me.  It is very inconsistent.  I did find a MacOS machine running FF3.3.  It sort of works.  Shows the same problem with the resizing applet, but will load most of a multiapplet notebook page when logged in.

If I can get the browser check working properly I will hide the pull-down menu only for the MacOS FF combination, since I don't think we've seen problems with it in any other cases.

I'll try to do some checking on some of our IE equipped machines tomorrow.


---

Comment by kcrisman created at 2011-03-25 01:49:14

> If I can get the browser check working properly I will hide the pull-down menu only for the MacOS FF combination, since I don't think we've seen problems with it in any other cases.
Yeah, I think my Safari problems with the pull-down menu must have been memory problems.
> I'll try to do some checking on some of our IE equipped machines tomorrow.
IE 7 doesn't work at all with Jmol, but even on XP it was no problem to upgrade to IE 8 and it worked ok there, except the "Toggle Advanced Controls" button didn't work at all.  Which means the functionality is the same as it was before, which is ok, I guess.

I managed to crash my Safari several times just now by trying to evaluate another cell (in a worksheet of mine) that would produce an applet while several were open.  Ordinarily that just sleeps one of the other ones, but this particular one must have a malformed applet in its directory or something.  I'm going to try to see what's going on with it.  The error message talks about height and width =0 but should be >0, so maybe that's a clue...


---

Comment by gutow created at 2011-03-25 12:58:40

The IE problem probably reflects IE not using standard javascript.  MS programmers seem to think they should use a different syntax than the  one agreed upon in the standards.  I will look into that.

I've sort of reproduced the Safari problem.  I've traced it to a js call in the standard Jmol.js package, which is rather odd.  That stuff is very well tested.  One possibility is that I've lost track of the appropriate applet names somehow in jmol_lib.js.


---

Attachment

fix to async load of many jmols and workaround for Safari bug (memory leak?)


---

Comment by gutow created at 2011-03-28 01:08:02

I need somebody to look at the latest patch to work around some Safari and asynchronous communication issues.  I think I may finally have it licked.  I've updated the description to include installing the new patch.


---

Comment by gutow created at 2011-03-28 02:26:38

More on the Safari problem.  It appears to be a memory problem that does not just depend on the number of applet.  It depends on the memory usage of the applets.  My patch only counts applets, so the workaround is not always successful.  Need a way to judge memory usage more closely at least to make Safari work.

Also note that older FF (<3.5) on MacOS seem to work OK.  It may be the 64 bit version of the browser or the JVM that is a problem.  Things look the worst on my newest machine.


---

Comment by gutow created at 2011-03-28 16:55:34

Some ideas for using less memory and getting more success loading multiple applets:

 * Don't turn on the antialiasing of the display.  Convert to an option in the applet tab with a warning that it uses more memory which may cause problems when lots of applets are used on one worksheet. (Displays will not be as nice, but uses about 1/2 the memory.  Static images will still be pretty).
 * set repaintWaitMs >1000 to allow more time for complex images to be drawn by applet.
 * set undo FALSE to save memory used for undo/redo in the console
 * make rough estimates of memory usage based on # of surfaces and size of each applet.  Use this to decide how many applets to keep alive...probably wouldn't help with the Safari problem which seems to occur after some amount of memory has been given to applets, even when later freed up.


---

Comment by jason created at 2011-03-28 20:27:47

I didn't even realize there was an undo/redo function.  Maybe we could turn it off, since there probably isn't a huge amount of scripting going on with Sage 3d plots.


---

Comment by kcrisman created at 2011-03-29 00:30:08

Things are a little bit of a mess because of the potential for flask changeover in SageNB.  What do people think of this?
 1. #9232 is used just for adding Volker's patch.  No sagenb change needed.
 1. Jonathan's patches there for the menu, help, and surface lighting/spt files are moved to this ticket.
 1. All the stuff here become part of the flask notebook changeover, and henceforth the property of those doing that :)
Otherwise this has the potential to just bitrot forever.


---

Comment by gutow created at 2011-03-29 00:38:18

I think this suggestion works.  The only problem is that Volker's patch really needs to be included in any update to Sage as well.  Can it be made high enough priority that it will be folded in?  The only other option I see is to include it here and close that ticket.


---

Comment by kcrisman created at 2011-03-29 01:20:33

Replying to [comment:140 gutow]:
> I think this suggestion works.  The only problem is that Volker's patch really needs to be included in any update to Sage as well.  
I don't see why it couldn't be folded immediately.  It is a very small change, and a sensible one - one that doesn't depend on any sagenb or jmol stuff.
>Can it be made high enough priority that it will be folded in?  The only other option I see is to include it here and close that ticket.
I don't think that will be necessary.  I think that making #9232 just about that makes sense.  His fix would work with both old and new Jmol, right?  I mean, it's just changing how the binary is called...


---

Comment by gutow created at 2011-03-29 02:31:25

What do we do to get #9232 folded in immediately?  Do we need some positive reviews? I agree that I don't think it depends on anything else.

I am trying to implement the memory usage reduction mentioned above as well as a fix for IE not showing advanced controls.  Another patch coming as soon as I figure this out.


---

Comment by gutow created at 2011-03-29 06:43:55

reduce Jmol memory usage try to make advanced toggle work in IE


---

Attachment


---

Comment by gutow created at 2011-03-29 07:06:28

This last patch tried to fix IE not working with advanced toggle button, but it didn't work.  Did significantly lower Jmol memory usage.  This should improve Safari performance.  Note this also gets rid of the white speckles that Jason complained about because no antialiasing is done.


---

Comment by kcrisman created at 2011-03-29 13:43:37

Okay, I've made it so that #9232 only modifies base.pyx _and_ fixes the lighting.  So [attachment:trac_9232_plot3d_base_pyx.patch] would need to remove that piece, which is fine, and in any case the name would be wrong.  The `spt` business only is necessary with the new Jmol, and #9232 isn't about that.

So from now on this ticket can feel free to focus only on Jmol update, and whatever is needed to make it succeed.  I'm really impressed by the amount of work you've put in on this, and I think it will soon bear good fruit, since it will be in the new notebook too.


---

Comment by jason created at 2011-03-29 14:01:40

Replying to [comment:144 gutow]:
> This last patch tried to fix IE not working with advanced toggle button, but it didn't work.  Did significantly lower Jmol memory usage.  This should improve Safari performance.  Note this also gets rid of the white speckles that Jason complained about because no antialiasing is done. 

+1 to turning off antialiasing (which is what we have currently with our old version of Jmol, right?) until we figure out that white sparkle issue with gridlines.

In Sage, you have jqueryui; I wonder if using a toggle button from jqueryui might be more cross-platform, if we're not using it now.


---

Comment by gutow created at 2011-03-29 14:51:27

Replying to [comment:146 jason]:

> In Sage, you have jqueryui; I wonder if using a toggle button from jqueryui might be more cross-platform, if we're not using it now.
We are using the jqueryui toggle() feature.  The problem seems to be with how IE handles calling strings as functions inside buttons.  I've tried forcing the use of eval(), but that didn't help.  May have to resort to a function call that calls toggle() on a string.


---

Comment by gutow created at 2011-04-02 18:25:05

Nice warnings for IE


---

Attachment

Fix to script file extension to work with new Jmol from command line


---

Comment by gutow created at 2011-04-02 19:27:00

Changing status from needs_work to needs_review.


---

Comment by gutow created at 2011-04-02 19:30:51

I cannot get everything working in IE.   I don't think we should hold things up for that.  I've made all the advanced features available in IE, some just fail quietly.  IE users get a dialog suggesting they use Chrome or FF until this is fixed.  IE (8 at least) is doing something funny.  Things that work once on a page often don't work again!

So I suggest this is ready for review.  I have had to change the patch sequence a little bit because of things removed from ticket #9232.  During testing please try this on a clean 4.6.2 to make sure I didn't miss anything.


---

Comment by kcrisman created at 2011-05-02 14:47:10

Jason, how much of this is in the current flask update?  Hopefully we can get this finished up at the Sage Days, for sure, since finals are rapidly approaching and we likely all won't have time to work on it in the immediate future.


---

Comment by jason created at 2011-05-02 15:06:29

Nothing is in the current flask update yet.  Well, I have a git branch where I applied an older version of the patches.  Finals are rapidly approaching, so I probably won't be able to work on this *too* much until two weeks from now.  I might be able to find time next week to work on it.


---

Comment by gutow created at 2011-06-13 17:05:57

Changing keywords from "" to "sd31".


---

Comment by was created at 2011-06-17 01:51:18

Some nitpicks with spkg-install in http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.7.spkg

1. Delete all the commented out code from spkg-install.  It is *not* comments, but code that makes no sense now.  It just makes it harder to read spkg-install.  The original code is in the hg history, anyways.

2. You use "cp -v" near the bottom, but this is not POSIX compliant, e.g., on Solaris we have:

```
wstein`@`t2:~$ touch a
wstein`@`t2:~$ cp -v a b
cp: illegal option -- v
Usage: cp [-f] [-i] [-p] [-`@`] f1 f2
       cp [-f] [-i] [-p] [-`@`] f1 ... fn d1
       cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-`@`] d1 ... dn-1 dn
```


(Yep, I learned something from David Kirkby.)


---

Comment by kcrisman created at 2011-06-17 02:26:59

> (Yep, I learned something from David Kirkby.)

 :)


---

Comment by gutow created at 2011-06-17 18:26:07

Fixed and refactored in http://www.uwosh.edu/faculty_staff/gutow/Jmol-12.0.45.p0.spkg .

Also see #11080 and latest comment of http://code.google.com/p/sagenb/issues/detail?id=1 

Replying to [comment:159 was]:

> Some nitpicks with spkg-install in http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.7.spkg 1. Delete all the commented out code from spkg-install.  It is *not* comments, but code that makes no sense now.  It just makes it harder to read spkg-install.  The original code is in the hg history, anyways. 2. You use "cp -v" near the bottom, but this is not POSIX compliant, e.g., on Solaris we have: ` wstein`@`t2:~$ touch a wstein`@`t2:~$ cp -v a b cp: illegal option -- v Usage: cp [-f] [-i] [-p] [-`@`] f1 f2 cp [-f] [-i] [-p] [-`@`] f1 ... fn d1 cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-`@`] d1 ... dn-1 dn ` (Yep, I learned something from David Kirkby.)


---

Comment by kcrisman created at 2011-08-19 02:26:01

Sorry to be dense, but what is the relation between this and #11503?  (I mean does one depend on the other?)


---

Comment by gutow created at 2011-08-19 02:48:55

I don't think that's dense.  It is confusing.  This ticket reflects the development before the Flask notebook.  As I was told we were switching over to Flask ASAP, I stopped working on things in the old version of the notebook.  However, I think this ticket belongs for people who want to incorporate an updated Jmol into pre-Flask versions of Sage.  Plus, I think it is good to lead people to the Flask version.

The .spkgs here would not install Jmol properly for setups that have made modifications as per #11503.  Should we say something about that?

Replying to [comment:165 kcrisman]:

> Sorry to be dense, but what is the relation between this and #11503?  (I mean does one depend on the other?)


---

Comment by kcrisman created at 2011-08-19 12:42:21

Well, in the meantime we aren't switching to Flask asap, so I might actually have time to test this over the next week or two and finally get it in.   Or are we just going to say we won't update Jmol and your nice changes until then?  

I think that having instructions (for instance, that #11503 can be done after this, but not the other way around) would be appropriate...


---

Comment by gutow created at 2011-08-19 12:49:35

In about 1.5 weeks I'll have time to look at this again.  I should be able to put together an spkg and the appropriate patches to make everything work without moving to Flask.  As we are ramping up for the semester, I don't think I will get to it before then.  Can we sit tight until then?  We've already missed 4.7.1 haven't we?


---

Comment by jason created at 2011-08-19 13:12:17

I talked with Rado the other day, and it seems like he's making a big push to get a lot of new stuff in and the bugs worked out while he has time before October.  My guess is that we'll see the flask notebook stabilize in mid- to late-September.


---

Comment by was created at 2011-08-24 23:36:36

Changing keywords from "sd31" to "sd31, sd32".


---

Comment by strogdon created at 2011-09-04 03:08:50

I've tested some of the features of this ticket on vanilla sage-4.7.2.alpha2 and I have some questions. I installed Jmol_for_SageNoteBook-1.1.6.spkg and applied the patches

```
trac_9238_interactive_js.patch
trac_9238-add-help.patch
trac_9238_jmol_lib_async.patch
```

The add-help patch would not apply with the response that a JmolHelp.html file already existed. I did not attempt to apply the IE patches. After applying the patches I issued "sage -b" and started sage and the notebook. Now when I load a worksheet that has Jmol applets I get pop-ups. If there are numerous applets, I get numerous pop-ups. These pop-ups seem to be triggered by the follow alerts in trac_9238_jmol_lib_async.patch

```
+    if(loading>=0){//we found a loading applet
+        jmolStatus.attempts[loading]+=1; //update number of checks for load completion.
+        if(jmolStatus.defaultdirectory[loading]=="done"){//Applet is ready.
+            jmolAppletLive(loading);
+            }else{ //Applet not ready. How many checks have we done?
+            if(jmolStatus.attempts[loading]==10){
+                alert("Jmol Applet #"+loading+" is having trouble loading.  Will retry once.");
+                var scriptStr = 'x=defaultdirectory; data "directory `@`x";';
+                scriptStr += 'set MessageCallback "jmolMessageHandler"; show defaultdirectory;';
+                jmolScript(scriptStr);
+                }
+            if(jmolStatus.attempts[loading]==20){
+                alert("Second attempt to finish launch of Jmol Applet #"+loading+" failed.  Recommend reevaluating the cell manually.");
+                jmolStatus.jmolArray[loading]=-2; //launch failed.
+                }
+            }
+        }else{//no loading applets. Search for queued applet.
```

since the quoted expressions in the alerts appear in the pop-ups. Loading the applets is extremely slow and the pop-ups have to be "clicked" before loading continues. Now if I do not install trac_9238_jmol_lib_async.patch then I do not get the pop-ups and the loading of the applets is much faster. I have used Firefox 3 and Firefox 6 with the same result. Are the pop-ups a feature or is the jmol_lib_async only intended for safari browsers?


---

Comment by gutow created at 2011-09-06 01:49:49

First, take note of the first paragraph of this ticket.  Because this involves working with the notebook interface all development since June 2011 has been on the Flask notebook version.  That means the package and patches here have not been updated since about 4.7.1.  They are up primarily so that people using 4.7.1 and older can get the controls that allow changing the display of surfaces.  Development has been limited to the Flask version of the notebook.  I have very limited time to work on this (I'm a chemistry professor), but if the Flask notebook is going to be severely delayed could try to package a version to work with the older notebook.  If you really want to test this you should test it in a Flask install (see the appropriate tickets).

That said your concerns about the patch warnings are valid.  I did not know that any of it had been folded into 4.7.2.  This is odd.

The pop-up warnings are because your server connection is relatively slow.  The notebook now allows about 15 seconds for an applet to load.  If it hasn't loaded by that time, one of these warnings pops up.  The idea is to provide some feedback when it takes a long time to load.  The reason for the async load code is that worksheets with lots of applets in them can overwhelm the browsers if too many applets try to load simultaneously.  This code requires them to load sequentially and limits worksheets to 4 running Jmol applets at a time.  Those that are not running are replaced with a picture and a button to wake them.  The primary reason for this is constraints on the memory available for applets within browsers.  The async code is for all browsers.  There are warnings associated with specific browsers that we have had difficulty with (e.g. MS IE and certain versions of FF and Safari).

If your worksheets worked without the async code, that suggests you were: 1) lucky; 2) had only one or very few applets in your worksheet.  If your worksheet did not work at all with the async code could you package it up so that we could test it in the latest code? Thanks.

Does this answer your questions?  I think the key message is that without more work on my part the enhanced Jmol interface may be tied to the Flask notebook.

Replying to [comment:172 strogdon]:

> I've tested some of the features of this ticket on vanilla sage-4.7.2.alpha2 and I have some questions. I installed Jmol_for_SageNoteBook-1.1.6.spkg and applied the patches ` trac_9238_interactive_js.patch trac_9238-add-help.patch trac_9238_jmol_lib_async.patch ` The add-help patch would not apply with the response that a JmolHelp.html file already existed. I did not attempt to apply the IE patches. After applying the patches I issued "sage -b" and started sage and the notebook. Now when I load a worksheet that has Jmol applets I get pop-ups. If there are numerous applets, I get numerous pop-ups. These pop-ups seem to be triggered by the follow alerts in trac_9238_jmol_lib_async.patch ` +    if(loading>=0){//we found a loading applet +        jmolStatus.attempts[loading]+=1; //update number of checks for load completion. +        if(jmolStatus.defaultdirectory[loading]=="done"){//Applet is ready. +            jmolAppletLive(loading); +            }else{ //Applet not ready. How many checks have we done? +            if(jmolStatus.attempts[loading]==10){ +                alert("Jmol Applet #"+loading+" is having trouble loading.  Will retry once."); +                var scriptStr = 'x=defaultdirectory; data "directory `@`x";'; +                scriptStr += 'set MessageCallback "jmolMessageHandler"; show defaultdirectory;'; +                jmolScript(scriptStr); +                } +            if(jmolStatus.attempts[loading]==20){ +                alert("Second attempt to finish launch of Jmol Applet #"+loading+" failed.  Recommend reevaluating the cell manually."); +                jmolStatus.jmolArray[loading]=-2; //launch failed. +                } +            } +        }else{//no loading applets. Search for queued applet. ` since the quoted expressions in the alerts appear in the pop-ups. Loading the applets is extremely slow and the pop-ups have to be "clicked" before loading continues. Now if I do not install trac_9238_jmol_lib_async.patch then I do not get the pop-ups and the loading of the applets is much faster. I have used Firefox 3 and Firefox 6 with the same result. Are the pop-ups a feature or is the jmol_lib_async only intended for safari browsers?


---

Comment by strogdon created at 2011-09-07 19:40:18

Replying to [comment:173 gutow]:

> First, take note of the first paragraph of this ticket.  Because this involves working with the notebook interface all development since June 2011 has been on the Flask notebook version.  That means the package and patches here have not been updated since about 4.7.1.  They are up primarily so that people using 4.7.1 and older can get the controls that allow changing the display of surfaces.  Development has been limited to the Flask version of the notebook.  I have very limited time to work on this (I'm a chemistry professor), but if the Flask notebook is going to be severely delayed could try to package a version to work with the older notebook.

No problem relative to time since things are rather busy here now too.

> If you really want to test this you should test it in a Flask install (see the appropriate tickets). That said your concerns about the patch warnings are valid.  I did not know that any of it had been folded into 4.7.2.  This is odd. The pop-up warnings are because your server connection is relatively slow.

I believe the server (desktop) is fast enough. The pop-ups seem to be associated with an inability to put certain applets in a sleep state. This code


```
x,y=var('x y'); plot3d( 4*x*exp(-x^2-y^2), (x,-2,2), (y,-2,2) )
```

generates an applet that can be put in a sleep state. If I replicate the code, say ten times, in a worksheet then I have no problem loading the saved worksheet with and without the async patch. I get four active applets and six that are sleeping. However, things are faster without the patch. The following code


```
x, y = var('x y');W = plot3d(sin(pi*((x)^2+(y)^2))/2,(x,-1,1),(y,-1,1), frame=False,color='purple', opacity=0.8);S = sphere((0,0,0),size=0.3, color='red', aspect_ratio=[1,1,1]);show(W + S, figsize=8)
```

generates an applet that cannot put in a sleep state, at least here it can't. The 'frame=False' option seems to be controlling the inability to do this. I get pop-ups with just one applet in a worksheet, even though the applet appears to have loaded within a second or two. Of course there are no pop-ups without the async patch. If I replicate the code, say six times, in a worksheet then loading the worksheet is extremely tedious with the async patch since for each applet I eventually get two pop-ups. As I mentioned, I don't believe the desktop is slow. Without the patch the applets load immediately, particularly when 'Action -> Evaluate All' is used; but only four or so of them can be re-evaluated if done individually. Then, I get a pop-up with


```
TypeError: stateStr.match(re_modelinline) is null
```

> The notebook now allows about 15 seconds for an applet to load.  If it hasn't loaded by that time, one of these warnings pops up.  The idea is to provide some feedback when it takes a long time to load.  The reason for the async load code is that worksheets with lots of applets in them can overwhelm the browsers if too many applets try to load simultaneously.  This code requires them to load sequentially and limits worksheets to 4 running Jmol applets at a time.  Those that are not running are replaced with a picture and a button to wake them.  The primary reason for this is constraints on the memory available for applets within browsers.  The async code is for all browsers.  There are warnings associated with specific browsers that we have had difficulty with (e.g. MS IE and certain versions of FF and Safari). If your worksheets worked without the async code, that suggests you were: 1) lucky; 2) had only one or very few applets in your worksheet.

Lucky, perhaps but I certainly have more than a few applets. I can't see where the second chunk of code would be associated with slowness. Perhaps the 'frame=False' option is triggering something it shouldn't?

> If your worksheet did not work at all with the async code could you package it up so that we could test it in the latest code? Thanks.

I would be nice to know if the same behavior is present in the flask-notebook. I could do this but it would take some time. Hopefully, the code I've provided can be easily tested by someone that has the flask stuff in place.

> Does this answer your questions?  I think the key message is that without more work on my part the enhanced Jmol interface may be tied to the Flask notebook.

Thanks for your feedback. It has caused me to look more carefully at what I've been doing. FWIW, the jmol issue surfaced in using the sage-on-gentoo port of Sage. There jmol has been outside the notebook for some time. But only recently, with jmol-12.0.45 and the patches of this ticket, have things started to act up. There is, not yet, a flask-notebook in sage-on-gentoo. And I'm guessing it won't be in sage-on-gentoo until it appears in Sage first. Therefore my ramblings here have been an attempt to determine whether vanilla Sage with the present notebook has the same issues as I have with sage-on-gentoo. It seems it does.


---

Comment by gutow created at 2011-09-07 23:44:35

Replying to [comment:174 strogdon]:

Thanks for the code snippets.  I have run them through a system with most of our latest patches in the flask version.  They do not seem to be problematic.  I had no trouble with a worksheet using your second (no-frame) example with 12 duplicates in a worksheet.  It does take a while to work its way back to the top from the 12th applet (about 25 seconds using my slow home connection).  This was a relatively severe test as the whole connection is encrypted as well, which slows things down further.  I did get a warning pop-up while the system was waiting for me to OK trusting the applet over the encrypted connection when I evaluated the first cell.  Once this was done things worked rapidly each time I evaluated an additional cell, because the applet was cached.

Does that sound like I checked everything?

Based on this test, I think I need to try to create a version of the patches that match the latest changes incorporated into the flask notebook, but can be applied to 4.7.2. I may have time this weekend.


---

Comment by gutow created at 2011-09-07 23:52:00

Replying to [comment:174 strogdon]:

I just found something.  Is this what you are describing?  I don't see it all the time, but I did manage to make it happen once, so should be able to trace it.  

1) Make a worksheet with lots of cells that evaluate to produce a jmol plot.

2) Do either of the following:

    a) select "delete all output", then select "evaluate all"

    b) select "evaluate all" without first deleting the output

3) What I see sometimes is that one of the applets does not load and then many of the cells do not evaluate to a jmol applet.  They can be recovered by manually clicking the evaluate button.


---

Comment by strogdon created at 2011-09-08 23:08:12

Replying to [comment:175 gutow]:

> Replying to [comment:174 strogdon]: Thanks for the code snippets.  I have run them through a system with most of our latest patches in the flask version.  They do not seem to be problematic.  I had no trouble with a worksheet using your second (no-frame) example with 12 duplicates in a worksheet.  It does take a while to work its way back to the top from the 12th applet (about 25 seconds using my slow home connection).  This was a relatively severe test as the whole connection is encrypted as well, which slows things down further.  I did get a warning pop-up while the system was waiting for me to OK trusting the applet over the encrypted connection when I evaluated the first cell.  Once this was done things worked rapidly each time I evaluated an additional cell, because the applet was cached. Does that sound like I checked everything?

This sounds good. If you get 12 applets to load in 25 seconds with the (no-frame) option then the flask implementation is definitely an improvement. With the async patch I'm able to load 12 applets, with frames, over nfs in about 40 seconds. I get one sequence of pop-ups after everything has loaded relative to trouble loading jmol Applet #0. However, with the (no-frame) option I get a sequence of pop-ups for each loading Applet. 

The odd behavior with "TypeError" in a pop-up seems to occur only if the async patch isn't applied. With the async patch and with frames doing either of

  a) select "delete all output", then select "evaluate all" 
  b) select "evaluate all" without first deleting the output

gives the above behavior of one sequence of pop-ups relative to loading jmol Applet #0. For the several times I've tried, all Applets do load.


---

Comment by kcrisman created at 2012-06-02 03:05:57

Hi Jonathan,

I've managed to get the Flask notebook installed in one of my development Sage installs, apparently, and it's summer, so I'd like to review #12299 so that it's ready to go in with the new notebook (likely in Sage 5.2, says jdemeyer).   Can you go through all the things here and maybe pick out any obvious things that should be hyper-tested, and put them on #12299?  I can't be sure, but reading through the comments it seems like most of the issues (including the command-line and Safari issues) were already resolved before this ticket became superseded by the new one?


---

Comment by gutow created at 2012-06-04 20:17:50

I think everything that was discussed above has been resolved.  The issues that are left are to get some tests from people other than me to find what else I've missed.  I've been running these modifications on the server I use for classes since last year, so I'm cautiously optimistic.  For all practical purposes, I think this ticket is closed and completely superseded by #12299.


---

Comment by kcrisman created at 2012-06-04 20:39:00

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-06-04 20:39:00

Okay, that sounds good.


---

Comment by jdemeyer created at 2012-09-05 07:17:05

Resolution: duplicate
