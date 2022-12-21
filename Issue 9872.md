# Issue 9872: Create Mac Application that people love to use

Issue created by migration from Trac.

Original creator: iandrus

Original creation time: 2010-09-08 07:16:09

Assignee: iandrus

CC:  kcrisman jason georgsweber mhampton mpatel

Keywords: mac

Many people want a Mac application, but so far none has appeared that was worthy of the name Sage.  This must change!  We need something which can launch terminal sessions, install spkg files, run and provide quicklook support for sage files.  Something that can be used as a MenuExtra, and optionally act as a primitive browser for the notebook.

Is such a thing even possible?  Yes!  In fact such an application is almost here!


---

Comment by jason created at 2010-09-08 13:04:12

I'm excited!

Also, Ivan: the author field should contain your full name.


---

Comment by iandrus created at 2010-09-08 13:13:57

A readme for Sage.app


---

Attachment

This will supersede #5296 if it gets in first.


---

Comment by iandrus created at 2010-09-08 13:53:43

Changing status from new to needs_review.


---

Comment by jason created at 2010-09-08 13:58:46

As Ivan points out in the sage-devel email: #8473 is related


---

Comment by jason created at 2010-09-08 14:09:04

I assume the "scripts" patch should be applied to the $SAGE_ROOT/local/bin repository?


---

Comment by iandrus created at 2010-09-08 14:28:27

Replying to [comment:6 jason]:
> I assume the "scripts" patch should be applied to the $SAGE_ROOT/local/bin repository?

Yes.  I think that's what hg_scripts points to, so that's why I called it "scripts".


---

Comment by kcrisman created at 2010-09-08 14:42:54

Replying to [comment:3 iandrus]:
> This will supersede #5296 if it gets in first.
Incorrect.  There are two READMEs in operation.

One is the one that gets bdisted to the top level of the dmg disk image, and has information like is on [here](http://trac.sagemath.org/sage_trac/attachment/ticket/5296/sage-README-osx.2.txt).  This one is more about the app bundle itself, not about how to use Sage for an absolute beginner.  

That doesn't mean they couldn't be combined, but for now they clearly address two different things.

Also, there's a typo in the comment on line 101 of the script patch.


---

Comment by jason created at 2010-09-08 14:56:54

Here is what appears when I do the bdist:


```
Sage works!
Copying files over to tmp directory
cp: *.sage: No such file or directory
Copying Sage library over
Making empty spkg's
There will be an error about x below that you can safely ignore.
mv: rename x to x/x: Invalid argument
If you wish to create a Mac Application please set
SAGE_APP_BUNDLE=yes
Creating dmg
(If you don't wish to create a disk image please set SAGE_APP_DMG=no)
............................................................
created: /Users/grout/sage-4.5.2/tmp/sage-4.4.2-i386-Darwin.dmg
Moving final distribution file to /Users/grout/sage/dist
```


1. The note about setting SAGE_APP_BUNDLE=yes should probably be deleted now, since it is done by default?

2. It'd be nice if the two other errors about moving/copying were taken care of, but they might be from other things in bdist and not be applicable to this ticket.


---

Comment by kcrisman created at 2010-09-08 15:02:30

Respecting 2., I think that the other errors are ok.  The first means that you must not have a .sage profile or whatever in your home directory (at least I think that is the point); the second one has been in this since the earliest days, and is definitely not related to the app bundle issue.  If you don't like them, that would be a separate ticket, in my opinion; they are longstanding.

Putting myself in reviewer since I already put in quite a bit of feedback before this hit primetime - but lots more review needed!


---

Comment by jason created at 2010-09-08 15:08:02

I spoke too soon.  I thought the app DMG would be created by default, but apparently it isn't, and I still need to set SAGE_APP_BUNDLE=yes.  I guess this is okay, as usually people would just download the app directly.


---

Comment by jason created at 2010-09-08 15:08:28

(if not creating an app dmg is going to be the default, then we can delete the note about SAGE_APP_BUNDLE=no)


---

Comment by kcrisman created at 2010-09-08 15:17:25

Something must have gotten messed up here.  Ivan, I think the idea was that the app bundle would be the default once we could do both Terminal and Notebook in the same app, right?  At least, that was my strongly encouraged idea :)  One should be able to NOT do the bundle, but the default should be the bundle (same with dmg versus tar.gz).  So maybe the scripts patch needs a change.


---

Comment by iandrus created at 2010-09-08 15:39:24

Replying to [comment:13 kcrisman]:
> Something must have gotten messed up here.  Ivan, I think the idea was that the app bundle would be the default once we could do both Terminal and Notebook in the same app, right?  At least, that was my strongly encouraged idea :)  One should be able to NOT do the bundle, but the default should be the bundle (same with dmg versus tar.gz).  So maybe the scripts patch needs a change.

