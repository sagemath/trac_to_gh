# Issue 1307: [graphs] Strongly regular graph database

archive/issues_001307.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  mvngu dimpase\n\nKeywords: graphs\n\nFrom Chris Godsil's wishlist:\n\n\n```\n> \n>>> A database of small graphs. Put Ted Spence's strongly regular graphs\n>>> into a\n>>> database. (In this case the important thing is to have the graphs\n>>> themselves,\n>>> we would not necessarily need much data.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1307\n\n",
    "created_at": "2007-11-28T19:54:36Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "[graphs] Strongly regular graph database",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1307",
    "user": "jason"
}
```
Assignee: mhansen

CC:  mvngu dimpase

Keywords: graphs

From Chris Godsil's wishlist:


```
> 
>>> A database of small graphs. Put Ted Spence's strongly regular graphs
>>> into a
>>> database. (In this case the important thing is to have the graphs
>>> themselves,
>>> we would not necessarily need much data.)
```


Issue created by migration from https://trac.sagemath.org/ticket/1307





---

archive/issue_comments_008223.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8223",
    "user": "rlm"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008224.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"database\".",
    "created_at": "2007-12-17T15:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8224",
    "user": "rlm"
}
```

Changing keywords from "graphs" to "database".



---

archive/issue_comments_008225.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2007-12-17T15:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8225",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_008226.json:
```json
{
    "body": "CC'ing myself",
    "created_at": "2009-06-27T00:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8226",
    "user": "mvngu"
}
```

CC'ing myself



---

archive/issue_comments_008227.json:
```json
{
    "body": "If it just consists in converting the 32,548 graphs with parameters (36-15-6-6) to some database, I could do that with a bit of scripting... I saw there was in SAGE_DATA a file graphs.db ( sqlite format ), and the trouble is that I do not know what it contains, how to open it, and how to build one myself if it is what you expect... Could I know a bit more about this ? :-)",
    "created_at": "2009-08-22T16:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8227",
    "user": "ncohen"
}
```

If it just consists in converting the 32,548 graphs with parameters (36-15-6-6) to some database, I could do that with a bit of scripting... I saw there was in SAGE_DATA a file graphs.db ( sqlite format ), and the trouble is that I do not know what it contains, how to open it, and how to build one myself if it is what you expect... Could I know a bit more about this ? :-)



---

archive/issue_comments_008228.json:
```json
{
    "body": "I believe that database just contains the data that is exposed here:\n\nhttp://good.math.iastate.edu/grout/graphs/\n\nYou can download one of the many SQLITE GUI tools listed at http://www.sqlite.org/cvstrac/wiki?p=ManagementTools and look at the database.",
    "created_at": "2009-08-22T19:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8228",
    "user": "jason"
}
```

I believe that database just contains the data that is exposed here:

http://good.math.iastate.edu/grout/graphs/

You can download one of the many SQLITE GUI tools listed at http://www.sqlite.org/cvstrac/wiki?p=ManagementTools and look at the database.



---

archive/issue_comments_008229.json:
```json
{
    "body": "Thank you !!! I understand how it works now :-)\n\nWell, so what about this database ? Do you think it would be a good idea to build a sqlite database for Sage with these graphs ? I do not know, for example, if this database will be compressed in any way, because there are a lot of graphs available and it could become a bit heavy.. \nIs there anything more efficient, in case the users needs to enumerate them all ?",
    "created_at": "2009-08-23T09:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8229",
    "user": "ncohen"
}
```

Thank you !!! I understand how it works now :-)

Well, so what about this database ? Do you think it would be a good idea to build a sqlite database for Sage with these graphs ? I do not know, for example, if this database will be compressed in any way, because there are a lot of graphs available and it could become a bit heavy.. 
Is there anything more efficient, in case the users needs to enumerate them all ?



---

archive/issue_comments_008230.json:
```json
{
    "body": "Here is a worksheet showing how to convert the graphs on Ted's page to Sage graphs: http://test.sagenb.org/home/pub/17/",
    "created_at": "2011-11-08T14:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8230",
    "user": "jason"
}
```

Here is a worksheet showing how to convert the graphs on Ted's page to Sage graphs: http://test.sagenb.org/home/pub/17/



---

archive/issue_comments_008231.json:
```json
{
    "body": "Hey, this\u00a0would be really useful.  Jason, if you see this, can you paste that code here?  Also, I'm not sure where your database lives now.  This could easily become an optional database, and Magma also has such things.",
    "created_at": "2014-10-23T14:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8231",
    "user": "kcrisman"
}
```

Hey, this would be really useful.  Jason, if you see this, can you paste that code here?  Also, I'm not sure where your database lives now.  This could easily become an optional database, and Magma also has such things.



---

archive/issue_comments_008232.json:
```json
{
    "body": "(just a note: we have 4 constructors of families of strongly regular graphs from http://www.win.tue.nl/~aeb/graphs/srg/srgtab.html. AffineOrthogonalPolarGraph, OrthogonalPolarGraph, PaleyGraph, SymplecticGraph)",
    "created_at": "2014-10-23T14:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8232",
    "user": "ncohen"
}
```

(just a note: we have 4 constructors of families of strongly regular graphs from http://www.win.tue.nl/~aeb/graphs/srg/srgtab.html. AffineOrthogonalPolarGraph, OrthogonalPolarGraph, PaleyGraph, SymplecticGraph)



---

archive/issue_comments_008233.json:
```json
{
    "body": "Yes, just that's not a database :)",
    "created_at": "2014-10-23T14:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1307#issuecomment-8233",
    "user": "kcrisman"
}
```

Yes, just that's not a database :)
