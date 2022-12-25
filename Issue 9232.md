# Issue 9232: jmol on commandline broken

archive/issues_009232.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @jasongrout @jdemeyer\n\nI can't see Graphics3d objects on the command line. For example, \n\n```\nsage: sphere()\nsage: \n```\n\nThe command returns without starting jmol or producing any other graphical output.\n\nStrangely enough, I can start jmol from the sage command line:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: !jmol\nsplash_image=jar:file:/home/vbraun/opt/sage-hg/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar!/org/openscience/jmol/images/Jmol_splash.jpg\nhistory file is /home/vbraun/.jmol/history\nusing Smarter Model Adapter\n(C) 2008 Jmol Development\nJmol Version 11.6.16  2008-11-24 13:39\njava.vendor:Sun Microsystems Inc.\njava.version:1.6.0_18\nos.name:Linux\nmemory:9.8/21.1\nuseCommandThread: false\nUser macros dir: /home/vbraun/.jmol/macros\n       exists: false\n  isDirectory: false\n```\n\n| Sage Version 4.4.3, Release Date: 2010-06-04                       |\n| Type notebook() for the GUI, and license() for information.        |\nThe following also works and shows a tachyon-generated plot:\n\n```\nsphere(viewer='tachyon')\n```\n\n\nMore verbosity:\n\n```\nsage: sphere(verbosity=99)\nTraceback (most recent call last):\n  File \"/home/vbraun/Sage/sage/local/bin/sage-pypkg-location\", line 3, in <module>\n    from pkg_resources import Requirement, working_set\nzipimport.ZipImportError: can't decompress data; zlib not available\nJmol.jar not found\n```\n\n\nFor the record, I'm running Fedora 13 x86_64\n\nIssue created by migration from https://trac.sagemath.org/ticket/9232\n\n",
    "created_at": "2010-06-13T20:57:16Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "jmol on commandline broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9232",
    "user": "https://github.com/vbraun"
}
```
Assignee: jason, was

CC:  @kcrisman @jasongrout @jdemeyer

I can't see Graphics3d objects on the command line. For example, 

```
sage: sphere()
sage: 
```

The command returns without starting jmol or producing any other graphical output.

Strangely enough, I can start jmol from the sage command line:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: !jmol
splash_image=jar:file:/home/vbraun/opt/sage-hg/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar!/org/openscience/jmol/images/Jmol_splash.jpg
history file is /home/vbraun/.jmol/history
using Smarter Model Adapter
(C) 2008 Jmol Development
Jmol Version 11.6.16  2008-11-24 13:39
java.vendor:Sun Microsystems Inc.
java.version:1.6.0_18
os.name:Linux
memory:9.8/21.1
useCommandThread: false
User macros dir: /home/vbraun/.jmol/macros
       exists: false
  isDirectory: false
```

| Sage Version 4.4.3, Release Date: 2010-06-04                       |
| Type notebook() for the GUI, and license() for information.        |
The following also works and shows a tachyon-generated plot:

```
sphere(viewer='tachyon')
```


More verbosity:

```
sage: sphere(verbosity=99)
Traceback (most recent call last):
  File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
    from pkg_resources import Requirement, working_set
zipimport.ZipImportError: can't decompress data; zlib not available
Jmol.jar not found
```


For the record, I'm running Fedora 13 x86_64

Issue created by migration from https://trac.sagemath.org/ticket/9232





---

archive/issue_comments_086490.json:
```json
{
    "body": "Does it work if you install the new version of Jmol?  See trac # 9238.  I think this broke when the notebook was put inside an egg.  I took that into account with the new version of Jmol.",
    "created_at": "2010-07-14T22:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86490",
    "user": "https://github.com/gutow"
}
```

Does it work if you install the new version of Jmol?  See trac # 9238.  I think this broke when the notebook was put inside an egg.  I took that into account with the new version of Jmol.



---

archive/issue_comments_086491.json:
```json
{
    "body": "I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.",
    "created_at": "2010-07-14T23:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86491",
    "user": "https://github.com/vbraun"
}
```

I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.



---

archive/issue_comments_086492.json:
```json
{
    "body": "It was worth a try as that still could have been a hidden Jmol.jar file not found error.  This is different than the problem I addressed.  Sorry.  I would guess it is a problem with the \"sphere\" command.  Does it work with a simple plot3d command?  I've tested the 1.1 version on MacOS and Ubuntu and it seems to work for me.\nReplying to [comment:2 vbraun]:\n> I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.",
    "created_at": "2010-07-15T00:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86492",
    "user": "https://github.com/gutow"
}
```

It was worth a try as that still could have been a hidden Jmol.jar file not found error.  This is different than the problem I addressed.  Sorry.  I would guess it is a problem with the "sphere" command.  Does it work with a simple plot3d command?  I've tested the 1.1 version on MacOS and Ubuntu and it seems to work for me.
Replying to [comment:2 vbraun]:
> I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.



---

archive/issue_comments_086493.json:
```json
{
    "body": "I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:\n\n```\nsage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output\nsage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)\nTraceback (most recent call last):\n  File \"/home/vbraun/Sage/sage/local/bin/sage-pypkg-location\", line 3, in <module>\n    from pkg_resources import Requirement, working_set\nzipimport.ZipImportError: can't decompress data; zlib not available\nJmol.jar not found\n```\n",
    "created_at": "2010-07-15T00:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86493",
    "user": "https://github.com/vbraun"
}
```

I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:

```
sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output
sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)
Traceback (most recent call last):
  File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
    from pkg_resources import Requirement, working_set
