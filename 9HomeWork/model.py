

def multyply_divide(text: str):
    text = text.replace(' ', '').replace('+', ' + ').\
        replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    text = text.split()
    while len(text) > 1:
        while '*' in text or '/' in text:
            i = 0
            while i < len(text):
                if text[i] == '*':
                    text[i-1] = int(text[i-1])*int(text[i+1])
                    text.pop(i)
                    text.pop(i)
                elif text[i] == '/':
                    text[i - 1] = int(text[i - 1]) / int(text[i + 1])
                    text.pop(i)
                    text.pop(i)
                i = i +1
        while '+' in text or '-' in text:
            i = 0
            while i < len(text):
                if text[i] =='+':
                    text[i - 1] = int(text[i-1]) + int(text[i+1])
                    text.pop(i)
                    text.pop(i)
                elif text[i] =='-':
                    text[i - 1] = int(text[i - 1]) - int(text[i +1])
                    text.pop(i)
                    text.pop[i]
                i = i+1
    print(text)
    return text