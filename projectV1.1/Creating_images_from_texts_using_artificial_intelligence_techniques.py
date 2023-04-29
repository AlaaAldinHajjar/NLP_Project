import ex_rel_lib
import GeneticAlgorithm
import tkinter as tk
from PIL import Image, ImageTk, ImageGrab, EpsImagePlugin
import json


resultNum = 1


def save_as_png(canvas, fileName):
    # save postscipt image
    canvas.postscript(file=fileName + '.eps')
    # use PIL to convert to PNG
    img = Image.open(fileName + '.eps')
    img.save('result/'+fileName + '.png', 'png')


def start_ga():

    global root
    global frame
    global can
    global pilimg
    global img
    global imagesprite
    json_file = open("sample_file.json", "r")
    json_object = json.load(json_file)
    s = sentence_entry.get("1.0", tk.END)
    spatial_rel, object_list, hand_list, adj, lemma_dict = ex_rel_lib.create_drawing_rel(
        s)
    population_size = int(population_size_entry.get())
    mutation_rate = float(mutation_rate_entry.get())
    crossover_rate = float(crossover_rate_entry.get())
    elitism_count = int(elitism_count_entry.get())
    num_of_generations = int(num_of_generations_entry.get())
    ga = GeneticAlgorithm.GeneticAlgorithm(
        population_size, mutation_rate, crossover_rate, elitism_count, num_of_generations, spatial_rel, object_list, lemma_dict)
    population = ga.initPopulation()
    ga.evalPopulation(population)
    generation = 1
    while not ga.isTerminationConditionMet(population, generation):
        population = ga.crossoverPopulation(population)
        population = ga.mutatePopulation(population)
        ga.evalPopulation(population)
        generation += 1
    print("Found solution at generation")
    Found_solution_at_generation_entry.delete(0, 'end')
    Found_solution_at_generation_entry.insert(0, generation)
    print(generation)
    for x in range(0, 10):
        ind = population.getFittest(x)
        print(ind.fitness)
        print(ind.chromosome)
    pilimg = []
    img = []
    x = 0
    Fittest = population.getFittest(0)
    # draw the background
    pilimg.append(Image.open(r'images\background.png'))
    img.append(ImageTk.PhotoImage(pilimg[x]))
    imagesprite = can.create_image(
        890, 505, image=img[x])
    x += 1
    numOfItem = 0
    z_draw = []
    # sort the objects on z cor
    for item in Fittest.getChromosome():
        z_draw.append((item, lemma_dict[object_list[numOfItem]]))
        numOfItem += 1
    z_draw.sort(key=lambda x: x[0][2], reverse=True)
    # draw objects
    for item in z_draw:
        source = "images\\"+item[1]+".png"
        pilimg.append(Image.open(source))
        img.append(ImageTk.PhotoImage(pilimg[x]))
        print("x: "+str(item[0][0])+" y: " +
              str(item[0][1])+" z: " + str(item[0][2]))
        imagesprite = can.create_image(
            item[0][0], item[0][1], image=img[x])
        x += 1
    objects = json_object['objects']
    # draw hand list
    for item in hand_list:
        hand = objects[lemma_dict[item[0]]]
        hand = hand['hand']
        handx = hand[0]
        handy = hand[1]
        index = object_list.index(item[0])
        center = Fittest.getChromosome()
        center = center[index]
        centerHandX = handx*100+center[0]
        centerHandY = handy*100+center[1]
        source = "images\\"+lemma_dict[item[1]]+".png"
        pilimg.append(Image.open(source))
        img.append(ImageTk.PhotoImage(pilimg[x]))
        imagesprite = can.create_image(
            centerHandX, centerHandY, image=img[x])
        x += 1
    best_fitness_entry.delete(0, 'end')
    best_fitness_entry.insert(0, Fittest.getFitness())


def save_result():
    global resultNum
    save_as_png(can, 'result'+str(resultNum))
    resultNum += 1


root = tk.Tk()
root.state('zoomed')
root.title("Creating images from tests using Artificial Intelligence techniques")
root.iconbitmap('ico.ico')
EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.53.1\bin\gswin64c'
can = tk.Canvas(root, width=1780, height=1010)
frame = tk.LabelFrame(root)
frame.grid(row=0, column=0)
can.grid(row=0, column=1)
sentence_entry = tk.Text(frame, height=20, width=15, wrap='word')
#scrollbar = tk.Scrollbar(frame)
sentence_entry.insert(1.0, '''A boy is eating an apple.
The sun is shiny.
The boy is near a tree.''')
population_size_entry = tk.Entry(frame)
population_size_entry.insert(0, '500')
mutation_rate_entry = tk.Entry(frame)
mutation_rate_entry.insert(0, '0.01')
crossover_rate_entry = tk.Entry(frame)
crossover_rate_entry.insert(0, '0.9')
elitism_count_entry = tk.Entry(frame)
elitism_count_entry.insert(0, '20')
num_of_generations_entry = tk.Entry(frame)
num_of_generations_entry.insert(0, '100')
best_fitness_entry = tk.Entry(frame)
Found_solution_at_generation_entry = tk.Entry(frame)
sentence_label = tk.Label(frame, text='Enter your text')
population_size_label = tk.Label(frame, text='Population size')
mutation_rate_label = tk.Label(frame, text='Mutation rate')
crossover_rate_label = tk.Label(frame, text='Crossover rate')
elitism_count_label = tk.Label(frame, text='Elitism count')
num_of_generations_label = tk.Label(frame, text='Number of generations')
best_fitness_label = tk.Label(frame, text="Best fitness")
Found_solution_at_generation_label = tk.Label(
    frame, text="Found solution at generation")
sentence_label.grid(row=0, column=0)
population_size_label.grid(row=3)
mutation_rate_label.grid(row=5)
crossover_rate_label.grid(row=7)
elitism_count_label.grid(row=9)
num_of_generations_label.grid(row=11)
best_fitness_label.grid(row=13)
Found_solution_at_generation_label.grid(row=15)
sentence_entry.grid(row=1)
#scrollbar.grid(row=1, column=1, sticky="E", ipady="40")
population_size_entry.grid(row=4)
mutation_rate_entry.grid(row=6)
crossover_rate_entry.grid(row=8)
elitism_count_entry.grid(row=10)
num_of_generations_entry.grid(row=12)
best_fitness_entry.grid(row=14)
Found_solution_at_generation_entry.grid(row=16)
# sentence_entry.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=sentence_entry.yview)
lable1 = tk.Label(frame)
lable2 = tk.Label(frame)
lable3 = tk.Label(frame)
lable1.grid(row=17)
start_button = tk.Button(frame, text='Start', width=15, command=start_ga)
start_button.grid(row=18)
save_result_button = tk.Button(
    frame, text='Save result', width=15, command=save_result)
lable2.grid(row=19)
save_result_button.grid(row=20)
lable3.grid(row=21)
root.mainloop()
