from struct import pack
import subprocess
import sys
import os

def get_max_buffer_length(program_name):
    buffer_length = 1
    write_new_buffer(buffer_length)
    while program_runs_with_buffer(program_name, buffer_length):
        buffer_length = buffer_length*2
    return buffer_length


def binary_search_buffer_length(program_name, max_buffer_length):
    min_buffer_length = 0
    while True:
        buffer_length_guess = int(((max_buffer_length - min_buffer_length) / 2) + min_buffer_length)
        if buffer_length_found(program_name, buffer_length_guess):

            return buffer_length_guess + 4
        elif program_runs_with_buffer(program_name, buffer_length_guess):
            min_buffer_length = buffer_length_guess
        else:
            max_buffer_length = buffer_length_guess


def buffer_length_found(program_name, buffer_length):
    if (not program_runs_with_buffer(program_name, buffer_length)) and program_runs_with_buffer(program_name, buffer_length-1):
        return True
    else:
        return False


def program_runs_with_buffer(program_name, buffer_length):
    write_new_buffer(buffer_length)
    args = ("./" + program_name, "buffer")
    try:
        subprocess.check_call(args, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def write_new_buffer(buffer_length):
    outfile = open('buffer', "wb")
    p = bytes("A" * buffer_length, 'ascii')
    outfile.write(p)
    outfile.close()


def calculate_buffer_length(program_name):
    buffer_length = binary_search_buffer_length(program_name, get_max_buffer_length(program_name))
    os.remove("buffer")
    return buffer_length


if __name__ == "__main__":
    print(calculate_buffer_length("vuln3-32"))
