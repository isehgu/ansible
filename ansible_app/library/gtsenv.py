#! /usr/bin/env python

DOCUMENTATION = '''
    Run commands within a gts env.

'''

EXAMPLE = '''

'''


from ansible.module_utils.basic import AnsibleModule
import subprocess

def main():
    input_structure = {}

    # Getting input from yml files
    module = AnsibleModule(
        argument_spec = input_structure,
        supports_check_mode = True
        )

    env_number = module.params['env_number']
    command = module.params['command']

    # Actual command -- echo "command" | gtsenv env_number
    # Need to make sure special characters are escaped correctly
    real_command = "echo \"%s\" | gtsenv %s" % (command, env_number)

    # Now use subprocess, run the command, capture output, parse it, and interpret if it's successful
    # then constructure resulting json

    result = {}
    module.exit_json(**result)

if __name__ == '__main__':
    main()