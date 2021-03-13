from optparse import OptionParser
from pip_check_reqs import common


def options(files, requirements_file):
    """
    Build options for missing_req
    :param files: list of files to run on
    :param requirements_file: requirements file path
    :return: ops
    """
    p = OptionParser()
    p.add_option(
        "-f", "--ignore-file", dest="ignore_files",
        action="append", default=[], help=""
    )
    p.add_option(
        "-m", "--ignore-module", dest="ignore_mods",
        action="append", default=[], help=""
    )
    p.add_option("-r",
        "--ignore-requirement", dest="ignore_reqs",
        action="append", default=[], help=""
    )
    (opts, args) = p.parse_args()
    opts.requirements_filename = requirements_file
    opts.verbose = False
    opts.version = False
    opts.debug = False
    opts.paths = files
    opts.ignore_files = common.ignorer(opts.ignore_files)
    opts.ignore_mods = common.ignorer(opts.ignore_mods)
    opts.ignore_reqs = common.ignorer(opts.ignore_reqs)
    opts.skip_incompatible = False
    return opts