zipimport.ZipImportError: can't decompress data; zlib not available
Jmol.jar not found
```




---

archive/issue_comments_086494.json:
```json
{
    "body": "Try installing the Jmol for notebook again.  It looks like the file on my server got corrupted and was missing the Jmol.jar application file as well as some others..Not sure what happened but we've had some power outages and the server may have been rebuilt from backups.  I've uploaded a new copy.\n\nBecause the name hasn't changed you will probably have to do some surgery to get it to download and do an install.  You will need to delete any copies of the .spkg (or its uncompressed directory) that you find in any of these subdirectories of your sage install before trying an install.  If you don't get a message about downloading the file you missed something:\nspkg/build\nspkg/installed\nspkg/optional\n\nLet us know if this fixes it.  Sorry for the inconvenience.\nJonathan\nReplying to [comment:4 vbraun]:\n> I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:\n> {{{\n> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output\n> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)\n> Traceback (most recent call last):\n>   File \"/home/vbraun/Sage/sage/local/bin/sage-pypkg-location\", line 3, in <module>\n>     from pkg_resources import Requirement, working_set\n> zipimport.ZipImportError: can't decompress data; zlib not available\n> Jmol.jar not found\n> }}}",
    "created_at": "2010-07-15T03:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86494",
    "user": "https://github.com/gutow"
}
```

Try installing the Jmol for notebook again.  It looks like the file on my server got corrupted and was missing the Jmol.jar application file as well as some others..Not sure what happened but we've had some power outages and the server may have been rebuilt from backups.  I've uploaded a new copy.

Because the name hasn't changed you will probably have to do some surgery to get it to download and do an install.  You will need to delete any copies of the .spkg (or its uncompressed directory) that you find in any of these subdirectories of your sage install before trying an install.  If you don't get a message about downloading the file you missed something:
spkg/build
spkg/installed
spkg/optional

Let us know if this fixes it.  Sorry for the inconvenience.
Jonathan
Replying to [comment:4 vbraun]:
> I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:
> {{{
> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output
> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)
> Traceback (most recent call last):
>   File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
>     from pkg_resources import Requirement, working_set
> zipimport.ZipImportError: can't decompress data; zlib not available
> Jmol.jar not found
> }}}



---

archive/issue_comments_086495.json:
```json
{
    "body": "I did a\n\n```\n[vbraun@localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg\n[vbraun@localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg\n```\n\nand it re-downloaded the Jmol spkg. Still fails with the same error message.",
    "created_at": "2010-07-15T04:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86495",
    "user": "https://github.com/vbraun"
}
```

I did a

```
[vbraun@localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg
[vbraun@localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg
```

and it re-downloaded the Jmol spkg. Still fails with the same error message.



---

archive/issue_comments_086496.json:
```json
{
    "body": "There is something special about your system...I've just retested that things work for Sage 4.4.3 on MacOS and Ubuntu Linux.  Let's see if everything actually got installed:\nCan you please post the directory listing (ls -l please) for the following two directories:\n<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol\nand\n<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/appletweb\n\nIf everything is there, I'm mystified.  If everything is not, then something is wrong with the install for your system and the .spkg needs to be fixed.\n\nJonathan\nReplying to [comment:6 vbraun]:\n> I did a\n> {{{\n> [vbraun`@`localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg\n> [vbraun`@`localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg\n> }}}\n> and it re-downloaded the Jmol spkg. Still fails with the same error message.\n>",
    "created_at": "2010-07-15T12:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86496",
    "user": "https://github.com/gutow"
}
```

There is something special about your system...I've just retested that things work for Sage 4.4.3 on MacOS and Ubuntu Linux.  Let's see if everything actually got installed:
Can you please post the directory listing (ls -l please) for the following two directories:
<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol
and
<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/appletweb

If everything is there, I'm mystified.  If everything is not, then something is wrong with the install for your system and the .spkg needs to be fixed.

Jonathan
Replying to [comment:6 vbraun]:
> I did a
> {{{
> [vbraun`@`localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg
> [vbraun`@`localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg
> }}}
> and it re-downloaded the Jmol spkg. Still fails with the same error message.
>



---

archive/issue_comments_086497.json:
```json
{
    "body": "I saved the `sys.path` within `sage-pypkg-location`, and it reads:\n\n```\n/home/vbraun/opt/sage-4.5.alpha1/local/bin\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/setuptools-0.6c9-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZODB3-3.7.0-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zdaemon-2.0.0-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZConfig-2.5-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testing-3.5.0-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.proxy-3.4.0-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Pygments-0.11.1-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja-1.2-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/SQLAlchemy-0.5.8-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/pytz-2010h-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.i18nmessageid-3.5.2-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.event-3.5.0_1-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ClientForm-0.2.10-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/mechanize-0.1.11-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.schema-3.6.3-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testbrowser-3.8.1-py2.6.egg\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg\n/home/vbraun/opt/sage-4.5.alpha1\n/home/vbraun/Sage/sage/local/lib/python\n/home/vbraun/Sage/sage/local/lib64/python26.zip\n/home/vbraun/Sage/sage/local/lib64/python2.6\n/home/vbraun/Sage/sage/local/lib64/python2.6/plat-linux2\n/home/vbraun/Sage/sage/local/lib64/python2.6/lib-tk\n/home/vbraun/Sage/sage/local/lib64/python2.6/lib-old\n/home/vbraun/Sage/sage/local/lib64/python2.6/lib-dynload\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/PIL\n```\n\nBut sage install zlib in\n\n```\n[vbraun@volker-two sage-4.5.alpha1]$ find | grep zlib.so\n./local/lib/python2.6/lib-dynload/zlib.so\n```\n\nNote: `/lib/`, not `/lib64/`. This explains why zlib cannot be imported. For the record, all libraries are 64-bit on my system.\n\nFrom within Sage, on the other hand, `sys.path` is set appropriately:\n\n```\nsage: '/home/vbraun/Sage/sage/local/lib/python2.6/lib-dynload' in sys.path\nTrue\n```\n",
    "created_at": "2010-07-15T14:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86497",
    "user": "https://github.com/vbraun"
}
```

I saved the `sys.path` within `sage-pypkg-location`, and it reads:

```
/home/vbraun/opt/sage-4.5.alpha1/local/bin
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/setuptools-0.6c9-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZODB3-3.7.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zdaemon-2.0.0-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZConfig-2.5-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testing-3.5.0-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.proxy-3.4.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Pygments-0.11.1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja-1.2-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/SQLAlchemy-0.5.8-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/pytz-2010h-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.i18nmessageid-3.5.2-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.event-3.5.0_1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ClientForm-0.2.10-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/mechanize-0.1.11-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.schema-3.6.3-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testbrowser-3.8.1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg
/home/vbraun/opt/sage-4.5.alpha1
/home/vbraun/Sage/sage/local/lib/python
/home/vbraun/Sage/sage/local/lib64/python26.zip
/home/vbraun/Sage/sage/local/lib64/python2.6
/home/vbraun/Sage/sage/local/lib64/python2.6/plat-linux2
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-tk
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-old
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-dynload
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/PIL
```

But sage install zlib in

```
[vbraun@volker-two sage-4.5.alpha1]$ find | grep zlib.so
./local/lib/python2.6/lib-dynload/zlib.so
```

Note: `/lib/`, not `/lib64/`. This explains why zlib cannot be imported. For the record, all libraries are 64-bit on my system.

From within Sage, on the other hand, `sys.path` is set appropriately:

```
sage: '/home/vbraun/Sage/sage/local/lib/python2.6/lib-dynload' in sys.path
True
```




---

archive/issue_comments_086498.json:
```json
{
    "body": "For the record, creating a symlink $SAGE_ROOT/local/lib64 pointing to $SAGE_ROOT/local/lib works. Another workaround is adding LIBRARY_PATH to DYLD_LIBRARY_PATH in sage-native-execute (from logix/#sage-devel).\n\nI still don't understand the underlying cause, where does python get the incorrect path from?",
    "created_at": "2010-08-05T16:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86498",
    "user": "https://github.com/vbraun"
}
```

For the record, creating a symlink $SAGE_ROOT/local/lib64 pointing to $SAGE_ROOT/local/lib works. Another workaround is adding LIBRARY_PATH to DYLD_LIBRARY_PATH in sage-native-execute (from logix/#sage-devel).

I still don't understand the underlying cause, where does python get the incorrect path from?



---

archive/issue_comments_086499.json:
```json
{
    "body": "#10286 is a follow-up which hopefully fixes this, such that this ticket can be closed as a duplicate when #10286 got merged.",
    "created_at": "2010-12-13T15:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86499",
    "user": "https://github.com/nexttime"
}
```

#10286 is a follow-up which hopefully fixes this, such that this ticket can be closed as a duplicate when #10286 got merged.



---

archive/issue_comments_086500.json:
```json
{
    "body": "Changing assignee from jason, was to @gutow.",
    "created_at": "2011-03-21T13:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86500",
    "user": "https://github.com/gutow"
}
```

Changing assignee from jason, was to @gutow.



---

archive/issue_comments_086501.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-03-21T13:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86501",
    "user": "https://github.com/gutow"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086502.json:
```json
{
    "body": "Attachment [trac_9232_plot3d_base_pyx.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_plot3d_base_pyx.patch) by @gutow created at 2011-03-22 14:49:28\n\nplot3d/base.pyx fixes to launch Jmol from cmd line",
    "created_at": "2011-03-22T14:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86502",
    "user": "https://github.com/gutow"
}
```

Attachment [trac_9232_plot3d_base_pyx.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_plot3d_base_pyx.patch) by @gutow created at 2011-03-22 14:49:28

plot3d/base.pyx fixes to launch Jmol from cmd line



---

archive/issue_comments_086503.json:
```json
{
    "body": "Notebook fixes for launch Jmol from cmd line",
    "created_at": "2011-03-22T14:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86503",
    "user": "https://github.com/gutow"
}
```

Notebook fixes for launch Jmol from cmd line



---

archive/issue_comments_086504.json:
```json
{
    "body": "Attachment [trac_9232_notebook_fixes.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_notebook_fixes.patch) by @gutow created at 2011-03-22 15:09:44\n\nThe above patches combined with installation of a newer version of Jmol fix this problem for Sage 4.6.2.  To install the new Jmol\n\n```\n./sage -f \"http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.5.spkg\"\n```\n\n\nNote that my linux and MacOS versions of sage seemed to have slightly different mercurial tracking.  On MacOS you get a warning about the SageMenu.mnu file, when you apply the notebook_fixes patch.  That is OK, the other untracked files are properly added.",
    "created_at": "2011-03-22T15:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86504",
    "user": "https://github.com/gutow"
}
```

Attachment [trac_9232_notebook_fixes.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_notebook_fixes.patch) by @gutow created at 2011-03-22 15:09:44

The above patches combined with installation of a newer version of Jmol fix this problem for Sage 4.6.2.  To install the new Jmol

```
./sage -f "http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.5.spkg"
```


Note that my linux and MacOS versions of sage seemed to have slightly different mercurial tracking.  On MacOS you get a warning about the SageMenu.mnu file, when you apply the notebook_fixes patch.  That is OK, the other untracked files are properly added.



---

archive/issue_comments_086505.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-22T15:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86505",
    "user": "https://github.com/gutow"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086506.json:
```json
{
    "body": "This will have to be part of a new SageNB package before it can be merged.  See also #9238.",
    "created_at": "2011-03-22T16:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86506",
    "user": "https://github.com/kcrisman"
}
```

This will have to be part of a new SageNB package before it can be merged.  See also #9238.



---

archive/issue_comments_086507.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> This will have to be part of a new SageNB package before it can be merged.  See also #9238.\n\nOK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?",
    "created_at": "2011-03-22T16:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86507",
    "user": "https://github.com/gutow"
}
```

Replying to [comment:14 kcrisman]:
> This will have to be part of a new SageNB package before it can be merged.  See also #9238.

OK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?



---

archive/issue_comments_086508.json:
```json
{
    "body": "Replying to [comment:15 gutow]:\n> Replying to [comment:14 kcrisman]:\n> > This will have to be part of a new SageNB package before it can be merged.  See also #9238.\n> \n> OK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?\nYes, eventually!  This is just for informational purposes to someone coming to the ticket.",
    "created_at": "2011-03-22T16:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86508",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:15 gutow]:
> Replying to [comment:14 kcrisman]:
> > This will have to be part of a new SageNB package before it can be merged.  See also #9238.
> 
> OK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?
Yes, eventually!  This is just for informational purposes to someone coming to the ticket.



---

archive/issue_comments_086509.json:
```json
{
    "body": "Getting bad news:\n\n```\ntar: This does not look like a tar archive\ntar: Skipping to next header\ntar: Archive contains obsolescent base-64 headers\n```\n",
    "created_at": "2011-03-23T15:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86509",
    "user": "https://github.com/kcrisman"
}
```

Getting bad news:

```
tar: This does not look like a tar archive
tar: Skipping to next header
tar: Archive contains obsolescent base-64 headers
```




---

archive/issue_comments_086510.json:
```json
{
    "body": "Did you use `./sage -pkg` to create this?  When I did, I got \n\n```\nCreating Sage package Jmol_for_SageNoteBook-1.1.5\n\nCreated package Jmol_for_SageNoteBook-1.1.5.spkg.\n\n    NAME: Jmol_for_SageNoteBook\n VERSION: 1.1.5\n    SIZE: 11.1M\n HG REPO: Error reading repository\nSPKG.txt: Good\n\nPlease test this package using\n```\n\n\nwhich is actually ok since I don't think you have an HG repo and this is a temporary package for testing.  Then success:\n\n```\nTemporary package directory: /Users/student/Desktop/sage-4.6.2/spkg/build/Jmol_for_SageNoteBook-1.1.5\nreplacing Jmol.js...\nJmol.js replaced.\nremoving Jmol*.jar and license files.\nrm: /Users/student/Desktop/sage-4.6.2/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory\ninstalling Jmol.jar and license files\u2026\nNew Jmol*.jar and license files installed.\n\nreal    0m1.051s\nuser    0m0.034s\nsys     0m0.320s\nSuccessfully installed Jmol_for_SageNoteBook-1.1.5\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing Jmol_for_SageNoteBook-1.1.5.spkg\n```\n\n\nThen applying the files is ok until\n\n```\napplying /Users/student/.sage/temp/Dasher_03.local/468/tmp_4.patch\nfile sagenb/data/jmol/appletweb/SageMenu.mnu already exists\n1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/jmol/appletweb/SageMenu.mnu.rej\n```\n\nProblematic is that then it's rejected?  I guess I'll see what happens... but this error will probably need to be fixed.",
    "created_at": "2011-03-23T15:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86510",
    "user": "https://github.com/kcrisman"
}
```

Did you use `./sage -pkg` to create this?  When I did, I got 

```
Creating Sage package Jmol_for_SageNoteBook-1.1.5

Created package Jmol_for_SageNoteBook-1.1.5.spkg.

    NAME: Jmol_for_SageNoteBook
 VERSION: 1.1.5
    SIZE: 11.1M
 HG REPO: Error reading repository
SPKG.txt: Good

Please test this package using
```


which is actually ok since I don't think you have an HG repo and this is a temporary package for testing.  Then success:

```
Temporary package directory: /Users/student/Desktop/sage-4.6.2/spkg/build/Jmol_for_SageNoteBook-1.1.5
replacing Jmol.js...
Jmol.js replaced.
removing Jmol*.jar and license files.
rm: /Users/student/Desktop/sage-4.6.2/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory
installing Jmol.jar and license files…
New Jmol*.jar and license files installed.

real    0m1.051s
user    0m0.034s
sys     0m0.320s
Successfully installed Jmol_for_SageNoteBook-1.1.5
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing Jmol_for_SageNoteBook-1.1.5.spkg
```


Then applying the files is ok until

```
applying /Users/student/.sage/temp/Dasher_03.local/468/tmp_4.patch
file sagenb/data/jmol/appletweb/SageMenu.mnu already exists
1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/jmol/appletweb/SageMenu.mnu.rej
```

Problematic is that then it's rejected?  I guess I'll see what happens... but this error will probably need to be fixed.



---

archive/issue_comments_086511.json:
```json
{
    "body": "Still zapped, probably because of the problem with the menu?\n\nBut then I tried it again, and it worked!  I don't get that.  \n\nI'll try the notebook next.  Okay, works, but I do not see the new stuff for the applet.  I guess that's okay, since that's the other ticket, right?\n\nIs there any way I can tell if the correct menu item is in there?  (Such as something to look for in the menu for the applet?)",
    "created_at": "2011-03-23T16:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86511",
    "user": "https://github.com/kcrisman"
}
```

Still zapped, probably because of the problem with the menu?

But then I tried it again, and it worked!  I don't get that.  

I'll try the notebook next.  Okay, works, but I do not see the new stuff for the applet.  I guess that's okay, since that's the other ticket, right?

Is there any way I can tell if the correct menu item is in there?  (Such as something to look for in the menu for the applet?)



---

archive/issue_comments_086512.json:
```json
{
    "body": "1. The correct menu is much shorter in the notebook than in the application launched from the command line.\u00a0 The application launched from the command line uses the default menu.\u00a0 I'll look into making them match.\n   1. Apply the patches in #9238 to see the updated notebook Jmol interface.\n   2. The .spkg problem is odd.\u00a0 I've got no errors ever.\u00a0 I just use ./sage -f \"<web address of patch>\".\n   3. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.\u00a0 For some reason the version I got for ubuntu 10.04 lts did not.",
    "created_at": "2011-03-23T17:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86512",
    "user": "https://github.com/gutow"
}
```

1. The correct menu is much shorter in the notebook than in the application launched from the command line.  The application launched from the command line uses the default menu.  I'll look into making them match.
   1. Apply the patches in #9238 to see the updated notebook Jmol interface.
   2. The .spkg problem is odd.  I've got no errors ever.  I just use ./sage -f "<web address of patch>".
   3. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.  For some reason the version I got for ubuntu 10.04 lts did not.



---

archive/issue_comments_086513.json:
```json
{
    "body": ">  1. The correct menu is much shorter in the notebook than in the application launched from the command line.\u00a0 The application launched from the command line uses the default menu.\u00a0 I'll look into making them match.\nWell, no need on this ticket!\n\nAs for this, the **first patch only** suffices to fix the command line problem, and the notebook still works right.  \n\nSo I would say that the second patch is *not* relevant to this ticket, esp. given its problems with import (which I am looking into - I think has to do with HG not applying some things correctly because of perceived line endings.  Look at the view of the attachment on this ticket, and look at the lines with `bond100` and `bond150` and note the weirdness there.  It looks like \n\n```\nbond100 | 0.10 \u221a\u00d6 = wireframe .1\n```\n\ninstead of angstroms like I think it's supposed to\n\n```\nbond100 | 0.10 \u00c5 = wireframe .1\n```\n\nNo wonder it's not applying, since it's not being interpreted right.  Anyway, not relevant for the ticket.\n\n>  1. Apply the patches in #9238 to see the updated notebook Jmol interface.\nAs I thought - thanks, not relevant for reviewing this.\n\n>  1. The .spkg problem is odd.\u00a0 I've got no errors ever.\u00a0 I just use ./sage -f \"<web address of patch>\".\nYes, that is what should work.  Since this isn't an spkg that would actually ever exist, it's not a problem, I hope.\n\n>  1. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.\u00a0 For some reason the version I got for ubuntu 10.04 lts did not.\nSee above.\n\nI get the following issue as well.\n\n```\nrm: /Users/.../sage-4.7.alpha2-jmol/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory\n```\n\nSo was there not a license before?  Apparently not - I can confirm that in an install that does not have the new Jmol.  So it's not a big deal, but at any rate you didn't have to put that in the script.\n\nOtherwise I think this is ready to go.  It would be nice to have someone on a system where command line plotting did *not* work before to try this.  Volker, du bist ja bei Sage Days 29, oder?  Probierst du es mal aus?",
    "created_at": "2011-03-23T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86513",
    "user": "https://github.com/kcrisman"
}
```

>  1. The correct menu is much shorter in the notebook than in the application launched from the command line.  The application launched from the command line uses the default menu.  I'll look into making them match.
Well, no need on this ticket!

As for this, the **first patch only** suffices to fix the command line problem, and the notebook still works right.  

So I would say that the second patch is *not* relevant to this ticket, esp. given its problems with import (which I am looking into - I think has to do with HG not applying some things correctly because of perceived line endings.  Look at the view of the attachment on this ticket, and look at the lines with `bond100` and `bond150` and note the weirdness there.  It looks like 

```
bond100 | 0.10 √Ö = wireframe .1
```

instead of angstroms like I think it's supposed to

```
bond100 | 0.10 Å = wireframe .1
```

No wonder it's not applying, since it's not being interpreted right.  Anyway, not relevant for the ticket.

>  1. Apply the patches in #9238 to see the updated notebook Jmol interface.
As I thought - thanks, not relevant for reviewing this.

>  1. The .spkg problem is odd.  I've got no errors ever.  I just use ./sage -f "<web address of patch>".
Yes, that is what should work.  Since this isn't an spkg that would actually ever exist, it's not a problem, I hope.

>  1. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.  For some reason the version I got for ubuntu 10.04 lts did not.
See above.

I get the following issue as well.

```
rm: /Users/.../sage-4.7.alpha2-jmol/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory
```

So was there not a license before?  Apparently not - I can confirm that in an install that does not have the new Jmol.  So it's not a big deal, but at any rate you didn't have to put that in the script.

Otherwise I think this is ready to go.  It would be nice to have someone on a system where command line plotting did *not* work before to try this.  Volker, du bist ja bei Sage Days 29, oder?  Probierst du es mal aus?



---

archive/issue_comments_086514.json:
```json
{
    "body": "Oh, and of course this can't actually be *merged* until a new SageNB package is produced.  I think I might be willing to do that once this and #9238 and one or two other things are ready; it would sure be worth it!",
    "created_at": "2011-03-23T19:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86514",
    "user": "https://github.com/kcrisman"
}
```

Oh, and of course this can't actually be *merged* until a new SageNB package is produced.  I think I might be willing to do that once this and #9238 and one or two other things are ready; it would sure be worth it!



---

archive/issue_comments_086515.json:
```json
{
    "body": "I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.",
    "created_at": "2011-03-25T18:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86515",
    "user": "https://github.com/vbraun"
}
```

I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.



---

archive/issue_comments_086516.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-25T18:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86516",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086517.json:
```json
{
    "body": "Replying to [comment:23 vbraun]:\n> I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.\nThanks for that feedback very much.  Ok, then I propose that that patch gets moved here, and then #10286 can be just about sage-native-execute.  Am I correct in assuming that *only* that patch from #10286 is needed to fix the behavior?",
    "created_at": "2011-03-25T18:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86517",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:23 vbraun]:
> I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.
Thanks for that feedback very much.  Ok, then I propose that that patch gets moved here, and then #10286 can be just about sage-native-execute.  Am I correct in assuming that *only* that patch from #10286 is needed to fix the behavior?



---

archive/issue_comments_086518.json:
```json
{
    "body": "Yes, it would be fine to move `trac_10286_call_jmol_correctly.patch` here. Only that one-liner is needed.",
    "created_at": "2011-03-25T18:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86518",
    "user": "https://github.com/vbraun"
}
```

Yes, it would be fine to move `trac_10286_call_jmol_correctly.patch` here. Only that one-liner is needed.



---

archive/issue_comments_086519.json:
```json
{
    "body": "Attachment [trac_9232_call_jmol_correctly.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_call_jmol_correctly.patch) by @kcrisman created at 2011-03-25 18:44:00\n\nApply this second.",
    "created_at": "2011-03-25T18:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86519",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9232_call_jmol_correctly.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232_call_jmol_correctly.patch) by @kcrisman created at 2011-03-25 18:44:00

Apply this second.



---

archive/issue_comments_086520.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-25T18:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86520",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086521.json:
```json
{
    "body": "Okay, this *should* be all okay then.",
    "created_at": "2011-03-25T18:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86521",
    "user": "https://github.com/kcrisman"
}
```

Okay, this *should* be all okay then.



---

archive/issue_comments_086522.json:
```json
{
    "body": "Things are a little bit of a mess because of the potential for flask changeover in SageNB.  What do people think of this?\n1. This ticket is used just for adding Volker's patch.  No sagenb change needed.\n2. Jonathan's patches for the menu, help, and surface lighting/spt files are moved to #9238.\n3. #9238 and all its attendant pieces become part of the flask notebook changeover, and henceforth the property of those doing that :)\nOtherwise this has the potential to just bitrot forever.",
    "created_at": "2011-03-29T00:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86522",
    "user": "https://github.com/kcrisman"
}
```

Things are a little bit of a mess because of the potential for flask changeover in SageNB.  What do people think of this?
1. This ticket is used just for adding Volker's patch.  No sagenb change needed.
2. Jonathan's patches for the menu, help, and surface lighting/spt files are moved to #9238.
3. #9238 and all its attendant pieces become part of the flask notebook changeover, and henceforth the property of those doing that :)
Otherwise this has the potential to just bitrot forever.



---

archive/issue_comments_086523.json:
```json
{
    "body": "The flask notebook has already split off of the current notebook.  So any patches that are applied to the current sage notebook will also need to be applied to the new notebook, probably in parallel.\n\nI'm already working on moving #9238 over to the new notebook.  It's just a matter of applying the patch to the new notebook, as far as I can tell.  (We'll find out better once we actually get jmol working with the new notebook!)",
    "created_at": "2011-03-29T01:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86523",
    "user": "https://github.com/jasongrout"
}
```

The flask notebook has already split off of the current notebook.  So any patches that are applied to the current sage notebook will also need to be applied to the new notebook, probably in parallel.

I'm already working on moving #9238 over to the new notebook.  It's just a matter of applying the patch to the new notebook, as far as I can tell.  (We'll find out better once we actually get jmol working with the new notebook!)



---

archive/issue_comments_086524.json:
```json
{
    "body": "Should I continue to put my patches into #9238? I've still got some fixes that should reduce memory problems making Safari somewhat more reliable and I may be able to get the advanced controls working in IE.",
    "created_at": "2011-03-29T02:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86524",
    "user": "https://github.com/gutow"
}
```

Should I continue to put my patches into #9238? I've still got some fixes that should reduce memory problems making Safari somewhat more reliable and I may be able to get the advanced controls working in IE.



---

archive/issue_comments_086525.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-29T13:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86525",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086526.json:
```json
{
    "body": "Jonathan, definitely keep working on #9238.  Jason can just put those things in the new notebook.  Having something working completely is a very good idea, and we can continue to test it on the old notebook, which is still the current notebook, after all.\n\nI do think we need to also add the piece of #9238 that changes the lighting.  Currently I have good lighting in the command line and bad lighting in the notebook, even without the new jmol - someone the new jmol is called from the notebook, even though I didn't install it in this version!!!  I even checked this in the advanced menu.  Mystifying. \n\nI'm just testing quick, and then I'll post patches.  Since they aren't mine, I feel free to give positive review.",
    "created_at": "2011-03-29T13:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86526",
    "user": "https://github.com/kcrisman"
}
```

Jonathan, definitely keep working on #9238.  Jason can just put those things in the new notebook.  Having something working completely is a very good idea, and we can continue to test it on the old notebook, which is still the current notebook, after all.

I do think we need to also add the piece of #9238 that changes the lighting.  Currently I have good lighting in the command line and bad lighting in the notebook, even without the new jmol - someone the new jmol is called from the notebook, even though I didn't install it in this version!!!  I even checked this in the advanced menu.  Mystifying. 

I'm just testing quick, and then I'll post patches.  Since they aren't mine, I feel free to give positive review.



---

archive/issue_comments_086527.json:
```json
{
    "body": "Attachment [trac_9232-lighting.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232-lighting.patch) by @kcrisman created at 2011-03-29 13:36:54",
    "created_at": "2011-03-29T13:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86527",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9232-lighting.patch](tarball://root/attachments/some-uuid/ticket9232/trac_9232-lighting.patch) by @kcrisman created at 2011-03-29 13:36:54



---

archive/issue_comments_086528.json:
```json
{
    "body": "Apply [attachment:trac_9232_call_jmol_correctly.patch] and [attachment:trac_9232-lighting.patch].",
    "created_at": "2011-03-29T13:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86528",
    "user": "https://github.com/kcrisman"
}
```

Apply [attachment:trac_9232_call_jmol_correctly.patch] and [attachment:trac_9232-lighting.patch].



---

archive/issue_comments_086529.json:
```json
{
    "body": "Just a ping to let the release manager know this is ready for alpha4.\n\n:-)",
    "created_at": "2011-04-06T12:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86529",
    "user": "https://github.com/kcrisman"
}
```

Just a ping to let the release manager know this is ready for alpha4.

:-)



---

archive/issue_comments_086530.json:
```json
{
    "body": "Please confirm that the `sagenb` does *not* need to be applied.",
    "created_at": "2011-04-07T08:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86530",
    "user": "https://github.com/jdemeyer"
}
```

Please confirm that the `sagenb` does *not* need to be applied.



---

archive/issue_comments_086531.json:
```json
{
    "body": "I meant to say more precisely: please confirm that the patch [attachment:trac_9232_notebook_fixes.patch] may be ignored.",
    "created_at": "2011-04-07T09:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86531",
    "user": "https://github.com/jdemeyer"
}
```

I meant to say more precisely: please confirm that the patch [attachment:trac_9232_notebook_fixes.patch] may be ignored.



---

archive/issue_comments_086532.json:
```json
{
    "body": "That is correct.  Only the two patches listed at the end of the description are necessary.  The other two have been incorporated into ticket #9238 because they are enhancements to how Jmol works.",
    "created_at": "2011-04-07T12:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86532",
    "user": "https://github.com/gutow"
}
```

That is correct.  Only the two patches listed at the end of the description are necessary.  The other two have been incorporated into ticket #9238 because they are enhancements to how Jmol works.



---

archive/issue_comments_086533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T13:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9232#issuecomment-86533",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
