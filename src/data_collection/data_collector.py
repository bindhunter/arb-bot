import logging
import random
from typing import List, Dict
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.sports = ["Football", "Basketball", "Tennis", "Baseball", "Hockey"]
        self.teams = {
            "Football": ["Patriots", "Rams", "Chiefs", "49ers", "Packers", "Cowboys"],
            "Basketball": ["Lakers", "Celtics", "Warriors", "Nets", "Bucks", "Heat"],
            "Tennis": ["Djokovic", "Nadal", "Federer", "Williams", "Osaka", "Barty"],
            "Baseball": ["Yankees", "Dodgers", "Red Sox", "Cubs", "Astros", "Mets"],
            "Hockey": ["Maple Leafs", "Canadiens", "Bruins", "Blackhawks", "Lightning", "Penguins"]
        }

    def get_stake_data(self) -> List[Dict]:
        return self._generate_data("Stake")

    def get_polymarkets_data(self) -> List[Dict]:
        return self._generate_data("Polymarkets")

    def get_roobet_data(self) -> List[Dict]:
        return self._generate_data("Roobet")

    def _generate_start_time(self):
        now = datetime.now()
        max_date = now + timedelta(days=3)
        
        # Generate a random datetime within the next 3 days
        random_seconds = random.randint(0, int((max_date - now).total_seconds()))
        random_date = now + timedelta(seconds=random_seconds)
        
        # # Adjust time to be more realistic for sports events
        # hour = random.randint(12, 23)  # Events between 12 PM and 11 PM
        # minute = random.choice([0, 15, 30, 45])
        
        return random_date.replace(hour=hour, minute=minute, second=0).strftime("%Y-%m-%d %H:%M:%S")

    def _generate_data(self, platform: str) -> List[Dict]:
        data = []
        for _ in range(10):  # Generate 10 events
            sport = random.choice(self.sports)
            home_team, away_team = random.sample(self.teams[sport], 2)
            
            home_odds = round(random.uniform(1.5, 4.0), 2)
            away_odds = round(random.uniform(1.5, 4.0), 2)
            draw_odds = round(random.uniform(2.5, 5.0), 2) if sport in ["Football", "Hockey"] else None

            event = {
                "sport": sport,
                "home_team": home_team,
                "away_team": away_team,
                "start_time": self._generate_start_time(),
                "odds": {
                    "home_win": home_odds,
                    "away_win": away_odds
                }
            }
            
            if draw_odds:
                event["odds"]["draw"] = draw_odds

            # Add some variance between platforms
            if platform in ["Polymarkets",]:
                variance = random.uniform(0.45, 0.55)
                event["odds"]["home_win"] = round(event["odds"]["home_win"] * variance, 2)
                event["odds"]["away_win"] = round(event["odds"]["away_win"] * variance, 2)
                if "draw" in event["odds"]:
                    event["odds"]["draw"] = round(event["odds"]["draw"] * variance, 2)

            # Add Roobet-specific variations
            if platform == "Roobet":
                event["roobet_id"] = f"RB-{random.randint(0.95, 1.05)}"
                event["roobet_market_type"] = random.choice(["standard", "live", "special"])

            data.append(event)

        return data