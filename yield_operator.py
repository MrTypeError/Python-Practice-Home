'''
Topic Covered :-
1)yield 
2)yield from
'''


def get_authorised_clients():
    i = 0
    yield "John"
    i += 1
    yield "Bob"
    i += 1
    yield "David"
    print("i am not yet reading")
    i += 1
    print(i)


def get_admins():
    yield "Anton"
    yield "Daniel"


def get_all_users():
    yield from get_authorised_clients()
    # yield authorised_client
    # yield from get_admins()
    # yield admin


for i in get_authorised_clients():
    print(i)

# # a = get_authorised_clients()

# # print(next(a))
# # print(next(a))

# # print(next(get_authorised_clients()))
# # print(next(get_authorised_clients()))

# g = get_all_users()

# print(next(g))
# print(next(g))
# print("1111")
# print(next(g))
# print("21212121")
# print(next(g))
# # print(next(g))
# # print(next(g))

# # print(next(get_all_users()))
# print("a")
