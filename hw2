from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    ERR = 2
    END = 3
    EXIT = auto()
    PROMPT2 = 4
    Ending = auto()
    # These are for the first response
    First_feeling_positive = auto()
    First_feeling_negative = auto()
    Catch_feeling_positive = auto()
    Catch_feeling_negative = auto()
    First_feeling_good = auto()

    # Positivity Tree
    First_positive_prompt = auto()

    # Negative Tree
    First_negative_prompt = auto()
    First_negative_response = auto()
    U2A = auto()
    U2B = auto()

    # 3rd
    P3 = auto()
    P3B = auto()
    U3A = auto()
    ERR2 = auto()

    ANGER1 = auto()
    ANGER2 = auto()
    QUESTION1 = auto()
    QUESTION2 = auto()
    PERSON = auto()
    ACTIVITY = auto()
    INEVITABLE = auto()
    AVOIDABLE = auto()
    IDENTIFYPERSON = auto()
    IDENTIFYACTIVITY = auto()
    INEVDESCRIP = auto()
    AVOIDDESCRIP = auto()
    TRIED = auto()
    NOTTRIED = auto()
    FRIEND = auto()
    FAMILY = auto()
    INEVITABLERESPYES = auto()
    INEVITABLERESPNO = auto()
    AVOIDABLERESPCONTROL = auto()
    AVOIDABLERESPINABILITY = auto()
    CHECKIN = auto()
    CHECKIN1 = auto()
    CHECKIN2 = auto()
    CHECKIN3 = auto()
    CHECKIN4 = auto()
    CHECKINRESP = auto()
    CHECKINRESP1 = auto()
    CHECKINRESP2 = auto()
    CHECKINRESP3 = auto()
    CHECKINRESP4 = auto()
    ERRANG = auto()
    ERRANG1 = auto()
    ERRANG2 = auto()
    ERRANG3 = auto()
    ERRANG4 = auto()
    ERRANG5 = auto()

    # DEPRESSION
    P4CD = auto()
    P4C = auto()
    P4C1 = auto()
    U4C1 = auto()
    U4C2 = auto()
    U4C3 = auto()
    U4C4 = auto()
    U4C5 = auto()
    P4C1A = auto()
    P4C1Asecond = auto()
    P4C2B = auto()
    P4C3C = auto()
    P4C4D = auto()
    P4C4E = auto()
    U4C4E1 = auto()
    U4C4D2 = auto()
    U4C4D1 = auto()
    U4C4D1A1 = auto()
    P4C4D2A = auto()
    P4C4D1A = auto()
    P4C4E1A = auto()
    P4C2B1A = auto()
    P4C2B2A = auto()
    U4C4E1A1 = auto()
    U4C4D1A2 = auto()
    U4C4E1A2 = auto()
    P4C4E1A1A = auto()
    U4C4E1A1A = auto()
    U4C4E1A1B = auto()
    U4C4D2A1 = auto()
    U4C2B1 = auto()
    U4C2B2 = auto()
    U4C2B3 = auto()
    U4C2B4 = auto()
    P4C2B4A = auto()
    U4C2B2A3 = auto()
    U4C2B2A2 = auto()
    U4C2B2A1 = auto()
    U4C2B1A2 = auto()
    U4C2B1A1 = auto()
    P4C2B1A1A = auto()
    P4C4E1A2A = auto()
    U4C4E1A2A1 = auto()
    U4C4E1A2A2 = auto()
    P4C2B2A3A = auto()
    P4C4D1A1A = auto()
    P4C2B2A1A = auto()
    P4C2B1A2A = auto()
    U4C2B1A1A1 = auto()
    P4C2B1A1A1A = auto()
    U4C2B1A1A1A1 = auto()
    U4C2B1A1A1A2 = auto()
    U4C2B2A1A1 = auto()
    U4C4D1A1A1 = auto()
    P4C4D1A2A = auto()
    U4C4D1A2A2 = auto()
    U4C4D1A2A1 = auto()
    U4C2B1A2A1 = auto()
    U4C2B1A2A2 = auto()
    P4C2B1A2A1A = auto()
    U4C2B1A2A1A1 = auto()
    U4C2B1A2A1A2 = auto()
    P4C4D1A1A1A = auto()
    P4C2B1A2A2A = auto()
    P4C2B2A1A1A = auto()
    U4C4D1A1A1A1 = auto()
    U4C2B2A1A1A2 = auto()
    U4C2B2A1A1A1 = auto()
    U4C2B1A2A2A1 = auto()
    P4C2B2A1A1A1A = auto()
    U4C2B2A1A1A1A1 = auto()
    U4C2B2A1A1A1A2 = auto()
    U4C2B2A1A1A2A1 = auto()
    P4C2B2A1A1A2A = auto()
    U4C2B2A1A1A2A2 = auto()
    P4C4D1A1A1A1A = auto()
    P4CE = auto()
    P4CERR = auto()
    P4CERR2 = auto()
    P4CERR3 = auto()
    P4CERR4 = auto()
    P4CERR5 = auto()
    P4CERR6 = auto()
    P4CERR7 = auto()
    P4CERR8 = auto()
    P4CERR9 = auto()
    P4CERR10 = auto()
    P4CERR11 = auto()
    P4CERR12 = auto()
    P4CERR13 = auto()
    P4CERR14 = auto()
    P4CERR15 = auto()
    P4CERR16 = auto()
    P4CERR17 = auto()
    P4CERR18 = auto()
    P4CERR19 = auto()
    P4CERR20 = auto()
    P4CERR21 = auto()

    P4D = auto()
    U4D1 = auto()
    P4D1 = auto()

    # eating
    P4E = auto()
    U4E1 = auto()
    U4E2 = auto()
    P4E1A = auto()
    P4E2A = auto()
    U4E1A2 = auto()
    U4E1A1 = auto()
    U4E2A1 = auto()
    U4E2A2 = auto()
    P4E1A2A = auto()
    P4E1A2B = auto()
    P4E2A1A = auto()
    P4E2A2A = auto()
    U4E1A2B1 = auto()
    U4E2A1A1 = auto()
    U4E2A1A2 = auto()
    U4E2A2A1 = auto()
    U4E2A2A2 = auto()
    U4E2A2A1A1 = auto()
    P4E2A2A1A = auto()
    P4E2A2A2A = auto()
    U4EA = auto()
    P4EERR = auto()
    P4E1AERR = auto()
    P4E1A2AERR = auto()
    P4E1A2BERR = auto()
    P4E2AERR = auto()
    P4E2A1AERR = auto()
    P4E2A2AERR = auto()
    P4E2A2A2AERR = auto()

    # Yuewu Zhou ######################################################################################################
    # confrontation branch ###################################################################

    # Confrontation prompt
    confrontation_prompt = auto()
    # A: We had an argument/fight
    confrontation_answer = auto()

    # - How did it start?
    confrontation_cause_prompt = auto()

    # - A: Other person / self / don't know (don't know leads to improvement branch)
    confrontation_cause_answer = auto()
    confrontation_cause_self = auto()
    confrontation_cause_other = auto()
    confrontation_cause_dontknow = auto()
    confrontation_cause_error = auto()

    # -- Do you think it was intentional?
    confrontation_intentional_yn = auto()

    # -- Yes / No
    confrontation_intentional_answer = auto()

    # --- Why do you think they said that?
    confrontation_intentional_motive_prompt = auto()

    # --- A: Positive / negative sentiment
    confrontation_intentional_motive_answer = auto()

    # ---- Is it justified to argue because (reason) ?
    confrontation_intentional_motive_yn = auto()

    # ---- TO DO: Handle positive vs negative answers

    # -- Is this something that usually happens?
    confrontation_usual_prompt = auto()

    # -- A: Yes / No (Yes leads to advice branch)
    confrontation_usual_yn = auto()

    # --- When was the last time this has happened?
    confrontation_usual_when = auto()

    # --- A: time
    confrontation_usual_when_answer = auto()

    # ---- Have you met with (pronoun) since (time) where you haven't had a (confrontation)?
    confrontation_usual_when_yn = auto()

    # caught self & other branch ###################################################################
    # A: I (catch verb)
    confrontation_self_answer = auto()

    # - How do you think that made them feel?
    confrontation_self_feel_prompt = auto()

    # - A: good / bad
    confrontation_self_feel_answer = auto()

    # -- What do you think could have gone better?
    confrontation_self_improvement_prompt = auto()

    # -- A: verbs (could have) / I don't know or nothing
    confrontation_self_improvement_answer = auto()

    # --- That's sounds great! / Interesting. / I think that would work! Anything else?
    confrontation_self_improvement_yn = auto()

    # --- A: Yes / No (yes returns to confrontation_self_improvement_yn, no transitions to advice)
    confrontation_self_improvement_yn_answer = auto()

    # A: He/She/They (catch verb)
    confrontation_other_answer = auto()

    # - Why do you think they (caught verb) (transitions to intentionality in argument branch)
    confrontation_other_why_prompt = auto()

    # no catch branch ###################################################################
    # A: (no catch)
    confrontation_noCatch_answer = auto()

    # - Was it something that you did?
    confrontation_noCatch_self_prompt = auto()

    # - A: Yes / No (yes leads to self branch)
    confrontation_noCatch_self_answer = auto()

    # -- Was it something that someone else did?
    confrontation_noCatch_other_prompt = auto()

    # -- A: Yes / No (yes leads to other branch branch)
    confrontation_noCatch_other_answer = auto()

    # advice branch ###################################################################
    # Could I offer you some advice?
    confrontation_advice_yn = auto()

    # A: Yes / No (no ends the conversation)
    confrontation_advice_yn_answer = auto()

    # - Would a calmer attitude have helped the situation?
    confrontation_advice_calmer_yn = auto()

    # - A: Yes / No / Maybe (no transitions to other treatment)
    confrontation_advice_calmer_answer = auto()

    # -- Here are some techniques to calm yourself down
    # TO DO: offer advice to calm down

    # usual branch ###################################################################
    # Why do you spend time with this person?
    confrontation_exposure_prompt = auto()

    # because ...
    confrontation_exposure_answer = auto()

    # Will you keep spending time with them?
    confrontation_exposure_why = auto()

    # Yes / No
    confrontation_exposure_yn = auto()

    # Is it maybe a good idea to spend some time away from them and cool off?
    confrontation_exposure_end = auto()

    # treatment branch ###################################################################
    # Still researching treatments, placeholder for advice
    confrontation_treatment_placeholder = auto()

    # END
    ENDwGREET = auto()

    ############# END Confrontation #####################

