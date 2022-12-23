# Issue 9519: scipy does not exit if there are build failures, but spkg-install looks OK

archive/issues_009519.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  leif mpatel mvngu jhpalmieri dimpase\n\nBuilding Sage 4.5 on a Sun Blade 2000, with dual UltraSPARC III+ processors in 64-bit mode, the build process produces some obvious **error** messages. These are not warnings, but errors. \n\n\n```\ngcc _configtest.o -L/export/home/drkirkby/64/sage-4.5/local/lib -lf77blas -lcblas -latlas -o _configtest\nld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64\nld: fatal: File processing errors. No output written to _configtest\ncollect2: ld returned 1 exit status\nld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64\nld: fatal: File processing errors. No output written to _configtest\ncollect2: ld returned 1 exit status\nfailure.\nremoving: _configtest.c _configtest.o\nStatus: 255\nOutput:\n```\n\n\n`wrong ELF class:` messages mean an attempt what made to link a mixture of 32-bit and 64-bit object files. \n\nBut the build process still goes on to report that scipy has installed OK. \n\n\n```\nreal    22m34.927s\nuser    20m23.356s\nsys     1m5.603s\nSuccessfully installed scipy-0.7.p5\n```\n\n\nWhat is odd, is that `spkg-install` looks to be OK to me. \n\n\n```\npython setup.py build\nif [ $? -ne 0 ]; then\n    echo \"Error building scipy.\"\n    exit 1\nfi\n\n# Intall\npython setup.py install\nif [ $? -ne 0 ]; then\n    echo \"Error installing scipy.\"\n    exit 1\nfi\n```\n\n\nThe problem is **not** like the cephes package, or several others, where the return code of *make* is not checked.  \n\nAt this point, I've not no idea if this is an upstream bug, or a Sage bug. \n\nAnyone got any ideas? \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9519\n\n",
    "created_at": "2010-07-16T22:43:58Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "scipy does not exit if there are build failures, but spkg-install looks OK",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9519",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  leif mpatel mvngu jhpalmieri dimpase

Building Sage 4.5 on a Sun Blade 2000, with dual UltraSPARC III+ processors in 64-bit mode, the build process produces some obvious **error** messages. These are not warnings, but errors. 


```
gcc _configtest.o -L/export/home/drkirkby/64/sage-4.5/local/lib -lf77blas -lcblas -latlas -o _configtest
ld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64
ld: fatal: File processing errors. No output written to _configtest
collect2: ld returned 1 exit status
ld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64
ld: fatal: File processing errors. No output written to _configtest
collect2: ld returned 1 exit status
failure.
removing: _configtest.c _configtest.o
Status: 255
Output:
```


`wrong ELF class:` messages mean an attempt what made to link a mixture of 32-bit and 64-bit object files. 

But the build process still goes on to report that scipy has installed OK. 


```
real    22m34.927s
user    20m23.356s
sys     1m5.603s
Successfully installed scipy-0.7.p5
```


What is odd, is that `spkg-install` looks to be OK to me. 


```
python setup.py build
if [ $? -ne 0 ]; then
    echo "Error building scipy."
    exit 1
fi

# Intall
python setup.py install
if [ $? -ne 0 ]; then
    echo "Error installing scipy."
    exit 1
fi
```


The problem is **not** like the cephes package, or several others, where the return code of *make* is not checked.  

At this point, I've not no idea if this is an upstream bug, or a Sage bug. 

Anyone got any ideas? 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9519





---

archive/issue_comments_091510.json:
```json
{
    "body": "Could you give a link to the full log for scipy?",
    "created_at": "2010-07-17T00:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91510",
    "user": "mpatel"
}
```

Could you give a link to the full log for scipy?



---

archive/issue_comments_091511.json:
```json
{
    "body": "Well, `_configtest` sounds rather harmless...\n\nAre you sure the finally produced(?) scipy is really broken?",
    "created_at": "2010-07-17T00:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91511",
    "user": "leif"
}
```

Well, `_configtest` sounds rather harmless...

Are you sure the finally produced(?) scipy is really broken?



---

