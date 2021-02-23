# QRgen
### Generates QR codes in bulk from a text file of URLs

This was written as a batch QR code generator for a printed publication containing a number of sometimes-lengthy URLs.  QR codes were used to provide a quick way to access web data by users in the field.  This script uses a text file as an input, with a URL on each line.  The output is a QR code (png) for each URL, renamed to reflect the target.

Additional customization is probably possible using parameters in the imported [**`qrcode`**](https://pypi.org/project/qrcode/) module.