# TODO: create the ontology as needed
ontology = {
    "ontology": {
        "ontP4C":
            [
                "ontschool",
                "onttired",
                "ontfunclub",
                "ontbadclub",
                "ontsad",
                "ontfamily",
                "ontdunno",
                "ontclubs",
                "ontwork",
                "ontunsure",
                "onthotline",
                "onteating",
                "onteatingtoolittle",
                "onteatingtoomuch"
            ],
        "onteating":
            [
                "eat",
                "eating"
                "food",
                "nutrition",
                "vitamins",
                "calorie",
                "calories"
                "hungry",
                "binge"
                "binge-eating"
                "eating"
            ],
        "onteatingtoolittle":
            [
                "little",
                "enough",
                "hungry",
                "malnourished",
                "nourished"
            ],
        "onteatingtoomuch":
            [
                "lot",
                "indulge",
                "binge",
                "binging",
                "binge-eating",
                "too",
                "much",
                "bad",
                "overeat",
                "overeating",
                "over-eating"
            ],
        "onthotline":
            [
                "die",
                "kill",
                "murder",
                "commit",
                "suicide"
            ],
        "ontunsure":
            [
                "unsure",
                "dunno",
                "uncertain",
                "not",
                "idk",
                "don't",
                "know",
                "Unsure",
                "Dunno",
                "IDK"
            ],
        "ontwork":
            [
                "work",
                "job",
                "money",
                "pay",
                "income",
                "Work",
                "Job",
                "Money",
                "Pay",
                "Income"
            ],
        "ontclubs":
            [
                "club",
                "Club",
                "sport",
                "Sport",
                "team",
                "Team",
                "group",
                "Group",
                "extracurricular",
                "Extracurricular",
                "activity",
                "Activity"
            ],
        "ontdunno":
            [
                "know",
                "no",
                "idk",
                "dunno",
                "reason",
                "just",
                "not",
                "sure",
                "Dunno",
                "IDK",
                "Idk",
                "Dunno"
            ],
        "ontfamily":
            [
                "family",
                "parent",
                "sister",
                "brother",
                "kid",
                "child",
                "sibling",
                "cousin",
                "dad",
                "mom",
                "father",
                "mother",
                "Parent",
                "Family",
                "PARENTS",
                "cousin",
                "uncle",
                "nephew",
                "aunt",
                "grandparents",
                "grandma",
                "grandpa",
                "grandmother",
                "grandfather"
            ],
        "ontsad":
            [
                "sad",
                "down",
                "unhappy",
                "depressed",
                "depressing",
                "lost",
                "purposeless"
                "blue",
                "dumps",
                "gross",
                "Sad",
                "Down",
                "Unhappy",
                "Depressed",
                "Blue",
                "Dumps",
                "Gross",
                "bad",
                "Bad"
            ],
        "ontbadclub":
            [
                "resume",
                "looks",
                "appears",
                "not",
                "dunno",
                "don't",
                "Dunno",
                "IDK",
                "idk",
                "Resume",
                "Idk"
            ],
        "ontfunclub":
            [
                "fun",
                "enjoy",
                "destress",
                "relaxing",
                "entertaining",
                "socializing",
                "friends",
                "entertain",
                "relax",
                "people",
                "social",
                "friend",
                "Fun",
                "great",
                "Destress",
                "Friend",
                "Relax",
                "Entertain",
                "Enjoy"
            ],
        "onttired":
            [
                "hours",
                "tired",
                "fatigue",
                "fatigued",
                "sleeping",
                "exhausted",
                "sleep",
                "too",
                "exhaust",
                "Hours",
                "Tired",
                "Fatigue",
                "Sleep",
                "Too",
                "Exhaust"
            ],
        "ontschool":
            [
                "grades",
                "midterm",
                "final",
                "college",
                "exam",
                "school",
                "class",
                "test",
                "course",
                "balance",
                "balancing"
                "Grades",
                "Midterm",
                "Final",
                "College",
                "Exam",
                "Test",
                "study",
                "Study",
                "course",
                "studying",
                "Course"
            ],
        "ontemotion":
            [
                "ontnegative",
                "onpositive",
                "ontneutral",
                "ontunexpected"
            ],
        "ontnegative":
            [
                "anger",
                "disgust",
                "sadness",
                "fear",
                "bad",
                "Bad",
                "scared",
                "scare",
                "scary",
                "onttired",
                "ontschool",
                "ontsad",
                "ontfamily",
                "ontdunno",
                "ontwork",
                "ontunsure"
            ],
        "ontpositive":
            [
                "happiness",
                "happy",
                "Happy",
                "joy",
                "Joy",
                "love",
                "Love",
                "great",
                "Great",
                "euphoria",
                "Euphoria",
                "super",
                "Super",
                "best",
                "Best",
                "amazing",
                "amaze",
                "amazed",
                "gold",
                "Gold",
                "luck",
                "Luck",
                "good",
                "Good"
            ],
        "ontneutral":
            [
                "good",
                "ok",
                "fine",
                "okay",
                "neutral",
                "Good",
                "Ok",
                "OK",
                "Okay",
                "OKAY",
                "Neutral"
            ],
        "ontunexpected":
            [
                "fear",
                "Fear",
                "surprise",
                "Surprise",
                "startle",
                "jumped",
                "startled",
                "Jump",
                "jump"
            ],
        "ontperception":
            [
                "control",
                "Control",
                "inability",
                "Inability",
                "unable",
                "Unable",
                "can't",
                "cant",
                "Can't",
                "Cant",
                "powerless",
                "Powerless",
                "lack"
                "Lack"
            ],
        "ontaffirm":
            [
                "yes",
                "Yes",
                "YES",
                "yea",
                "YEA",
                "Yea",
                "yeah",
                "Yeah",
                "YEAH",
                "Yep",
                "YEP",
                "yep",
                "mhm",
                "mmhmm",
                "mmhm",
                "mhmm",
                "okay",
                "ok",
                "OK",
                "Ok",
                "Okay"
            ],
        "ontnegate":
            [
                "no",
                "nah",
                "nope",
                "No",
                "NO",
                "Nah",
                "NAH",
                "Nope",
                "NOPE",
                "na",
                "Na",
                "nah"
            ],
        "ontbecause":
            [
                "because",
                "since"
            ],
        ########## confrontation branch ontologies ##############
        "ontconfrontation":
            [
                "argument",
                "fight",
                "dispute",
                "yelling",
                "screaming",
                "confrontation"
            ]
    }
}
knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, how are you feeling today?"')

