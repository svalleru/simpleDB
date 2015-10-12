# -*- coding: utf-8 -*-
__author__ = 'svalleru'

"""
Implements simple database - Thumbtack challenge @ https://www.thumbtack.com/challenges/simple-database
Usage:
    - Interactive Mode: python database.py
    - batch Mode: python database.py < input.txt
"""

import itertools
from copy import deepcopy


class Database(object):
    # Keep track of transactions
    transaction = []

    def __init__(self):
        self.data = {}  # for name-value pairs
        Database.transaction.append(self)  # add to transaction list

    # Data Commands - SET, GET, UNSET, NUMEQUALTO, END
    # Always work on latest transaction
    # SET name value
    def set(self, name, value):
        self.transaction[-1].data[name] = value

    # GET name
    def get(self, name):
        return self.transaction[-1].data[name] if name in self.transaction[-1].data.keys() else 'NULL'

    # UNSET name
    def unset(self, name):
        if name in self.transaction[-1].data.keys():
            self.transaction[-1].data.pop(name, None)
        else:
            pass  # name doesn't exists

    # NUMEQUALTO value
    def numequalto(self, value):
        val_tup = [(k, len(list(v))) for k, v in itertools.groupby(sorted(self.transaction[-1].data.values()))]
        val_dict = dict(val_tup)
        del val_tup
        return val_dict[value] if value in val_dict.keys() else 0

    # END
    def end(self):
        exit()

    # Transaction Commands - BEGIN, ROLLBACK, COMMIT
    # BEGIN
    def begin(self):
        # Clone previous state and make it as latest transaction
        Database.transaction.append(deepcopy(db))

    # ROLLBACK
    def rollback(self):
        # Pop latest transaction and move to prev. transaction state
        if len(Database.transaction) > 1:
            self.transaction.pop()
        else:
            print 'NO TRANSACTION'

    # COMMIT
    def commit(self):
        # Commit latest working transaction and pop it fm global transaction list
        Database.transaction[-2] = deepcopy(Database.transaction[-1])
        Database.transaction.pop()


if __name__ == '__main__':
    db = Database()
    while True:
        cmd = raw_input()
        cmd = cmd.split()
        if cmd[0] == 'SET':
            db.set(cmd[1], cmd[2])
        elif cmd[0] == 'GET':
            print db.get(cmd[1])
        elif cmd[0] == 'UNSET':
            db.unset(cmd[1])
        elif cmd[0] == 'NUMEQUALTO':
            print db.numequalto(cmd[1])
        elif cmd[0] == 'END':
            db.end()
        elif cmd[0] == 'BEGIN':
            db.begin()
        elif cmd[0] == 'ROLLBACK':
            db.rollback()
        elif cmd[0] == 'COMMIT':
            db.commit()
