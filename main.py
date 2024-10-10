import turtle
import pandas as pd

SCREEN = turtle.Screen()
SCREEN.title('U.S States Game')
image = "blank_states_img.gif"
SCREEN.addshape(image)

turtle.shape(image)

# def get_mouse_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_coordinates)
# turtle.mainloop()

guessed_dict = {
    "list": [],
    "count": 0
}
states = pd.read_csv('50_states.csv')
states_count = len(states['state'])

def write_name_of_guessed_state(states_row):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    x,y = states_row.x, states_row.y
    pen.goto(x,y)
    pen.write(str(states_row.state))

def check_resp(gs_state, gs_record):
    for index, row in states.iterrows():
        if row.state == gs_state:
           gs_record['count'] += 1
           gs_record['list'].append(row.name)
           print(gs_record)
           write_name_of_guessed_state(row)
           break
    else:
       print("wrong answer", gs_state)

while guessed_dict['count'] <= states_count:
      state_guessed = SCREEN.textinput(title=f"{guessed_dict['count']} on {states_count}", prompt="Which state would you like to guess?")
      if state_guessed == "Exit" or state_guessed == None:
         unguessed_states = [state for state in states['state'] if state not in guessed_dict['list']]
         pd.DataFrame(unguessed_states, columns=["missed"]).to_csv('unguessed_states.csv')
         SCREEN.bye()
         break
      else:
        check_resp(state_guessed, guessed_dict)

SCREEN.exitonclick()

