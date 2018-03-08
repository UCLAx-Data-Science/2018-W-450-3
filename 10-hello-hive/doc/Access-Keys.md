# AWS Access Token

Access keys consist of an access key ID (for example, `AKIAIOSFODNN7EXAMPLE`) and a secret access key (for example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). You use access keys to sign programmatic requests that you make to AWS if you use the AWS SDKs, REST, or Query API operations. The AWS SDKs use your access keys to sign requests for you, so that you don't have to handle the signing process.

Access keys are also used with command line interfaces (CLIs). When you use a CLI, the commands that you issue are signed by your access keys. You can pass access keys either with the command or store as configuration settings on your computer.

## Managing Access Keys for Your AWS Account

You can create, rotate, disable, or delete access keys (access key IDs and secret access keys) for your AWS account root user. Anyone who has an access key for your AWS account has unrestricted access to all the resources in your account, including billing information.

We recommend that you don't create access keys for your AWS account and delete any that exist. Instead, create a user in AWS Identity and Access Management (IAM) and choose Programmatic access to create an access key for the user. For more information, see Lock away your AWS account root user access keys in the IAM User Guide.

When you create an access key, AWS gives you an opportunity to view and download the secret access key only once. If you don't download it or if you lose it, you can delete the access key and then create a new one.

A newly created access key has the status of active, which means that you can use the access key for API calls. You can have up to two access keys for your AWS account, which is useful when you want to rotate the access keys. When you disable an access key, you can't use it for API calls.

You can create or delete an access key any time. However, when you delete an access key, it's gone forever and can't be retrieved.

### Creating, Disabling, and Deleting Access Keys for Your AWS Account

Follow these steps to manage access keys for your AWS account. For information about managing access keys for IAM users, see Managing Access Keys for IAM Users in the IAM User Guide.

To create, disable, or delete an access key for your AWS account root user:

1. Use your AWS account email address and password to sign in to the AWS Management Console as the AWS account root user.
1. On the IAM Dashboard page, choose your account name in the navigation bar, and then choose My Security Credentials.
1. If you see a warning about accessing the security credentials for your AWS account, choose Continue to Security Credentials.
1. Expand the Access keys (access key ID and secret access key) section.

Choose your preferred action:

#### To create an access key
Choose Create New Access Key. Then choose Download Key File to save the access key ID and secret access key to a file on your computer. After you close the dialog box, you can't retrieve this secret access key again.

#### To disable an existing access key
Choose Make Inactive next to the access key that you are disabling. To reenable an inactive access key, choose Make Active.

#### To delete an existing access key
Before you delete an access key, make sure it's no longer in use. For more information, see Finding unused access keys in the IAM User Guide. You can't recover an access key after deleting it. To delete your access key, choose Delete next to the access key that you you want to delete.