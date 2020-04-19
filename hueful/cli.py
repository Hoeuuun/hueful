from hueful.Connection import Connection
from hueful.Group import Group


def main():
    connection = Connection(verify=False)
    g = Group('1', connection=connection)
    g.setBri(14)


if __name__ == '__main__':
    main()