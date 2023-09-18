def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2  # muda o valor diretamente na lista (como se passasse o ponteiro -> por referência)
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