# The first user response feeling
df.add_user_transition(State.PROMPT, State.First_feeling_positive, '[$positive=#ONT(ontpositive)]')
df.add_user_transition(State.PROMPT, State.First_feeling_negative, '[$negative=#ONT(ontnegative)]')
df.set_error_successor(State.PROMPT, State.ERR)
# df.set_error_successor(State.First_feeling_positive, State.ERR2)
# df.set_error_successor(State.First_feeling_negative, State.ERR2)


# Feeling Positive
df.add_system_transition(State.First_feeling_positive, State.First_positive_prompt,
                         '"That\'s great, good luck on the rest of life!"')
df.add_user_transition(State.First_positive_prompt, State.END, "/.*/")

# Feeling Negative
df.add_system_transition(State.First_feeling_negative, State.First_negative_prompt,
                         '[!"What\'s been making you feel"$negative"?"]')
# df.add_user_transition(State.x, State.U2B, '[$conju=#ONT(ontbecause)]')
# df.set_error_successor(State.First_negative_prompt, State.ERR2)

####### Move to confrontation branch ##########################
df.add_user_transition(State.First_negative_prompt,State.confrontation_answer,'[$confrontation=#ONT(ontconfrontation)]')
######################################################################

# U2B
df.add_system_transition(State.U2B, State.P3, '"Can you tell me more about how you\'re feeling?"')
df.set_error_successor(State.U2B, State.ERR2)

# U2A
df.add_system_transition(State.First_negative_prompt, State.P3, '"Why is that?"')
df.set_error_successor(State.First_negative_prompt, State.ERR2)

