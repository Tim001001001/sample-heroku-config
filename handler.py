russianName = {"ru": "Русский язык ", "Chem": "Химия"}

teacherName = {"ru": "НЕКТО"}

lessons = [["ru", "Rus", 'Chem', 'Chem', 'Math', 'Math'],
           ["ch", "tt", 'Che', 'Che', 'Mat', 'Mat'],
           ["ru", "ru", 'hem', 'hem', 'ath', 'ath'],
           ["Rs", "Rs", 'Cm', 'Cm', 'Mh', 'Mh']
           ]


def handle_message(message, nickname="user"):
    '''handles message:
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''

    global lessons
    answer = nickname + ': '
    answer += 'Your message is ' + message
    day = int(message.split()[0])-1
    number_of_lesson = int(message.split()[1])-1
    currentLesson = lessons[day][number_of_lesson]
    answer = russianName[currentLesson] + teacherName[currentLesson]
    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
