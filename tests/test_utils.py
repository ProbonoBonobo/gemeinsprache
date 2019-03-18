#!/usr/local/bin/env python
import os
import sys
import pytest
import datetime
sys.path.append(os.path.abspath('../gemeinsprache'))
from gemeinsprache.utils import Pretty as pp, run_shell_command, gen_find

class TestFunc__run_shell_command:
    def test_it_runs_basic_bash_commands(self):
        cmd = "echo 'Hello!'"
        ok, output, exit_code, error_msg = run_shell_command(cmd)
        assert(ok)
        assert output == 'Hello!'
        assert exit_code == 0
        assert not error_msg

    def test_it_returns_nonzero_exit_code_if_unsuccessful(self):
       cmd = "sl"
       ok, output, exit_code, error_msg = run_shell_command(cmd)
       assert not ok
       assert exit_code
       assert error_msg

class TestClass__Pretty:
    def test_it_prints_serializable_objects(self):
        serializable_object = {
            "x": 3,
            "y": [1, 2, 3],
            "z": {
                "a": 0,
                "b": "hello",
                "c": ["world"]
            }
        }

        pretty = pp(serializable_object)
        assert pretty.ok
        assert pretty.prettified()
        assert pretty.output == pretty.prettified()
        assert pretty.print() is None
      
    def test_it_prints_unserializable_objects(self):
        unserializable_object = {
            "x": 3,
            "y": [1, 2, 3],
            "z": datetime.datetime.now()
        }
        pretty = pp(unserializable_object)
        assert pretty.ok
        assert pretty.prettified()
        assert pretty.prettified() == pretty.output
        assert pretty.print() is None

    def test_it_prints_lists(self):
        a_list = ['bananas',
                  'oranges',
                  'ferrets']
        pretty = pp(a_list)
        assert pretty.ok
        assert pretty.prettified()
        assert pretty.prettified() == pretty.output
        assert pretty.print() is None
    def test_it_prints_strings(self):
        a_string = "Bananas, oranges, and ferrets."
        pretty = pp(a_string)
        assert pretty.ok
        assert pretty.prettified()
        assert pretty.prettified() == pretty.output
        assert pretty.print() is None
    def test_it_fails_gracefully_with_null_objects(self):
        nothing = None
        pretty = pp(nothing)
        assert pretty.ok
        assert pretty.prettified()
        assert pretty.prettified() == pretty.output
        assert pretty.print() is None

class TestFunc__gen_find():
    def test_it_correctly_infers_the_users_path(self):
        out = gen_find(r'*')
        cwd = os.getcwd()
        assert(all([path.startswith(cwd) for path in out]))
        