# P3
df.set_error_successor(State.P3, State.ERR2)

# Intro Errors
df.add_system_transition(State.ERR2, State.PROMPT2,
                         '"I didn\'t catch that, could you tell me more about how you are feeling?"')
df.add_user_transition(State.PROMPT2, State.First_feeling_positive, '[$positive=#ONT(ontpositive)]')
df.add_user_transition(State.PROMPT2, State.First_feeling_negative, '[$negative=#ONT(ontnegative)]')
df.set_error_successor(State.PROMPT2, State.ERR)
df.set_error_successor(State.First_feeling_positive, State.ERR)
df.set_error_successor(State.First_feeling_negative, State.ERR)

# Ending
df.add_system_transition(State.ERR, State.EXIT, '"I don\'t understand, Goodbye!"')
df.add_system_transition(State.END, State.EXIT, '"Goodbye! Thank you for talking to me today!"')
#df.set_error_successor(State.END, State.END)

# ANGER

df.add_system_transition(State.ANGER1, State.QUESTION1,
                         '"Is there a particular person/ activity that comes to mind that may cause you anger? "')
df.add_system_transition(State.ANGER2, State.QUESTION2,
                         '"Do you think getting angry was or was not inevitable? If it was not inevitable, how do you think it could have been avoided or not avoided?"')

# 4 POSSIBLE BRANCHES DEPENDING ON USER RESPONSE

df.add_user_transition(State.QUESTION1, State.PERSON, '[$person=#NER(person)]')
df.add_user_transition(State.QUESTION1, State.ACTIVITY, '[$activity=#POS(noun,verb)]')
df.add_user_transition(State.QUESTION2, State.INEVITABLE, r"[/(.*)((inevitable) | (was inevitable))(.*)/]")
df.add_user_transition(State.QUESTION2, State.AVOIDABLE, r"[/(.*)((not inevitable) | (avoidable))(.*)/]")
####### Move to confrontation branch ##########################
df.add_user_transition(State.QUESTION1,State.confrontation_answer,'[$confrontation=#ONT(ontconfrontation)]')
######################################################################

# D5 TRANSITIONS
df.add_system_transition(State.PERSON, State.IDENTIFYPERSON,
                         '[!"Thank you for telling me about your hard time dealing with that " $person ". \n Have you tried or not tried resolving this issue directly with the " $person "? \n Please feel free to tell me exactly how you went about fixing this relationship if you have already tried."]')
df.add_system_transition(State.ACTIVITY, State.IDENTIFYACTIVITY,
                         '[!"Thank you for telling me about your difficult time engaging with that " $activity ". \n Have you tried talking to your friends or family about this activity? \n Let me know explicitly whether you spoke to either your friends or family."]')
df.add_system_transition(State.INEVITABLE, State.INEVDESCRIP,
                         '"Would you say that your anger partly stems from the lack of control over your situation?"')
df.add_system_transition(State.AVOIDABLE, State.AVOIDDESCRIP,
                         '"Did you feel inability or control over trying to avoid the situation"')

# U5 TRANSITIONS
df.add_user_transition(State.IDENTIFYPERSON, State.TRIED, r"[/(.*)((tried))(.*)/]")
df.add_user_transition(State.IDENTIFYPERSON, State.NOTTRIED, r"[/(.*)((not tried))(.*)/]")
df.add_user_transition(State.IDENTIFYACTIVITY, State.FRIEND, r"[/(.*)((friend) | (friends) | (best friend))(.*)/]")
df.add_user_transition(State.IDENTIFYACTIVITY, State.FAMILY,
                       r"[/(.*)((mom) | (mother) | (dad) | (father) | (brother) | (sister) | (cousin) | (uncle) | (aunt) | (family))(.*)/]")
df.add_user_transition(State.INEVDESCRIP, State.INEVITABLERESPYES, "$yes=#ONT(ontaffirm)")
df.add_user_transition(State.INEVDESCRIP, State.INEVITABLERESPNO, "$no=#ONT(ontnegate)")
df.add_user_transition(State.AVOIDDESCRIP, State.AVOIDABLERESPCONTROL, "$control=#ONT(ontcontrol)")
df.add_user_transition(State.AVOIDDESCRIP, State.AVOIDABLERESPINABILITY, "$inability=#ONT(ontinability)")

# P6 TRANSITIONS
df.add_system_transition(State.TRIED, State.CHECKIN,
                         '"I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.NOTTRIED, State.CHECKIN,
                         '"I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.FRIEND, State.CHECKIN,
                         '"I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.FAMILY, State.CHECKIN,
                         '"I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.INEVITABLERESPYES, State.CHECKIN1,
                         '"$yes. I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.INEVITABLERESPNO, State.CHECKIN2,
                         '"$no. I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.AVOIDABLERESPCONTROL, State.CHECKIN3,
                         '"$control. I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')
df.add_system_transition(State.AVOIDABLERESPINABILITY, State.CHECKIN4,
                         '"$inability. I see. Well, I\'d say now is a great time for a quick break. In one word, could you tell me how you are feeling at this moment? "')

# U6 TRANSITIONS(SENTIMENT ANALYZER WILL BE USED FOR THIS SECTION EVENTUALLY)
df.add_user_transition(State.CHECKIN, State.CHECKINRESP, '[$checkin=POS(adjective)]')
df.add_user_transition(State.CHECKIN1, State.CHECKINRESP1, '[$checkin1=POS(adjective)]')
df.add_user_transition(State.CHECKIN2, State.CHECKINRESP2, '[$checkin2=POS(adjective)]')
df.add_user_transition(State.CHECKIN3, State.CHECKINRESP3, '[$checkin3=POS(adjective)]')
df.add_user_transition(State.CHECKIN4, State.CHECKINRESP4, '[$checkin4=POS(adjective)]')

