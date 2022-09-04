"""
This requires invoke to be installed on the machine (not venv), which can be
done via:
    pipx install invoke
"""
from hashlib import md5
from pathlib import Path
from shutil import rmtree as shutil_rmtree
from typing import Optional
from datetime import datetime

from invoke import task

PROJECT: str = "toy-calculator"
SRC_PATH: Path = Path(__file__).parent
VCPKG_TOOLCHAIN = SRC_PATH / "vcpkg/scripts/buildsystems/vcpkg.cmake"
WORKSPACE: Path = Path("/tmp/builds/cpp")
MD5: Optional[str] = None
BUILD_PATH: Optional[Path] = None
INSTALL_PATH: Optional[Path] = None


def get_md5(content: str) -> str:
    global MD5
    if MD5 is None:
        MD5 = md5(str.encode(content)).hexdigest()
    return MD5


def get_cmake_workspace() -> Path:
    hash = get_md5(str(SRC_PATH))
    return WORKSPACE / f"{PROJECT}_{SRC_PATH.name}_{hash}"


def get_build_path() -> Path:
    global BUILD_PATH
    if BUILD_PATH is None:
        BUILD_PATH = get_cmake_workspace() / "build"
    return BUILD_PATH


def get_install_path() -> Path:
    global INSTALL_PATH
    if INSTALL_PATH is None:
        INSTALL_PATH = get_cmake_workspace() / "install"
    return INSTALL_PATH


@task
def info(c, topic="all"):
    """Show project info."""
    if topic == "all":
        print(f"Project         = {PROJECT}")
        print(f"Source path     = {SRC_PATH}")
        print(f"Build path      = {get_build_path()}")
        print(f"Install path    = {get_install_path()}")
    elif topic == "build_path":
        print(get_build_path())
    elif topic == "install_path":
        print(get_install_path())
    else:
        print("Error: Valid 'topic' names are 'build_path'/'install_path'")


@task
def config(c):
    """Run cmake configure."""
    do_config(c)


def do_config(c):
    build_path = get_build_path()
    build_path.mkdir(parents=True, exist_ok=True)
    cmd = [
        "cmake",
        "-S",
        str(SRC_PATH),
        "-B",
        str(build_path),
        "-GNinja",
        "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=1",
        f"-DCMAKE_TOOLCHAIN_FILE={str(VCPKG_TOOLCHAIN)}",
    ]
    c.run(" ".join(cmd), pty=True)

    # Symlink compile_commands.json
    src_ccdb_file = SRC_PATH / "compile_commands.json"
    build_ccdb_file = build_path / "compile_commands.json"
    if build_ccdb_file.exists():
        if not src_ccdb_file.exists():
            src_ccdb_file.symlink_to(build_ccdb_file)


@task
def build(c, config=False):
    """Run builds via cmake."""
    build_path = get_build_path()

    if not build_path.exists():
        if config:
            do_config(c)
        else:
            print("Error: build path doesn't exist.")
            return

    cmd = ["cmake", "--build", str(build_path)]
    c.run(" ".join(cmd), pty=True)


@task
def install(c):
    """Run install via cmake."""
    build_path = get_build_path()
    install_path = get_install_path()

    if not build_path.exists():
        print("Error: build path doesn't exist.")
        return

    cmd = ["cmake", "--install", str(build_path)]
    c.run(" ".join(cmd), env={"DESTDIR": install_path}, pty=True)


@task
def clean(c):
    """Clean build directory."""
    # Don't clean during CppCon and the week before/after
    _, week, _ = datetime.now().isocalendar()
    if week in (36, 37, 38):
        print(f"I'm sorry I can't do that Dave as the current week is {week}.")
        return

    build_path = get_build_path()
    if build_path.exists():
        shutil_rmtree(build_path)
        print(f"Cleaned {build_path}")
    else:
        print("Build path absent. Nothing to do.")


@task(pre=[clean])
def clean_all(c):
    """Clean build and install directory."""
    install_path = get_install_path()
    if install_path.exists():
        shutil_rmtree(install_path)
        print(f"Cleaned {install_path}")
    else:
        print("Install path absent. Nothing to do.")
