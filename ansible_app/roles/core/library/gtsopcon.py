#! /usr/bin/env python
from ansible.module_utils.basic import AnsibleModule
import subprocess


DOCUMENTATION = '''
---
module: gtsopcon
author: Han Gu
description: Run opcon commands
options:
  env_number:
    required: True
    description: gts env number
  command:
    required: True
    description: opcon command to run


'''

EXAMPLES = '''
    - name: Run opcon commands
      gtsopcon: command="gtsstatus -m" env_number=038

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
    command = module.params['command']
    real_command = "echo 'echo " + command + "| opcon -s' | gtsenv " + env_number
    # Now use subprocess, run the command, capture output, parse it,
    # and interpret if it's successful then constructure resulting json
    command_result = subprocess.Popen(
        real_command, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

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
    # command_result.stderr.close()
    # command_result.stdout.close()

    #######################
    # Reading command results using communicate
    rc = ''
    stderr = ''
    stdout = ''

    stdout, stderr = command_result.communicate()
    rc = command_result.wait()

    result = {
        'rc': rc,
        'command_executed': real_command,
        'stderr': stderr,
        'stdout': stdout
    }

    if rc == 0:
        module.exit_json(**result)
    else:
        module.fail_json(msg='Command returned with error', **result)

if __name__ == '__main__':
    main()
