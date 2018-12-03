

'''
This file will contain different variable ordering heuristics to be used within
bt_search.

1. ord_dh(csp)
    - Takes in a CSP object (csp).
    - Returns the next Variable to be assigned as per the DH heuristic.
2. ord_mrv(csp)
    - Takes in a CSP object (csp).
    - Returns the next Variable to be assigned as per the MRV heuristic.
3. val_lcv(csp, var)
    - Takes in a CSP object (csp), and a Variable object (var)
    - Returns a list of all of var's potential values, ordered from best value
      choice to worst value choice according to the LCV heuristic.

The heuristics can use the csp argument (CSP object) to get access to the
variables and constraints of the problem. The assigned variables and values can
be accessed via methods.
'''


from cspbase import *
from propagators import *


def ord_dh(csp):
    # TODO! IMPLEMENT THIS!

    max_value = None
    max_cons = -1
    unasigned = csp.get_all_unasgn_vars()

    for v in unasigned:
        count = 0
        cons = csp.get_cons_with_var(v)
        for c in cons:
            n = c.get_n_unasgn()
            count += n-1
        if max_cons < 0 :
            max_cons = count
            max_value = v

        elif max_cons < count:
            max_cons = count
            max_value = v

    return max_value


def ord_mrv(csp):
    # TODO! IMPLEMENT THIS!

    min_value = None
    min_dom = -1
    unasinged = csp.get_all_unasgn_vars()

    for v in unasinged:
        if min_dom < 0:
            min_dom = v.cur_domain_size()
            min_value = v

        elif v.cur_domain_size() < min_dom:
            min_dom = v.cur_domain_size()
            min_value = v

    return min_value


def val_lcv(csp, var):
    # TODO! IMPLEMENT THIS!

    domain = var.cur_domain()
    lcv = []
    list = []
    cons = csp.get_cons_with_var(var)
    for d in domain:
        var.assign(d)
        num_pruned = 0
        for c in cons:
            vars = c.get_unasgn_vars()
            for V in vars:
                d_new = V.cur_domain()
                for i in d_new:
                    if not c.has_support(V, i):
                        num_pruned = 1 + num_pruned

        var.unassign()
        list.append((num_pruned, d))

    list.sort()

    for i in list:
        lcv.append(i[1])

    return lcv








