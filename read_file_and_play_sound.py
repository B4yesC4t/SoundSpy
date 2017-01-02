# coding: utf-8

import sys
import time
import argparse
from gooey import Gooey, GooeyParser


sleep_time = 0.2  # s


def str2bin(content):
    # 字符串转为二进制串
    # 每个字符转为8位二进制，不足8位在开头补0
    result = ''
    for string_num in content:
        string_num = ord(string_num)
        num = int(string_num)
        mid = []
        base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'), ord('A')+6)]
        while True:
            if num == 0: break
            num, rem = divmod(num, 2)
            mid.append(base[rem])
        tmp = ''.join([str(x) for x in mid[::-1]])
        for i in range(8 - len(tmp)): tmp = '0' + tmp 
        result += tmp
    print "Bin is: %s" % result
    return result


def bin2sound(bin, model):
    if sys.platform.find("win") == -1:    # linux
        pass
    else:                                 # windows
        import winsound
        if model == 0:
            high_frequent = 1000
            low_frequent = 1000
            high_time = 150
            low_time = 100
        else:
            high_frequent = 2000
            low_frequent = 1000
            high_time = 150
            low_time = 150
        for b in bin:
            if int(b) == 1:
                winsound.Beep(high_frequent, high_time)
            else:
                winsound.Beep(low_frequent, low_time)
            time.sleep(sleep_time)


def handle_arg():
    mparser = argparse.ArgumentParser(description='Read file and play Beep.')
    mparser.add_argument('-s', action="store", dest="start", choices=["c", "g"], default='g',
                        help="Start model.\n'c' for start with command.\n'g' for start with gui.")
    mparser.add_argument('-f', action="store", dest="file", help="Target txt file.")
    mparser.add_argument('-m', '--model',  default="t", type=str, choices=["t", "f"],
                        help='Play model. \n\t\tt for playing with different time\n\t\tf for playing with different frequency.')
    mparser.add_argument('--version', action='version', version='%(prog)s 1.0')
    margs = mparser.parse_args()
    if margs.start == "g":
        gui_arg()
    else:
        if margs.file:
            print "Target is %s." % margs.file
            model = margs.model
            try:
                fp = open(margs.file)
                content = fp.read()
                fp.close()
                bin = str2bin(content)
                bin2sound(bin, model)
            except:
                pass


@Gooey(program_name="Attack!!!", language="chinese")
def gui_arg():
    parser = GooeyParser(description='Read file and play Beep.')
    parser.add_argument('-f', '--file', widget="FileChooser")
    parser.add_argument('-m', '--model',  default="t", type=str, choices=["t", "f"],
                        help='Play model. \n\t\tt for playing with different time\n\t\tf for playing with different frequency.')
    args = parser.parse_args()
    if args.file:
        print "Target is %s." % args.file
        model = 0 if args.model == "time" else 1
        try:
            fp = open(args.file)
            content = fp.read()
            fp.close()
            bin = str2bin(content)
            bin2sound(bin, model)
        except:
            pass


if __name__ == "__main__":
    # print str2bin("name")
    handle_arg()
    # gui_arg()
