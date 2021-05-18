import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.upload import VkUpload

session = vk_api.VkApi(token="86d583c440c856add6de1fcc1f91b303bbe89f80b88a60fd00d242a9ba9b269f8e0f2a81899e9d081dd00")


def send_message(user_id, message, keyboard=None, attachment = ""):
    post = {
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        "attachment": attachment
    }
    if keyboard is not None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    session.method("messages.send", post)


for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_text = event.text.lower()
        user_id = event.user_id
        if user_text == "Привет".lower():  # Старт общения с ботом
            keyboard = VkKeyboard()
            keyboard.add_button("Меню", VkKeyboardColor.PRIMARY)
            send_message(user_id, "Привет, для удобства открываю меню!", keyboard)

        elif user_text == "Меню".lower() or user_text == "В меню".lower():
            keyboard = VkKeyboard()
            buttons = ["Пекарня", "Кондитерская"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)
            send_message(user_id, "Вы в меню", keyboard)
        elif user_text == "Пекарня".lower() or user_text == "К разделам пекарни".lower():
            keyboard = VkKeyboard()
            buttons = ["Хлеб", "Булочки", "Пирожки", "В меню"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE, VkKeyboardColor.SECONDARY,
                             VkKeyboardColor.SECONDARY]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)
            send_message(user_id, "Вы в разделах пекарни!", keyboard)
        elif user_text == "Хлеб".lower():
            keyboard = VkKeyboard()
            buttons = ["Хлеб белый", "Хлеб бородинский", "Багет", "К разделам пекарни"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY,
                             VkKeyboardColor.NEGATIVE]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)
            send_message(user_id, "Выберите желаемый для просмотра товар!", keyboard)
        elif user_text == "Хлеб белый".lower():
            send_message(user_id, "Хлеб белый:\n\nЦена - 45  рублей\nОписание - Хлеб на дрожевом тесте, выпеченный с "
                                  "любовью!", keyboard=None, attachment = "photo-204613785_457239021")
        elif user_text == "Хлеб бородинский".lower():
            send_message(user_id, "Хлеб бородинский:\n\nЦена - 55  рублей\nОписание - Хлеб на бездрожевом тесте, "
                                  "выпеченный с любовью!", keyboard=None, attachment = "photo-204613785_457239020")
        elif user_text == "Багет".lower():
            send_message(user_id, "Багет:\n\nЦена - 67  рублей\nОписание - Хлеб Итальянский, "
                                  "выпеченный с любовью по особому рецепту!", keyboard=None, attachment = "photo-204613785_457239019")
        elif user_text == "Булочки".lower():
            keyboard = VkKeyboard()
            buttons = ["Булочка с маком", "Булочка с корицей", "Булочка сдобная", "К разделам пекарни"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY,
                             VkKeyboardColor.NEGATIVE]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)
            send_message(user_id, "Выберите желаемый для просмотра товар!", keyboard)
        elif user_text == "Булочка с маком".lower():
            send_message(user_id, "Булочка с маком:\n\nЦена - 26  рублей\nОписание - Булочка выпеченная по "
                                  "старонородному рецепту "
                                  "для вас!", keyboard=None, attachment = "photo-204613785_457239023")
        elif user_text == "Булочка с корицей".lower():
            send_message(user_id, "Булочка с корицей:\n\nЦена - 55  рублей\nВыпеченная по особому рецепту из Франции! "
                                  , keyboard=None, attachment = "photo-204613785_457239022")
        elif user_text == "Булочка сдобная".lower():
            send_message(user_id, "Булочка сдобная:\n\nЦена - 24  рублей\nОписание - Булочка сдобная, "
                                  "на бездрожжевом тесте, хороша к чаю!", keyboard=None, attachment = "photo-204613785_457239024")

        elif user_text == "Пирожки".lower():
            keyboard = VkKeyboard()
            buttons = ["Пирожок с мясом", "Пирожок с капустой", "Пирожок с картошкой", "К разделам пекарни"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY,
                             VkKeyboardColor.NEGATIVE]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)
            send_message(user_id, "Выберите желаемый для просмотра товар!", keyboard)
        elif user_text == "Пирожок с мясом".lower():
            send_message(user_id, "Пирожок с мясом:\n\nЦена - 44  рублей\nОписание - мясной пирожок для голодного "
                                  "студента! "
                                  , keyboard=None, attachment="photo-204613785_457239025")
        elif user_text == "Пирожок с капустой".lower():
            send_message(user_id, "Пирожок с капустой:\n\nЦена - 46  рублей\nОписание - бабушкини пирожки с капусткой!"
                                  , keyboard=None, attachment="photo-204613785_457239026")
        elif user_text == "Пирожок с картошкой".lower():
            send_message(user_id, "Пирожок с картошкой:\n\nЦена - 34  рублей\nОписание - картофель нежно обжарен с "
                                  "луком, хорошо преправлен, хорошо заходит с баночкой колы! :) "
                                  , keyboard=None, attachment="photo-204613785_457239027")
        elif user_text == "Кондитерская".lower():
            send_message(user_id, "Вы в кондитерской.")
        else:
            send_message(user_id, "Я не понимаю что вы имеете ввиду под:" + " " + user_text)
