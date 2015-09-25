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

def get_total_download(owner, repo):
    res = 0
    gh = GitHub(access_token=TOKEN)
    releases = gh.repos(owner)(repo).releases.get()
    for r in releases:
        assets = r['assets']
        for a in assets:
            res += a['download_count']
    
    return res

if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] -u <github_user> -r <github_repo>")
    parser.add_option("-u", action="store", type="string", dest="github_user")
    parser.add_option("-r", action="store", type="string", dest="github_repo")
    (options, args) = parser.parse_args()
    if not options.github_user or not options.github_repo:
        help()
    print get_total_download(options.github_user, options.github_repo)

