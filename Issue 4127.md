# Issue 4127: Python scripts to search for libraries that get wrongly called in

Issue created by migration from Trac.

Original creator: dphilp

Original creation time: 2008-09-15 05:42:06

Assignee: mabshoff

CC:  dphilp jason

The build process isn't very robust, and occasionally links to unintended libraries from e.g. /sw and /opt.  These scripts are good for detecting when and where that happens.  (OS X only)

First, construct a whitelist on a OS X-and-Sage vanilla installation.  (Run the script from SAGE_ROOT after sourcing sage-env.)

```/usr/bin/env python

# Run this script on a vanilla sage build on a clean OS X to figure out 
# what external libraries vanilla sage links to.  This forms a reference
# for figuring out build problems with non-vanilla configurations.
# dphilp 15/9/8

import os
import re

SAGE_ROOT=os.environ.get('SAGE_ROOT')

# We are building a list of known good external libraries
whitelist = []

# Find all binaries that could be pulling in external libraries
binary_list = os.popen('find . -name *.so -or -name *.dylib').readlines()

# For removing the trailing (compatiblity version .....) stuff
brace_pattern = re.compile('\(.*\)')
def trim_linked_file(x) :
  return re.sub(brace_pattern, '', x).strip()

# For identifying relative file paths, or absolute paths that refer to things
# inside SAGE_ROOT
nonlocal_file_pattern = re.compile('^(?!'+SAGE_ROOT+')/')

for file in binary_list :
  binary_name = file.strip()
  # Find what the binary links to
  linked_file_list = os.popen('otool -L ' + binary_name).readlines()
  # Strip whitespace, and ignore first result (it's the binary name)
  linked_file_list = [i.strip() for i in linked_file_list[1:]]
  for linked_file in linked_file_list :
    # Just get the file name
    linked_name = trim_linked_file(linked_file)
    # If it's not a local file, and not already known, give an error message
    if re.match(nonlocal_file_pattern, linked_name) and not(linked_name in whitelist):
      whitelist.append(linked_name)

whitelist.sort()
whitelist = [ i + '\n' for i in whitelist]
WHITELIST_FILE = open('tmp/linked_file_whitelist.txt', 'w')
WHITELIST_FILE.writelines(whitelist)
```


Second, copy the whitelist to the non-vanilla configuration.

Third, run this script from non-vanilla SAGE_ROOT:

```/usr/bin/env python

# Identify any external (non-sage) libraries that are linked by
# sage binaries, that are not on the 'known good' whitelist.
# dphilp 15/9/8

import os
import re

SAGE_ROOT=os.environ.get('SAGE_ROOT')

# List of non-local files we're allowed to link to
whitelist = open('tmp/linked_file_whitelist.txt').readlines()
whitelist = [i.strip() for i in whitelist]

# Find all binaries that could be pulling in naughty libraries
binary_list = os.popen('find . -name *.so -or -name *.dylib').readlines()

# For removing the trailing (compatiblity version .....) stuff
brace_pattern = re.compile('\(.*\)')
def trim_linked_file(x) :
  return re.sub(brace_pattern, '', x).strip()

# For identifying relative file paths, or absolute paths that refer to things
# inside SAGE_ROOT
nonlocal_file_pattern = re.compile('^(?!'+SAGE_ROOT+')/')

for file in binary_list :
  binary_name = file.strip()
  # Find what the binary links to
  linked_file_list = os.popen('otool -L ' + binary_name).readlines()
  # Strip whitespace, and ignore first result (it's the binary name)
  linked_file_list = [i.strip() for i in linked_file_list[1:]]
  for linked_file in linked_file_list :
    # Just get the file name
    linked_name = trim_linked_file(linked_file)
    # If it's not a local file, and not already known, give an error message
    if re.match(nonlocal_file_pattern, linked_name) and not(linked_name in whitelist):
      print binary_name + ' links to non-whitelisted file ' + linked_name
```




---

Comment by dphilp created at 2008-09-15 05:44:34

Sample output:

```
./local/lib/python2.5/site-packages/matplotlib/_image.so links to non-whitelisted file /opt/local/lib/libpng12.0.dylib
./local/lib/python2.5/site-packages/matplotlib/backends/_backend_agg.so links to non-whitelisted file /opt/local/lib/libpng12.0.dylib
./local/lib/python2.5/site-packages/matplotlib/backends/_tkagg.so links to non-whitelisted file /opt/local/lib/libpng12.0.dylib
```



---

Comment by mabshoff created at 2008-09-15 08:54:13

David,

*very* nice work. Can you name them sage-$FOO, add them to the repo in $SAGE_ROOT/local/bin and post a patch? One possibility would be to unifiy both scripts and depending on command line option either create a whitelist or alternatively look for "bad" extensions. Another one would be that if the whitelist does not exist it is created automatically in $SAGE_ROOT/tmp. Using the script should be idiot proof :)

Once we got this in and 3.1.2 is out we can start fixing the issues you are hitting. This will make debugging issues much, much easier.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-15 08:54:13

Changing priority from minor to blocker.


---

Comment by dphilp created at 2008-09-15 11:03:33

I didn't want to merge the two scripts because they are used at entirely different times and in entirely different ways.  The make-whitelist script would be run when making the sage source distribution, the check script run at diagnosis.

That means there is some second rate duplication of code, though.


---

Comment by dphilp created at 2008-09-16 21:41:20

Ok, I merged them.  The -w option creates a whitelist in data/extcode.  The -o file exports the 'whitelist' as it would be constructed on the current machine to 'file'.  And without any options, it runs in 'check against whitelist' mode.


---

Attachment


---

Comment by mabshoff created at 2008-09-20 00:50:23

Nice work. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 00:57:14

Merged in Sage 3.1.3.alpha0

In the future please post proper patches and not diffs, i.e. use hg export instead of hg diff.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 00:57:14

Resolution: fixed


---

Comment by jason created at 2010-10-13 01:07:19

I suppose we can use this script to see if the ban on macports is needed anymore.


---

Comment by kcrisman created at 2011-04-26 03:06:10

Replying to [comment:7 jason]:
> I suppose we can use this script to see if the ban on macports is needed anymore.

And Fink.    It would probably depend on what libraries were present.  Note that even now, we still seem to be linking against a lot of non-prereqs:

```
/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib
/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib
/System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
/System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
/System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
/System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
/System/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl
/System/Library/Frameworks/Tk.framework/Versions/8.5/Tk
/usr/lib/libSystem.B.dylib
/usr/lib/libcrypto.0.9.8.dylib
/usr/lib/libffi.dylib
/usr/lib/libiconv.2.dylib
/usr/lib/libicucore.A.dylib
/usr/lib/libncurses.5.4.dylib
/usr/lib/libobjc.A.dylib
/usr/lib/libpanel.5.4.dylib
/usr/lib/libssl.0.9.8.dylib
/usr/lib/libstdc++.6.dylib
/usr/local/lib/libgcc_s.1.dylib
/usr/local/lib/libgfortran.2.dylib
```

I thought at least some of these things were just part of Sage... well, anyway, this is a closed ticket :)
