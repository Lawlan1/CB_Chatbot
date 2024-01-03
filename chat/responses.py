from simple_chatbot.responses import GenericRandomResponse

class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you", 
               "Hey friend. How are you? How can I help you?")
    
class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.", 
               "Thanks fo visiting",
               "See ya! Have a nice day.")
class MentalHealthAdviserResponse(GenericRandomResponse):
    choices = ("You can call me Mental Health Advisor Chatbot", 
               "People refer to me as Mental Health Advisor Chatbot",
               "My name is Mental Health Advisor Chatbot")


class StressManagementResponse(GenericRandomResponse):
    choices = (
        "It's completely normal to feel stressed. Finding healthy ways to cope, like talking to friends, family, or a counselor, can make a big difference. What activities or hobbies help you relax?",
        "Feeling stressed is a common experience. Engaging in activities you enjoy, like reading a book or going for a walk, can provide relief. What are your favorite ways to unwind?",
        "Stress is a natural part of life. Have you tried talking to someone about what's on your mind, like a friend, family member, or counselor? Also, what activities do you find calming?",
        "Dealing with stress is important, and you're not alone in feeling this way. Consider sharing your feelings with someone you trust. Additionally, what hobbies or activities bring you a sense of peace?",
        "Acknowledging stress is the first step. Talking to someone you trust and exploring activities you enjoy, such as listening to music or practicing mindfulness, can be helpful. What do you find most relaxing?",
    )

class AnxietySupportResponse(GenericRandomResponse):
    choices = (
        "It's brave of you to reach out. Anxiety is common, and seeking support is important. Have you considered talking to a trusted adult or a mental health professional about what you're going through?",
        "Acknowledging your feelings is a courageous step. Many people face anxiety, and seeking help is a positive choice. Have you thought about discussing your concerns with someone you trust or a mental health professional?",
        "Dealing with anxiety can be challenging, but reaching out for support is a strong move. Is there someone in your life, like a friend, family member, or teacher, with whom you feel comfortable sharing your feelings?",
        "Facing anxiety is a brave decision. Talking to a trusted adult or a mental health professional can provide valuable insights. Is there someone specific you feel you could confide in about your struggles?",
        "You're not alone in dealing with anxiety. Seeking support is a commendable choice. Have you explored talking to someone you trust or a mental health professional to help navigate through this?",
    )

class LonelinessSupportResponse(GenericRandomResponse):
    choices = (
        "I'm here for you. It's tough to feel alone. Consider talking to someone you trust about your feelings, whether it's a friend, family member, or teacher. You don't have to face this alone.",
        "Feeling alone is difficult, but reaching out is a positive step. You have people in your life who care about you. Have you thought about confiding in a friend, family member, or teacher about what you're going through?",
        "You're not alone in this. It's challenging to feel isolated, but there are people who care. Have you considered opening up to someone you trust, like a friend, family member, or teacher, about your feelings?",
        "Loneliness can be tough, but remember, there are people who care about you. Is there someone specific in your life you feel comfortable talking to, such as a friend, family member, or teacher?",
        "It's not easy to feel alone, but you're not on your own. Talking to someone you trust, whether it's a friend, family member, or teacher, can make a difference. Have you considered reaching out to someone for support?",
    )

class FriendSupportResponse(GenericRandomResponse):
    choices = (
        "It's great that you want to help your friend. Let them know you're there to listen without judgment. Encourage them to talk to a trusted adult or a mental health professional. Sometimes, just being there for someone can make a big difference.",
        "Supporting a friend is wonderful. Reassure them that you're ready to listen without judgment. Suggest talking to a trusted adult or a mental health professional for additional support. Your presence can have a significant impact. Have you considered having this conversation with them?",
        "Helping a friend is admirable. Let them feel your support by listening without judgment. Recommend talking to a trusted adult or a mental health professional for guidance. Sometimes, your presence alone can make a big difference. Have you thought about encouraging them to seek professional help?",
        "Your desire to help your friend is commendable. Assure them that you're there to listen without any judgment. Suggest reaching out to a trusted adult or a mental health professional for further support. Just being there for someone can be incredibly meaningful. Have you discussed this possibility with your friend?",
        "Supporting your friend is important, and your willingness to listen without judgment is valuable. Encourage them to speak with a trusted adult or a mental health professional. Sometimes, your presence alone can provide significant comfort. Have you considered discussing this with your friend?",
    )

