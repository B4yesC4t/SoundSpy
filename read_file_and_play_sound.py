# coding: utf-8

import sys
import time
import argparse


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
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', action="store", dest="file", help="Target txt file.")
    parser.add_argument('-m',  action='store', dest='model', default=0, type=int, choices=[0, 1],
                        help='Play model. \n\t\t0 for playing with different time\n\t\t1 for playing with different frequent.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    if args.file:
        print "Target is %s." % args.file
        model = args.model
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
