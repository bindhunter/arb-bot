from data_collection.data_collector import DataCollector
from opportunity_identification.arbitrage_finder import ArbitrageFinder
from decision_engine.decision_maker import DecisionMaker
from automated_betting.bettor import Bettor
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_simulation(iterations=100):
    data_collector = DataCollector()
    arbitrage_finder = ArbitrageFinder()
    decision_maker = DecisionMaker()
    bettor = Bettor()

    total_profit = 0
    opportunities_found = 0
    bets_placed = 0

    for i in range(iterations):
        try:
            stake_data = data_collector.get_stake_data()
            polymarkets_data = data_collector.get_polymarkets_data()
            roobet_data = data_collector.get_roobet_data()

            opportunities = arbitrage_finder.find_arbitrage(stake_data, polymarkets_data, roobet_data)
            opportunities_found += len(opportunities)

            decisions = decision_maker.make_decision(opportunities)

            for decision in decisions:
                result = bettor.place_bets(decision)
                bets_placed += 1
                total_profit += result['profit'] if 'profit' in result else 0

            logger.info(f"Iteration {i+1}/{iterations} - Current balances - "
                       f"Stake: ${bettor.balance_stake}, "
                       f"Polymarkets: ${bettor.balance_polymarkets}, "
                       f"Roobet: ${bettor.balance_roobet}")

        except Exception as e:
            logger.error(f"An error occurred in iteration {i+1}: {str(e)}")

    logger.info(f"Simulation complete. Total profit: ${total_profit}")
    logger.info(f"Opportunities found: {opportunities_found}")
    logger.info(f"Bets placed: {bets_placed}")
    logger.info(f"Final balances - "
               f"Stake: ${bettor.balance_stake}, "
               f"Polymarkets: ${bettor.balance_polymarkets}, "
               f"Roobet: ${bettor.balance_roobet}")

def main(test_mode=True):
    if test_mode:
        run_simulation()
    else:
        # Your original live trading code here
        pass

if __name__ == "__main__":
    main(test_mode=True)