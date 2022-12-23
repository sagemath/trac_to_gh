# Issue 5728: limit option is misdocumented in n=100; n.factor?

Issue created by migration from https://trac.sagemath.org/ticket/5728

Original creator: was

Original creation time: 2009-04-09 19:55:51

Assignee: was

if limit is beyond pari prime bound, then limit is just replaced by min(limit, pari prime bound), which silently misleads the poor user. 
