#! /usr/bin/env python
# Custom ansible filters for linux. 
# Common ones that are not found in ansible


def cutLastLoginLine(output_list):
    result_list = []

    for line in output_list:

        if 'Last login' in line:
            continue

        result_list.append(line)

    return result_list

def HasUniqueListItem(list1, list2)
    """ Is there any item in list1 that doesn't
    contain any of list2 items?
    Yes/True - There is at least one item in list1 that doesnt
    contain any one of the list2 items
    No/False -- All items of list1 contains at least one item from
    list2"""
    
    for item1 in list1:
        # We assume item1 is unique unless discovered in the inner loop
        unique = True
        for item2 in list2:
            if item2 in item1
                # Item1 has item2, it's no longer unique
                unique = False
                break

        # if unique = False, then this specific item1 contains at least 1 of list2
        # then we move onto the next item1
        # if unique = True, then this particular item1 doesn't contain any of list2
        # then we return True because an unqiue list item has been found
        if unique == True:
            return unique

    # Last item1 processed, and unique is not True for that last item1
    # So just return unique, which is false
    return unique





class FilterModule(object):
    ''' The FilterModule class defines a filters method 
    that returns a dictionary with the name of the 
    filter function and the function itself.
    The FilterModule class is Ansible-specific code that
    makes the Jinja2 filter available to Ansible.  '''

    def filters(self):
        return {
            'cutLastLoginLine': cutLastLoginLine,
            'HasUniqueListItem': HasUniqueListItem,
        }
