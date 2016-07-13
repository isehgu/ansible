#! /usr/bin/env python
from ansible.module_utils.basic import AnsibleModule
import subprocess


DOCUMENTATION = '''
    Run commands within a gts env.

'''

EXAMPLE = '''
    - name: Run command inside gtsenv
      gtsenv: command=gtsCtrl status env_number=038

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
    real_command = "echo " + command + "| gtsenv " + env_number
    # Now use subprocess, run the command, capture output, parse it,
    # and interpret if it's successful then constructure resulting json
    command_result = subprocess.Popen(
        real_command, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    #######################
    # Reading command results
    line = ''
    rc = ''
    stderr = ''
    stdout = ''
    stdoutlines = []
    while True:
        line = command_result.stdout.readline()
        rc = command_result.poll()

        if not line:
            if rc is not None:
                break
        else:
            stdoutlines.append(line.rstrip())

    stderr = command_result.stderr.read()
    stdout = ' '.join(stdoutlines)

    result = {
        'rc': rc,
        'command_executed': real_command,
        'stderr': stderr,
        'stdout': stdout,
        'stdoutlines': stdoutlines
    }

    if rc == 0:
        module.exit_json(**result)
    else:
        module.fail_json(**result)

if __name__ == '__main__':
    main()
