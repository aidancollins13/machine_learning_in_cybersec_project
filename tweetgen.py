import sys


try:
    mode = sys.argv[1]
    if mode == 'collect_data':
        import scrape
    if mode == 'gen_tweets':
        import min_char_rnn
except :
    e = sys.exc_info()[0]
    print(e)
    print("USAGE: tweetgen <collect_data or gen_tweets>")
