###########################################################################
#   SALG - SNAKE AND LADDER GAME 
#
#    Copyright (C) 2022-2023 ARCHANA.V S <archanavs1211@gmail.com>
#    
#    FILL-VTB-INFO 
#    Supervised by Zendalona(2022-2023)
#
#    Project home page : www.zendalona.com/SNAKE AND LADDER GAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################
import cairo ,speechd ,math,time
import gi
import random
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk,GLib
class Player:
    def __init__(self, name, position,color):
        self.name = name
        self.position = position
        self.color=color
class GameBoard(Gtk.Window):
    def __init__(self,board_num,num_players,players_names):
        Gtk.Window.__init__(self, title="Game Board")
        self.set_default_size(500, 700)
        self.count = num_players
        color_rgb = Gdk.RGBA(1, 1, 1, 1)
        self.override_background_color(Gtk.StateFlags.NORMAL,color_rgb)
        self.speech = speechd.SSIPClient('game_board')  
        self.dice_number=1
        
       
        self.board_num = board_num
        self.connect("destroy", self.cleanup)
        
        grid = Gtk.Grid()
        self.add(grid)
       
        
        drawing_area = Gtk.DrawingArea()
        drawing_area.set_size_request(500, 700)
        drawing_area.connect("draw", self.draw_board)
        drawing_area.add_events(Gdk.EventMask.KEY_PRESS_MASK)
        self.connect("key-press-event", self.on_key_press)  
        
        
        
       
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.set_size_request(500,700)
        scrolled_window.add(drawing_area)
        self.current_cell= [9, 0]
       
       
        grid.attach(scrolled_window, 0, 0, 1, 1)
        
       
        

        '''button = Gtk.Button(label="Roll dice")
        button.connect("clicked", self.roll_dice)'''        
      
        grid.show_all()
        
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        self.players = [] 
        self.num_players = num_players
        self.players_names=players_names
        
        self.create_players()
        
        self.speech.speak(self.players_names[0]+"can roll dice by pressing the space bar")
   
    def create_players(self):
        colors = [(0.5, 0.3, 0), (0, 0.7, 0.4), (0.2, 0, 0.5), (0.6, 0.7, 0),(0.0,0.9,0.2)] 
        for i in range(self.num_players):
            player_name = self.players_names[i]
            player_color = colors[i % len(colors)] 
            player = Player(player_name, [9, 0],player_color)  
            self.players.append(player)
        if self.num_players == 1:
            player = Player("Machine", [9, 0], colors[1 % len(colors)])  
            self.players.append(player)
            self.num_players=2
            self.count =2
    def draw_board(self, widget, cr):
        
        cr.set_source_rgb(1, 1, 1)  
        cr.paint()
        
        
        cr.set_source_rgb(0, 0, 0)  
        for i in range(10):
            for j in range(10):
                cr.rectangle(i * 50, j * 50, 50, 50) 
                
                
                if self.board_num == 1: 
                    if (i+j) % 2 == 0:
                        cr.set_source_rgb(1, 1, 1)     
                                
                    else:
                        cr.set_source_rgb(0, 0, 1)     
	                           
	        
                    cr.fill_preserve()
                    cr.stroke() 
                    
                elif self.board_num == 2: 
                    if (i+j) % 2 == 0:
                        cr.set_source_rgb(0.5, 0, 0)     
                                
                    else:
                        cr.set_source_rgb(1, 1, 1)     
	                           
	        
                    cr.fill_preserve()
                    cr.stroke() 
                    
                elif self.board_num == 3: 
                    if (i+j) % 2 == 0:
                        cr.set_source_rgb(1, 1, 1)     
                                
                    else:
                        cr.set_source_rgb(0, 0.6, 0)     
	                           
	        
                    cr.fill_preserve()
                    cr.stroke() 
                    
                elif self.board_num == 4: 
                    if (i+j) % 2 == 0:
                        cr.set_source_rgb(1, 1, 1)     
                                
                    else:
                        cr.set_source_rgb(0, 0.3, 0.5)  
                    cr.fill_preserve()
                    cr.stroke()        
                elif self.board_num == 5: 
                    if (i+j) % 2 == 0:
                        cr.set_source_rgb(1, 1, 1)     
                                
                    else:
                        cr.set_source_rgb(0.7, 0, 0.5)  
	        
                    cr.fill_preserve()
                    cr.stroke() 
        square_size = 50
        num = 100
        for i in range(10):
            if i % 2 == 0:
                for j in range(10):
                    x = j * square_size
                    y = i * square_size
                    cr.set_source_rgb(0, 0, 0)  
                    cr.rectangle(x, y, square_size, square_size)
                    cr.stroke() 
                    cr.set_source_rgb(0, 0, 0)  
                    cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                    cr.set_font_size(20)
                    cr.move_to(x + square_size/2 , y + square_size/2 ) 
                    cr.show_text(str(num)) 
                    num -= 1  
            else:
                 for j in range(10):
                    x = (9 - j) * square_size  
                    y = i * square_size
                    cr.set_source_rgb(0, 0, 0)  
                    cr.rectangle(x, y, square_size, square_size)
                    cr.stroke() 
                    cr.set_source_rgb(0, 0, 0)
                    
                    cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                    cr.set_font_size(20)
                    cr.move_to(x + square_size/2 , y + square_size/2 )  
                    cr.show_text(str(num))  
                    num -= 1 
        cr.set_source_rgb(0.6, 0.7, 0.2)
        cr.set_line_width(5)
    
        line_sets = [
            
            [(460, 170), (460, 260)],
            [(210, 160), (370, 420)],
            [(205, 369), (260, 480)],
            [(210, 20), (160, 160)],
            [(10,360), (60, 210)],
            [(365, 165), (255, 70)],
            [(10,120), (115,30)]
            
        ]
    
        
        for line_set in line_sets :
            
            line1_start_x, line1_start_y = line_set[0]
            line1_end_x, line1_end_y = line_set[1]
    
            line2_start_x, line2_start_y = line1_start_x + 30, line1_start_y + 5
            line2_end_x, line2_end_y = line1_end_x + 30, line1_end_y + 5
    
            cr.move_to(line1_start_x, line1_start_y)
            cr.line_to(line1_end_x, line1_end_y)
            cr.stroke()
    
            cr.move_to(line2_start_x, line2_start_y)
            cr.line_to(line2_end_x, line2_end_y)
            cr.stroke()
    
            
            rung_count = 10  
            rung_height = (line2_end_y - line1_start_y) / (rung_count + 1)
    
            
            
            for j in range(1, rung_count + 1):
                rung_y = line1_start_y + (rung_height * j)
                         
                rung_start_x = line1_start_x + ((line1_end_x - line1_start_x) * (rung_y - line1_start_y) // (line1_end_y - line1_start_y))
                rung_end_x = line2_start_x + ((line2_end_x - line2_start_x) * (rung_y - line2_start_y) // (line2_end_y - line2_start_y))

                cr.move_to(rung_start_x, rung_y)
                cr.line_to(rung_end_x, rung_y)
                cr.stroke()

       
 
        
        
        width = 75
        height = 30
        cr.set_source_rgb(1, 0.0, 0.0)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(1.0, 0.0, 0.0) 
        cr.move_to(75, 32)  #snakebody
        cr.curve_to(190,50,100,210,180, 320)  
        cr.stroke()
        
        cr.set_line_width(2)#tongue
        cr.set_source_rgb(0.0, 0.0, 0.0) 
        cr.move_to(70, 30)  
        cr.curve_to(50, 60, 50, 30, 40, 30)  
        cr.stroke()
        
        width = 75 #eye1
        height = 35
        cr.set_source_rgb(0.0, 0.0, 0.0)
        radius = 2
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)
        cr.fill()
        
        width = 75 #eye2
        height = 20
        cr.set_source_rgb(0.0, 0.0, 0.0)
        radius = 2
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)
        cr.fill()
        
        cr.set_source_rgb(1, 0.5, 0.0)
        radius = 15
        cr.arc(120,370, radius, 0, 2 * 3.14)
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(1.0, 0.5, 0.0) 
        cr.move_to(125, 380)  #snakebody
        cr.curve_to(180, 450, 150, 450, 220, 480)  
        cr.stroke()
        
        
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(110,370,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(125,370,2,0, 2 * 3.14)
        cr.fill()
        
        cr.set_source_rgb(0.0, 0.5, 0.0)
        radius = 15
        cr.arc(420,70, radius, 0, 2 * 3.14)
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(0.0, 0.5, 0.0) 
        cr.move_to(420, 70)  #snakebody
        cr.curve_to(290,100,300,100,280, 220)  
        cr.stroke()
        
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(430,70,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(420,70,2,0, 2 * 3.14)
        cr.fill()
        
        cr.move_to(260, 240)#tail
        cr.line_to(275, 220)
        cr.line_to(280, 220)
        cr.close_path()
        cr.set_line_width(3)
        cr.set_source_rgb(0.0, 0.5, 0.0)
        cr.stroke()
        
        cr.move_to(190, 340)#tail
        cr.line_to(175, 320)
        cr.line_to(185, 315)
        cr.close_path()
        cr.set_line_width(3)
        cr.set_source_rgb(1, 0.0, 0.0)
        cr.fill()
        cr.stroke()
        
        cr.move_to(210, 480)#tail
        cr.line_to(230, 500)
        cr.line_to(215, 470)
        cr.close_path()
        cr.set_line_width(3)
        cr.set_source_rgb(1, 0.5, 0.0)
        cr.fill()
        cr.stroke()
        
        
        width = 420
        height = 270
        cr.set_source_rgb(0, 1.0, 1.0)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(0, 1.0, 1.0) 
        cr.move_to(420, 270)  #snakebody
        cr.curve_to(440,288,410,490,440, 420)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(410,270,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(425,260,2,0, 2 * 3.14)
        cr.fill()
        
        width = 270
        height = 320
        cr.set_source_rgb(1, 1.0, 0)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(1, 1.0, 0.0) 
        cr.move_to(270, 320)  #snakebody
        cr.curve_to(230,340,330,430,340, 470)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(265,320,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(275,320,2,0, 2 * 3.14)
        cr.fill()
        
        width = 420
        height = 270
        cr.set_source_rgb(0, 1.0, 1.0)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.set_source_rgb(0, 1.0, 1.0) 
        cr.move_to(420, 270)  #snakebody
        cr.curve_to(440,288,410,490,440, 420)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(410,270,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(425,260,2,0, 2 * 3.14)
        cr.fill()
        
        
        width = 220
        height = 220
        cr.set_source_rgb(0, 0.5, 1.0)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.move_to(220, 220)  #snakebody
        cr.curve_to(410,280,150,340,170, 360)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(220,210,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(220,225,2,0, 2 * 3.14)
        cr.fill()
        
        width = 70
        height = 120
        cr.set_source_rgb(0, 1, 0.5)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.move_to(70, 120)  #snakebody
        cr.curve_to(30,150,110,340,30, 230)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(70,110,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(70,125,2,0, 2 * 3.14)
        cr.fill()
        
        width = 330
        height = 30
        cr.set_source_rgb(0.9, 0.5, 0.5)
        radius = 15
        center_x = width 
        center_y = height 
        cr.arc(center_x, center_y, radius, 0, 2 * 3.14)#circle
        cr.fill()
        
        cr.set_line_width(10)
        cr.move_to(335, 40)  #snakebody
        cr.curve_to(490,90,350,200,430, 230)  
        cr.stroke()
        cr.set_source_rgb(0.0, 0.0, 0.0)#eyes
        cr.arc(330,20,2,0, 2 * 3.14)
        cr.fill()
        cr.arc(320,30,2,0, 2 * 3.14)
        cr.fill()
        
        
        
    
       
            
        dice_size = 50
        dice_x = 300  
        dice_y = 580  
    
       
        cr.set_line_width(2)
        cr.set_source_rgb(0, 0, 1)
        cr.rectangle(dice_x, dice_y, dice_size, dice_size)
        cr.stroke()
        dot_radius = 4
        dot_margin = 10
    
        dot_positions = [
        [],  # No dots for 0
        [(dice_x + dice_size / 2, dice_y + dice_size / 2)], 
        [(dice_x + dice_size / 4, dice_y + dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + 3 * dice_size / 4)],  
        [(dice_x + dice_size / 4, dice_y + dice_size / 4),
         (dice_x + dice_size / 2, dice_y + dice_size / 2),
         (dice_x + 3 * dice_size / 4, dice_y + 3 * dice_size / 4)], 
        [(dice_x + dice_size / 4, dice_y + dice_size / 4),
         (dice_x + dice_size / 4, dice_y + 3 * dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + 3 * dice_size / 4)], 
        [(dice_x + dice_size / 4, dice_y + dice_size / 4),
         (dice_x + dice_size / 4, dice_y + 3 * dice_size / 4),
         (dice_x + dice_size / 2, dice_y + dice_size / 2),
         (dice_x + 3 * dice_size / 4, dice_y + dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + 3 * dice_size / 4)],  
        [(dice_x + dice_size / 4, dice_y + dice_size / 4),
         (dice_x + dice_size / 4, dice_y + dice_size / 2),
         (dice_x + dice_size / 4, dice_y + 3 * dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + dice_size / 4),
         (dice_x + 3 * dice_size / 4, dice_y + dice_size / 2),
         (dice_x + 3 * dice_size / 4, dice_y + 3 * dice_size / 4)] 
    ]
        for dot_x, dot_y in dot_positions[self.dice_number]:
            dot_radius = 4
            cr.arc(dot_x, dot_y, dot_radius, 0, 2 * math.pi)
            cr.fill()
        cr.set_source_rgb(1, 0, 0)
        cr.move_to(18,520)
        cr.set_font_size(15)
        cr.show_text("Player Name") 
        cr.move_to(130,520)
        cr.show_text("Position")      
        i=20
        for player in self.players:
            x, y = self.get_cell_coordinates(player.position[0], player.position[1])
            cr.set_source_rgb(*player.color)
            cr.arc(x + square_size/2, y + square_size/2, 10, 0, 2 * math.pi)  
            cr.fill()
            
            cr.arc(25 , 515+i, 10, 0, 2 * math.pi)
            cr.fill()  
            cr.select_font_face("Arial", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(15)
            cr.move_to(50,520+i)
            cr.show_text(player.name)
            
            row=player.position[0]
            col=player.position[1]
            if(row % 2 != 0) :
                num = (9 - row) * 10 + col + 1
            else:
               num = (9 - row) * 10 +(9 - col) + 1 
            cr.move_to(160,520+i)
            cr.show_text(str(num))
            i+=30
            
         
	       
            cr.set_source_rgba(1, 0, 0.5, 0.2)
            x = player.position[1] * 50
            y = player.position[0] * 50
            cr.rectangle(x, y, 50, 50)
            
            #cr.set_source_rgb(1, 0, 0)  
            #cr.select_font_face("Arial", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
            #cr.set_font_size(18)
            #cr.move_to(x + square_size /2 - 8, y + square_size/2 + 8) 
            #cr.show_text(player.name) 
            cr.set_source_rgba(1, 1, 0, 0.3)
            cr.fill()
            
        #to mark the current position in gameboard
        x = self.current_cell[1] * 50
        y = self.current_cell[0] * 50
        cr.rectangle(x+5, y+5, 40, 40)
        cr.set_source_rgba(1, 0.2,0.4, 0.6)
        cr.fill()
        
       
    def get_cell_coordinates(self, row, column):
       
        x = column * 50
        y = row * 50
        return x, y

    def roll_dice(self):
        
        if self.check_game_over():
            return
    
        self.dice_number = random.randint(1, 6)
        self.speech.speak("you got a"+str(self.dice_number)+"on the dice")
        player = self.players[self.count % len(self.players)] 
        current_row, current_col = player.position[0], player.position[1]
        if current_row % 2 != 0:
            new_col = current_col + self.dice_number
            if new_col >= 10:
                new_col = 9
                count= self.dice_number- (10 - current_col)
                current_row -= 1
                new_col = new_col - count
        elif current_row % 2 == 0:
            new_col = current_col - self.dice_number
            if new_col < 0:
                count = new_col  
                new_col = 0
                current_row -= 1
                new_col -= count + 1
        if current_row < 0 :
            current_row =0
            new_col=current_col
            self.speech.cancel()
            self.speech.speak("the number is larger than the number you were hoping to win")
            
        player.position[0],player.position[1] = [current_row, new_col]
        self.count += 1 
        self.queue_draw() 
        
        self.speak_number(current_row, new_col,player)   
        player = self.players[self.count % len(self.players)] 
        if self.check_game_over():
            winner = self.get_winner()
            self.speech.speak("Congratulations, " + winner.name + " has won the game!")
        else:
            if player.name == "Machine":
                GLib.timeout_add(8000, self.roll_dice)
            else:    
                self.speech.speak(player.name+"can roll dice by pressing spacebar")
            
        
    def speak_number(self, row, col,player):
         
        if(row % 2 != 0) :
            number = (9 - row) * 10 + col + 1
            #self.speech.cancel() 
            self.speech.speak(player.name+"in position"+str(number))  
        else :
            number = (9 - row) * 10 +(9 - col) + 1
            #self.speech.cancel()  
            self.speech.speak(player.name+"in position"+str(number))  
        self.snakes = [ 23 , 35 , 49 , 56 , 79 , 89 , 94 , 99]
        self.ladders = [ 6 , 13 , 21 ,  50 , 64 , 68 , 80]
        if number in self.ladders:
            self.speech.speak("great !! You have found a ladder!")
            
            #time.sleep(0.5)
            self.move_player(player,number) 

        elif number in self.snakes:
            self.speech.speak("oops !! you are on a snake ")
           
            self.speech.speak("you have to move back!")
            #time.sleep(0.5)
            self.move_player(player,number) 
        else :
            for snake in self.snakes:
                if ( snake - number) <=6 and (snake -number) > 0 :
                    pos = snake -number
                    self.speech.speak("watch out !there is a snake at " + str(snake) +"and it is" +str(pos)+"position away from you")
            for ladder in self.ladders :
                if (ladder - number) <= 6 and (ladder - number) > 0:
                    pos = ladder - number
                    self.speech.speak(" there is a ladder at " + str(ladder) +"it is"+str(pos)+"position away from you")
                
            
    def move_player(self,player,number):
        time.sleep(2)
        
        if number == 6:
            end_pos = [7, 4]
        elif number == 13:
            end_pos = [3, 4]
        elif number == 21:
            end_pos = [4, 1]
        elif number == 50:
            end_pos = [3, 9]
        elif number == 64:
            end_pos = [0, 4]
        elif number == 68:
            end_pos = [1, 5]
        elif number == 80:
            end_pos = [0, 2]
        elif number == 23:
            end_pos = [ 9, 4 ]
        elif number == 35:
            end_pos = [9 , 6]
        elif number == 49:
            end_pos = [ 8, 8]
        elif number == 56 :
            end_pos = [ 7,3 ]
        elif number == 79 :
            end_pos = [ 4, 0 ]
        elif number == 89 :
            end_pos = [ 4 , 5]
        elif number == 94 :
            end_pos = [4 , 8 ]
        elif number == 99 :
            end_pos = [ 6, 3]
        
        player.position = end_pos
        self.queue_draw()
        self.speak_number(player.position[0], player.position[1], player)

    def cleanup(self, widget):
        self.speech.close() 
    
    
    def check_game_over(self):
        for player in self.players:
            if player.position[0] ==  0 and player.position[1] == 0:
                return True
        return False

    def get_winner(self):
        for player in self.players:
            if player.position[0] == 0 and player.position[1] == 0:
                return player
        return None
               
    def on_key_press(self, widget, event):
        keyval = event.keyval
        if keyval == Gdk.KEY_Left:
            self.move_current_cell(-1, 0)
        elif keyval == Gdk.KEY_Right:
            self.move_current_cell(1, 0)
        elif keyval == Gdk.KEY_Up:
            self.move_current_cell(0, -1)
        elif keyval == Gdk.KEY_Down:
            self.move_current_cell(0, 1)
        #check whether player pressed spacebar ,and execute roll_dice method
        elif keyval == Gdk.KEY_space:
            self.roll_dice()
        self.queue_draw()
        
    def move_current_cell(self, dx, dy):
        new_row = self.current_cell[0] + dy
        new_col = self.current_cell[1] + dx
        if 0 <= new_row < 10 and 0 <= new_col < 10:
            self.current_cell = [new_row, new_col]    
            self.speak(new_row,new_col)
            
            
    def speak(self,row,col):
        if(row % 2 != 0) :
            num = (9 - row) * 10 + col + 1
            self.speech.cancel() 
            self.speech.speak(str(num))  
        else :
            num = (9 - row) * 10 +(9 - col) + 1
            self.speech.cancel()  
            self.speech.speak(str(num))  
        snakes = [ 23 , 35 , 49 , 56 , 79 , 89 , 91 , 99]
        ladders = [ 6 , 13 , 21 ,  50 , 64 , 68 , 80]
        if num in snakes :
            self.speech.speak("its a snake")
        elif num in ladders:
            self.speech.speak("its a ladder")

