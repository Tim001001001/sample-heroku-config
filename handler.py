lessons = [["Rus", "Rus", 'Chem', 'Chem', 'Math', 'Math'], ["Ru", "Ru", 'Che', 'Che', 'Mat', 'Mat'], ["us", "us", 'hem', 'hem', 'ath', 'ath'], ["Rs", "Rs", 'Cm', 'Cm', 'Mh', 'Mh']]


def handle_message(message, nickname="user"):
    '''handles message:
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''

    words = message.split()
    global lessons
    answer = nickname + ': '
    answer += 'Your message is ' + message
    answer = lessons[int(message.split()[0])-1][int(message.split()[1])-1]
    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
