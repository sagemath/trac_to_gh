# Issue 4817: make an os x clickable .app launcher thing for sage automatically when one does -bdist on osx

archive/issues_004817.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n\nHi sage-devel,\n\nThanks to some assistance from Dan and my chair/sysadmin, and a lot of\ntime trying to figure out vagaries of the not-for-the-faint-of-heart\ndocumentation of Mac shell and Mac app property lists, I have the\nfollowing steps to make a Sage app clickable from anywhere which can\nbe easily changed to have it do the notebook instead.\n\nI assume this can be turned into a .dmg (I don't know how to do that)\nthat could then be made available for download instead of the usual -\nat least for major releases; the point is not to provide another\nshortcut for the cognoscenti to make, but rather for easy instructions\nfor someone else (mabshoff? William?) to occasionally provide the app\nfor download when convenient for that person.\n\nThe point is that you should only have to do the following ONCE: after\nthat, all that has to happen is to plop a different Sage build where\nit goes every time a new Sage build is made.  At least, I sure hope\nso!\n\n1. Create a folder called Sage.\n\n2. Make a subfolder called Contents.\n\n3. Go in Contents folder and make a subfolder called MacOS.\n\n4. Drop entire sage installation for appropriate architecture/OSX\nversion in the MacOS folder.\n\n5. Make the following script, name it Sage.command, make it executable\n(e.g. \"chmod 755 Sage.command\"), and also place it in the MacOS\nfolder.  Note the grave accents (non-shifted tilde on most American\nkeyboards) in the second echo line.  This script creates a temporary\nscript which starts Sage, and then runs the new script (which deletes\nitself once you log out of Sage, a nice touch).\n\n#!/usr/bin/env sh\n\ncmd=/tmp/SageStart_$$\necho '#!/usr/bin/env sh' > $cmd\necho `dirname $0`/sage/sage >> $cmd\necho \"rm -f $cmd\" >> $cmd\nchmod 755 $cmd\nopen -a /Applications/Utilities/Terminal.app $cmd\n\n6. Go back to the Contents folder and create the document Info.plist\nbelow.  The CFBundleInfoDictionaryVersion may need to be different on\nX.5 (I have X.4), and I made the last string 3.2.1 since that is the\nSage version I dropped in.\n\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple Computer//DTD PLIST 1.0//EN\" \"http://\nwww.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<dict>\n       <key>CFBundleDevelopmentRegion</key>\n       <string>English</string>\n       <key>CFBundleExecutable</key>\n       <string>Sage.command</string>\n       <key>CFBundleIdentifier</key>\n       <string>com.sage.Sage</string>\n       <key>CFBundleInfoDictionaryVersion</key>\n       <string>6.0</string>\n       <key>CFBundleName</key>\n       <string>Sage</string>\n       <key>CFBundlePackageType</key>\n       <string>APPL</string>\n       <key>CFBundleSignature</key>\n       <string>????</string>\n       <key>CFBundleVersion</key>\n       <string>3.2.1</string>\n</dict>\n</plist>\n\n7. Rename the Sage folder as Sage.app - you now have an application!\nYou may have to move Sage from whatever folder you started to\nsomewhere else, then back - this helps the Mac OS realize you have\nmade/changed the .plist file.\n\nTo make it a little nicer, add an icon:\n\nA. Create a subfolder Resources in the Contents folder.\n\nB. Add\n\n       <key>CFBundleIconFile</key>\n       <string>SageIcon.icns</string>\n\nto the file Info.plist.\n\nC. Assuming you have installed developer tools, open the program\n/Developer/Applications/Utilities/Icon\\ Composer.app/\nand drag your favorite Sage icon into the boxes.  Save this as\nSageIcon.icns in the Resources folder.\n\n\n(If one hasn't installed the tools, probably any image would work if\nyou reference it in the .plist file, but I'm not sure about how Mac\nwould do it, so it might not.  Incidentally, I tried using the usual\nSage.png icosahedron for the .icns file, and found it is a little low\nresolution; they like 128x128 pixels for the biggest, and Sage.png\nseems to be 86x88.  On the other hand, it's a little busy for the icon\nat the smallest levels.  Whatever.)\n\nIncidental notes:\n\nI. The user will still have to manually close the program and Terminal\nwindow at the end of all this.  Terminal is what really launches.\n\nII. To have it do the notebook instead, change the line\n\necho `dirname $0`/sage/sage >> $cmd\n\nto\n\necho `dirname $0`/sage/sage -notebook >> $cmd\n\nOf course, to change the file, you will now have to Ctrl-click on the\napplication and choose \"Show Package Contents\" to get to it again, or\nuse the command line.  Note that the user will have to Ctrl-C at the\nend of this in the Terminal window - no way around that.\n\nIII. It would be great to actually have an interface etc - ideally,\none that just was an easy front end to Sage but also included the Help\nmenu, since one could just put the /doc folder in Resources and then\nhave it there, the canonical Mac way to do it.  Well, that will have\nto wait for the oft-mentioned OSX guru.\n\nI hope this is helpful to at least one other person.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4817\n\n",
    "created_at": "2008-12-16T17:32:27Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "make an os x clickable .app launcher thing for sage automatically when one does -bdist on osx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4817",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/4817





---

archive/issue_comments_036451.json:
```json
{
    "body": "This should probably wait until 3.3, but it would be great if we could get this done for the AMS binaries.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T10:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This should probably wait until 3.3, but it would be great if we could get this done for the AMS binaries.

Cheers,

Michael



---

archive/issue_comments_036452.json:
```json
{
    "body": "Any volunteers to make this happen?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T02:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36452",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Any volunteers to make this happen?

Cheers,

Michael



---

archive/issue_comments_036453.json:
```json
{
    "body": "The Sage.app skeleton",
    "created_at": "2009-02-03T19:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36453",
    "user": "https://github.com/gvol"
}
```

The Sage.app skeleton



---

archive/issue_comments_036454.json:
```json
{
    "body": "Attachment [trac_4817_part1.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part1.patch) by @gvol created at 2009-02-03 19:52:30\n\nchanges to sage-bdist",
    "created_at": "2009-02-03T19:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36454",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_4817_part1.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part1.patch) by @gvol created at 2009-02-03 19:52:30

changes to sage-bdist



---

archive/issue_comments_036455.json:
```json
{
    "body": "Attachment [trac_4817_part2.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part2.patch) by @gvol created at 2009-02-03 19:53:18\n\nchanges to sage-native-execute",
    "created_at": "2009-02-03T19:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36455",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_4817_part2.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part2.patch) by @gvol created at 2009-02-03 19:53:18

changes to sage-native-execute



---

archive/issue_comments_036456.json:
```json
{
    "body": "Attachment [trac_4817_part3.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part3.patch) by @gvol created at 2009-02-03 19:56:43\n\nI hope no one was using the incorrect quoting of commandline parameters in sage-native-execute. I originally needed this change since I had sage-bdist call platypus directly, but I have since gotten rid of that so I guess I don't need those changes anymore.  Unfortunately, I didn't realize that until I had uploaded it.  I'm not sure how to delete it (though the patch should go in anyway IMHO).",
    "created_at": "2009-02-03T19:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36456",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_4817_part3.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817_part3.patch) by @gvol created at 2009-02-03 19:56:43

I hope no one was using the incorrect quoting of commandline parameters in sage-native-execute. I originally needed this change since I had sage-bdist call platypus directly, but I have since gotten rid of that so I guess I don't need those changes anymore.  Unfortunately, I didn't realize that until I had uploaded it.  I'm not sure how to delete it (though the patch should go in anyway IMHO).



---

archive/issue_comments_036457.json:
```json
{
    "body": "Ok, positive review, but there are a couple caveats:\n\n* the copyright notice should be changed to reflect the year as well as the Sage devs as authors of Sage\n* the second patch has the wrong path to the sage.app tarball, but I will post a patch that corrects that.\n* the sage.app tarball contains a couple extra index files which I will remove and post an updated patch for the extrepo.\n \nA couple suggestions: \n\n* it would be nice if we created sage-x.y.z.app, but renaming the obvious files does not work for me. Somebody ought to take a closer look. \n* README needs to be updated since now one can just drag the app to any location and it will work.\n\nNice work!\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T21:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_036458.json:
```json
{
    "body": "Ivan's patch clean up - apply this patch to the bin repo only",
    "created_at": "2009-02-03T23:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ivan's patch clean up - apply this patch to the bin repo only



---

archive/issue_comments_036459.json:
```json
{
    "body": "Attachment [trac_4817-ext-update-copyright.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817-ext-update-copyright.patch) by mabshoff created at 2009-02-04 00:05:49\n\nApply on top of part1.",
    "created_at": "2009-02-04T00:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4817-ext-update-copyright.patch](tarball://root/attachments/some-uuid/ticket4817/trac_4817-ext-update-copyright.patch) by mabshoff created at 2009-02-04 00:05:49

Apply on top of part1.



---

archive/issue_comments_036460.json:
```json
{
    "body": "Merged \n\n* trac_4817_bin-cleaned_up.patch\n* trac_4817-ext-update-copyright.patch\n* trac_4817_part1.patch\n\nin Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T00:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 

* trac_4817_bin-cleaned_up.patch
* trac_4817-ext-update-copyright.patch
* trac_4817_part1.patch

in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_036461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T00:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4817#issuecomment-36461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005061.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-04T00:35:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4817#event-5061"
}
```