class SeriousConcernResponse(GenericRandomResponse):
    choices = (
        "I'm really sorry to hear that. It's crucial to take this seriously. Encourage your friend to talk to a trusted adult or reach out to a helpline for advice. Your concern and support can make a positive impact.",
        "I'm sorry that your friend is going through this. Taking the situation seriously is important. Encourage them to speak with a trusted adult or contact a helpline for guidance. Your support can make a positive difference. Have you discussed these options with your friend?",
        "It's unfortunate to hear about your friend's situation. Taking it seriously is the right approach. Encourage them to talk to a trusted adult or contact a helpline for advice. Your support is crucial and can have a positive impact. Have you considered discussing this with your friend?",
        "I'm genuinely sorry to hear about your friend. Taking the situation seriously is key. Encourage them to reach out to a trusted adult or a helpline for support and advice. Your concern and support can be a positive influence. Have you talked to your friend about these options?",
        "It's concerning to hear about your friend's situation. Taking it seriously is crucial. Encourage them to speak with a trusted adult or contact a helpline for assistance. Your support and concern can make a positive impact. Have you explored these options with your friend?",
    )

class SelfConfidenceBuildingResponse(GenericRandomResponse):
    choices = (
        "Building self-confidence takes time, and it's a journey. Focus on your strengths, set realistic goals, and celebrate your achievements. If self-doubt persists, talking to a counselor or a mental health professional can provide additional guidance.",
        "Developing self-confidence is a process, and it's okay to take your time. Concentrate on your strengths, set achievable goals, and acknowledge your accomplishments. If self-doubt lingers, consider speaking with a counselor or a mental health professional for further support.",
        "It's a gradual process to build self-confidence. Identify your strengths, set practical goals, and take pride in your achievements. If self-doubt continues, seeking guidance from a counselor or a mental health professional can be beneficial. Have you considered talking to someone about it?",
        "Self-confidence grows over time, and it's normal to face challenges. Focus on your strengths, set realistic goals, and celebrate small victories. If you find that self-doubt persists, reaching out to a counselor or a mental health professional can offer valuable guidance.",
        "Building self-confidence is a journey with ups and downs. Concentrate on your strengths, set achievable goals, and recognize your successes. If self-doubt persists, consider discussing your feelings with a counselor or a mental health professional. What steps have you taken to focus on your strengths?",
    )

class OverwhelmedFeelingResponse(GenericRandomResponse):
    choices = (
        "It's okay to feel overwhelmed. Consider breaking tasks into smaller steps, practicing relaxation techniques, and reaching out to someone you trust for support. If these feelings persist, talking to a mental health professional can provide additional strategies.",
        "Feeling overwhelmed is completely normal. Try breaking tasks into smaller, manageable steps, engage in relaxation techniques, and reach out to someone you trust for support. If these feelings persist, consider seeking additional strategies from a mental health professional.",
        "It's understandable to feel overwhelmed at times. Break tasks into smaller steps, practice relaxation techniques, and reach out to someone you trust for support. If these feelings persist, seeking advice from a mental health professional can provide additional strategies.",
        "Feeling overwhelmed is a common experience. Break tasks into smaller steps, try relaxation techniques, and talk to someone you trust for support. If these feelings persist, consulting with a mental health professional can offer additional strategies. What specific tasks are causing you the most stress?",
        "Don't worry if you're feeling overwhelmed. Take tasks one step at a time, practice relaxation techniques, and lean on someone you trust for support. If these feelings persist, consider talking to a mental health professional for additional strategies. How can you prioritize your tasks to make them more manageable?",
    )

class EncourageReportingBullyingResponse(GenericRandomResponse):
    choices = (
        "Encourage reporting bullying is crucial for creating a safe environment. If you witness bullying, consider reporting it to a teacher, school counselor, or another trusted adult. Your actions can contribute to fostering a supportive atmosphere.",
        "Reporting bullying is an important step in creating a positive school environment. If you come across instances of bullying, consider reporting it to a teacher, school counselor, or a trusted adult. Your involvement can make a difference.",
        "Taking action against bullying is essential. If you see someone being bullied, encourage reporting it to a teacher, school counselor, or another trusted adult. Your support can help create a safer space for everyone.",
        "It's important to stand against bullying. If you become aware of any incidents, consider reporting them to a teacher, school counselor, or a trusted adult. Your commitment to addressing bullying contributes to a safer community.",
        "Encouraging others to report bullying is vital for fostering a safe environment. If you witness any form of bullying, prompt reporting to a teacher, school counselor, or another trusted adult is crucial. Your involvement matters.",
    )


class OopsWhatHappenedResponse(GenericRandomResponse):
    choices = (
        "Oops, what happened?",
        "I noticed something seems off. Can you share what happened?",
        "I'm here for you. What's going on?",
        "I sense something isn't right. Can you tell me what happened?",
        "I'm sorry you're going through this. What happened?",
    )

