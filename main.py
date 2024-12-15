import sys


def main():
    # Check if any arguements are passed
    if len(sys.argv) < 2:
        print("Error: No command provided. Use 'add', 'update', 'delete', 'list', etc.")
        return
    