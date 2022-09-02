import datetime
from typing import List, Tuple

class Solution:
    trades = []
    
    def one_min(self, day1, time1, day2, time2):
        hms1 = time1.split(":")
        hms2 = time2.split(":")
        ymd1 = day1.split("-")
        ymd2 = day2.split("-")
        one = datetime.datetime(int(ymd1[0]), int(ymd1[1]), int(ymd1[2]), int(hms1[0]), int(hms1[1]), int(hms1[2]))
        two = datetime.datetime(int(ymd2[0]), int(ymd2[1]), int(ymd2[2]), int(hms2[0]), int(hms2[1]), int(hms2[2]))
        difference = (one-two).total_seconds()
        if difference >= 0 and difference <= 60: return True
        else: return False
            
    
    def is_front(self, trade, idx):
        fronts = []
        for i in range(0, idx):
            front = True
            trade2 = self.trades[i]
            #Condition A
            if (trade[3] == trade2[3]):
                front = False
            #Condition B
            if not self.one_min(trade[1], trade[2], trade2[1], trade2[2]):
                front = False
            #Condition C
            if (trade[5] != trade2[5]):
                front = False
            #Condition D
            if (trade[6] != trade2[6]):
                front = False
            #Condition E
            if (trade[10] != trade2[10]):
                front = False
            #Condition F
            if (trade[7] != trade2[7]):
                front = False
            #Condition G
            if (trade[9] != trade2[9]):
                front = False
                
            if front: fronts.append(trade2[0])
            
        return fronts
        
    
    def process_raw_trade(self, raw_trade: List):
        trade_data = []
        #Add side for CBOE data
        if len(raw_trade) == 10:
            if int(raw_trade[9]) >= 0: raw_trade.append("BUY")
            else: raw_trade.append("SELL")
        #Append each value w/ it's corresponding field
        for i in raw_trade:
            trade_data.append(i)
        self.trades.append(trade_data)    
    
        
    def run(self) -> List[Tuple[str, str]]:
        #Sort by date then time
        sorted_trades = sorted(self.trades, key = lambda x: (x[1].replace('-', ''), x[2].replace(':', '')))
        self.trades = sorted_trades
        #Check each trade
        front_runners = []
        for idx,trade in enumerate(sorted_trades):
            front_trades = self.is_front(trade, idx)
            for i in front_trades:
                front_runners.append((trade[0], i))
        
        return front_runners

if __name__ == '__main__':
    solution = Solution()
    for row in fileinput.input():
        raw_trade = list(row.strip().replace(" ", "").split(","))
        solution.process_raw_trade(raw_trade)
        
    print(solution.run())
