def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        if token in "+-*/":
            # Виймаємо два останні операнди
            b = stack.pop()
            a = stack.pop()
            
            # Виконуємо операцію відповідно до оператора
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Ділимо і конвертуємо в ціле число відповідно до вимог (скоротити до нуля)
                stack.append(int(a / b))  # int() автоматично усіче в Python до цілого при діленні націло
        else:
            # Якщо це число, додаємо його до стека
            stack.append(int(token))
    
    return stack[0]  # Результат виразу залишиться як єдиний елемент у стеку

# Приклади використання
print(eval_rpn(["2", "1", "+", "3", "*"]))       # Output: 9
print(eval_rpn(["4", "13", "5", "/", "+"]))      # Output: 6
print(eval_rpn(["10", "6", "9", "3", "/", "*", "-11", "+", "*", "17", "+", "5", "+"])) # Output: 22
