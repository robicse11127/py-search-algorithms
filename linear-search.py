# Linear search
def search( items, n ):
    for index, item in enumerate( items ):
        if item == n:
            return print( "Found @ position ", index )


items = [5, 8, 9, 2, 5, 6, 0, 3]
n = 9
search( items, n )

# With while loop

#
# def search_with_while(items, n):
#     i = 0
#     while i < len(items):
#         if n == items[i]:
#             return print("Found @ position ", i)
#         i = i + 1
#
#
# items = [5, 8, 9, 2, 4, 6, 0, 3]
# n = 4
# search_with_while(items, n)