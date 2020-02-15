# File Based Semaphore Lock Failure

## Problem statement

Two applications compete over the same file acting as a semaphore lock. When one of the applications do not close the lock correctly, or crashes before it manages to release the lock, the other applications, or the next instance will fail to obtain the lock and will stuck in busy wait.

## Assumptions

## Observations

One or more applications are stuck with high CPU usage.

## Investigations path

Attempt to understand the source of issue by investigating the applicaiton logs and standard output and error.
Determine the process hogging the lock file by either reading the PID out of the file (a common practice), or by using `lsof <file_name>`

## Final the drill down to display the discovered root cause of the problem