# ERROR SYSTEM TRANSITIONS
df.add_system_transition(State.ERRANG, State.ERRANG, r"[!I don't know that person.]")
df.add_system_transition(State.ERRANG1, State.ERRANG1, r"[!I've never heard of that activity.]")
df.add_system_transition(State.ERRANG2, State.ERRANG2, r"[!I've not heard of that type of friend.]")
df.add_system_transition(State.ERRANG3, State.ERRANG3, r"[!I've not heard of that type of family member.]")
# USE THE BELOW ERROR STATE FOR THE INEVITABLE/AVOIDABLE BRANCHES
df.add_system_transition(State.ERRANG4, State.ERRANG4, r"[!I don't understand.]")
df.add_system_transition(State.ERRANG5, State.ERRANG5, r"[!I have not heard of that feeling.]")

# ERROR SUCCESSOR STATES
df.set_error_successor(State.PERSON, State.ERRANG)
df.set_error_successor(State.ACTIVITY, State.ERRANG1)
df.set_error_successor(State.FRIEND, State.ERRANG2)
df.set_error_successor(State.FAMILY, State.ERRANG3)
df.set_error_successor(State.INEVITABLERESPYES, State.ERRANG4)
df.set_error_successor(State.INEVITABLERESPNO, State.ERRANG4)
df.set_error_successor(State.AVOIDABLERESPCONTROL, State.ERRANG4)
df.set_error_successor(State.AVOIDABLERESPINABILITY, State.ERRANG4)

df.set_error_successor(State.CHECKINRESP, State.ERRANG5)
df.set_error_successor(State.CHECKINRESP1, State.ERRANG5)
df.set_error_successor(State.CHECKINRESP2, State.ERRANG5)
df.set_error_successor(State.CHECKINRESP3, State.ERRANG5)
df.set_error_successor(State.CHECKINRESP4, State.ERRANG5)

# P7 TRANSITIONS(CONTINUED DURING/AFTER SPRING BREAK)

# angela's stuff
####################################################################################

df.add_user_transition(State.First_negative_prompt, State.U4C1, "[$response=#ONT(ontschool)]")
df.add_user_transition(State.First_negative_prompt, State.U4C2, "[$response=#ONT(ontfamily)]")
df.add_user_transition(State.First_negative_prompt, State.U4C3, "[$response=#ONT(ontdunno)]")
df.add_user_transition(State.First_negative_prompt, State.U4C4, "[$response=#ONT(ontclubs)]")
df.add_user_transition(State.First_negative_prompt, State.U4C5, "[$response=#ONT(ontwork)]")

df.add_system_transition(State.U4C1, State.P4C1A, '"What do you do to de-stress from school?"')

# df.add_system_transition(State.P4CERR2, State.P4C1A, '"I\'m sorry, could you restate that?"')
# df.set_error_successor(State.P4C1A, State.P4CERR2)

df.add_system_transition(State.P4CERR2, State.P4C1Asecond, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C1A, State.P4CERR2)

df.add_system_transition(State.P4C1Asecond, State.P4C1Asecond, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4C1Asecond, State.U4C4, "[$response=#ONT(ontclubs)]")
df.set_error_successor(State.P4C1Asecond, State.U4C4E1A2)

df.add_user_transition(State.P4C1A, State.U4C4, "[$response=#ONT(ontclubs)]")
df.add_system_transition(State.U4C2, State.P4C2B,
                         '"Do you think your family places pressure on you? Or maybe you do it to yourself?"')
df.add_system_transition(State.P4CERR3, State.P4C2B, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B, State.P4CERR3)
df.add_system_transition(State.U4C3, State.P4C3C,
                         '"Has anything changed in your life recently? If so, what field of your life has changed?"')
df.add_system_transition(State.P4CERR4, State.P4C3C, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C3C, State.P4CERR4)
df.add_user_transition(State.P4C2B, State.U4C2B1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B, State.U4C2B2, r"[/(.*)(myself)(.*)/]")
df.add_user_transition(State.P4C2B, State.U4C2B3, "[$no=#ONT(ontnegate)]")
df.add_user_transition(State.P4C2B, State.U4C2B4, "[$response=#ONT(ontunsure)]")
df.add_system_transition(State.U4C2B1, State.P4C2B1A, '"Have you talked to them about how this is unnecessary?"')
df.add_system_transition(State.P4CERR5, State.P4C2B1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A, State.P4CERR5)
df.add_system_transition(State.U4C2B2, State.P4C2B2A,
                         '"So you place pressure on yourself, I assume. Do you do any activities to destress?"')
df.add_system_transition(State.U4C2B3, State.P4C2B2A,
                         '"So you place pressure on yourself, I assume. Do you do any activities to detress?"')
df.add_system_transition(State.P4CERR6, State.P4C2B2A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B2A, State.P4CERR6)
df.add_user_transition(State.P4C2B2A, State.U4C2B2A1, "[$no=#ONT(ontnegate)]")
df.add_user_transition(State.P4C2B2A, State.U4C2B2A3, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B1A, State.U4C2B1A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B1A, State.U4C2B1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B1A2, State.P4C2B1A2A,
                         '"I feel like you should talk to them about how they place unnecessary pressure on you. Can you try that?"')
df.add_system_transition(State.P4CERR7, State.P4C2B1A2A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A2A, State.P4CERR7)
df.add_user_transition(State.P4C2B1A2A, State.U4C2B1A2A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B1A2A, State.U4C2B1A2A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B1A2A1, State.P4C2B1A2A1A,
                         '"Great! Why don\'t you let me know how it goes next session?"')
df.add_system_transition(State.P4CERR8, State.P4C2B1A2A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A2A1A, State.P4CERR8)
df.add_user_transition(State.P4C2B1A2A1A, State.U4C2B1A2A1A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B1A2A1A, State.U4C2B1A2A1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B1A2A1A2, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4C2B1A2A1A1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4C2B1A1, State.P4C2B1A1A, '"What did they say?"')
df.add_system_transition(State.P4CERR9, State.P4C2B1A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A1A, State.P4CERR9)
df.add_user_transition(State.P4C2B1A1A, State.U4C2B1A1A1, "/.*/")
df.add_system_transition(State.U4C2B1A1A1, State.P4C2B1A1A1A,
                         '"That\'s very interesting. Do you do any activities to take your mind off this stress? "')
df.add_system_transition(State.P4CERR10, State.P4C2B1A1A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A1A1A, State.P4CERR10)
df.add_user_transition(State.P4C2B1A1A1A, State.U4C2B1A1A1A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C2B1A1A1A, State.U4C2B1A1A1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B2A1, State.P4C2B2A1A,
                         '"That\'s not good! You should always participate in something you enjoy. What would you do for fun if you had the time?"')
