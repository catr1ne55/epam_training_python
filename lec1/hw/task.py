num_students = int(input("Введите количество студентов на курсе > "))
num_tasks = int(input("Введите количество заданий на курсе > "))
students = {}

for i in range(num_students):
    name = input("Введите имя студента > ")
    scores = []
    scores_sum = 0
    for j in range(num_tasks):
        score = int(input("Введите оценку студента от 0 до 10 > "))
        scores_sum += score
        scores.append(score)
    students.setdefault((name, scores_sum), scores)

all_scores = zip(*students.values())
all_scores_sums = []
for i in all_scores:
    all_scores_sums.append(sum(i))
all_scores_sums = zip(range(1, num_tasks + 1), all_scores_sums)

top3_st = sorted(students.keys(), key=lambda x: x[1], reverse=True)[:3]
print("TOP-3 студентов:")
for i in top3_st:
    print(i[0])

top3_tsk = sorted(all_scores_sums, key=lambda x: x[1])[:3]
print("TOP-3 сложных заданий:")
for i in top3_tsk:
    print("№" + str(i[0]))
