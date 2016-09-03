from nose.tools import *
from ex48 import parser

def test_sentence():
        a= parser.parse_sentence([('verb','run'),('direction','north')])
	assert_equal(a.subject, 'player')
	assert_equal(a.verb,'run')
	assert_equal(a.object,'north')

def test_parse_verb():
	 arg=[('noun','run'),('direction','north')]
         assert_raises(parser.ParserError,parser.parse_verb,arg)

def test_parse_object():
         assert_raises(parser.ParserError,parser.parse_object,"[('verb','run'),('verb','north')]")
