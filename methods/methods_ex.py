# create a method that takes state and gross income and returns net income


def get_net_income(state, gross_income):
    """
    Calculate the net income based on the state and gross income
    :param state: the state name
    :param gross_income_orig: amount of gross income
    :return: net income after deducting the taxes
    """
    state_taxes = {'NY': 0.05, 'Alabama': 0.10, 'Florida': 0.20, 'Kentucky': 0.33}
    fed_tax = 0.10

    if state in state_taxes:
        state_tax = state_taxes[state]
        net_income = gross_income - gross_income * (state_tax + fed_tax)
        print('Gross income in {} is {}$\nNet income is {:.2f}$\n'
              .format(state, gross_income, net_income))
        return net_income
    else:
        print('This state ({}) is not in the database.'.format(state))
        return None


get_net_income('NY', 100000)
