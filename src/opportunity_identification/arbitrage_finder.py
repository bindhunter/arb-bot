class ArbitrageFinder:
    def find_arbitrage(self, stake_data, polymarkets_data, roobet_data):
        opportunities = []
        for stake_event in stake_data:
            for pm_event in polymarkets_data:
                for rb_event in roobet_data:
                    if self._events_match(stake_event, pm_event, rb_event):
                        arb_opportunity = self._calculate_arbitrage(stake_event, pm_event, rb_event)
                        if arb_opportunity:
                            opportunities.append(arb_opportunity)
        return opportunities

    def _events_match(self, stake_event, polymarkets_event, roobet_event):
        return (
            self._all_equal([stake_event['sport'], polymarkets_event['sport'], roobet_event['sport']]) and
            self._all_equal([stake_event['home_team'], polymarkets_event['home_team'], roobet_event['home_team']]) and
            self._all_equal([stake_event['away_team'], polymarkets_event['away_team'], roobet_event['away_team']]) and
            self._times_close_enough([stake_event['start_time'], polymarkets_event['start_time'], roobet_event['start_time']])
        )

    def _all_equal(self, items):
        return len(set(items)) == 1

    def _times_close_enough(self, times):
        parsed_times = [self._parse_time(time) for time in times]
        return max(parsed_times) - min(parsed_times) < 300  # 5 minutes

    def _calculate_arbitrage(self, stake_event, pm_event, rb_event):
        total_implied_probability = 0
        best_odds = {}

        for outcome in ['home_win', 'away_win', 'draw']:
            odds = [
                ('Stake', stake_event['odds'].get(outcome, 0)),
                ('Polymarkets', pm_event['odds'].get(outcome, 0)),
                ('Roobet', rb_event['odds'].get(outcome, 0))
            ]
            best_odds[outcome] = max(odds, key=lambda x: x[1])
            if best_odds[outcome][1] > 0:
                total_implied_probability += 1 / best_odds[outcome][1]

        if total_implied_probability < 0.98:
            profit_percentage = (1 - total_implied_probability) * 100
            return {
                'sport': stake_event['sport'],
                'home_team': stake_event['home_team'],
                'away_team': stake_event['away_team'],
                'start_time': stake_event['start_time'],
                'profit_percentage': profit_percentage,
                'best_odds': {k: {'odds': v[1], 'platform': v[0]} for k, v in best_odds.items()}
            }

        return None

    def _parse_time(self, time_str):
        # Needs time parsing logic here
        # Convert the time string to a comparable format (e.g., Unix timestamp)
        pass