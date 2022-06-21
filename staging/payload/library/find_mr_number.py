#!/usr/bin/python

DOCUMENTATION = '''
---
module: find_mr_number
short_description: Get the Commserve's Maintenance Release number from the infofile or database.
'''

EXAMPLES = '''
- name: Get Maintenance Release from infofile.json
  find_mr_number:
    infofile_path: /mnt/escalationlogs/ABCDE/211205-100/2021_12_05_21_00_32
  register: customer_mr_num

- name: Get Maintenance Release from CSDB
  find_mr_number:
    check_db: true
  register: customer_mr_num
'''

from ansible.module_utils.basic import AnsibleModule
from re import findall
from os.path import exists
from json import load as readjson

def main():
    csmr = -1
    fields = {
        "infofile_path": { "default": None, "type":"str" },
	    "check_db": { "default":False, "type":"bool" }
    }

    module = AnsibleModule(argument_spec=fields)

    infofile_path = module.params['infofile_path']
    check_db = module.params['check_db']

    if infofile_path:
        if exists(infofile_path + "/infofile.json"):
            with open(infofile_path + "/infofile.json") as f:
                infofile = readjson(f)
            csmr = infofile['Servers']['Id_2']['SoftwareVersion'][2]

        elif exists(infofile_path + "/infofile.html"):
            with open(infofile_path + "/infofile.html") as f:
                infofile = f.read()

            results = findall(r'Platform:.+|Software Version:.+', infofile)

            for x in range(len(results)):
                if "CommServer" in results[x]:
                    csmr = results[x+1].split('.')[-1]
                    break
                else:
                    csmr = None

    if check_db and not csmr:
        # TBD: Query the MR from the DB
        # select distinct top 1 UPNumber from simInstalledPackages where ClientId = 2 and HighestSP = $CVLTServicePackNumber order by UPNumber desc
        pass

    # response = {"mr": mr}
    module.exit_json(changed=False, mr=csmr)

if __name__ == '__main__':
    main()
