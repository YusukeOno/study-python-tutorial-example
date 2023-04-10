TAX_RATES_BY_STATE = {  # 州ごとの売上税率
    'MI': 1.06,  # ミシガン州
}


def add_sales_tax(total, state):
    return total * TAX_RATES_BY_STATE[state]
