"""QRgen.py
Bulk QR code generator
uses a text file, containing one URL per line, to generate a batch of QR code images"""

__author__ = "Justin Johnson"
__email__ = "authalic@gmail.com"
__date__ = "23 Feb, 2021"
__version__ = "1.0"
__status__ = "Production"


import argparse
from os import makedirs
from os.path import join, exists
from urllib.parse import urlparse
import qrcode  # see: https://pypi.org/project/qrcode/  for options


# configure the command-line parsing

parser = argparse.ArgumentParser()
parser.add_argument("urlfile", help="name of input text file containing URLs")
parser.add_argument("-o", "--outdir", help="name of output folder for QR image files (default is current directory)")

args = parser.parse_args()


# parse the input text file name and output directory from the command line parameters

# check if the optional output directory was included
outdir = args.outdir

# create the path in os if it does not already exist
if outdir:
    if not exists(outdir):
        makedirs(outdir)

# input filename
infile = args.urlfile

# open the input file
with open(infile) as f:
    urllist = f.readlines()

    # loop through the URLs from the input file
    for url in urllist:

        # create the output filename string
        # replace slashes in URL with underscores and dots with dashes
        # TODO: make this less klunky

        o = urlparse(url) # remove the newline character from end of line
        netloc = o.netloc.replace('.', '-')

        if len(o.path.strip()) > 1: # an empty path is the '/' character
            path = o.path.replace(r'/', '_').replace('.', '-')
            outfilename = netloc + '_' + path.strip().strip('_') + '.png'
        else:
            outfilename = netloc + '.png'

        # prepend the optional output folder to the output file name
        if outdir:
            outfilename = join(outdir, outfilename)

        # generate the QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(outfilename, "PNG")
