import argparse
import logging

from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s')

parser = argparse.ArgumentParser(description='Sends a decimal code via a 433/315MHz GPIO device')
parser.add_argument('code', metavar='CODE', type=int)
parser.add_argument('-g', dest='gpio', type=int, default=17)
parser.add_argument('-p', dest='pulselength', type=int, default=None)
parser.add_argument('-t', dest='protocol', type=int, default=None)
args = parser.parse_args()

rfdevice = RFDevice(args.gpio)
rfdevice.enable_tx()

if args.protocol:
    protocol = args.protocol
else:
    protocol = "default"
if args.pulselength:
    pulselength = args.pulselength
else:
    pulselength = "default"
logging.info(str(args.code) +
            " [pulselength " + str(pulselength) +
            ", protocol " + str(protocol) + "]")
rfdevice.tx_code(args.code, args.protocol, args.pulselength)
rfdevice.cleanup()