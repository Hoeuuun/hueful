import hueful.log
from hueful.Connection import Connection
from hueful.Group import Group


def main():
    # Connection and Group
    connection = Connection(verify=False)
    groups = connection.get_all_groups()
    print(f"All groups {groups.keys}")
    for group in groups.values():
        group.turn_on(False)


if __name__ == '__main__':
    main()