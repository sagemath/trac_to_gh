# Issue 8015: Unify code for cusps over Q and number fields

archive/issues_008015.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @JohnCremona mtaranes\n\nThe code at #6863 provides an implementation of cusps over number fields other than Q. As I commented on the ticket, this code should be merged with that for cusps over Q. This ticket is a request to do exactly that.\n\nIt's important that great care be taken when doing this, so that we don't accidentally slow down cusps over Q, which are crucial to modular symbols calculations. In particular, no patch should be merged on this ticket without some comprehensive benchmarks showing no slowdown.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8015\n\n",
    "created_at": "2010-01-20T20:07:37Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Unify code for cusps over Q and number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8015",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

CC:  @JohnCremona mtaranes

The code at #6863 provides an implementation of cusps over number fields other than Q. As I commented on the ticket, this code should be merged with that for cusps over Q. This ticket is a request to do exactly that.

It's important that great care be taken when doing this, so that we don't accidentally slow down cusps over Q, which are crucial to modular symbols calculations. In particular, no patch should be merged on this ticket without some comprehensive benchmarks showing no slowdown.

Issue created by migration from https://trac.sagemath.org/ticket/8015


