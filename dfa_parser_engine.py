file_name, input_name = map(str, input().split())

f = open(input_name, "r")

counter = 0
sigma = []
states = []
final_states = []
start_state = []

transitions = []

f.readline()
f.readline()
f.readline()

for line in f:
    line = line.strip("\n")
    if line == "Sigma:":
        letter = f.readline().strip("\n")
        letter = letter.strip(" ")
        while letter != "End":
            sigma.append(letter)
            letter = f.readline().strip("\n")
            letter = letter.strip(" ")
        counter = counter + 1
        if counter != 3:
            f.readline()
            f.readline()
            f.readline()
    elif line == "States:":
        state = f.readline().strip("\n")
        state = state.strip(" ")
        while state != "End":
            lista_state = state.split(",")
            if(len(lista_state) == 1):
                states.append(state)
            else:
                lista_state[0] = lista_state[0].strip(" ")
                if lista_state[1] == "F":
                    final_states.append(lista_state[0])
                else:
                    start_state.append(lista_state[0])
                states.append(lista_state[0])
            state = f.readline().strip("\n")
            state = state.strip(" ")
        counter = counter + 1
        if counter != 3:
            f.readline()
            f.readline()
            f.readline()
    elif line == "Transitions:":
        transition = f.readline().strip("\n")
        transition = transition.strip(" ")
        while transition != "End":
            transitions.append(transition)
            transition = f.readline().strip("\n")
            transition = transition.strip(" ")
        counter = counter + 1
        if counter != 3:
            f.readline()
            f.readline()
            f.readline()

transitions_matrix = [[None for i in range(len(states))] for j in range(len(states))]

for i in range(len(transitions)):
    a,b,c = transitions[i].split(",")
    b = b.strip(" ")
    c = c.strip(" ")
    x = states.index(a)
    y = states.index(c)
    transitions_matrix[x][y] = b
    
if len(start_state) != 1:
    print("Error: There is more than one start state")
elif len(final_states) == 0:
    print("Error: There are no final states")
elif start_state[0] not in states:
    print("Error: The start state is not in the states list")
elif start_state[0] in final_states:
    print("Error: The start state is a final state")
elif len(states) < 3:
    print("Error: There are less than 3 states")
else:
    ok = True
    for i in range(len(transitions_matrix)):
        for j in range(len(sigma)):
            if transitions_matrix[i].count(sigma[j]) > 1:
                ok = False
    if ok == False:
        print("Error: There are more than one transition for the same state and letter")
    else:
        print("The DFA is correct")