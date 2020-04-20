import hueful.log
from hueful.Connection import Connection
from hueful.Group import Group


def main():
    # Connection and Group
    connection = Connection(verify=False)
    groups = connection.get_all_groups()
    print(f"All groups {groups.keys()}")
    # for group in groups.items():
    #     print("group", group)

    g1 = Group()
    # print(g1.set_effect(True))


if __name__ == '__main__':
    main()