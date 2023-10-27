from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1)

    club_emails = ["john@simplylift.com", "admin@irontemple.com", "kate@shelifts.co.uk"]


    @task(1)
    def load_homepage(self):
        response = self.client.get("/")
        assert response.elapsed.total_seconds() <= 5, "Homepage loading took more than 5 seconds!"

    @task(2)
    def show_summary(self):
        for email in self.club_emails:
            response = self.client.post("/showSummary", data={"email": email})
            assert response.elapsed.total_seconds() <= 5, "Loading summary took more than 5 seconds!"

    @task(3)
    def book(self):
        club_name = "Simply Lift"
        competition_name = "Spring Festival"
        response = self.client.get(f'/book/{competition_name}/{club_name}')
        assert response.elapsed.total_seconds() <= 5, "Booking page loading took more than 5 seconds!"

    @task(4)
    def purchase_places(self):
        club_name = "Simply Lift"
        competition_name = "Spring Festival"
        response = self.client.post('/purchasePlaces', data={'club': club_name, 'competition': competition_name, 'places': '1'})
        assert response.elapsed.total_seconds() <= 2, "Purchasing places took more than 2 seconds!"

    @task(5)
    def points_display(self):
        response = self.client.get('/pointsDisplay')
        assert response.elapsed.total_seconds() <= 5, "Points display loading took more than 5 seconds!"

    @task(6)
    def logout(self):
        self.client.get('/logout')

