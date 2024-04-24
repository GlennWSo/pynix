{
  inputs.nixpkgs.url = "github:NixOs/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  # inputs.flake-utils.inputs.nixpkgs.follows = "nixpkgs";

  outputs = {
    flake-utils,
    nixpkgs,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
      hellopy = with pkgs;
        derivation {
          inherit system coreutils;
          name = "hello";
          builder = "${bash}/bin/bash";
          py = python311;
          src = ./hello.py;
          args = [./builder.sh];
        };
    in {
      packages.default = hellopy;
    });
}