The reason that I didn't make building the app default is that last time I did that I got in trouble :-)  Well I just had to back out that portion.  I'm happy to make it the default though if people think it should be.  We should probably ask on sage-devel first though since it may catch people off guard (the message doesn't come until near the end of a long process).


---

Comment by jason created at 2010-09-08 15:58:49

I just applied both patches and tried building with the SAGE_APP_BUNDLE=yes, and got errors:


```
grout`@`tiny:~/sage/dist% export SAGE_APP_BUNDLE=yes
grout`@`tiny:~/sage/dist% sage -bdist 4.4.2-app     
Sage works!
Copying files over to tmp directory
cp: *.sage: No such file or directory
Copying Sage library over
Making empty spkg's
There will be an error about x below that you can safely ignore.
mv: rename x to x/x: Invalid argument
Building the Mac Application
Build settings from command line:
    ARCHES = ppc ppc64 i386 x86_64


### BUILD NATIVE TARGET Sage OF PROJECT Sage WITH CONFIGURATION Debug
Check dependencies
ProcessInfoPlistFile build/Debug/Sage.app/Contents/Info.plist Sage-Info.plist
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    builtin-infoPlistUtility Sage-Info.plist -genpkginfo /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/PkgInfo -expandbuildsettings -platform macosx -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Info.plist

error: The file “Sage-Info.plist” couldn’t be opened because there is no such file.
The file “Sage-Info.plist” couldn’t be opened because there is no such file.
CpResource build/Debug/Sage.app/Contents/Resources/English.lproj/Credits.html English.lproj/Credits.html
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/Credits.html /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources/English.lproj

CompileXIB English.lproj/MainMenu.xib
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/usr/bin/ibtool --errors --warnings --notices --output-format human-readable-text --compile /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources/English.lproj/MainMenu.nib /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib

/* com.apple.ibtool.document.notices */
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:551: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:547: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:1268: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:1252: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:1320: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:549: note: This view is clipping its content.
This view is clipping its content.
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MainMenu.xib:1315: note: This view is clipping its content.
This view is clipping its content.
CpResource build/Debug/Sage.app/Contents/Resources/appl.icns appl.icns
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/appl.icns /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: appl.icns: No such file or directory
pbxcp: appl.icns: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/Defaults.plist Defaults.plist
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/Defaults.plist /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: Defaults.plist: No such file or directory
pbxcp: Defaults.plist: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-document-py.icns sage-document-py.icns
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-document-py.icns /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-document-py.icns: No such file or directory
pbxcp: sage-document-py.icns: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-document-spkg.icns sage-document-spkg.icns
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-document-spkg.icns /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-document-spkg.icns: No such file or directory
pbxcp: sage-document-spkg.icns: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-document-sage.icns sage-document-sage.icns
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-document-sage.icns /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-document-sage.icns: No such file or directory
pbxcp: sage-document-sage.icns: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-document-sws.icns sage-document-sws.icns
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-document-sws.icns /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-document-sws.icns: No such file or directory
pbxcp: sage-document-sws.icns: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-small-blue.png sage-small-blue.png
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-small-blue.png /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-small-blue.png: No such file or directory
pbxcp: sage-small-blue.png: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-small-grey.png sage-small-grey.png
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-small-grey.png /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-small-grey.png: No such file or directory
pbxcp: sage-small-grey.png: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-small-green.png sage-small-green.png
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-small-green.png /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-small-green.png: No such file or directory
pbxcp: sage-small-green.png: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/sage-small-red.png sage-small-red.png
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/sage-small-red.png /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

pbxcp: sage-small-red.png: No such file or directory
pbxcp: sage-small-red.png: No such file or directory
CpResource build/Debug/Sage.app/Contents/Resources/start-sage.sh start-sage.sh
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/start-sage.sh /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

CpResource build/Debug/Sage.app/Contents/Resources/open-location.sh open-location.sh
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/open-location.sh /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

CpResource build/Debug/Sage.app/Contents/Resources/loading-page.html loading-page.html
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/loading-page.html /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources

CopyStringsFile build/Debug/Sage.app/Contents/Resources/English.lproj/InfoPlist.strings English.lproj/InfoPlist.strings
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv ICONV /usr/bin/iconv
    /Developer/Library/Xcode/Plug-ins/CoreBuildTasks.xcplugin/Contents/Resources/copystrings --validate --inputencoding utf-8 --outputencoding UTF-16 English.lproj/InfoPlist.strings --outdir /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources/English.lproj

CompileXIB English.lproj/MyDocument.xib
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /Developer/usr/bin/ibtool --errors --warnings --notices --output-format human-readable-text --compile /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources/English.lproj/MyDocument.nib /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MyDocument.xib

/* com.apple.ibtool.document.notices */
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/English.lproj/MyDocument.xib:100025: note: This view is clipping its content.
This view is clipping its content.
ProcessPCH /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch.gch Sage_Prefix.pch normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c-header -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/Sage_Prefix.pch -o /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch.gch

CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/MyDocument.o MyDocument.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/MyDocument.o

/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m: In function '-[MyDocument connectURL:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:99: warning: no '-loadRequest:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:99: warning: (Messages without a matching method signature
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:99: warning: will be assumed to return 'id' and accept
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:99: warning: '...' as arguments.)
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m: In function '-[MyDocument webView:createWebViewWithRequest:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:110: warning: no '-loadRequest:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m: In function '-[MyDocument browseURL:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:127: warning: no '-loadRequest:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m: In function '-[MyDocument webView:didStartProvisionalLoadForFrame:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:133: warning: no '-provisionalDataSource' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m: In function '-[MyDocument openPanelDidEnd:returnCode:contextInfo:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/MyDocument.m:156: warning: no '-chooseFilename:' method found
CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/main.o main.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/main.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/main.o

CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/PreferencePanelController.o PreferencePanelController.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/PreferencePanelController.o

/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m: In function '-[PreferencePanelController apply:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m:41: warning: no '-setupPaths' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m:41: warning: (Messages without a matching method signature
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m:41: warning: will be assumed to return 'id' and accept
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/PreferencePanelController.m:41: warning: '...' as arguments.)
CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/AppDelegate.o AppDelegate.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/AppDelegate.o

/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m: In function '-[AppDelegate application:openFile:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:86: warning: no '-webView' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:86: warning: (Messages without a matching method signature
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:86: warning: will be assumed to return 'id' and accept
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:86: warning: '...' as arguments.)
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:86: warning: no '-mainFrame' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:90: warning: no '-loadRequest:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m: In function '-[AppDelegate getUrl:withReplyEvent:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:125: warning: no '-webView' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:125: warning: no '-mainFrame' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppDelegate.m:126: warning: no '-loadRequest:' method found
CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/AppController.o AppController.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/AppController.o

/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m: In function '-[AppController sageBrowse:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:261: warning: no '-webView' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:261: warning: (Messages without a matching method signature
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:261: warning: will be assumed to return 'id' and accept
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:261: warning: '...' as arguments.)
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:261: warning: no '-mainFrame' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:262: warning: no '-loadRequest:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m: In function '-[AppController terminalSessionPromptForInput:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:321: warning: no '-runCommand:withPrompt:withArguments:editingCommand:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m: In function '-[AppController sageTerminalRun:withArguments:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/AppController.m:384: warning: no '-runCommand:withPrompt:withArguments:editingCommand:' method found
CompileC build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/InputPanelController.o InputPanelController.m normal x86_64 objective-c com.apple.compilers.gcc.4_2
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv LANG en_US.US-ASCII
    /Developer/usr/bin/gcc-4.2 -x objective-c -arch x86_64 -fmessage-length=0 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -O0 -Wreturn-type -Wunused-variable -isysroot /Developer/SDKs/MacOSX10.5.sdk -mfix-and-continue -mmacosx-version-min=10.5 -gdwarf-2 -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-generated-files.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-own-target-headers.hmap -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-all-target-headers.hmap -iquote /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Sage-project-headers.hmap -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/include -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources/x86_64 -I/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/DerivedSources -include /var/folders/2J/2JGMKXefHFWmTZ1Ln92Z4U+++TI/-Caches-/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-cgjcfjqijsdnkvcdpwtgjctwsaxz/Sage_Prefix.pch -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/InputPanelController.o

/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m: In function '-[InputPanelController accept:]':
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m:33: warning: no '-terminalRun:' method found
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m:33: warning: (Messages without a matching method signature
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m:33: warning: will be assumed to return 'id' and accept
/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/InputPanelController.m:33: warning: '...' as arguments.)
Ld build/Debug/Sage.app/Contents/MacOS/Sage normal x86_64
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    setenv MACOSX_DEPLOYMENT_TARGET 10.5
    /Developer/usr/bin/gcc-4.2 -arch x86_64 -isysroot /Developer/SDKs/MacOSX10.5.sdk -L/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -F/Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug -filelist /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Objects-normal/x86_64/Sage.LinkFileList -mmacosx-version-min=10.5 -framework Cocoa -framework WebKit -framework Carbon -o /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/MacOS/Sage

PhaseScriptExecution "Run Script" build/Sage.build/Debug/Sage.build/Script-1967A8B911D6696A00ABC39D.sh
    cd /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app
    /bin/sh -c /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Sage.build/Debug/Sage.build/Script-1967A8B911D6696A00ABC39D.sh

** BUILD FAILED **


The following build commands failed:
Sage:
	ProcessInfoPlistFile /Users/grout/sage-4.5.2/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Info.plist Sage-Info.plist
	CpResource build/Debug/Sage.app/Contents/Resources/appl.icns appl.icns
	CpResource build/Debug/Sage.app/Contents/Resources/Defaults.plist Defaults.plist
	CpResource build/Debug/Sage.app/Contents/Resources/sage-document-py.icns sage-document-py.icns
	CpResource build/Debug/Sage.app/Contents/Resources/sage-document-spkg.icns sage-document-spkg.icns
	CpResource build/Debug/Sage.app/Contents/Resources/sage-document-sage.icns sage-document-sage.icns
	CpResource build/Debug/Sage.app/Contents/Resources/sage-document-sws.icns sage-document-sws.icns
	CpResource build/Debug/Sage.app/Contents/Resources/sage-small-blue.png sage-small-blue.png
	CpResource build/Debug/Sage.app/Contents/Resources/sage-small-grey.png sage-small-grey.png
	CpResource build/Debug/Sage.app/Contents/Resources/sage-small-green.png sage-small-green.png
	CpResource build/Debug/Sage.app/Contents/Resources/sage-small-red.png sage-small-red.png
(11 failures)

Failed to build Sage.app.
If you don't wish to build Sage.app set SAGE_APP_BUNDLE=no
```



---

Comment by jason created at 2010-09-08 16:04:03

I should say that I'm running OSX 10.6.4 and XCode 3.2.2


---

Comment by jason created at 2010-09-08 16:08:42

In downloading and looking at the posted patch, I see things like:


```
diff -r 406cb5e053a5 -r 9af17582a1cb sage/ext/mac-app/Sage-Info.plist
Binary file sage/ext/mac-app/Sage-Info.plist has changed
```


Apparently mercurial doesn't include the binary files when exporting a patch?


---

Comment by jason created at 2010-09-08 16:12:24

If all the changes are in the mac-app directory, it may be easiest just to make a tarball of the directory and post it.  To include binary changes, you can also use hg bundle (I don't know how) or use the --text option to hg export.


---

Comment by iandrus created at 2010-09-08 16:17:15

Replying to [comment:18 jason]:
> If all the changes are in the mac-app directory, it may be easiest just to make a tarball of the directory and post it.  To include binary changes, you can also use hg bundle (I don't know how) or use the --text option to hg export.

I created new diffs with --git which I think works.  It's good to know about the --text option too.  The scripts diff simply fixes the typo.


---

Comment by jason created at 2010-09-08 16:52:31

Okay, it seemed to build successfully.  I posted up the log at http://sage.pastebin.com/NNDhyjdc -- it seemed like there were lots of warnings.  Do we have to have the warnings?  It'd be more comfortable if the warnings weren't there.


---

Comment by jason created at 2010-09-08 16:53:23

The readme packaged in the dmg should definitely get changed, or even better, just removed.


---

Comment by jason created at 2010-09-08 17:02:49

What is the "crap" menu item under the Development|Packaging menu?


---

Comment by jason created at 2010-09-08 17:10:47

After playing with it a bit, I think it's great.  It also seems to have too many options---it is confusing.  Personally, I would be happy if:

1. It defaulted to the system browser

2. It defaulted to only showing the MenuExtras item, which I think has the right simplicity.


---

Comment by kcrisman created at 2010-09-08 17:18:19

Replying to [comment:23 jason]:
> After playing with it a bit, I think it's great.  It also seems to have too many options---it is confusing.  Personally, I would be happy if:
> 
> 1. It defaulted to the system browser
+1
> 2. It defaulted to only showing the MenuExtras item, which I think has the right simplicity.
But the problem with that is that many people are probably not familiar with how these work, especially those new to computing in general.  Having a regular application is better.

The crap menu item is a legitimate sage script - see `sage-crap`, which apparently tests for random binary stuff or other things in a given folder.  But like many other things, it could be in an "advanced" menu.

I'm not ready to test yet - still have a lot of stuff to do - but tonight I should be able to do something rigorous, also hopefully try PPC tonight or tomorrow to see if it performs as advertised.  I won't be able to test bdisting on PPC in the immediate future, though; maybe Georg can?  I'll cc: him.


---

Comment by jason created at 2010-09-08 17:32:08

Replying to [comment:24 kcrisman]:
> Replying to [comment:23 jason]:
> > After playing with it a bit, I think it's great.  It also seems to have too many options---it is confusing.  Personally, I would be happy if:
> > 
> > 1. It defaulted to the system browser
> +1
> > 2. It defaulted to only showing the MenuExtras item, which I think has the right simplicity.
> But the problem with that is that many people are probably not familiar with how these work, especially those new to computing in general.  Having a regular application is better.

I view these two as going hand-in-hand.  It is pretty confusing to have the full Sage app menu (like an "Edit" menu) and then have everything work through the browser.  If we're using the system browser (which I think we should do by default), the user should have a super-simple interface.  The Edit menu, the Format menu, and most of the File menu are completely unnecessary and confusing.




> 
> The crap menu item is a legitimate sage script - see `sage-crap`, which apparently tests for random binary stuff or other things in a given folder.  But like many other things, it could be in an "advanced" menu.

I would definitely rename it in the menu then.  It looks very unprofessional.  Maybe "binary-test" or even just delete it.


---

Comment by kcrisman created at 2010-09-08 17:38:12

Replying to [comment:25 jason]:
> Replying to [comment:24 kcrisman]:
> > Replying to [comment:23 jason]:
> > > After playing with it a bit, I think it's great.  It also seems to have too many options---it is confusing.  Personally, I would be happy if:
> > > 
> > > 1. It defaulted to the system browser
> > +1
> > > 2. It defaulted to only showing the MenuExtras item, which I think has the right simplicity.
> > But the problem with that is that many people are probably not familiar with how these work, especially those new to computing in general.  Having a regular application is better.
> 
> I view these two as going hand-in-hand.  It is pretty confusing to have the full Sage app menu (like an "Edit" menu) and then have everything work through the browser.  If we're using the system browser (which I think we should do by default), the user should have a super-simple interface.  The Edit menu, the Format menu, and most of the File menu are completely unnecessary and confusing.

I can't comment more on this; I feel like that would be more for a future ticket, but maybe Ivan has some comments.  It's good to have more than two people trying this out, that's for sure!

> > 
> > The crap menu item is a legitimate sage script - see `sage-crap`, which apparently tests for random binary stuff or other things in a given folder.  But like many other things, it could be in an "advanced" menu.
> 
> I would definitely rename it in the menu then.  It looks very unprofessional.  Maybe "binary-test" or even just delete it.

Presumably most users wouldn't need it.  Perhaps you should raise renaming this script on sage-devel as well; I agree it looks somewhat unprofessional, but it probably dates back to when William was the only person using Sage and that wasn't an issue.


---

Comment by jason created at 2010-09-08 17:57:04

If using the application through the system web browser, I think there ought to be only the following menus:

  * File
    * New Worksheet
    * Upload Worksheet
    * Open Notebook
  * Server
    * Start Server
    * Stop Server
    * View Log
  * Terminal Session
    * Sage
    * Math submenu (leave as it is)
    * Misc (leave as it is)
  * Development
    * Reveal SAGE_ROOT in Finder
    * Reveal SAGE_ROOT in Terminal
    * Build Sage Library
    * Testing
      * Test...
      * Test All
      * Coverage
    * Debugging
      * Preparse...
      * gdb
    * Packaging
      * Binary Distribution  (this should make a .app by default)
      * Source Distribution
      * Sage Package...
  * Help
    * Sage Help through Developer Guide (the top section of the menu as it is now)
    * divider
    * Ask a question (link to ask.sagemath.org)
    * divider
    * Sagemath through IRC (the last section of the menu as it is now

That's it.  By default, I think we ought to start off supporting only the subset of things we think will be really useful to people.

If the preference is to have Sage.app manage its own web browser, then the Edit and Window menus should be available.  However, even just now, I was having problems with the Sage.app browser.  It just gave an error, and the log said something about a bad token (possibly the startup hash token for a local user?)


---

Comment by iandrus created at 2010-09-08 19:50:20

Deleting menus is easy, but I don't know how to make them depend on an option (it is possible though).  We probably should get rid of much of the File, Edit and Format menus.  I meant to go over them at some point, but never did.  Also, renaming things in the menu is currently not easy since it just tacks a `sage --` onto the beginning (or the first character if it's upper case).  There is a special case for "Sage", but I would like to keep those to a minimum.

How will I know if the consensus is to strip the menus to Jason's suggestion (which I think is sensible), defaulting to system browser, and building the app by default?


---

Comment by jason created at 2010-09-08 19:55:06

Replying to [comment:28 iandrus]:


> How will I know if the consensus is to strip the menus to Jason's suggestion (which I think is sensible), defaulting to system browser, and building the app by default?

Well, we've already posted to sage-devel, and the only replies seem to be kcrisman and me.  So I guess the three of us form a consensus.  Then when people start using it, I'm sure we'll hear more opinions.


---

Comment by kcrisman created at 2010-09-08 19:58:35

> > How will I know if the consensus is to strip the menus to Jason's suggestion (which I think is sensible), defaulting to system browser, and building the app by default?
> 
> Well, we've already posted to sage-devel, and the only replies seem to be kcrisman and me.  So I guess the three of us form a consensus.  Then when people start using it, I'm sure we'll hear more opinions.

Correct.  After all, none of these things are removing functionality that existed before; it's still a vast improvement.  You might want to make some notes in the source as to how to (re)enable some of the more heavy functionality.


---

Comment by jason created at 2010-09-08 20:04:06

How about this: in the officially distributed version right now, we just use the system browser and distribute the minimal menu?  That seems like it would make things much simpler on both the users and developers.  I'd also delete the "loading" page in this case.  Is it easy to just make the doc icon bounce up and down while the server is starting, or display a progress bar?

Then we can work on ironing out things with the Sage.app browser.  For example, after switching back to the sage.app browser, it's no longer opening up the notebook interface automatically upon startup.  When I click the link in the "loading" page, it doesn't log me in automatically.  If I stop the server, then start it again, it then opens up the notebook page automatically.


---

Comment by jason created at 2010-09-08 20:08:34

One more problem I found.  If you delete (or move) your .sage directory, then there is a problem starting up the server since it requests an admin password.  Here is the log:


```
Starting Notebook
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the Sage Notebook server starts...
Setting permissions of DOT_SAGE directory so only you can read and write it.
/tmp/sage-mac-app/local/lib/python/getpass.py:79: GetPassWarning: Can not control echo on the terminal.
  passwd = fallback_getpass(prompt, stream)
Warning: Password input may be echoed.
Enter new password: ...
The notebook files are stored in: sage_notebook.sagenb



Please choose a new password for the Sage Notebook 'admin' user.
Do _not_ choose a stupid password, since anybody who could guess your password
and connect to your machine could access or delete your files.
NOTE: Only the md5 hash of the password you type is stored by Sage.
You can change your password by typing notebook(reset=True).



Traceback (most recent call last):
  File "/tmp/sage-mac-app/local/bin/sage-notebook", line 36, in <module>
    notebook(port=8000)
  File "/Users/grout/projects/sagenb-0.8.2/src/sagenb/sagenb/notebook/notebook_object.py", line 217, in __call__
    return self.notebook(*args, **kwds)
  File "/Users/grout/projects/sagenb-0.8.2/src/sagenb/sagenb/notebook/run_notebook.py", line 194, in notebook_twisted
    passwd = get_admin_passwd()                
  File "/Users/grout/projects/sagenb-0.8.2/src/sagenb/sagenb/notebook/run_notebook.py", line 424, in get_admin_passwd
    passwd = getpass.getpass("Enter new password: ")
  File "/tmp/sage-mac-app/local/lib/python/getpass.py", line 79, in unix_getpass
    passwd = fallback_getpass(prompt, stream)
  File "/tmp/sage-mac-app/local/lib/python/getpass.py", line 114, in fallback_getpass
    return _raw_input(prompt, stream)
  File "/tmp/sage-mac-app/local/lib/python/getpass.py", line 130, in _raw_input
    raise EOFError
EOFError
```


The same sort of thing happens if the notebook tries to upgrade an old notebook (pre-2009 or so).  The user is prompted to enter Y/N to whether they want to upgrade.

The first problem is definitely a problem, since every new user will have it happen to them.


---

Comment by iandrus created at 2010-09-08 20:38:33

Replying to [comment:33 jason]:
> One more problem I found.  If you delete (or move) your .sage directory, then there is a problem starting up the server since it requests an admin password.  

Is there a way to know ahead of time (some file we can check) if this is going to happen, and then send them to an interactive shell or ask for a password or something?

> The same sort of thing happens if the notebook tries to upgrade an old notebook (pre-2009 or so).  The user is prompted to enter Y/N to whether they want to upgrade.

> The first problem is definitely a problem, since every new user will have it happen to them.

How often do you think the second will be a problem?


---

Comment by jason created at 2010-09-08 21:16:37

Replying to [comment:34 iandrus]:
> Replying to [comment:33 jason]:
> > One more problem I found.  If you delete (or move) your .sage directory, then there is a problem starting up the server since it requests an admin password.  
> 
> Is there a way to know ahead of time (some file we can check) if this is going to happen, and then send them to an interactive shell or ask for a password or something?

We could check for existence of the .sage/sage_notebook.sagenb directory, which is where the sage notebook is stored by default.  If it's not there, then the notebook will be created and the password will be solicited.

> 
> > The same sort of thing happens if the notebook tries to upgrade an old notebook (pre-2009 or so).  The user is prompted to enter Y/N to whether they want to upgrade.
> 
> > The first problem is definitely a problem, since every new user will have it happen to them.
> 
> How often do you think the second will be a problem?

Not very often any more, though it bit my postdoc mentor over the weekend.  My guess is that there will be a lot of people right off that never upgraded an old Sage version that will download the app and run into it.  But after that initial rush, I don't see this happening at all.

Maybe there ought to be a separate notebook_intialized() command that checks to see if the notebook is initialized.


---

Comment by jason created at 2010-09-08 21:19:24

I've posted to sage-notebook about this.


---

Comment by jhpalmieri created at 2010-09-08 21:23:49

First, the app looks great.  I think that if you build the app by default, people will be a little surprised.  I would suggest not building it by default but strongly encourage people to try it out (on sage-devel, for example), with the goal of distributing it by default with Sage 5.0.

As far as the menu items go, I have to disagree with kcrisman's comment

> After all, none of these things are removing functionality that existed before

How do I get the output from "sage --help" or "sage --advanced"?  If you remove menu items (like "crap"), then how do I execute "sage -crap"?  Could we have a menu item (like the current "Calculate" one) which just lets you type in any command line options you want?  Or it could be fancier and have a menu to choose a command-line option from the ones not already included.  Then you can eliminate "crap" but people can still use it if they want to.

If I select "Also Show Menu Extra", I don't see any difference.  (It's also not completely clear what it's supposed to do; could it say `Also show "Extra" menu` instead?)

I unfortunately have my terminal program set to close the window when the shell exits, so using the "Calculate" option is not ideal: it closes the window as soon as it is done executing, so I can't see it.  My only options seem to be to change this for all of my Terminal windows, or to not exit after running Sage.  Is that right?


---

Comment by jason created at 2010-09-08 21:46:48

Replying to [comment:37 jhpalmieri]:
> First, the app looks great.  I think that if you build the app by default, people will be a little surprised.  I would suggest not building it by default but strongly encourage people to try it out (on sage-devel, for example), with the goal of distributing it by default with Sage 5.0.

That sounds good.  Again, I see most people downloading a pre-built app.

> 
> As far as the menu items go, I have to disagree with kcrisman's comment
> 
> > After all, none of these things are removing functionality that existed before
> 
> How do I get the output from "sage --help" or "sage --advanced"?  If you remove menu items (like "crap"), then how do I execute "sage -crap"?  Could we have a menu item (like the current "Calculate" one) which just lets you type in any command line options you want?  Or it could be fancier and have a menu to choose a command-line option from the ones not already included.  Then you can eliminate "crap" but people can still use it if they want to.

+1 to having "Sage (advanced)" pop up a dialog box asking for command-line switches.


> 
> If I select "Also Show Menu Extra", I don't see any difference.  (It's also not completely clear what it's supposed to do; could it say `Also show "Extra" menu` instead?)

I guess because people don't know what a MenuExtra is.  Maybe changing the option to "Menu Bar Control" would be clearer?


> 
> I unfortunately have my terminal program set to close the window when the shell exits, so using the "Calculate" option is not ideal: it closes the window as soon as it is done executing, so I can't see it.  My only options seem to be to change this for all of my Terminal windows, or to not exit after running Sage.  Is that right? 


I think we ought to delete the Calculate option.  I don't see a valuable purpose for it.


---

Comment by jason created at 2010-09-09 00:45:05

Replying to [comment:35 jason]:
> Replying to [comment:34 iandrus]:
> > Replying to [comment:33 jason]:
> > > One more problem I found.  If you delete (or move) your .sage directory, then there is a problem starting up the server since it requests an admin password.  
> > 
> > Is there a way to know ahead of time (some file we can check) if this is going to happen, and then send them to an interactive shell or ask for a password or something?
> 
> We could check for existence of the .sage/sage_notebook.sagenb directory, which is where the sage notebook is stored by default.  If it's not there, then the notebook will be created and the password will be solicited.


Actually, this check would take care of the upgrade issue as well.  In the upgrade case, it sees that .sage/sage_notebook.sagenb is not available, so it tries to upgrade the old sage notebook.

So: check to see if ~/.sage/sage_notebook.sagenb directory exists.  If it doesn't, start a terminal session with the notebook (or have some way for the user to interact with Sage).  If it does exist, assume that there will be no interaction and just start up normally.


---

Comment by kcrisman created at 2010-09-09 01:39:45

Replying to [comment:37 jhpalmieri]:
> First, the app looks great.  I think that if you build the app by default, people will be a little surprised.  I would suggest not building it by default but strongly encourage people to try it out (on sage-devel, for example), with the goal of distributing it by default with Sage 5.0.

This seems like a good progression.

> As far as the menu items go, I have to disagree with kcrisman's comment
> 
> > After all, none of these things are removing functionality that existed before
> 
> How do I get the output from "sage --help" or "sage --advanced"?  If you remove menu items (like "crap"), then how do I execute "sage -crap"?  Could we have a menu item (like the current "Calculate" one) which just lets you type in any command line options you want?  Or it could be fancier and have a menu to choose a command-line option from the ones not already included.  Then you can eliminate "crap" but people can still use it if they want to.

I think I was saying that all these things are in the Terminal option still; you can run the terminal.   As it was I think I actually was for additional menu options before I was against them ;) but really I think that for the menu, it's not as crucial, since we didn't have that before.  I also think there was a way in Preferences to execute any old command you wanted, or?  Maybe not - that should be a high priority.  

(The Calculate was also based on a request of mine, but if we're shrinking the # of options, then that should go away too for now.)

> If I select "Also Show Menu Extra", I don't see any difference.  (It's also not completely clear what it's supposed to do; could it say `Also show "Extra" menu` instead?)

I think you have to restart for ALL the things in Preferences to work, not just the ones it says; at least, that's the only way I could get them to work.  I agree with Jason's comment about the Menu Extra, as I mentioned above.  However, now that I've tried it a bit, it seems that it functions in such a way that you can have Sage not running, but then almost immediately turn it on with just a mouse flick along the top, even with the various options - is that right?  

Related to that is that I did finally get the other binary to work, by dragging and selecting; the key is that you have to actually get the ./sage file, and that's probably not obvious to those who might think the folder is the 'binary', since ./sage isn't actually a compiled binary file... anyway.  I don't know whether this comment is important.  This also seems to require a restart.

> I unfortunately have my terminal program set to close the window when the shell exits, so using the "Calculate" option is not ideal: it closes the window as soon as it is done executing, so I can't see it.  My only options seem to be to change this for all of my Terminal windows, or to not exit after running Sage.  Is that right? 

You can set this in Preferences; in fact, Ivan's first default behavior was not to exit.

Related to this, hooray - there is only ONE window opening now!  Thanks for fixing that.  You were right that I had to delete the TerminalEmulatorList - weirdly, since I never created any new ones.

Random: when you click on an sws file it starts the browser, but doesn't *do* anything to suggest that it can't actually open them.  That seems problematic, and I don't remember that behavior in earlier versions.

I also finally looked at some of the code (some of which I even understood), and I'm really impressed that you found all those hacks and basically learned Objective-C for this project.  Really great work, even with all the minor things we are talking about.

I'm going to test this on PPC in the next few minutes.  But after that I'll probably bow out, because actual discussion is happening, and that should soon lead to a positively reviewed final version :)


---

Comment by kcrisman created at 2010-09-09 01:49:03

Bad news on PPC.. "You cannot use ... with this version of Mac OS X".

BUT I think that this might be because of some use of the wrong `MAC_OS_X_DEPLOYMENT_TARGET` or something, because I am using Tiger (10.4), not necessarily because of PPC (hence it's still possible that it would work on Leopard PPC, which someone should test).  

Next step; try to get the extcode thing in and see whether a bdist on this machine works.


---

Comment by jason created at 2010-09-09 02:14:56

Replying to [comment:40 kcrisman]:


> I also finally looked at some of the code (some of which I even understood), and I'm really impressed that you found all those hacks and basically learned Objective-C for this project.  Really great work, even with all the minor things we are talking about.


+1. Ivan, you are doing a tremendous job here that lots of people have wanted for a long time.  Thanks!


---

Comment by jhpalmieri created at 2010-09-09 02:33:56

I see what the "Menu Extra" option does, and it looks nice.  I think it should be on by default.  Can we figure out what to call it so that people will understand the option in the Preferences dialogue?

> I think I was saying that all these things are in the Terminal option still; you can run the terminal.

Maybe I don't understand you. When I run the "Terminal Session" option, it runs Sage in a terminal window, as I would expect.  Executing "sage -crap" doesn't actually run sage: it runs some script in SAGE_ROOT/local/bin and then quits.  It's not something you run within sage.  Same with other advanced options like "bdist" or "coverage".

> You can set this [whether the Terminal exits] in Preferences.

I see that I can set Sage so that the terminal doesn't exit after running Sage, or I can set Terminal so it doesn't close windows when the shell exits, but in the first case I have a terminal window running the shell, and in the second I have to manually close all of my terminal windows.  Is there some way to call Terminal and override the global preference to "close the window" or "close if the shell exited cleanly" for that particular Terminal session? 

By the way, if I delete the "exit" part of the terminal script in Sage, it would be nice if there were a button to hit to restore the default script.  Plenty of people using this won't necessarily know the appropriate shell syntax.

It would also be nice (but it's way beyond the scope of this particular ticket) to have a "calculate" option which just displays the result (if there is anything to display) in a window which you can close when you're done, or from which you can copy, etc.  If we could run a Sage server in the background so that the "calculate" option could just send queries to it, that would be nice.  I think I've heard of a possibility like this, but I can't remember where...


---

Comment by kcrisman created at 2010-09-09 02:36:15

> It would also be nice (but it's way beyond the scope of this particular ticket) to have a "calculate" option which just displays the result (if there is anything to display) in a window which you can close when you're done, or from which you can copy, etc.  If we could run a Sage server in the background so that the "calculate" option could just send queries to it, that would be nice.  I think I've heard of a possibility like this, but I can't remember where...

Funny - this is something I requested earlier, Ivan put in, but then we nixed.  `./sage -c`, that is.  Unfortunately it doesn't quite calculate, see a recent sage-support/ask.sagemath.org thread.  Something like you are talking about (with server running) sounds like a great idea as well.


---

Comment by kcrisman created at 2010-09-09 02:36:32

Bad news on OS X 10.4 front...

```

Crismans-Computer:~/Desktop/sage-4.5.3 crisman$ ./sage -bdist Test
Sage works!
Copying files over to tmp directory
cp: *.sage: No such file or directory
Copying Sage library over
Making empty spkg's
There will be an error about x below that you can safely ignore.
mv: rename x to x/x: Invalid argument
Building the Mac Application
(NOTE: project Sage was written by a newer version of Xcode (45) -- temporarily downgrading it to version 42 (without modifying project file))

### BUILDING NATIVE TARGET Sage WITH CONFIGURATION Debug

Checking Dependencies...
SDK package /Users/crisman/Desktop/sage-4.5.3/data/extcode/sage/ext/mac-app/macosx10.5 does not exist
** BUILD FAILED **
Failed to build Sage.app.
If you don't wish to build Sage.app set SAGE_APP_BUNDLE=no
```

So we will have to deal with this somehow, or deal with not having it available for Tiger (a mistake, in my opinion, since the people most likely to use this are least likely to have $ to upgrade).  A quick and uninformed internet search for help on this issue didn't do much for me, but then again I don't have a lot of expertise with Xcode.


---

Comment by jhpalmieri created at 2010-09-09 02:42:28

By the way, I think the "xtermApplescript" and "iTermApplescript" options are reversed.  In what is currently labeled "iTermApplescript", the text "to exit active" should read "to stay active".

Regarding "Use Alternate Sage Binary:", maybe it should say "Use alternate Sage executable"?  I personally also think that too many words are capitalized in the preferences.  They should say:

 - Start server on launch
 - Show in Dock (requires restart)
   - Use system browser   [or "Use default browser"?]
   - Also show menu extra   [rephrased somehow]
 - Use alternate Sage executable:

 - Always prompt for arguments (hold ...)
 - Edit full commands (not just arguments)


Regarding the 10.4 issue: it shouldn't be too hard to test whether running 10.4, and then refuse to make the binary.  I think that we could release it soon just for 10.5 and 10.6, and Sage 5.0 could be the target for getting it to work on 10.4.  Does anyone know whether this is possible (working on 10.4) or likely?

Can you build a binary on 10.5 or 10.6 which works on 10.4 by setting appropriate flags?


---

Comment by kcrisman created at 2010-09-09 03:10:21

> Regarding the 10.4 issue: it shouldn't be too hard to test whether running 10.4, and then refuse to make the binary.  I think that we could release it soon just for 10.5 and 10.6, and Sage 5.0 could be the target for getting it to work on 10.4.  Does anyone know whether this is possible (working on 10.4) or likely?
> 
> Can you build a binary on 10.5 or 10.6 which works on 10.4 by setting appropriate flags?
 
In general, yes, with that nasty [deployment](http://developer.apple.com/library/mac/#documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html) target thing you tracked down (?) which caused the Snow Leopard problems.  It could be as simple as setting that.

On the other hand, since this uses Xcode in a much tighter way than other spkgs, perhaps not; the error is also a little mystifying, because I don't know what Xcode 45 is supposed to be.  

Okay, I finally found ONE thing that might help.  In Xcode, go to Info once you've (Ivan?) opened the project, and click on "General"..   Make the "Project Format" Xcode 2.4 compatible" and make the Base SDK for all configurations Mac OS X 10.4 (the first one for sure, I suspect, the second one I'm less sure on but I figure you might as well take a whirl).  There isn't anything really cool you used from Xcode 3.x, is there?  Presumably not, if this is a fairly basic Cocoa application.

I hope this works!


---

Comment by iandrus created at 2010-09-09 07:56:13

Regarding 10.4, NSPathControl (which is how you to pick the sage executable) is 10.5+ only.  I can replace it with a text field to type the path in which case drag and drop still works to some extent.  If I get a chance, I will do that soon.

As for problems with the Applescript options being out of order, I think that's due to a bug in Apple's API which I think I have now worked around to some extent.  If you select using the keyboard instead of the mouse it should work correctly.

I have also added an alert when opening sws files, fixed the warnings, and added a way to reset the Applescript used.

I haven't redone the menus because I'm not sure if jhpalmieri was disagreeing with the idea of a minimal set.  I did add a Sage (advanced) which will prompt for any args you wish to give it.


---

Comment by kcrisman created at 2010-09-09 17:31:55

Once you get the 10.4 compatibility, give me a holler and I'll try it out again on PPC.  Are you also still updating your sage.math account with the new versions?  That would make it (slightly) easier for me to check this; otherwise I have to do an annoying flash drive switch.


---

Comment by jhpalmieri created at 2010-09-09 21:23:46

Replying to [comment:48 iandrus]:

> I haven't redone the menus because I'm not sure if jhpalmieri was disagreeing with the idea of a minimal set.  I did add a Sage (advanced) which will prompt for any args you wish to give it.

I would be very happy with a smaller set of menu options.


---

Comment by iandrus created at 2010-09-10 12:36:20

I have 10.4 support (I think), as well as paring down the menus.  I also rearranged the Preferences window.  

Looking back over the comments, I believe that I addressed all concerns raised so far except the following (which I do not have plans to fix for this ticket--unless you change my mind):
 * some problems jason had with the browser (can you reproduce those) 
 * Making bdist build application by default 
 * the "loading" page still appears when using the system browser (I think this is best--perhaps there should be an option)
 * override emulator choice per command 
   * jhpalmieri, did you want a version that would exit only on success -- you could use "%`@` && exit"
   * Perhaps we should provide an exit and a not exit version (and exit on success)
 * calculate dialog


---

Attachment


---

Comment by kcrisman created at 2010-09-10 14:46:30

Replying to [comment:51 iandrus]:
> I have 10.4 support (I think), as well as paring down the menus.  I also rearranged the Preferences window.  

Great, I'll try this out on PPC 10.4 as soon as I get a chance (should be within 2-3 hours).

>  * the "loading" page still appears when using the system browser (I think this is best--perhaps there should be an option)
This seems reasonable to leave in place for now.  All your other stuff would be better to improve on in another ticket, esp. if it isn't default build behavior yet, you are right.


---

Comment by kcrisman created at 2010-09-10 17:54:34

Replying to [comment:52 kcrisman]:
> Replying to [comment:51 iandrus]:
> > I have 10.4 support (I think), as well as paring down the menus.  I also rearranged the Preferences window.  
> 
> Great, I'll try this out on PPC 10.4 as soon as I get a chance (should be within 2-3 hours).

I'm still getting the same error message about not being able to use the application with this version of Mac OS X.  Probably removing 10.5 specific things isn't enough, but one would have to do all the preference stuff for 10.4 I mentioned above in the project file.  Or did you do those things too?  In which case I'm stumped.  Except...

One thing on the internet suggested "The only snag I've hit is that the new IB defaults to a format that's not compatible with the old IB, so it's easy to create a NIB that can't be edited with the 2.4 version of tools." If that's relevant?  Also, "You can specifiy a "2.4 compatible" project in XCode 3.x, but the accompanying Interface Builder part is not set to that level: therefore, all your developed applescripts don't run any longer on 10.4 (be it intel or ppc)".  And "However, it is not possible to create new objects on existing 1.2 version NIB objects as new Interface Builder objects are set to a higher incompatible version."  This seems problematic.  One person said that xib objects seemed to work fine, but that's all you have, as far as I can tell...


---

Comment by iandrus created at 2010-09-10 19:02:32

Replying to [comment:53 kcrisman]:

> Replying to [comment:52 kcrisman]:
> > Replying to [comment:51 iandrus]:
> > > I have 10.4 support (I think), as well as paring down the menus.  I also rearranged the Preferences window.
> > Great, I'll try this out on PPC 10.4 as soon as I get a chance (should be within 2-3 hours).
> I'm still getting the same error message about not being able to use the application with this version of Mac OS X.  Probably removing 10.5 specific things isn't enough, but one would have to do all the preference stuff for 10.4 I mentioned above in the project file.  Or did you do those things too?  In which case I'm stumped.  Except...

I changed the base SDK to 10.4 and made the project Xcode 2.4 compatible.  In interface builder it warns me that image scaling on a few elements isn't supported before 10.5, but I don't think that should cause this problem--it's a warning not an error.  Did you build this yourself, or use the prebuilt version?

> One thing on the internet suggested "The only snag I've hit is that the new IB defaults to a format that's not compatible with the old IB, so it's easy to create a NIB that can't be edited with the 2.4 version of tools." If that's relevant?  Also, "You can specifiy a "2.4 compatible" project in XCode 3.x, but the accompanying Interface Builder part is not set to that level: therefore, all your developed applescripts don't run any longer on 10.4 (be it intel or ppc)".  And "However, it is not possible to create new objects on existing 1.2 version NIB objects as new Interface Builder objects are set to a higher incompatible version."  This seems problematic.  One person said that xib objects seemed to work fine, but that's all you have, as far as I can tell...

Can you open the xib files?  If you double click them what happens?  The xibs have a deployment target of 10.4 and a development target of 3.0 which is the oldest I can choose.  Perhaps I have to recreate them for an older version?

Actually I think it may be [due to the compiler I'm using](http://lists.apple.com/archives/cocoa-dev/2009/Aug/msg01631.html).  Can you try setting the compiler to 4.0 and building again?  Go to Project > Edit Project Settings (near the bottom) > Build tab > Compiler Version (5th section)  and then choose 4.0 (that's the oldest I have).  Then try building.


---

Comment by jhpalmieri created at 2010-09-10 20:07:28

> jhpalmieri, did you want a version that would exit only on success -- you could use "%`@` && exit"

For me the only issue is when using the "Calculate" menu option, and I don't even know if that's still there.  When using this option, if the Terminal automatically closes windows when their process is done, you don't see any output from the command, which makes it pretty pointless.  So it would be nice to be able to keep the window open after running "sage -c ..." until manually closed.

With the new version, I can't run it successfully on my Intel iMac running 10.6: I see

```
Building the Mac Application
Build settings from command line:
    ARCHES = ppc ppc64 i386 x86_64


### BUILD NATIVE TARGET Sage OF PROJECT Sage WITH CONFIGURATION Debug
Check dependencies
error: There is no SDK with the name or path '/Developer/SDKs/MacOSX10.4u.sdk'
[BEROR]error: There is no SDK with the name or path '/Developer/SDKs/MacOSX10.4u.sdk'
** BUILD FAILED **

Failed to build Sage.app.
```



---

Comment by kcrisman created at 2010-09-10 20:12:44

Hmm, that's weird.  I'll have to check this out on my computer as well.  Obviously jhpalmieri won't have the 10.4 SDK, but that shouldn't mean he can't compile it... This is going to take some work, aargh.


---

Comment by kcrisman created at 2010-09-10 20:14:51

> I changed the base SDK to 10.4 and made the project Xcode 2.4 compatible.  In interface builder it warns me that image scaling on a few elements isn't supported before 10.5, but I don't think that should cause this problem--it's a warning not an error.  Did you build this yourself, or use the prebuilt version?

Right, a warning - that it might crash :)  I used the prebuilt version, though; doing it myself would have taken many moons on the work computer.  I'll try this in a bit at home, hopefully.

> Can you open the xib files?  If you double click them what happens?  The xibs have a deployment target of 10.4 and a development target of 3.0 which is the oldest I can choose.  Perhaps I have to recreate them for an older version?

I haven't tried this on an older computer yet.  Sadly, that may be the case.

> Actually I think it may be [due to the compiler I'm using](http://lists.apple.com/archives/cocoa-dev/2009/Aug/msg01631.html).  Can you try setting the compiler to 4.0 and building again?  Go to Project > Edit Project Settings (near the bottom) > Build tab > Compiler Version (5th section)  and then choose 4.0 (that's the oldest I have).  Then try building.

I can try this, though not immediately.  Thanks for looking into this so much.


---

Comment by kcrisman created at 2010-09-10 20:31:46

> > Can you open the xib files?  If you double click them what happens?  The xibs have a deployment target of 10.4 and a development target of 3.0 which is the oldest I can choose.  Perhaps I have to recreate them for an older version?

Well, they open on the older computer fine.  The build fails, though (using the Xcode GUI).

> > Actually I think it may be [due to the compiler I'm using](http://lists.apple.com/archives/cocoa-dev/2009/Aug/msg01631.html).  Can you try setting the compiler to 4.0 and building again?  Go to Project > Edit Project Settings (near the bottom) > Build tab > Compiler Version (5th section)  and then choose 4.0 (that's the oldest I have).  Then try building.

This isn't an option in my version of Xcode (on the 10.4 system).

I wonder why jhpalmieri wasn't able to compile this, though.  You'd think Mac would be smart enough to look for a *newer* SDK if that one wasn't available.  Hmm.


---

Comment by iandrus created at 2010-09-10 20:35:09

Replying to [comment:55 jhpalmieri]:
> > jhpalmieri, did you want a version that would exit only on success -- you could use "%`@` && exit"
> 
> For me the only issue is when using the "Calculate" menu option, and I don't even know if that's still there.  When using this option, if the Terminal automatically closes windows when their process is done, you don't see any output from the command, which makes it pretty pointless.  So it would be nice to be able to keep the window open after running "sage -c ..." until manually closed.

Cool, I won't worry about it then.

> With the new version, I can't run it successfully on my Intel iMac running 10.6: I see
> {{{
> error: There is no SDK with the name or path '/Developer/SDKs/MacOSX10.4u.sdk'
> [BEROR]error: There is no SDK with the name or path '/Developer/SDKs/MacOSX10.4u.sdk'
> }}}

Now that I think of it, I think I had to choose to install the 10.4 SDK.  Clearly, not everyone who wants to build it will have it though, so I'll have to figure out a way to use 10.4 if they have it, but 10.5 (or 10.6) if they don't.  In the mean time you can open up the Project Settings and change the Base SDK (at the bottom of the General tab) to build it that way.


---

Comment by iandrus created at 2010-09-10 20:43:30

Replying to [comment:58 kcrisman]:
> > > Can you open the xib files?  If you double click them what happens?  The xibs have a deployment target of 10.4 and a development target of 3.0 which is the oldest I can choose.  Perhaps I have to recreate them for an older version?
> 
> Well, they open on the older computer fine.  The build fails, though (using the Xcode GUI).

What error do you get?


---

Comment by kcrisman created at 2010-09-10 23:47:52

> > > > Can you open the xib files?  If you double click them what happens?  The xibs have a deployment target of 10.4 and a development target of 3.0 which is the oldest I can choose.  Perhaps I have to recreate them for an older version?
> > 
> > Well, they open on the older computer fine.  The build fails, though (using the Xcode GUI).
> 
> What error do you get?

Same thing (sadly) happens on the home computer.  Looks like all `.m` files compiled (they have a check in the build column), and nearly everything with a checkbox in the target column is checked.  Several Frameworks aren't, and of course `Sage.app` and `Sage-info.plist` aren't.  Here's the full report - the build stopped while going through `Sage_Prefix.pch`, whatever that is.

```

Building target “Sage” of project “Sage” with configuration “Release”


Checking Dependencies
Processing /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Info.plist Sage-Info.plist
    mkdir /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents
    cd /Users/crisman/Desktop/SageSrc
    com.apple.tools.info-plist-utility Sage-Info.plist -genpkginfo /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/PkgInfo -expandbuildsettings -o /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Info.plist

CpResource build/Release/Sage.app/Contents/Resources/English.lproj/Credits.html English.lproj/Credits.html
    mkdir /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources/English.lproj
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/English.lproj/Credits.html /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources/English.lproj

CpResource build/Release/Sage.app/Contents/Resources/English.lproj/InfoPlist.strings English.lproj/InfoPlist.strings
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/English.lproj/InfoPlist.strings /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources/English.lproj

CpResource build/Release/Sage.app/Contents/Resources/English.lproj/MyDocument.xib English.lproj/MyDocument.xib
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/English.lproj/MyDocument.xib /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources/English.lproj

CpResource build/Release/Sage.app/Contents/Resources/English.lproj/MainMenu.xib English.lproj/MainMenu.xib
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/English.lproj/MainMenu.xib /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources/English.lproj

CpResource build/Release/Sage.app/Contents/Resources/appl.icns appl.icns
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/appl.icns /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/Defaults.plist Defaults.plist
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/Defaults.plist /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-document-py.icns sage-document-py.icns
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-document-py.icns /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-document-sage.icns sage-document-sage.icns
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-document-sage.icns /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-document-spkg.icns sage-document-spkg.icns
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-document-spkg.icns /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-document-sws.icns sage-document-sws.icns
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-document-sws.icns /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-small-blue.png sage-small-blue.png
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-small-blue.png /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-small-green.png sage-small-green.png
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-small-green.png /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-small-grey.png sage-small-grey.png
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-small-grey.png /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/sage-small-red.png sage-small-red.png
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/sage-small-red.png /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/start-sage.sh start-sage.sh
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/start-sage.sh /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/open-location.sh open-location.sh
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/open-location.sh /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

CpResource build/Release/Sage.app/Contents/Resources/loading-page.html loading-page.html
    cd /Users/crisman/Desktop/SageSrc
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -strip-debug-symbols -resolve-src-symlinks /Users/crisman/Desktop/SageSrc/loading-page.html /Users/crisman/Desktop/SageSrc/build/Release/Sage.app/Contents/Resources

ProcessPCH /Library/Caches/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-eznqjueptjnfnofhfaeeuuyiiihc/Sage_Prefix.pch.gch Sage_Prefix.pch normal x86_64 objective-c com.apple.compilers.gcc.4_0
    cd /Users/crisman/Desktop/SageSrc
    /Developer/usr/bin/gcc-4.0 -x objective-c-header -arch x86_64 -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -Os -Wreturn-type -Wunused-variable -fmessage-length=0 -fvisibility=hidden -mmacosx-version-min=10.4 -gdwarf-2 -iquote /Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-generated-files.hmap -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-own-target-headers.hmap -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-all-target-headers.hmap -iquote /Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-project-headers.hmap -mdynamic-no-pic -F/Users/crisman/Desktop/SageSrc/build/Release -I/Users/crisman/Desktop/SageSrc/build/Release/include -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/DerivedSources -isysroot /Developer/SDKs/MacOSX10.4u.sdk -c /Users/crisman/Desktop/SageSrc/Sage_Prefix.pch -o /Library/Caches/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-eznqjueptjnfnofhfaeeuuyiiihc/Sage_Prefix.pch.gch
In file included from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/DriverServices.h:32,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/CarbonCore.h:125,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Headers/CoreServices.h:21,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/ApplicationServices.framework/Headers/ApplicationServices.h:20,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Foundation.framework/Headers/NSAppleEventDescriptor.h:8,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Foundation.framework/Headers/Foundation.h:104,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Cocoa.framework/Headers/Cocoa.h:12,
                 from /Users/crisman/Desktop/SageSrc/Sage_Prefix.pch:6:
/Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/MachineExceptions.h:286: error: parse error before '*' token
/Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/MachineExceptions.h:320: error: parse error before '*' token
In file included from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/CarbonCore.h:161,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Headers/CoreServices.h:21,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/ApplicationServices.framework/Headers/ApplicationServices.h:20,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Foundation.framework/Headers/NSAppleEventDescriptor.h:8,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Foundation.framework/Headers/Foundation.h:104,
                 from /Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/Cocoa.framework/Headers/Cocoa.h:12,
                 from /Users/crisman/Desktop/SageSrc/Sage_Prefix.pch:6:
/Developer/SDKs/MacOSX10.4u.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/CarbonCore.framework/Headers/fp.h:1338: error: 'SIGDIGLEN' undeclared here (not in a function)
```



---

Comment by kcrisman created at 2010-09-10 23:51:25

Also, I get the big red X next to 

```
    #import <Cocoa/Cocoa.h>
```

in that file, which apparently is where things stopped.


---

Comment by iandrus created at 2010-09-13 07:07:12

I finally got the MACOSX_DEPLOYMENT_TARGET set in the Xcode interface by changing it 10.1, and then back.  For some reason changing between 10.5 and 10.4 didn't actually cause it to be set in the project file correctly, even though it showed up in the interface.  It finally builds an app with Minimum System Version set to 10.4 instead of 10.5.  I also deleted the SDK so it should default to what the machine has for default.  Hopefully this will allow it to be built on both 10.4 and on 10.6 without the 10.4 SDK.


---

Comment by jhpalmieri created at 2010-09-13 17:41:04

On 10.6, this builds successfully for me.  (There are a few warnings, but no errors.) It looks good to me; I like the new menus.  My comment about Terminal windows closing when the shell exits now applies to the option "Reveal in shell": if I'm lucky, I see a Terminal window flash open and then close, but sometimes I don't see anything at all.  I'm not sure this option is worth keeping; other opinions?

One other minor suggestion: perhaps change the "Sagemath" menu item in the Help menu to "www.sagemath.org" or "Visit www.sagemath.org"?


---

Comment by kcrisman created at 2010-09-13 18:00:45

Replying to [comment:63 iandrus]:
> I finally got the MACOSX_DEPLOYMENT_TARGET set in the Xcode interface by changing it 10.1, and then back.  For some reason changing between 10.5 and 10.4 didn't actually cause it to be set in the project file correctly, even though it showed up in the interface.  It finally builds an app with Minimum System Version set to 10.4 instead of 10.5.  I also deleted the SDK so it should default to what the machine has for default.  Hopefully this will allow it to be built on both 10.4 and on 10.6 without the 10.4 SDK.
Thanks, Ivan.  So close... now it attempts to open.  Apparently the selector is causing trouble, though, and it doesn't actually open.  Bug report coming up.


---

Comment by kcrisman created at 2010-09-13 18:02:33

As you can see, I tried several times :)  

```
2010-09-13 13:56:01.391 Sage[251] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:56:01.414 Sage[251] An uncaught exception was raised
2010-09-13 13:56:01.420 Sage[251] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:56:01.421 Sage[251] *** Uncaught exception: <NSInvalidArgumentException> *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
Sep 13 13:56:09 Dasher-03 crashdump[252]: Sage crashed
Sep 13 13:56:11 Dasher-03 crashdump[252]: crash report written to: /Users/student/Library/Logs/CrashReporter/Sage.crash.log
2010-09-13 13:56:46.859 Sage[255] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:56:46.859 Sage[255] An uncaught exception was raised
2010-09-13 13:56:46.860 Sage[255] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:56:46.860 Sage[255] *** Uncaught exception: <NSInvalidArgumentException> *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
Sep 13 13:56:59 Dasher-03 crashdump[256]: Sage crashed
Sep 13 13:57:02 Dasher-03 crashdump[256]: crash report written to: /Users/student/Library/Logs/CrashReporter/Sage.crash.log
2010-09-13 13:58:00.238 Sage[258] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:58:00.238 Sage[258] An uncaught exception was raised
2010-09-13 13:58:00.239 Sage[258] *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
2010-09-13 13:58:00.239 Sage[258] *** Uncaught exception: <NSInvalidArgumentException> *** -[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]: selector not recognized [self = 0x230af40]
Sep 13 13:58:11 Dasher-03 crashdump[259]: Sage crashed
Sep 13 13:58:18 Dasher-03 crashdump[259]: crash report written to: /Users/student/Library/Logs/CrashReporter/Sage.crash.log
```



---

Comment by kcrisman created at 2010-09-13 21:08:10

Another issue - if you start it without a binary inside, and then click to choose a starting binary, it turns out that if you choose the folder and not the "executable" (which I think means the script `$SAGE_ROOT/sage`), you never get a warning message, except in the Console.  Here is some pertinent information:

```

9/13/10 4:28:17 PM	Sage[9812]	sageBinary:(null)
9/13/10 4:28:30 PM	Sage[9812]	Not showing in Dock
9/13/10 4:30:02 PM	Sage[9812]	starting sage
9/13/10 4:30:02 PM	Sage[9812]	Running command: /Users/.../sage
```

And when I try to get a terminal (in this case, the preference was already for only menu bar item - really confusing to me that it remembers prefs, but I think that's probably "correct" behavior):

```
Last login: Mon Sep 13 16:30:05 on ttys000
/Users/.../sage; exit
$ /Users/.../sage; exit
-bash: /Users/.../sage: is a directory
logout

[Process completed]
```

But there is no check that first time that the executable actually is one if you don't have the Sage server starting automatically.  I realize this would be unusual - someone that started with some prefs - but anyway it seems like it should be checked for.


---

Comment by iandrus created at 2010-09-13 21:15:02

Replying to [comment:64 jhpalmieri]:
> On 10.6, this builds successfully for me.  (There are a few warnings, but no errors.) It looks good to me; I like the new menus.  My comment about Terminal windows closing when the shell exits now applies to the option "Reveal in shell": if I'm lucky, I see a Terminal window flash open and then close, but sometimes I don't see anything at all.  I'm not sure this option is worth keeping; other opinions?

I changed it to run `cd ... && $SHELL` which makes more sense anyway.  So that particular problem should be fixed.  I guess you can tell that I tested with a version that doesn't exit :-)

> One other minor suggestion: perhaps change the "Sagemath" menu item in the Help menu to "www.sagemath.org" or "Visit www.sagemath.org"?

Good idea.

Replying to [comment:65 kcrisman]:
> Replying to [comment:63 iandrus]:
> > I finally got the MACOSX_DEPLOYMENT_TARGET set in the Xcode interface by changing it 10.1, and then back.  For some reason changing between 10.5 and 10.4 didn't actually cause it to be set in the project file correctly, even though it showed up in the interface.  It finally builds an app with Minimum System Version set to 10.4 instead of 10.5.  I also deleted the SDK so it should default to what the machine has for default.  Hopefully this will allow it to be built on both 10.4 and on 10.6 without the 10.4 SDK.
> Thanks, Ivan.  So close... now it attempts to open.  Apparently the selector is causing trouble, though, and it doesn't actually open.  Bug report coming up.

I see that that is indeed 10.5+ only.  Unfortunately, I can't find how to get Xcode to warn me of such things.  I swear I had it doing that before...  Anyway, if you could try compiling again and send me any warnings that are produced when building.  I made sure to fix all the warnings on my machine.  In particular what we are looking for is "may not respond to" warnings.

Thanks both of you for your patience.


---

Comment by jhpalmieri created at 2010-09-13 21:24:29

> Thanks both of you for your patience.

No, thank you for your work here.

This might be more appropriate for a further ticket, but to what extent does the app depend on a Sage installation?  It seems like it shouldn't have to depend on it at all, because of the option to select another executable.  So it might be nice to a smaller app (the current one takes over 1 1/2 gigabytes on my machine) which is just the front end: it relies on having a separate Sage installation.  On my machine, I always create a link /Applications/sage/ pointing to SAGE_ROOT for my most recent Sage installation, so if I had a small app, I would just point it at /Applications/sage/sage, and I would never have to rebuild the app.

Or maybe there is an easy way to modify the current app to make it smaller so it does what I want: can I just delete the directory Contents/Resources/sage, as long as I use an external executable?  If something like this works, we might want to document it and separately distribute a smaller app, built this way, as a front end.


---

Comment by iandrus created at 2010-09-13 21:51:07

Replying to [comment:67 kcrisman]:
> Another issue - if you start it without a binary inside, and then click to choose a starting binary, it turns out that if you choose the folder and not the "executable" (which I think means the script `$SAGE_ROOT/sage`), you never get a warning message, except in the Console.  Here is some pertinent information:

I have changed it so that you can choose SAGE_ROOT (since I think that makes sense), but also that it will keep prompting you for a sage executable (which is $SAGE_ROOT/sage) until you choose one 

> And when I try to get a terminal (in this case, the preference was already for only menu bar item - really confusing to me that it remembers prefs, but I think that's probably "correct" behavior):

It's certainly standard.  It's just that you don't usually reinstall the same application so many times :-)

Replying to [comment:69 jhpalmieri]:
> This might be more appropriate for a further ticket, but to what extent does the app depend on a Sage installation?  It seems like it shouldn't have to depend on it at all, because of the option to select another executable.  So it might be nice to a smaller app (the current one takes over 1 1/2 gigabytes on my machine) which is just the front end: it relies on having a separate Sage installation.  On my machine, I always create a link /Applications/sage/ pointing to SAGE_ROOT for my most recent Sage installation, so if I had a small app, I would just point it at /Applications/sage/sage, and I would never have to rebuild the app.

You are right.  It doesn't really depend on Sage at all (except of course to be useful).

> Or maybe there is an easy way to modify the current app to make it smaller so it does what I want: can I just delete the directory Contents/Resources/sage, as long as I use an external executable?  If something like this works, we might want to document it and separately distribute a smaller app, built this way, as a front end.

You can just delete that directory, or instead just build from the xcode project instead of through `sage --bdist`.  Yes we probably ought to document this.  Perhaps we could have a `sage --app-bundle` command or something that would build it?  Or yet another option to `sage --bdist`.


---

Comment by kcrisman created at 2010-09-14 01:20:55

It seems to work!  But doesn't (?) ... although this may have to do with the fact that I'm installing a large spkg at the same time.  I'll try again in a second.  More relevantly...

```
If you think you have waited long enough, then try View Log under the Development menu which may give you some clues as to why it has not started.
```

There is no such option in the Development menu of the menu bar thing.

I also just want to echo jhpalmieri's comment.  It's not our patience, but yours - it will be so awesome to have something that has actually been tested by more than two people, look at all the (inevitable) bugs/user improvements already found.


---

Comment by kcrisman created at 2010-09-14 02:26:07

> There is no such option in the Development menu of the menu bar thing.
What I meant is of course that it is in the main menu.

Sadly, there seems to be yet ANOTHER problem.  I will try building it in a second.

```
2010-09-13 22:12:40.728 Sage[6297] sageBinary:/Users/crisman/Desktop/sage-4.5.3/sage
2010-09-13 22:12:40.776 Sage[6297] Starting server
2010-09-13 22:12:40.786 Sage[6297] Sage Browsing: /Users/crisman/Desktop/Sage-ppc.app/Contents/Resources/loading-page.html
usage: /Users/crisman/Desktop/Sage-ppc.app/Contents/Resources/start-sage.sh SAGE_EXECUTABLE LOG
2010-09-13 22:13:53.681 Sage[6297] starting sage
2010-09-13 22:13:53.692 Sage[6297] Running command: /Users/crisman/Desktop/sage-4.5.3/sage
2010-09-13 22:13:53.693 Sage[6297] *** -[NSCFString stringByReplacingOccurrencesOfString:withString:]: selector not recognized [self = 0x230cd70]
2010-09-13 22:13:53.698 Sage[6297] *** -[NSCFString stringByReplacingOccurrencesOfString:withString:]: selector not recognized [self = 0x230cd70]
```

Anyway, so nothing works.  Weirdly, the server shows up ending in the Console, but it never starts - localhost cannot be found, in fact.

> I see that that is indeed 10.5+ only. Unfortunately, I can't find how to get Xcode to warn me of such things. I swear I had it doing that before... Anyway, if you could try compiling again and send me any warnings that are produced when building. I made sure to fix all the warnings on my machine. In particular what we are looking for is "may not respond to" warnings.
I don't get any warnings, just failures.  Currently it makes it through the files, then (good!) finishes one of the two predefined headers or whatever (maybe both?), but fails at

```
Building target “Sage” of project “Sage” with configuration “Release”


Checking Dependencies
CompileC build/Sage.build/Release/Sage.build/Objects-normal/ppc/MyDocument.o /Users/crisman/Desktop/SageSrc/MyDocument.m normal ppc objective-c com.apple.compilers.gcc.4_0
    cd /Users/crisman/Desktop/SageSrc
    /Developer/usr/bin/gcc-4.0 -x objective-c -arch ppc -pipe -std=gnu99 -Wno-trigraphs -fpascal-strings -fasm-blocks -Os -Wreturn-type -Wunused-variable -fmessage-length=0 -mtune=G5 -fvisibility=hidden -mmacosx-version-min=10.4 -gdwarf-2 -iquote /Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-generated-files.hmap -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-own-target-headers.hmap -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-all-target-headers.hmap -iquote /Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Sage-project-headers.hmap -mdynamic-no-pic -F/Users/crisman/Desktop/SageSrc/build/Release -I/Users/crisman/Desktop/SageSrc/build/Release/include -I/Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/DerivedSources -include /Library/Caches/com.apple.Xcode.501/SharedPrecompiledHeaders/Sage_Prefix-fkbwhauskrjhrpepyujyksrnuqml/Sage_Prefix.pch -c /Users/crisman/Desktop/SageSrc/MyDocument.m -o /Users/crisman/Desktop/SageSrc/build/Sage.build/Release/Sage.build/Objects-normal/ppc/MyDocument.o
/Users/crisman/Desktop/SageSrc/MyDocument.m:162: error: parse error before 'NSInteger'
```

which is 

```
- (void)openPanelDidEnd:(NSSavePanel *)openPanel returnCode:(NSInteger)code contextInfo:(id <WebOpenPanelResultListener>)listener {
}}} 
I agree that it must be annoying that so many things were added.  I truly hope the effort will be worth it!


---

Comment by kcrisman created at 2010-09-14 02:27:37

> I agree that it must be annoying that so many things were added.  I truly hope the effort will be worth it!
I mean in Xcode for 10.5, of course, not in the Mac app!  There the extras are great :)


---

Attachment

Patch to plug into bdist


---

Comment by iandrus created at 2010-09-16 12:04:53

I fixed some things relating to building on 10.4.  This includes modifying sage -bdist, so if people could re-test that portion it would be great, particularly on 10.4 and 10.5.


---

Comment by kcrisman created at 2010-09-16 14:03:49

Replying to [comment:74 iandrus]:
> I fixed some things relating to building on 10.4.  This includes modifying sage -bdist, so if people could re-test that portion it would be great, particularly on 10.4 and 10.5.
I'm going to try using this later, but right now I want to ask whether `-a -e` is portable enough to satisfy drkirkby.  I know that one way of doing those is a "Gnuism" and the other one isn't.  It probably doesn't matter here, since we only do it on OS X, but still...


---

Comment by kcrisman created at 2010-09-17 14:38:52

Replying to [comment:74 iandrus]:
> I fixed some things relating to building on 10.4.  This includes modifying sage -bdist, so if people could re-test that portion it would be great, particularly on 10.4 and 10.5.

Okay, bdist works correctly on 10.4, both with and without `SAGE_APP_BUNDLE` set (that is, it works as it is supposed to). 

Jason or John, can you comment on whether you want anything else done to give this positive review?  Since this won't be the default bdist to start out, I think that it's okay to give this positive review so that people who aren't looking at this ticket can begin testing it for a while before it becomes default.  

Also, one very minor thing - should there be an "about" section in the menu extra?


---

Comment by iandrus created at 2010-09-20 19:25:51

I added a safeguard so that the MenuExtra always shows up on 10.4 since I can't figure out how to make it optionally be a regular application (in a clean way).  It's definitely not perfect, but at least you should never be left without a UI now (as could happen before).

I also added support for determining when the server is running in the case of using the system browser and added an option to not respect `SAGE_BROWSER` since that can be quite slow as it requires running `sage -c`.

Replying to [comment:76 kcrisman]:

> Also, one very minor thing - should there be an "about" section in the menu extra?

I don't think so because I don't think it would ever get used.

Replying to [comment:75 kcrisman]:
> I'm going to try using this later, but right now I want to ask whether `-a -e` is portable enough to satisfy drkirkby.  I know that one way of doing those is a "Gnuism" and the other one isn't.  It probably doesn't matter here, since we only do it on OS X, but still...

From discussion on sage-devel, I think we're okay here since we're already using bash instead of sh.


---

Comment by kcrisman created at 2010-09-21 02:33:55

Did you add something in one place but not another, related to checking whether Sage is running?  It didn't build the bundle on one of my 10.4 boxes this time.  This is based off of 4.6.alpha1.

```
CpResource build/Debug/Sage.app/Contents/Resources/sage-is-running-on-port.sh sage-is-running-on-port.sh
    cd /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app/sage-is-running-on-port.sh /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources
pbxcp: sage-is-running-on-port.sh: No such file or directory

CpResource build/Debug/Sage.app/Contents/Resources/English.lproj/MyDocument.nib English.lproj/MyDocument.nib
    cd /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app
    /Developer/Library/PrivateFrameworks/DevToolsCore.framework/Resources/pbxcp -exclude .DS_Store -exclude CVS -exclude .svn -resolve-src-symlinks /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app/English.lproj/MyDocument.nib /Users/crisman/Desktop/sage-4.6.alpha1/data/extcode/sage/ext/mac-app/build/Debug/Sage.app/Contents/Resources/English.lproj
** BUILD FAILED **
Failed to build Sage.app.
If you don't wish to build Sage.app set SAGE_APP_BUNDLE=no
```



---

Comment by iandrus created at 2010-09-21 06:21:56

Patch for the extcode repository


---

Attachment

Replying to [comment:78 kcrisman]:
> Did you add something in one place but not another, related to checking whether Sage is running?  It didn't build the bundle on one of my 10.4 boxes this time.  This is based off of 4.6.alpha1.

Yep, I forgot to add the script to the repository.  Fixed now.  Sorry.


---

Comment by kcrisman created at 2010-09-21 16:16:23

Seems to be working now - I'll report back later on tests. 

One thing I noticed is that the README.txt that appears (currently in `/local/bin`, I think) will have to be updated in this case.  I think there is already a trac ticket open for this in general, but of course for now this won't be the default.  I'm not sure how to handle it, other than adding a second (temporary) README and changing the bdist script to use that one instead of the usual one if one has `SAGE_APP_BUNDLE=yes`.


---

Comment by kcrisman created at 2010-09-21 16:38:12

Good, this seems to have fixed it on 10.4.  I'll check it out on higher one later.

I noticed that if you bdist from a Sage that doesn't have its documentation built, the first half of help pages don't exist.  (This could happen if, for instance, LaTeX wasn't in the path of the build.)  I don't know if this means they should be the live ones after all, which build (just not as nicely) without TeX... not sure about this.

Also, it's not possible to use a browser other than the system browser on 10.4 now.  What is the connection between this and the Dock - that is, why does it show up as a sub-preference?

But these are all relatively small issues, of course.


---

Comment by kcrisman created at 2010-09-21 16:59:47

> This will supersede #5296 if it gets in first.
Just bumping this in anticipation of things working out.  So perhaps for this ticket we add a non-default script, then if it's default #5296 can be closed.


---

Comment by kcrisman created at 2010-09-21 19:03:29

Ok, I've tested many version of this on OS X 10.4 PPC and 10.6 Intel, and I think that the following needs to be done for positive review:

 * Do something about the README issue.  This is necessary.
 * Find someone with an OS X 10.5 machine to test whether the bdisting works there too.  I think Marshall has one...

Otherwise this is at the point where it's time to let people try it, not just sit in obscurity.


---

Comment by iandrus created at 2010-09-21 20:10:44

Replying to [comment:81 kcrisman]:
> Good, this seems to have fixed it on 10.4.  I'll check it out on higher one later.

Excellent.

> I noticed that if you bdist from a Sage that doesn't have its documentation built, the first half of help pages don't exist.  (This could happen if, for instance, LaTeX wasn't in the path of the build.)  I don't know if this means they should be the live ones after all, which build (just not as nicely) without TeX... not sure about this.

It would be good to always have the documentation.  Perhaps someone who knows more about the documentation could give some insight into what would be preferred.  The only thing that I want is that it be offline, i.e. doesn't need network access.

> Also, it's not possible to use a browser other than the system browser on 10.4 now.  What is the connection between this and the Dock - that is, why does it show up as a sub-preference?

If the application doesn't show up in the dock then the windows don't belong to any application (like the Preferences window now).  I think this would be extremely confusing and nearly impossible to work with.  It's okay for Preferences because it's a single window.

Replying to [comment:83 kcrisman]:
> Ok, I've tested many version of this on OS X 10.4 PPC and 10.6 Intel, and I think that the following needs to be done for positive review:

>  * Do something about the README issue.  This is necessary.

Can we just change the OS X README to have a section about Sage.app and a section for the case that it's not created since it will still be possible to create a binary distribution without Sage.app?

>  * Find someone with an OS X 10.5 machine to test whether the bdisting works there too.  I think Marshall has one...


---

Comment by kcrisman created at 2010-09-21 20:15:07

> > I noticed that if you bdist from a Sage that doesn't have its documentation built, the first half of help pages don't exist.  (This could happen if, for instance, LaTeX wasn't in the path of the build.)  I don't know if this means they should be the live ones after all, which build (just not as nicely) without TeX... not sure about this.
> 
> It would be good to always have the documentation.  Perhaps someone who knows more about the documentation could give some insight into what would be preferred.  The only thing that I want is that it be offline, i.e. doesn't need network access.

I think that the 'live' documentation only needs the local browser and the ability to connect that way.   No actual network connection is needed, just on the person's computer.

> > Also, it's not possible to use a browser other than the system browser on 10.4 now.  What is the connection between this and the Dock - that is, why does it show up as a sub-preference?
> 
> If the application doesn't show up in the dock then the windows don't belong to any application (like the Preferences window now).  I think this would be extremely confusing and nearly impossible to work with.  It's okay for Preferences because it's a single window.

Thanks for clarifying that.
> Can we just change the OS X README to have a section about Sage.app and a section for the case that it's not created since it will still be possible to create a binary distribution without Sage.app?

That sounds like a great solution.  You can finally remove that part about OS X gurus - because you are one now :)

Great, really close now!  I think the relevant file can be checked in using `hg_scripts`, so you'd probably want to just make it depend on the already existing `hg_scripts` change for `bdist`.


---

Comment by iandrus created at 2010-09-21 20:50:36

Replying to [comment:85 kcrisman]:
> > Can we just change the OS X README to have a section about Sage.app and a section for the case that it's not created since it will still be possible to create a binary distribution without Sage.app?
> 
> That sounds like a great solution.  You can finally remove that part about OS X gurus - because you are one now :)
> 
> Great, really close now!  I think the relevant file can be checked in using `hg_scripts`, so you'd probably want to just make it depend on the already existing `hg_scripts` change for `bdist`.

It looks like sage-README-osx.txt is in .hgignore and is not checked into mercurial.  It is in the sage_scripts spkg though, so I'm confused about that.  I'm just going to put the file here i.e. not as a patch.


---

Attachment

To edit the file sage-README-osx.txt, you should edit the one in local/bin (the one in the sage-scripts repo); this should automatically be copied to the top level directory of the relevant dmg.

(As kcrisman will also tell you, the one in SAGE_ROOT shouldn't even be there in the first place. See #6938, the resolution of which was to delete SAGE_ROOT/sage-README-osx.txt.)


---

Comment by jhpalmieri created at 2010-09-21 23:20:25

A few comments on sage-README.osx.txt: 

 - overall, I like the changes.

 - when I create the app and open up the dmg, I see two "files": README.txt and "Sage-VERSION".  I don't see anything called "Sage-VERSION.app".  When I don't create the app, I see README.txt and a *folder* called "sage". So maybe we could change

```
One is as a
"regular" OS X application named something like Sage-VERSION.app.  If
you see such an application skip to the section about Sage.app.
```

 to

```
One is as a
"regular" OS X application named something like Sage-VERSION.  If
you see such an application, skip to the section about Sage.app.  
If you instead see a folder called "sage", proceed as follows.
```


 - on line 56, "holding the option" should either be "holding option" or "holding the option key".  I have a slight preference for the second of these, in which case "holding command" should be changed correspondingly.

 - I don't understand the instructions

```
Therefore please use something like

SAGE_BROWSER=${SAGE_BROWSER-YOUR_VALUE}
```

 Maybe add an explicit example?

 - would it be worth adding a section on how to build the app if you don't have it?  This could be combined with, or referenced from, the section on Tiger and the comment on running "sage -bdist".


---

Comment by kcrisman created at 2010-09-22 00:22:40

I like John's comments.  A few copy-editing remarks:

In line 52, sage should be Sage, as in line 80.  There might be others, you should just check quickly.  

Line 129 has 'dock', but everywhere else it seems to be 'Dock'.  

I would also use "OS X 10.4 (Tiger)" instead of just "10.4 (Tiger)", as there might be one or two folks unsure what the 10.4 is referring to and scared it might be special instructions for them.

John is also right about how and where to edit the `sage-README-osx.txt` file.


---

Comment by mhampton created at 2010-09-22 01:41:43

My laptop runs 10.5, so I will try to test this on that.
-Marshall


---

Comment by mhampton created at 2010-09-22 01:48:13

I'm confused about how to apply the patch.  Can someone summarize what to do?

Thanks,
Marshall


---

Comment by jhpalmieri created at 2010-09-22 02:30:36

Replying to [comment:91 mhampton]:
> I'm confused about how to apply the patch.  Can someone summarize what to do?

From within Sage, for example:

```
sage: hg_extcode.import_patch('trac_9873_extcode_sage_deluxe.patch')
sage: hg_scripts.import_patch('trac_9873_scripts_sage_deluxe.patch')
```

Then quit Sage and do

```
$ export SAGE_APP_BUNDLE=yes
$ sage -bdist 4.6.beta0
```

(I just made up "4.6.beta0"; I don't think it matters what version you type in.)

Then after a while, you'll end up with a folder called something like `SAGE_ROOT/dist/sage-4.6.beta0-i386-Darwin/Sage-4.6.alpha2.app`.  Move this to /Applications or to ~/Desktop or someplace, then double-click on it.


---

Comment by mhampton created at 2010-09-22 03:50:11

Changing assignee from iandrus to mhampton.


---

Comment by mhampton created at 2010-09-22 03:50:11

Thanks John.

It seems to work fine on OS X 10.5.  I didn't read the new readme first, just started it up and used Server->Start Server.  This seemed to work fine although it took a while to start up the first time.  Looking at the log it seems this is just from the move to the Desktop; later starts were much quicker.  The latest readme seems more complicated than that, so either I am doing something wrong or the instructions could be simplified.

This is really great progress though, great work.


---

Comment by iandrus created at 2010-09-22 09:54:55

I created another patch trac_9873_scripts_sage_deluxe_plus_readme.patch which includes the changes to sage -bdist as well as adding the README to the repository.  It supersedes the old scripts patch and all the READMEs.  I'm not sure if it will apply cleanly since sage-README-osx.txt is already in the directory, but not tracked.

So the two patches needed are `trac_9873_extcode_sage_deluxe.patch` and `trac_9873_scripts_sage_deluxe_plus_readme.patch`.


---

Comment by kcrisman created at 2010-09-23 00:29:38

Assuming the new patch applies properly (I can't test this now) it should be fine, with the exception that John's comment for an example for `SAGE_BROWSER` leaves me even more confused now that there IS an example.  What is

```
SAGE_BROWSER=${SAGE_BROWSER-/Applications/Sage-Fluid.app/Contents/Resources/open-location.sh
```

?  Fluid?  what does `open-location.sh` have to do with things?  Is this an option to a command?


---

Comment by kcrisman created at 2010-09-23 17:40:53

Replying to [comment:94 iandrus]:
> I created another patch trac_9873_scripts_sage_deluxe_plus_readme.patch which includes the changes to sage -bdist as well as adding the README to the repository.  It supersedes the old scripts patch and all the READMEs.  I'm not sure if it will apply cleanly since sage-README-osx.txt is already in the directory, but not tracked.

No, it doesn't apply cleanly.  So the release manager would have to do the following upon positive review:

 * Remove `sage-README-osx.txt` from the scripts repository

 * Apply the patches here to the extcode and scripts repositories.

 * Close #5296 and this ticket

 * Rejoice!

I'm ready to give this positive review once Ivan explains the `SAGE_BROWSER` comment above :)


---

Comment by iandrus created at 2010-09-23 17:50:18

Replying to [comment:95 kcrisman]:
> Assuming the new patch applies properly (I can't test this now) it should be fine, with the exception that John's comment for an example for `SAGE_BROWSER` leaves me even more confused now that there IS an example.  What is
> {{{
> SAGE_BROWSER=${SAGE_BROWSER-/Applications/Sage-Fluid.app/Contents/Resources/open-location.sh
> }}}
> ?  Fluid?  what does `open-location.sh` have to do with things?  Is this an option to a command?

I just put what I had it set to--I used an instance of Fluid which comes with a script to open things from the command line.  I have changed it to

```
SAGE_BROWSER=${SAGE_BROWSER-/path/to/script/to/open/your/browser}
```

Hopefully that is more understandable.


---

Attachment

Great!   It applies fine once I remove the old file, still builds fine, and it even knows that it can't open from within the disk image (just tried that, but read-only filesystem).

VERY nice work and I hope that it all goes well with merging - I'm cc:ing the release manager, since this should be quite orthogonal to anything else (unless someone messed with sage-bdist) in 4.6.


---

Comment by kcrisman created at 2010-09-23 18:56:27

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 11:27:33

Just to check: Should I follow the steps in [comment:96 comment 96], except use [attachment:trac_9873_scripts_sage_deluxe_plus_readme.patch] as the only scripts repository patch?


---

Comment by iandrus created at 2010-09-28 12:30:42

Replying to [comment:99 mpatel]:
> Just to check: Should I follow the steps in [comment:96 comment 96], except use [attachment:trac_9873_scripts_sage_deluxe_plus_readme.patch] as the only scripts repository patch?

That's correct.  I wish I could delete all but the 2 relevant patches, but there you have it.

Thanks,
Ivan


---

Comment by kcrisman created at 2010-09-28 13:05:10

Replying to [comment:101 iandrus]:
> Replying to [comment:99 mpatel]:
> > Just to check: Should I follow the steps in [comment:96 comment 96], except use [attachment:trac_9873_scripts_sage_deluxe_plus_readme.patch] as the only scripts repository patch?
Like Ivan says, yes.
> That's correct.  I wish I could delete all but the 2 relevant patches, but there you have it.
Yeah, it's really annoying that one can't even delete one's OWN patches, though I understand that for archiving one might want to have several versions... yet if one just gives it the same name and clicks on "replace", it goes away.  Is this a bug?

By the way, congrats on reaching 100 comments, Ivan!  There should be an award for such tickets...


---

Comment by jason created at 2010-09-28 13:29:09

I hereby nominate Ivan for the "most persistant author" club!


---

Comment by davidloeffler created at 2010-09-28 13:41:50

Competition is tough though, since #9343 has 393 comments and counting :-)


---

Comment by jason created at 2010-09-28 13:45:14

Yes, the club only has the very elite (persistant) authors!


---

Comment by mpatel created at 2010-09-29 09:51:13

It seems that `sage-README-osx.txt` is under revision control in the scripts repository.  Can someone post an update of the scripts repo patch that doesn't first require deleting the file?  Or am I mistaken?


---

Comment by mpatel created at 2010-09-29 09:51:20

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2010-09-29 12:17:51

Replying to mpatel:

> It seems that sage-README-osx.txt is under revision control in the scripts repository. Can someone post an update of the scripts repo patch that doesn't first require deleting the file? Or am I mistaken?

Hmm, maybe that's new? You're right that the file isn't in .hgignore. Of course, that file includes

```
sage-bdist~
sage-clone~   
```

Whatever that means, since without the ~ those are obviously under revision control.

And running hg on that file gives me

```
changeset:   992:e83ef403be0d
user:        mabshoff`@`sage.math.washington.edu
date:        Fri Oct 31 14:25:18 2008 -0700
summary:     Update README

changeset:   837:ee5ea120914a
tag:         3.0.2.alpha0
user:        William Stein <wstein`@`gmail.com>
date:        Sat May 10 16:21:08 2008 -0700
summary:     trac #3136 -- the readme for osx should be changed to delete the line about inotebook()
```

and so on. So apparently this will have to be done. I am not sure if I will have time right now, but I'll try my best.


---

Comment by jhpalmieri created at 2010-09-29 14:53:20

Replying to [comment:106 mpatel]:
> It seems that `sage-README-osx.txt` is under revision control in the scripts repository.  Can someone post an update of the scripts repo patch that doesn't first require deleting the file?  Or am I mistaken?

I think you're mistaken.  It's included in the scripts spkg (I'm not sure how it gets there and I don't have time to look at it now), but it's not under revision control.  If you cd to the local/bin directory and type "hg manifest", that file is not listed.

This may still "need work": if we add file to the repo but then it also gets copied there manually, that's not good.


---

Comment by jhpalmieri created at 2010-09-29 14:56:53

Changing status from needs_work to positive_review.


---

Comment by jhpalmieri created at 2010-09-29 14:56:53

I think this is okay as is.  In the script sage-make_devel_packages, the line

```
cp -p $SAGE_ROOT/*.txt $SCRIPTS/
```

copies SAGE_ROOT/sage-README-osx.txt to the scripts repo, but if that file gets deleted from SAGE_ROOT (it's still there in 4.6.alpha1), then it shouldn't appear again in the scripts repo.


---

Comment by kcrisman created at 2010-09-29 18:45:44

Replying to [comment:110 jhpalmieri]:
> I think this is okay as is.  In the script sage-make_devel_packages, the line
> {{{
> cp -p $SAGE_ROOT/*.txt $SCRIPTS/
> }}}
> copies SAGE_ROOT/sage-README-osx.txt to the scripts repo, but if that file gets deleted from SAGE_ROOT (it's still there in 4.6.alpha1), then it shouldn't appear again in the scripts repo.

Then the release manager should first close #5296, then do the stuff on this one.  In that sense this ticket now 'depends' on #5296.


---

Comment by jhpalmieri created at 2010-09-29 20:05:31

I thought that the file was deleted from SAGE_ROOT because of #6938 (merged in 4.6.alpha1).  So I'm not sure in what sense this depends on #5296.  But I think I'm getting confused...


---

Comment by kcrisman created at 2010-09-29 20:09:08

Replying to [comment:112 jhpalmieri]:
> I thought that the file was deleted from SAGE_ROOT because of #6938 (merged in 4.6.alpha1).  So I'm not sure in what sense this depends on #5296.  But I think I'm getting confused...
You're right that it SHOULD have been.  I got confused, too, though; it's #6938 that should have taken care of this.


---

Comment by iandrus created at 2010-09-29 21:38:18

Replying to [comment:108 kcrisman]:
> Replying to mpatel:
> 
> > It seems that sage-README-osx.txt is under revision control in the scripts repository. Can someone post an update of the scripts repo patch that doesn't first require deleting the file? Or am I mistaken?
> 
> Hmm, maybe that's new? You're right that the file isn't in .hgignore. Of course, that file includes

```
sage-bdist~
sage-clone~   
```

> Whatever that means, since without the ~ those are obviously under revision control.

The tilde is a common means of indicating a backup file.  It should be something like `*~` though to ignore all backup files.  But that's another patch for another day :-)

> And running hg on that file gives me

```
changeset:   992:e83ef403be0d
user:        mabshoff`@`sage.math.washington.edu
date:        Fri Oct 31 14:25:18 2008 -0700
summary:     Update README

changeset:   837:ee5ea120914a
tag:         3.0.2.alpha0
user:        William Stein <wstein`@`gmail.com>
date:        Sat May 10 16:21:08 2008 -0700
summary:     trac #3136 -- the readme for osx should be changed to delete the line about inotebook()
```

> and so on. So apparently this will have to be done. I am not sure if I will have time right now, but I'll try my best.

I was very confused by this for a long time, but I finally tracked it down to 

```
$ hg log -r 1370
changeset:   1370:80bc1e909378
user:        Mike Hansen <mhansen`@`gmail.com>
date:        Thu Nov 12 20:55:24 2009 -0800
summary:     Remove the sage-README-osx.txt file from the scripts repo.
```


Personally I think it's a bug in mercurial to not show removal of a file in `hg log`.


---

Comment by mpatel created at 2010-09-29 23:06:35

Thanks to everyone for clearing my confusion!

The analogue of [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2) for alpha1 did include a line to remove the root `sage-README-osx.txt`.  I don't know why it reappeared.  It's quite possible that I made a mistake.


---

Comment by mpatel created at 2010-09-29 23:17:44

Resolution: fixed
