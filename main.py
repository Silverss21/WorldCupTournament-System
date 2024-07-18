import flet as ft
from copy import copy

class Team():
    
    def __init__(self, country):
        self.country = country
        self.points = 0
        self.matches_played = 0
        self.won = 0
        self.draw = 0
        self.loss = 0
        self.goals_for = 0
        self.goals_against = 0
        self.goals_difference = 0
        
    def __lt__(self, other):
        if(self.points == other.points):
            if(self.goals_difference == other.goals_difference):
                return self.goals_for > other.goals_for
            else:
                return self.goals_difference > other.goals_difference
        else:
            return self.points > other.points
        
    def addMatch(self, gf, ga):
        self.matches_played += 1
        self.goals_for += gf
        self.goals_against += ga
        
        result = gf - ga
        self.goals_difference = self.goals_difference + result
        
        if(result > 0):
            self.won += 1
            self.points += 3
            
        if(result == 0):
            self.draw += 1
            self.points += 1
            
        if(result < 0):
            self.loss += 1


    
class Group():
    
    def __init__(self, group_name, team1, team2, team3, team4 ):
        self.title = group_name
        self.team_list = [team1, team2, team3, team4]
        self.closedGroupTeams = []
        self.winner_1 = None
        self.winner_2 = None
        
    def showGroup(self):
        print(self.title, ": ", self.team_list[0].country, " ,", self.team_list[1].country, " ,", self.team_list[2].country, " ,", self.team_list[3].country)
    
    def closeGroup(self):
        self.team_list.sort()
        t1 = copy(self.team_list[0])
        t2 = copy(self.team_list[1])
        t3 = copy(self.team_list[2])
        t4 = copy(self.team_list[3])
        self.closedGroupTeams = [t1, t2, t3, t4]
        self.winner_1 = self.team_list[0]
        self.winner_2 = self.team_list[1]
        
    
class Round16():
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = None
        self.team2_score = None
        self.round_winner = None
        
    def showRound(self):
        return print("Round 16 teams: ", self.team1.country, self.team2.country)
    
    def closeRound(self):
        if(self.team1_score > self.team2_score):
            self.round_winner = self.team1
        else:
            self.round_winner = self.team2
        
        return print("Round 16 between: [", self.team1.country, "] and [", self.team2.country, "] - winner: [", self.round_winner.country, "] ")
    
class QFinal():
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = None
        self.team2_score = None
        self.round_winner = None
        
    def showRound(self):
        return print("Quarter-finals teams: ", self.team1.country, self.team2.country)
    
    def closeRound(self):
        if(self.team1_score > self.team2_score):
            self.round_winner = self.team1
        else:
            self.round_winner = self.team2
            
        return print("Quarter-finals between: [", self.team1.country, "] and [", self.team2.country, "] - winner: [", self.round_winner.country, "] ")
        
class SFinal():
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2 
        self.team1_score = None
        self.team2_score = None
        self.round_winner = None
        
    def showRound(self):
        return print("Semi-finals teams: ", self.team1.country, self.team2.country)
    
    def closeRound(self):
        if(self.team1_score > self.team2_score):
            self.round_winner = self.team1
        else:
            self.round_winner = self.team2
            
        return print("Semi-finals between: [", self.team1.country, "] and [", self.team2.country, "] - winner: [", self.round_winner.country, "] ")

class Final():
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2 
        self.team1_score = None
        self.team2_score = None
        self.round_winner = None
        
    def showRound(self):
        return print("Final teams: ", self.team1.country, self.team2.country)
    
    def closeRound(self):
        list = [self.team1, self.team2]
        list.sort()
        self.round_winner = list[0]
        return print("Final between: [", self.team1.country, "] and [", self.team2.country, "] - winner: [", self.round_winner.country, "] ")

