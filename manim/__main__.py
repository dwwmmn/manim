from . import extract_scene
from . import config
from . import constants
from .addon import addon_loader


def main():
    addon_loader.read_addons(True)
    args = config.parse_cli()
    cfg = config.get_configuration(args)
    config.initialize_directories(cfg)
    addon_loader.pass_config_to_addons(cfg)
    extract_scene.main(cfg)


if __name__ == "__main__":
    main()
