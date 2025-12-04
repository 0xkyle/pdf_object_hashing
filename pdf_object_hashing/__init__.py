"""
PDF Object Hashing Library

This is a python library for analyzing PDFs, focusing on the structure through object hashing.
Similar to imphash or ja3, we create a structural fingerprint of the PDF focusing on the 
type of objects, instead of the content of those objects. This lets us quickly find documents with
the same (or similar) structure. 

Blog: https://www.proofpoint.com/us/blog/threat-insight/proofpoint-releases-innovative-detections-threat-hunting-pdf-object-hashing
"""

__version__ = "0.2.0"
__author__ = "kyle eaton"

# import classes
from .pdf_lib import pdf_object
from .pdf_param_parser import pdf_param_parser, parse_pdf_parameters

# from pdf_object_hashing import *
__all__ = [
	'pdf_object',
	'pdf_param_parser',
	'parse_pdf_parameters',
]

