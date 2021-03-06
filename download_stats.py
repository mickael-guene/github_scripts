import sys
import os.path
import subprocess
from optparse import OptionParser

from github import *
from uritemplate import expand

TOKEN=os.environ['GITHUB_TOKEN']

def help():
    parser.print_help()
    sys.exit(-1)

def get_stats(owner, repo):
    gh = GitHub(access_token=TOKEN)
    releases = gh.repos(owner)(repo).releases.get()
    for r in releases:
        assets = r['assets']
        print r['tag_name']
        for a in assets:
            print " - ", a['name'], " ", a['download_count']

if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] -u <github_user> -r <github_repo>")
    parser.add_option("-u", action="store", type="string", dest="github_user")
    parser.add_option("-r", action="store", type="string", dest="github_repo")
    (options, args) = parser.parse_args()
    if not options.github_user or not options.github_repo:
        help()
    get_stats(options.github_user, options.github_repo)

