# Python bulk QR code generator

# uses a text file, containing one URL per line, specified as a command-line parameter
# outputs a QR code image in the current directory, or in a location specified in the
# second command line parameter

import argparse
from os.path import join
from urllib.parse import urlparse
import qrcode  # https://pypi.org/project/qrcode/


# configure the command-line parsing

parser = argparse.ArgumentParser()
parser.add_argument("urlfile", help="name of input text file containing URLs")
parser.add_argument("-o", "--outdir", help="name of output folder for QR image files (default is current directory)")

args = parser.parse_args()



# parse the input text file name and output directory from the command line parameters

# input filename
infile = args.urlfile

# output directory (defaults to current dir)
if args.outdir:
    outdir = args.outdir
else:
    outdir = ''

# (join(outdir, "testfile.txt"))


# open the input file
with open(infile) as f:
    urllist = f.readlines()
    for url in urllist:

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        outfilename = ''

        img.save(outfilename, "PNG")
