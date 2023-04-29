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


def analayzing_nmod():
    for item in nmod_list:
        tempVB = item[0], item[2]
        if tempVB in VB_dict:
            do = -1, -1
            ns = -1, -1
            nsp = -1, -1
            if item[1] == 'agent':
                usedVB_dict[item[0], item[2]] = 'yes'
                third = null
                case = null
                for item0 in nmod_list:
                    tempVB0 = item0[0], item0[2]
                    if tempVB0 == tempVB and item0[1] != 'agent':
                        third = item0[0], item0[4]
                        if third in coref_dict:
                            third = coref_dict[third]
                        case = item0[1]
                first = item[0], item[4]
                if first in coref_dict:
                    first = coref_dict[first]
                for item1 in nsubjpass_list:
                    if item[0] == item1[0] and item[2] == item1[1]:
                        nsp = item[0], item1[3]
                        if nsp in coref_dict:
                            nsp = coref_dict[nsp]
                        temp = [first], lemma_dict[first], [tempVB], lemma_dict[tempVB], [
                            nsp], lemma_dict[nsp], case, [third], lemma_dict[third]
                        draw_list.append(temp)
                        usedNN_dict[item[0], item[4]] = 'yes'
                        usedNN_dict[nsp] = 'yes'
                        usedNN_dict[third] = 'yes'
                if nsp == null:
                    temp = [first], lemma_dict[first], [tempVB], lemma_dict[tempVB], [
                        nsp], lemma_dict[nsp], case, [third], lemma_dict[third]
                    draw_list.append(temp)
                    usedNN_dict[item[0], item[4]] = 'yes'
                    usedNN_dict[third] = 'yes'
            else:
                boolflag = False
                for ag in agent_list:
                    if ag[0] == item[0]and ag[1] == item[2]:
                        boolflag = True
                if not boolflag:
                    usedVB_dict[item[0], item[2]] = 'yes'
                    third = item[0], item[4]
                    if third in coref_dict:
                        third = coref_dict[third]
                    for item1 in dobj_list:
                        if item[0] == item1[0] and item[2] == item1[1]:
                            do = item[0], item1[3]
                            if do in coref_dict:
                                do = coref_dict[do]
                            for item1 in nsubj_list:
                                if item[0] == item1[0] and item[2] == item1[1]:
                                    ns = item[0], item1[3]
                                    if ns in coref_dict:
                                        ns = coref_dict[ns]
                                    temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                        do], lemma_dict[do], item[1], [third], lemma_dict[third]
                                    draw_list.append(temp)
                                    usedNN_dict[ns] = 'yes'
                                    usedNN_dict[do] = 'yes'
                                    usedNN_dict[item[0], item[4]] = 'yes'
                            if ns == null:
                                for item1 in acl_list:
                                    if item[0] == item1[0] and item[2] == item1[3]:
                                        ns = item[0], item1[1]
                                        if ns in coref_dict:
                                            ns = coref_dict[ns]
                                        temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                            do], lemma_dict[do], item[1], [third], lemma_dict[third]
                                        draw_list.append(temp)
                                        usedNN_dict[ns] = 'yes'
                                        usedNN_dict[do] = 'yes'
                                        usedNN_dict[item[0],
                                                    item[4]] = 'yes'
                    if do == null:
                        for item1 in nsubjpass_list:
                            if item[0] == item1[0] and item[2] == item1[1]:
                                do = item[0], item1[3]
                                if do in coref_dict:
                                    do = coref_dict[do]
                        for item1 in nsubj_list:
                            if item[0] == item1[0] and item[2] == item1[1]:
                                ns = item[0], item1[3]
                                if ns in coref_dict:
                                    ns = coref_dict[ns]
                                temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                    do], lemma_dict[do], item[1], [third], lemma_dict[third]
                                draw_list.append(temp)
                                usedNN_dict[ns] = 'yes'
                                usedNN_dict[item[0], item[4]] = 'yes'
                                usedNN_dict[do] = 'yes'
                                usedNN_dict[third] = 'yes'
                        if ns == null:
                            for item1 in acl_list:
                                if item[0] == item1[0] and item[2] == item1[3]:
                                    ns = item[0], item1[1]
                                    if ns in coref_dict:
                                        ns = coref_dict[ns]
                                    temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                        do], lemma_dict[do], item[1], [third], lemma_dict[third]
                                    draw_list.append(temp)
                                    usedNN_dict[ns] = 'yes'
                                    usedNN_dict[item[0], item[4]] = 'yes'
                        if do != null and ns == null:
                            temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                do], lemma_dict[do], item[1], [third], lemma_dict[third]
                            draw_list.append(temp)

        else:
            first = item[0], item[2]
            if first in coref_dict:
                first = coref_dict[first]
            third = item[0], item[4]
            if third in coref_dict:
                third = coref_dict[third]
            temp = [first], lemma_dict[first], [null], lemma_dict[null], [
                null], lemma_dict[null], item[1], [third], lemma_dict[third]
            draw_list.append(temp)
            usedNN_dict[first] = 'yes'
            usedNN_dict[third] = 'yes'


