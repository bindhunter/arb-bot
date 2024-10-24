class Normalizer:
    def normalize_odds(self, data, platform):
        if platform == "hard_rock":
            return self._normalize_hard_rock(data)
        elif platform == "polymarkets":
            return self._normalize_polymarkets(data)
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def _normalize_hard_rock(self, data):
        normalized = []
        for event in data['events']:
            normalized.append({
                'event_id': event['id'],
                'event_name': event['name'],
                'outcomes': [
                    {'name': outcome['name'], 'odds': outcome['odds']}
                    for outcome in event['outcomes']
                ]
            })
        return normalized

    def _normalize_polymarkets(self, data):
        normalized = []
        for market in data['markets']:
            normalized.append({
                'event_id': market['id'],
                'event_name': market['name'],
                'outcomes': [
                    {'name': outcome['name'], 'odds': 1 / outcome['probability']}
                    for outcome in market['outcomes']
                ]
            })
        return normalized