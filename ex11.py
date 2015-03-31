# -*- coding: utf-8 -*-

print "Hur gammal är du?",
age = raw_input()
print "Hur lång är du",
height = raw_input()
print "Hur mycket väger du?",
weight = raw_input()

print "Du är %r år gammal, %r cm hög och %r tung." % (
	age, height, weight)