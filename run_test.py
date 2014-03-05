from argparse import ArgumentParser

from subprocess import Popen

from test_object import Test



parser = ArgumentParser(description='Set the environment')
parser.add_argument('-p', '--production', action='store_true')
parser.add_argument('-s', '--staging', action='store_true')

def run(*args, **kwargs):
    p = Popen(args, **kwargs)
    p.wait()
    if p.returncode != 0:
        sys.exit(p.returncode)
    return p

if __name__ == '__main__':
    args = parser.parse_args()

    test = Test()

    if args.production:
        test.test_all_sites('production')
    if args.staging:
        test.test_all_sites('staging')
    if not args.staging and not args.production:
        test.test_all_sites('staging')

    test.quit()

