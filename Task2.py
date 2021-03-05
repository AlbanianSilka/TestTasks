from collections import Counter


# Функция соответствует заданию - учитывает пунктуацию, выбирает три самых часто встречаемых слова и отменяется,
# если нельзя будет выбрать три случайных слова, также все слова сводятся к нижнему регистру, возможно использование
# текста как кириллического, так и латиницы
def top_duplicates(k=3):
    texted = input("Enter your text: ")
    punc_signs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in texted:
        if ele in punc_signs:
            texted = texted.replace(ele, "")

    user_list = list(texted.split(" "))
    print(user_list)
    total_count = Counter(user_list)
    num_duplicates = sum(1 for x in total_count if total_count[x] > 1)
    if num_duplicates < 3:
        return

    for i in range(len(user_list)):
        user_list[i] = user_list[i].lower()

    counter = {}
    for number in user_list:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    sorted_by_value = reversed(sorted(counter.items(), key=lambda kv: kv[1]))

    top_values = [item[0] for item in sorted_by_value][:k]
    print("Три самых повторяемых слова: ", top_values)

    return top_values


top_duplicates()
