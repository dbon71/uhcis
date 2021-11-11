#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#class for team
class Team:
    #defining name, wins and losses
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0
    #defining win percentage
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":

    #element identification
    team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    #if-else statement to check for winning and losing averages
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
