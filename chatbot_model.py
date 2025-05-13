def get_bot_response(user_input):
    # Define a few simple responses
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine. How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "course" in user_input:
        return "We offer a variety of courses. Can you specify which one you're interested in?"
    elif "help" in user_input:
        return "I'm here to help! You can ask me about courses, your account, or anything else related to the university."
    elif "when is the exam" in user_input or "when is the exam scheduled" in user_input:
        return "The exam is scheduled for June 15th, 2025."
    elif "exam date" in user_input:
        return "The exam will be held on June 15th, 2025."
    elif "location of the exam" in user_input:
        return "The exam will be held in the main auditorium on campus."
    elif "registration deadline" in user_input:
        return "The deadline for registration is June 1st, 2025."
    elif "what is the syllabus" in user_input or "syllabus" in user_input:
        return "The syllabus for the exam covers all chapters from the semester, including the latest topics discussed in class."
    elif "how to register" in user_input or "registration process" in user_input:
        return "To register for the exam, visit the registration portal on the university website and follow the instructions."
    elif "how many questions in the exam" in user_input or "exam questions" in user_input:
        return "The exam will have 50 multiple-choice questions."
    elif "passing marks" in user_input:
        return "The passing marks for the exam are 60%."
    elif "exam format" in user_input:
        return "The exam will be online and will consist of multiple-choice questions, with a time limit of 2 hours."
    elif "exam duration" in user_input:
        return "The exam duration is 2 hours."
    elif "admission date" in user_input:
        return "The admission process starts on July 1st, 2025."
    elif "how to contact faculty" in user_input:
        return "You can contact your faculty via email or visit the faculty office during working hours."
    elif "student support" in user_input:
        return "Student support is available at the student help desk or through the online support portal."
    elif "can i reschedule the exam" in user_input:
        return "Exam rescheduling is not allowed unless there is a valid emergency. Please contact the exam office for more information."
    elif "can i get a copy of the exam" in user_input:
        return "Copies of the exam are not shared. However, you can refer to past papers available in the library."
    elif "exam center" in user_input:
        return "The exam will take place in the main auditorium on the university campus."
    elif "how to prepare for the exam" in user_input:
        return "You can prepare for the exam by reviewing your class notes, textbooks, and practicing sample papers."
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"
