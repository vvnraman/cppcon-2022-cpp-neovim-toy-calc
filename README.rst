##############
Toy Calculator
##############

Toy calculator in C++ to demonstrate Neovim features for my talk.


Build steps
***********

The task builds using ``cmake`` and ``Ninja``.

We're using `invoke`_ to avoid having to type the same things repeatedly on the
command line. It makes use of the ``tasks.py`` file in the root of our repo.

.. _invoke: https://www.pyinvoke.org/

.. code-block:: console

   $ inv --list
   Available tasks:

     build       Run builds via cmake.
     clean       Clean build directory.
     clean-all   Clean build and install directory.
     config      Run cmake configure.
     info        Show project info.
     install     Run install via cmake.


Build
=====

.. code-block:: sh

   # First time
   invoke config build
   # subsequently
   invoke build

Pre-requisites
==============

- ``gcc``

- ``cmake``

- ``ninja``

- ``invoke`` - Python and can be installed via ``pipx install invoke`` (`pipx`
  installs tools in an isolated virtual environment.)

One-time setup for vcpkg
========================

.. code-block:: console

   git submodule add https://github.com/microsoft/vcpkg.git
   git submodule update --init
   cd vcpkg
   ./bootstrap-vcpkg.sh -disableMetrics

