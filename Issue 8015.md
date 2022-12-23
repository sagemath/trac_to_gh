# Issue 8015: Unify code for cusps over Q and number fields

Issue created by migration from https://trac.sagemath.org/ticket/8015

Original creator: craigcitro

Original creation time: 2010-01-20 20:07:37

Assignee: craigcitro

CC:  cremona mtaranes

The code at #6863 provides an implementation of cusps over number fields other than Q. As I commented on the ticket, this code should be merged with that for cusps over Q. This ticket is a request to do exactly that.

It's important that great care be taken when doing this, so that we don't accidentally slow down cusps over Q, which are crucial to modular symbols calculations. In particular, no patch should be merged on this ticket without some comprehensive benchmarks showing no slowdown.
