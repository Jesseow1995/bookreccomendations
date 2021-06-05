import heapq


def main():
    # n = input("Please enter number of friends: ")
    n = 2
    recommended_file = open('recommendations.txt', 'w')
    for name in sorted(rating_data.keys()):
        recommended_file.write((name + ': [\'' + '\', \''.join(sorted(friends(name, n))) + '\']\n'))
        for book in sorted(recommend(name, n)):
            recommended_file.write(('\t' + "(\'" + '\', \"'.join(book) + '\")\n'))
    recommended_file.close()


def dotprod(x, y):
    x = [int(i) for i in x.strip().split(' ')]
    y = [int(i) for i in y.strip().split(' ')]
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return total


file_name = "booklist.txt"
book_file = open(file_name, 'r')
book_list = []

for line in book_file:
    book_tuple = tuple(line.strip().split(','))
    book_list.append(book_tuple)

rating_file_name = 'ratings.txt'
rating_file = open(rating_file_name, 'r')
rating_file_lines = rating_file.readlines()
rating_data = {}
for i in range(0, len(rating_file_lines), 2):
    if (i + 1) >= len(rating_file_lines):
        break
    rating_data[rating_file_lines[i].strip().lower()] = rating_file_lines[i + 1].strip()
sim_score = {}
for name1 in rating_data:
    temp_dict = {}
    for name2 in rating_data:
        if name1 == name2:
            continue
        temp_dict[name2] = dotprod(rating_data[name1], rating_data[name2])
    sim_score[name1] = temp_dict


def friends(name, n=2):
    friend_list = heapq.nlargest(int(n), sim_score[name], key=sim_score[name].get)
    friends_return = []
    for item in friend_list:
        friends_return.append(item)
    return friends_return


def recommend(name, n=2):
    sim_friends = friends(name, n)
    recommend_return = []
    i = 0
    for rating in rating_data[name].split(' '):
        if rating == '0':
            for f in sim_friends:
                if int(rating_data[f].split(' ')[i]) >= 3:
                    recommend_return.append(book_list[i])
                    break
        i += 1
        if i > len(book_list):
            break
    return recommend_return


main()