def analayzing_verbs():
    for item in VB_list:
        tempVB = item[0][0], item[0][1]
        if tempVB not in usedVB_dict and lemma_dict[tempVB] != 'be':
            do = -1, -1
            ns = -1, -1
            for item1 in dobj_list:
                if item[0][0] == item1[0] and item[0][1] == item1[1]:
                    do = item[0][0], item1[3]
                    if do in coref_dict:
                        do = coref_dict[do]
                    for item1 in nsubj_list:
                        if item[0][0] == item1[0] and item[0][1] == item1[1]:
                            ns = item[0][0], item1[3]
                            if ns in coref_dict:
                                ns = coref_dict[ns]
                            temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                do], lemma_dict[do], lemma_dict[null], [null], lemma_dict[null]
                            draw_list.append(temp)
                            usedNN_dict[ns] = 'yes'
                            usedNN_dict[do] = 'yes'
                    if ns == null:
                        for item1 in acl_list:
                            if item[0][0] == item1[0] and item[0][1] == item1[3]:
                                ns = item[0][0], item1[1]
                                if ns in coref_dict:
                                    ns = coref_dict[ns]
                                temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                    do], lemma_dict[do], lemma_dict[null], [null], lemma_dict[null]
                                draw_list.append(temp)
                                usedNN_dict[ns] = 'yes'
                                usedNN_dict[do] = 'yes'
            if do == null:
                for item1 in nsubj_list:
                    if item[0][0] == item1[0] and item[0][1] == item1[1]:
                        ns = item[0][0], item1[3]
                        if ns in coref_dict:
                            ns = coref_dict[ns]
                        temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                            do], lemma_dict[do], lemma_dict[null], [null], lemma_dict[null]
                        draw_list.append(temp)
                        usedNN_dict[ns] = 'yes'
                if ns == null:
                    for item1 in acl_list:
                        if item[0][0] == item1[0] and item[0][1] == item1[3]:
                            ns = item[0][0], item1[1]
                            if ns in coref_dict:
                                ns = coref_dict[ns]
                            temp = [ns], lemma_dict[ns], [tempVB], lemma_dict[tempVB], [
                                do], lemma_dict[do], lemma_dict[null], [null], lemma_dict[null]
                            draw_list.append(temp)
                            usedNN_dict[ns] = 'yes'


def analayzing_nsubj():
    for item in nsubj_list:
        tempNS = item[0], item[1]
        if tempNS in NN_dict:
            if tempNS in coref_dict:
                tempNS = coref_dict[tempNS]
            for item1 in case_list:
                if item[0] == item1[0] and item[1] == item1[1]:
                    case = item[0], item1[3]
                    me = item[0], item[3]
                    if me in coref_dict:
                        me = coref_dict[me]
            temp = [me], lemma_dict[me], [null], lemma_dict[null], [
                null], lemma_dict[null], lemma_dict[case], [tempNS], lemma_dict[tempNS]
            draw_list.append(temp)
            usedNN_dict[me] = 'yes'
            usedNN_dict[tempNS] = 'yes'


