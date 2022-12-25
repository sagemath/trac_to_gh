# Issue 7019: update biopython optional package to 1.52

archive/issues_007019.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  tkeller\n\nKeywords: biopython\n\nUpdating to biopython-1.52, which was released September 22, 2009.  Main improvements were to alignment and sequence file conversion, population genetics statistics, and the Bio.SeqIO.indexed_dict() for handling large numbers of sequences.\n\nHere is an example that will not work with previous biopython packages:\n\n```\nsage: import urllib2 as U\nsage: f = U.urlopen('http://biopython.org/DIST/docs/tutorial/examples/ls_orchid.gbk')\nsage: orchidfile = file(DATA+\"ls_orchid.gbk\",'w')\nsage: orchidfile.write(f.read())\nsage: orchidfile.close()\nsage: f.close()\nsage: from Bio import SeqIO\nsage: orchid_dict = SeqIO.index(DATA+\"ls_orchid.gbk\", \"genbank\")\nsage: print 'Number of records: ' + str(len(orchid_dict))\nsage: orchid_dict.keys()\nsage: seq_record = orchid_dict[\"Z78475.1\"]\nsage: print 'Description: ' + seq_record.description\nsage: seq_record.seq\n\nNumber of records: 94\nDescription: P.supardii 5.8S rRNA gene and ITS1 and ITS2 DNA.\nSeq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGATCACAT...GGT', IUPACAmbiguousDNA())\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7019\n\n",
    "created_at": "2009-09-26T14:40:37Z",
    "labels": [
        "component: packages: optional",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "update biopython optional package to 1.52",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: tbd

CC:  tkeller

Keywords: biopython

Updating to biopython-1.52, which was released September 22, 2009.  Main improvements were to alignment and sequence file conversion, population genetics statistics, and the Bio.SeqIO.indexed_dict() for handling large numbers of sequences.

Here is an example that will not work with previous biopython packages:

```
sage: import urllib2 as U
sage: f = U.urlopen('http://biopython.org/DIST/docs/tutorial/examples/ls_orchid.gbk')
sage: orchidfile = file(DATA+"ls_orchid.gbk",'w')
sage: orchidfile.write(f.read())
sage: orchidfile.close()
sage: f.close()
sage: from Bio import SeqIO
sage: orchid_dict = SeqIO.index(DATA+"ls_orchid.gbk", "genbank")
sage: print 'Number of records: ' + str(len(orchid_dict))
sage: orchid_dict.keys()
sage: seq_record = orchid_dict["Z78475.1"]
sage: print 'Description: ' + seq_record.description
sage: seq_record.seq

