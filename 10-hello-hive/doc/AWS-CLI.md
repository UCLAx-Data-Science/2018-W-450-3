# What Is the AWS Command Line Interface?

The AWS CLI is an open source tool built on top of the AWS SDK for Python (Boto) that provides commands for interacting with AWS services. With minimal configuration, you can start using all of the functionality provided by the AWS Management Console from your favorite terminal program.

- Linux shells – Use common shell programs such as Bash, Zsh, and tsch to run commands in Linux, macOS, or Unix.
- Windows command line – On Microsoft Windows, run commands in either PowerShell or the Windows Command Processor.
- Remotely – Run commands on Amazon EC2 instances through a remote terminal such as PuTTY or SSH, or with Amazon EC2 systems manager.
- The AWS CLI provides direct access to AWS services' public APIs. Explore a service's capabilities with the AWS CLI, and develop shell scripts to manage your resources. Or take what you've learned to develop programs in other languages with the AWS SDK.

In addition to the low level, API equivalent commands, the AWS CLI also provides customizations for several services. Customizations are higher level commands that simplify using a service with a complex API. For example, the aws s3 set of commands provide a familiar syntax for managing files in Amazon S3.

## Example Upload a file to Amazon S3

`aws s3 cp` provides a shell-like copy command, and automatically performs a multipart upload to transfer large files quickly and resiliently.

```
~$ aws s3 cp myvideo.mp4 s3://mybucket/
``` 