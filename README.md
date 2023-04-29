---
abstract: |
  This paper presents a two-stage process for converting natural
  language text into a 3D scene. In the first stage, the text is
  analyzed to identify the objects in the scene and their spatial
  relationships. Natural language processing techniques are primarily
  used to extract this information. In the second stage, a virtual 3D
  coordinate system is assumed, and coordinates are assigned to the
  objects based on their relationships. A genetic algorithm is used to
  optimize the placement of objects in the scene. The paper also
  discusses the conversion of extracted features into quintuple
  relationships, which represent parts of the scene. These quintuple
  relationships are used to create three-part relationships between
  objects based on their spatial relationships. The paper presents a
  detailed explanation of the two-stage process and the steps involved
  in converting natural language text into a 3D scene.

title: Translating text to scene
---

# Introduction

This work is focused on analyzing and understanding written text in
natural language to create logical and realistic scenes. The process
involves two main stages. In the first stage, natural language
processing techniques are used to identify the objects in the scene and
the spatial relationships between them. The second stage assumes the
existence of a virtual 3D coordinate system and uses a genetic algorithm
to find suitable coordinates for the objects to achieve the largest
possible number of spatial relationships. The extracted features from
the text are converted into quintuple relationships, which represent a
part of a scene. The quintuple relationships are used to produce
three-part relationships in which there are three parties: the first and
second are objects, and the third party is the spatial relationship that
connects these two objects. This work provides a detailed explanation of
the techniques and algorithms used in each stage.

# The Idea of the text analysis

The first stage of the process focuses on analyzing and understanding
written text in natural language. In general, there are two main types
of information that we focus on inferring from the text: the objects
included in the scene and the spatial relationships between these
objects. For example, if we have the following text: \"There is a tree.
Two cats are around the tree. There is a bird above the tree. There is a
football.\" We can identify the following objects: a tree, two cats, a
bird, and a football. The spatial relationships between these objects
are: the cats are around the tree, and the bird is above the tree.
Knowing the spatial relationships between objects helps to create a more
logical and realistic scene. We primarily rely on natural language
processing techniques to identify objects and their relationships, and a
detailed explanation of these techniques and the first stage algorithm
will be provided. In the second stage, when we draw the scene, we assume
the existence of a virtual 3D coordinate system (x, y, z) network. Each
object in the scene has coordinates, which we infer from the objects and
spatial relationships identified in the first stage. The goal of this
stage is to find suitable coordinates for the objects to achieve the
largest possible number of spatial relationships. If the spatial
relationships are achieved, the scene will be more consistent with the
description in the text. The objects are also classified into
categories, and each category indicates the appropriate section of the
image to place an object. We use a genetic algorithm to determine the
coordinates of the objects, and a detailed explanation of the second
stage will be provided.

# Conversion of extracted features into quintuple relationships

After extracting the features from the text, quintuple relationships
will be extracted from these features. These quintuple relationships
represent (adverbial modifier of place, place adverbial, object of the
preposition, verb, subject) and this relationship represents a part of a
scene. An example of this is: \"Ahmad is playing football near the
tree\". In this sentence, the subject is \"Ahmad\", the verb is
\"play\", the object of the preposition is \"football\", the adverbial
modifier of place is \"near\", and the place adverbial is \"tree\". In
some sentences, the verb and the object of the preposition may be
missing or the adverbial and the adjectival modifier may be absent. The
purpose of this relationship is to be a pivotal stage that enables us to
produce three-part relationships in which there are three parties: the
first and second are objects, and the third party is the spatial
relationship that connects these two objects. We will explain these
relationships later, and there are several steps to extract quintuple
relationships.

### Analysis of extracted nmod relationships

In the previous stage, we were able to obtain all nmod relationships in
the input text, and this relationship has several types. We will go
through each type and extract the appropriate relationship from it.

### Analysis of nmod relationships whose origin is not a verb

In this stage, we will go through each nmod relationship whose origin is
not a verb and examine whether the type of this relationship is \"of\".
In this case, we will merge the two parties of the relationship into one
word and replace them with the dictionary with the new word. An example
of this is when the phrase \"cup of tea\" appears, there will be an nmod
relationship whose origin is \"cup\" and whose target is \"tea\", and
the relationship is of type \"of\". In this case, the two words will be
merged, and the result of the merge will be \"cupoftea\" so that it will
be treated as a single word and a single object because it is not
appropriate to treat each party as a separate object. As for those
relationships whose type is not \"of\", the quintuple relationship will
be created: (adverbial modifier of place, place adverbial, missing
value, missing value, subject). This relationship does not contain a
verb or subject, but only a subject with an adverbial of place and a
modifier related to this adverbial. The origin of the relationship will
be the subject, and the target will be the adjectival modifier, and the
relationship type will be the place adverbial.

