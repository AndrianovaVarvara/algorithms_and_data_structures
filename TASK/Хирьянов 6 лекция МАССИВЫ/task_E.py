# Результаты работы студентов в семестре

N = int(input())  # количество студентов
if N > 1000:  # в этом случае выводим все простые числа
    C = [True] * (N+1)
    Primes = []
    for d in range (2, N+1):
        if C[d]:
            Primes.append(d)
            for i in range (d ** 2, N + 1, d):
                C[i]=False
    for i in Primes:  # эти три строчки - вывод на печать
        print(i, end=' ')
    exit()    # ОБЯЗАТЕЛЬНО! иначе программа пойдет дальше, а данных нема

b = []
while 1:
    m = input()
    if m == '#':  # остановка цикла по условному знаку
        break
    b.append(m)  # промежуточный спиосок со всеми данными

A = []
for i in range(N):
    A.append([i])  # даем имена студентам

for i in range(len(b)):
    y = int(b[i][:2])  # имя студента
    x = int(b[i][2:])  # оценка студента
    for i in range(0, N):
        if y == i:
            A[i].append(x)  # раскладываем каждому его оценки

for i in range(N):
    del A[i][0]  # удаляем ранее присвоенное имя
    A[i].sort(reverse=True)  # сортируем по убыванию от 10 до 1

A.sort(key=lambda x: sum(x), reverse=True)  # сортируем студентов во убыванию суммы его оценок

for i in A:  # эти три строчки - вывод на печать
    for j in i:
        print(j, end=' ')
