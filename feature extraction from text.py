# import
from pycorenlp import StanfordCoreNLP
import json


nlp = StanfordCoreNLP('http://localhost:9000')

json_file = open("sample_file.json", "r")
json_object = json.load(json_file)
# creating varibels
resultpos = []
resultlemma = []
resultdepparse = []
resultcoref = []
null = -1, -1
token_list = []
lemma_dict = {null: '$'}
pos_dict = {null: '$'}
NN_list = []
NN_dict = {null: '$'}
VB_list = []
VB_dict = {null: '$'}
nmod_list = []
nummod_dict = {null: '$'}
amod_list = []
tmod_list = []
advmod_list = []
agent_list = []
case_list = []
cop_list = []
nsubj_list = []
nsubjpass_list = []
acl_list = []
dobj_list = []
conj_list = []
openie_list = []
coref_list = []
coref_dict = {null: '$'}
of_dict = {null: '$'}
draw_list = []
direct_draw_list = []
direct_draw_set = {""}
adjectives_list = []
adjectives_set = {""}
hand_list = []
object_list = []
usedVB_dict = {null: '$'}
usedNN_dict = {null: '$'}
num_s = -2
num_w = 0


def init_var():
    global resultpos
    resultpos = []
    global resultlemma
    resultlemma = []
    global resultdepparse
    resultdepparse = []
    global resultcoref
    resultcoref = []
    global token_list
    token_list = []
    global lemma_dict
    lemma_dict = {null: '$'}
    global pos_dict
    pos_dict = {null: '$'}
    global NN_list
    NN_list = []
    global NN_dict
    NN_dict = {null: '$'}
    global VB_list
    VB_list = []
    global VB_dict
    VB_dict = {null: '$'}
    global nmod_list
    nmod_list = []
    global nummod_dict
    nummod_dict = {null: '$'}
    global amod_list
    amod_list = []
    global tmod_list
    tmod_list = []
    global advmod_list
    advmod_list = []
    global agent_list
    agent_list = []
    global case_list
    case_list = []
    global cop_list
    cop_list = []
    global nsubj_list
    nsubj_list = []
    global nsubjpass_list
    nsubjpass_list = []
    global acl_list
    acl_list = []
    global dobj_list
    dobj_list = []
    global conj_list
    conj_list = []
    global coref_list
    coref_list = []
    global coref_dict
    coref_dict = {null: '$'}
    global of_dict
    of_dict = {null: '$'}
    global draw_list
    draw_list = []
    global direct_draw_list
    direct_draw_list = []
    global direct_draw_set
    direct_draw_set = {""}
    global adjectives_list
    adjectives_list = []
    global adjectives_set
    adjectives_set = {""}
    global hand_list
    hand_list = []
    global object_list
    object_list = []
    global usedVB_dict
    usedVB_dict = {null: '$'}
    global usedNN_dict
    usedNN_dict = {null: '$'}
    global num_s
    num_s = -2
    global num_w
    num_w = 0

# extracting the important features form the sentenc using nlp


