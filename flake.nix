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
      # py = pkgs.python312;
      py = pkgs.python311.withPackages (ps: [
        ps.python-lsp-server
        ps.black
      ]);
      hellopy = with pkgs;
        derivation {
          inherit system coreutils py;
          name = "hello";
          builder = "${bash}/bin/bash";
          src = ./hello.py;
          args = [./builder.sh];
        };
    in {
      packages.default = hellopy;
      devShells.default = pkgs.mkShell {
        name = "pyenv";
        buildInputs = [
          py
        ];
      };
    });
}
