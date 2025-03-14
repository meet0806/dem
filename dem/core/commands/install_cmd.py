"""install CLI command implementation."""
# dem/cli/command/install_cmd.py

from dem.core.dev_env import DevEnv
from dem.core.platform import Platform
from dem.core.exceptions import DevEnvError, PlatformError
from dem.cli.console import stderr, stdout

def execute(platform: Platform, dev_env_name: str) -> None:
    """
        Install the given Development Environment.
        
        Args:
            platform -- the platform
            dev_env_name -- the name of the Development Environment to install
    """

    platform.assign_tool_image_instances_to_all_dev_envs()

    dev_env_to_install: DevEnv | None = platform.get_dev_env_by_name(dev_env_name)

    if dev_env_to_install is None:
        stderr.print(f"[red]Error: The {dev_env_name} Development Environment does not exist.[/]")
    elif dev_env_to_install.is_installed == True:
        stderr.print(f"[red]Error: The {dev_env_name} Development Environment is already installed.[/]")
    else:
        try:
            dev_env_to_install.start_engines()
            platform.install_dev_env(dev_env_to_install)            
        except (PlatformError, DevEnvError) as e:
            stderr.print(f"[red]{e}[/]")
        else:
            stdout.print(f"[green]Successfully installed the {dev_env_name}![/]")