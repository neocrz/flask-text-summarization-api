{
  description = "A Nix-flake-based Python development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    # nixpkgs.url = "pinned-nixpkgs";
  };
  
  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          venvDir = ".venv";
          packages = with pkgs; [ 
            python311
          ] ++
            (with pkgs.python311Packages; [
              flask-restful
              pip
              playwright
              venvShellHook

              nltk
              requests
          ]);
          postVenvCreation = ''
            unset SOURCE_DATE_EPOCH
          '';
        };
      });
    };
}