Number of records: 94
Description: P.supardii 5.8S rRNA gene and ITS1 and ITS2 DNA.
Seq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGATCACAT...GGT', IUPACAmbiguousDNA())
```


Issue created by migration from https://trac.sagemath.org/ticket/7019





---

archive/issue_comments_057996.json:
```json
{
    "body": "Changing assignee from tbd to mhampton.",
    "created_at": "2009-09-26T14:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-57996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from tbd to mhampton.



---

archive/issue_comments_057997.json:
```json
{
    "body": "Where is the spkg? ~ Adam",
    "created_at": "2009-10-06T08:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-57997",
    "user": "https://github.com/maxthemouse"
}
```

Where is the spkg? ~ Adam



---

archive/issue_comments_057998.json:
```json
{
    "body": "Oops!  Sorry about that.  I put a copy here:\n\nhttp://sage.math.washington.edu/home/mhampton/biopython-1.52.spkg\n\nThanks very much for taking a look!\n\nMarshall",
    "created_at": "2009-10-06T21:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-57998",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Oops!  Sorry about that.  I put a copy here:

http://sage.math.washington.edu/home/mhampton/biopython-1.52.spkg

Thanks very much for taking a look!

Marshall



---

archive/issue_comments_057999.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-07T07:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-57999",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058000.json:
```json
{
    "body": "The program itself looks nice but the package does not seem to conform to the guidelines at http://www.sagemath.org/doc/developer/producing_spkgs.html. \n\nFor example:\n* no hg repository\n* no src directory: there is a source directory and then a link to it. \n* missing parts in the SPKG.txt (Description,License,Upstream Contact)\n* this package does have it's own test suite so a spkg-check would also be nice\n\nDo you have time or should I work on it? \n\nCheers,\nAdam",
    "created_at": "2009-10-07T07:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58000",
    "user": "https://github.com/maxthemouse"
}
```

The program itself looks nice but the package does not seem to conform to the guidelines at http://www.sagemath.org/doc/developer/producing_spkgs.html. 

For example:
* no hg repository
* no src directory: there is a source directory and then a link to it. 
* missing parts in the SPKG.txt (Description,License,Upstream Contact)
* this package does have it's own test suite so a spkg-check would also be nice

Do you have time or should I work on it? 

Cheers,
Adam



---

archive/issue_comments_058001.json:
```json
{
    "body": "Some suggestions. ;-)\n\nSPKG.txt\n\n```\n## Description\n\nBiopython is a set of freely available tools for biological computation written in Python by an international team of developers.\n\nIt is a distributed collaborative effort to develop Python libraries and applications which address the needs of current and future work in bioinformatics.\n\n## License\n\nBiopython License\n\n## SPKG Maintainers\n\n  -- Marshall Hampton, mhampton at d.umn.edu or hamptonio at gmail.com.\n\n## Upstream Contact\n\n  -- wiki - http://biopython.org/wiki/Main_Page\n```\n\n\nspkg-check (keeping biopython as directory name)\n\n```/usr/bin/env bash\n\nif [ \"$SAGE_LOCAL\" = \"\" ]; then\n   echo \"SAGE_LOCAL undefined ... exiting\";\n   echo \"Maybe run 'sage -sh'?\"\n   exit 1\nfi\n\ncd biopython\npython setup.py test\n\nif [ $? -ne 0 ]; then\n   echo \"Error testing biopython\"\n   exit 1\nfi\n```\n\n\nI hope this is useful,\n\nAdam",
    "created_at": "2009-10-07T18:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58001",
    "user": "https://github.com/maxthemouse"
}
```

Some suggestions. ;-)

SPKG.txt

```
## Description

Biopython is a set of freely available tools for biological computation written in Python by an international team of developers.

It is a distributed collaborative effort to develop Python libraries and applications which address the needs of current and future work in bioinformatics.

## License

Biopython License

## SPKG Maintainers

  -- Marshall Hampton, mhampton at d.umn.edu or hamptonio at gmail.com.

## Upstream Contact

  -- wiki - http://biopython.org/wiki/Main_Page
```


spkg-check (keeping biopython as directory name)

```/usr/bin/env bash

if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi

cd biopython
python setup.py test

if [ $? -ne 0 ]; then
   echo "Error testing biopython"
   exit 1
fi
```


I hope this is useful,

Adam



---

archive/issue_comments_058002.json:
```json
{
    "body": "Thanks, that's very useful.  The biopython optional package has existed for quite a while - William Stein added it for me in 2006 I think - and so it predates some of those good newer conventions.  \n\nI don't have a lot of time for sprucing it up, so if you want to to take the lead on that please go ahead! \n\nThe test suite is quite extensive, and I agree that it would be good to have a spkg-check for it.  I have experienced some funny issues running the tests, with some path-related failures unless I copied the tests into the sage directory structure.  Unfortunately I don't really understand what causes them.  If those path issues are cleared up then everything in the test suite should pass.\n\nRealistically I won't have time to improve the spkg until mid-November at least.",
    "created_at": "2009-10-08T02:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Thanks, that's very useful.  The biopython optional package has existed for quite a while - William Stein added it for me in 2006 I think - and so it predates some of those good newer conventions.  

I don't have a lot of time for sprucing it up, so if you want to to take the lead on that please go ahead! 

The test suite is quite extensive, and I agree that it would be good to have a spkg-check for it.  I have experienced some funny issues running the tests, with some path-related failures unless I copied the tests into the sage directory structure.  Unfortunately I don't really understand what causes them.  If those path issues are cleared up then everything in the test suite should pass.

Realistically I won't have time to improve the spkg until mid-November at least.



---

archive/issue_comments_058003.json:
```json
{
    "body": "OK,\n\nI'll see what I can do. ~ Adam",
    "created_at": "2009-10-08T05:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58003",
    "user": "https://github.com/maxthemouse"
}
```

OK,

I'll see what I can do. ~ Adam



---

archive/issue_comments_058004.json:
```json
{
    "body": "Where do I put the spkg when I have it done? Is there an in-box or something? ~ Adam",
    "created_at": "2009-10-08T13:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58004",
    "user": "https://github.com/maxthemouse"
}
```

Where do I put the spkg when I have it done? Is there an in-box or something? ~ Adam



---

archive/issue_comments_058005.json:
```json
{
    "body": "Well, uploading it anywhere you have access to is fine.  If you don't have a good place to park it, you should ask for a sage.math account and put it there.  Just email William Stein, or ask on IRC.  I'm not sure, maybe Minh or someone else also has the ability to make sage.math accounts.\n\n-Marshall",
    "created_at": "2009-10-08T23:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Well, uploading it anywhere you have access to is fine.  If you don't have a good place to park it, you should ask for a sage.math account and put it there.  Just email William Stein, or ask on IRC.  I'm not sure, maybe Minh or someone else also has the ability to make sage.math accounts.

-Marshall



---

archive/issue_comments_058006.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-11T09:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58006",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058007.json:
```json
{
    "body": "I put a new spkg at http://sage.math.washington.edu/home/awebb/biopython-1.52.p0.spkg. \n\nAdam",
    "created_at": "2009-10-11T09:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58007",
    "user": "https://github.com/maxthemouse"
}
```

I put a new spkg at http://sage.math.washington.edu/home/awebb/biopython-1.52.p0.spkg. 

Adam



---

archive/issue_comments_058008.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-24T15:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058009.json:
```json
{
    "body": "Looks good!  Thanks!\nI'm a little confused on how to use the spkg-check script, but that's not your fault I think.  I will write to sage-devel about that.  I just haven't used such a script before.",
    "created_at": "2009-10-24T15:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Looks good!  Thanks!
I'm a little confused on how to use the spkg-check script, but that's not your fault I think.  I will write to sage-devel about that.  I just haven't used such a script before.



---

archive/issue_events_007241.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-10-25T06:52:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7019#event-7241"
}
```



---

archive/issue_comments_058010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-25T06:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58010",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_058011.json:
```json
{
    "body": "I posted it.",
    "created_at": "2009-10-25T06:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7019#issuecomment-58011",
    "user": "https://github.com/williamstein"
}
```

I posted it.