df.add_system_transition(State.U4C2B1A1A1A2, State.P4C2B2A1A,
                         '"That\'s not good! You should always participate in something you enjoy. What would you do for fun if you had the time?"')
df.add_system_transition(State.P4CERR11, State.P4C2B2A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B2A1A, State.P4CERR11)
df.add_user_transition(State.P4C2B2A1A, State.U4C2B2A1A1, "/.*/")
df.add_system_transition(State.U4C2B2A1A1, State.P4C2B2A1A1A,
                         '"Does your college have a club for this? What is it called?"')
df.add_system_transition(State.P4CERR12, State.P4C2B2A1A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B2A1A1A, State.P4CERR12)
df.add_user_transition(State.P4C2B2A1A1A, State.U4C2B2A1A1A2, "[$no=#ONT(ontnegate)]")
df.add_user_transition(State.P4C2B2A1A1A, State.U4C2B2A1A1A1, "[$response=#ONT(ontclubs)]")
df.add_system_transition(State.U4C2B2A1A1A2, State.P4C2B2A1A1A2A,
                         '"That\'s unfortunate. Why don\'t you seek out off-campus resources for this activity and let me know how it goes next time?"')
df.add_system_transition(State.P4CERR13, State.P4C2B2A1A1A2A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B2A1A1A2A, State.P4CERR13)
df.add_user_transition(State.P4C2B2A1A1A2A, State.U4C2B2A1A1A2A2, "[$yes=#ONT(ontaffirm)]")
df.add_system_transition(State.U4C2B2A1A1A2A2, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_user_transition(State.P4C2B2A1A1A2A, State.U4C2B2A1A1A2A1, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B2A1A1A2A1, State.P4C2B1A2A2A,
                         '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
df.add_system_transition(State.P4CERR14, State.P4C2B1A2A2A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B1A2A2A, State.P4CERR14)
df.add_system_transition(State.U4C2B2A1A1A1, State.P4C2B2A1A1A1A,
                         '"Great! Why don\'t you join it and let me know how it goes?"')
df.add_user_transition(State.P4C2B2A1A1A1A, State.U4C2B2A1A1A1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C2B2A1A1A1A2, State.P4C2B1A2A2A,
                         '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
df.add_user_transition(State.P4C2B2A1A1A1A, State.U4C2B2A1A1A1A1, "[$yes=#ONT(ontaffirm)]")
df.add_system_transition(State.U4C2B2A1A1A1A1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_user_transition(State.P4C2B1A2A2A, State.U4C2B1A2A2A1, "/.*/")
df.add_system_transition(State.U4C2B1A2A2A1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4C2B1A2A2, State.P4C2B1A2A2A,
                         '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
df.add_system_transition(State.U4C4D1A2A2, State.P4C2B1A2A2A,
                         '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
df.add_system_transition(State.U4C2B2A3, State.P4C2B2A3A, '"Which activities do you participate in?"')
df.add_system_transition(State.U4C2B1A1A1A1, State.P4C2B2A3A, '"Which activities do you participate in?"')
df.add_system_transition(State.P4CERR15, State.P4C2B2A3A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B2A3A, State.P4CERR15)
df.add_user_transition(State.P4C2B2A3A, State.P4C, "/.*/")
df.add_system_transition(State.P4C, State.P4C4D, '"Why do you participate in this?"')
df.add_user_transition(State.P4C4D, State.U4C4D2, "[$response=#ONT(ontbadclub])")
df.add_user_transition(State.P4C4D, State.U4C4D1, "[$response=#ONT(ontfunclub)]")
df.add_system_transition(State.U4C2B4, State.P4C2B4A,
                         '"I suggest you first try to figure out where this pressure is coming from, then. Do you do any activities to destress?"')
df.add_system_transition(State.P4CERR16, State.P4C2B4A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C2B4A, State.P4CERR16)
df.add_user_transition(State.P4C2B4A, State.P4C1, "/.*/")
df.add_system_transition(State.P4C1, State.P4C4D, '"Why do you participate in $reponse?"')
df.add_system_transition(State.P4CERR17, State.P4C4D, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C4D, State.P4CERR17)
df.add_system_transition(State.U4C4, State.P4C4D, '"Why do you participate in $reponse?"')
df.add_system_transition(State.U4C4D1, State.P4C4D1A,
                         '"I\'m glad you enjoy it! Does this add any stress to your life? Why?"')
df.add_system_transition(State.U4C2B2A2, State.P4C4D1A,
                         '"I\'m glad you enjoy it! Does this add any stress to your life? Why?"')
df.add_system_transition(State.P4CERR18, State.P4C4D1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C4D1A, State.P4CERR18)
df.add_user_transition(State.P4C4D1A, State.U4C4D1A1, "[$yes=#ONT(ontaffirm)]")
df.add_system_transition(State.U4C4D1A1, State.P4C4D1A1A,
                         '"You must really care about it if it stresses you out and you still participate. Can you tell me more about why you care about this activity?"')
df.add_user_transition(State.P4C4D1A1A, State.U4C4D1A1A1, "/.*/")
df.add_system_transition(State.U4C4D1A1A1, State.P4C4D1A1A1A,
                         '"It seems to add another dimension into your life, which is good. I suggest you continue participating and try to focus on the positives. Why don\'t you let me know how this goes next session?"')
df.add_user_transition(State.P4C4D1A1A1A, State.U4C4D1A1A1A1, "/.*/")
df.add_system_transition(State.U4C4D1A1A1A1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_user_transition(State.P4C4D1A, State.U4C4D1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C4D1A2, State.P4C4D1A2A,
                         '"I suggest you first try to categorize what activities add or detract stress from your life. Can you do that for me before our next session?"')
df.add_user_transition(State.P4C4D1A2A, State.U4C4D1A2A2, "[$no=#ONT(ontnegate)]")
df.add_user_transition(State.P4C4D1A2A, State.U4C4D1A2A1, "[$yes=#ONT(ontaffirm)]")
df.add_system_transition(State.P4C4D1A2A, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4C5, State.P4C4E, '"Where do you work?"')
df.add_user_transition(State.P4C4E, State.U4C4E1, "/.*/")
df.add_system_transition(State.U4C4D2, State.P4C4D2A,
                         '"That\'s not a great reason to put time into something. Do you enjoy it at all?"')
df.add_user_transition(State.P4C4D2A, State.U4C4D2A1, "/.*/")
df.add_system_transition(State.U4C4D2A1, State.P4C4E1A1A,
                         '"That\'s good, that you have something you enjoy. So what stresses you out about it?"')
df.add_system_transition(State.U4C4E1, State.P4C4E1A, '"Do you enjoy your job at all?"')
df.add_system_transition(State.P4CERR19, State.P4C4E1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C4E1A, State.P4CERR19)
df.add_user_transition(State.P4C4E1A, State.U4C4E1A1, "[$yes=#ONT(ontaffirm])")
df.add_user_transition(State.P4C4E1A, State.U4C4E1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C4E1A2, State.P4C4E1A2A,
                         '"Well, do you participate in an extracurricular that you enjoy?"')
df.add_system_transition(State.P4CERR20, State.P4C4E1A2A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C4E1A2A, State.P4CERR20)
df.add_user_transition(State.P4C4E1A2A, State.U4C4E1A2A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4C4E1A2A, State.U4C4E1A2A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4C4E1A2A1, State.P4C2B2A3A, '"Which activities do you participate in?"')
df.add_system_transition(State.U4C4E1A2A2, State.P4C2B2A1A,
                         '"That\'s not good! You should always participate in something you enjoy. What would you do for fun if you had the time?"')
df.add_system_transition(State.U4C4E1A1, State.P4C4E1A1A,
                         '"That\'s good, that you have something you enjoy. So what stresses you out about it?"')
df.add_system_transition(State.P4CERR21, State.P4C4E1A1A, '"I\'m sorry, could you restate that?"')
df.set_error_successor(State.P4C4E1A1A, State.P4CERR21)
df.add_user_transition(State.P4C4E1A1A, State.U4C1, "[$response=#ONT(ontschool)]")
df.add_user_transition(State.P4C4E1A1A, State.U4C4E1A1B, "[$response=#ONT(onttired)]")
df.add_system_transition(State.U4C4E1A1B, State.P4C2B1A1A1A,
                         '"That\'s very interesting. Do you do any activities to take your mind off this stress?"')

# --------------------------------------------------------------------
# hotlinecatch
df.add_user_transition(State.First_negative_prompt, State.P4D, "[$response=#ONT(onthotline)]")
df.add_system_transition(State.P4D, State.U4D1,
                         '"Oh no! I am very afraid that this may be a violent or life-threatening situation. Here are some hotlines: Suicide: 8002738255, Domestic violence: 8007997233, Sexual assault: 8006564673."')
df.add_user_transition(State.U4D1, State.P4D1, "/.*/")
df.add_system_transition(State.P4D1, State.END, '"Goodbye! Thanks for talking to me today!"')

######################################################################
# eating
df.add_user_transition(State.First_negative_prompt, State.U4EA, "[$response=#ONT(onteating)]")
df.add_system_transition(State.U4EA, State.P4E,
                         '"Oh no! Eating regularly and healthily is a very important part of growing. Can you tell me more about your problem?"')
df.add_system_transition(State.P4EERR, State.P4E, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E, State.U4E1, "[$response=#ONT(onteatingtoomuch)]")
df.add_user_transition(State.P4E, State.U4E2, "[$response=#ONT(onteatingtoolittle)]")
df.add_system_transition(State.U4E1, State.P4E1A,
                         '"Haha, weight gain is common in college students. Do you think it actually harms you, though?"')
df.add_system_transition(State.P4E1AERR, State.P4E1A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E1A, State.U4E1A2, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4E1A, State.U4E1A1, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4E1A2, State.P4E1A2A,
                         '"You may eat excessively because you are stressed. Has anything been stressing you out recently?"')
df.add_system_transition(State.P4E1A2AERR, State.P4E1A2A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E1A2A, State.U4C1, "[$response=#ONT(ontschool)]")
df.add_user_transition(State.P4E1A2A, State.U4C2, "[$response=#ONT(ontfamily)]")
df.add_user_transition(State.P4E1A2A, State.U4C3, "[$response=#ONT(ontdunno)]")
df.add_user_transition(State.P4E1A2A, State.U4C4, "[$response=#ONT(ontclubs)]")
df.add_user_transition(State.P4E1A2A, State.U4C5, "[$response=#ONT(ontwork)]")
df.add_system_transition(State.U4E1A1, State.P4E1A2B,
                         '"Haha, I think you\'re doing just fine. Your body is just growing, as it should be. "')
df.add_system_transition(State.P4E1A2BERR, State.P4E1A2B, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E1A2B, State.U4E1A2B1, "/.*/")
df.add_system_transition(State.U4E1A2B1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4E2, State.P4E2A,
                         '"Oh no, that\'s a problem! You need to eat. Are you on a meal plan?"')
df.add_system_transition(State.P4E2AERR, State.P4E2A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E2A, State.U4E2A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4E2A, State.U4E2A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4E2A1, State.P4E2A1A,
                         '" I think you need to make more of an effort to go to dining halls. They have very healthy options. Can you try that?"')
df.add_system_transition(State.P4E2A1AERR, State.P4E2A1A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E2A1A, State.U4E2A1A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4E2A1A, State.U4E2A1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4E2A1A1, State.END, '"Goodbye! Thanks for talking to me today!"')
df.add_system_transition(State.U4E2A1A2, State.P4C2B1A2A2A,
                         '"I think this inability to take action holds you back. Why don\'t you brace yourself to take action and then we can talk again next time?"')
df.add_system_transition(State.U4E2A2, State.P4E2A2A,
                         '"Then you need to start grocery shopping for yourself. Is money a problem?"')
df.add_system_transition(State.P4E2A2AERR, State.P4E2A2A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E2A2A, State.U4E2A2A2, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4E2A2A, State.U4E2A2A1, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4E2A2A2, State.P4E2A2A2A,
                         '"You should talk to your career center about finding a job. You need to eat. Do you think you can look for a job?"')
df.add_system_transition(State.P4E2A2A2AERR, State.P4E2A2A2A, '"I\'m sorry, could you restate that?"')
df.add_user_transition(State.P4E2A2A2A, State.U4E2A1A1, "[$yes=#ONT(ontaffirm)]")
df.add_user_transition(State.P4E2A2A2A, State.U4E2A1A2, "[$no=#ONT(ontnegate)]")
df.add_system_transition(State.U4E2A2A1, State.P4E2A2A1A, '"Good, then you should go grocery shopping more often."')
df.add_user_transition(State.P4E2A2A1A, State.U4E2A2A1A1, "/.*/")
df.add_system_transition(State.U4E2A2A1A1, State.END, '"Goodbye! Thanks for talking to me today!"')

########### Confrontation Branch (Yuewu) ########################
df.add_system_transition(State.confrontation_answer, State.confrontation_cause_prompt, '[!"How did the"$confrontation"start?"]')
df.set_error_successor(State.confrontation_answer, State.confrontation_cause_self)
# -> argument branchag

df.add_system_transition(State.confrontation_cause_error, State.confrontation_noCatch_self_prompt, '"Do you feel like it had something to do with what you did?"')
df.add_user_transition(State.confrontation_noCatch_self_prompt,State.confrontation_cause_self,"#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_noCatch_self_prompt,State.confrontation_cause_self)


##### argument branch
df.add_user_transition(State.confrontation_cause_prompt, State.confrontation_cause_self, '[{I,i}]')
df.add_system_transition(State.confrontation_cause_self, State.confrontation_usual_prompt,'"Is this something that has happened before?"')
# -> usual

df.add_user_transition(State.confrontation_cause_prompt, State.confrontation_cause_other, '[$person=#POS(propn)]')
df.add_system_transition(State.confrontation_cause_other, State.confrontation_intentional_yn, '"Do you think it was intentional?"')
# -> argument motive

df.set_error_successor(State.confrontation_cause_prompt,State.confrontation_cause_self)
# -> usual


##### argument motive
df.add_user_transition(State.confrontation_intentional_yn,State.confrontation_intentional_answer,"#ONT(ontaffirm)")
# -> exposure
df.set_error_successor(State.confrontation_intentional_yn,State.confrontation_advice_yn)
# -> advice

df.add_system_transition(State.confrontation_intentional_answer,State.confrontation_intentional_motive_prompt,'"Why do you think they did that?"')
df.add_user_transition(State.confrontation_intentional_motive_prompt,State.confrontation_intentional_motive_answer, '[{because,Because} $reason=/.*/]')
df.set_error_successor(State.confrontation_intentional_motive_prompt,State.confrontation_cause_self)
# -> usual

df.add_system_transition(State.confrontation_intentional_motive_answer,State.confrontation_intentional_motive_yn, '"Is it justified to argue because"$reason"?"')
df.add_user_transition(State.confrontation_intentional_motive_yn,State.confrontation_exposure_prompt, "#ONT(ontaffirm)")
# -> usual
df.add_user_transition(State.confrontation_intentional_motive_yn, State.confrontation_advice_yn,"#ONT(ontnegate)")
# -> advice

##### usual
df.add_user_transition(State.confrontation_usual_prompt,State.confrontation_usual_yn,"#ONT(ontaffirm)")
df.add_system_transition(State.confrontation_usual_yn,State.confrontation_usual_when,'"When was the last time this has happened?"')
#df.add_user_transition(State.confrontation_usual_when,State.confrontation_usual_when_answer,"$time=#NER(date)")
df.set_error_successor(State.confrontation_usual_when,State.confrontation_usual_when_answer)
# -> exposure (because no time catch)
df.add_system_transition(State.confrontation_usual_when_answer,State.confrontation_usual_when_yn,'"Have you met with them since then where you haven\'t had a "$confrontation"?"')
df.set_error_successor(State.confrontation_usual_when_answer,State.confrontation_advice_yn)
# -> advice if error

df.add_user_transition(State.confrontation_usual_when_yn,State.confrontation_advice_yn,"#ONT(ontaffirm)")
# -> advice
df.add_user_transition(State.confrontation_usual_when_yn,State.confrontation_exposure_end,"#ONT(ontnegate)")
# -> exposure

df.add_user_transition(State.confrontation_usual_prompt,State.confrontation_exposure_prompt,"#ONT(ontnegate)")
# -> exposure

##### advice
df.add_system_transition(State.confrontation_advice_yn,State.confrontation_advice_yn_answer,'"Could I offer you some advice?"')
df.add_user_transition(State.confrontation_advice_yn_answer,State.confrontation_advice_calmer_yn,"#ONT(ontaffirm)")
df.set_error_successor(State.confrontation_advice_yn_answer,State.ENDwGREET)
# -> END
df.add_system_transition(State.confrontation_advice_calmer_yn,State.confrontation_advice_calmer_answer,'"Okay, do you think a calmer attitude would have mitigated the"$confrontation"?"')
df.set_error_successor(State.confrontation_advice_calmer_answer,State.confrontation_treatment_placeholder)

df.add_system_transition(State.confrontation_treatment_placeholder,State.ENDwGREET,'"We\'re still researching the best advice to give, please come back soon"')
# TO DO: add treatments


##### exposure
df.add_system_transition(State.confrontation_exposure_prompt,State.confrontation_exposure_answer, '"Why do you spend time with "$pronoun"?"')
df.add_user_transition(State.confrontation_exposure_answer,State.confrontation_exposure_why,'[{because,Because} $reason=/.*/]')
df.set_error_successor(State.confrontation_exposure_answer,State.confrontation_exposure_why)

df.add_system_transition(State.confrontation_exposure_why,State.confrontation_exposure_yn, '"Do you think you\'ll talk with them again soon?"')

df.add_user_transition(State.confrontation_exposure_yn,State.confrontation_advice_yn, "#ONT(ontaffirm)")
# -> advice
df.set_error_successor(State.confrontation_exposure_yn, State.confrontation_exposure_end)

df.add_system_transition(State.confrontation_exposure_end,State.END,'"I think it\'s best to spend some time cooling off after a"$confrontation"."')
# -> END

#ENDwGREET
df.add_system_transition(State.ENDwGREET,State.EXIT,'"Alright, have a nice day!"')

if __name__ == '__main__':
    df.run(debugging=False)
