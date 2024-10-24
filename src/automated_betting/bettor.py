import random
import logging

logger = logging.getLogger(__name__)

class Bettor:
    def __init__(self):
        self.balance_stake = 500  # Starting balance for Stake in USD
        self.balance_polymarkets = 500  # Starting balance for Polymarkets in USD
        self.balance_roobet = 500  # Starting balance for Roobet in USD

    def place_bets(self, decision):
        total_profit = 0
        results = []

        for bet in decision['bets']:
            try:
                if bet['platform'] == 'Stake':
                    result = self._simulate_stake_bet(decision['event_name'], bet['outcome'], bet['stake'], bet['odds'])
                elif bet['platform'] == 'Polymarkets':
                    result = self._simulate_polymarkets_bet(decision['event_name'], bet['outcome'], bet['stake'], bet['odds'])
                elif bet['platform'] == 'Roobet':
                    result = self._simulate_roobet_bet(decision['event_name'], bet['outcome'], bet['stake'], bet['odds'])
                else:
                    logger.error(f"Unknown platform: {bet['platform']}")
                    continue

                total_profit += result['profit']
                results.append(result)
                logger.info(f"Bet placed: {result}")
            except Exception as e:
                logger.error(f"Error placing bet: {str(e)}")

        return {
            'results': results,
            'total_profit': total_profit
        }

    def _simulate_stake_bet(self, event_name, outcome, stake, odds):
        if stake > self.balance_stake:
            raise ValueError(f"Insufficient balance on Stake. Current balance: ${self.balance_stake}, Bet amount: ${stake}")

        success = random.random() < 0.95  # 95% chance of successful bet placement
        if success:
            self.balance_stake -= stake
            simulated_win = random.random() < 1 / odds
            profit = stake * (odds - 1) if simulated_win else -stake
            self.balance_stake += stake + profit
            return {
                "platform": "Stake",
                "status": "success",
                "message": f"Bet of ${stake} placed on {outcome} for event {event_name}",
                "profit": profit,
                "new_balance": self.balance_stake
            }
        else:
            return {
                "platform": "Stake",
                "status": "failed",
                "message": f"Failed to place bet on {outcome} for event {event_name}",
                "profit": 0,
                "balance": self.balance_stake
            }

    def _simulate_polymarkets_bet(self, event_name, outcome, stake, odds):
        if stake > self.balance_polymarkets:
            raise ValueError(f"Insufficient balance on Polymarkets. Current balance: ${self.balance_polymarkets}, Bet amount: ${stake}")

        success = random.random() < 0.93  # 93% chance of successful bet placement
        if success:
            self.balance_polymarkets -= stake
            simulated_win = random.random() < 1 / odds
            profit = stake * (odds - 1) if simulated_win else -stake
            self.balance_polymarkets += stake + profit
            return {
                "platform": "Polymarkets",
                "status": "success",
                "message": f"Bet of ${stake} placed on {outcome} for event {event_name}",
                "profit": profit,
                "new_balance": self.balance_polymarkets
            }
        else:
            return {
                "platform": "Polymarkets",
                "status": "failed",
                "message": f"Failed to place bet on {outcome} for event {event_name}",
                "profit": 0,
                "balance": self.balance_polymarkets
            }

    def _simulate_roobet_bet(self, event_name, outcome, stake, odds):
        if stake > self.balance_roobet:
            raise ValueError(f"Insufficient balance on Roobet. Current balance: ${self.balance_roobet}, Bet amount: ${stake}")

        success = random.random() < 0.94  # 94% chance of successful bet placement
        if success:
            self.balance_roobet -= stake
            simulated_win = random.random() < 1 / odds
            profit = stake * (odds - 1) if simulated_win else -stake
            self.balance_roobet += stake + profit
            return {
                "platform": "Roobet",
                "status": "success",
                "message": f"Bet of ${stake} placed on {outcome} for event {event_name}",
                "profit": profit,
                "new_balance": self.balance_roobet
            }
        else:
            return {
                "platform": "Roobet",
                "status": "failed",
                "message": f"Failed to place bet on {outcome} for event {event_name}",
                "profit": 0,
                "balance": self.balance_roobet
            }