#! /usr/bin/env python
from ansible.module_utils.basic import AnsibleModule
import subprocess


DOCUMENTATION = '''
---
module: gtsenv
author: Han Gu
description: Run commands within a gts env.
options:
  env_number:
    required: True
    description: gts env number
  command:
    required: True
    description: command to run within the gts environment
'''

EXAMPLES = '''
- name: Run command inside gtsenv
  gtsenv: command="gtsCtrl status" env_number=038

'''


def main():
    input_structure = {
        'env_number': {'required': True, 'type': 'str'},
        'command': {'required': True, 'type': 'str'}
    }

    # Getting input from yml files
    module = AnsibleModule(
        argument_spec=input_structure,
        supports_check_mode=True
        )

    env_number = module.params['env_number']
    command = '"' + module.params['command'] + '"'
    #command = module.params['command']
    real_command = "echo " + command + "| gtsenv " + env_number
    #real_command = "ls -al | grep ansible_stuff"
    # Now use subprocess, run the command, capture output, parse it,
    # and interpret if it's successful then constructure resulting json
    # command_result = subprocess.Popen(
    #     real_command, shell=True,
    #     stdout=subprocess.PIPE, stderr=subprocess.PIPE
    #     )

    #######################
    # Reading command results
    # line = ''
    # rc = ''
    # stderr = ''
    # stdout = ''
    # stdoutlines = []
    # while True:
    #     line = command_result.stdout.readline()
    #     rc = command_result.poll()

    #     if not line:
    #         if rc is not None:
    #             break
    #     else:
    #         if "Last login" in line:
    #             continue
    #         else:
    #             stdoutlines.append(line.rstrip())

    # stderr = command_result.stderr.read()
    # stdout = ' '.join(stdoutlines)

    ################################################
    # Using ansible's own run_command function
    rc = ''
    stderr = ''
    stdout = ''
    (rc, stdout, stderr) = module.run_command(real_command, use_unsafe_shell=True)
    result = {
        'rc': rc,
        'command_executed': real_command,
        'stderr': stderr,
        'stdout': stdout
        # 'stdoutlines': stdoutlines
    }

    if rc == 0:
        module.exit_json(**result)
    else:
        module.fail_json(msg='Command returned with error', **result)

if __name__ == '__main__':
    main()