def add_unused_NN():
    for item in NN_list:
        NN = item[0][0], item[0][1]
        if NN not in usedNN_dict and NN not in coref_dict:
            temp = [NN], lemma_dict[NN], [null], lemma_dict[null], [
                null], lemma_dict[null], lemma_dict[null], [null], lemma_dict[null]
            draw_list.append(temp)


def analayzing_adj():
    for item in nsubj_list:
        tempNS = item[0], item[1]
        if pos_dict[tempNS] == 'JJ'or pos_dict[tempNS] == 'RB'or pos_dict[tempNS] == 'RBR' or pos_dict[tempNS] == 'RBS' or pos_dict[tempNS] == 'RP':
            tempO = item[0], item[3]
            if tempO in coref_dict:
                tempO = coref_dict[tempO]
            temp = tempO, lemma_dict[tempNS]
            adjectives_list.append(temp)
            adjectives_set.add(temp)


def convert_to_three():
    global num_s
    global num_w
    json_verb = json_object['verbs']
    for rel in draw_list:
        if rel[2] != [null]:
            if rel[3] in json_verb:
                verb = json_verb[rel[3]]
                if rel[4] != [null]:
                    if verb[0] != 'none':
                        temp = rel[0][0], rel[4][0], verb[0]
                        if temp not in direct_draw_set:
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)

                    if rel[6] != '$':
                        temp = rel[0][0], rel[7][0], rel[6]
                        if temp not in direct_draw_set:
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)
                        temp = rel[4][0], rel[7][0], rel[6]
                        if temp not in direct_draw_set:
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)
                    if verb[1] != 'none':
                        adj = verb[1]
                        if verb[1] == 'object':
                            adj = lemma_dict[rel[4][0]]
                        temp = rel[0][0], adj
                        if temp not in adjectives_set:
                            adjectives_list.append(temp)
                            adjectives_set.add(temp)
                else:
                    temp = rel[0][0], rel[7][0], rel[6]
                    if temp not in direct_draw_set:
                        if temp[2] != 'hand':
                            direct_draw_list.append(temp)
                            direct_draw_set.add(temp)
                        else:
                            if temp not in hand_list:
                                hand_list.append(temp)
                                temp = rel[0][0], null, '$'
                                if temp not in direct_draw_set:
                                    direct_draw_list.append(temp)
                                    direct_draw_set.add(temp)
                    if verb[1] != 'none':
                        adj = verb[1]
                        if verb[1] == 'object':
                            adj = lemma_dict[rel[4][0]]
                        temp = rel[0][0], adj
                        if temp not in adjectives_set:
                            adjectives_list.append(temp)
                            adjectives_set.add(temp)
            else:
                if rel[4] != [null]:
                    temp = rel[0][0], rel[4][0], 'near'
                    if temp not in direct_draw_set:
                        if temp[2] != 'hand':
                            direct_draw_list.append(temp)
                            direct_draw_set.add(temp)
                        else:
                            if temp not in hand_list:
                                hand_list.append(temp)
                                temp = rel[0][0], null, '$'
                                if temp not in direct_draw_set:
                                    direct_draw_list.append(temp)
                                    direct_draw_set.add(temp)
                    if rel[6] != '$':
                        temp = rel[0][0], rel[7][0], rel[6]
                        if temp not in direct_draw_set:
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)
                        temp = rel[4][0], rel[7][0], rel[6]
                        if temp not in direct_draw_set:
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)
                else:
                    temp = rel[0][0], rel[7][0], rel[6]
                    if temp not in direct_draw_set:
                        if temp[2] != 'hand':
                            direct_draw_list.append(temp)
                            direct_draw_set.add(temp)
                        else:
                            if temp not in hand_list:
                                hand_list.append(temp)
                                temp = rel[0][0], null, '$'
                                if temp not in direct_draw_set:
                                    direct_draw_list.append(temp)
                                    direct_draw_set.add(temp)
        else:
            temp = rel[0][0], rel[7][0], rel[6]
            if temp not in direct_draw_set:
                if temp[2] != 'hand':
                    direct_draw_list.append(temp)
                    direct_draw_set.add(temp)
                else:
                    if temp not in hand_list:
                        hand_list.append(temp)
                        temp = rel[0][0], null, '$'
                        if temp not in direct_draw_set:
                            direct_draw_list.append(temp)
                            direct_draw_set.add(temp)

    json_numbers = json_object['numbers']
    for item in nummod_dict:
        if item != null:
            for obj in direct_draw_list:
                if item == obj[0]:
                    for x in range(1, json_numbers[nummod_dict[item].lower()]):
                        new_obj = num_s, num_w
                        lemma_dict[new_obj] = lemma_dict[item]
                        temp = new_obj, obj[1], obj[2]
                        if temp not in direct_draw_list:
                            num_w += 1
                            if temp[2] != 'hand':
                                direct_draw_list.append(temp)
                                direct_draw_set.add(temp)
                            else:
                                if temp not in hand_list:
                                    hand_list.append(temp)
                                    temp = rel[0][0], null, '$'
                                    if temp not in direct_draw_set:
                                        direct_draw_list.append(temp)
                                        direct_draw_set.add(temp)
                            for adj in adjectives_list:
                                if item == adj[0]:
                                    new_adj = adj[1]
                                    temp = new_obj, new_adj
                                    if temp not in adjectives_set:
                                        adjectives_list.append(temp)
                                        adjectives_set.add(temp)
    json_adverbs = json_object['adverbs']
    c = 0
    for obj in direct_draw_list:
        adverb = 'near'
        if obj[2] in json_adverbs:
            adverb = json_adverbs[obj[2]]
        if obj[2] != '$':
            direct_draw_list[c] = obj[0], obj[1], adverb
        c += 1


