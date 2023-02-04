import tkinter as tk


ans = {'result': str()}


def btn_show_operator(operator):
    curr = lbl_result['text']
    if curr[-2:] == '**':
        lbl_result['text'] = curr[:-2] + operator

    elif curr[-1] in ['+', '-', 'x', '÷']:
        lbl_result['text'] = curr[:-1] + operator

    else:
        lbl_result['text'] += operator


def btn_equals(answer):
    curr = lbl_result['text'].replace('x', '*').replace('÷', '/')
    lbl_result['text'] = f"{eval(curr)}"  # ==> str(eval(curr))
    answer['result'] = lbl_result['text']


def btn_all_clear():
    lbl_result['text'] = '0'


def btn_clear():
    curr = lbl_result['text']
    if len(curr) == 1:
        lbl_result['text'] = '0'
    else:
        lbl_result['text'] = lbl_result['text'][:-1]


def btn_show_point(point):
    curr = lbl_result['text']
    if not is_last_number_decimal(curr):
        lbl_result['text'] += point


def is_last_number_decimal(curr):
    for char in curr[::-1]:
        if char == '*':
            char = '**'
        if char == '.':
            return True
        if char in ['+', '-', 'x', '÷', '**']:
            return False

    return False


def btn_show_number(number, answer):
    curr = lbl_result['text']
    
    if curr == '0':
        lbl_result['text'] = number

    elif answer['result'] == curr:
        lbl_result['text'] = number
        answer['result'] = str()

    elif any(operator in curr for operator in ['+', '-', 'x', '÷', '**']):
        for i in range(len(curr)):
            last_operator = curr[(i*-1)-1]
            if last_operator == '*':
                last_operator = '**'
            if last_operator in ['+', '-', 'x', '÷', '**']:
                last_number = curr.split(last_operator)[-1]
                if last_number == '0':
                    lbl_result['text'] = curr[:-1] + number
                    return
                else:
                    lbl_result['text'] += number
                    return

    else:
        lbl_result['text'] += number


window = tk.Tk()
window.title('Calculator')

lbl_result = tk.Label(
    master=window,
    text='0',
    width=32,
    height=3,
)
lbl_result.grid(row=0, column=0, columnspan=4)

btns_properties = [
    {
        'text': 'AC',
        'command': btn_all_clear,
    },
    {
        'text': 'C',
        'command': btn_clear,
    },
    {
        'text': '+',
        'command': lambda: btn_show_operator('+'),
    },
    {
        'text': '-',
        'command': lambda: btn_show_operator('-'),
    },
    {
        'text': '7',
        'command': lambda: btn_show_number('7', ans),
    },
    {
        'text': '8',
        'command': lambda: btn_show_number('8', ans),
    },
    {
        'text': '9',
        'command': lambda: btn_show_number('9', ans),
    },
    {
        'text': 'x',
        'command': lambda: btn_show_operator('x'),
    },
    {
        'text': '4',
        'command': lambda: btn_show_number('4', ans),
    },
    {
        'text': '5',
        'command': lambda: btn_show_number('5', ans),
    },
    {
        'text': '6',
        'command': lambda: btn_show_number('6', ans),
    },
    {
        'text': '÷',
        'command': lambda: btn_show_operator('÷'),
    },
    {
        'text': '1',
        'command': lambda: btn_show_number('1', ans),
    },
    {
        'text': '2',
        'command': lambda: btn_show_number('2', ans),
    },
    {
        'text': '3',
        'command': lambda: btn_show_number('3', ans),
    },
    {
        'text': '**',
        'command': lambda: btn_show_operator('**'),
    },
    {
        'text': '.',
        'command': lambda: btn_show_point('.'),
    },
    {
        'text': '0',
        'command': lambda: btn_show_number('0', ans),
    },
    {
        'text': '=',
        'command': lambda: btn_equals(ans),
    },
    {
        'text': '☺',
        'command': None, 
    },
]


for index, btn_property in enumerate(btns_properties):
    btn = tk.Button(
        master=window,
        text=btn_property['text'],
        command=btn_property['command'],
        height=2,
    )
    btn.grid(row=(index//4)+1, column=index % 4, sticky='nsew')


if __name__ == '__main__':
    # This code won't run if this file is imported
    window.mainloop()
