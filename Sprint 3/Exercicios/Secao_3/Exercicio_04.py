def is_primo(num):
   
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Itera sobre números de 1 a 100 e imprime os números primos
for número in range(1, 101):
    if is_primo(número):
        print(número)