def object_extr():
    print(direct_draw_list)
    for item in direct_draw_list:
        if item[0] not in object_list:
            if item[0] != null:
                object_list.append(item[0])
        if item[1] not in object_list and item[1] != null:
            if item[1] != null:
                object_list.append(item[1])


def objects_correction():
    names = json_object['names']
    objects = json_object['objects']
    for obj in object_list:
        if lemma_dict[obj] in names:
            if names[lemma_dict[obj]] == '0':
                lemma_dict[obj] = 'male'
            else:
                lemma_dict[obj] = 'female'
        if lemma_dict[obj] not in objects:
            lemma_dict[obj] = 'unknown'
    for item in hand_list:
        if lemma_dict[item[1]] in names:
            if names[lemma_dict[item[1]]] == '0':
                lemma_dict[item[1]] = 'male'
            else:
                lemma_dict[item[1]] = 'female'
        if lemma_dict[item[1]] not in objects:
            lemma_dict[item[1]] = 'unknown'


def clear_intersect():
    rel_list = []
    for i in range(0, len(object_list)):
        rel_list.append([])
        for j in range(0, len(object_list)):
            rel_list[i].append(0)
    for item in direct_draw_list:
        if item[1] != null and item[0] != null:
            rel_list[object_list.index(
                item[0])][object_list.index(item[1])] = 1
            rel_list[object_list.index(
                item[1])][object_list.index(item[0])] = 1
    for i in range(0, len(object_list)):
        for j in range(i+1, len(object_list)):
            if rel_list[i][j] == 0:
                temp = object_list[i], object_list[j], 'not_intersect'
                direct_draw_list.append(temp)
    for i in range(0, len(object_list)):
        print(rel_list[i])


def create_drawing_rel(s):
    init_var()
    extracting_features(s)
    analayzing_nmod()
    analayzing_verbs()
    analayzing_nsubj()
    add_unused_NN()
    analayzing_adj()
    for rel in draw_list:
        print(rel)
    convert_to_three()
    object_extr()
    clear_intersect()
    objects_correction()
    for item in direct_draw_list:
        print(item)
    for item in object_list:
        print(item)
    for item in hand_list:
        print(item)
    for item in adjectives_list:
        print(item)
    return direct_draw_list, object_list, hand_list, adjectives_list, lemma_dict