### Analysis of nmod relations whose origin is a verb

These types of relationships are divided into two categories: the first
is of the agent type, and the second is the remainder. First category:
In this type, the pentadic relationship is created such that the object
of the verb is the agent, and the stable nmod relationship is the verb
itself. Then, we examine whether there is a second relationship whose
origin is this verb. In this case, the stable element is the adverbial
modifier related to location, and the modifier is the location itself.
If neither of these characteristics is present, the value will remain
null. An example of this is: \"A car is driven on the road by the
police\" In this sentence, there is an agent-type relationship whose
origin is the verb \"drive,\" and its stable element is the word
\"police.\" There is also an \"on\" type relationship whose origin is
the verb \"drive,\" and its stable element is the word \"road.\" The
resulting pentadic relationship is:\
(police, drive, car, on, road) However, if the sentence is in the form:\
\"A car is driven by the police\"\
The pentadic relationship would be:\
(police, drive, car, null, null) Second category: In this stage, we go
through each nmod relationship whose origin is a verb, then go through
each subject and object of this verb, considering all the subject-object
arrangements that apply to this verb, and considering the type of nmod
relationship to be the location modifier, with the stable relationship
being the modifier related to the adverbial modifier. The resulting
pentadic relationships are: (modifier related to the adverbial modifier,
location modifier, object, verb, subject) In some cases, there may be no
object for this verb. An example of this is: \"Ahmad and Lama are
playing football and chess near the tree under the sun\" The resulting
pentadic relationships are:\
(ahmad, play, football, near, tree)\
(ahmad, play, chess, near, tree)\
(ahmad, play, football, under, sun)\
(ahmad, play, chess, under, sun)\
(lama, play, football, near, tree)\
(lama, play, chess, near, tree)\
(lama, play, football, under, sun)\
(lama, play, chess, under, sun) In the previous sentence, we had two
nmod relationships for the verb \"play.\" The first is of the \"near\"
type, and its stable element is the word \"tree.\" The second is of the
\"under\" type, and its stable element is the word \"sun.\" We also had
two subjects and two objects for this verb, resulting in 2x2x2 = 8
pentadic relationships for this sentence, as previously explained. If
this verb is in the passive voice, the object of the verb becomes the
agent, and there will be no subject related to this relationship.

## Analysis of Non-nmod-Related Verbs

During this stage, we will examine verbs that are not part of the nmod
relationship. We will review each subject related to this verb and each
object affected by this verb, taking into consideration all
subject-object orders that pertain to this verb. We will create
quintuple relationships (null value, null value, object, verb, subject)
and in some cases, there may not be an object affected by this verb, as
in the following example:

Ahmad and Lama are playing football and chess.

The following quintuple relationships are generated:\
(ahmad, play, football, null, null)\
(ahmad, play, chess, null, null)\
(lama, play, football, null, null)\
(lama, play, chess, null, null) In the case where this verb is passive,
the subject pronoun will become the object pronoun and there will be no
subject related to this relationship.

### Analysis of Non-nmod-Related Verbs

During this stage, we will examine nsubj relationships that are not
related to a verb, where the subject is the stable element of the
relationship, and the starting point of the relationship is the
prepositional phrase indicating location, with the preposition being the
modifier of the element in question. We will add the relationship to the
list of relationships and create the quintuple relationship: (modifier,
preposition, null value, null value, subject). An example of this is:\
A car is on the road.\
In this sentence, we have an nsubj relationship, where the starting
point is the word \"road\" and the stable element is the word \"car\".
The preposition associated with the word \"road\" is \"on\", and the
resulting quintuple relationship is: (car, null, null, on, road)\
This relationship occurs when there is only a copular verb (e.g.,
\"is\") in the sentence and there is no nmod relationship. In this case,
the solution is to analyze the nsubj relationship.

###  Dealing with nouns not covered by relations

At this stage, we will go through nouns that have not been covered by
any pentagonal relation, and create a pentagonal relation that only has
an actor, where the actor is the noun itself. The relation will take the
following form: (null, null, null, null, actor) For example, the noun
\"sun\" will have a pentagonal relation in the following form: (sun,
null, null, null, null)

### Converting amod relations into object-specific adjectives

In this stage, we will examine amod relations and for each relation, we
will create an adjective relation that pertains to the object,
represented in the form of (adjective, object). For example: \"A black
car.\" In the above example, there is an amod relation originating from
the word \"car\" and its target is the adjective \"black\". The
resulting adjective relation will be represented as:

(car, black)

# Transformation of Quintuple Relations into Triple Relations with Actor-specific Attributes

