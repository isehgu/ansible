#! /usr/bin/env python
# Custom ansible filters for gts core


def gtsOpconCutFluff(output_list):
    """ Cut out everything above ======= including ======== from opcon output """
    result_list = []
    separator = 0

    for line in output_list:
        if '========' in line:
            separator = 1
            continue

        if 'Last login' in line:
            continue

        if separator:
            result_list.append(line)

    return result_list


def gtsOpconResultCount(output_list):
    """ Count the number of lines after ======= from opcon output """
    result_count = 0
    separator = 0
    for line in output_list:
        if '========' in line:
            separator = 1
            continue

        if 'Last login' in line:
            continue

        if separator:
            result_count += 1

    return result_count

class FilterModule(object):
    ''' The FilterModule class defines a filters method 
    that returns a dictionary with the name of the 
    filter function and the function itself.
    The FilterModule class is Ansible-specific code that
    makes the Jinja2 filter available to Ansible.  '''

    def filters(self):
        return {
            'gtsOpconCutFluff': gtsOpconCutFluff,
            'gtsOpconResultCount': gtsOpconResultCount
        }
