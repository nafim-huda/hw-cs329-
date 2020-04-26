from emora_stdm import KnowledgeBase, DialogueFlow, Macro
from enum import Enum, auto
#from emora_stdm import Macro
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VERSION(Macro):
    def run(self, ngrams, vars, args):
        if 'time_type' in vars:
            m = vars['time_type']
        sentences = [m]
        analyzer = SentimentIntensityAnalyzer()
        for sentence in sentences:
            vs = analyzer.polarity_scores(sentence)
            print("{:-<65} {}".format(sentence, str(vs)))

 # class time(Macro):
 #    def run(self, ngrams, vars, args):
 #        if 'time_type' in vars:
 #            m = vars['time_type']
 #        sentences = [m]
 #        analyzer = SentimentIntensityAnalyzer()
 #        for sentence in sentences:
 #            vs = analyzer.polarity_scores(sentence)
 #            print("{:-<65} {}".format(sentence, str(vs)))

time_natex = r"{[$time_type=/.*/]}"

#class VERSION(Macro):

#    def run(self):
#      sentences = ["hello"]
#      analyzer = SentimentIntensityAnalyzer()
#      for sentence in sentences:
#        vs = analyzer.polarity_scores(sentence)
#        print("{:-<65} {}".format(sentence, str(vs)))

################################
# Modify State enum for any Quiz2 tasks as needed
################################
class State(Enum):
    START = 0
    PROMPT = 1
    MAMMAL = 2
    BIRD = 3
    REPTILE = 4
    AMPHIBIAN = 5
    ERR = 6
################################

################################
# Modify ont_dict for Quiz2 Task 3
################################
ont_dict = {
             "ontology": {
                 "ontamphibian": ["frog", "salamander"],
                 "ontyes": ["yea", "yeah"]
             }
          }

################################
knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge, macros={"VERSION":VERSION()})

df.add_system_transition(State.START, State.PROMPT, '"Enter an animal"')

#df.add_user_transition(State.PROMPT, State.MAMMAL, '[$reason=/.*/]')




df.add_user_transition(State.PROMPT, State.MAMMAL, time_natex)

df.add_system_transition(State.MAMMAL, State.BIRD, r'[!oh are you using #VERSION"?"]')


df.add_system_transition(State.MAMMAL, State.PROMPT, '[! $animal " is a mammal, enter another animal"]')
df.add_system_transition(State.BIRD, State.PROMPT, '[! $animal "is a bird, enter another animal"]')

df.add_system_transition(State.ERR, State.PROMPT, '"i dont know that one, enter another animal"')
df.set_error_successor(State.PROMPT, State.ERR)



################################
# Add Quiz2 Task 2 below
################################
#df.add_user_transition(State.PROMPT, State.AMPHIBIAN, "$animal=#ONT(ontamphibian)")
df.add_user_transition(State.PROMPT, State.AMPHIBIAN, "$animal=#ONT(ontyes)")
df.add_system_transition(State.AMPHIBIAN, State.PROMPT, '[! $animal is an amphibian"," enter another animal":"]')

################################
# Add Quiz2 Task 3 below
# (except do not move ont_dict from line 11)
################################

df.run(debugging=False)
