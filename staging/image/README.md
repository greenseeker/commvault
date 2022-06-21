# image
## scripts
These files need to be copied into the image:
* initiator.py goes in /opt/staging/initiator/
* sysprep_*distro* goes in /usr/local/sbin, renamed to 'sysprep'

Be sure to run `chmod +x /opt/staging/initiator/initiator.py /usr/local/sbin/sysprep` so the scripts can be executed.

### running initiator.py
Usage:  `initiator.py <key=value> [<key=value> ...]`

This script is called by SCVMM at provisioning to write the parameters to a yaml file and then launch the ansible payload to configure the VM. Make sure there are no spaces on either side of the equals sign in <key=value> arguments. 

When passing values with backslashes or exclamation points, be sure to wrap the whole key=value in single quotes to avoid them being treated as special characters.

The following initiator.py arguments are required:
* database_path = string; path to dump file to be restored.
* install_hpk = boolean; to install the maintenance release matching customer environment.

The following initiator.py arguments are optional:
* test_mode = boolean; pull the payload from the test branch instead of main and save copies of files before cleanup in the playbook.
* ansible_vers = string; this can be specified to upgrade Ansible before calling the playbook so that we can standardize on a single version without having to update all existing images. parameters['ansible_vers'] within the script should be set to whatever version is included in the image.


## repo file
You must manually create /etc/staging/repo.yaml with the following syntax:
```
---
main: "https://credentials@git_repo_url"
...
```

## updating the image
Whenever you update the image, use the `sysprep` command to shut it down instead of `poweroff` or `shutdown`.

