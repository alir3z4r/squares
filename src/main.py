import argparse
from utils.arguments import arguments
from train.main_train import main as main_train
from play.main_play import main as main_play


def main():
    print("square building game...")
    parser = arguments()
    args = parser.parse_args()
    if args.mode == "train":
        print("train mode ...")
        main_train(args)
    elif args.mode == "play":
        print("play mode ...")
        main_play(args)


if __name__ == '__main__':
    main()
