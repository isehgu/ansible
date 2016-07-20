#! /usr/bin/env python
# Custom ansible filters for linux. 
# Common ones that are not found in ansible


def cutLastLoginLine(output_list):
    """ Cut out everything above ======= including ======== from opcon output """
    result_list = []
    separator = 0

    for line in output_list:

        if 'Last login' in line:
            continue

        if separator:
            result_list.append(line)

    return result_list

class FilterModule(object):
    ''' The FilterModule class defines a filters method 
    that returns a dictionary with the name of the 
    filter function and the function itself.
    The FilterModule class is Ansible-specific code that
    makes the Jinja2 filter available to Ansible.  '''

    def filters(self):
        return {
            'cutLastLoginLine': cutLastLoginLine
        }
