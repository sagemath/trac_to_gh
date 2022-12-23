# Issue 9993: gcc 4.2.4 generates an internal compiler issue when buidling symmetrica on AIX 5.3

archive/issues_009993.json:
```json
{
    "body": "Assignee: tbd\n\nThis would not appear to be a Sage problem as such, but rather of gcc. \n == Hardware and software ==\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1 (which has singular-3-1-1-4.p2)\n\n == The problem ==\n\n```\ngcc -c -O1 -fPIC -g -DFAST -DALLTRUE zykelind.c\ngcc -c -O1 -fPIC -g -DFAST -DALLTRUE zyk.c\n: In function 'mult_hashtable_hashtable_faktor':\n:596: internal compiler error: Segmentation fault\nPlease submit a full bug report,\nwith preprocessed source if appropriate.\nSee <URL:http://gcc.gnu.org/bugs.html> for instructions.\nmake[2]: *** [tmh.o] Error 1\nmake[2]: Target `test' not remade because of errors.\nmake[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/symmetrica-2.0.p5/src'\nError building symmetrica.\n\nreal    37m5.981s\nuser    87m12.220s\nsys     0m31.967s\nsage: An error occurred while installing symmetrica-2.0.p5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9994\n\n",
    "created_at": "2010-09-24T00:45:18Z",
    "labels": [
        "PLEASE CHANGE",
        "major",
        "bug"
    ],
    "title": "gcc 4.2.4 generates an internal compiler issue when buidling symmetrica on AIX 5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9993",
    "user": "drkirkby"
}
```
Assignee: tbd

This would not appear to be a Sage problem as such, but rather of gcc. 
 == Hardware and software ==
* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1 (which has singular-3-1-1-4.p2)

 == The problem ==

```
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE zykelind.c
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE zyk.c
: In function 'mult_hashtable_hashtable_faktor':
:596: internal compiler error: Segmentation fault
Please submit a full bug report,
with preprocessed source if appropriate.
See <URL:http://gcc.gnu.org/bugs.html> for instructions.
make[2]: *** [tmh.o] Error 1
make[2]: Target `test' not remade because of errors.
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/symmetrica-2.0.p5/src'
Error building symmetrica.

real    37m5.981s
user    87m12.220s
sys     0m31.967s
sage: An error occurred while installing symmetrica-2.0.p5
```


Issue created by migration from https://trac.sagemath.org/ticket/9994





---

archive/issue_comments_100420.json:
```json
{
    "body": "Changing component from PLEASE CHANGE to AIX or HP-UX ports.",
    "created_at": "2010-09-24T00:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100420",
    "user": "drkirkby"
}
```

Changing component from PLEASE CHANGE to AIX or HP-UX ports.



---

archive/issue_comments_100421.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-09-24T00:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100421",
    "user": "drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_100422.json:
```json
{
    "body": "Does anyone still care?",
    "created_at": "2015-04-13T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100422",
    "user": "mmezzarobba"
}
```

Does anyone still care?



---

archive/issue_comments_100423.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2015-04-13T13:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100423",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_100424.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-06-27T11:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100424",
    "user": "aapitzsch"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_100425.json:
```json
{
    "body": "Replying to [comment:2 mmezzarobba]:\n> Does anyone still care?\n\nNo.",
    "created_at": "2015-06-27T11:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100425",
    "user": "aapitzsch"
}
```

Replying to [comment:2 mmezzarobba]:
> Does anyone still care?

No.



---

archive/issue_comments_100426.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-07-17T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9993#issuecomment-100426",
    "user": "vbraun"
}
```

Resolution: wontfix
