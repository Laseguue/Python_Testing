import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'something_special'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        clubs = loadClubs()
        competitions = loadCompetitions()
        club = [club for club in clubs if club['email'] == request.form['email']]
        if not club:
            flash("Email not found. Please try again.")
            return redirect(url_for('index'))
        return render_template('welcome.html', club=club[0], competitions=competitions)

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        clubs = loadClubs()
        competitions = loadCompetitions()
        foundClub = [c for c in clubs if c['name'] == club]
        foundCompetition = [c for c in competitions if c['name'] == competition]
        if not foundClub or not foundCompetition:
            flash("Something went wrong-please try again")
            return redirect(url_for('index'))
        competition_datetime = datetime.strptime(foundCompetition[0]['date'], '%Y-%m-%d %H:%M:%S')
        if competition_datetime < datetime.now():
            flash("This competition has already taken place!")
            return redirect(url_for('showSummary'))
        return render_template('booking.html', club=foundClub[0], competition=foundCompetition[0])


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()