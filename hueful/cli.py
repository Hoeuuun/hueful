import hueful.log
from hueful.Connection import Connection
from hueful.Group import Group
from hueful.Light import Light


def main():
    # Connection and Group
    connection = Connection(verify=False)
    groups = connection.get_all_groups()
    print(f"All groups {groups.keys()}")
    # for group in groups.items():
    #     print("group", group)

    g1 = Group(1, connection)
    g1.turn_on(True)
    g1.set_effect(False)
    g1.set_bri(50)
    # print(g1.set_effect(True))

    l2 = Light(2, connection)
    l2.turn_on(True)


if __name__ == '__main__':
    main()