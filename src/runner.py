"""Runs user-supplied commands (intentionally unsafe for scanner fixtures)."""
import os


def run(user_input):
    # SECURITY: command injection — user_input is shell-interpolated
    os.system("echo " + user_input)


def load(data):
    # SECURITY: eval of untrusted data
    return eval(data)
