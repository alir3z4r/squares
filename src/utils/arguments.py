import argparse


def arguments():
    parser = argparse.ArgumentParser("Argument parser for squares game.")
    subparser = parser.add_subparsers(dest="mode")
    
    """
    Train subparser
    """
    parser_train = subparser.add_parser("train")
    parser_train.add_argument("-d","--dims", type=int, nargs=2, help="Dimensions of the Board.")

    """
    Play subparser
    """
    parser_play = subparser.add_parser("play")
    parser_play.add_argument("-s","--starter", type=int, help="Who will start the game?")
    parser_play.add_argument("-d","--dims", type=int, nargs=2, help="Dimensions of the Board.")
    
    return parser