In this stage, the quintuple relations inferred in previous stages will
be transformed into triple relations representing three entities. The
first entity is an object, the second entity is an object, and the third
entity is the spatial relation that connects these two objects. The
triple relation is represented as (Spatial Relation, Object 2, Object
1). For example, if Object 1 is above Object 2, the relation would be
represented as (Above, Object 2, Object 1). Several steps are involved
in achieving this stage.\
Each quintuple relation undergoes three stages: In this stage, it is
determined whether the quintuple relation contains a verb and an actor.
If present, the verb is checked against a dictionary of verbs. If the
verb is found in the dictionary and it connects the actor and the object
with a triple relation, the triple relation will be formed as (Relation,
Object, Actor). Additionally, if there are any actor-specific
attributes, a relational attribute of the form (Attribute, Actor) will
be created.\
In this stage, it is determined whether the quintuple relation contains
a location adverb and an object. If so, the corresponding relation for
the location adverb in the relation dictionary is searched. In this
case, two triple relations will be created for each of the actor and the
object if they are present individually. The two triple relations are
formed as (Relation, Adverbial Modifier, Actor) and (Relation, Adverbial
Modifier, Object).\
In this stage, if an actor or an object remains unhandled from the
previous stages, a fictitious triple relation is created containing only
the actor or the object in the first position of the relation. It is
formed as (Null Value, Null Value, Actor) or (Null Value, Null Value,
Object).\
Example: Let's consider the following quintuple relations:\
(ahmad, play, football, null, null)\
(car, null, null, on, road)\
(lama, play, football, near, tree)\
(cat, null, null, next_to, car)\
Verb Dictionary:\
\"play\": \[\"near\", \"happy\"\]\
Relation Dictionary:\
\"near\": \"near\",\
\"on\": \"on\",\
\"next_to\": \"near\"\
The corresponding triple relations are:\
(ahmad, football, near)\
(car, road, on)\
(lama, football, near)\
lama, tree, near)\
(football, tree, near)\
(cat, car, near)\
The inferred attributes are:\
(ahmad, happy)\
(lama, happy)

## Analysis of Nummod Relations and Repetition of Triple Relations

In this stage, each nummod relation is examined. If the first entity of
the triple relation is a part of a nummod relation, that relation is
repeated with the value of the number specified within the nummod
relation. However, in each repetition, the first entity in the triple
relation is a new object named after the object found in the first
entity of the triple relation.

## Identification of Entity List from Triple Relations

In this stage, the resulting triple relations are traversed. In each
relation, if either the first or the second entity, or both, are not
present in the entity list, they are added to the list. Each object is
associated with the sentence number it belongs to and its position as a
word within the sentence, ensuring a distinct value for each object.
When adding each object, we check if it exists in the dictionary of
scientific names. If it does, it is replaced with a male or female
object based on the dictionary. If it is not found, we check if the
object exists in the object dictionary. In that case, it is replaced
with the name representing that object. If the object is not found in
either of them, it is replaced with the unknown object represented by a
question mark symbol.

# Using Genetic Algorithms to Generate Suitable Coordinates for Objects

In this section, we will discuss the application of genetic algorithms
to achieve solutions that fulfill the desired relationships in the
image.

## Chromosome Structure

A chromosome representing a complete image is created by representing
the position of each element on the original image. Each gene within
this chromosome represents an element of the image, and the chromosome
is a sequence of genes.

## Generation of the First Generation

Each individual of the first generation is generated as follows:\
For each object in the image, a gene of three alleles is generated:\
- The first allele represents the position of the object on the x-axis.\
- The second allele represents the position of the object on the
y-axis.\
- The third allele represents the order of object placement. If object A
is placed before object B, object B will appear above object A in the
image.\
Each of the three values is randomly selected within the domain specific
to the image on the three axes.\
Example: \[(1,2,5),(4,2,1),(3,4,7)\]\
This individual represents a chromosome that contains three genes. Each
gene represents the position of an object in the image. In this example,
there are three objects, and we can understand their placement in the
figure (10-4) as follows:\
Object 1: (1,2,5)\
Object 2: (4,2,1)\
Object 3: (3,4,7)

## Crossover Operation

A parent individual is selected to undergo the crossover operation with
the current individual. The selection is performed using a roulette
wheel selection method, where the probability is associated with the
fitness of the individual. After the previous step, each gene from the
two parent individuals is examined, and a new gene is created with its
three values taken randomly between the values of the first parent
individual and the values of the second parent individual. Finally, the
new genes are assembled into a new chromosome (the offspring) and
transferred to the new generation.

Example: Let's consider the first parent individual
\[(1,2,5),(4,2,1),(3,4,7)\] and the second parent individual
\[(3,1,3),(5,3,1),(1,2,1)\]. The result of the crossover between the two
parents is \[(3,2,4),(5,2,1),(2,3,7)\].

