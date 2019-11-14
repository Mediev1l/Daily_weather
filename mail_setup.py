import sys
from forecast import mail_list


def save(new_list):
    with open('forecast/mail_list.py', 'w') as file:
        file.truncate(0)
        file.write(f"mails = {new_list}")


if __name__ == '__main__':

    mails = mail_list.mails

    try:
        if sys.argv[1] == 'list':
            if len(mails) > 0:
                for mail in mails:
                    print(mail, end=' ')
            else:
                print('Subscription list is empty')

        elif sys.argv[1] == 'add':
            for args in sys.argv[2:]:
                if args not in mails:
                    mails.append(args)
                    print('email " {} " has been added to the subscription list'.format(args))
            save(mails)

        elif sys.argv[1] == 'del':
            for args in sys.argv[2:]:
                if args not in mails:
                    raise KeyError(args)
            for args in sys.argv[2:]:
                mails.remove(args)
                print('email " {} " has been deleted from the subscription list'.format(args))
                save(mails)

        elif sys.argv[1] == 'clear':
            if len(mails) > 0:
                mails.clear()
                print('Subscription list has been cleared')
                save(mails)
            else:
                print('Subscription list is empty')

        elif sys.argv[1] == 'help':
            print("Script arguments:\n"
            "list -  mails with a subscription\n"
            "add - add an email's to the subscription list\n"
            "del - delete email's from the subscription list\n"
            "clear - clear all email's from the subscription list")

    except ValueError:
        print("Invalid argument")
    except IndexError:
        print('No argument given, use help argument to see possible actions')
    except KeyError as value:
        print('There is no mail such as " {} " in a subscription list'.format(value.args[0]))
