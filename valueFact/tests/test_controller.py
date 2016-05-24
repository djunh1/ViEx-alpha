from django.test import TestCase

from valueFact.controller import stat_cleaner, yahoo_cleaner

class ValueFactTesting(TestCase):
    def test_stat_cleaner(self):
        '''
        The stat cleaner looks at market cap of companies.  We need to normalize market cap for subsequent calculations
        such as EV/EBITDA etc.  This will convert all market cap to millions of dollars but looking for a B and
        multiplying by 1000 to convert.
        '''
        # Convert the string into a decimal ( into millions of USD)
        ticker = '10B'
        tickerNew = stat_cleaner(ticker)
        self.assertEqual(10000.0, tickerNew)

        # Converts the string, but doesn't apply the conversion.
        ticker1 = '10'
        tickerNew1 = stat_cleaner(ticker1)
        self.assertEqual(10.0, tickerNew1)

    def test_yahoo_cleaner(self):
        '''
        This converts tickers with periods to tickers with dashes.  This is because yahoo finance API only accepts
        tickers with dashes.  This should either return the ticker, or clean the ticker to contain a dash (-)
        '''
        # Changes the ticker
        ticker = 'BRK.B'
        tickerNew = yahoo_cleaner(ticker)
        self.assertEqual('BRK-B', tickerNew)

        # Leaves ticker alone
        ticker1 = 'BRK-A'
        tickerNew1 = yahoo_cleaner(ticker1)
        self.assertEqual('BRK-A', tickerNew1)