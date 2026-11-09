"""Copy main's static site to the Pages root and dev's site to /dev/."""

from pathlib import Path
import shutil
import sys


def assemble(main_dist, dev_dist, output):
    # Check both trees before copying, so invalid dev content cannot publish a
    # production-only artefact. Pages artefacts must not contain symlinks.
    for source in (main_dist, dev_dist):
        if not (source / "index.html").is_file():
            raise ValueError(f"Missing regular index.html in {source}")
        if source.is_symlink() or any(path.is_symlink() for path in source.rglob("*")):
            raise ValueError(f"Symlinks are not supported in {source}")
    if (main_dist / "dev").exists():
        raise ValueError("The main site must reserve /dev/ for the dev branch")
    # copytree refuses an existing output, preventing stale deployment files.
    shutil.copytree(main_dist, output)
    shutil.copytree(dev_dist, output / "dev")


if __name__ == "__main__":
    assemble(*(Path(argument) for argument in sys.argv[1:]))