archive/issue_comments_091512.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Could you give a link to the full log for scipy?\nSure. Will attach to the ticket. Since its fairly large, I have compressed it. \n\nI think there is a problem with the build of ATLAS, as that shows a `wrong ELF class:` message. Since scipy links to ATLAS, that is probably the problem. But I don't think that is an excuse for the scipy build to continue, though Leif thinks it's harmless. \n\nDave",
    "created_at": "2010-07-17T00:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91512",
    "user": "drkirkby"
}
```

Replying to [comment:2 mpatel]:
> Could you give a link to the full log for scipy?
Sure. Will attach to the ticket. Since its fairly large, I have compressed it. 

I think there is a problem with the build of ATLAS, as that shows a `wrong ELF class:` message. Since scipy links to ATLAS, that is probably the problem. But I don't think that is an excuse for the scipy build to continue, though Leif thinks it's harmless. 

Dave



---

archive/issue_comments_091513.json:
```json
{
    "body": "Attachment\n\nCompressed version of sage-4.5/spkg/logs/scipy-0.7.p5.log",
    "created_at": "2010-07-17T00:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91513",
    "user": "drkirkby"
}
```

Attachment

Compressed version of sage-4.5/spkg/logs/scipy-0.7.p5.log



---

archive/issue_comments_091514.json:
```json
{
    "body": "If enough parts of Sage run, you could try running the test suite, e.g.,\n\n```sh\n$ ./sage -sh\nsage subshell$ easy_install nose\nsage subshell$ exit\n$ ./sage -python -c \"import scipy; scipy.test()\"\n```\n\n[Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.\n\nI suppose we could optionally (if the user/developer desires) install nose automatically.",
    "created_at": "2010-07-17T00:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91514",
    "user": "mpatel"
}
```

If enough parts of Sage run, you could try running the test suite, e.g.,

```sh
$ ./sage -sh
sage subshell$ easy_install nose
sage subshell$ exit
$ ./sage -python -c "import scipy; scipy.test()"
```

[Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.

I suppose we could optionally (if the user/developer desires) install nose automatically.



---

archive/issue_comments_091515.json:
```json
{
    "body": "Replying to [comment:3 leif]:\n> Well, `_configtest` sounds rather harmless...\n> \n> Are you sure the finally produced(?) scipy is really broken?\n\nI'm not certain. I thought ATLAS was broken, but I think I have remade the broken library. How can I test just scipy? The 64-bit SPARC port is not 100% ok. I can't run the doctests, as it segfaults, but Sage does semi-work. I can do computations with it. So `sage -t foobar` might work\n\nDave",
    "created_at": "2010-07-17T00:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91515",
    "user": "drkirkby"
}
```

Replying to [comment:3 leif]:
> Well, `_configtest` sounds rather harmless...
> 
> Are you sure the finally produced(?) scipy is really broken?

I'm not certain. I thought ATLAS was broken, but I think I have remade the broken library. How can I test just scipy? The 64-bit SPARC port is not 100% ok. I can't run the doctests, as it segfaults, but Sage does semi-work. I can do computations with it. So `sage -t foobar` might work

Dave



---

archive/issue_comments_091516.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> If enough parts of Sage run, you could try running the test suite, e.g.,\n> {{{\n> #!sh\n> $ ./sage -sh\n> sage subshell$ easy_install nose\n> sage subshell$ exit\n> $ ./sage -python -c \"import scipy; scipy.test()\"\n> }}}\n> [Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.\n> \n> I suppose we could optionally (if the user/developer desires) install nose automatically.\n\nI've never come across 'nose' - my python skills are next to zero. I will attach a log. As you can see, it finally fails with a core dump, but perhaps has some useful information before it dumps core.\n\nBTW, I've removed the static atlas libs, leaving only the shared ones. That might be a cause of a problem. I can't understand the need for both. If yyou look in the ATLAS package, you can see about 3 dynamic libraries will be missing. Two are not built, and one is deleted. I built them all and deleted no dynamic ones - only the static. \n\n\nDave",
    "created_at": "2010-07-17T00:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91516",
    "user": "drkirkby"
}
```

Replying to [comment:5 mpatel]:
> If enough parts of Sage run, you could try running the test suite, e.g.,
> {{{
> #!sh
> $ ./sage -sh
> sage subshell$ easy_install nose
> sage subshell$ exit
> $ ./sage -python -c "import scipy; scipy.test()"
> }}}
> [Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.
> 
> I suppose we could optionally (if the user/developer desires) install nose automatically.

I've never come across 'nose' - my python skills are next to zero. I will attach a log. As you can see, it finally fails with a core dump, but perhaps has some useful information before it dumps core.

BTW, I've removed the static atlas libs, leaving only the shared ones. That might be a cause of a problem. I can't understand the need for both. If yyou look in the ATLAS package, you can see about 3 dynamic libraries will be missing. Two are not built, and one is deleted. I built them all and deleted no dynamic ones - only the static. 


Dave



---

archive/issue_comments_091517.json:
```json
{
    "body": "Attachment\n\nOutput from: ./sage -python -c \"import scipy; scipy.test()\" > scipy.test.log  2>&1",
    "created_at": "2010-07-17T00:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91517",
    "user": "drkirkby"
}
```

Attachment

Output from: ./sage -python -c "import scipy; scipy.test()" > scipy.test.log  2>&1



---

archive/issue_comments_091518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-30T20:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91518",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091519.json:
```json
{
    "body": "outdated, should be closed",
    "created_at": "2020-08-30T20:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91519",
    "user": "mkoeppe"
}
```

outdated, should be closed



---

archive/issue_comments_091520.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-30T21:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91520",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091521.json:
```json
{
    "body": "ok",
    "created_at": "2020-08-30T21:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91521",
    "user": "dimpase"
}
```

ok



---

archive/issue_comments_091522.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-21T16:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9519#issuecomment-91522",
    "user": "chapoton"
}
```

Resolution: invalid
