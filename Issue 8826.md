# Issue 8826: [build error] ImportError: No module named sage.all

archive/issues_008826.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nI'm using gcc 4.5 but I'm not sure if this is related. I am on 64bit archlinux. If you need any more info, I'll be happy to provide it.\n\n!`spkg/base/.hg/store/data/bzip2-1.0.5-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/bzip2-1.0.5-install.i'\n\n!`spkg/base/.hg/store/data/_r_e_a_d_m_e.txt.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/_r_e_a_d_m_e.txt.i'\n!`spkg/base/.hg/store/data/testcxx.sh.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/testcxx.sh.i'\n!`spkg/base/.hg/store/data/prereq-0.3-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.3-install.i'\n!`spkg/base/.hg/store/data/stdint.h___solaris9.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/stdint.h!___solaris9.i'\n!`spkg/base/.hg/store/data/prereq-0.7-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.7-install.i'\n!`spkg/base/.hg/store/data/.hgignore.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/.hgignore.i'\n!`spkg/base/.hg/store/data/testcc.sh.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/testcc.sh.i'\n!`spkg/base/.hg/store/data/prereq-0.6-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.6-install.i'\n!`spkg/base/.hg/store/00changelog.i' -> `/opt/sage/sage/spkg/base/.hg/store/00changelog.i'\n!`spkg/base/.hg/store/undo' -> `/opt/sage/sage/spkg/base/.hg/store/undo'\n!`spkg/base/.hg/attic' -> `/opt/sage/sage/spkg/base/.hg/attic'\n!`spkg/base/.hg/requires' -> `/opt/sage/sage/spkg/base/.hg/requires'\n!`spkg/base/.hg/branch' -> `/opt/sage/sage/spkg/base/.hg/branch'\n!`spkg/base/sage-make_relative' -> `/opt/sage/sage/spkg/base/sage-make_relative'\n!`spkg/base/bzip2-1.0.5.tar.gz' -> `/opt/sage/sage/spkg/base/bzip2-1.0.5.tar.gz'\n!`spkg/base/.hgignore' -> `/opt/sage/sage/spkg/base/.hgignore'\n!`spkg/base/README.txt' -> `/opt/sage/sage/spkg/base/README.txt'\n!`spkg/base/testcxx.sh' -> `/opt/sage/sage/spkg/base/testcxx.sh'\n!`spkg/base/sage-spkg' -> `/opt/sage/sage/spkg/base/sage-spkg'\n!`spkg/base/testcc.sh' -> `/opt/sage/sage/spkg/base/testcc.sh'\n!`spkg/base/bzip2-1.0.5-install' -> `/opt/sage/sage/spkg/base/bzip2-1.0.5-install'\n!`spkg/base/prereq-0.7-install' -> `/opt/sage/sage/spkg/base/prereq-0.7-install'\n!`tmp' -> `/opt/sage/sage/tmp'\n!`tmp/COPYING.txt' -> `/opt/sage/sage/tmp/COPYING.txt'\n!`tmp/README.txt' -> `/opt/sage/sage/tmp/README.txt'\n!`tmp/sage-README-osx.txt' -> `/opt/sage/sage/tmp/sage-README-osx.txt'\n!`tmp/install' -> `/opt/sage/sage/tmp/install'\npython local/bin/sage-hardcode_sage_root /opt/sage/sage/sage \"/opt/sage\"/sage\ncp /opt/sage/sage/sage /opt/sage/bin/\ncd /opt/sage/bin/; ./sage -c\nTraceback (most recent call last):\n\u00a0 File \"/opt/sage/sage/local/bin/sage-eval\", line 4, in <module>\n\u00a0\u00a0\u00a0 from sage.all import *\nImportError: No module named sage.all\n\nmake: *** [install] Error 1\nerror: command failed to execute correctly\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8826\n\n",
    "created_at": "2010-04-29T20:38:19Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[build error] ImportError: No module named sage.all",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8826",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```
Assignee: GeorgSWeber

I'm using gcc 4.5 but I'm not sure if this is related. I am on 64bit archlinux. If you need any more info, I'll be happy to provide it.

