# Issue 4817: make an os x clickable .app launcher thing for sage automatically when one does -bdist on osx

Issue created by migration from https://trac.sagemath.org/ticket/4817

Original creator: was

Original creation time: 2008-12-16 17:32:27

Assignee: mabshoff


```

Hi sage-devel,

Thanks to some assistance from Dan and my chair/sysadmin, and a lot of
time trying to figure out vagaries of the not-for-the-faint-of-heart
documentation of Mac shell and Mac app property lists, I have the
following steps to make a Sage app clickable from anywhere which can
be easily changed to have it do the notebook instead.

I assume this can be turned into a .dmg (I don't know how to do that)
that could then be made available for download instead of the usual -
at least for major releases; the point is not to provide another
shortcut for the cognoscenti to make, but rather for easy instructions
for someone else (mabshoff? William?) to occasionally provide the app
for download when convenient for that person.

The point is that you should only have to do the following ONCE: after
that, all that has to happen is to plop a different Sage build where
it goes every time a new Sage build is made.  At least, I sure hope
so!

1. Create a folder called Sage.

2. Make a subfolder called Contents.

3. Go in Contents folder and make a subfolder called MacOS.

4. Drop entire sage installation for appropriate architecture/OSX
version in the MacOS folder.

5. Make the following script, name it Sage.command, make it executable
(e.g. "chmod 755 Sage.command"), and also place it in the MacOS
folder.  Note the grave accents (non-shifted tilde on most American
keyboards) in the second echo line.  This script creates a temporary
script which starts Sage, and then runs the new script (which deletes
itself once you log out of Sage, a nice touch).

#!/usr/bin/env sh

cmd=/tmp/SageStart_$$
echo '#!/usr/bin/env sh' > $cmd
echo `dirname $0`/sage/sage >> $cmd
echo "rm -f $cmd" >> $cmd
chmod 755 $cmd
open -a /Applications/Utilities/Terminal.app $cmd

6. Go back to the Contents folder and create the document Info.plist
below.  The CFBundleInfoDictionaryVersion may need to be different on
X.5 (I have X.4), and I made the last string 3.2.1 since that is the
Sage version I dropped in.

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://
www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
       <key>CFBundleDevelopmentRegion</key>
       <string>English</string>
       <key>CFBundleExecutable</key>
       <string>Sage.command</string>
       <key>CFBundleIdentifier</key>
       <string>com.sage.Sage</string>
       <key>CFBundleInfoDictionaryVersion</key>
       <string>6.0</string>
       <key>CFBundleName</key>
       <string>Sage</string>
       <key>CFBundlePackageType</key>
       <string>APPL</string>
       <key>CFBundleSignature</key>
       <string>????</string>
       <key>CFBundleVersion</key>
       <string>3.2.1</string>
</dict>
</plist>

7. Rename the Sage folder as Sage.app - you now have an application!
You may have to move Sage from whatever folder you started to
somewhere else, then back - this helps the Mac OS realize you have
made/changed the .plist file.

To make it a little nicer, add an icon:

A. Create a subfolder Resources in the Contents folder.

B. Add

       <key>CFBundleIconFile</key>
       <string>SageIcon.icns</string>

to the file Info.plist.

C. Assuming you have installed developer tools, open the program
/Developer/Applications/Utilities/Icon\ Composer.app/
and drag your favorite Sage icon into the boxes.  Save this as
SageIcon.icns in the Resources folder.


(If one hasn't installed the tools, probably any image would work if
you reference it in the .plist file, but I'm not sure about how Mac
would do it, so it might not.  Incidentally, I tried using the usual
Sage.png icosahedron for the .icns file, and found it is a little low
resolution; they like 128x128 pixels for the biggest, and Sage.png
seems to be 86x88.  On the other hand, it's a little busy for the icon
at the smallest levels.  Whatever.)

Incidental notes:

I. The user will still have to manually close the program and Terminal
window at the end of all this.  Terminal is what really launches.

II. To have it do the notebook instead, change the line

echo `dirname $0`/sage/sage >> $cmd

to

echo `dirname $0`/sage/sage -notebook >> $cmd

Of course, to change the file, you will now have to Ctrl-click on the
application and choose "Show Package Contents" to get to it again, or
use the command line.  Note that the user will have to Ctrl-C at the
end of this in the Terminal window - no way around that.

III. It would be great to actually have an interface etc - ideally,
one that just was an easy front end to Sage but also included the Help
menu, since one could just put the /doc folder in Resources and then
have it there, the canonical Mac way to do it.  Well, that will have
to wait for the oft-mentioned OSX guru.

I hope this is helpful to at least one other person.
```



---

Comment by mabshoff created at 2008-12-17 10:00:10

This should probably wait until 3.3, but it would be great if we could get this done for the AMS binaries.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-12 02:29:20

Any volunteers to make this happen?

Cheers,

Michael


---

Comment by iandrus created at 2009-02-03 19:51:43

The Sage.app skeleton


---

Attachment

changes to sage-bdist


---

Attachment

changes to sage-native-execute


---

Attachment

I hope no one was using the incorrect quoting of commandline parameters in sage-native-execute. I originally needed this change since I had sage-bdist call platypus directly, but I have since gotten rid of that so I guess I don't need those changes anymore.  Unfortunately, I didn't realize that until I had uploaded it.  I'm not sure how to delete it (though the patch should go in anyway IMHO).


---

Comment by mabshoff created at 2009-02-03 21:35:44

Ok, positive review, but there are a couple caveats:

 * the copyright notice should be changed to reflect the year as well as the Sage devs as authors of Sage
 * the second patch has the wrong path to the sage.app tarball, but I will post a patch that corrects that.
 * the sage.app tarball contains a couple extra index files which I will remove and post an updated patch for the extrepo.
 
A couple suggestions: 

 * it would be nice if we created sage-x.y.z.app, but renaming the obvious files does not work for me. Somebody ought to take a closer look. 
 * README needs to be updated since now one can just drag the app to any location and it will work.

Nice work!

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 23:59:16

Ivan's patch clean up - apply this patch to the bin repo only


---

Attachment

Apply on top of part1.


---

Comment by mabshoff created at 2009-02-04 00:35:04

Merged 

 * trac_4817_bin-cleaned_up.patch
 * trac_4817-ext-update-copyright.patch
 * trac_4817_part1.patch

in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 00:35:04

Resolution: fixed
