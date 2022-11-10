import model
import view

def button():
    value_a = view.get_valuea()
    op = view.oper()
    value_b = view.get_valueb()
    model.init(value_a,value_b)
    if op == '*':
        result = model.mult()
    elif op == '/':
        result = model.div()
    elif op == '+':
        result = model.sum()
    elif op == '-':
        result = model.sub()
    view.view_data(result)
