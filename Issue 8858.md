# Issue 8858: 4.4.1 accessing internet during compilation

archive/issues_008858.json:
```json
{
    "body": "Assignee: jason, was\n\n\n```\n[sage-devel] 4.4.1 accessing internet during compilation \t\t\t\t\t\tInbox\t\tX\t\t\t\t\t\t \nReply to all\nHarald Schilly to sage-devel\nshow details 7:39 AM (20 minutes ago)\nHi, while watching the compilation of 4.4.1 I saw that it stopped\ncompiling and waited for a package to download. I'm curious if this is\nintended or just a strange glitch. At least my idea of a self\ncontaining source package is that it doesn't need to download software\nfrom the internet!\n\n...\ncreating 'dist/Sphinx-0.6.3-py2.6.egg' and adding 'build/bdist.linux-\ni686/egg' to it\nremoving 'build/bdist.linux-i686/egg' (and everything under it)\nProcessing Sphinx-0.6.3-py2.6.egg\ncreating /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/\nsite-packages/Sphinx-0.6.3-py2.6.egg\nExtracting Sphinx-0.6.3-py2.6.egg to /scratch/scratch/schilly/sage/\nsage-4.4.1/local/lib/python2.6/site-packages\nAdding Sphinx 0.6.3 to easy-install.pth file\nInstalling sphinx-build script to /scratch/scratch/schilly/sage/\nsage-4.4.1/local/bin\nInstalling sphinx-quickstart script to /scratch/scratch/schilly/sage/\nsage-4.4.1/local/bin\nInstalling sphinx-autogen script to /scratch/scratch/schilly/sage/\nsage-4.4.1/local/bin\n\nInstalled /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/\nsite-packages/Sphinx-0.6.3-py2.6.egg\nProcessing dependencies for Sphinx==0.6.3\nSearching for docutils==0.5\nBest match: docutils 0.5\nAdding docutils 0.5 to easy-install.pth file\n\nUsing /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/\nsite-packages\nSearching for Jinja2==2.3.1\nReading http://pypi.python.org/simple/Jinja2/\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\nDownload error: [Errno 110] Connection timed out -- Some packages may\nnot be found!\nReading http://jinja.pocoo.org/\n\nAnd well, it waits the usual 2 minutes socket timeout in each line and\nthe pocoo website is really down.\n\nH\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8858\n\n",
    "created_at": "2010-05-03T15:01:14Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "4.4.1 accessing internet during compilation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8858",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was


```
[sage-devel] 4.4.1 accessing internet during compilation 						Inbox		X						 
Reply to all
Harald Schilly to sage-devel
show details 7:39 AM (20 minutes ago)
Hi, while watching the compilation of 4.4.1 I saw that it stopped
compiling and waited for a package to download. I'm curious if this is
intended or just a strange glitch. At least my idea of a self
containing source package is that it doesn't need to download software
from the internet!

...
creating 'dist/Sphinx-0.6.3-py2.6.egg' and adding 'build/bdist.linux-
i686/egg' to it
removing 'build/bdist.linux-i686/egg' (and everything under it)
Processing Sphinx-0.6.3-py2.6.egg
creating /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages/Sphinx-0.6.3-py2.6.egg
Extracting Sphinx-0.6.3-py2.6.egg to /scratch/scratch/schilly/sage/
sage-4.4.1/local/lib/python2.6/site-packages
Adding Sphinx 0.6.3 to easy-install.pth file
Installing sphinx-build script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin
Installing sphinx-quickstart script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin
Installing sphinx-autogen script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin

Installed /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages/Sphinx-0.6.3-py2.6.egg
Processing dependencies for Sphinx==0.6.3
Searching for docutils==0.5
Best match: docutils 0.5
Adding docutils 0.5 to easy-install.pth file

Using /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages
Searching for Jinja2==2.3.1
Reading http://pypi.python.org/simple/Jinja2/
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/

And well, it waits the usual 2 minutes socket timeout in each line and
the pocoo website is really down.

H
```


Issue created by migration from https://trac.sagemath.org/ticket/8858





---

archive/issue_comments_081271.json:
```json
{
    "body": "I think that's not the notebook component, because it affects the sphinx package. john cremona had another problem with the notebook spkg. So, there are at least two issues like that and probably even more?",
    "created_at": "2010-05-03T15:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8858#issuecomment-81271",
    "user": "https://github.com/haraldschilly"
}
```

I think that's not the notebook component, because it affects the sphinx package. john cremona had another problem with the notebook spkg. So, there are at least two issues like that and probably even more?



---

archive/issue_comments_081272.json:
```json
{
    "body": "From Tim, who also points out that I was wrong:\n\n\n```\nThis isn't related to my new package includes. Jinja2 wasn't one of those new packages. \nThe problem is that SageNB is installed before Jinja2 is installed, so it's more of\na problem in the dependency script.\n```\n",
    "created_at": "2010-05-03T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8858#issuecomment-81272",
    "user": "https://github.com/williamstein"
}
```

From Tim, who also points out that I was wrong:


```
This isn't related to my new package includes. Jinja2 wasn't one of those new packages. 
The problem is that SageNB is installed before Jinja2 is installed, so it's more of
a problem in the dependency script.
```




---

archive/issue_comments_081273.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-05-05T11:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8858#issuecomment-81273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_events_009022.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-05-05T11:30:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8858#event-9022"
}
```



---

archive/issue_comments_081274.json:
```json
{
    "body": "Closing this as a duplicate of #8861.",
    "created_at": "2010-05-05T11:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8858#issuecomment-81274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as a duplicate of #8861.