class RoundDisplay(ft.UserControl):
    
    # [Note]:    group_list = list of either round16, qfinal, sfinal, final from [App] class
    #            title = title to show - "Round 16", "Quarter-Final", etc...
    #            show_next_button  =  next button leads to another MatchCard
    #            nextButtonFunction  =  function from [App] class
    
    def __init__(self, groups_list, title = "", nextButtonFunction = None, show_next_button = False):
        super().__init__()
        self.group_list = groups_list
        self.title = title
        self.nextButtonFunction = nextButtonFunction
        self.show_next_button = show_next_button
    
    
    # [Note]: button will always pass 'event' to function, and we don't want to pass anything, that's why we have this function ( "e" is that event )
    
    def nextMatches(self, e):
        self.nextButtonFunction()
    
    
    
    def build(self):
        
        # [Note]: This is our view... everything will be inside 
        
        self.view = ft.Column()
        
        
        
        # [Note]: Title label
        
        self.view.controls.append(
            ft.Container(content=(
                    ft.Text(self.title, size=24, weight=ft.FontWeight.W_800)
                ),
                alignment=ft.alignment.center   
            )
        )
        
        
        # [Note]: For each round from array/list create a display
        
        for r in self.group_list:
            self.view.controls.append(
                ft.Container(content=(
                    ft.Container(
                        ft.Column([
                            ft.Row([
                                ft.Text("Team 1", size=16, color="#AAAAAA", width=220),
                                ft.Text(" - ", size=16, color="#AAAAAA", width=100),
                                ft.Text(" - ", size=16, color="#AAAAAA", width=100),
                                ft.Text("Team 2", size=16, color="#AAAAAA", width=180)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN ),
                            ft.Row([
                                ft.Text(r.team1.country, size=16, width=220, weight=ft.FontWeight.W_800),
                                ft.Text(r.team1_score, size=16, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(r.team2_score, size=16, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(r.team2.country, size=16, width=180, weight=ft.FontWeight.W_800),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN ),
                        ],
                        spacing=10,
                        width=660,
                        alignment=ft.MainAxisAlignment.CENTER,
                       ),
                        padding=20,
                        width=700,
                        border_radius=10,
                        border=ft.border.all(2, "#999999")
                    )
                ),
                alignment=ft.alignment.center,
                )
            )
            
            
        # [Note]: Row with empty container
        self.next_button = ft.Row([ft.Container()], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        # [Note]: Do we show next_button ? If TRUE then add button to Row above /\
        if(self.show_next_button == True):
            self.next_button.controls.append(ft.ElevatedButton("Next", on_click=self.nextMatches))
            
        # [Note]: Add this Row /\ to our view 
        self.view.controls.append(ft.Container(content=(
                    ft.Container(
                        ft.Column([self.next_button],
                        spacing=10,
                        width=600,
                        alignment=ft.MainAxisAlignment.CENTER,
                       ), padding=20, width=700, )
                ), alignment=ft.alignment.center, )
            )
            
        return self.view

class GroupsDisplay(ft.UserControl):
    
    
    # [Note]:    groups_list = list of self.groups from [App] class
    #            show_next_button  =  next button leads to another MatchCard
    #            nextButtonFunction  =  function from [App] class
    
    def __init__(self, groups_list, show_next_button = False, nextMatchesFunction = None):
        super().__init__()
        self.group_list = groups_list
        self.showButton = show_next_button
        self.nextMatchesFunction = nextMatchesFunction
        
    
    
    # [Note]: button will always pass 'event' to function, and we don't want to pass anything, that's why we have this function ( "e" is that event )
    
    def nextMatches(self, e):
        self.nextMatchesFunction()
    
    
    
    
    def build(self):
        
        
        # [Note]: This is our view... everything will be inside 
        self.view = ft.Column()
        
        
        
        # [Note]: for every group inside groups_list create a display/table
        
        for group in self.group_list:
            self.view.controls.append(
                ft.Container(content=(
                    ft.Container(
                        ft.Column([
                            ft.Row([
                                ft.Text(group.title, size=20, color="#AAAAAA", weight=ft.FontWeight.W_900, width=200),
                                ft.Text("MP", size=20, color="#AAAAAA", width=100),
                                ft.Text("W", size=20, color="#AAAAAA", width=100),
                                ft.Text("D", size=20, color="#AAAAAA", width=100),
                                ft.Text("L", size=20, color="#AAAAAA", width=100),
                                ft.Text("GF", size=20, color="#AAAAAA", width=100),
                                ft.Text("GA", size=20, color="#AAAAAA", width=100),
                                ft.Text("GD", size=20, color="#AAAAAA", width=100),
                                ft.Text("Pts", size=20, color="#AAAAAA", width=100),
                            ]),
                            ft.Row([
                                ft.Text(group.closedGroupTeams[0].country, size=20, width=200, weight=ft.FontWeight.W_800),
                                ft.Text(group.closedGroupTeams[0].matches_played, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].won, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].draw, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].loss, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].goals_for, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].goals_against, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].goals_difference, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[0].points, size=20, width=100, weight=ft.FontWeight.W_600),
                            ]),
                            ft.Row([
                                ft.Text(group.closedGroupTeams[1].country, size=20, width=200, weight=ft.FontWeight.W_800),
                                ft.Text(group.closedGroupTeams[1].matches_played, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].won, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].draw, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].loss, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].goals_for, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].goals_against, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].goals_difference, size=20, width=100, weight=ft.FontWeight.W_600),
                                ft.Text(group.closedGroupTeams[1].points, size=20, width=100, weight=ft.FontWeight.W_600),
                            ]),
                            ft.Row([
                                ft.Text(group.closedGroupTeams[2].country, size=20, width=200),
                                ft.Text(group.closedGroupTeams[2].matches_played, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].won, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].draw, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].loss, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].goals_for, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].goals_against, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].goals_difference, size=20, width=100),
                                ft.Text(group.closedGroupTeams[2].points, size=20, width=100),
                            ]),
                            ft.Row([
                                ft.Text(group.closedGroupTeams[3].country, size=20, width=200),
                                ft.Text(group.closedGroupTeams[3].matches_played, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].won, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].draw, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].loss, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].goals_for, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].goals_against, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].goals_difference, size=20, width=100),
                                ft.Text(group.closedGroupTeams[3].points, size=20, width=100),
                            ]),
                        ],
                        spacing=10,
                        width=1100,
                        alignment=ft.MainAxisAlignment.CENTER,
                       ),
                        padding=20,
                        width=1200,
                        border_radius=10,
                        border=ft.border.all(2, "#999999")
                    )
                ),
                alignment=ft.alignment.center,
                )
            )
            
        
        
        # [Note]: end of for loop
        
        # [Note]: Create row with empty container inside
        self.next_button = ft.Row([ft.Container()], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        
        # [Note]: If TRUE then add button to this Row /\
        if(self.showButton == True):
            self.next_button.controls.append(ft.ElevatedButton("Next", on_click=self.nextMatches))
            
            
        # [Note]: Add this row /\ to our view
        
        self.view.controls.append(ft.Container(content=(
                    ft.Container(
                        ft.Column([self.next_button],
                        spacing=10,
                        width=600,
                        alignment=ft.MainAxisAlignment.CENTER,
                       ), padding=20, width=700, )
                ), alignment=ft.alignment.center, )
            )
            
        return self.view
        
class MatchCard(ft.UserControl):
    
    def __init__(self, createMatchFunction, round_name, team1, team2, score_1=None, score_2=None):
        super().__init__()
        self.round_name = round_name
        self.team1 = team1
        self.team2 = team2
        self.score_1 = score_1
        self.score_2 = score_2
        self.createMatchFunction = createMatchFunction
    
    def build(self):
        
        self.error_text = ft.Text("", color="#DD1111", size=16, weight=ft.FontWeight.W_900)
        
        self.score_1_inputField = ft.TextField(hint_text="0", expand=False, autofocus=True, value=self.score_1)
        self.score_2_inputField = ft.TextField(hint_text="0", expand=False, autofocus=True, value=self.score_2)
        
        self.match_between = "Match between: " + str(self.team1.country) + " - " + str(self.team2.country)
        
        self.match_tab = ft.Container(
            content = ft.Column([
                    self.error_text,
                    ft.Text(self.round_name, size=24, weight=ft.FontWeight.W_900),
                    ft.Text(self.match_between, size=16, weight=ft.FontWeight.W_500),
                    ft.Row([
                        self.score_1_inputField,
                        ft.Text(" - "),
                        self.score_2_inputField
                    ]),
                    ft.Row([
                        ft.Container(),
                        ft.ElevatedButton("Submit match", on_click=self.createMatch)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ],
                spacing=20,
                width=600,
                alignment=ft.MainAxisAlignment.CENTER,
               ),
            alignment=ft.alignment.center,
            margin=20,
        )
        
        return self.match_tab
    
    def createMatch(self, e):
        score1 = self.score_1_inputField.value
        score2 = self.score_2_inputField.value
        
        if(score1 == None or score1 == ""):
            score1 = 0
        if(score2 == None or score2 == ""):
            score2 = 0
        self.createMatchFunction(self, self.team1, self.team2, score1, score2)
        

class GroupCard(ft.UserControl):
    
    def __init__(self, backFunction, createFunction, group_name, t1=None, t2=None, t3=None, t4=None):
        super().__init__()
        self.group_name = group_name
        self.createGroupFunction = createFunction
        self.backFunction = backFunction
        self.t1_name = t1
        self.t2_name = t2
        self.t3_name = t3
        self.t4_name = t4
    
    def build(self):
        
        
        self.error_text = ft.Text("", color="#DD1111", size=16, weight=ft.FontWeight.W_900)
        
        
        
        # [Note]: If we create [Group A] - we don't want back button
        if(self.group_name == "Group A"):
            backButton = ft.Container()
        else:
            backButton = ft.ElevatedButton("Back", on_click=self.backGroup)
        
        
        
        self.team_1_inputField = ft.TextField(hint_text="Team 1 Name", expand=False, autofocus=True, value=self.t1_name)
        self.team_2_inputField = ft.TextField(hint_text="Team 2 Name", expand=False, autofocus=False, value=self.t2_name)
        self.team_3_inputField = ft.TextField(hint_text="Team 3 Name", expand=False, autofocus=False, value=self.t3_name)
        self.team_4_inputField = ft.TextField(hint_text="Team 4 Name", expand=False, autofocus=False, value=self.t4_name)
        
        
        
        self.team_tab = ft.Container(
            content = ft.Column([
                    self.error_text,
                    ft.Text(self.group_name, size=24, weight=ft.FontWeight.W_900),
                    self.team_1_inputField,
                    self.team_2_inputField,
                    self.team_3_inputField,
                    self.team_4_inputField,
                    ft.Row([
                        backButton,
                        ft.ElevatedButton("Submit group", on_click=self.createGroup)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ],
                spacing=20,
                width=600,
                alignment=ft.MainAxisAlignment.CENTER,
               ),
            alignment=ft.alignment.center,
            margin=20,
        )
        
        return self.team_tab
    
    
    # [Note]: This calls function inside [App] to save data of this group and go back 1 group
    def backGroup(self, e):
        t1_val = self.team_1_inputField.value
        t2_val = self.team_2_inputField.value
        t3_val = self.team_3_inputField.value
        t4_val = self.team_4_inputField.value
        
        self.backFunction(self, t1_val, t2_val, t3_val, t4_val)
    
    
    # [Note]: This calls function inside [App] to create [Group] with [Teams]
    def createGroup(self, e):
        t1_val = self.team_1_inputField.value
        t2_val = self.team_2_inputField.value
        t3_val = self.team_3_inputField.value
        t4_val = self.team_4_inputField.value
        
        # [Note]: Verifying if InputFields are empty and showing [Error] is so
        if(t1_val == "" or t1_val == None):
            self.error_text.value = "Input Team 1 name!"
            return self.update()
        if(t2_val == "" or t2_val == None):
            self.error_text.value = "Input Team 2 name!"
            return self.update()
        if(t3_val == "" or t3_val == None):
            self.error_text.value = "Input Team 3 name!"
            return self.update()
        if(t4_val == "" or t4_val == None):
            self.error_text.value = "Input Team 4 name!"
            return self.update()
        
        # [Note]: calling create function
        self.createGroupFunction(self, t1_val, t2_val, t3_val, t4_val)
    
class Topbar(ft.UserControl):
    
    
    # [Note]: When there is only one button "Autofill" then we pass only 'customFunction' that leads to specific autofill function in [App] class
    #   customFunction  -  function from [App] class
    #   lastTopbar  -  if TRUE that means that this is our last Topbar... this will show buttons for Groups table, Round16 table, Qfinal, etc... 
    #   other functions (r16, qf...) are for passing functions that will show these /\ tables 
    
    def __init__(self, customFunction=None, lastTopbar=False, r16=None, qf=None, sf=None, f=None):
        super().__init__()
        self.customFunction = customFunction
        self.lastTopbar = lastTopbar
        self.previewRound16 = r16
        self.previewQFinals = qf
        self.previewSFinals = sf
        self.previewFinal = f
        
    def click_handler(self, e):
        self.customFunction()
        
    def round16_handler(self, e):
        self.previewRound16()
        
    def qfinals_handler(self, e):
        self.previewQFinals()
        
    def sfinals_handler(self, e):
        self.previewSFinals()
        
    def final_handler(self, e):
        self.previewFinal()
    
    
    
    
    def build(self):
        
        # [Note]: If this is not last Topbar then show button "Autofill" with function 'self.customFunction'
        
        if(self.lastTopbar == False):
            self.tmp = ft.Container(
                    ft.Row([
                        ft.Container(), 
                        ft.ElevatedButton("Autofill", on_click=self.click_handler)
                    ], 
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                )
        else:
            
            # [Note]: This is our last Topbar  =  show buttons for showing tables 
            
            self.tmp = ft.Column([
                ft.Row([
                    ft.Container(), 
                    ft.ElevatedButton("Groups", on_click=self.click_handler, bgcolor=('#8A1538'), color=('#FFFFFF') ),
                    ft.ElevatedButton("Round 16", on_click=self.round16_handler, bgcolor=('#8A1538'), color=('#FFFFFF') ),
                    ft.ElevatedButton("Quarter-Final", on_click=self.qfinals_handler, bgcolor=('#8A1538'), color=('#FFFFFF') ),
                    ft.ElevatedButton("Semi-Final", on_click=self.sfinals_handler, bgcolor=('#8A1538'), color=('#FFFFFF') ),
                    ft.ElevatedButton("Final", on_click=self.final_handler, bgcolor=('#8A1538'), color=('#FFFFFF') ), 
                    ft.Container()
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Container()
            ])
            
        return self.tmp
        

class App(ft.UserControl):
    
    
    #  self.view  = our view ( everything under AppBar )
    #  self.assigned_groups  =  amount of groups that we assigned
    #  self.teams, self.groups... list of data classes
    #  self.group_names  -  so we know what title we should name group ( based on assigned_groups )
    #  self.match_index  -  which match is it
    #  self.matches_schedule  -  correct order of matches >> from what list we should take ; which object from that list ; that team play with what team
    
    def __init__(self):
        super().__init__()
        self.view = ft.Column()
        self.assigned_groups = 0
        self.teams = []
        self.groups = []
        self.group_names = [ "Group A",  "Group B", "Group C", "Group D",  "Group E",  "Group F", "Group G", "Group H" ]
        self.round16 = []
        self.qfinal = []
        self.sfinal = []
        self.final = []
        self.match_index = 0
        self.matches_schedule = [
            ["groups", 0, 0, 1],
            ["groups", 0, 0, 2],
            ["groups", 0, 0, 3],
            ["groups", 0, 1, 2],
            ["groups", 0, 1, 3],
            ["groups", 0, 2, 3],
            ["groups", 1, 0, 1],
            ["groups", 1, 0, 2],
            ["groups", 1, 0, 3],
            ["groups", 1, 1, 2],
            ["groups", 1, 1, 3],
            ["groups", 1, 2, 3],
            ["groups", 2, 0, 1],
            ["groups", 2, 0, 2],
            ["groups", 2, 0, 3],
            ["groups", 2, 1, 2],
            ["groups", 2, 1, 3],
            ["groups", 2, 2, 3],
            ["groups", 3, 0, 1],
            ["groups", 3, 0, 2],
            ["groups", 3, 0, 3],
            ["groups", 3, 1, 2],
            ["groups", 3, 1, 3],
            ["groups", 3, 2, 3],
            ["groups", 4, 0, 1],
            ["groups", 4, 0, 2],
            ["groups", 4, 0, 3],
            ["groups", 4, 1, 2],
            ["groups", 4, 1, 3],
            ["groups", 4, 2, 3],
            ["groups", 5, 0, 1],
            ["groups", 5, 0, 2],
            ["groups", 5, 0, 3],
            ["groups", 5, 1, 2],
            ["groups", 5, 1, 3],
            ["groups", 5, 2, 3],
            ["groups", 6, 0, 1],
            ["groups", 6, 0, 2],
            ["groups", 6, 0, 3],
            ["groups", 6, 1, 2],
            ["groups", 6, 1, 3],
            ["groups", 6, 2, 3],
            ["groups", 7, 0, 1],
            ["groups", 7, 0, 2],
            ["groups", 7, 0, 3],
            ["groups", 7, 1, 2],
            ["groups", 7, 1, 3],
            ["groups", 7, 2, 3],
            ["round16", 0, 0, 1],
            ["round16", 1, 0, 1],
            ["round16", 2, 0, 1],
            ["round16", 3, 0, 1],
            ["round16", 4, 0, 1],
            ["round16", 5, 0, 1],
            ["round16", 6, 0, 1],
            ["round16", 7, 0, 1],
            ["qfinal", 0, 0, 1],
            ["qfinal", 1, 0, 1],
            ["qfinal", 2, 0, 1],
            ["qfinal", 3, 0, 1],
            ["sfinal", 0, 0, 1],
            ["sfinal", 1, 0, 1],
            ["final", 0, 0, 1],
        ]
    
    def build(self):
        
        topbar = Topbar(lambda: self.autoFillMatches("group_names"))
        
        self.view.controls.append(topbar)
        
        group_card = GroupCard(self.backGroups, self.createGroup, "Group A")
        
        self.view.controls.append(group_card)
        
        # ---------------------- View ----------------------
        
        return ft.Column(
            controls=[
                self.view,
            ],
        )
    
    
    # =============================================================================================
    #                                    SHOW TABLES
    # =============================================================================================
    
    
    # this is function for last Topbar,  it takes 1 parameter > which table should we open 
    #  it clears page and add new Topbar along with table 
    
    def showTable(self, tableType):
        
        self.view.controls.clear()
        
        topbar = Topbar(
            lambda: self.showTable("groups"), 
            True, 
            lambda: self.showTable("round16"),
            lambda: self.showTable("qfinal"),
            lambda: self.showTable("sfinal"),
            lambda: self.showTable("final")
        )
        self.view.controls.append(topbar)
        
        if(tableType == "groups"):
            card = GroupsDisplay(self.groups, False, None)
            
        elif(tableType == "round16"):
            card = RoundDisplay(self.round16, "Round 16", None, False)
            
        elif(tableType == "qfinal"):
            card = RoundDisplay(self.qfinal, "Quarter-Final", None, False)
            
        elif(tableType == "sfinal"):
            card = RoundDisplay(self.sfinal, "Semi-Final", None, False)
            
        elif(tableType == "final"):
            card = RoundDisplay(self.final, "Final", None, False)
            
            
        self.view.controls.append(card)
        return self.update()
    
    
    
    # =============================================================================================
    #                                    SHOW MATCH TAB
    # =============================================================================================
    
    
    
    # after showing table after each stage, next thing is to show [MatchCard], but we need to know which stage it will be, so we can pass correct autofill function to Topbar
    
    def showMatchTab(self, title):
        
        # [Note]: Clear page
        self.view.controls.clear()
        
        # [Note]: Get round index from matches schedule
        round_index = self.matches_schedule[self.match_index][1]
        
        if(title == 'Round 16'):
            t1 = self.round16[round_index].team1
            t2 = self.round16[round_index].team2
            topbar = Topbar(lambda: self.autoFillMatches("round16"))
            
        elif(title == 'Quarter-Final'):
            t1 = self.qfinal[round_index].team1
            t2 = self.qfinal[round_index].team2
            topbar = Topbar(lambda: self.autoFillMatches("qfinal"))
            
        elif(title == 'Semi-Final'):
            t1 = self.sfinal[round_index].team1
            t2 = self.sfinal[round_index].team2
            topbar = Topbar(lambda: self.autoFillMatches("sfinal"))
            
        elif(title == 'Final'):
            t1 = self.final[0].team1
            t2 = self.final[0].team2
        
        match_card = MatchCard(self.createMatch, title, t1, t2)
        
        if(title != 'Final'):
            self.view.controls.append(topbar)
        
        self.view.controls.append(match_card)
        self.view.update()        
            
            
            
            
    # =============================================================================================
    #                                    CREATE MATCH
    # =============================================================================================
    
    
    
    def createMatch(self, component, team1, team2, score1, score2):
        
        # [Note]: Add match data to Team 
        self.addMatch(team1, team2, score1, score2)
        
        # [Note]: Add match data to Round 
        roundType = self.matches_schedule[self.match_index][0]
        roundIndex = self.matches_schedule[self.match_index][1]
        
        self.addScoreToRound(roundType, roundIndex, score1, score2)
        
        
        self.view.controls.remove(component)
        self.match_index += 1
        
        
        # =======================================================================
        #               LAST MATCH ?
        
        
        # [Note]: Last match of [Groups]
        # ----------------------------------
        if(self.match_index == 48):
            
            # [Note]: delete Topbar
            self.view.controls.clear()
            
            # [Note]: close groups and create [Round16] classes
            for g in self.groups:
                g.closeGroup()
                
            self.createRound16Classes()
            
            # [Note]: display table
            card = GroupsDisplay(self.groups, True, lambda: self.showMatchTab("Round 16"))
            self.view.controls.append(card)
            return self.update()
        
        
        
        # [Note]: Last match of [Round16]
        # ----------------------------------
        if(self.match_index == 56):
            
            # [Note]: delete Topbar, close Rounds, create next classes and display table
            self.view.controls.clear()
            
            for i in range(0, 4):
                t1 = i * 2
                t2 = (i * 2) + 1
                self.round16[t1].closeRound()
                self.round16[t2].closeRound()
                self.qfinal.append(QFinal(self.round16[t1].round_winner, self.round16[t2].round_winner))
                
                
            card = RoundDisplay(self.round16, "Round 16", lambda: self.showMatchTab("Quarter-Final"), True)
            self.view.controls.append(card)
            return self.update()
        
        
        
        
        # [Note]: Last match of [QFinal]
        # ----------------------------------
        if(self.match_index == 60):
            
            # [Note]: delete Topbar, close Rounds, create next classes and display table
            self.view.controls.clear()
            
            for i in range(0, 2):
                t1 = i * 2
                t2 = (i * 2) + 1
                self.qfinal[t1].closeRound()
                self.qfinal[t2].closeRound()
                self.sfinal.append(SFinal(self.qfinal[t1].round_winner, self.qfinal[t2].round_winner))
                
            card = RoundDisplay(self.qfinal, "Quarter-Final", lambda: self.showMatchTab("Semi-Final"), True)
            self.view.controls.append(card)
            return self.update()
            
            
            
        #  [Note]: Last match of [SFinal]
        # ----------------------------------
        if(self.match_index == 62):
            
            # [Note]: delete Topbar, close Rounds, create next classes and display table
            self.view.controls.clear()
            
            self.sfinal[0].closeRound()
            self.sfinal[1].closeRound()
            self.final.append(Final(self.sfinal[0].round_winner, self.sfinal[1].round_winner))
            
            card = RoundDisplay(self.sfinal, "Semi-Final", lambda: self.showMatchTab("Final"), True)
            self.view.controls.append(card)
            return self.update()
        
        
        #  [Note]: Last match of [Final]
        # ---------------------------------- ---[TODO change function here \/ ]-------------
        if(self.match_index == 63):
            print(self.final)
            self.view.controls.clear()
            
            self.final[0].closeRound()
            
            topbar = Topbar(
                lambda: self.showTable("groups"), 
                True, 
                lambda: self.showTable("round16"),
                lambda: self.showTable("qfinal"),
                lambda: self.showTable("sfinal"),
                lambda: self.showTable("final")
            )
            self.view.controls.append(topbar)
            
            card = RoundDisplay(self.final, "Final", None, False)
            self.view.controls.append(card)
            return self.update()
        
        
        
        
        
        # =======================================================================
        #               ANOTHER MATCH CARD
        # -----------------------------------------------------------------------
        
        
        roundType = self.matches_schedule[self.match_index][0]
        roundIndex = self.matches_schedule[self.match_index][1]
        
        if(roundType == "groups"):
            
            # [Note]: Get group name from [Group] class
            round_name = self.groups[roundIndex].title
            
            t1_index = self.matches_schedule[self.match_index][2]
            t2_index = self.matches_schedule[self.match_index][3]
            
            # [Note]: Get object of [Team] class from [Group]
            t1 = self.groups[roundIndex].team_list[t1_index]
            t2 = self.groups[roundIndex].team_list[t2_index]
            
            match_card = MatchCard(self.createMatch, round_name, t1, t2)
            
        if(roundType == "round16"):
            
            round_name = "Round 16"
            
            t1 = self.round16[roundIndex].team1
            t2 = self.round16[roundIndex].team2
            
            match_card = MatchCard(self.createMatch, round_name, t1, t2)
            
        if(roundType == "qfinal"):
            
            round_name = "Quarter-Final"
            
            t1 = self.qfinal[roundIndex].team1
            t2 = self.qfinal[roundIndex].team2
            
            match_card = MatchCard(self.createMatch, round_name, t1, t2)
            
        if(roundType == "sfinal"):
            
            round_name = "Semi-Final"
            
            t1 = self.sfinal[roundIndex].team1
            t2 = self.sfinal[roundIndex].team2
            
            match_card = MatchCard(self.createMatch, round_name, t1, t2)
            
            
            
        self.view.controls.append(match_card)
        self.update()
    
    
    
    # =============================================================================================
    #                                    CUSTOM FUNCTIONS
    # =============================================================================================
    
    
    def addMatch(self, team_1, team_2, t1_goals, t2_goals):
    
        def checkTeam(team):
            if(isinstance(team, Team)):
                return True
            else:
                print("[ERROR]: Team parameter is not a Team class")
                return False

        def checkScore(score):
            if(isinstance(score, int)):
                if(score >= 0):
                    return True
                else:
                    print("[ERROR]: Match goal parameter is a negative integer !")
                    return False
            else:
                print("[ERROR]: Match goal parameter is not an integer !")
                return False

        if(checkTeam(team_1) == False): 
            return
        if(checkTeam(team_1) == False): 
            return

        if(checkScore(int(t1_goals)) == False): 
            return
        if(checkScore(int(t2_goals)) == False): 
            return

        team_1.addMatch(int(t1_goals), int(t2_goals))
        team_2.addMatch(int(t2_goals), int(t1_goals))
        
        
        
        
        
    def addScoreToRound(self, roundType, roundIndex, score1, score2):
        
        if(roundType == "round16"):
            self.round16[roundIndex].team1_score = score1
            self.round16[roundIndex].team2_score = score2
        
        if(roundType == "qfinal"):
            self.qfinal[roundIndex].team1_score = score1
            self.qfinal[roundIndex].team2_score = score2
            
        if(roundType == "sfinal"):
            self.sfinal[roundIndex].team1_score = score1
            self.sfinal[roundIndex].team2_score = score2
            
        if(roundType == "final"):
            self.final[0].team1_score = score1
            self.final[0].team2_score = score2
            
            
    
    
    
    def createRound16Classes(self):
        
        # A1 - B2        D1 - C2
        # C1 - D2        B1 - A2
        # E1 - F2        F1 - E2
        # G1 - H2        H1 - G2
        
        self.round16.append(Round16(self.groups[0].winner_1, self.groups[1].winner_2))
        self.round16.append(Round16(self.groups[2].winner_1, self.groups[3].winner_2))
        self.round16.append(Round16(self.groups[4].winner_1, self.groups[5].winner_2))
        self.round16.append(Round16(self.groups[6].winner_1, self.groups[7].winner_2))
        self.round16.append(Round16(self.groups[3].winner_1, self.groups[2].winner_2))
        self.round16.append(Round16(self.groups[1].winner_1, self.groups[0].winner_2))
        self.round16.append(Round16(self.groups[5].winner_1, self.groups[4].winner_2))
        self.round16.append(Round16(self.groups[7].winner_1, self.groups[6].winner_2))
    
    
    # =============================================================================================
    #                                        GROUPS LOGIC
    # =============================================================================================
    
    
    # [Note]: Function to check if team value exist in group 
    def doesTeamExist(self, groupIndex, teamIndex):
        if(len(self.groups) < (groupIndex + 1) ):
            return None
        else:
            return self.groups[self.assigned_groups].team_list[teamIndex].country
    
    
    # ------------------------------------------------------------
    # [NOTE]: Creating [Team] and [Group] class 
    # ------------------------------------------------------------
    
    def addGroup(self, t1_name, t2_name, t3_name, t4_name):
        
        t1 = Team( t1_name.title() )
        t2 = Team( t2_name.title() )
        t3 = Team( t3_name.title() )
        t4 = Team( t4_name.title() )

        
        t1_index = (self.assigned_groups * 4)  
        if(len(self.teams) <= t1_index):
            self.teams.append(t1)
        else:
            self.teams[t1_index] = t1

        t2_index = (self.assigned_groups * 4) + 1
        if(len(self.teams) <= t2_index):
            self.teams.append(t2)
        else:
            self.teams[t2_index] = t2
            
        t3_index = (self.assigned_groups * 4) + 2
        if(len(self.teams) <= t3_index):
            self.teams.append(t3)
        else:
            self.teams[t3_index] = t3
            
        t4_index = (self.assigned_groups * 4) + 3
        if(len(self.teams) <= t4_index):
            self.teams.append(t4)
        else:
            self.teams[t4_index] = t4
            
  
        
        if(len(self.groups) <= self.assigned_groups):
            self.groups.append(Group(self.group_names[self.assigned_groups], t1, t2, t3, t4))
        else:
            self.groups[self.assigned_groups] = Group(self.group_names[self.assigned_groups], t1, t2, t3, t4)
         
    
    
    
    
    # ------------------------------------------------------------
    # [NOTE]: GUI creating teams and groups, tabs management
    # ------------------------------------------------------------
    
    def createGroup(self, component, t1_name, t2_name, t3_name, t4_name):
        
        # -------------------- create [Group] and [Team]s classes --------------------
        self.addGroup(t1_name, t2_name, t3_name, t4_name)
        self.assigned_groups += 1
        
        
        self.view.controls.remove(component)
        
        # -------------------- all [Group] assigned --------------------
        if(self.assigned_groups == 8):
            
            # [Note]: \/ to remove topbar
            self.view.controls.clear()
            
            topbar = Topbar(lambda: self.autoFillMatches("groups"))
            self.view.controls.append(topbar)
            
            card = MatchCard(self.createMatch, "Group A", self.groups[0].team_list[0], self.groups[0].team_list[1])
            self.view.controls.append(card)
            
        else:
            # -------------------- not all [Group] are assigned --------------------
            
            # [Note]:   \/ check if data for this group exist  (if we went back before)
            t1 = self.doesTeamExist(self.assigned_groups, 0)
            t2 = self.doesTeamExist(self.assigned_groups, 1)
            t3 = self.doesTeamExist(self.assigned_groups, 2)
            t4 = self.doesTeamExist(self.assigned_groups, 3)
            
            card = GroupCard(self.backGroups, self.createGroup, self.group_names[self.assigned_groups], t1, t2, t3, t4)
            self.view.controls.append(card)
            
        self.update()
    
    
    
    
    
    # ------------------------------------------------------------
    # [NOTE]: GUI store group data and go back 1 tab
    # ------------------------------------------------------------
    
    def backGroups(self, component, t1_name, t2_name, t3_name, t4_name):
        
        # ------------ remember values ------------
        self.addGroup(t1_name, t2_name, t3_name, t4_name)
        
        # ------------ first page ? ------------
        if(self.assigned_groups != 0):
            # ------------ remove component, load old with data ------------
            self.assigned_groups -= 1
            self.view.controls.remove(component)

            t1 = self.groups[self.assigned_groups].team_list[0].country
            t2 = self.groups[self.assigned_groups].team_list[1].country
            t3 = self.groups[self.assigned_groups].team_list[2].country
            t4 = self.groups[self.assigned_groups].team_list[3].country

            group_card = GroupCard(self.backGroups, self.createGroup, self.group_names[self.assigned_groups], t1, t2, t3, t4)
            self.view.controls.append(group_card)
            self.update()
            
            
            
            
            
            
            
    # =============================================================================================
    #                                          AUTOFILLING
    # =============================================================================================
    
    
    # parameter is > is what stage do we autofill list
    
    def autoFillMatches(self, stage):
        
        # -------- autoFill for group names --------
        if(stage == "group_names"):
            self.teams.clear()
            self.groups.clear()
            self.assigned_groups = 0
            
            print(self.teams)
            print(self.groups)
            
            self.addGroup("Netherlands", "Senegal", "Ecuador", "Qatar")
            self.assigned_groups += 1
            self.addGroup("England", "USA", "Iran", "Wales")
            self.assigned_groups += 1
            self.addGroup("Argentina", "Poland", "Mexico", "Saudi Arabia")
            self.assigned_groups += 1
            self.addGroup("France", "Australia", "Tunisia", "Denmark")
            self.assigned_groups += 1
            self.addGroup("Japan", "Spain", "Germany", "Costa Rica")
            self.assigned_groups += 1
            self.addGroup("Morocco", "Croatia", "Belgium", "Canada")
            self.assigned_groups += 1
            self.addGroup("Brazil", "Switzerland", "Cameroon", "Serbia")
            self.assigned_groups += 1
            self.addGroup("Portugal", "South Korea", "Uruguay", "Ghana")
            
            self.assigned_groups = 7

            t1 = self.groups[self.assigned_groups].team_list[0].country
            t2 = self.groups[self.assigned_groups].team_list[1].country
            t3 = self.groups[self.assigned_groups].team_list[2].country
            t4 = self.groups[self.assigned_groups].team_list[3].country

            card = GroupCard(self.backGroups, self.createGroup, self.group_names[self.assigned_groups], t1, t2, t3, t4)
        
        
        
        
        # -------- autoFill for groups --------
        if(stage == "groups"):
            self.round16.clear()
            
            # ------------ Group A ------------
            self.addMatch(self.groups[0].team_list[0], self.groups[0].team_list[1], 2, 0)
            self.addMatch(self.groups[0].team_list[0], self.groups[0].team_list[2], 1, 1)
            self.addMatch(self.groups[0].team_list[0], self.groups[0].team_list[3], 2, 0)
            self.addMatch(self.groups[0].team_list[1], self.groups[0].team_list[2], 2, 1)
            self.addMatch(self.groups[0].team_list[1], self.groups[0].team_list[3], 3, 1)
            self.addMatch(self.groups[0].team_list[2], self.groups[0].team_list[3], 2, 0)
            # ------------ Group B ------------
            self.addMatch(self.groups[1].team_list[0], self.groups[1].team_list[2], 6, 2)
            self.addMatch(self.groups[1].team_list[0], self.groups[1].team_list[1], 0, 0)
            self.addMatch(self.groups[1].team_list[0], self.groups[1].team_list[3], 3, 0)
            self.addMatch(self.groups[1].team_list[2], self.groups[1].team_list[1], 0, 1)
            self.addMatch(self.groups[1].team_list[2], self.groups[1].team_list[3], 2, 0)
            self.addMatch(self.groups[1].team_list[3], self.groups[1].team_list[1], 1, 1)
            # ------------ Group C ------------
            self.addMatch(self.groups[2].team_list[0], self.groups[2].team_list[1], 2, 0)
            self.addMatch(self.groups[2].team_list[0], self.groups[2].team_list[2], 2, 0)
            self.addMatch(self.groups[2].team_list[0], self.groups[2].team_list[3], 1, 2)
            self.addMatch(self.groups[2].team_list[1], self.groups[2].team_list[2], 0, 0)
            self.addMatch(self.groups[2].team_list[1], self.groups[2].team_list[3], 2, 0)
            self.addMatch(self.groups[2].team_list[2], self.groups[2].team_list[3], 2, 1)
            # ------------ Group D ------------
            self.addMatch(self.groups[3].team_list[0], self.groups[3].team_list[1], 4, 1)
            self.addMatch(self.groups[3].team_list[0], self.groups[3].team_list[2], 0, 1)
            self.addMatch(self.groups[3].team_list[0], self.groups[3].team_list[3], 2, 1)
            self.addMatch(self.groups[3].team_list[1], self.groups[3].team_list[2], 1, 0)
            self.addMatch(self.groups[3].team_list[1], self.groups[3].team_list[3], 1, 0)
            self.addMatch(self.groups[3].team_list[2], self.groups[3].team_list[3], 0, 0)
            # ------------ Group E ------------
            self.addMatch(self.groups[4].team_list[0], self.groups[4].team_list[1], 2, 1)
            self.addMatch(self.groups[4].team_list[0], self.groups[4].team_list[2], 2, 1)
            self.addMatch(self.groups[4].team_list[0], self.groups[4].team_list[3], 0, 1)
            self.addMatch(self.groups[4].team_list[1], self.groups[4].team_list[2], 1, 1)
            self.addMatch(self.groups[4].team_list[1], self.groups[4].team_list[3], 7, 0)
            self.addMatch(self.groups[4].team_list[2], self.groups[4].team_list[3], 4, 2)
            # ------------ Group F ------------
            self.addMatch(self.groups[5].team_list[0], self.groups[5].team_list[1], 0, 0)
            self.addMatch(self.groups[5].team_list[0], self.groups[5].team_list[2], 2, 0)
            self.addMatch(self.groups[5].team_list[0], self.groups[5].team_list[3], 2, 1)
            self.addMatch(self.groups[5].team_list[1], self.groups[5].team_list[2], 0, 0)
            self.addMatch(self.groups[5].team_list[1], self.groups[5].team_list[3], 4, 1)
            self.addMatch(self.groups[5].team_list[2], self.groups[5].team_list[3], 1, 0)
            # ------------ Group G ------------
            self.addMatch(self.groups[6].team_list[0], self.groups[6].team_list[1], 1, 0)
            self.addMatch(self.groups[6].team_list[0], self.groups[6].team_list[2], 0, 1)
            self.addMatch(self.groups[6].team_list[0], self.groups[6].team_list[3], 2, 0)
            self.addMatch(self.groups[6].team_list[1], self.groups[6].team_list[2], 1, 0)
            self.addMatch(self.groups[6].team_list[1], self.groups[6].team_list[3], 3, 2)
            self.addMatch(self.groups[6].team_list[2], self.groups[6].team_list[3], 3, 3)
            # ------------ Group H ------------
            self.addMatch(self.groups[7].team_list[0], self.groups[7].team_list[1], 1, 2)
            self.addMatch(self.groups[7].team_list[0], self.groups[7].team_list[2], 2, 0)
            self.addMatch(self.groups[7].team_list[0], self.groups[7].team_list[3], 3, 2)
            self.addMatch(self.groups[7].team_list[1], self.groups[7].team_list[2], 0, 0)
            self.addMatch(self.groups[7].team_list[1], self.groups[7].team_list[3], 2, 3)
            self.addMatch(self.groups[7].team_list[2], self.groups[7].team_list[3], 2, 0)

            for g in self.groups:
                g.closeGroup()

            self.createRound16Classes()

            self.match_index = 48

            card = GroupsDisplay(self.groups, True, lambda: self.showMatchTab("Round 16"))
        
        
        
        
        # -------- autoFill for Round16 --------
        if(stage == "round16"):
            self.qfinal.clear()
            
            self.addMatch(self.round16[0].team1, self.round16[0].team2, 3, 1)
            self.round16[0].team1_score = 3
            self.round16[0].team2_score = 1
            self.addMatch(self.round16[1].team1, self.round16[1].team2, 2, 1)
            self.round16[1].team1_score = 2
            self.round16[1].team2_score = 1
            self.addMatch(self.round16[2].team1, self.round16[2].team2, 1, 3)
            self.round16[2].team1_score = 1
            self.round16[2].team2_score = 3
            self.addMatch(self.round16[3].team1, self.round16[3].team2, 4, 1)
            self.round16[3].team1_score = 4
            self.round16[3].team2_score = 1
            self.addMatch(self.round16[4].team1, self.round16[4].team2, 3, 1)
            self.round16[4].team1_score = 3
            self.round16[4].team2_score = 1
            self.addMatch(self.round16[5].team1, self.round16[5].team2, 3, 0)
            self.round16[5].team1_score = 3
            self.round16[5].team2_score = 0
            self.addMatch(self.round16[6].team1, self.round16[6].team2, 3, 0)
            self.round16[6].team1_score = 3
            self.round16[6].team2_score = 0
            self.addMatch(self.round16[7].team1, self.round16[7].team2, 6, 1)
            self.round16[7].team1_score = 6
            self.round16[7].team2_score = 1

            for r in self.round16:
                r.closeRound()

            self.qfinal.append(QFinal(self.round16[0].round_winner, self.round16[1].round_winner))
            self.qfinal.append(QFinal(self.round16[2].round_winner, self.round16[3].round_winner))
            self.qfinal.append(QFinal(self.round16[4].round_winner, self.round16[5].round_winner))
            self.qfinal.append(QFinal(self.round16[6].round_winner, self.round16[7].round_winner))

            self.match_index = 56
            card = RoundDisplay(self.round16, "Round 16", lambda: self.showMatchTab("Quarter-Final"), True)
            
            
            
        # -------- autoFill for Quarter-Final --------
        elif(stage == "qfinal"):
            self.sfinal.clear()
            
            self.addMatch(self.qfinal[0].team1, self.qfinal[0].team2, 3, 4)
            self.qfinal[0].team1_score = 3
            self.qfinal[0].team2_score = 4
            self.addMatch(self.qfinal[1].team1, self.qfinal[1].team2, 4, 2)
            self.qfinal[1].team1_score = 4
            self.qfinal[1].team2_score = 2
            self.addMatch(self.qfinal[2].team1, self.qfinal[2].team2, 2, 1)
            self.qfinal[2].team1_score = 2
            self.qfinal[2].team2_score = 1
            self.addMatch(self.qfinal[3].team1, self.qfinal[3].team2, 1, 0)
            self.qfinal[3].team1_score = 1
            self.qfinal[3].team2_score = 0
            
            for r in self.qfinal:
                r.closeRound()

            self.sfinal.append(SFinal(self.qfinal[0].round_winner, self.qfinal[1].round_winner))
            self.sfinal.append(SFinal(self.qfinal[2].round_winner, self.qfinal[3].round_winner))

            self.match_index = 60
            card = RoundDisplay(self.qfinal, "Quarter-Final", lambda: self.showMatchTab("Semi-Final"), True)
            
            
            
        # -------- autoFill for Quarter-Final --------
        elif(stage == "sfinal"):
            self.final.clear()
        
            self.addMatch(self.sfinal[0].team1, self.sfinal[0].team2, 3, 0)
            self.sfinal[0].team1_score = 3
            self.sfinal[0].team2_score = 0
            self.addMatch(self.sfinal[1].team1, self.sfinal[1].team2, 2, 0)
            self.sfinal[1].team1_score = 2
            self.sfinal[1].team2_score = 0

            self.sfinal[0].closeRound()
            self.sfinal[1].closeRound()

            self.final.append(Final(self.sfinal[0].round_winner, self.sfinal[1].round_winner))

            self.match_index = 62
            card = RoundDisplay(self.sfinal, "Semi-Final", lambda: self.showMatchTab("Final"), True)
            
            
            
        self.view.controls.clear()
        self.view.controls.append(card)
        return self.update()


def main(page: ft.Page):
    
    # ---------------------- Page specification ----------------------
    page.title = "World Cup System"
    
    page.window_width = 1300
    page.window_height = 830
    page.window_resizable = False
    
    page.scroll = ft.ScrollMode.ALWAYS
    
    # ---------------------- Header ----------------------
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SPORTS_SOCCER, color="#FFFFFF"),
        leading_width=40,
        title=ft.Text("World Cup System",
            size=32,
            color=('#FFFFFF'),
           ),
        center_title=True,
        bgcolor=('#8A1538'),
    )
    
    
    # ft.Container()
    # ft.Column( [], style )
    # ft.Row()
    
    

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    appInstance = App()
    
    page.add(appInstance)

ft.app(target=main)