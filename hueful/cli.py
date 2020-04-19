from hueful.Connection import Connection
from hueful.Group import Group


def main():
    # Connection and Group
    connection = Connection(verify=False)
    g = Group('1', connection=connection)
    g.turnLights(True)


if __name__ == '__main__':
    main()