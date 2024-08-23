# mylist = ['Gabriel', 45, 637.89, True, False]
# mylists = ['Adrian', 'Ando', 23, 9833.830, False, mylist]
#
# print(mylist, end='\n\n')
#
# for i in mylist:
#     print(i, end=' ')
#     print(type(i))
#
# print()
#
# print(mylists, end='\n\n')
#
# for i in mylists:
#     print(i, end=' ')
#     print(type(i))
#     if mylists.index(i) == 5:
#         for j in i:
#             print(j, end=' ')
#             print(type(j))

klasse = [['Gabriel', 13],
          ['Ando', 13],
          ['Adrian', 13],
          ['Martin', 50]]

for person in klasse:
    for i in person:
        print(i)
    print()
