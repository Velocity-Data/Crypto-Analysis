#!/usr/bin/env python
import sqlite3




def inputdb():
	conn = sqlite3.connect('monero.db')
	c = conn.cursor()