## Mutation Operation

A gene is randomly selected and recreated using the previously mentioned
method.

Example: Consider the individual \[(1,2,5),(4,2,1),(3,4,7)\]. The result
of the mutation operation on this individual would be
\[(7,6,2),(4,2,1),(3,4,7)\].

## New Generation Selection

We iterate through the individuals of the current generation. If an
individual belongs to the elite, it is transferred to the new generation
without any modifications. However, if it does not belong to the elite,
we proceed as follows: if the crossover probability is met, we select an
individual from the current generation using the roulette wheel method
and apply the crossover operation between this individual and the
current individual. If the mutation probability is met, we apply the
mutation operation to the individual. Finally, this individual is
transferred to the new generation. In this way, the number of
individuals in the new generation remains equal to the number of
individuals in the current generation.

## Genetic Algorithm Parameters

These values were selected after experimental trials to achieve the best
results.\
Crossover rate: 90\
Mutation rate: 0.1\
Population size: 500 individuals\
Number of elite individuals: 20 individuals

## Termination Criterion

The termination criterion can be either reaching an individual with a
fitness score of 100% or reaching the allowed number of generations,
which is determined by the user.

## Fitness Function

The calculation of an individual's fitness score is of great importance,
as it determines the achievement of the desired result. It is calculated
as follows: We know that each individual has a chromosome composed of
multiple genes, and each gene represents the location and layer of a
specific object in the image. The fitness score is calculated based on
the fulfillment of the specific genes for each object within the
individual, which determine the desired spatial relationships.
Additionally, the presence of each object within the allowed boundaries
is considered, and the relationships and boundaries are weighted. Each
relationship has its own weight, meaning that not all relationships have
the same impact on the fitness score calculation.

For example, let's consider the individual with the chromosome
\[(1,2,5),(4,2,1),(3,4,7)\]. This chromosome represents the positioning
of three objects in the image. Assuming we have two relationships to be
fulfilled: the first relationship is \"on\" between object 1 and object
2 with a weighting value of 3, and the second relationship is \"far\"
between object 1 and object 3 with a weighting value of 3. The fitness
score calculation involves examining each relationship and checking if
the genes specific to the objects fulfill these relationships. If they
do, the weighting value is added to the fitness score.

# Results

Upon completion of the genetic algorithm, we obtain coordinates for each
primary object in the image. In the initial stage, we have assigned a
name to each object, indicating its nature. Now, we only need a set of
images representing each object. A collection of images representing a
large number of possible objects in the texts has been gathered. At this
stage, we have the ability to construct a comprehensive image by placing
an image representing each object at its respective coordinate. This
will result in an expressive image representing the entire text. The
appropriate background for this image remains to be determined, as well
as fulfilling the generated hand relationships from the initial stage.

## Examples

Example 1: Tom and Jerry are playing football next to the tree.\
Example 2: Dora is playing with a cat. the cat is next to a tree. Dora
is eating an apple. The sun is shining.\
Example 3: Ahmad and Lama are eating a sandwich. The sun is shining.\
Example 4: A car on the road.

[Result 1.]
![plot](https://github.com/AlaaAldinHajjar/NLP_Project/edit/main/image.jpg?raw=true)

[Result 2.]
![plot](https://github.com/AlaaAldinHajjar/NLP_Project/edit/main/image1.jpg?raw=true)

[Result 3.]
![plot](https://github.com/AlaaAldinHajjar/NLP_Project/edit/main/image2.jpg?raw=true)

[Result 4.]
![plot](https://github.com/AlaaAldinHajjar/NLP_Project/edit/main/image3.jpg?raw=true)

# Conclusion

The presented work proposes a two-stage process for converting natural
language text into a 3D scene. The first stage involves analyzing the
text to identify objects and spatial relationships using natural
language processing techniques. The second stage assumes a virtual 3D
coordinate system and assigns coordinates to the objects based on their
relationships, optimizing their placement using a genetic algorithm. The
work also discusses the conversion of extracted features into quintuple
relationships, representing parts of the scene, and further transforming
them into three-part relationships between objects. The paper provides a
detailed explanation of the techniques and algorithms used in each
stage.\
In conclusion, this work offers a methodology to convert natural
language text into a 3D scene by analyzing and understanding the text,
identifying objects and their spatial relationships, and assigning
coordinates to the objects. The proposed two-stage process provides a
systematic approach to create logical and realistic scenes based on
textual descriptions. The paper contributes to the field of natural
language understanding and computer graphics by bridging the gap between
textual information and visual representations.\
At the end our approach is salable and no need for NN training.



