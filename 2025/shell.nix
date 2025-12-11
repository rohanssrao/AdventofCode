{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShellNoCC {
  packages = [
    pkgs.python313
    pkgs.python313Packages.numpy
  ];
}