class SorryAboutExperienceResponse(GenericRandomResponse):
    choices = (
        "I am sorry about your experience, it's not a good thing to be treated that way. If you're comfortable, I'm here to listen and support. Can you explain what transpired?",
        "I'm sorry to hear about your experience. It's not okay to be treated that way. If you're comfortable, I'm here to listen and support. Can you share what happened?",
        "Sorry to hear that you went through this. If you're comfortable, I'm here to listen and offer support. Can you explain what transpired?",
        "I apologize for the situation you faced. It's not right to be treated that way. If you're comfortable, I'm here to listen. Can you share what happened?",
        "I'm sorry about your experience. It's important to talk about it. If you're comfortable, I'm here to listen and support. Can you tell me what transpired?",
    )

class SorryOnceAgainResponse(GenericRandomResponse):
    choices = (
        "Sorry once again about the situation. Is this the first time it happened? If No, how long?",
        "I'm sorry once again about the situation. Can you let me know if this is the first time it happened? If not, how long has it been going on?",
        "I apologize once again for the situation. Is this the first occurrence, or has it happened before? If it's not the first time, can you share how long it's been going on?",
        "I'm sorry to hear about the situation. Can you tell me if this is the first time, or has it happened before? If it's not the first time, how long has it been going on?",
        "Sorry once again about what happened. Can you provide some context? Is this the first time, or has it happened before? If yes, how long has it been going on?",
    )

class YouDontDeserveResponse(GenericRandomResponse):
    choices = (
        "You don't deserve such treatment; it's not your fault. Do not worry too much as everything will be alright.",
        "It's not your fault, and you don't deserve to be treated that way. Try not to worry too much; everything will be alright.",
        "You don't deserve such treatment, and it's not your fault. Don't worry too much; things will get better.",
        "You deserve better than this treatment, and it's not your fault. Try not to worry too much; everything will be alright.",
        "You shouldn't have to endure such treatment. Remember, it's not your fault, and things will get better.",
    )

class CopingStrategiesResponse(GenericRandomResponse):
    choices = (
        "To help you get through these unwanted moments, I can provide you with coping strategies that can help you manage the stress and challenges in this situation. \ni. Be assertive by being confident in expressing yourself and don't lose interest in your life goals and social life.",
        "In challenging times like these, coping strategies can make a difference. Here are some suggestions to help you navigate through these moments: \nii. You can talk to trusted friends or family for further support.",
        "I understand these are tough moments. Here are some coping strategies to help you manage stress and challenges in this situation: \niii. Access resources provided on this platform by clicking on the provided link to read or download. This will help you navigate through these moments.",
        "Coping with difficult situations can be challenging. Here are some strategies to help you navigate through these moments: \niv. You can report about bullying to either National Bullying Helpline (NBH). Tel: 08452255785 Helpline: 03003230169 \nhttps://www.nationalbullyinghelpline.co.uk/contact.html",
        "Dealing with stress is tough, but here are some coping strategies that may help you manage challenges in this situation: \niv. You can report about bullying to either National Bullying Helpline (NBH). Tel: 08452255785 Helpline: 03003230169 \nhttps://www.nationalbullyinghelpline.co.uk/contact.html",
    )


class YesYouCanResponse(GenericRandomResponse):
    choices = (
        "Yes, you can. Feel free, as I'm here to help you.",
        "Absolutely, you can. Feel free to share, and I'm here to assist you.",
        "Certainly, you can. Feel free to open up, and I'm here to support you.",
        "Of course, you can. Don't hesitate to share, and I'm here to help.",
        "Yes, you can. Feel free to express yourself, and I'm here to assist you.",
    )

class BullyingFactorsResponse(GenericRandomResponse):
    choices = (
        "There are many factors behind bullying such as looking for power and control over the powerless, imitating behavior of others, seeking attention to be relevant, peer pressure, feeling jealous of others, and many more.",
        "Bullying can have various factors, including looking for power and control, imitating others, seeking attention, peer pressure, feeling jealous, and more.",
        "The motivations behind bullying can vary, including factors like seeking power, imitating others, seeking attention, peer pressure, feeling jealous, and many more.",
        "Understanding the factors behind bullying is complex. It can include seeking power and control, imitating others, seeking attention, peer pressure, feeling jealous, and more.",
        "There are multiple factors contributing to bullying, such as looking for power and control, imitating behavior, seeking attention, peer pressure, feeling jealous, and many others.",
    )