!`spkg/base/.hg/store/data/bzip2-1.0.5-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/bzip2-1.0.5-install.i'

!`spkg/base/.hg/store/data/_r_e_a_d_m_e.txt.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/_r_e_a_d_m_e.txt.i'
!`spkg/base/.hg/store/data/testcxx.sh.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/testcxx.sh.i'
!`spkg/base/.hg/store/data/prereq-0.3-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.3-install.i'
!`spkg/base/.hg/store/data/stdint.h___solaris9.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/stdint.h!___solaris9.i'
!`spkg/base/.hg/store/data/prereq-0.7-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.7-install.i'
!`spkg/base/.hg/store/data/.hgignore.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/.hgignore.i'
!`spkg/base/.hg/store/data/testcc.sh.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/testcc.sh.i'
!`spkg/base/.hg/store/data/prereq-0.6-install.i' -> `/opt/sage/sage/spkg/base/.hg/store/data/prereq-0.6-install.i'
!`spkg/base/.hg/store/00changelog.i' -> `/opt/sage/sage/spkg/base/.hg/store/00changelog.i'
!`spkg/base/.hg/store/undo' -> `/opt/sage/sage/spkg/base/.hg/store/undo'
!`spkg/base/.hg/attic' -> `/opt/sage/sage/spkg/base/.hg/attic'
!`spkg/base/.hg/requires' -> `/opt/sage/sage/spkg/base/.hg/requires'
!`spkg/base/.hg/branch' -> `/opt/sage/sage/spkg/base/.hg/branch'
!`spkg/base/sage-make_relative' -> `/opt/sage/sage/spkg/base/sage-make_relative'
!`spkg/base/bzip2-1.0.5.tar.gz' -> `/opt/sage/sage/spkg/base/bzip2-1.0.5.tar.gz'
!`spkg/base/.hgignore' -> `/opt/sage/sage/spkg/base/.hgignore'
!`spkg/base/README.txt' -> `/opt/sage/sage/spkg/base/README.txt'
!`spkg/base/testcxx.sh' -> `/opt/sage/sage/spkg/base/testcxx.sh'
!`spkg/base/sage-spkg' -> `/opt/sage/sage/spkg/base/sage-spkg'
!`spkg/base/testcc.sh' -> `/opt/sage/sage/spkg/base/testcc.sh'
!`spkg/base/bzip2-1.0.5-install' -> `/opt/sage/sage/spkg/base/bzip2-1.0.5-install'
!`spkg/base/prereq-0.7-install' -> `/opt/sage/sage/spkg/base/prereq-0.7-install'
!`tmp' -> `/opt/sage/sage/tmp'
!`tmp/COPYING.txt' -> `/opt/sage/sage/tmp/COPYING.txt'
!`tmp/README.txt' -> `/opt/sage/sage/tmp/README.txt'
!`tmp/sage-README-osx.txt' -> `/opt/sage/sage/tmp/sage-README-osx.txt'
!`tmp/install' -> `/opt/sage/sage/tmp/install'
python local/bin/sage-hardcode_sage_root /opt/sage/sage/sage "/opt/sage"/sage
cp /opt/sage/sage/sage /opt/sage/bin/
cd /opt/sage/bin/; ./sage -c
Traceback (most recent call last):
  File "/opt/sage/sage/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
ImportError: No module named sage.all

make: *** [install] Error 1
error: command failed to execute correctly


Issue created by migration from https://trac.sagemath.org/ticket/8826





---

archive/issue_events_008989.json:
```json
{
    "actor": "gostrc",
    "created_at": "2010-05-04T01:36:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8826#event-8989"
}
```



---

archive/issue_comments_080917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T01:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80917",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

Resolution: fixed



---

archive/issue_comments_080918.json:
```json
{
    "body": "Fixed in 4.4.1",
    "created_at": "2010-05-04T01:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80918",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

Fixed in 4.4.1



---

archive/issue_comments_080919.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-05-18T03:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80919",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_080920.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-05-18T03:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80920",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

Changing status from closed to new.



---

archive/issue_events_008990.json:
```json
{
    "actor": "gostrc",
    "created_at": "2010-05-18T03:14:16Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8826#event-8990"
}
```



---

archive/issue_events_008991.json:
```json
{
    "actor": "gostrc",
    "created_at": "2010-06-06T20:16:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8826#event-8991"
}
```



---

archive/issue_comments_080921.json:
```json
{
    "body": "had to unset LDFLAGS MAKEFLAGS CFLAGS CXXFLAGS",
    "created_at": "2010-06-06T20:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80921",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

had to unset LDFLAGS MAKEFLAGS CFLAGS CXXFLAGS



---

archive/issue_comments_080922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T20:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80922",
    "user": "https://trac.sagemath.org/admin/accounts/users/gostrc"
}
```

Resolution: fixed



---

archive/issue_comments_080923.json:
```json
{
    "body": "Resolution changed from fixed to invalid",
    "created_at": "2010-06-07T17:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8826#issuecomment-80923",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to invalid