def extracting_features(s):
    respos = nlp.annotate(s,
                          properties={
                              'annotators': 'pos',
                              'outputFormat': 'json',
                          })
    for sen in respos['sentences']:
        x = [sen['tokens']]
        resultpos.append(x)

    reslemma = nlp.annotate(s,
                            properties={
                                'annotators': 'lemma',
                                'outputFormat': 'json',
                                'timeout': 15000,
                            })
    for sen in reslemma['sentences']:
        x = [sen['tokens']]
        resultlemma.append(x)

    resdepparse = nlp.annotate(s,
                               properties={
                                   'annotators': 'depparse',
                                   'outputFormat': 'json',
                                   'timeout': 15000,
                               })
    for sen in resdepparse['sentences']:
        x = [sen['enhancedPlusPlusDependencies']]
        resultdepparse.append(x)

    rescoref = nlp.annotate(s,
                            properties={
                                'annotators': 'dcoref',
                                'outputFormat': 'json',
                                'timeout': 1500000,
                            })
    resultcoref = [rescoref["corefs"]]
    c = 0
    for item in resultpos:
        c += 1
        for i in item:
            for token in i:
                tokens = [c, token['index']], token['word'], token['pos']
                token_list.append(tokens)
                pos_dict[c, token['index']] = token['pos']
                print(tokens)
    c = 0
    for item in resultlemma:
        c += 1
        for i in item:
            for token in i:
                lemma_dict[c, token['index']] = token['lemma'].lower()
                print([c, token['index']], token['lemma'])
    c = 0
    for item in resultpos:
        c += 1
        for i in item:
            for token in i:
                if token['pos'] == 'NN' or token['pos'] == 'NNP' or token['pos'] == 'NNS'or token['pos'] == 'NNPS':
                    tokens = [c, token['index']], token['word'], token['pos']
                    NN_list.append(tokens)
                    NN_dict[c, token['index']] = 'yes'
                    print(tokens)
    c = 0
    for item in resultpos:
        c += 1
        for i in item:
            for token in i:
                if token['pos'] == 'VBD' or token['pos'] == 'VBG' or token['pos'] == 'VBN'or token['pos'] == 'VBP'or token['pos'] == 'VBZ':
                    tokens = [c, token['index']], token['word'], token['pos']
                    VB_list.append(tokens)
                    VB_dict[c, token['index']] = 'yes'
                    print(tokens)
    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nmod'):
                    if temp[5:] != 'of':
                        deps = c, temp[5:], dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                        nmod_list.append(deps)
                        print(deps)
                    else:
                        third = c, dep['governor']
                        rest = c, dep['dependent']
                        of_dict[third] = rest
                        usedNN_dict[rest] = 'yes'

    for item in of_dict:
        if item != (null):
            lemma_dict[item] = lemma_dict[item]+'of'+lemma_dict[of_dict[item]]
            print(lemma_dict[item], item)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nummod'):
                    deps = c, dep['governor']
                    nummod_dict[deps] = dep['dependentGloss']
    for item in nummod_dict:
        print(item, "=", nummod_dict[item])

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('amod'):
                    deps = (c, dep['governor']
                            ), lemma_dict[c, dep['dependent']]
                    adjectives_list.append(deps)
                    adjectives_set.add(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nmod:tmod'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    tmod_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('advmod'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    advmod_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nmod:agent'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    agent_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('case'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    case_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('cop'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    cop_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nsubj') and not temp.startswith('nsubjpass'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    nsubj_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('nsubjpass'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    nsubjpass_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('acl'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    acl_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('dobj'):
                    deps = c, dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    dobj_list.append(deps)
                    print(deps)

    c = 0
    for item in resultdepparse:
        c += 1
        for i in item:
            for dep in i:
                temp = dep['dep']
                if temp.startswith('conj'):
                    deps = c, temp[5:], dep['governor'], dep['governorGloss'], dep['dependent'], dep['dependentGloss']
                    conj_list.append(deps)
                    print(deps)

    for i in resultcoref:
        for j in i.values():
            temp = ()
            for k in j:
                temp1 = k['sentNum'], k['text'], [
                    k['startIndex'], k['endIndex']]
                temp += temp1
            print(temp)
            coref_list.append(temp)

    for item in coref_list:
        lenth = len(item)/3
        if lenth > 1:
            for x in range(1, int(lenth)):
                done = False
                for y in range(item[x*3+2][0], item[x*3+2][1]):
                    if not done:
                        type1 = item[x*3], y
                        if pos_dict[type1] == 'PRP':
                            for z in range(item[2][0], item[2][1]):
                                type2 = item[0], z
                                if not done and type2 in NN_dict:
                                    coref_dict[type1] = type2
                                    done = True
                if not done:
                    for y in range(item[x*3+2][0], item[x*3+2][1]):
                        if not done:
                            type1 = item[x*3], y
                            if type1 in NN_dict:
                                for z in range(item[2][0], item[2][1]):
                                    type2 = item[0], z
                                    if not done and type2 in NN_dict:
                                        if lemma_dict[type1] == lemma_dict[type2]:
                                            coref_dict[type1] = type2
                                            done = True
    print(coref_dict)
