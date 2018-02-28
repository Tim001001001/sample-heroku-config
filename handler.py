import datetime
russianName = {"ru": "Русский язык ", "Ch": "Химия", "Mat": "Математика", "Phis": "Физика"}

teacherName = {"ru": " с НЕКТО", "Ch": " c некто", "Mat": " с некто", "Phis": " с некто"}
daysofweek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
lessons = [
    ["ru", "ru", 'Ch', 'Ch', 'Mat', 'Mat'],
    ["ch", "Mat", 'Ch', 'Ch', 'Mat', 'Mat'],
    ["ru", "ru", 'hem', 'hem', 'ath', 'ath'],
    ["Rs", "Rs", 'Cm', 'Cm', 'Mh', 'Mh'],
    ["Rs", "Rs", 'Cm', 'Cm', "Mat", 'Mat']
]

time = ["9:00", "9:50", "10:40", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
weday = datetime.datetime.now()


def handle_message(message, nickname=""):

    income = message.split()
    day = income[0]

    if day == "Сегодня":
        answer = lessons[weday.weekday()]
    else:
        day = daysofweek.index(income[0])
        if int(len(income)) == 1:
            answer = lessons[day]
        else:

            number_of_lesson = int(income[1]) - 1

            currentLesson = lessons[day][number_of_lesson]

            answer = russianName[currentLesson] + teacherName[currentLesson] + " в " + time[number_of_lesson]

    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
