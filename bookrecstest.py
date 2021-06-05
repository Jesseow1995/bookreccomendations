from heapq import nlargest

# Reads the book data into tuples
bookFile = open("booklist.txt", "r")
books = []

count = len(open("booklist.txt").readlines())
for i in range(count):
    bookRead = tuple(bookFile.readline().strip().split(","))
    books.append(bookRead)

    

# Dot Product Function
def dotprod(x, y):
    x = [int(i) for i in x.strip().split(' ')]
    y = [int(i) for i in y.strip().split(' ')]
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return (total)
# Read the ratings.txt file into a list
reviewers = []
rating = {}

ratingFile = open('ratings.txt', 'r')
count2 = ratingFile.readlines()

i = 0
for i in range(0, len(count2), 2):
    if (i + 1) >= len(count2):
        break
    rating[count2[i].strip().lower()] = count2[i + 1].strip()
sim_score = {}
for name1 in rating:
    temp_dict = {}
    for name2 in rating:
        if name1 == name2:
            continue
    temp_dict[name2] = dotprod(rating[name1], rating[name2])
    sim_score[name1] = temp_dict


def friends():



# Creats the recommendation text file
recommendedBooks = open('recommendations.txt', 'w')



