class DecisionMaker:
    def make_decision(self, opportunities):
        decisions = []
        for opportunity in opportunities:
            bets = []
            for outcome, data in opportunity['best_odds'].items():
                bets.append({
                    'platform': data['platform'],
                    'outcome': outcome,
                    'odds': data['odds'],
                    'stake': self._calculate_stake(opportunity['profit_percentage'])
                })
            decisions.append({
                'event_name': opportunity['event_name'],
                'bets': bets
            })
        return decisions

    def _calculate_stake(self, profit_percentage):
        # Simple stake calculation based on profit percentage
        # You might want to implement a more sophisticated staking strategy
        base_stake = 10
        return round(base_stake * (1 + profit_percentage / 100), 2)