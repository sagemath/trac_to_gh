# Issue 3060: biopython optional package update (to 1.45)

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-04-30 01:31:59

Assignee: somebody

Keywords: biopython, biology, packages

On March 22, 2008, the biopython devs released version 1.45.  I have put an updated sage package at:
http://www.d.umn.edu/~mhampton/biopython-1.45.spkg



---

Comment by mabshoff created at 2008-05-02 13:47:23

Ok, there are a couple issues. For one:

```
running install_data
running install_egg_info
Removing /scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/site-packages/egenix_mx_base-2.0.6-py2.5.egg-info
Writing /scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/site-packages/egenix_mx_base-2.0.6-py2.5.egg-info
running install
Traceback (most recent call last):
  File "setup.py", line 545, in <module>
    data_files=DATA_FILES,
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/distutils/core.py", line 151, in setup
    dist.run_commands()
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/distutils/dist.py", line 974, in run_commands
    self.run_command(cmd)
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/distutils/dist.py", line 994, in run_command
    cmd_obj.run()
  File "setup.py", line 147, in run
    if check_dependencies_once():
  File "setup.py", line 65, in check_dependencies_once
    _CHECKED = check_dependencies()
  File "setup.py", line 89, in check_dependencies
    if is_installed_fn():
  File "setup.py", line 320, in is_mxTextTools_installed
    return can_import("mx.TextTools")
  File "setup.py", line 275, in can_import
    return __import__(module_name)
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/site-packages/mx/TextTools/__init__.py", line 8, in <module>
    from TextTools import *
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/site-packages/mx/TextTools/TextTools.py", line 13, in <module>
    from mxTextTools import *
  File "/scratch/mabshoff/release-cycle/sage-3.0.1.alpha1/local/lib/python2.5/site-packages/mx/TextTools/mxTextTools/__init__.py", line 12, in <module>
    BMS = TextSearch
NameError: name 'TextSearch' is not defined
Error install biopython

real    0m10.058s
user    0m8.569s
sys     0m1.252s
```

There is also a bunch of OSX indexing crap in the spkg. I fixed those, added an hg repo, checked in everything, added proper "exit 1" in two places in case the install failed. What seems to cause the above failure in an installed biopython-1.44. Fixing this requires nuking 

```
rm -rf mx/ Bio Martel/ BioSQL/ biopython-1.44-py2.5.egg-info  egenix_mx_base-* 
```

in $SAGE_LOCAL/lib/python2.5/site-packages/ - I am fixing this in the spkg-install and will take half the credit for this spkg since I am a mean, mean guy ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 14:03:36

Ok, all is fixed in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/rc0/biopython-1.45.spkg

Positive review and uploading it to the official repo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 14:04:40

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 14:04:40

Merged into the optional package repo in Sage 3.0.1.rc0.
