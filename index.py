import time
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout

def display_banner():
    console = Console()


    title = Text(
        """
 _______  _______ _________ _______           _______       
(  ___  )\__   __/(  ____ )(  ____ \( \      (  ___  )|\     /|
| (   ) |   ) (   | (    )|| (    \/| (      | (   ) || )   ( |
| (___) |   | |   | (____)|| (__    | |      | |   | || | _ | |
|  ___  |   | |   |     __)|  __)   | |      | |   | || |( )| |
| (   ) |   | |   | (\ (   | (      | |      | |   | || || || |
| )   ( |___) (___| ) \ \__| )      | (____/\| (___) || () () |
|/     \|\_______/|/   \__/|/       (_______/(_______)(_______)
        """,
        style="bold yellow",
        justify="center",
    )
    subtitle = Text("Generador de Beacons", style="bold green", justify="center")
    author = Text("by Sento Marcos Ibarra", style="bold yellow", justify="center")



            # Create the banner layout
    banner_panel = Panel(
        f"\n\n{title}\n{subtitle}\n{author}\n",
        border_style="cyan",
    )
    console.print(banner_panel)

# Main application logic
if __name__ == "__main__":
    try:
        display_banner()

        # Placeholder for the rest of the application logic
        import requests
        from MedicionesSender import get_all_sensors_of_user, generate_random_measurements

        def main():
            user_id = 1
            sensors = get_all_sensors_of_user(user_id)
            if sensors:
                print(f"User {user_id} has {len(sensors)} sensors. Starting to send measurements...")
                generate_random_measurements(sensors)
            else:
                print(f"User {user_id} has no sensors.")

        main()

    except KeyboardInterrupt:
        Console().print("\n[bold red]Animation interrupted by user.[/bold red]")
