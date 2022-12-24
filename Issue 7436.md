# Issue 7436: frobby optional spkg doesn't build on a lot of machines

archive/issues_007436.json:
```json
{
    "body": "Assignee: tbd\n\nOn many Linux boxes, building the frobby-0.7.6 spkg fails as follows:\n\n\n```\ngcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu8) \n****************************************************\nmkdir -p bin/release/ \ng++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /tmp/wstein/farm/sage-4.2.1.alpha0/loc\nal/include -O3 -c src/main.cpp -o bin/release/main.o\nsrc/main.cpp: In function \u2018int main(int, const char**)\u2019:\nsrc/main.cpp:30: error: \u2018srand\u2019 was not declared in this scope\nmake: *** [bin/release/main.o] Error 1\nError building Frobby.\n\nreal    0m2.271s\nuser    0m0.320s\nsys     0m0.410s\nsage: An error occurred while installing frobby-0.7.6\n```\n\n\nI ran the command \"sage -i frobby-0.7.6\" on the build farm and it fails on:\n\n* debian32/64\n* fedora32/64\n* mandriva32/64\n* opensuse32/64\n* ubuntu32/64\n\nIt works on centos (=REDHAT).    It works on sage.math.   Basically it works with gcc <= 4.2 and fails with newer GCC's. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7436\n\n",
    "created_at": "2009-11-12T04:35:18Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "frobby optional spkg doesn't build on a lot of machines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7436",
    "user": "@williamstein"
}
```
Assignee: tbd

On many Linux boxes, building the frobby-0.7.6 spkg fails as follows:


```
gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu8) 
****************************************************
mkdir -p bin/release/ 
g++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /tmp/wstein/farm/sage-4.2.1.alpha0/loc
al/include -O3 -c src/main.cpp -o bin/release/main.o
src/main.cpp: In function ‘int main(int, const char**)’:
src/main.cpp:30: error: ‘srand’ was not declared in this scope
make: *** [bin/release/main.o] Error 1
Error building Frobby.

real    0m2.271s
user    0m0.320s
sys     0m0.410s
sage: An error occurred while installing frobby-0.7.6
```


I ran the command "sage -i frobby-0.7.6" on the build farm and it fails on:

* debian32/64
* fedora32/64
* mandriva32/64
* opensuse32/64
* ubuntu32/64

It works on centos (=REDHAT).    It works on sage.math.   Basically it works with gcc <= 4.2 and fails with newer GCC's. 

Issue created by migration from https://trac.sagemath.org/ticket/7436





---

archive/issue_comments_062575.json:
```json
{
    "body": "I get the same problem on Solaris, with gcc 4.4.2\n\ndave",
    "created_at": "2009-11-12T04:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62575",
    "user": "drkirkby"
}
```

I get the same problem on Solaris, with gcc 4.4.2

dave



---

archive/issue_comments_062576.json:
```json
{
    "body": "Also fail on Solaris 10 (SPARC) with gcc 4.4.2",
    "created_at": "2009-11-12T21:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62576",
    "user": "drkirkby"
}
```

Also fail on Solaris 10 (SPARC) with gcc 4.4.2



---

archive/issue_comments_062577.json:
```json
{
    "body": "Oops, I appear to have put the same comment twice!",
    "created_at": "2009-11-12T21:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62577",
    "user": "drkirkby"
}
```

Oops, I appear to have put the same comment twice!



---

archive/issue_comments_062578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T01:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62578",
    "user": "@benjaminfjones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062579.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T01:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62579",
    "user": "@benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062580.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-05-26T01:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62580",
    "user": "@jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_062581.json:
```json
{
    "body": "As a matter of interest, what was the reason for not fixing it? I thought optional packages were supposed to build on all supported machines. So the only logical things to me were to either \n\n1) Fix it \n2) Make it experimental and not optional. \n\nIt this bug report a duplicate, as the resolution is set to? \n\nI appreciate the fact this has remained like this for 3 years probably means nobody cares too much, but the concept of closing a ticket without fixing an issue seems wrong to me. \n\nDave",
    "created_at": "2012-05-26T21:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62581",
    "user": "drkirkby"
}
```

As a matter of interest, what was the reason for not fixing it? I thought optional packages were supposed to build on all supported machines. So the only logical things to me were to either 

1) Fix it 
2) Make it experimental and not optional. 

It this bug report a duplicate, as the resolution is set to? 

I appreciate the fact this has remained like this for 3 years probably means nobody cares too much, but the concept of closing a ticket without fixing an issue seems wrong to me. 

Dave



---

archive/issue_comments_062582.json:
```json
{
    "body": "This was closed because #13007 does fix the problem on the platforms in the ticket description. I did not test the new spkg there on solaris though.",
    "created_at": "2012-05-27T00:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7436#issuecomment-62582",
    "user": "@benjaminfjones"
}
```

This was closed because #13007 does fix the problem on the platforms in the ticket description. I did not test the new spkg there on solaris though.
