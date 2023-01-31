import view
import model

def start():
    text = view.input_quest()
    result = model.multyply_divide(text)
    view.print_quest(result)



# def start():
# quest = ''
# view.input_quest()
# view.print_quest()
# model.multyply_divide(quest)

# model.multyply_divide(print_quest)